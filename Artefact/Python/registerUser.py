from firebase import firebase
import datetime
import time
import serial
import firebase_admin
from firebase_admin import db

#initializes firebase application
cred_object = firebase_admin.credentials.Certificate(r'C:\Users\mahee\OneDrive\Documents\School\Comp. Science\LC HL 2022\Python\smart-home-5344a-firebase-adminsdk-kuz0n-3b6d966c4f.json')
default_app = firebase_admin.initialize_app(cred_object, {
    'databaseURL': "https://smart-home-5344a-default-rtdb.firebaseio.com/"
    })

#open connection with microbit for transfer of data
ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM5"
ser.open()

rName = ""

myDB = firebase.FirebaseApplication('https://smart-home-5344a-default-rtdb.firebaseio.com/', None)

#until the room is identified, the code loops
while rName == "":
    print("Register room.")
    
    microbitdata = str(ser.readline())

    rID = microbitdata[1:]
    rID = rID.replace(" ", "")
    rID = rID.replace("\\r\\n", "")
    rID = rID.replace("\\r\\n", "")
    rID = rID.replace("'", "")
    #the code is cleaned up to be read
    
    #if the data sent from the microbit isn't all didgits and is also 2 characters long
    #it is registered as the room ID. e.g "R2" will be read as the room ID but "01" or "R03" won't
    if rID.isdigit() == False and len(rID) == 2:
        roomID = rID[-1]

        roomRecords = myDB.get("Rooms", None)
        roomPrimaryKeys = []
        userListRecords = myDB.get("Users", None)
        userListPrimaryKeys = []
        displayIndex = 1

        for key in userListRecords:
            userListPrimaryKeys.append(key)
            # Retrieves keys from the "userList" database in Firebase
            
        print("\n|      Room List      |")
        for key in roomRecords:
            roomPrimaryKeys.append(key)
            print(str(displayIndex) + ": " + roomRecords[key]["1: Name"])
            displayIndex += 1
            # Lists rooms along with their ID
            
        rIndex = int(roomID)
        # Input room's ID to log in
            
        rName = (roomRecords[roomPrimaryKeys[rIndex]]["1: Name"])
        # Retrieves the room's name
        
        print("\n")
        
        print("Room evaluated. This is: "+rName+".")
            
        print("\n")
        

firebase = firebase.FirebaseApplication('https://smart-home-5344a-default-rtdb.firebaseio.com/', None)        

def openclose():
    result = firebase.get("/WindowStatus/ "+rName, 'Condition')
    return result
#retreives whether the blinds are up or down and stores the info    
    
    
while True:
#when the room ID is retrieved, the code starts looping and collecting the temperature data

    res = openclose()
    print(res)
    data = res+","
    if res == "open":
        ser.write(data.encode())
        print("Windows in "+rName+": "+res)
    elif res == "close":
        ser.write(data.encode())
        print("Windows in "+rName+": "+res)
    #writes the result from Firebase to Microbit
    
    recID = str(ser.readline())
    recID = recID[1:]
    recID = recID.replace(" ", "")
    recID = recID.replace("\\r\\n", "")
    recID = recID.replace("\\r\\n", "")
    recID = recID.replace("'", "")
    
    
    #if the receieved id is all numbers, the data received is recognised as temperature and is logged into firebase
    if recID.isdigit() == True:
        temp = recID
        time = datetime.datetime.today().strftime("%H:%M:%S")
        print("The temperature in " + rName + " at " + time + " is " + temp + ".")
        #displays current room temperature
        
        record = {
            "Temperature" : temp,
            "Timestamp" : time
            }
        
        myDB.post("Temps/"+rName, record)
        #posts all the data to firebase
        
        ref = db.reference("Current Temperature/"+rName)
        
        aircon = db.reference("AirConStatus/"+rName)
        
        cTemp = {
            "Temperature" : temp
            }
        ref.set(cTemp)
        #sets the current temperature of the room in firebase
        
        #turns on air conditioning if temperature above certain level
        if int(temp) >= 28:
            on = {
                "Condition" : "on"
                }
            aircon.set(on)
            
        else:
            off = {
                "Condition" : "off"
                }
            aircon.set(off)         
        
    elif len(recID) == 7:
        #if the received data is 7 characters in length, it is treated as the user ID
        
        print("User ID = ", recID)
        # Process received ID to be readable
        
        usID = recID[:6]
        usInd = int(recID[6:])
        userKey = userListPrimaryKeys[usInd]
        # Splits up the received ID into the user's ID and user index (ie. PA29120 -> ID: PA2912 & Index: 0) and retrieves the user's database key
            
        uName = userListRecords[userKey]["1: Firstname"] + " " + userListRecords[userKey]["2: Surname"]
        # Retrieves the user's first and last name
            
        print(uName + " entered " + rName + " at " + datetime.datetime.today().strftime("%d/%m/%Y, %H:%M:%S"))
        # Displays that a user has entered a room
            
        record = {
            "1: User ID" : usID,
            "2: User Name" : uName,
            "3: Room" : rName,
            "4: Time Entered" : datetime.datetime.today().strftime("%d/%m/%Y, %H:%M:%S")
            }
        # Records the collected data in a dictionary
            
        myDB.post("Registry", record)
        # Sends the dictionary to Firebase
    
#Close serial connection
ser.close()
