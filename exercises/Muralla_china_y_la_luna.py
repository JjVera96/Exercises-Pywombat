import math

def main():
    distance_wall = 11
    diameter_moon = 3476
    towers = 67

    lng_moon = diameter_moon * math.pi
    walls = lng_moon / distance_wall
    towers_moon = walls * towers

    print('Las murallas necesarias son: {}'.format(int(round(walls,0))))
    print('Las torres de vigilancia necesarias son: {}'.format(int(round(towers_moon,0))))


if __name__ == '__main__':
    main()
