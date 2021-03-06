from math import log10
from math import floor
def pascals_triangle(tiers):
  tiers += 1
  rows = list()
  for i in range(tiers):
    this_row = list()
    for j in range(i):
      left = -1
      right = -1
      if j == 0:
        left = 0
      if j == (i-1):
        right = 0
      if left is 0 and right is 0:
        this_row.append(1)
        continue
      if left is not 0:
        left = rows[i-1][j-1]
      if right is not 0:
        right = rows[i-1][j]
      this_row.append(left+right)  
    rows.append(this_row)   
  return rows

def triangulate(list2d): #get it
  ldigit = 0
  for i in list2d:
    for r in i:
      tldigit = floor(log10(abs(r))) + 1
      if tldigit > ldigit:
        ldigit = tldigit
  formatted = ""
  for index, i in enumerate(reversed(range(len(list2d)))):
    for j in range(i * ldigit):
        formatted += ' '
    for k in list2d[index]:
      formatted += str(k)
      kl = floor(log10(abs(k)))
      for l in range(ldigit - kl + (ldigit - 1)):
        formatted += ' '
    formatted += '\n'  
  return formatted

#changeme
while True:
  TIERS = input("\n\n>")
  if TIERS is "EXIT" or TIERS is "exit":
    exit()
  r = triangulate(pascals_triangle(int(TIERS)))
  print (r)
