#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Program that checks each line in a text file for properly nested brackets

"""
__author__ = "Rob Spears (GitHub: Forty9Unbeaten)"

import sys


def is_nested(line):
    bracketRef = {'(': ')', '{': '}', '[': ']', '<': '>', '(*': '*)'}
    openBrackets = bracketRef.keys()
    closingBrackets = bracketRef.values()
    balanceStack = []
    countStack = []
    count = 0

    while line:
        # token determination that accounts for two character tokens
        # and avoids out of bounds exceptions
        if len(line) > 1:
            token = line[0] + line[1]
            if token not in openBrackets and token not in closingBrackets:
                token = line[0]
        else:
            token = line[0]

        # check if token is open or closing bracket and perform
        # appropriate checks
        if token in openBrackets:
            balanceStack.append(token)
            countStack.append(count)
        elif token in closingBrackets:
            if len(balanceStack) and token == bracketRef[balanceStack[-1]]:
                balanceStack.pop()
                countStack.pop()
            else:
                return ("Unbalanced, there is a problem with the '" + token +
                        "' character at position " + str(count)
                        + " in the line.")

        # reduce line copy by the length of the token at the front of the copy
        line = line[len(token):]
        count += len(token)

    if len(balanceStack):
        return ("Unbalanced, there is a problem with the '" + balanceStack[0] +
                "' character at position " + str(countStack[0]) +
                " in the line.")
    else:
        return "Perfectly Balanced!"


def main(args):
    with open(args, 'r') as inFile:
        with open('output.txt', 'w') as outFile:
            for line in inFile.readlines():
                outFile.write(is_nested(line) + '\n')
                print(is_nested(line))


if __name__ == '__main__':
    main(sys.argv[1])
