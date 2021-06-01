# task 4 q13
import operator
from functools import reduce
 
if __name__ == '__main__':
 
    lists = [[1, 2, 3], [4, 5], [6, 7, 8]]
    joinedlist = reduce(operator.add, lists)
 
    print(joinedlist)