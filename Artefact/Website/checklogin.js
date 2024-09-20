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

var usernames = [];
var passwords = [];

var myDBConn = firebase.database().ref("logins");

myDBConn.on("child_added", function(data, prevChildKey){

  // The data returned from the branch is put into a variable, dataPoint
  var dataPoint = data.val();

  // Populate the lists with the various data from the database
  usernames.push(dataPoint.Email);
  passwords.push(dataPoint.Password);

});

function login(){

  username1 = document.getElementById("usernameIn").value;
  pass = document.getElementById("passwordIn").value;
  
  var credCorrect = "N";
  for(var index = 0; index < usernames.length; index+=1){
  if(usernames[index] == username1 && passwords[index] == pass){
  credCorrect = "Y"
  }
  }
  
  if(credCorrect == "Y"){
  window.open("home.html","_self");
  }
  
  else{
  alert("Wrong details. Please try again.")
  }
  }