from firebase import firebase

# https://bogosbinted-82a8f-default-rtdb.firebaseio.com/

myDB = firebase.FirebaseApplication('https://smart-home-5344a-default-rtdb.firebaseio.com/', None)
#                                                          Location                        Authentication

def createUser():
    
    print("\n|| User Information ||")
    
    fName = input("Please enter the First Name of user: ")
    sName = input("Please enter the Last Name of user: ")
    IDref = input("Please enter the user's date of birth (month and year in form MMYY): ")
    uID = fName[0]+sName[0]+IDref
    uIND = 0
    userListRecords = myDB.get("Users", None)
    for key in userListRecords:
        uIND += 1

    record = {
        "1: Firstname" : fName,
        "2: Surname" : sName,
        "3: ID"   : uID,
        "4: Index"  : uIND
        }

    myDB.post("Users", record)
    
def createRoom():
    
    print("\n|| Room Information ||")
    
    rName = input("Please enter the room's name: ")
    rIND = 0
    roomListRecords = myDB.get("Rooms", None)
    for key in roomListRecords:
        rIND += 1
    rID = rIND

    record = {
        "1: Name" : rName,
        "2: ID Number" : rID
        }
        
    myDB.post("Rooms", record)
    
def readRegistry():
    registryRecords = myDB.get("Registry", None)
    
    print("\n---  User Registry  ---\n")
    for key in registryRecords:
        print("| User ID: " + registryRecords[key]["1: User ID"], end = "\t")
        print("| User Name: " + registryRecords[key]["2: User Name"],end = "\t")
        print("| Room: " + registryRecords[key]["3: Room"], end = "\t")
        print("| Time Entered: " + registryRecords[key]["4: Time Entered"])
        print("\n--------------------------\n")
    # Prints information from the student registry from the Firebase database onto the computer
    
def readUsers():
    userRecords = myDB.get("Users", None)
    
    print("\n---    User List    ---\n")
    for key in userRecords:
        print("|    User Name: " + str(userRecords[key]["1: Firstname"]), str(userRecords[key]["2: Surname"]), end = "\t")
        print("|    User ID: " + userRecords[key]["3: ID"]) 
        print("\n--------------------------\n")

def readRooms():
    roomRecords = myDB.get("Rooms", None)
    
    print("\n---    Room List    ---\n")
    for key in roomRecords:
        print("|    Room Name: " + str(roomRecords[key]["1: Name"]), end = "\t")
        print("|    Room ID: " + str(roomRecords[key]["2: ID Number"]), end = "\t")
        print("\n--------------------------\n")
    # Prints information from the teacher list from the Firebase database onto the computer 

while True:
    print("\n\n|||||   MAIN MENU   |||||\n[1] Create User\n[2] Create Room\n[3] Read Registry\n[4] Read Users\n[5] Read Rooms\n[6] End Program")
    
    move = ''
    
    while move == '':

        move = input('> ')

    move = move.lower().split()


    if move[0] == '1':
        createUser()
        
    elif move[0] == '2':
        createRoom()
        
    elif move[0] == '3':
        readRegistry()
        
    elif move[0] == '4':
        readUsers()
    
    elif move[0] == '5':
        readRooms()    
        
    elif move[0] == '6':
        break
        
# Menu for the program