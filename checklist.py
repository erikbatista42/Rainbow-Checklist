# creating a list
checklist = list()
print(checklist)

checklist.append("hello")
print(checklist)

checklist.append("world")
print(checklist)

# a function that adds something to our checklist
def add_something_to_my_checklist(add_item):
    checklist.append(add_item)
# adding something to our list when our function is called
add_something_to_my_checklist("i'm")
print(checklist)

add_something_to_my_checklist("erik")
print(checklist)