from enum import Enum


class System(Enum):
    """The password system associated against which the password will be validated."""

    OLD = 1
    NEW = 2


def is_valid_old_system(password, policy):
    """
    Each line gives the password policy and then the password. The password policy indicates
    the lowest and highest number of times a given letter must appear for the password to be
    valid. For example, 1-3 a means that the password must contain a at least 1 time and at
    most 3 times.
    """
    num_required = policy[0].split("-")
    lower_bound = int(num_required[0])
    upper_bound = int(num_required[1])
    letter = policy[1]

    # Validate the password
    count = password.count(letter)
    if (count >= lower_bound) and (count <= upper_bound):
        return True

    return False


def is_valid_new_system(password, policy):
    """
    Each policy describes two positions in the password, where 1 means the first
    character, 2 means the second character, and so on. (Be careful; Toboggan Corporate
    Policies have no concept of "index zero"!) Exactly one of these positions must
    contain the given letter. Other occurrences of the letter are irrelevant for the
    purposes of policy enforcement.

    """
    # Parse the policy.
    # password line example:
    #   1-3 a: abcde
    positions = policy[0].split("-")
    # Note, the whitespace was never stripped from the beginning of the password
    # so the index doesn't need to be shifted to account for one-based indexing
    pos1 = int(positions[0])
    pos2 = int(positions[1])
    letter = policy[1]

    # Extract relevant characters from password
    char1 = password[pos1]
    char2 = password[pos2]

    # Validate the password
    if (char1 == letter) ^ (char2 == letter):
        return True

    return False


def is_line_valid(password_line, system):
    # Choose validation strategy
    if system == System.OLD:
        is_password_valid = is_valid_old_system
    elif system == System.NEW:
        is_password_valid = is_valid_new_system

    # Parse the line
    policy = password_line[0].split()
    password = password_line[1]

    return is_password_valid(password, policy)


def count_valid(file, system):
    num_valid = 0
    f = open(file, "r")
    for line in f:
        password_line = line.rstrip("\n").split(":")
        if is_line_valid(password_line, system):
            num_valid += 1
    return num_valid


if __name__ == "__main__":
    input_file = "./passwords.txt"
    # input_file = "./test_passwords.txt"

    # Part 1
    num_valid = count_valid(input_file, System.OLD)
    print(f"{num_valid} passwords are valid according to the old policy.")

    # Part 2
    num_valid = count_valid(input_file, System.NEW)
    print(f"{num_valid} passwords are valid according to the new policy.")
