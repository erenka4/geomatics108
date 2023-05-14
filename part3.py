stationary_traverse_ID = input("Enter the stationary traverse ID : ")   #P102
referenced_traverse_ID = input("Enter the referenced traverse ID : ")   #P101
Y_coordinates_P101 = float(input("Enter the Y coordinates of P101 (m) : "))    #3540.650
X_coordinates_P101 = float(input("Enter the x coordinates of P101 (m) : "))    #2360.420
height_P101 = float(input("Enter the height of P101 (m) : "))                  #110.600    
Y_coordinates_P102 = float(input("Enter the Y coordinates of P102 (m) : "))    #3740.650
X_coordinates_P102 = float(input("Enter the X coordinates of P102 (m) : "))    #2360.420
height_P102 = float(input("Enter the height of P102 (m) : "))                 #125.100
point_ID_detail_point = int(input("Enter the point ID of detail point : "))  #1
horizontal_direction_point1 = float(input("Enter the horizontal direction of point 1 (grad): "))
#111.0554
verticle_angle_point1 = float(input("Enter the verticle angle of point 1 (grad) : "))  #99.8568
slope_distance_P102_1 = float(input("Enter the slope distance between P102 and 1 (m) :"))  #82.576
height_instrument = float(input("Enter the height of instrument (m) :"))  #2.00
height_reflector = float(input("Enter the height of reflector (m) :"))        #1.50

import math

azimuth_P102_1 = math.atan(height_P101 / height_P102)
if azimuth_P102_1 < 200: 
    print("azimuth_P102,1 = ", azimuth_P102_1 + 200)
elif 200 < azimuth_P102_1 and 600 > azimuth_P102_1:
    print("azimuth_P102,1 = ", azimuth_P102_1 - 200 )
else:
    print("azimuth_P102,1 = ", azimuth_P102_1 - 600)

X1 = X_coordinates_P102 + slope_distance_P102_1 * math.cos(azimuth_P102_1)
print("X1 = ", X1)
Y1 = Y_coordinates_P102 + slope_distance_P102_1 * math.sin(azimuth_P102_1)
print("Y1 = ", Y1)

# Delta H
Delta_H = (slope_distance_P102_1 * math.cos(99.8568)) + (height_reflector - height_instrument)
print("∆H = ", Delta_H)
a = math.cos(99.8568)
print(a)
# H1
H1 = height_P102 + Delta_H
print("Elevation H1 = ", H1)
