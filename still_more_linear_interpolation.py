#By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Ram Verma
#               Carter Lain
#               Micheal Tidwell
# Section:      544
# Assignment:   3.18 (e.g. Lab 1b-2)
# Date:         05/09/2024


def interpolate_position(t, t1, t2, P1, P2):
    
    x1, y1, z1 = P1
    x2, y2, z2 = P2
    
    x = x1 + ((x2 - x1)/(t2 - t1)) * (x2 - x1)
    y = y1 + ((t - t1) / (t2 - t1)) * (y2 - y1)
    z = z1 + ((t - t1) / (t2 - t1)) * (z2 - z1)
    
    return (x, y, z)

def main():
    #data for times and inputs
    t1 = float(input('Enter time 1: '))
    x1 = float(input('Enter x position of the object at time 1: '))
    y1 = float(input('Enter y position of the object at time 1: '))
    z1 = float(input('Enter z position of the object at time 1: '))
    P1 = (x1, y1, z1)  # Position at t1
    
    t2 = float(input('Enter time 2: '))
    x2 = float(input('Enter x position of the object at time 2: '))
    y2 = float(input('Enter y position of the object at time 2: '))
    z2 = float(input('Enter z position of the object at time 2: '))
    P2 = (x2, y2, z2)  # Position at t2

    print('\n')
    num_points = 5  # Number of points

    
    # Calculate evenly spaced time points
    time_points = [t1 + i * (t2 - t1) / (num_points - 1) for i in range(num_points)]
    
    # Interpolate and print
    for t in time_points:
        interpolated_position = interpolate_position(t, t1, t2, P1, P2)
        x, y, z = interpolated_position

    # Interpolate and print the results
    for t in time_points:
        interpolated_position = interpolate_position(t, t1, t2, P1, P2)
        x, y, z = interpolated_position

        print(f"At time {t:.2f} seconds the object is at ({x:.3f}, {y:.3f}, {z:.3f})")

if __name__ == "__main__":
    main()

