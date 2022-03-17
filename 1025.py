def consecutive_number (l):
   c = 1
   while True:
      if c in l:
         c += 1
      else:
         return c-1

l=[7,1,6,34,23,2,3,4,5,8]
print(consecutive_number(l))
