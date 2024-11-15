#program to display postive numbers form the list
l1=[]
n=(int)(input("enter how many numbers"))
for i in range (0,n):
    element=(int)(input())
    l1.append(element)
    print("postive numbers form list are as fallows")
    for i in range (0,len(l1)):
        if (l1[i]>0):
            print(l1[i])
