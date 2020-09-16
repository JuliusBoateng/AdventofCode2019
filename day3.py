#!/usr/bin/env python3
import sys
import collections

Position = collections.namedtuple('Position',['x','y'])

def grid_list(wire):
    position = Position(0,0)
    xrange_list = []
    yrange_list = []

    for change in wire:
        direction = change[0]
        value = int(change[1:])

        if direction == "R":
            new_position = Position(position.x + value, position.y)
            xrange_list.append([(position.x,new_position.x),position.y])

        if direction == "L":
            new_position = Position(position.x - value, position.y)
            xrange_list.append([(new_position.x,position.x),position.y])

        if direction == "U":
            new_position = Position(position.x, position.y + value)
            yrange_list.append([(position.x),(position.y,new_position.y)])

        if direction == "D":
            new_position = Position(position.x, position.y - value)
            yrange_list.append([(position.x),(new_position.y,position.y)])

        position = new_position

    return (xrange_list,yrange_list)

def main():
    wire1 = sys.stdin.readline().strip().split(",")
    wire2 = sys.stdin.readline().strip().split(",")

    xrange_list1,yrange_list1 = grid_list(wire1)
    xrange_list2,yrange_list2 = grid_list(wire2)

    print(xrange_list1)

    for position_wire1 in xrange_list1:
        y1 = position_wire1[1]
        x1_start = position_wire1[0][0]
        x1_end = position_wire1[0][1]

        for position_wire2 in xrange_list2:
            y2 = position_wire2[1]
            if y1 != y2:
                continue

            x2_start = position_wire2[0][0]
            x2_end = position_wire2[0][1]


    # for position_wire1 in yrange_list1:
    #     x1 = position_wire1[0]
    #     y1_start = position_wire1[1][0]
    #     y1_end = position_wire1[1][1]
    #
    #     for position_wire2 in yrange_list2:
    #         x2 = position_wire2[0]
    #         if x1 != x2:
    #             continue
    #
    #         y2_start = position_wire2[1][0]
    #         y2_end = position_wire2[1][1]
    #
    #
    # for position_wire1 in xrange_list1:
    #     x1 = position_wire1[0]
    #     y1_start = position_wire1[1][0]
    #     y1_end = position_wire1[1][1]
    #
    #
    #     for position_wire2 in yrange_list2:
    #         x2 = position_wire2[0]
    #         y2_start = position_wire2[1][0]
    #         y2_end = position_wire2[1][1]








    # for position_wire1 in position_list1:
    #     if isinstance(position_wire1[0], tuple):
    #         y1 = position_wire1[1]
    #         x1_list = []
    #         x1_list.append(position_wire1[0][0])
    #         x1_list.append(position_wire1[0][1])
    #         # x1_start = position_wire1[0][0]
    #         # x1_end = position_wire1[0][1]
    #
    #         print(x1_list)
    #
    #         for position_wire2 in position_list2:
    #             if isinstance(position_wire2[0], tuple):
    #                 y2 = position_wire2[1]
    #                 x2_start = position_wire2[0][0]
    #                 x2_end = position_wire2[0][1]
    #
    #
    #
    #             else:
    #                 x2 = position_wire2[0]
    #                 y2_start = position_wire2[1][0]
    #                 y2_end = position_wire2[1][1]
    #

        #
        # else:
        #     x = position[0]
        #     y_start = position[1][0]
        #     y_end = position[1][1]








if __name__ == "__main__":
    main()
