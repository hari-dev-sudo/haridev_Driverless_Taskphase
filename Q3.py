#Q3
'''
Q3
Create a class with a function that does binary search in a list of strings.
Input a list like Q1, sort it using your Q2 function, input a string, search for it.
'''
class sorter:
    def __init__ (self,L):
        self.li=L

    def selection_sort(self):
        n=len(self.li)

        for i in range(n-1):
             
             small=i

             for j in range(i+1,n):
                 if self.li[j]<self.li[small]:
                     small=j
             self.li[i],self.li[small]=self.li[small],self.li[i]
        
        return self.li

class finder: 
    def __init__(self,L,ele):
        self.li=L #Sorted list to search in
        self.ele=ele #element to search for

    
    def binary_search(self):
        low=0
        high=len(self.li)-1
        while low<=high:
           mid=low+(high-low)//2
           if self.li[mid]==self.ele:
               return mid+1
           elif self.li[mid]>self.ele:
                high=mid-1
           elif self.li[mid]<self.ele:
               low=mid+1
        return -1
        
            

#main

L=eval(input("Enter a list of strings : "))
sorted_list=sorter(L)
L1=sorted_list.selection_sort()
print(L1)
ele=input("Enter an element to be found : ")

finding=finder(L1,ele)

ind=finding.binary_search()

if ind != -1:
    print("Element found at ",ind)
else:
    print("Element not found.")