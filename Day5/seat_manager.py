from dataclasses import dataclass
from math import floor, ceil


@dataclass()
class BoardingPass:
    """Class for holding the information on a plane ticket."""

    row_num: int
    col_num: int
    seat_id: int


def apply_partitioning(code, max_val):
    # Example code = "1000110" max_val = 127
    lower_bound = 0
    upper_bound = max_val
    for val in code:
        middle = (upper_bound - lower_bound) / 2 + lower_bound
        if val == "0":
            # Take lower half
            upper_bound = floor(middle)
        elif val == "1":
            # Take upper half
            lower_bound = ceil(middle)
        else:
            raise ValueError("Invalid character in partitioning code.")
    if lower_bound != upper_bound:
        raise RuntimeError("Partition code didn't converge.")
    return lower_bound


def decode_row(row_code):
    row_code = row_code.replace("F", "0")
    row_code = row_code.replace("B", "1")

    return apply_partitioning(row_code, 127)


def decode_column(column_code):
    column_code = column_code.replace("L", "0")
    column_code = column_code.replace("R", "1")

    return apply_partitioning(column_code, 7)


def get_seat_id(row, column):
    return row * 8 + column


def parse_boarding_pass(boarding_pass):
    row_code = boarding_pass[0:7]
    row_num = decode_row(row_code)

    column_code = boarding_pass[7:10]
    column_num = decode_column(column_code)

    seat_id = get_seat_id(row_num, column_num)
    return seat_id
    # return BoardingPass(row_num, column_num, seat_id)


def parse_boarding_passes(boarding_passes_file):
    f = open(boarding_passes_file, "r")
    boarding_passes = []
    for boarding_pass in f:
        parsed_boarding_pass = parse_boarding_pass(boarding_pass)
        boarding_passes.append(parsed_boarding_pass)
    return boarding_passes


if __name__ == "__main__":
    boarding_passes_file = "boarding-passes.txt"
    # boarding_passes_file = "test-boarding-passes.txt"

    # Part 1. Find the highest seat id
    try:
        boarding_passes = parse_boarding_passes(boarding_passes_file)
        boarding_passes.sort()
        print(boarding_passes)
    except ValueError:
        print("Internal Error.")
        raise SystemExit(0)
    except RuntimeError:
        print("Internal Error.")
        raise SystemExit(0)
    highest_id = max(boarding_pass.seat_id for boarding_pass in boarding_passes)
    print(f"The highest seat id is {highest_id}.")

    # Part 2. Find your seat id (it's the missing value!)

    # TODO (TEMPORARILY):
    # reread and make sure I understood wtf is going on
    # rename parse_boarding_passes to get_seat_id
    # remove the class
    # collect the seat_ids instead
    # sort them.
    # print to see it
    # hmm, wonder if we could use some fancy tree structure thing to make searching faster?
    # brute force is increment id[i] and compare with id[i+1]
