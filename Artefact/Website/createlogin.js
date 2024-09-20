// will need to be replaced with the link to most current firebase database
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
	apiKey: "AIzaSyBUqDSzigfTm-k846uY4eUTRomJkVMCUSc",
	authDomain: "smart-home-5344a.firebaseapp.com",
	databaseURL: "https://smart-home-5344a-default-rtdb.firebaseio.com",
	projectId: "smart-home-5344a",
	storageBucket: "smart-home-5344a.appspot.com",
	messagingSenderId: "1022737554100",
	appId: "1:1022737554100:web:2f10df6ae44055c94715e1",
	measurementId: "G-640DHBRBZQ"
  };

	  // Initialize Firebase
	  firebase.initializeApp(firebaseConfig);


// fucntion for inserting records 
function insertRecords(){

	// used to show javascript is working. Can be removed later
	alert("Submitted");

	
	var eN=document.getElementById('emailIn').value;
	var passN=document.getElementById('passwordIn').value;
	var fName=document.getElementById('fName').value;
	var sName=document.getElementById('sName').value;

	// connects to the current firebase database 
	var myDB=firebase.database().ref();
	// identifies the node the data is to be pushed too
	var addRecords=myDB.child('logins').push();
		
		record={
		
			"First Name" : fName,
			"Last Name" : sName,
			"Email" : eN,
			"Password" : passN,
		
		};
		addRecords.set(record);
	}