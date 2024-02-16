# https://judge.beecrowd.com/en/problems/view/1023

# Due to the continuous drought that happened recently in some regions of Brazil,
# the Federal Government created an agency to assess the consumption of these
# regions in order to verify the behavior of the population at the time of rationing.
# This agency will take some cities (for sampling) and it will verify the consumption
# of each of the townspeople and the average consumption per inhabitant of each town.

# Input
# The input contains a number of test's cases. The first line of each case of test
# contains an integer N (1 ≤ N ≤ 1 * 10 6), indicating the amount of properties.
# The following N lines contains a pair of values X (1 ≤ X ≤ 10) and Y ( 1 ≤ Y ≤ 200)
# indicating the number of residents of each property and its total consumption (m3).
# Surely, no residence consumes more than 200 m3 per month. The input's end is represented by zero.

# Output
# For each case of test you must present the message “Cidade# n:”,
# where n is the number of the city in the sequence (1, 2, 3, ...),
# and then you must list in ascending order of consumption, the people's
# amount followed by a hyphen and the consumption of these people, rounding the value down.
# In the third line of output you should present the consumption per person in that town,
# with two decimal places without rounding, considering the total real consumption.
# Print a blank line between two consecutives test's cases. There is no blank line
# at the end of output.

def truncate_float(number, places):
    multiplier = 10 ** places
    return int(number*multiplier)/multiplier

def get_city_data(n):
    data = []    
    for _ in range(n):
        x, y = map(int, input().split())
        data.append((x,y))
    return data

def print_data(data, index):
    print(f'Cidade# {index}:')
    citizens = 0
    volume = 0
    volume_citizen_dict = {}
    for c,v in data:
        citizens += c
        volume += v
        try:
            volume_citizen_dict[v//c] += c
            continue
        except:
            volume_citizen_dict[v//c] = c
            continue
    for i, j in enumerate(sorted(list(volume_citizen_dict.keys()))):
        if i < len(volume_citizen_dict) -1 :
            print(f'{volume_citizen_dict[j]}-{j}', end=" ")
        else:
            print(f'{volume_citizen_dict[j]}-{j}', end="")

    print()
    print(f'Consumo medio: {truncate_float(volume/citizens, 2):.2f} m3.')


def main():
    n = int(input())
    cities_data = []
    while n > 0:
        data = cities_data.append(get_city_data(n))
        n = int(input())
    

    for index, city_data in enumerate(cities_data):
        print_data(city_data, index+1)
        if index < len(cities_data) - 1:
            print()


if __name__ == '__main__':
    main()