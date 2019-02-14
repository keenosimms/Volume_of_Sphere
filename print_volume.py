#volume of a sphere is 4/3πr3.
#In this section I define all variables
#that I will use to apply to my function:"

import math

radius_r1 = 5 # first radius 
float_f1 = 4.0/3.0

radius_r2 = 7 # second radius
float_f2 = 4.0/3.0

radius_r3 = 11 # third radius
float_f3 = 4.0/3.0

#In this section I define 3 functions
#using the variables that I assigned values to above
# I also imported the math library and used it to define pi
# Something I learned is that I can define one function,
# only and just adjust my variables above
# and receive the same results without defining two
# additional functions.

def sphere_vol(radius_r, float_f):
    volume = float_f * math.pi * radius_r **3
    print("With 5 as the radius, the volume of the sphere is: ") 
    print(volume)

def sphere_vol2(radius_r1, float_f2):
    volume = float_f2 * math.pi * radius_r2 **3
    print("With 7 as the radius, the volume of the sphere is: ") 
    print(volume)

def sphere_vol3(radius_r3, float_f3):
    volume = float_f3 * math.pi * radius_r3 **3
    print("With 11 as the radius, the volume of the sphere is: ") 
    print(volume)

result = sphere_vol(radius_r1, float_f1)
result = sphere_vol2(radius_r2, float_f2)
result = sphere_vol3(radius_r3, float_f3)


#used π as the value of "pi" given in Section 2.1 of the text
#wrote a function called print_volume that takes an argument for r
#the radius of the sphere, and prints the volume of the sphere
#called print_volume function with three different values for radius.

#by Keeno Simms - Thursday February 14th, 2019