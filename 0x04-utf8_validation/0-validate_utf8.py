#!/usr/bin/python3
"""Module for validating UTF-8 encoding"""


def validUTF8(data):
    """Validates UTF-8 encoding"""
    index = 0
    length = len(data)
    def getBinary(x): return format(x, 'b').zfill(8)
    while index < length:
        num = getBinary(data[index])
        if num[0] == '0':
            index += 1
        elif num[0:3] == '110':
            if length - index > 1:
                temp = getBinary(data[index+1])
                if temp[0:2] != '10':
                    return False
                else:
                    index += 2
            else:
                return False
        elif num[0:4] == '1110':
            if length - index < 2:
                return False
            else:
                index += 1
                for i in range(2):
                    temp = getBinary(data[index])
                    if temp[0:2] != '10':
                        return False
                    index += 1
        elif num[0:5] == '11110':
            if length - index > 3:
                index += 1
                for i in range(3):
                    temp = getBinary(data[index])
                    if temp[0:2] != '10':
                        return False
                    index += 1
            else:
                return False
        else:
            return False
    return True
