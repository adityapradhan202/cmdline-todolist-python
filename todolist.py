# Function for showing the entire list
def showList(t):
    centerString = "YOUR TO DO LIST"
    print(centerString.center(50, "."))
    
    for i in range(len(t)):
        print(f"{i+1}. {t[i]}")
    
    centerString2 = "."
    print(centerString2.center(50, "."))
    

def addTask(s, l):
    l.append(s)

def removeTask(ind, l):
    l.remove(l[ind-1])

def replaceTask(ind, l, s):
    l.remove(l[ind-1])
    l.insert(ind-1, s)
    
def delAllTasks(l):
    l.clear()

def doneTask(ind, l):
    a = l.pop(ind-1)
    l.insert(ind-1, f"{a} (Done)")
    

def homepage():
    print()
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Show all tasks")
    print("4. Clear to-do-list")
    print("5. Update a task")
    print("6. Mark a task as done")
    print("7. Exit the to-do-list")
    print()
    userInput = int(input("Choose your option: "))
    
    match userInput:
        case 1:
            nTask = input("Enter the new task: ")
            addTask(s=nTask, l=tasks)
            homepage()
        case 2: 
            rtask = int(input("Enter the number of task that you want to remove: "))
            removeTask(ind=rtask, l=tasks)
            homepage()
        case 3:
            showList(t=tasks)
            homepage()
        case 4:
            delAllTasks(l=tasks)
            homepage()
        case 5:
            uTaskInd = int(input("Enter the number of the task that you want to update: "))
            uTask = input("Enter the new task: ")
            
            replaceTask(ind=uTaskInd, l=tasks, s=uTask)
            homepage()
        case 6:
            dTask = int(input("Enter the task number that you want to mark as done: "))
            doneTask(ind=dTask, l=tasks)
            homepage()
        case 7:
            print("Thanks for using our to-do-list!")
            exit(0)
        case _:
            print("Invalid input!")
            print("Please enter valid input!")
            homepage()

def main():
    x = input("Type start to use the to-do-list: ")
    
    if x.lower() == "start":
        homepage()
    else:
        print("Invalid input!")
        print("Press enter key to start the to-do-list!")
        main()
    
    
tasks = [] # Empty list

# Calling the main function now
main()



