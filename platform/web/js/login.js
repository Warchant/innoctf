// Generated by CoffeeScript 1.11.1
(function() {
  var login, resetPassword;

  login = function(e) {
    e.preventDefault();
    return apiCall("POST", "/api/user/login", $("#login-form").serializeObject()).done(function(data) {
      switch (data['status']) {
        case 0:
          $("#login-button").apiNotify(data, {
            position: "right"
          });
          return ga('send', 'event', 'Authentication', 'LogIn', 'Failure::' + data.message);
        case 1:
          ga('send', 'event', 'Authentication', 'LogIn', 'Success');
          if (data.data['teacher']) {
            return document.location.href = "/classroom";
          } else {
            return document.location.href = "/team";
          }
      }
    });
  };

  resetPassword = function(e) {
    $("#reset-password-button").html("Please Wait...");
    $("#reset-password-button").attr('disabled', true);
    e.preventDefault();
    return apiCall("GET", "/api/user/reset_password", $("#password-reset-form").serializeObject()).done(function(data) {
      apiNotify(data);
      switch (data['status']) {
        case 0:
          ga('send', 'event', 'Authentication', 'PasswordReset', 'Failure::' + data.message);
          break;
        case 1:
          ga('send', 'event', 'Authentication', 'PasswordReset', 'Success');
      }
      $("#reset-password-button").html("Reset Password");
      return $("#reset-password-button").attr('disabled', false);
    });
  };

  $(function() {
    $("#password-reset-form").toggle();
    $("#login-form").on("submit", login);
    $("#password-reset-form").on("submit", resetPassword);
    return $(".toggle-login-ui").on("click", function(e) {
      e.preventDefault();
      $("#login-form").toggle();
      return $("#password-reset-form").toggle();
    });
  });

}).call(this);
