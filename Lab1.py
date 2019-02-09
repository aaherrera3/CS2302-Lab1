#CS2302
#Made by Anthony Herrea
#Lab 1
#Olac Fuentes
#Anindita Nath
#2/8/19
#The purpose of this program is to understand recursion better

import numpy as np
import matplotlib.pyplot as plt
import math


def draw_squares(ax,n,p,w):                                                     #This is the basic draw square method provided to us in the lab
    if n>0:
        i1 = [1,2,3,0,1]
        q = p*w + p[i1]*(1-w)
        ax.plot(p[:,0],p[:,1],color='k')
        draw_squares(ax,n-1,q,w)

def draw_squares2(ax,p,n,li,r,loop):                                                #this method will create part one of the lab
    if n < len(p):                                                                  #It will create squerse of all the corners of the starting square and all the ones after that
        ax.plot(p[:, 0], p[:, 1], color='k')                                        #it takes a shape, a double array that contains all points, number of repetitions, a list, a modifire r, and the number of loops
        xx = p[n,0]                                                                 #what it does is that after ploting the first square it stores all corners x and y to be use as the next senter of the square.
        yy = p[n,1]
        q = np.array([[xx-r,yy-r],[xx+r,yy-r],[xx+r,yy+r],[xx-r,yy+r],[xx-r,yy-r]])
        if loop > 0:
            li.append(q)
        ax.plot(q[:, 0], q[:, 1], color='k')
        draw_squares2(ax,p,n+1,li,r,loop)
    if len(li)>0:
        x = li.pop(0)
        draw_squares2(ax, x,0, li, r*.25,loop-1)

def circle(center, rad):                    #this method creates all the points for a cirlce by using the center and the radius
    n = int(4 * rad * math.pi)
    t = np.linspace(0, 6.3, n)
    x = center[0] + rad * np.sin(t)
    y = center[1] + rad * np.cos(t)
    return x, y

def draw_circles2(ax, n, center, radius,w):         #This is a method that will creat part 3 of the lab
 if n > 0:                                          #it will create circles that run along the x axis
     x, y = circle([center[0]+radius,center[1]], radius)    #it takes a shape, number of repetitions, first center, first radius , and a modifire w
     ax.plot(x, y, color='k',linewidth=1)
     draw_circles2(ax, n - 1,center, radius*w,w)



def draw_circles(ax, n, center, radius, w):         #This is the basic method to draw a circle and change the radius
    if n > 0:
        x, y = circle(center, radius)
        ax.plot(x, y, color='k',linewidth=1)
        draw_circles(ax, n - 1, center, radius *w, w)

def draw(ax,n,center,radius,w):                 #This method will create part 4 of the lab
    if n > 0:                                   #it creates the centers for all the circles
        left = [center[0]-radius,center[1]]     #Then it calls the method draw_circles that will plot them.
        right = [center[0]+radius,center[1]]    # it takes a shape,number of repetition,the first origin, first radius, and a modifier w
        top = [center[0],center[1]+radius]
        bottom = top = [center[0],center[1]-radius]
        mid = top = [center[0],center[1]]
        draw_circles(ax,n-1,center,radius,w)
        draw_circles(ax, n-1, left, radius*w, w)
        draw_circles(ax, n-1, right, radius*w, w)
        draw_circles(ax, n-1, top, radius*w, w)
        draw_circles(ax, n-1, bottom, radius*w, w)
        draw_circles(ax, n-1, mid, radius*w, w)

#This shape will be part 1 A
list = []
plt.close("all")
orig_size = 1000
r = orig_size*.25
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
draw_squares2(ax,p,0,list,r,0)
ax.set_aspect(1.0)
# ax.axis('off')
plt.show()
fig.savefig('squares1.png')

#This shape will be part 1 B and C
list = []
plt.close("all")
orig_size = 1000
r = orig_size*.25
p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
draw_squares2(ax,p,0,list,r,3)
ax.set_aspect(1.0)
# ax.axis('off')
plt.show()
fig.savefig('squares2.png')

#this shape will be part 2 A
plt.close("all")
fig, ax = plt.subplots()
draw_circles2(ax, 7, [100, 0], 50, .5)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles1.png')

#this shape will be part 2 B
plt.close("all")
fig, ax = plt.subplots()
draw_circles2(ax, 100, [100, 0], 50, .9)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles2.png')

#this shape will be part 2 C
plt.close("all")
fig, ax = plt.subplots()
draw_circles2(ax, 100, [100, 0], 50, .95)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles3.png')

#This part will be part 4 A-C
plt.close("all")
fig, ax = plt.subplots()
draw(ax, 100, [100, 0], 50, 1/3)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles4.png')