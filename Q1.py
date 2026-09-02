'''
Task One : Python
Welcome to Driverless Taskphase. Solve all of the following using Python
(compulsory) and C++ (optional). All questions share one deadline, do not
wait till the last day.'''
#Task 1

#Q1 
'''Q1
Input an integer n, input n strings into a list. Create a dictionary where
the key is an alphabet and the value is how many times it appears across all
the strings. Not case sensitive. Eg for 
["Formula", "Manipal"] the output
looks like 
{'f':1, 'o':1, 'a':3 ...}
'''

n=int(input("Enter number of strings : "))
L=list()
for i in range(n):
    s1=input("Enter a string : ")
    L.append(s1)
d=dict()
for i in L:
    for j in i:
        if j.isalpha():
            if j.lower() not in d:
                d[j.lower()]=1
            else:
                d[j.lower()]+=1
print(d)