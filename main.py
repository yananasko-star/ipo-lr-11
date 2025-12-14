"""
Лабораторная работа №11
Главный файл
"""

def main():
    print("Лабораторная работа №11")
    print("Работа с виртуальным окружением, пакетами и модулями")
    print("="*50)
    
    while True:
        print("\nВыберите задание:")
        print("1. Задание 1 - Виртуальное окружение")
        print("2. Задание 2 - Парсинг GitHub")
        print("3. Задание 3 - JSON файл")
        print("4. Задание 4 - HTML страница")
        print("5. Показать структуру")
        print("0. Выход")
        
        choice = input("\nВаш выбор: ").strip()
        
        if choice == '0':
            print("Выход")
            break
        elif choice == '1':
            print("\nЗадание 1: Виртуальное окружение")
            print("Файлы: task_1/requirements.txt")
            print("Файлы: task_1/venv_instruction.md")
        elif choice == '2':
            print("\nЗадание 2: Парсинг GitHub")
            print("Файлы: task_2/github_parser.py")
            print("Пример вывода: 1. Repository: microsoft / vscode; Stars: 150,342;")
        elif choice == '3':
            print("\nЗадание 3: JSON файл")
            print("Файлы: task_3/data.json")
            print("Файлы: task_3/json_saver.py")
        elif choice == '4':
            print("\nЗадание 4: HTML страница")
            print("Файлы: task_4/index.html")
            print("Файлы: task_4/generate_html.py")
        elif choice == '5':
            print("\nСтруктура проекта:")
            print("ipo-lr-11/")
            print("├── task_1/")
            print("├── task_2/")
            print("├── task_3/")
            print("├── task_4/")
            print("├── main.py")
            print("├── .gitignore")
            print("└── README.md")
        else:
            print("Неверный выбор")
        
        input("\nНажмите Enter...")

if name == "main":
    main()
