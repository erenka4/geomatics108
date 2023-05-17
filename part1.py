point_id_A = str(input("Enter the point ID of first known point : "))
y = float(input("Enter the Y coordinates of first known point (m): "))
x = float(input("Enter the X coordinates of first known point (m): "))
point_id_B = str(input("Enter the point ID of first known point : "))
ysecond = float(input("Enter the Y coordinates of second known point (m): "))
xsecond = float(input("Enter the X coordinates of second known point (m): "))
traverse_points = input("Enter the number of unknown traverse points : ")
point_id_1 = int(input("Enter the point ID of unknown point 1 : "))
point_id_2 = int(input("Enter the point ID of unknown point 2 : "))
point_id_3 = int(input("Enter the point ID of unknown point 3 : "))
traverse_angles_B = float(input("Enter the traverse angle of B (grad) : "))
traverse_angles_1 = float(input("Enter the traverse angle of 1 (grad) : "))
traverse_angles_2 = float(input("Enter the traverse angle of 2 (grad) : "))
horizontal_distance_B1 = float(
    input("Enter the horizontal distance between B and 1 (m): ")
)
horizontal_distance_12 = float(
    input("Enter the horizontal distance between 1 and 2 (m): ")
)
horizontal_distance_23 = float(
    input("Enter the horizontal distance between 2 and 3 (m): ")
)


# This code block written for calculate the azimuth between points A and B:
import math

deltaY = float(ysecond - y)
deltaX = float(xsecond - x)
delta = abs(((deltaY) / (deltaX)))
azimuth_A_B = math.atan(delta) * (180 / math.pi) * (10 / 9)

if deltaY > 0 and deltaX < 0:
    azimuth_A_B = 200 - azimuth_A_B
    print("azimuth_AB = ", format(azimuth_A_B, ".4f"))
else:
    print("azimuth_AB = ", format(azimuth_A_B, ".4f"))


# This code block written for calculate the azimuth between points B and 1:
azimuth_B_1 = azimuth_A_B + traverse_angles_B

if azimuth_B_1 < 200:
    print("azimuth_B1 = ", format(azimuth_B_1, ".4f"))
    new_azimuth_B_1 = azimuth_B_1
elif 200 < azimuth_B_1 and 600 > azimuth_B_1:
    print("azimuth_B1 = ", format(azimuth_B_1 - 200, ".4f"))
    new_azimuth_B_1 = azimuth_B_1 - 200
else:
    print("azimuth_B1 = ", format(azimuth_B_1 - 600, ".4f"))
    new_azimuth_B_1 = azimuth_B_1 - 600


# This code block written for calculate the azimuth between points 1 and 2:
azimuth_1_2 = azimuth_B_1 + traverse_angles_1
if azimuth_1_2 < 200:
    print("azimuth_12 = ", format(azimuth_1_2, ".4f"))
    new_azimuth_1_2 = azimuth_1_2
elif 200 < azimuth_1_2 and 600 > azimuth_1_2:
    print("azimuth_12 = ", format(azimuth_1_2 - 400, ".4f"))
    new_azimuth_1_2 = azimuth_1_2 - 400
else:
    print("azimuth_12 = ", format(azimuth_1_2 - 600, ".4f"))
    new_azimuth_1_2 = azimuth_1_2 - 600

# This code block written for calculate the azimuth between points 2 and 3:
azimuth_2_3 = azimuth_1_2 + traverse_angles_2

if azimuth_2_3 < 200:
    print("azimuth_23 = ", format(azimuth_2_3, ".4f"))
    new_azimuth_2_3 = azimuth_2_3
elif 200 < azimuth_2_3 and 600 > azimuth_2_3:
    print("azimuth_23 = ", format(azimuth_2_3 - 200, ".4f"))
    new_azimuth_2_3 = azimuth_2_3 - 200
else:
    print("azimuth_23 = ", format(azimuth_2_3 - 600, ".4f"))
    new_azimuth_2_3 = azimuth_2_3 - 600


# This code block written for after all azimuth angles are computed, ∆X and ∆Y between points can be calculated as
import math

Delta_X_B1 = horizontal_distance_B1 * math.cos(new_azimuth_B_1 * math.pi / 200)
print("Delta X B1 = ", format(Delta_X_B1, ".2f"))
Delta_Y_B1 = horizontal_distance_B1 * (math.sin(new_azimuth_B_1 * math.pi / 200))
print("Delta Y B1 = ", format(Delta_Y_B1, ".2f"))

Delta_X_12 = horizontal_distance_12 * (math.cos(new_azimuth_1_2 * math.pi / 200))
print("Delta X 12 = ", format(Delta_X_12, ".2f"))
Delta_Y_12 = horizontal_distance_12 * (math.sin(new_azimuth_1_2 * math.pi / 200))
print("Delta Y 12 = ", format(Delta_Y_12, ".2f"))

Delta_X_23 = horizontal_distance_23 * (math.cos(new_azimuth_2_3 * math.pi / 200))
print("Delta X 23 = ", format(Delta_X_23, ".2f"))
Delta_Y_23 = horizontal_distance_23 * (math.sin((new_azimuth_2_3 * math.pi / 200)))
print("Delta Y 23 = ", format(Delta_Y_23, ".2f"))

total_valueof_X = Delta_X_B1 + Delta_X_12 + Delta_X_23
print("Total value of  ∆ X = ", format(total_valueof_X, ".2f"))
total_valueof_Y = Delta_Y_B1 + Delta_Y_12 + Delta_Y_23
print("Total value of ∆ Y = ", format(total_valueof_Y, ".2f"))

# This code block written for calculate the coordinates

Y1 = ysecond + Delta_Y_B1
print("Y1 = ", format(Y1, ".2f"))
X1 = xsecond + Delta_X_B1
print("X1 = ", format(X1, ".2f"))

Y2 = Y1 + Delta_Y_12
print("Y2 = ", format(Y2, ".2f"))
X2 = X1 + Delta_X_12
print("X2 = ", format(X2, ".2f"))

Y3 = Y2 + Delta_Y_23
print("Y3 = ", format(Y3, ".2f"))
X3 = X2 + Delta_X_23
print("X3 = ", format(X3, ".2f"))


# Data table code block

print("-----------------------------------------")

print("Point ID Point ID Azimuth Delta Y Delta X")

print("-----------------------------------------")

print(point_id_A, point_id_B, (format(azimuth_A_B, ".4f")))
print(
    (point_id_B),
    (point_id_1),
    (format(azimuth_B_1, ".4f")),
    (format(Delta_Y_B1, ".2f")),
    (format(Delta_X_B1, ".2f")),
)
print(
    (point_id_1),
    (point_id_2),
    (format(azimuth_1_2, ".4f")),
    (format(Delta_Y_12, ".2f")),
    (format(Delta_X_12, ".2f")),
)

print(
    (point_id_2),
    (point_id_3),
    (format(azimuth_2_3, ".4f")),
    (format(Delta_Y_23, ".2f")),
    (format(Delta_X_23, ".2f")),
)

print("-----------------------------------------")

print("Point ID Coordinate (Y) Coordinate (X)")

print("--------------------------------------")

print(
    (point_id_1),
    (format(Y1, ".2f")),
    (format(X1, ".2f")),
)

print(
    (point_id_2),
    (format(Y2, ".2f")),
    (format(X2, ".2f")),
)
print(
    (point_id_3),
    (format(Y3, ".2f")),
    (format(X3, ".2f")),
)
