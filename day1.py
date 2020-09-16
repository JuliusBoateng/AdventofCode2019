#!/usr/bin/env python3
import sys
import math

def recursive(num,count=0):
    value = math.floor(num/3) - 2
    if value < 0:
        return 0

    count += recursive(value) + value

    return count


def main():
    value = 0
    list = [int(x) for x in sys.stdin.readlines()]
    for mass in list:
        fuel = math.floor(mass/3) - 2
        add_fuel = recursive(fuel)
        value += fuel + add_fuel

    print(value)

    # value = int(sys.stdin.readline())
    # print(recursive(value))




if __name__ == "__main__":
    main()
