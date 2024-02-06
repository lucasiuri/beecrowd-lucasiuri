# https://www.beecrowd.com.br/judge/en/problems/view/1016



# Two cars (X and Y) leave in the same direction. The car X leaves with
# a constant speed of 60 km/h and the car Y leaves with a constant speed of 90 km / h.

# In one hour (60 minutes) the car Y can get a distance of 30 kilometers
# from the X car, in other words, it can get away one kilometer for each 2 minutes.

# Read the distance (in km) and calculate how long it takes (in minutes)
# for the car Y to take this distance in relation to the other car.

# Input
# The input file contains 1 integer value.

# Output
# Print the necessary time followed by the message "minutos" that means minutes in Portuguese.

SPEED_X = 60.0
SPEED_Y = 90.0

rate = abs(SPEED_Y-SPEED_X)/60.0    # kilometers per minute

dist = int(input())

time = dist/rate

print(f'{time:.0f} minutos')