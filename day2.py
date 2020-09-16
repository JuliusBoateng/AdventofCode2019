#!/usr/bin/env python3
import sys

def intcode(list):
    offset = 4
    new_index = 0
    for index,value in enumerate(list):
        if index < new_index:
            continue

        if list[index] == 1:
            pos1 = list[index + 1]
            pos2 = list[index + 2]
            pos3 = list[index + 3]

            value1 = list[pos1]
            value2 = list[pos2]

            sum = value1 + value2

            list[pos3] = sum
            new_index = index + offset

        elif list[index] == 2:
            pos1 = list[index + 1]
            pos2 = list[index + 2]
            pos3 = list[index + 3]

            value1 = list[pos1]
            value2 = list[pos2]

            mult = value1 * value2

            list[pos3] = mult
            new_index = index + offset

        else:
            break

    return list[0]


def main():
    input = [int(x) for x in sys.stdin.readline().strip().split(",")]
    list = input.copy()
    noun = 0
    verb = 0
    value = 0

    for x in range(100):
        noun = x
        for y in range(100):
            verb = y
            list[1] = noun
            list[2] = verb
            value = intcode(list)
            if value == 19690720:
                # print(noun,verb,value)
                print(100*noun+verb)

            list = input.copy()



    # print(noun,verb,value)




if __name__ == "__main__":
  main()
