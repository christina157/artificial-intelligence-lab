rooms = {
    "Left": "Dirty",
    "Right": "Dirty"
}

current_room = "Left"

while "Dirty" in rooms.values():
    print("Vacuum is in", current_room)

    if rooms[current_room] == "Dirty":
        print("Cleaning", current_room, "Room...")
        rooms[current_room] = "Clean"

    if current_room == "Left":
        current_room = "Right"
    else:
        current_room = "Left"

print("\nFinal State:")
print("Left Room:", rooms["Left"])
print("Right Room:", rooms["Right"])

print("\nBoth rooms are clean.")
