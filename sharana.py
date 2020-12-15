list1=[12,18,3,13,5]
n=int(input('enter the maximum you want '))
for i in range(len(list1)-1):
  for j in range(i+1,len(list1)):
      if list1[i]>list1[j]:
        temp=list1[i]
        list1[i]=list1[j]
        list1[j]=temp
print(list1[len(list1)-n])
# To print nth minimum
#print(list1[n-1])
