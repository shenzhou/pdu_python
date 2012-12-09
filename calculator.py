#!/usr/bin/env python
'''
Description:
            Name: calculator.py
            Functionality: Extract data from example.file, do corresponding
                           calculation and return result.
            Usage: python calculator.py example.file

The example.file should has format as "function <value>" :

ADD 5
ADD 7
SUB 9
SQR

The limitation for the number of rows is 10.

Comments:
        This script will automatically correct common mistakes in example.file:
            1. Whitespaces in the end of the each row.
            2. More than one whitespace between function and value.
            3. Empty lines in the end of example.file and in between rows.
'''
import os
import sys
import math

class CALCULATOR():
    def __init__(self, raw_path):
        path = os.path.abspath(raw_path)
        if os.path.isfile(path):
            self._abs_path = path
        else:
            print 'Error: File: %s does not exist!' % path
            sys.exit(1)

    def run(self):
        result = 0
        data_list = self._data_collect(self._abs_path)
        for data in data_list:
            try:
                result = self._data_compute(result, data[0], data[-1])
            except Exception as e:
                print 'Error: %s' % e
                sys.exit(1)
        return result

    def _data_collect(self, path):
        """ Extract data from the given file and Reconstruct the data

            Input:  path(string):       Absolute path of the given file
            Output: data_list(list):    Nested list, contains functions and
                                        values
        """
        try:
            fo = open(path, 'r')
            raw_lines = fo.readlines()
        except Exception as e:
            print 'Error: %s' % e
            sys.exit(1)
        finally:
            fo.close()

        strip_lines = [item.strip() for item in raw_lines]
        data_list = []
        for line in strip_lines:
            # Check and remove empty lines
            if line:
                data_list.append(line.split(' '))

        if len(data_list) <= 10:
            return data_list
        else:
            print 'Error: %d rows required from the example file. Exceed '\
                  'limitation: 10 ' % len(data_list)
            sys.exit(1)

    def _data_compute(self, org_value, function, value):
        """ Do computation between the original value and the given value
            with the corresponding function

            Input: org_value(num):      Original value
                   function(string):    Given function for calculation
                   value(string):       Corresponding value with the given function

            Output: org_value(num):     Calculated base value
        """
        if(function == 'ADD'):
            org_value = org_value + float(value)
        elif(function == 'SUB'):
            org_value = org_value - float(value)
        elif(function == 'MUL'):
            org_value = org_value * float(value)
        elif(function == 'DIV'):
            org_value = org_value / float(value)
        elif(function == 'SQR'):
            org_value = math.pow(org_value, 2)
        else:
            print 'Error: function type: \'%s\' not supported!' % function
            sys.exit(1)
        return org_value

if __name__ == '__main__':
    if len(sys.argv) is not 2:
        print 'Error: Wrong number of arguments. Please use: ' \
              'Path of the example file as the only input.'
        sys.exit(1)

    path = sys.argv[1]
    calc = CALCULATOR(path)
    print calc.run()
