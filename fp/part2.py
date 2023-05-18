import math


def calculate(known_point_elevation, unknown_point_ids, BS_list,FS_list ):

    delta_list = []
    elevation_list = []
    
    #calculate deltas
    for i , FS_reading in enumerate(FS_list):
        BS_reading = BS_list[i]
        delta = BS_reading - FS_reading
        delta_list.append(delta)

    for i,point_id in enumerate(unknown_point_ids):
        if i==0:
            elevation_list.append(known_point_elevation+delta_list[i])
        else:
            elevation_list.append(elevation_list[-1]+delta_list[i])

    
    return delta_list,elevation_list


def calculate_open_levelling_net():

    # known_point_id = ""
    # known_point_elevation = 108.00

    unknown_point_ids = []

    #A->2
    BS_list = []
    #B->3
    FS_list = []

    print("This program calculates the elevations in open levelling net\n")

    known_point_id = input("Enter the point ID of known point : ") 
    known_point_elevation = float(input("Enter the elevation of first known point  (m): "))
  

    # Input unknown traverse points
    num_unknown_points = int(input("Enter the number of unknown points: "))


    for i in range(num_unknown_points):
        point_id = input("Enter the point ID of unknown point {}: ".format(i + 1))
        unknown_point_ids.append(point_id)

    bs_reading = float(input("Enter the BS reading of point {} (m): ".format(known_point_id)))
    BS_list.append(bs_reading)

    for point_id in unknown_point_ids[:-1]:
        fs_reading = float(input("Enter the FS reading of point {} (m): ".format(point_id)))
        FS_list.append(fs_reading)
        bs_reading = float(input("Enter the BS reading of point {} (m): ".format(point_id)))
        BS_list.append(bs_reading)

    fs_reading = float(input("Enter the FS reading of point {} (m): ".format(unknown_point_ids[-1])))
    FS_list.append(fs_reading)

    # Calculate
    delta_list,elevation_list = calculate(   known_point_elevation,
        unknown_point_ids,  BS_list,FS_list )
    
        # Print the results
    print("\nPoint ID\tPoint ID\tDelta H\t")
    print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−---" )
    print("{}\t\t{}\t{:8.4f}".format(known_point_id, unknown_point_ids[0], delta_list[0]))

    for i in range(len(unknown_point_ids)-1):
        point_id = unknown_point_ids[i]
        next_point_id = unknown_point_ids[i+1]
        print("{}\t\t{}\t{:8.4f}".format( point_id, next_point_id, delta_list[i+1]))

    print("\nPoint ID\tElevation")
    print("−−−−−−−−−−−−−−−−−−−−−---")

    for i,point_id in enumerate(unknown_point_ids):
        elevation = elevation_list[i]
        print("{}\t{:10.4f}".format(point_id, elevation))



def test():
    known_point_id = "A"
    known_point_elevation = 108.00

    unknown_point_ids = ["B",1,2,3]

    #A->2
    BS_list = [2.650,2.325,2.516,2.877]
    FS_list = [0.650,1.623,1.437,0.915]
    

    delta_list,elevation_list = calculate(   known_point_elevation,
        unknown_point_ids,  BS_list,FS_list )
    
        # Print the results
    print("\nPoint ID\tPoint ID\tDelta H\t")
    print("−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−---" )
    print("{}\t\t{}\t{:8.4f}".format(known_point_id, unknown_point_ids[0], delta_list[0]))

    for i in range(len(unknown_point_ids)-1):
        point_id = unknown_point_ids[i]
        next_point_id = unknown_point_ids[i+1]
        print("{}\t\t{}\t{:8.4f}".format( point_id, next_point_id, delta_list[i+1]))

    print("\nPoint ID\tElevation")
    print("−−−−−−−−−−−−−−−−−−−−−---")

    for i,point_id in enumerate(unknown_point_ids):
        elevation = elevation_list[i]
        print("{}\t{:10.4f}".format(point_id, elevation))


# Run
calculate_open_levelling_net()
# test()