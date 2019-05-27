import pandas as pd
import numpy as np


def check(x,y,d):
	if((x == 0 and d == 'N') or (x==0 and d=='W') or (x==4 and d=='S') or (x==C and d=='E') ):
		s=0
		return s

def valid(s,a,i):
	if (s == 0):
		a[x, y] = 1
		print(a)
		print("The robot is at position", x, i)
	else:
		print("Robot cant be moved")


def inc(x,y,a,d):
	if(a[x,y]==1 and d =='S' ):
		x += 1
		x += 1

	if(a[x,y]==0 and d =='S'):
		x += 1

	if(a[x,y]==1 and d=='N'):
		x -= 1
		x -= 1

	if (a[x, y] == 0 and d == 'N'):
		x -= 1

	if(a[x,y]==1 and d=='E'):
		y += 1
		y += 1

	if (a[x, y] == 0 and d == 'E'):
		y += 1

	if(a[x,y]==1 and d=='W'):
		y -= 1
		y -= 1

	if (a[x, y] == 0 and d == 'W'):
		y -= 1


def ip(m,n,x,y,ins):
	a = np.zeros((m, n))
	a[x,y]=1
	print(a)
	for i in ins:
		inc(x,y,a,i)
		s=check(x,y,i)
		valid(s,a,i)


start_i,start_j=input("Enter starting values of robot i and j").split()
x=int(start_i)-1
y=int(start_j)-1
d = list(input("enter a direction"))
R,C=input("Enter no of rows and columns").split()
R=int(R)
C=int(C)
ip(R,C,x,y,d)
