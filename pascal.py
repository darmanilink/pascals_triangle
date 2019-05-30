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
      if j==0:
        left = 0
      if j==(i-1):
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

#TODO: find the length of the longest number and compensate whitespasce everywhere else accordingly
def triangulate(list2d): #get it
  ldigit = 0
  for i in list2d:
    for r in i:
      tldigit = floor(log10(abs(r))) + 1
      if tldigit > ldigit:
        ldigit = tldigit
  formatted = ""
  length = len(list2d)-1
  for i in reversed(range(len(list2d))):
    index = length-i
    for j in range(i):
      for l in range(ldigit):
        formatted += ' '
    for k in list2d[index]:
      formatted += str(k)
      for l in range(ldigit):#-(floor(log10(abs(k))) + 1)):
        formatted += ' '
    formatted += '\n'  
  return formatted

r = triangulate(pascals_triangle(5))
print (r)

      
