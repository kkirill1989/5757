xpath:
    # Поле ввода "username" страницы авторизации
    LOCATOR_LOGIN_FIELD: //*[@id="login"]/div[1]/label/input
    # Поле ввода "password" страницы авторизации
    LOCATOR_PASS_FIELD: //*[@id="login"]/div[2]/label/input
    # Блок ошибки страницы авторизации
    LOCATOR_ERROR_FIELD: //*[@id="app"]/main/div/div/div[2]/h2
    # Ссылка на профиль пользователя с выпадающим меню на главной странице
    LOCATOR_USER_PROFILE_LINK: //*[@id="app"]/main/nav/ul/li[3]/a
    # Поле ввода "Title" формы создания поста
    LOCATOR_FORM_POST_TITLE: /html/body/div/main/div/div/form/div/div/div[1]/div/label/input
    # Поле ввода "Description" формы создания поста
    LOCATOR_FORM_POST_DESCRIPTION: /html/body/div/main/div/div/form/div/div/div[2]/div/label/span/textarea
    # Поле ввода "Content" формы создания поста
    LOCATOR_FORM_POST_CONTENT: /html/body/div/main/div/div/form/div/div/div[3]/div/label/span/textarea
    # Название поста на странице поста сразу после его создания
    LOCATOR_POST_NAME: //*[@id="app"]/main/div/div[1]/h1
    # Поле ввода "Your name" формы "Contact us!"
    LOCATOR_USERNAME_FIELD_CONTACT_US_FORM: //*[@id="contact"]/div[1]/label/input
    # Поле ввода "Your email" формы "Contact us!"
    LOCATOR_EMAIL_FIELD_CONTACT_US_FORM: //*[@id="contact"]/div[2]/label/input
    # Поле ввода "Content" формы "Contact us!"
    LOCATOR_CONTENT_FIELD_CONTACT_US_FORM: //*[@id="contact"]/div[3]/label/span/textarea
css:
    # Кнопка "Login" страницы авторизации
    LOCATOR_LOGIN_BTN: button
    # Кнопка создания поста на главной странице
    LOCATOR_CREATE_POST_BTN: '#create-btn'
    # Кнопка сохранения поста "SAVE" формы создания поста
    LOCATOR_SAVE_POST_BTN: '.mdc-button__label'
    # Кнопка "Contact" открытия формы "Contact us!" на главной странице
    LOCATOR_CONTACT_FORM_BTN: '#app > main > nav > ul > li:nth-child(2) > a'
    # Кнопка "CONTACT US" отправки формы "Contact us!"
    LOCATOR_SEND_CONTACT_US_FORM_BTN: button