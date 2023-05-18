import math


def calculate(   point_ids,
    coordinates,  unknown_point_ids,
    traverse_angles,
    horizontal_distances ):

    azimuth_list= []
    delta_list = []
    new_coordinates = []

    deltaY = float(coordinates[1][1] - coordinates[0][1] )
    deltaX = float(coordinates[1][0] - coordinates[0][0] )
    delta = abs(((deltaY) / (deltaX)))
# convert radian to degrees and to gradian
    azimuth_A_B = math.atan(delta) * (180 / math.pi) * (10 / 9) 
    
    if deltaY > 0 and deltaX < 0:
        azimuth_A_B = 200 - azimuth_A_B
    azimuth_list.append(azimuth_A_B)

    #calculate azimuth between B + all unknown points
    for angle in traverse_angles:
        new_azimuth = azimuth_list[-1] + angle
        if 200 < new_azimuth and 600 > new_azimuth:
            new_azimuth = new_azimuth - 200
        elif new_azimuth>600:
            new_azimuth = new_azimuth - 600
        azimuth_list.append(new_azimuth)
    # print(azimuth_list)
    

    for i,distance in enumerate(horizontal_distances):
        new_delta_x = distance * math.cos(azimuth_list[i+1] * math.pi / 200)
        new_delta_y = distance * (math.sin(azimuth_list[i+1] * math.pi / 200))
        delta_list.append( (new_delta_x,new_delta_y) )

    B_x = coordinates[1][0]
    B_y = coordinates[1][1] 
    new_coordinates.append( (B_x,B_y) )

    for delta in delta_list:
        x = new_coordinates[-1][0]
        y = new_coordinates[-1][1]
        new_coordinates.append( (x+delta[0],y+delta[1]) )

    new_coordinates.pop(0) # remove B coordinates
    
    return azimuth_list,delta_list,new_coordinates

# Function to calculate the coordinates in an open traverse series
def calculate_traverse():
    # Input known points
    point_ids = []
    coordinates = []

    print("This program calculates the coordinates in open traverse serie\n")

    point_id = input("Enter the point ID of first known point : ") 
    y = float(input("Enter the Y coordinates of first known point  (m): "))
    x = float(input("Enter the X coordinates of first known point  (m): "))
    point_ids.append(point_id)
    coordinates.append((x, y))

    point_id = input("Enter the point ID of second known point : " )
    y = float(input("Enter the Y coordinates of second known point  (m): " ))
    x = float(input("Enter the X coordinates of second known point  (m): " ))
    point_ids.append(point_id)
    coordinates.append((x, y))

    # Input unknown traverse points
    num_unknown_points = int(input("Enter the number of unknown traverse points: "))
    unknown_point_ids = []
    traverse_angles = []
    horizontal_distances = []

    for i in range(num_unknown_points):
        point_id = input("Enter the point ID of unknown point {}: ".format(i + 1))
        unknown_point_ids.append(point_id)

    for i,point_id in enumerate(unknown_point_ids):
        traverse_angle = float(input("Enter the traverse angle of {} (grad): ".format(point_id)))
        traverse_angles.append(traverse_angle)

    for i,point_id in enumerate(unknown_point_ids):
        if i == 0:
            distance_to_prev = float(input("Enter the horizontal distance between {} and {} (m): ".format(point_ids[-1], point_id)))
        else:
            distance_to_prev = float(input("Enter the horizontal distance between {} and {} (m): ".format(unknown_point_ids[i-1], point_id)))
        horizontal_distances.append(distance_to_prev)

    # Calculate azimuths and deltas
    azimuth_list,delta_list,new_coordinates = calculate(   point_ids,
    coordinates,  unknown_point_ids,
    traverse_angles,
    horizontal_distances )

            # Print the results
    print("\nPoint ID\tPoint ID\tAzimuth\tDelta Y\tDelta X")
    print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−" )
    print("{}\t\t{}\t{:8.4f}".format(point_ids[0], point_ids[1], azimuth_list[0]))

    for i,point_id in enumerate(unknown_point_ids):
        if i == 0:
            
            print("{}\t\t{}\t{:8.4f}\t{:8.2f}\t{:8.2f}".format(point_ids[-1], point_id, traverse_angles[i], delta_list[i][1], delta_list[i][0]))
        else:
            print("{}\t\t{}\t{:8.4f}\t{:8.2f}\t{:8.2f}".format(unknown_point_ids[i-1], point_id, traverse_angles[i], delta_list[i][1], delta_list[i][0]))

    print("\nPoint ID\tCoordinate (Y)\tCoordinate (X)")
    print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")

    for i,point_id in enumerate(unknown_point_ids):
        print("{}\t{:10.2f}\t{:10.2f}".format(point_id, new_coordinates[i][1], new_coordinates[i][0]))




def test():
    point_ids = ["A","B"]
    coordinates = []
    coordinates.append((9300.50,8450.00))
    coordinates.append((9125.75,8575.00))

    unknown_point_ids = [1,2,3]
    traverse_angles = [98.3570,255.6520, 207.8930]
    horizontal_distances = [175.58,168.75,184.94]
    azimuth_list,delta_list,new_coordinates = calculate(   point_ids,
        coordinates,  unknown_point_ids,
        traverse_angles,
        horizontal_distances )
    
        # Print the results
    print("\nPoint ID\tPoint ID\tAzimuth\tDelta Y\tDelta X")
    print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−" )
    print("{}\t\t{}\t{:8.4f}".format(point_ids[0], point_ids[1], azimuth_list[0]))

    for i,point_id in enumerate(unknown_point_ids):
        if i == 0:
            
            print("{}\t\t{}\t{:8.4f}\t{:8.2f}\t{:8.2f}".format(point_ids[-1], point_id, traverse_angles[i], delta_list[i][1], delta_list[i][0]))
        else:
            print("{}\t\t{}\t{:8.4f}\t{:8.2f}\t{:8.2f}".format(unknown_point_ids[i-1], point_id, traverse_angles[i], delta_list[i][1], delta_list[i][0]))

    print("\nPoint ID\tCoordinate (Y)\tCoordinate (X)")
    print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")

    for i,point_id in enumerate(unknown_point_ids):
        print("{}\t{:10.2f}\t{:10.2f}".format(point_id, new_coordinates[i][1], new_coordinates[i][0]))


# Run
calculate_traverse()
#test()