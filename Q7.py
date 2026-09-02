'''
#Q7
 Let (x,y) be a point in 2D space. Given a list of coordinates, write a sort
function that sorts them by proximity to a reference point given by the user
that is not in the list. Eg list 
[(0,1),(0,3),(1,2)] , reference 
(0,0) ,
output 
[(0,1),(1,2),(0,3)]'''

def sort_coords():
    x=float(input("Enter x-coordinate of reference : "))
    y=float(input("Enter y-coordinate of reference : "))

    L=eval(input("Enter list of coordinates to be sorted : "))
    L=sorted(L,key = lambda R: ((R[0]-x)**2+(R[1]-y)**2)**0.5)
    return L 
