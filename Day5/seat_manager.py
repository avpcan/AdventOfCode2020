from math import floor, ceil


def traverse_partition(code, max_val):
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

    return traverse_partition(row_code, 127)


def decode_column(column_code):
    column_code = column_code.replace("L", "0")
    column_code = column_code.replace("R", "1")

    return traverse_partition(column_code, 7)


def get_seat_id(boarding_pass):
    row_code = boarding_pass[0:7]
    row_num = decode_row(row_code)

    column_code = boarding_pass[7:10]
    column_num = decode_column(column_code)

    return row_num * 8 + column_num


def get_all_seat_ids(boarding_passes_file):
    f = open(boarding_passes_file, "r")
    seat_ids = []
    for boarding_pass in f:
        seat_id = get_seat_id(boarding_pass)
        seat_ids.append(seat_id)
    return seat_ids


def find_missing_seat_id(seat_ids):
    lowest_id = seat_ids[0]

    lower_bound = seat_ids[0]  # 59
    upper_bound = seat_ids[-1]  # 904

    while True:
        lower_middle = floor((upper_bound - lower_bound) / 2 + lower_bound)
        upper_middle = ceil((upper_bound - lower_bound) / 2 + lower_bound)

        if seat_ids[lower_middle] + 2 == seat_ids[upper_middle]:
            # There's one seat missing in between! That's mine.
            return seat_ids[lower_middle] + 1
        if seat_ids[lower_middle] == lowest_id + lower_middle + 1:
            # Take lower half
            upper_bound = lower_middle
        elif seat_ids[upper_middle] == lowest_id + upper_middle:
            # Take upper half
            lower_bound = upper_middle
        else:
            raise RuntimeError(
                "Something went wrong while looking for the missing seat."
            )


if __name__ == "__main__":
    boarding_passes_file = "boarding-passes.txt"
    # boarding_passes_file = "test-boarding-passes.txt"

    # Part 1. Find the highest seat id
    try:
        seat_ids = get_all_seat_ids(boarding_passes_file)
    except ValueError:
        print("Internal Error.")
        raise SystemExit(0)
    except RuntimeError:
        print("Internal Error.")
        raise SystemExit(0)

    # Using sort() instead of max() because we need the sorted ids for part 2
    seat_ids.sort()
    highest_id = seat_ids[-1]
    print(f"The highest seat id is {highest_id}.")

    # Part 2. Find your seat id (it's the missing value!)
    my_seat_id = find_missing_seat_id(seat_ids)
    print(f"My seat id must be {my_seat_id}.")
