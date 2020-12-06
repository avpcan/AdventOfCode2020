from pydantic import ValidationError
from validation_models import SneakyPassport, ExtraValidPassport


def is_valid_passport(passport_fields, validation_model):
    try:
        validation_model.parse_obj(passport_fields)
        return True
    except ValidationError:
        return False
    except ValueError:
        return False


def parse_fields(line, fields):
    for field in line:
        field = field.split(":")
        fields[field[0]] = field[1]
    return fields


def count_valid_passports(passports_file, validation_model):
    f = open(passports_file, "r")
    passport_fields = {}
    num_valid = 0
    for passport_line in f:
        if passport_line == "\n":
            num_valid += (
                1 if is_valid_passport(passport_fields, validation_model) else 0
            )
            passport_fields.clear()
        else:
            passport_line = passport_line.rstrip("\n").split()
            passport_fields = parse_fields(passport_line, passport_fields)

    num_valid += 1 if is_valid_passport(passport_fields, validation_model) else 0
    return num_valid


if __name__ == "__main__":
    passports_file = "passports.txt"
    # passports_file = "test-passports.txt"
    # passports_file = "test-passports-pt2.txt"

    # Day 1: No additional validation
    num_valid = count_valid_passports(passports_file, SneakyPassport)
    print(f"{num_valid} passports are valid.")

    # Day 2: Additional validation
    num_valid = count_valid_passports(passports_file, ExtraValidPassport)
    print(f"{num_valid} passports are VERY valid.")
