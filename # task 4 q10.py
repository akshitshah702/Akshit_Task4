# task 4 q10

  
lis1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
  
is_even = lambda x: x % 2 == 0
  
lis2 = list(filter(is_even, lis1))
  
print(lis2)