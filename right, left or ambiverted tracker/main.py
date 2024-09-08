# Title: Handedness Categorization Program

# Lists to store names based on handedness
left = []         # List for left-handed people
right = []        # List for right-handed people
ambi = []         # List for ambidextrous people

while True:
    # Prompt the user to enter a name or type 'quit' to exit the loop
    name = input('Enter name or quit to exit: ')

    # Check if the user wants to exit the program
    if name.lower() == 'quit':
        break

    while True:
        # Prompt the user to enter the handedness of the person
        hand = input('Enter right-handed, left-handed or ambidextrous: ')

        # Validate the handedness input
        if hand.lower() in ['right-handed', 'left-handed', 'ambidextrous']:
            break
        else:
            # Inform the user of invalid input and prompt again
            print('Invalid, enter again:')

    # Categorize the person based on their handedness and add to the corresponding list
    if hand.lower() == 'left-handed':
        left.append(name)
    elif hand.lower() == 'right-handed':
        right.append(name)
    elif hand.lower() == 'ambidextrous':
        ambi.append(name)

# Print out the categorized lists of people
print('Left-handed people: ', left)
print('Right-handed people: ', right)
print('Ambidextrous people: ', ambi)
