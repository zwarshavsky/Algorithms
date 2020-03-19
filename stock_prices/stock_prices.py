#!/usr/bin/python

import argparse

def find_max_profit(prices):

  min_price = prices[0]
  max_profit = prices[1] - min_price 
  

  for i in range(len(prices)):
    price = prices[i]
    max_profit = max(price - min_price, max_profit)
    min_price = min(price, min_price)
    print(max_profit, min_price)
  
  return max_profit



  # smallest = min(prices[:-1])
  # largest = max(prices[1:])
  # return abs(largest-smallest) 

  #   if prices[i] < prices[i+1]:
  #     smallest = prices[i]

  # largest = [prices[i] for i in range(1,len(prices) - 1)  if prices[i] > prices [i + 1]]
  # smallest = [prices[i] for i in range(len(prices) - 2)  if prices[i] < prices [i + 1]]
  # print(largest,smallest)


  # d = {}
  # for index,value in enumerate(prices):
    # d.update({index:value})

# [1050 270 1540 3800 2]

# [270 1540 3800 2]

# [270 3800]

  # largest = []
  # smallest = []
  # for i in range(len(prices)- 1):
  #   if prices[i] > prices[i+1]:
  #     largest.append(prices[i])
  #     smallest.append(prices[i+1])
  # print("largest:",largest)
  # print("smallest:",smallest)
  

      # print(val)

    # profit = [largest[i] - smallest[i]]
    # print(profit)
  



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))