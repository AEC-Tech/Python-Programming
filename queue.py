def isEmpty(que):
    if len(que) == 0:
        return True
    else:
        return False

def Enqueue(que,item):
    que.append(item)
    if len(que) == 1:
        front = rear = 0
    else:
        rear = len(que) - 1

def Dequeue(que):
    if isEmpty(que):
        return "Underflow"
    else:
        item = que.pop(0)
        if len(que) == 0:
            front = rear = None
        else:
            rear = len(que) - 1
        return item

def peek(que):
    if isEmpty(que):
        return "Underflow"
    else:
        front = 0
        return que[front]
    
def display(que):
    if isEmpty(que):
        print("Queue is Empty")
    elif len(que) == 1:
        print("Front = Rear => ",que[0])
    else:
        front = 0
        rear = len(que) - 1
        print("Front => ",que[front])
        for i in range(front+1, rear):
            print(que[i])
        print("Rear => ",que[rear])



queue = []
front = None
rear = None

while True:
    print("QUEUE IMPLEMENTATION ")
    print("Press 1 - Enqueue ")
    print("Press 2 - Dequeue ")
    print("Press 3 - Peek")
    print("Press 4 - Display")
    print("Press 5 - Exit")
    choice = int(input("enter your choice "))
    if choice == 1:
        value = int(input("Enter a number to be inserted : "))
        Enqueue(queue,value)
    elif choice == 2:
        value = Dequeue(queue)
        print("Deleted value is ", value)
    elif choice == 3:
        value = peek(queue)
        print("Top most value is ",value)
    elif choice == 4:
        display(queue)
    else:
        break
