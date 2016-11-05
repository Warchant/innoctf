updatePassword = (e) ->
  e.preventDefault()
  apiCall "POST", "/api/user/update_password", $("#password-update-form").serializeObject()
  .done (data) ->
    switch data['status']
      when 1
        ga('send', 'event', 'Authentication', 'UpdatePassword', 'Success')
      when 0
        ga('send', 'event', 'Authentication', 'UpdatePassword', 'Failure::' + data.message)
    apiNotify data, "/account"

resetPassword = (e) ->
  e.preventDefault()
  form = $("#password-reset-form").serializeObject()
  form["reset-token"] = window.location.hash.substring(1)
  apiCall "POST", "/api/user/confirm_password_reset", form
  .done (data) ->
    ga('send', 'event', 'Authentication', 'ResetPassword', 'Success')
    apiNotify data, "/login"

disableAccount = (e) ->
  e.preventDefault()
  confirmDialog("Ваш аккаунт будет отключен, Вы будете исключены из команды и не сможете больше вернуться!", "Отключить подтверждение аккаунта", "Отключить", "Отмена",
  () ->
    form = $("#disable-account-form").serializeObject()
    apiCall "POST", "/api/user/disable_account", form
    .done (data) ->
      ga('send', 'event', 'Authentication', 'DisableAccount', 'Success')
      apiNotify data, "/")

$ ->
  $("#password-update-form").on "submit", updatePassword
  $("#password-reset-form").on "submit", resetPassword
  $("#disable-account-form").on "submit", disableAccount
