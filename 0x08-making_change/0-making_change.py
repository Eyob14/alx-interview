#!/usr/bin/python3
"""
This file contains a function that calculates make coin
change.
"""


from math import inf


def makeChange(coins, total):
    """ find the min coin change """
    storage = {}

    def helper(coins, rem):
        """ a helper function to find the min coin change"""
        nonlocal storage
        if rem in storage:
            return storage[rem]
        if rem < 0:
            return -1
        if rem == 0:
            return 0

        minimum = inf
        for i in coins:
            if rem-i < -2:
                continue
            res = helper(coins, rem-i)
            if (res >= 0 and res < minimum):
                minimum = 1 + res
        storage[rem] = minimum if minimum != inf else -1
        return storage[rem]

    if total < 1:
        return 0
    return helper(coins, total)
