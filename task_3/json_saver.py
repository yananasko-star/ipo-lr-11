"""
Задание 3: Сохранение данных в JSON
Программа сохраняет данные в файл data.json
"""

import json
import os
from datetime import datetime

def save_to_json(data, filename="data.json"):
    """
    Сохраняет данные в JSON файл
    """
    print(f"💾 Сохраняю данные в файл {filename}...")
    
    try:
        # Создаем структуру данных
        json_data = {
            "metadata": {
                "source": "GitHub Trending",
                "url": "https://github.com/trending",
                "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "total_repositories": len(data)
            },
            "repositories": data
        }
        
        # Сохраняем в файл
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(json_data, file, ensure_ascii=False, indent=2)
        
        print(f"✅ Данные успешно сохранены в {filename}")
        print(f"📊 Сохранено репозиториев: {len(data)}")
        
        return True
        
    except Exception as e:
        print(f"❌ Ошибка при сохранении: {e}")
        return False

def load_from_json(filename="data.json"):
    """
    Загружает данные из JSON файла
    """
    print(f"📂 Загружаю данные из файла {filename}...")
    
    try:
        if not os.path.exists(filename):
            print(f"❌ Файл {filename} не найден")
            return None
        
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        print(f"✅ Данные успешно загружены")
        return data
        
    except Exception as e:
        print(f"❌ Ошибка при загрузке: {e}")
        return None

def create_example_data():
    """
    Создает пример данных для тестирования
    """
    example_data = [
        {
            "rank": 1,
            "name": "microsoft / vscode",
            "full_name": "microsoft/vscode",
            "stars": 150342,
            "url": "https://github.com/microsoft/vscode",
            "description": "Visual Studio Code"
        },
        {
            "rank": 2,
            "name": "facebook / react",
            "full_name": "facebook/react",
            "stars": 210987,
            "url": "https://github.com/facebook/react",
            "description": "A JavaScript library for building user interfaces"
        },
        {
            "rank": 3,
            "name": "tensorflow / tensorflow",
            "full_name": "tensorflow/tensorflow",
            "stars": 175432,
            "url": "https://github.com/tensorflow/tensorflow",
            "description": "An Open Source Machine Learning Framework for Everyone"
        }
    ]
    
    return example_data

def main():
    """
    Главная функция программы
    """
    print("=" * 50)
    print("ПРОГРАММА ДЛЯ СОХРАНЕНИЯ ДАННЫХ В JSON")
    print("=" * 50)
    
    # Создаем пример данных
    print("\n📊 Создаю пример данных...")
    data = create_example_data()
    
    # Сохраняем данные
    filename = "data.json"
    if save_to_json(data, filename):
        print(f"\n📄 Файл {filename} создан успешно!")
        print("Содержимое файла можно посмотреть в папке task_3")
    
    print("\n" + "=" * 50)
    print("Задание 3 выполнено успешно!")
    print("=" * 50)

if name == "main":
    main()"""
Задание 3: Сохранение данных в JSON
Программа сохраняет данные в файл data.json
"""

import json
import os
from datetime import datetime

def save_to_json(data, filename="data.json"):
    """
    Сохраняет данные в JSON файл
    """
    print(f"💾 Сохраняю данные в файл {filename}...")
    
    try:
        # Создаем структуру данных
        json_data = {
            "metadata": {
                "source": "GitHub Trending",
                "url": "https://github.com/trending",
                "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "total_repositories": len(data)
            },
            "repositories": data
        }
        
        # Сохраняем в файл
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(json_data, file, ensure_ascii=False, indent=2)
        
        print(f"✅ Данные успешно сохранены в {filename}")
        print(f"📊 Сохранено репозиториев: {len(data)}")
        
        return True
        
    except Exception as e:
        print(f"❌ Ошибка при сохранении: {e}")
        return False

def load_from_json(filename="data.json"):
    """
    Загружает данные из JSON файла
    """
    print(f"📂 Загружаю данные из файла {filename}...")
    
    try:
        if not os.path.exists(filename):
            print(f"❌ Файл {filename} не найден")
            return None
        
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        print(f"✅ Данные успешно загружены")
        return data
        
    except Exception as e:
        print(f"❌ Ошибка при загрузке: {e}")
        return None

def create_example_data():
    """
    Создает пример данных для тестирования
    """
    example_data = [
        {
            "rank": 1,
            "name": "microsoft / vscode",
            "full_name": "microsoft/vscode",
            "stars": 150342,
            "url": "https://github.com/microsoft/vscode",
            "description": "Visual Studio Code"
        },
        {
            "rank": 2,
            "name": "facebook / react",
            "full_name": "facebook/react",
            "stars": 210987,
            "url": "https://github.com/facebook/react",
            "description": "A JavaScript library for building user interfaces"
        },
        {
            "rank": 3,
            "name": "tensorflow / tensorflow",
            "full_name": "tensorflow/tensorflow",
            "stars": 175432,
            "url": "https://github.com/tensorflow/tensorflow",
            "description": "An Open Source Machine Learning Framework for Everyone"
        }
    ]
    
    return example_data

def main():
    """
    Главная функция программы
    """
    print("=" * 50)
    print("ПРОГРАММА ДЛЯ СОХРАНЕНИЯ ДАННЫХ В JSON")
    print("=" * 50)
    
    # Создаем пример данных
    print("\n📊 Создаю пример данных...")
    data = create_example_data()
    
    # Сохраняем данные
    filename = "data.json"
    if save_to_json(data, filename):
        print(f"\n📄 Файл {filename} создан успешно!")
        print("Содержимое файла можно посмотреть в папке task_3")
    
    print("\n" + "=" * 50)
    print("Задание 3 выполнено успешно!")
    print("=" * 50)

if name == "main":
    main()
