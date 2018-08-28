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
    # read(0)
    # print(read(0))
    # print(read(1))
    # update(0, "purple socks")
    # destroy(1)
    # print(read(0))
    # print(read(1))

    # print(checklist)
    # list_all_items()
    # create("bananas")
    # print(mark_completed(0))
    running = True
    while running:
        selection = user_input("Press C to add to list, R to read from list, P to display list and Q to quit")
        running = select(selection)

    # print(checklist)
    # select("C")
    # list_all_items()
    # select("R")
    # list_all_items()
    # user_value = input("Please enter a value:")
    # print(user_value)

    
test() # runs the above function
