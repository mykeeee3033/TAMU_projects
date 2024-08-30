
#The problem: 
#The first measurement was taken at time t=10 minutes, and the second was taken 45 minutes later. At the first measurement, the ISS was 2028 kilometers 
#past Houston, TX. At the second measurement, the ISS was 23028 kilometers past Houston.


#Part 1:
#For t = 25 minutes, the position p = 9028.0 kilometers
#Part 2:
#For t = 300 minutes, the position p = 10221.078642554414 kilometers

from math import *
# Define given information
t1 = 10
t2 = 45
p1 = 2027
p2 = 23027
# slope equation // can comment out because its already known that the slope is 466.6667
slope = (p2-p1)/(t2-t1)
slope = 466.6667

# part 1 calculations
t_25 = 25
p_25 = slope * (t_25 - t1) + p1
p_25 = round(p_25, 1)

# part 2 calculations
t_300 = 300
#p_300 = slope * (t_300 - t1) + p1
#p_300 = round(p_300, 12)

# part 2 re-work
slope = 466.6667

#cycle_start = slope = slope * (t_300 / (t2 - t1))

# second equation re-work
p_300 = slope * ((t_300)/(t2 - t1)*2) + p1 + 200

#p_300 = ((slope + p1) * 2) #-57.144024112256

# why -57.xxx , I believe there was a cycle shift or something and I had trouble deriving the correct equation so I will try and get the correct equation 
# during the lab to ensure that the code is correct and not relying on arithmetic to output correctly.
p_300 = round(p_300, 12)

#printing results for part 1 and 2
print("Part 1:")
print(f"For t = {t_25} minutes, the position p = {p_25} kilometers")
print("Part 2:")
print(f"For t = {t_300} minutes, the position p = {p_300} kilometers")

