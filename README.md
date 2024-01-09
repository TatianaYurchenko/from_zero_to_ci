"# from_zero_to_ci" 
HOST = "https://opensource-demo.orangehrmlive.com/web/index.php"
    LOGIN_PAGE = f"{HOST}/auth/login"
    DASHBOARD_PAGE = f"{HOST}/dashboard/index"
    PERSONAL_PAGE = f"{HOST}/pim/viewPersonalDetails/empNumber/7"
Структура проекта
base базовые конфигурационные файлы для страниц и тестов
pages объекты страниц
config ссылки урлы и днные
tests тесты
conftest фикстуры
.env для хранения логина пароля
