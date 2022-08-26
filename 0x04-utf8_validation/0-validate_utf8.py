#!/usr/bin/python3
"""
Write a method that determines if a given data set represents
a valid UTF-8 encoding.
Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need to
handle the 8 least significant bits of each integer
"""


def validUTF8(data):
    """
    Function to check the UTF-8 encoding of a data
    Args:
        data: list of integers
    Return: True if it satisfies the condition, False otherwise
    """
    index = 0
    length = len(data)
    def getbinary(x): return format(x, 'b').zfill(8)
    while index < length:
        num = getbinary(data[index])
        if num[0] == '0':
            index += 1
        elif num[0:3] == '110':
            if length - index > 1:
                temp = getbinary(data[index+1])
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
                    temp = getbinary(data[index])
                    if temp[0:2] != '10':
                        return False
                    index += 1
        elif num[0:5] == '11110':
            if length - index > 3:
                index += 1
                for i in range(3):
                    temp = getbinary(data[index])
                    if temp[0:2] != '10':
                        return False
                    index += 1
            else:
                return False
        else:
            return False
    return True
