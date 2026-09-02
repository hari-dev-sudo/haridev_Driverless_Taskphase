#Q6   
'''Q6
 Improve Q5. Insert each new number so the sublist stays sorted. Do not
sort after insertion. Hint, find the insertion index using binary search.'''


def hasher(val):
    return val%10

def add_improved(n):
    index=hasher(n)
    low=0
    high=len(hash_table[index])-1

    while low<=high:
        mid=(low+(high-low))//2
        
        if hash_table[index][mid]>n:
                        high=mid-1
        elif hash_table[index][mid]<n:
                       low=mid+1
        else:
               break
    pos=low
    
    hash_table[index].insert(pos,n)

def creator():
    n=int(input("Enter how many integers : "))
    for i in range(n):
        x=int(input("Enter number : "))
        add_improved(x)
    print(hash_table)
#Q6   

hash_table=[[] for i in range(10)]
creator()
