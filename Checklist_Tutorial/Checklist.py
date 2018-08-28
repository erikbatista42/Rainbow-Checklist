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

test() # runs the above function