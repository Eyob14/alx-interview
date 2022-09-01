#!/usr/bin/python3
"""Module for printing a valid N Queen problem"""


import sys

args = sys.argv
length = len(args)
if length != 2:
    print("Usage: nqueens N")
    exit(1)
if args[1].isdigit():
    n = int(args[1])
else:
    print("N must be a number")
    exit(1)
if n < 4:
    print("N must be at least 4")
    exit(1)
cols = set()
posDiag = set()
negDiag = set()
board = [["."]*n for i in range(n)]
ans = []


def nqueens(r):
    """This function prints all valid values"""
    if r == n:
        final = []
        for x in range(n):
            for y in range(n):
                if board[x][y] == "Q":
                    final.append([x, y])
        ans.append(final)
        return
    for c in range(n):
        if c in cols or (r+c) in posDiag or (r-c) in negDiag:
            continue
        cols.add(c)
        posDiag.add(r+c)
        negDiag.add(r-c)
        board[r][c] = "Q"
        nqueens(r+1)
        cols.remove(c)
        posDiag.remove(r+c)
        negDiag.remove(r-c)
        board[r][c] = "."


nqueens(0)

for row in ans:
    print(row)
