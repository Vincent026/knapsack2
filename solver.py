#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
from copy import deepcopy
import copy

Item = namedtuple("Item", ['index', 'value', 'weight'])
CellValue = namedtuple("CellValue", ['OrgValue', 'PrevValue', 'PrevValueCol', 'Borrowed', 'MaxValueSameRow', 'ShiftedValue'])

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

    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data

def solve_it2(input_data):
    # prepare the solution in the specified output format
    output_data = str('abc') + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, ''))
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []
    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    for i in range(1, item_count+1):
        for j in range(1, item_count+1):
            print(items[i-1].weight, j)

    return output_data

def FillStatus01(col, items, row, statusX):
    waarde1 = 11
    for index in range(0,row):
        weight = items[index].weight
        value = items[index].value
        if col >= weight:
            if row > 0:
                value = statusX[row-1][col]
            waarde1 = value
        else:
            waarde1 = 13
    return waarde1

def FillStatus02(col, items, row, statusX):
    waarde2 = 22
    for index in range(0,row):
        weight = items[index].weight
        value = items[index].value
        if col >= weight:
            if row > 0:
                value = statusX[row-1][col]
                #waarde2Nieuw = status[row-1][col]
                #waarde2Nieuw = 444
            waarde2 = value
        else:
            waarde2 = 44
    return waarde2

def FillStatus03(colIndex, items, rowIndex, statusX):
    waarde3 = 0
    cell = CellValue(0, 0, 0, 0, 0, 0)
    start = rowIndex-1 if rowIndex > 0 else 0
    for index in range(start,rowIndex):
        waarde3 = index
        weight = items[index].weight
        value = items[index].value
        prevalue = 0
        shiftvalue = 0
        if colIndex >= weight:
            waarde3 = value
            if rowIndex > 0:
                prevalue = statusX[rowIndex-1][colIndex]
        else:
            waarde3 = 0
        cell = CellValue(value, 0, 0, 0, prevalue, shiftvalue)
    return waarde3, cell

def FillStatus04(colIndex, items, rowIndex, statusX):
    cell = CellValue(0, 0, 0, 0, 0, 0)
    start1 = rowIndex-1 if rowIndex > 0 else 0
    weight = 0
    itemValue = 0
    prevValue = 0
    prevValueCol = 0
    maxValue = 0
    shiftvalue = 0
    borrowed = 0
    if rowIndex > 0:
        itemValue = items[start1].value
        weight = items[start1].weight
        #prevValue = copy.copy(statusX[rowIndex-1][colIndex].OrgValue)
        if colIndex >= weight:
            start2 = rowIndex-1 if rowIndex > 0 else 0
            #prevValue = 55
        else:
            itemValue = 0
        # als het item niet past nemen we de waarde voor dezelfde capaciteit maar voor j-1 items
        if itemValue == 0:
            borrowed = prevValue
        prevValue = statusX[rowIndex-1][colIndex].OrgValue
        if colIndex > 0:
            prevValueCol = statusX[rowIndex-1][colIndex-1].OrgValue
        if prevValue > itemValue:
            maxValue = prevValue
        else:
            maxValue = itemValue
    cell = CellValue(itemValue, prevValue, prevValueCol, borrowed, maxValue, shiftvalue)
    return cell

def solve_it3(input_data):
    # prepare the solution in the specified output format
    output_data = str('abc') + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, ''))
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []
    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        print(parts)
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    # manier 1
    #m = item_count
    #n = item_count
    #a = [[items[i].weight for j in range(m)] for i in range(n)]
    #for rowIndex in a:
    #    print(' '.join([str(elem) for elem in rowIndex]))

    print('-------')

    # manier 2
    status1 = []
    status2 = []
    status3 = []
    XC = item_count+1
    YC = capacity
    for rowIndex in range(0,XC):
        status1.append([])
        status2.append([])
        status3.append([])
        # https://www.coursera.org/learn/discrete-optimization/lecture/wFFdN/knapsack-4-dynamic-programming
        # rijen en kolommen staan hier anders dan in videau.
        for colIndex in range(0,YC):  
            #waarde1 = FillStatus01(colIndex, items, rowIndex, status1)
            #status1[rowIndex].append(waarde1)

            #waarde2 = FillStatus02(colIndex, items, rowIndex, status2)
            #status2[rowIndex].append(waarde2)

            cell4 = FillStatus04(colIndex, items, rowIndex, status3)
            status3[rowIndex].append(cell4)

    # for row in range(0,XC):
    #     for col in range(0,YC):
    #         if row > 0:
    #             status[row][col] = status[row][col] + status[row-1][col]

    #print('........')
    #for row1 in status1:
    #    print(' '.join([str(elem) for elem in row1]))

    #print('........')
    #for row2 in status2:
    #    print(' '.join([str(elem) for elem in row2]))

    print('........ OrgValue')
    for row3 in status3:
        print(' '.join([str(elem.OrgValue) for elem in row3]))

    print('........ Borrowed')
    for row4 in status3:
        print(' '.join([str(elem.Borrowed) for elem in row4]))

    print('........ PrevValue')
    for row5 in status3:
        print(' '.join([str(elem.PrevValue) for elem in row5]))

    print('........ PrevValueCol')
    for row5 in status3:
        print(' '.join([str(elem.PrevValueCol) for elem in row5]))

    print('........ MaxValueSameRow')
    for row6 in status3:
        print(' '.join([str(elem.MaxValueSameRow) for elem in row6]))

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it3(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

