import math

class Vectic:
 def __init__(A,x,y):
  A.x=x
  A.y=y
 def __add__(A,v):return Vectic(v.x+A.x,v.y+A.y)
 def __iadd__(A,v):
  A.x+=v.x
  A.y+=v.y
  return A
 def __sub__(A,v):return Vectic(A.x-v.x,A.y-v.y)
 def __isub__(A,v):
  A.x-=v.x
  A.y-=v.y
  return A
 def __mul__(A,s):return Vectic(A.x*s,A.y*s)
 def __imul__(A,s):
  A.x*=s
  A.y*=s
  return A
 def __repr__(A):return f"Vectic({A.x}, {A.y})"
 def __truediv__(A,s):
  if isinstance(s,Vectic):return Vectic(A.x/s.x,A.y/s.y)
  return Vectic(A.x/s,A.y/s)
 def __floordiv__(A,s):
  if isinstance(s,Vectic):return Vectic(A.x//s.x,A.y//s.y)
  return Vectic(A.x//s,A.y//s)
 def __floor__(A):return A//1
 def __len__(A):return A.norm()
 def __eq__(A,v):return A.x==v.x and A.y==v.y
 def dist(A,v):return math.sqrt(A.dist2(v))
 def dist2(A,v):return(A.x-v.x)**2+(A.y-v.y)**2
 def norm(A):return A.dist(Vectic.zero())
 def normalized(A):return A/A.norm()
 def rot(A,t):return Vectic(A.x*math.cos(t)-A.x*math.sin(t),A.y*math.sin(t)+A.y*math.cos(t))
 def copy(A):return Vectic(A.x,A.y)
 def zero():return Vectic(0,0)
 

class Moutic(Vectic):
 def __init__(A, keep_history=5, pause=10):
  super(Moutic, A).__init__(mouse()[0],mouse()[1])
  A.history = [A.copy() for _ in range(keep_history)]
  A.pause=pause
  A._waiting=pause
 def update(A):
  if A._waiting>=A.pause:
    A.add_to_history(A.copy())
    A._waiting=-1
  A._waiting+=1
  A.x=mouse()[0]
  A.y=mouse()[1]
 def add_to_history(A, v: "Vectic"):
  A.history.insert(0, v)
  return A.history.pop()
 def last_position(A):
  return A.history[-1]
 def speed(A):
  a = A.history[-1]
  b = A.history[-2]
  return a.dist(b)
 def avg_speed(A):
  h=A.history
  return sum([h[i].dist(h[i+1]) for i in range(len(h)-1)]) / len(h)