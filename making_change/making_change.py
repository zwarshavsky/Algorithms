#!/usr/bin/python

import sys

def making_change(amount, denominations):
  amount = n
  if amount >= 4:
    return 1
  if n >= 5:
    return 2
  # if n >= 10:
  #   return 4
  # if n >= 15:
  #   return 5
  # if n >= 15:
  #   return 5 
  # if n >= 15:
  #   return 5
  # if n >= 15:
  #   return 5  
  # return amount


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")