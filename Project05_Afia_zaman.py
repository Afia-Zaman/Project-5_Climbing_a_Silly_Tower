"""A climber is climbing a tower of some height, measured in bricks. The tower is made up of 3
 types of bricks. For the 1st type, rock, nothing special happens when it is hit. The other 2 types
 of bricks are strategically placed and cause the climber to slide back down some number of
 bricks"""

# Take the variable for height of tower, current height, climbs and longest climb (for extension)
tower_height = 70
print("Tower Height = ", tower_height)
current_height = 0
climbs = 0
longest_climb = 0

# Create loop so that the climber can reach the top of tower
while current_height < tower_height:
    print("current height:", current_height)
    height = int(input("Enter the height you want to climb now (whole feet): "))
    if 1 <= height <= 15:
        current_height += height
        climbs += 1

# Take a height number where the silly brick is and push the user slide down
        if height == 6 or height == 9:
            back_down = 5
            current_height -= back_down
            print("You've hit a silly brick and slide down 5 feet!🥲 ")
            print()
        else:
            pass
# Calculate the longest climb user take for reaching the top
        if height > longest_climb:
            longest_climb = height
            print()
        else:
            print("🙁 Not a valid climb, try again: ")
            print()
    else:
        print("🙁 Not a valid climb, try again: ")
        print()


# print how many climbs it take to reach the top of the tower and the longest climb the user take
print(f"You used {climbs} mini climbs to climb the tower 🫡!")
print(f"The longest valid mini climb you made during your ascent was {longest_climb} feet.")
