#!/usr/bin/env python3
import fileinput
import sys, os
import argparse
import logging
import time

def replace_string(filename, string_to_search, string_to_replace):
	with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
	    for line in file:
	        print(line.replace(string_to_search, string_to_replace), end='')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Replace name",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--filename', type=str, dest='filename',
                        default='item', help='file location',
                        required=True)

    parser.add_argument('--search_string', type=str, dest='search_string',
                        default='item', help='string to search',
                        required=True)

    parser.add_argument('--replace_string', type=str, dest='replace_string',
                        default='item', help='string to replace',
                        required=True)

    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG)

    replace_string(args.filename, args.search_string, args.replace_string)
