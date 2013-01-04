#!/usr/bin/env python

import os
import sys
from operator import itemgetter

class ORDER():
    def __init__(self, raw_path):
        path = os.path.abspath(raw_path)
        if not os.path.isdir(path):
            print '[ERORR]: DIR %s not exist' % path
            sys.exit(1)
        self._abs_path = path
        self._path_list = []
        self._dir_list = []
        self._files_list = []
        for (dirpath, dirname, filenames) in os.walk(self._abs_path):
            self._files_list.extend(filenames)
            break

    def size(self):
        size_list = {}
        os.chdir(self._abs_path)
        for file in self._files_list:
            size_list[file] = os.path.getsize(file)
        print 'Origin order: %s' % self._files_list
        print 'Sorted order: %s' % sorted(size_list, key=size_list.get, reverse=True)
        print 'Anothor way: %s' % sorted(size_list.items(), key=itemgetter(1))

if __name__ == '__main__':
    if len(sys.argv) is not 2:
        print '[Error]: Wrong number of arguments.'
        sys.exit(1)

    order = ORDER(sys.argv[1])
    order.size()



