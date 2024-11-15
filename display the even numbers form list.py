#program to display the even numbers from list
L1=[23,24,25,26,28,29,256,245,234]
print(L1)
print("even numbers form the list as fallows")
for i in range (0,len(L1)):
    if (L1[i]%2==0):
        print(L1[i])
