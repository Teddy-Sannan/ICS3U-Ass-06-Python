#!/usr/bin/env python3

# Created by: Teddy Sannan
# Created on: November 2019
# This program takes user input
#  and calculates the volume of a pyramid


def volume_caclculation(base, height):
    # This function uses the input to calculate and print the answer
    # process
    volume = base ** 2 * height / 3
    # output
    print(str(base) + "^2 x " + str(height) + "/3 =", volume)


def main():
    # This function takes the input for the shape
    # helps ask again
    while True:
        # input
        baseEdge_as_string = input("Enter the base edge: ")
        height_as_string = input("Enter the height: ")
        print()

        try:
            # converst string to int
            baseEdge_as_int = int(baseEdge_as_string)
            height_as_int = int(height_as_string)

            # enters the volume_calculation function
            volume_caclculation(baseEdge_as_int, height_as_int)

        # prevents crashing from false input
        except ValueError:
            print("Invalid Input")
            print()
            continue

        # break out of loop
        else:
            break


if __name__ == "__main__":
    main()
