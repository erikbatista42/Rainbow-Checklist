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
    create("Hey,") # Creates elements in the checklist
    create(" Erik")
    print(checklist)
    read(1) # reads what's on the 1 index in the checklist
    update(0, "Sup")
    print(checklist)
test()