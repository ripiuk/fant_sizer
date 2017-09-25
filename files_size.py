#!/usr/bin/python3.6

import os
import argparse


def get_sorted_file_size(the_path, number, min_first):
    result = {}
    for root, dirs, files in os.walk(the_path):
        for fn in files:
            path = os.path.join(root, fn)
            size = os.stat(path).st_size
            result[path] = size
    size_len = max(len(str(val)) for val in result.values())
    number_len = len(str(number))
    result = sorted(result.items(), key=lambda x: x[1], reverse=not min_first)
    # additional information
    print(f'Path: {the_path}')
    print(f'Number of files: {len(result)}')
    # header
    print(f'{"№":>{number_len}} | {"b":^{size_len}} | {"mb":^3} | path')
    # content
    for i in range(number):
        print(f'{i+1:{number_len}} | {result[i][1]:{size_len}} | {result[i][1] * 0.000001:2.1f} | {result[i][0]}')

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Finds recursively files in directory with max or min size')
    parser.add_argument('-p', dest='path', metavar='PATH', help='the path to parent dir', action='store',
                        default=os.getcwd())
    parser.add_argument('-n', type=int, dest='number', metavar='NUMBER', help='how much files will be shown',
                        action='store', default=5)
    parser.add_argument('-m', '--min', help='sorted by min size', action='store_true')

    args = parser.parse_args()
    get_sorted_file_size(the_path=args.path, number=args.number, min_first=args.min)
