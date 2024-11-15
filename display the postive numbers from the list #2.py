#program to display the postive numbers from the list
list1=[23,34,45,-45,67,-78,-89,89,78,-67,-34,-23]
print(list1)
print('The postive numbers from the list as fallows')
for i in range (0,len(list1)):
    if (list1[i]>=0):
        print(list1[i])
    
