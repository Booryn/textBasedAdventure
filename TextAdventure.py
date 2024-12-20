#Aryn Parker
#10/13/24
#Move between rooms
#Setting up loops and dictionaries to allow a player to move between rooms

#Dictionary of rooms and their available directions
rooms = {
    'Living Room': {'West': 'Laundry Room'},
    'Laundry Room': {'East': 'Living Room', 'North': 'Mud Room', 'Item': ' the carrier'},
    'Mud Room': {'South': 'Laundry Room', 'Item': 'her harness'}
}

#The players current room
current_room = 'Living Room'

#Creating the initial loop for when the player does not use 'exit'
while current_room != 'exit':
    #Let them know which room they are in
    print("You've entered the", current_room)
    #Ask them the direction they'd like to take
    user_command = input('Which direction would you like to go? ').split()[-1].title()

    # If they choose to exit the game
    if user_command == 'Exit':
        print('THanks for playing!')
    # If user enters a valid command
    elif user_command in rooms[current_room]:
        current_room = rooms[current_room][user_command]
    elif user_command == 'Get item'
            if 'Item' in rooms[current_room]:
            return rooms[current_room]['Item']
    # If user enters invalid command
    else:
        print('Invalid move.')
# Invalid command
else:
    print('Invalid move.')
