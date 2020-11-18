def isEmpty(stk):
    if len(stk) == 0:
        return True
    else:
        return False

def push(stk,item):
    stk.append(item)
    top = len(stk) - 1

def pop(stk):
    if isEmpty(stk):
        return "Underflow"
    else:
        item = stk.pop()
        if len(stk) == 0:
            top = None
        else:
            top = len(stk) - 1
        return item
def peek(stk):
    if isEmpty(stk):
        return "Underflow"
    else:
        top = len(stk) - 1
        return stk[top]
def display(stk):
    if isEmpty(stk):
        print("Stackis Empty")
    else:
        top = len(stk) - 1
        print("Top => ",stk[top])
        for i in range(top-1, -1, -1):
            print(stk[i])



stack = []
top = None

while True:
    print("STACK IMPLEMENTATION ")
    print("Press 1 - Push ")
    print("Press 2 - Pop ")
    print("Press 3 - Peek")
    print("Press 4 - Display")
    print("Press 5 - Exit")
    choice = int(input("enter your choice "))
    if choice == 1:
        value = int(input("Enter a number to be pushed : "))
        push(stack,value)
    elif choice == 2:
        value = pop(stack)
        print("Deleted value is ", value)
    elif choice == 3:
        value = peek(stack)
        print("Top most value is ",value)
    elif choice == 4:
        display(stack)
    else:
        break
