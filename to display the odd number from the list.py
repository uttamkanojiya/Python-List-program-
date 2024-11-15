#program to display the odd numbers from the list
L1=[23,24,25,26,28,29,256,245,234,898,900,888,236,457,123,1500,235,987,875,567,4549]
print(L1)
print("even numbers form the list as fallows")
for i in range (0,len(L1)):
    if ( L1[i]%2==1):
        print(L1[i])
