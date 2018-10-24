import sys

checklist = list()

def create(item):
    # Create item code here
    checklist.append(item)

def read(index):
    # Read code here
    pickedItem = checklist[int(index)]
    print(pickedItem)
    return pickedItem

def update(index, item):
    # Update code here
    checklist[int(index)] = item

def destroy(index):
    # Destroy code here
    checklist.pop(int(index))

def list_all_items():
    # Code to list all items in list
    index = 0
    for list_item in checklist:
        print(str(index) + " " + list_item)
        index += 1

def mark_completed(index):
    # Complete the function above. Hint: Add a character to the front of the checklist item that denotes an item as completed.
    # All we need to do is append some text to the front of the checked item in the list. Let's use the character √ to indicate whether an item is marked as completed or not.d
    item = checklist[index]
    item_list = list(item)
    item_list.insert(0, "√")
    new_word = "".join(item_list)
    update(index, new_word)

def select(function_code):
    # Create item
    if function_code == "C":
        input_item = input("Input item: ")
        create(input_item)
    # Read
    elif function_code == "R":
        item_index = user_input("Index number? ")
        # Remember that item_index must actually exist our porgram will crash
        try:
            read(item_index)
        except IndexError:
            print("ERROR! Index doesn't exist!")

    elif function_code == "U":
        update_item_index = user_input("Index number? ")
        update_item_info = user_input("Input item: ")
        update(update_item_index, update_item_info)

    elif function_code == "D":
        item_input = user_input("Index number? ")
        destroy(item_input)

    # Print all items
    elif function_code == "P":
        list_all_items()

    elif function_code == "M":
        item_index = user_input("Index number? ")
        mark_completed(int(item_index))

    ## This is where we want to stop our loop
    elif function_code == "Q":
        exit = sys.exit()
        return exit

    # Catch all
    else:
        print("Unknown Option")
    return True

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input.upper()

def test():
    running = True
    while running:
        selection = user_input("Press C to add to list, R to Read from list, U to Update an item from the list, D to delete something, P to display list and Press Q to Exit")

        select(selection)

test()



