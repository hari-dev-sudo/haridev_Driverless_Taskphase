#Q2
'''Q2
 Create a class with a function that does selection sort on a list of
strings. Input a list like Q1, call the function, print the output.
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