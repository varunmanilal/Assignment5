import math
from Functions import *
#1st equations
def func(x):
    p = math.log(x,math.exp(1))-math.sin(x)
    return p

#All methods called from library
#bisection method
(x1,y1)= bisection(1.5,2.5,func)
print(x1,"is the root of Q1 from Bisection Method")
q1=open("Q1bisection.txt","w")
#Code for writing in notepad
Notepadwrt(q1,y1)

#Regula Falsi
(x1,y1)= regulafalsi(1.5,2.5,func)
print(x1,"is the root of Q1 from Regula Falsi")
q1=open("Q1regulafalsi.txt","w")
Notepadwrt(q1,y1)

#Newton Raphson
(x1,y1)= newtonraph(1.5,func)
print(x1,"is the root of Q1 by Newton Raphson Method")
q1=open("Q1newtonraph.txt","w")
Notepadwrt(q1,y1)

# 2nd Equation
def func2(x):
    p = -x-math.cos(x)
    return p

#Bisection method
(x1,y1)= bisection(-1,0.5,func2)
print(x1,"is the root of Q2 from Bisection Method")
q1=open("Q2bisection.txt","w")
Notepadwrt(q1,y1)

#Regula Falsi
(x1,y1)= regulafalsi(-1,-0.5,func2)
print(x1,"is the root of Q2 from Regula Falsi")
q1=open("Q2regulafalsi.txt","w")
Notepadwrt(q1,y1)

#Newton Raphson
(x1,y1)= newtonraph(-0.5,func2)
print(x1,"is the root of Q2 by Newton Raphson Method")
q1=open("Q2newtonraph.txt","w")
Notepadwrt(q1,y1)

#2.219106674194336 is the root of Q1 from Bisection Method
#2.2191071418525734 is the root of Q1 from Regula Falsi
#2.2191071489137406 is the root of Q1 by Newton Raphson Method
#-0.7390854358673096 is the root of Q2 from Bisection Method
#-0.7390851288908863 is the root of Q2 from Regula Falsi
#-0.7390851332151585 is the root of Q2 by Newton Raphson Method