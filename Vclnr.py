# Vacuum Cleaner Agent

room = {
    "A": "Dirty",
    "B": "Dirty"
}

position = "A"

print("Initial State:")
print(room)
print("Vacuum is in Room", position)

while room["A"] == "Dirty" or room["B"] == "Dirty":

    # If current room is dirty, clean it
    if room[position] == "Dirty":
        print("Action: SUCK")
        room[position] = "Clean"

    # If current room is clean, move to the other room
    else:
        if position == "A":
            print("Action: MOVE RIGHT")
            position = "B"
        else:
            print("Action: MOVE LEFT")
            position = "A"

    print("Room Status:", room)
    print("Vacuum Position:", position)

print("\nGoal Reached!")
print("Both rooms are clean.")
