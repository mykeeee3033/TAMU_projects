# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Micheal Tidwell
# Section:      102 536
# Assignment:   2.10 (e.g. Lab 1b-2)
# Date:         26/08/2024

#input type of stuff
#time_1 = float(input('Enter time 1: '))
#time_2 = float(input('Enter time 2: '))


def interpolate_position(t, t1, t2, P1, P2):
    
    x1, y1, z1 = P1
    x2, y2, z2 = P2
    
    # x = x1 + ((t - t1) / (t2 - t1)) * (x2 - x1) 
    # The problem was the incorrect equation for this you had it backwards! make sure to refer to the canvas video to correctly get the equation for linear inter..
    x = ((x2 - x1)/(t2 - t1)) * (t - t1) + x1
    y = ((t - t1) / (t2 - t1)) * (t - t1) + y1
    z = ((t - t1) / (t2 - t1)) * (t - t1) + z1
    
    return (x, y, z)

def main():
    #data
    t1 = float(input('Enter time 1: '))
    x1 = float(input('Enter x position of the object at time 1: '))
    y1 = float(input('Enter y position of the object at time 1: '))
    z1 = float(input('Enter z position of the object at time 1: '))
    P1 = (x1, y1, z1)  # Position at t1
    
    t2 = float(input('Enter time 2: '))
    x2 = float(input('Enter x position of the object at time 2: '))
    y2 = float(input('Enter y position of the object at time 2: '))
    z2 = float(input('Enter z position of the object at time 2: '))
    P2 = (x1, y1, y1)  # Position at t2

# What the issue was: god it was so simple, I had numerical values instead of the xyz cords....
 
    
    start_time = t1
    end_time = t2
    num_points = 5  # Number of points
    
    # Calculate evenly spaced time points
    time_points = [start_time + i * (end_time - start_time) / (num_points - 1) for i in range(num_points)]
    
    # Interpolate and print
    for i, t in enumerate(time_points):
        interpolated_position = interpolate_position(t, t1, t2, P1, P2)
        x, y, z = interpolated_position


        # Print the position
        print(f"At time {t:.2f} seconds the object is at ({x:.3f}, {y:.3f}, {z:.3f}) ")

if __name__ == "__main__":
    main()

