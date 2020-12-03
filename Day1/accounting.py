def find_pair(file, sum):
    f = open(file, "r")
    vals = []
    for val in f:
        x = int(val)
        for y in vals:
            if x + y == sum:
                f.close()
                return x, y
        vals.append(x)
    f.close()
    return None, None


def find_trio(file, sum):
    f = open(file, "r")
    vals = []
    for val in f:
        x = int(val)
        for i in range(len(vals)):
            for j in range(i):
                if x + vals[i] + vals[j] == sum:
                    f.close()
                    return x, vals[i], vals[j]
        vals.append(x)
    f.close()
    return None, None, None


if __name__ == "__main__":
    sum = 2020
    input_file = "./input.txt"
    # input_file = "./test_data.txt"

    # Part 1
    x, y = find_pair(input_file, sum)
    if x and y:
        print(f"{x} and {y} multiply to give {x*y}"")
    else:
        print(f"No pair of values sums to {sum}")

    # Part 2
    x, y, z = find_trio(input_file, sum)
    if x and y and z:
        print(f"{x}, {y}, and {z} multiply to give {x*y*z}")
    else:
        print(f"No trio of values sums to {sum}")
