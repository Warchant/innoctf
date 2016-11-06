apiOffline =
  Инфо: "/about"
  Новости: "/news"

teacherLoggedIn =
  Задания: "/problems"
#  Shell: "/shell"
  Рейтинг: "/scoreboard"
  Класс: "/classroom"
  Инфо:
    Инфо: "/about"
    Новости: "/news"
  Аккаунт:
    Настройка: "/account"
    Выйти: "#"

teacherLoggedInNoCompetition =
  Класс: "/classroom"
  Инфо: "/about"
  Новости: "/news"
  Аккаунт:
    Настройка: "/account"
    Выйти: "#"

userLoggedIn =
  Задания: "/problems"
#  Shell: "/shell"
  Команда: "/team"
  Чат: "/chat"
  Рейтинг: "/scoreboard"
  Инфо:
    Инфо: "/about"
    Новости: "/news"
  Аккаунт:
    Настройка: "/account"
    Выйти: "#"

userLoggedInNoCompetition =
  Команда: "/team"
  Чат: "/chat"
  Рейтинг: "/scoreboard"
  Инфо:  
    Инфо: "/about"
    Новости: "/news"
  Аккаунт:
    Настройка: "/account"
    Выйти: "#"


userNotLoggedIn =
  Инфо: "/about"
  Новости: "/news"
  Рейтинг: "/scoreboard"
  Войти: "/login"

loadNavbar = (renderNavbarLinks, renderNestedNavbarLinks) ->

  navbarLayout = {
    renderNavbarLinks: renderNavbarLinks,
    renderNestedNavbarLinks: renderNestedNavbarLinks
  }

  apiCall "GET", "/api/user/status", {}
  .done (data) ->
    navbarLayout.links = userNotLoggedIn
    navbarLayout.topLevel = true
    if data["status"] == 1
      if not data.data["logged_in"]
        $(".show-when-logged-out").css("display", "inline-block")
      if data.data["teacher"]
        if data.data["competition_active"]
           navbarLayout.links = teacherLoggedIn
        else
           navbarLayout.links = teacherLoggedInNoCompetition
      else if data.data["logged_in"]
         if data.data["competition_active"]
            navbarLayout.links = userLoggedIn
         else
            navbarLayout.links = userLoggedInNoCompetition
    $("#navbar-links").html renderNavbarLinks(navbarLayout)
    $("#navbar-item-logout").on("click", logout)

  .fail ->
    navbarLayout.links = apiOffline
    $("#navbar-links").html renderNavbarLinks(navbarLayout)

$ ->
  renderNavbarLinks = _.template($("#navbar-links-template").remove().text())
  renderNestedNavbarLinks = _.template($("#navbar-links-dropdown-template").remove().text())

  loadNavbar(renderNavbarLinks, renderNestedNavbarLinks)
