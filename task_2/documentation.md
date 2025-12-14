

Задание 2: Парсинг GitHub репозиториев

Описание задачи
Программа собирает информацию о популярных репозиториях на GitHub и выводит данные в заданном формате.

Требуемый формат вывода

1. Repository: twentyhq / twenty; Stars: 21,766;
2. Repository: payloadcms / payload; Stars: 27,207;
3. Repository: leaningtech / webvm; Stars: 9,663;

Реализация
Программа github_parser.py делает следующее:

1. Отправляет запрос на страницу https://github.com/trending
2. Парсит HTML страницу с помощью BeautifulSoup
3. Извлекает названия репозиториев и количество звезд
4. Выводит результат в консоль

Используемые библиотеки

· requests - для получения HTML страницы
· beautifulsoup4 - для парсинга HTML

Как запустить

1. Активировать виртуальное окружение
2. Установить зависимости: pip install -r ../task_1/requirements.txt
3. Запустить программу: python github_parser.py

Пример работы программы
После запуска программа выведет:

1. Repository: microsoft / vscode; Stars: 150,342;
2. Repository: facebook / react; Stars: 210,987;
3. Repository: tensorflow / tensorflow; Stars: 175,432;

Для следующих заданий
Собранные данные будут использованы:

· В задании 3: сохранение в JSON файл
· В задании 4: генерация HTML страницы
