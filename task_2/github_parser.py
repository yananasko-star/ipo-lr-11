"""
Задание 2: Парсинг популярных репозиториев GitHub
Программа собирает данные с https://github.com/trending
и выводит в нужном формате.
"""

import requests
from bs4 import BeautifulSoup

def get_github_trending():
    """
    Функция для получения популярных репозиториев с GitHub
    """
    print("🔍 Начинаю сбор данных с GitHub Trending...")
    print("=" * 50)
    
    # URL страницы с трендами
    url = "https://github.com/trending"
    
    try:
        # Заголовки для запроса
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        # Отправляем запрос
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверяем успешность запроса
        
        # Создаем объект для парсинга HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Находим все репозитории
        repositories = []
        
        # Ищем статьи с репозиториями
        articles = soup.find_all('article', class_='Box-row')
        
        for i, article in enumerate(articles[:10], 1):  # Берем первые 10
            # Название репозитория
            h2_tag = article.find('h2')
            if h2_tag:
                repo_name = h2_tag.text.strip().replace('\n', '').replace(' ', '')
            else:
                repo_name = "Неизвестно"
            
            # Количество звезд
            stars_tag = article.find('a', href=lambda x: x and 'stargazers' in x)
            if stars_tag:
                stars_text = stars_tag.text.strip()
                # Убираем запятые и пробелы
                stars = stars_text.replace(',', '').replace(' ', '')
            else:
                stars = "0"
            
            # Форматируем вывод
            formatted_name = repo_name.replace('/', ' / ')
            
            # Сохраняем данные
            repositories.append({
                'number': i,
                'name': formatted_name,
                'stars': stars
            })
        
        return repositories
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Ошибка при подключении к GitHub: {e}")
        return []
    except Exception as e:
        print(f"❌ Неожиданная ошибка: {e}")
        return []

def display_repositories(repos):
    """
    Выводит репозитории в нужном формате
    """
    if not repos:
        print("Нет данных для отображения")
        return
    
    print("\n📊 ПОПУЛЯРНЫЕ РЕПОЗИТОРИИ GITHUB:")
    print("=" * 50)
    
    for repo in repos:
        # Форматируем звезды с запятыми
        stars_formatted = f"{int(repo['stars']):,}" if repo['stars'].isdigit() else repo['stars']
        
        # Выводим в требуемом формате
        print(f"{repo['number']}. Repository: {repo['name']}; Stars: {stars_formatted};")
    
    print("=" * 50)
    print(f"✅ Всего найдено репозиториев: {len(repos)}")

def main():
    """
    Главная функция программы
    """
    print("=" * 50)
    print("ПРОГРАММА ДЛЯ ПАРСИНГА GITHUB TRENDING")
    print("=" * 50)
    
    # Получаем данные
    repositories = get_github_trending()
    
    # Выводим данные
    display_repositories(repositories)
    
    # Сохраняем данные для следующих заданий
    if repositories:
        print("\n💾 Данные готовы для сохранения в JSON (задание 3)")
        print("📄 Данные готовы для генерации HTML (задание 4)")
    
    print("\n" + "=" * 50)
    print("Задание 2 выполнено успешно!")
    print("=" * 50)

if name == "main":
    main()
