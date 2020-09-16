#!/usr/bin/env python3
import sys

width = 25
height = 6

color = {}

def main():
    input = sys.stdin.readline().strip()
    data_size = width*height
    min_zeros = len(input)
    min_layer = ""
    layers = []
    layer = [1]

    offset = 0
    data_read = data_size

    while len(input[offset:data_read]) > 0:
        layer = input[offset:data_read]
        layers.append(layer)
        if min_zeros > layer.count('0'):
            min_layer = layer
            min_zeros = layer.count('0')

        offset += data_size
        data_read += data_size



    print(min_layer.count('1') * min_layer.count('2'))

    for layer in layers:
        for index,char in enumerate(layer):
            if index in color:
                if color[index] == 'clear':
                    if char == '0':
                        color[index] = 'black'
                    if char == '1':
                        color[index] = 'white'
                    if char == '2':
                        color[index] = 'clear'
            else:
                if char == '0':
                    color[index] = 'black'
                if char == '1':
                    color[index] = 'white'
                if char == '2':
                    color[index] = 'clear'

    offset = 0
    output = []
    for x in range(height):
        temp = []
        for y in range(width):
            if color[y+offset] == 'black':
                temp.append(' ')
            else:
                temp.append('X')

        output.append(temp)
        offset += width

    for line in output:
        print(" ".join(line))

if __name__ == "__main__":
  main()
