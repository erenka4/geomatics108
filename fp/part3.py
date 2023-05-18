import math


def calculate_electrometric_tacheometry():

    # known_point_id = ""
    # known_point_elevation = 108.00

    unknown_point_ids = []

    #A->2
    BS_list = []
    #B->3
    FS_list = []

    print(" Program for Electrometric Tacheometry Computation\n")

    print("---------------------------------")

    st_traverse_id = input("Enter the stationary traverse ID : ")
    ref_traverse_id = input("Enter the referenced traverse ID : ")

    ref_y = float(input("Enter the Y coordinates of " + ref_traverse_id + " (m) : "))
    ref_x = float(input("Enter the X coordinates of " + ref_traverse_id + " (m) : "))
    ref_h = float(input("Enter the height of " + ref_traverse_id + " (m) : "))

    st_y = float(input("Enter the Y coordinates of " + st_traverse_id + " (m) : "))
    st_x = float(input("Enter the X coordinates of " + st_traverse_id + " (m) : "))
    st_h = float(input("Enter the height of " + st_traverse_id + " (m) : "))

    detail_point_id = input("Enter the point ID of detail point : ")

    detail_horizontal_direction = float(input("Enter the horizontal direction of point " + detail_point_id + " (grad) : "))
    detail_vertical_angle = float(input("Enter the vertical angle of point " + detail_point_id + " (grad) : "))

    slope_distance = float(input("Enter the slope distance between " + st_traverse_id + " and " + detail_point_id + " (m) : "))

    instrument_h = float(input("Enter the height of instrument (m) : "))
    reflector_h = float(input("Enter the height of reflector (m) : "))


    azimuth = math.atan(ref_h / st_h)


    if azimuth < 200:
        azimuth = azimuth
    elif 200 < azimuth and 600 > azimuth:
        azimuth = azimuth - 200
    else:
        azimuth = azimuth - 600



    # Delta H
    Delta_H = (slope_distance * math.cos(detail_vertical_angle * math.pi / 200)) + (reflector_h - instrument_h )

    # H1 Elevation
    H1 = st_h + Delta_H

    coord_x = (st_x) + ( slope_distance * math.cos(detail_horizontal_direction * math.pi / 200)  )
    coord_y = (st_y) + ( slope_distance * math.sin(detail_horizontal_direction * math.pi / 200)  )
    
        # Print the results
    print("\nPointID\tPointID\tHor. Dist.\tDelta H\tElevation\tCoord .(Y)\tCoord .(X))")
    print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−---−−−−−−−−---" )
    print("{}\t{}\t{:8.3f}\t{:8.3f}\t{:8.3f}\t{:8.3f}".format(ref_traverse_id, detail_point_id, slope_distance, Delta_H,  coord_y, coord_x))



def test():
    st_traverse_id = "P102"
    ref_traverse_id = "P101"

#P101
    ref_y =  3540.650
    ref_x = 2360.420
    ref_h = 110.600

#P102
    st_y = 3740.650
    st_x = 2360.420
    st_h = 125.100

    detail_point_id = 1

    detail_horizontal_direction = 111.0554
    detail_vertical_angle = 99.8568

    slope_distance = 82.576

    instrument_h = 2.00
    reflector_h = 1.50


    
    azimuth = math.atan(ref_h / st_h)


    if azimuth < 200:
        azimuth = azimuth
    elif 200 < azimuth and 600 > azimuth:
        azimuth = azimuth - 200
    else:
        azimuth = azimuth - 600



    # Delta H
    Delta_H = (slope_distance * math.cos(detail_vertical_angle * math.pi / 200)) + (reflector_h - instrument_h )

    # H1 Elevation
    H1 = st_h + Delta_H

    coord_x = (st_x) + ( slope_distance * math.cos(detail_horizontal_direction * math.pi / 200)  )
    coord_y = (st_y) + ( slope_distance * math.sin(detail_horizontal_direction * math.pi / 200)  )
    
        # Print the results
    print("\nPointID\tPointID\tHor. Dist.\tDelta H\tElevation\tCoord .(Y)\tCoord .(X))")
    print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−---−−−−−−−−---" )
    print("{}\t{}\t{:8.3f}\t{:8.3f}\t{:8.3f}\t{:8.3f}".format(ref_traverse_id, detail_point_id, slope_distance, Delta_H,  coord_y, coord_x))



# Run
calculate_electrometric_tacheometry()
# test()