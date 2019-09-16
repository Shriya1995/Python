#author shriya

def reverseList(newList):
  size = len(newList) 
  temp = newList[0] 
  newList[0] = newList[size - 1] 
  newList[size - 1] = temp 
  return newList 

n = int(input("Enter number of elements in list"))
li = []
for x in range(0,n):
  val = int(input("Enter element for list"))
  li.append(val)
print("List Before")
print(li)
print("List After")
print(reverseList(li))
