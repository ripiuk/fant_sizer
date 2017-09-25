#!/usr/bin/python3.6

import os
import argparse


def get_sorted_file_size(the_path, number, max_first):
    result = {}
    for root, dirs, files in os.walk(the_path):
        for fn in files:
            path = os.path.join(root, fn)
            size = os.stat(path).st_size
            result[path] = size
    size_len = max(len(str(val)) for val in result.values())
    result = sorted(result.items(), key=lambda x: x[1], reverse=max_first)
    print(f'Path: {the_path}')
    print(f'Number of files: {len(result)}')
    print(f'{"b":^{size_len}} | {"mb":^7} | path')
    # for file_path, size in result:
    #     print(f'{size:{size_len}} | {size * 0.000001:7.1f} | {file_path}')
    for i in range(number):
        print(f'{result[i][1]:{size_len}} | {result[i][1] * 0.000001:7.1f} | {result[i][0]}')

if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='Find recursively files with max or min size')
    # parser.add_argument('path', type=str, help='path of parent dir', default='/home')
    # parser.add_argument('number', type=str, help='how much files will be shown', default=5)
    # parser.add_argument('max_first', type=str, help='max or min size first (1 or 0)', default=1)
    #
    # args = parser.parse_args()
    # print(args.accumulate(args.integers))
    path = '/home/sany/PycharmProjects'
    number = 5
    max_first = 1
    get_sorted_file_size(path, number, max_first)
