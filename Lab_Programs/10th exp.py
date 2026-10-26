rooms = {'A': 1, 'B': 1}
location = 'A'

while 1 in rooms.values():
    if rooms[location] == 1:
        print("Room", location, "is Dirty. Cleaning...")
        rooms[location] = 0
    else:
        print("Room", location, "is Clean.")

    if location == 'A':
        location = 'B'
    else:
        location = 'A'

print("All rooms are clean!")
