Дипломный проект. 
Предстояло протестировать новый интерфейс авторизации в личном кабинете от заказчика Ростелеком Информационные Технологии. 
Ссылка на сайт - https://b2c.passport.rt.ru/


1. В папке pages находится:
- base_page.py  содержит конструктор webdriver для всех тестируемых страниц методы.
- locators.py  находятся все локаторы.
- change_pass.py  содержит методы проверок формы восстановления пароля.
- authorization.py  содержит методы проверок формы авторизации.
- registration.py  содержит методы проверок формы регистрации.


2. В папке tests находится:
- test_authorization.py  тесты формы авторизации.
- test_change_pass.py  тесты формы восстановления пароля.
- test_registration.py  тесты формы регистрации.


Последовательность проверок идет в последовательности: Регистрация -> Авторизация -> Восстановление пароля. 


Файлы в корне:
- conftest.py  в нем находится фикстура с функцией открытия и закрытия браузера.
- settings.py  в нем находятся методы для параметризации тестов.
- requirements.py  в нем находится все используемые библиотеки из PyCharm.
- .gitinore 

Все тесты написаны с использованием среды разработки PyCharm и вирнального окружения. Так же все тесты запускаются через библиотеку Pytest.
Каждый тесты имеет соответствующий номер в тест-кейсе 
https://docs.google.com/spreadsheets/d/1nTDXSp4MyhOt4149bBOL5qBRIKyZKKDcG_z7CLVDG7M/edit?usp=share_link
