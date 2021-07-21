import shelve

print("Welcome to the To-Do List application!")
userName = input("Please enter your name to access your To-Do List. ")
userName= userName.lower() + ".dat"

toDoList = shelve.open(userName)         #opens DB
toDoList.sync()                  #syncs to pre-existing data
list(toDoList.keys())            #opens list

choice = 'n'
def chooseAction():
  print("\n[Q]uit / [A]dd / [R]emove / [S]how / [C]lear ")
  choice = input()
  choice = choice.lower()
  if(choice == 'q'):
    quitProgram()
  elif(choice == 'a'):
    addItem(toDoList)
  elif(choice == 'r'):
    removeItem(toDoList)
  elif(choice == 's'):
    showList(toDoList)
  elif(choice == 'c'):
    clearList(toDoList)

  
def quitProgram():
  print("Thanks for using our program")
  exit()

def addItem(toDoList):
  itemToAdd = input("Which task would you like to add? ")
  toDoList[itemToAdd] = itemToAdd

def removeItem(toDoList):         
  print("Which task would you like to remove? ")
  removeThis = input()
  print(removeThis + " has been removed. ")
  del toDoList[removeThis]

def showList(toDoList):
  if(len(toDoList) == 0):
    print("Your To-Do List is empty. ")
  else:
    print("Here's your To-Do List: ")
    print(*toDoList)



def clearList(toDoList):
  toDoList.clear()
  print("To-Do List is now empty. ")


def main():
  while(choice != 'q'):
    chooseAction()
  toDoList.close()

main()