# Add python code in this file
import csv 

tl_x=[]
br_x=[]
tl_y=[]
br_y=[]
cnames=[]

point_x=[]
point_y=[]
point_id=[]

def read_cities_file():
 i=0
 with open('cities.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
		if i > 0:
		 cnames.append(row[0]) 
		 tl_x.append(int(row[1]))
		 tl_y.append(int(row[2]))
		 br_x.append(int(row[3]))
		 br_y.append(int(row[4]))
		i = i + 1
		
def read_points_file():
 i=0
 with open('points.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
		if i > 0:
		 point_id.append(row[0])
		 point_x.append(int(row[1]))
		 point_y.append(int(row[2]))
		i = i + 1


def swap (a, b):
 temp = b 
 b = a
 a = temp
 
def prepare_list (l1,l2):
 j=0
 for x1 in l1:
  if (x1 > l2[j]):
   l1[j]=l2[j]
   l2[j]=x1
  j = j + 1
 
def locate():
 print("Enter a new point to locate it")
 px=input('x = ')
 py=input('y = ')
 located=0
 index=0
 max_index = len(cnames) - 1 
 while index <= max_index:
  if (((px >= tl_x[index]) & (px <= br_x[index])) & ((py >= tl_y[index]) & (py <= br_y[index]))):
   print ("point is located in "+cnames[index])
   located=1
   index = index + 1
   break
  index = index + 1
 if located == 0:
  print ("point is located in None")
  
 
def add_new_city():
 print("Add a new city to list of cities")
 name=raw_input('city name : ')
 cnames.append(name)
 tlx=input('top left x = ')
 tly=input('top left y = ')
 brx=input('bottom right x = ')
 bry=input('bottom right y = ')
 if tlx > brx :
  swap(tlx,brx) 
 if tly > bry :
  swap(tly,bry)  
 tl_x.append(tlx)
 tl_y.append(tly)
 br_x.append(brx)
 br_y.append(bry)
 with open('cities.csv', mode='a') as csv_file:
    fieldnames = ['Name','TopLeft_X','TopLeft_Y','BottomRight_X','BottomRight_Y']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writerow({'Name':name,'TopLeft_X':tlx,'TopLeft_Y':tly,'BottomRight_X':brx,'BottomRight_Y':bry})
 
#main test code for cities and points given
read_cities_file()
read_points_file()
prepare_list( tl_x , br_x )
prepare_list( tl_y , br_y )

index=0
max_index = len(cnames) - 1 
p_index=0
p_max_index = len(point_id) - 1
located=0
while p_index <= p_max_index:
 located = 0
 while index <= max_index:
  px=point_x[p_index]
  py=point_y[p_index]
  if (((px >= tl_x[index]) & (px <= br_x[index])) & ((py >= tl_y[index]) & (py <= br_y[index]))):
   print (point_id[p_index]+" is located in "+cnames[index])
   located=1
   index = index + 1
   break
  index = index + 1
 if located == 0:
  print (point_id[p_index]+" is located in None")	
 p_index = p_index +1

 
#main interact section
while True:
 print ("choose 1.locate point 2.add new city 3.exit")
 ch = input()
 if ch==3:
  break
 elif ch==1:
  locate()
 elif ch==2:
  add_new_city()
 
 
 
