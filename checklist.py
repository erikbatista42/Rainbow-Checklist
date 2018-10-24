checklist = list()

def create(item):
    # Create item code here
    checklist.append(item)

def read(index):
    # Read code here
    return checklist[index]

def update(index, item):
    # Update code here
    checklist[index] = item

def destroy(index):
    # Destroy code here
    checklist.pop(index)

def list_all_items():
    # Code to list all items in list
    index = 0
    for list_item in checklist:
        print(str(index) + list_item)
        index += 1

def mark_completed(index):
    # Complete the function above. Hint: Add a character to the front of the checklist item that denotes an item as completed.
    # All we need to do is append some text to the front of the checked item in the list. Let's use the character √ to indicate whether an item is marked as completed or not.d
    pass

def select(function_code):
    # Create item
    if function_code == "C":
        input_item = input("Input item:")
        create(input_item)
    # Read item
    elif function_code == "R":
        item_index = user_input("Index number?")

        # Remember that item_index must actually exist our porgram will crash
        read(item_index)

    # Print all items
    elif function_code == "P":
        list_all_items()

    ## This is where we want to stop our loop
    elif function_code == "Q":
        return False

    # Catch all
    else:
        print("Unknown Option")
    return True

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input



def test():
    running = True
    while running:
        selection = user_input("Press C to add to list, R to Read from list and P to display list")
        select(selection)


test()



