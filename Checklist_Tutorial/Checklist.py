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

def mark_completed(index):


def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def test(): # test the functions above
    create("purple sox") # Creates elements in the checklist
    create("red cloak")
    print(read(0))
    print(read(1))
    update(0, "purple socks")
    destroy(1)
    print(read(0))
    # print(read(1))

    print(checklist)
    list_all_items()

test() # runs the above function


