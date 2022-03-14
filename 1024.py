def conf(bl):
   l = [ch for ch in bl]
   l = [n.replace('1','2') for n in l]
   l = [n.replace('0','1') for n in l]
   l = [n.replace('2','0') for n in l]
   return ''.join(l)


bl = '11110000111100001111000011110000'
print(conf(bl))
