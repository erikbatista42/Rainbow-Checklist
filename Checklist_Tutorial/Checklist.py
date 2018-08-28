# CRUD - Create, Read, Update, Destroy
checklist = list()

 # a function that adds something to our checklist
def create(item): # create item code here
    checklist.append(item)
# print(checklist)

def read(index): # read item code here
    # item = checklist[index]
    print(checklist[index])
    return checklist[index]

def update(index, item): # update item code here
    checklist[index] = item

def destroy(index): # destory item code here
    checklist.pop()

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    # checklist.insert() = index
    #  complete_Mark = checklist.insert(index, "√")
    # complete_Mark = checklist[index] 
    # complete_Mark =  "√"
    complete_Mark = "√" + checklist[index] 
    # checklist.
    #  complete_Mark = checklist[index]  + "√"
    return complete_Mark

def user_input(prompt):
    user_input = input(prompt)

    return user_input

def select(function_code):
    # Create item
    if function_code == "C":
        input_item = input("Input item:")
        create(input_item)
    #read item
    elif function_code == "R":
        item_index = input("Index Number?")
        # item_index must exist else our program will crash
        read(int(item_index))

    elif function_code == "U":
        update_item_index = input("Index number of item you want to update:")
        print(update_item_index)
        update_item_text = input("Text of what you want to update the item with:")
        print(type(update_item_text))
        update(update_item_index, update_item_text)
        # update(update_item_index)
    elif function_code == "D":
        destroy_item_index = input("Index number of item you want to destroy:")

        destroy(destroy_item_index)
        # print all items
    elif function_code == "P":
        list_all_items()
        # catch all
    elif function_code == "Q":
        return False
    else:
        print("Unknown Option")
    return True

def test(): # test the functions above
    create("purple sox") # Creates elements in the checklist
    create("red cloak")
    # update(0, "zoom")
    print(checklist)
    running = True
    while running:
        selection = user_input("Press C to add to list, R to read from list, U to update, D to destory, P to display list and Q to quit")
        running = select(selection)

test() # runs the above function
# add update and destroy functions 
# Allow for the user to use upper or lowercase for function selection