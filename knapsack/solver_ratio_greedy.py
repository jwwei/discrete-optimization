#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0]*len(items)
    ratio = 0.0
    selectedindex = 0
    flag = True

    while weight <= capacity and flag == True:
        flag = False
        for item in items:
            if taken[item.index] == 0:
                flag = True
                if ratio == 0:
                    ratio = float(item.value) / float(item.weight)
                    selectedindex = item.index
                else:
                    if float(item.value) / float(item.weight) > ratio:
                        ratio = float(item.value) / float(item.weight)
                        selectedindex = item.index
        if flag == True:
            if weight + items[selectedindex].weight > capacity:
                taken[selectedindex] = -1
                ratio = 0.0
            else:
                value += items[selectedindex].value
                weight += items[selectedindex].weight
                taken[selectedindex] = 1
                ratio = 0.0

    for item in items:
        if taken[item.index] == 0 and weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight
    
    for index in range(len(items)):
        if taken[index] == -1:
            taken[index] = 0

    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

