#Q5
'''Q5
 Learn open hashing. Implement a hash table using 2D lists. Input n
integers. Every number where 
num % 10 == 0 goes in sublist 0, 
== 1 goes in sublist 1, and so on. Print the hash table.
num % 10'''

def hasher(val):
    return val%10

def add(n):
    index=hasher(n)
    hash_table[index].append(n)

def creator():
    n=int(input("Enter how many integers : "))
    for i in range(n):
        x=int(input("Enter number : "))
        add(x)
    print(hash_table)

hash_table=[[] for i in range(10)]
creator()