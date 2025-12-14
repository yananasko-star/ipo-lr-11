}}
        
        .source-link:hover {{
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(72, 187, 120, 0.4);
        }}
        
        .footer {{
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #e2e8f0;
            color: #718096;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 GitHub Trending Repositories</h1>
            <div class="subtitle">Самые популярные репозитории на GitHub</div>
        </div>
        
        <div class="info-box">
            📊 Всего репозиториев: {data['metadata']['total_repositories']} | 
            📅 Дата обновления: {data['metadata']['collected_at']}
        </div>
        
        <table>
            <thead>
                <tr>
                    <th class="rank">#</th>
                    <th>Репозиторий</th>
                    <th>Описание</th>
                    <th class="stars">⭐ Звезды</th>
                </tr>
            </thead>
            <tbody>
'''
    
    # Добавляем строки с репозиториями
    for repo in data['repositories']:
        html += f'''                <tr>
                    <td class="rank">{repo['rank']}</td>
                    <td>
                        <a href="{repo['url']}" target="_blank" class="repo-link">
                            <span class="repo-name">{repo['name']}</span>
                        </a>
                    </td>
                    <td>{repo['description']}</td>
                    <td class="stars">{repo['stars']:,} ⭐</td>
                </tr>
'''
    
    # Закрываем HTML
    html += f'''            </tbody>
        </table>
        
        <div style="text-align: center; margin-top: 30px;">
            <a href="{data['metadata']['url']}" target="_blank" class="source-link">
                📊 Посмотреть на GitHub
            </a>
        </div>
        
        <div class="footer">
            Страница сгенерирована автоматически • {datetime.now().year}
        </div>
    </div>
</body>
</html>'''
    
    return html

def save_html(html_content, filename="index.html"):
    """
    Сохраняет HTML в файл
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(html_content)
        return True
    except Exception as e:
        print(f"❌ Ошибка сохранения HTML: {e}")
        return False

def main():
    """
    Главная функция программы
    """
    print("Генератор HTML страницы для GitHub Trending")
    
    # Загружаем данные
    print("Загружаю данные из JSON...")
    data = load_json_data()
    
    if not data:
        print("Не удалось загрузить данные")
        return
    
    # Генерируем HTML
    print("Генерирую HTML страницу...")
    html_content = generate_html(data)
    
    if not html_content:
        print("Не удалось сгенерировать HTML")
        return
    
    # Сохраняем HTML
    filename = "index.html"
    if save_html(html_content, filename):
        print(f"HTML страница сохранена: {filename}")
    else:
        print("Не удалось сохранить HTML страницу")

if name == "main":
    main()
