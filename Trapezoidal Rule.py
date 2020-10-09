#Question 01 part 02
#Python implementation of Trapezoidal Rule
#To obtain the total profit of the beverage company over the nine-month period

def Trapezoidal(x,y):
   #to find the value of h
   h = (x[-1]-x[0])/(len(x)-1) 

   #to calculate the n-subinterval in Trapezoidal approximation
   Sum = y[0]
   for val in y[1:-1]:
      Sum = Sum +(2*val)
   Sum = Sum + y[-1]

   #to get the final answer  
   T = (h/2)*Sum
   print("The total profit of the company over 9 month period is",T*1000, "in dollars.")

#Driver code 
x = (1,2,3,4,5,6,7,8,9)
y = (3.1,4.4,6.4,6.6,5.9,5.6,5.1,4.9,4.6)
Trapezoidal(x,y)






