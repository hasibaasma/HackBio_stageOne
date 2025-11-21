#!/bin/bash/python3

def hamming_distance(str1, str2, ignore_spaces=False):
    # Remove spaces if the user chooses to ignore them
    if ignore_spaces:
        str1 = str1.replace(" ", "")
        str2 = str2.replace(" ", "")

    # Pad shorter string
    max_len = max(len(str1), len(str2))
    str1 = str1.ljust(max_len)
    str2 = str2.ljust(max_len)

    distance = 0
    for c1, c2 in zip(str1, str2):
        if c1 != c2:
            distance += 1
    return distance, str1, str2


def main():
    print("=== Hamming Distance Calculator ===")

    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")

    choice = input("Ignore spaces? (yes/no): ").strip().lower()
    ignore_spaces = (choice == "yes")

    distance, padded1, padded2 = hamming_distance(s1, s2, ignore_spaces)

    print("\nAfter processing:")
    print("String 1:", repr(padded1))
    print("String 2:", repr(padded2))
    print("Hamming Distance:", distance)


if __name__ == "__main__":
    main()

