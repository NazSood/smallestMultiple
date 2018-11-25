'''

array = [m for m in range(2, 11)]

for h in range(0, 9):
  print("Array values: {:d}" .format(array[h]))


for k in range(0, 9):
  for j in range(2, 11):
    if(array[k] % j == 0):
       array[k] = array[k] / j
  
    for g in range(0,9):
      print("array: ", array[g])
      print("-----------------")


'''
result   = 1
Multiple = 1
s = 2
k = 21
once = False
reIterate = True
array = [m for m in range(s, k)]

for h in range(0, 19):
  print("range", array[h])

 
while(reIterate):
  reIterate = False
  for i in range(s, k):
    once = True
    for l in range(0, 19):

      if((array[l] % i) == 0) and i != 4 and i != 9 and i != 6 and i != 10 and i != 8:
        array[l]  = array[l] / i
        if(once == True):
          Multiple *= i
          once = False   

        #print("End: {:d}" .format(i))

    for j in range(0, 19):
      #print("array[ {:1f} ]".format(array[j]))
      if(array[j] > 1):
        reIterate = True
        s = 2
        k = 21


print("Mulitplier: {:d}" .format(Multiple))





