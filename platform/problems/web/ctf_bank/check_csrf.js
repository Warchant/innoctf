var page = new WebPage(), testindex = 0, loadInProgress = false;

page.onConsoleMessage = function(msg) {
  console.log(msg);
};

page.onLoadStarted = function() {
  loadInProgress = true;
  console.log("load started");
};

page.onLoadFinished = function() {
  loadInProgress = false;
  console.log("load finished");
};

var steps = [
  function() {
    //Load Login Page
    page.open("http://127.0.0.1:8000/login");
  },
  function() {
    //Enter Credentials
    page.evaluate(function() {

      var arr = document.getElementsByClassName("login-form");
      var i;

      for (i=0; i < arr.length; i++) { 
        if (arr[i].getAttribute('method') == "post") {

          arr[i].elements["username"].value="banker";
          arr[i].elements["password"].value="2";
          return;
        }
      }
    });
  }, 
  function() {
    //Login
    page.evaluate(function() {
      var arr = document.getElementsByClassName("login-form");
      var i;

      for (i=0; i < arr.length; i++) {
        if (arr[i].getAttribute('method') == "post") {
          arr[i].submit();
          return;
        }
      }
    });
  },
  function() {
      page.open("http://127.0.0.1:8000/loan/");
      console.log("Success");
  }
];


interval = setInterval(function() {
  if (!loadInProgress && typeof steps[testindex] == "function") {
    steps[testindex]();
    testindex++;
  }
  if (typeof steps[testindex] != "function") {
    phantom.exit();
  }
}, 50);