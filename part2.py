idA = str(input("Enter the point ID of first known point : "))      
elevation_point_A = float(input("Enter the elevation of point A (m) :"))          
unknown_points = int(input("Enter the number of unknown points :"))     
unknown_point1 = str(input("Enter the point ID of unknown point 1 :"))  
unknown_point2 = int(input("Enter the point ID of unknown point 2 :"))  
unknown_point3 = int(input("Enter the point ID of unknown point 3 :"))  
unknown_point4 = int(input("Enter the point ID of unknown point 4 :"))  
BS_reading_point_A = float(input("Enter the BS reading of point A (m) :"))  
FS_reading_point_B = float(input("Enter the FS reading of point B (m) :"))  
BS_reading_point_B = float(input("Enter the BS reading of point B (m) :"))
FS_reading_point_1 = float(input("Enter the FS reading of point 1 (m) :"))
BS_reading_point_1 = float(input("Enter the BS reading of point 1 (m) :"))
FS_reading_point_2 = float(input("Enter the FS reading of point 2 (m) :"))
BS_reading_point_2 = float(input("Enter the BS reading of point 2 (m) :"))
FS_reading_point_3 = float(input("Enter the FS reading of point 3 (m) :"))

# This code block written for calculate Delta H 
Delta_H_AB = BS_reading_point_A - FS_reading_point_B
print("Delta H AB = ", Delta_H_AB)
Delta_H_B1 = BS_reading_point_B - FS_reading_point_1
print("Delta H B1 = ", Delta_H_B1)
Delta_H_12 = BS_reading_point_1 - FS_reading_point_2
print("Delta H 12 = ", Delta_H_12)
Delta_H_23 = BS_reading_point_2 - FS_reading_point_3
print("Delta H 23 = ", Delta_H_23)

# This code block written for caluclate elevation

H_B = elevation_point_A + Delta_H_AB
print("Hb = ", H_B)
H_1 = H_B + Delta_H_AB
print("H1 = ", H_B)
H_2 = H_1 + Delta_H_AB
print("H2 = ", H_2)
H_3 = H_2 + Delta_H_AB
print("H3 = ", H_3)