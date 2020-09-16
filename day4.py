#!/usr/bin/env python3
import sys
import collections

puzzle_start = 264793
puzzle_end = 803935

def num_pass():
    count = 0

    for value in range(puzzle_start, puzzle_end + 1):
        password = str(value)
        double = False
        decrease = False
        value_double = collections.defaultdict(int)


        for index in range(len(password) - 1):
            if password[index] == password[index+1]:
                value_double[password[index]] += 1

            if int(password[index]) > int(password[index+1]):
                decrease = True

        for num in value_double.values():
            if num == 1:
                double = True

        if (double == True) & (decrease == False):
            count += 1

    return count





def main():
    count = num_pass()
    print(count)



if __name__ == "__main__":
  main()
