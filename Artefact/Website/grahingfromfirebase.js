  // Your web app's Firebase configuration
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

var livingroomTemps = [];
var kitchenTemps = [];
var juTemp = [];
var time = [];
var time1 = [];

  //on database update
var livingRoom = firebase.database().ref("/Temps/Living Room/");

livingRoom.on("child_added", function (data, prevChildKey) {
    var dataPoint = data.val();
    livingroomTemps.push(dataPoint.Temperature);
    time.push(dataPoint.Timestamp);
    drawGraph();
  });

  //on database update
var kitchen = firebase.database().ref("/Temps/Kitchen/");

kitchen.on("child_added", function (data, prevChildKey) {
    var dataPoint = data.val();
    kitchenTemps.push(dataPoint.Temperature);
    time.push(dataPoint.Timestamp);
    drawGraph();
  });

  //on database update
var juroom = firebase.database().ref("/Temps/Jason's Room/");

juroom.on("child_added", function (data, prevChildKey) {
    var dataPoint = data.val();
    juTemp.push(dataPoint.Temperature);
    time.push(dataPoint.Timestamp);
    drawGraph();
  });

function drawGraph() {
    var livingroom = {
      y: livingroomTemps,
      x: time,
      name: "Living Room",
      mode: "lines+markers",
    };

    var kitchen = {
      y: kitchenTemps,
      x: time,
      name: "Kitchen",
      mode: "lines+markers",
    };

    var juroom = {
      y: juTemp,
      x: time,
      name: "Jason's Room",
      mode: "lines+markers",
    };

    var layout = {
      title: "Home Temperatures",
      plot_bgcolor:"white",
      xaxis: {
        title: "Time",
      },

      yaxis: { title: "Temp" },
    };

    var data = [livingroom, kitchen, juroom];

    Plotly.newPlot("myGraph", data, layout);
  }
