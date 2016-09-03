import math
#import sys
#import time
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
def Cross(A,B):
    return A.x*B.y-A.y*B.x
def Rotate(p,rad):
    return Point(p.x*math.cos(rad)-p.y*math.sin(rad),p.x*math.sin(rad)+p.y*math.cos(rad))
def v_add(A,B):
    return Point((A.x+B.x),(A.y+B.y))
def v_inverse(A):
    return Point(-A.x,-A.y)
def ConvexHull(dot):
    ans=[Point(0,0) for _ in range(len(dot))]
    dot.sort(key=lambda A: A.x)
    dot.sort(key=lambda A: A.y)
    m=0
    for i in range(len(dot)):
        while m>1 and Cross(v_add(ans[m-1],v_inverse(ans[m-2])),v_add(dot[i],v_inverse(ans[m-2])))<=0:
            m-=1
        ans[m]=dot[i]
        m+=1
    k=m
    for i in range(len(dot)-2,-1,-1):
        while m>k and Cross(v_add(ans[m-1],v_inverse(ans[m-2])),v_add(dot[i],v_inverse(ans[m-2])))<=0:
            m-=1
        ans[m]=dot[i]
        m+=1
    if(len(dot)>1): m-=1
    return ans,m

def PolygonArea(p,n):
    area=0.0
    for i in range(1,n-1):
        area+=Cross(v_add(p[i],v_inverse(p[0])),v_add(p[i+1],v_inverse(p[0])))
    return area/2
time.sleep(0.05)
N=int(input().strip('\n'))
time.sleep(0.05)
for _ in range(N):
    n=int(input().strip('\n'))
    table=[]#table:xy
    dot=[]
    table_area=0.0
    time.sleep(0.05)
    for i in range(n):
        line=input().split()
        O=Point(float(line[0]),float(line[1]))
        table.append(O)
        ang=-math.radians(float(line[4]))
        w=float(line[2])
        h=float(line[3])
        dot.append(v_add(O,Rotate(Point(-w/2,-h/2),ang)))
        dot.append(v_add(O,Rotate(Point(w/2,-h/2),ang)))
        dot.append(v_add(O,Rotate(Point(-w/2,h/2),ang)))
        dot.append(v_add(O,Rotate(Point(w/2,h/2),ang)))
        table_area+=w*h
    '''
    print(table_area)

    print(PolygonArea(ConvexHull(dot)))
    '''
    p,m=ConvexHull(dot)
    #for d in p:
        #print(d.x,' ',d.y)
    print("%.1f %%"%(table_area*100/PolygonArea(p,m)))
    #print("%.1f %%"%2.78787878)
