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
    del checklist[index]

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
    if function_code == "C" or function_code == "c":
        input_item = input("New item name:")
        create(input_item)
    #read item
    elif function_code == "R" or function_code == "r":
        
        # item_index must exist else our program will crash
        try:
            item_index = input("Index Number: ")
            read(int(item_index))
        except IndexError:
            print("try a number that's in range.")
        

    elif function_code == "U" or function_code == "u":
         try:
            update_index = input("Index number to update: ")
            update_text = input("Update item text with..: ")
            update(int(update_index), str(update_text))
         except IndexError:
            print("try a number that's in range.")
        
        # update_text = input("Text of what you want to update the item with:")
        # print(type(update_item_text))

    elif function_code == "D" or function_code == "d":
        
        try:
            destroy_item_index = input("Index number of item you want to destroy:")
            destroy(int(destroy_item_index))
        except IndexError:
            print("try a number that's in range.")
        # if destroy_item_index != type(str()):
        #     print("please enter a valid Integer next time.")
            
        # print all items
    elif function_code == "P" or function_code == "p":
        list_all_items()
        # catch all
    elif function_code == "Q"or function_code == "q":
        return False
    else:
        print("Unknown Option")
    return True

def test(): # test the functions above
    create("purple sox") # Creates elements in the checklist
    create("red cloak")
    print(checklist)
    running = True
    while running:
        selection = user_input("Press C to add to list, R to read from list, U to update, D to destory, P to display list and Q to quit")
        running = select(selection)

test() # runs the above function
# add update and destroy functions 
# Allow for the user to use upper or lowercase for function selection