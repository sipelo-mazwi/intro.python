from math import pi
print (pi)
radius = float(input ("Enter the radius of the circle : "))
print ("The area of the circle with radius " + str(radius) + " is: " + str(pi * radius**2))

diameter = radius * 2
print (f"The diameter of the circle is: {diameter}")


circumference = 2 * pi * radius **2
print (f"The cirumference of the circle is: {circumference}")