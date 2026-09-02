
import csv

'''
Q8
 Consider a CSV (
cones.csv ) with cone id, x, y, colour (blue or yellow)
per row. Sort the rows by distance from the origin. Write two new CSVs, one
per colour, keeping the sorted order. Then find the midpoint between every
blue cone and its nearest yellow cone and write those midpoints to
centreline.csv .
Q8 is a stripped down version of what path planning actually does on the
car. Understand it, do not just match the output.'''




#Q8 Part 1
with open('cones.csv','r',newline='') as f1:
    reader=csv.reader(f1)
    header=next(reader)
    data=[]

    for row in reader:
        data.append(row)


blue=tuple()
for i in data:
    if i[3].lower() =='blue':
        blue=blue+(tuple(i),)
blue=tuple(sorted(blue,key = lambda R: ((float(R[1]))**2+float((R[2]))**2)**0.5))

yellow=tuple()
for i in data:
    if i[3].lower() =='yellow':
        yellow=yellow+(tuple(i),)
yellow=tuple(sorted(yellow,key = lambda R: ((float(R[1]))**2+float((R[2]))**2)**0.5))

with open('blue.csv','w',newline='\r\n') as f2:
    writer=csv.writer(f2)
    writer.writerows(blue)

with open('yellow.csv','w',newline='\r\n') as f3:
    writer=csv.writer(f3)
    writer.writerows(yellow)

d1=dict()
for b in blue:
    if not yellow:
        break
    nearest_y = yellow[0]
    min_d = (float(b[1]) - float(nearest_y[1]))**2 + (float(b[2]) - float(nearest_y[2]))**2
    
    for y in yellow[1:]:
        distance = (float(b[1]) - float(y[1]))**2 + (float(b[2]) - float(y[2]))**2
        if distance < min_d:
            min_d = distance
            nearest_y = y
            
    d1[b] = nearest_y

def midpoint(x1,x2,y1,y2):
    x=(x1+x2)/2
    y=(y1+y2)/2
    return (x,y)

with open('centreline.csv','w',newline='\r\n') as f1:
    writer=csv.writer(f1)
    for i in d1:
        point=midpoint(float(i[1]),float(d1[i][1]),float(i[2]),float(d1[i][2]))
        writer.writerow(point)
