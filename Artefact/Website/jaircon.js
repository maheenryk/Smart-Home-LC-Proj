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
  firebase.initializeApp(firebaseConfig);
  
  var myDB = firebase.database().ref("AirConStatus/ Jason's Room");
  var light = firebase.database().ref("LightStatus/ Jason's Room");
  var win = firebase.database().ref("WindowStatus/ Jason's Room");
  var blinds = firebase.database().ref("BlindsStatus/ Jason's Room");

  function on() {
    myDB.set({
        'Condition':'on'
    });
  }
  
  function off() {
    myDB.set({
        'Condition':'off'
    });
  }
  
  function lightOn() {
    light.set({
        'Condition':'on'
    });
  }
  
  function lightOff() {
    light.set({
        'Condition':'off'
    });
  }
  
  function winOpen() {
    win.set({
        'Condition':'open'
    });
  }
  
  function winClose() {
    win.set({
        'Condition':'close'
    });
  }

  function blindsUp() {
    blinds.set({
        'Condition':'up'
    });
  }
  
  function blindsDown() {
    blinds.set({
        'Condition':'down'
    });
  }