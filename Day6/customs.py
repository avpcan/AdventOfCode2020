def count_yes_responses(input_file, joining_policy):
    """Finds the sum of the count of the questions that people in each group said yes to

    Args:
        input_file (str): Name of the file containing the input
        joining_policy (Callable): a set operation.
            set.union determines the count for which ANYONE answered "yes".
            set.intersection determines the count for which EVERYONE answered "yes".

    Returns:
        int: The sum of the count of the questions that people in each group said yes to
    """
    f = open(input_file, "r")
    group_answers = set()
    running_total = 0
    is_first_member = True

    for line in f:
        if line == "\n":
            running_total += len(group_answers)
            group_answers.clear()
            is_first_member = True
            continue

        line = line.rstrip("\n")
        if is_first_member:
            # Ensure that we are always joining with a populated set
            group_answers = set(line)
            is_first_member = False
        else:
            group_answers = joining_policy(group_answers, set(line))

    # Account for the last line
    running_total += len(group_answers)
    return running_total


if __name__ == "__main__":
    input_file = "input.txt"
    # input_file = "test-input.txt"

    # Part 1.
    # For each group, count the number of questions to which ANYONE answered "yes".
    # Find the sum of those counts.
    some_yes = count_yes_responses(input_file, set.union)
    print(
        f"{some_yes}: sum of the counts of questions to which ANYONE in a group "
        "answered 'yes'."
    )

    # Part 2.
    # For each group, count the number of questions to which EVERYONE answered "yes".
    # Find the sum of those counts.
    all_yes = count_yes_responses(input_file, set.intersection)
    print(
        f"{all_yes}: sum of the counts of questions to which EVERYONE in a group "
        "answered 'yes'."
    )
