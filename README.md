
### План по решению задачи
1. **Авторизация и доступ к Google Drive**
   - Создать сервисный аккаунт в Google Cloud.
   - Скачать `credentials.json`.
   - Дать сервисному аккаунту доступ к нужному Excel-файлу в Google Drive.

2. **Чтение Excel-файла**
   - Использовать Google Drive API для скачивания файла.
   - Прочитать его.

3. **Нормализация данных**
   - Убедиться, что таблица содержит нужные колонки:
     - `Название инструмента`
     - `Ссылка на раздел`
   - Проверить дубликаты и пустые значения.
   - Сохранить в удобный формат (JSON).

4. **Подготовка к интеграции**
   - Сделать REST-эндпоинт `/agent/chat` на FastAPI.
   - Возвращать данные в JSON для дальнейшего использования в Open WebUI.

---

### Шаги реализации
1. Создать сервисный аккаунт в Google Cloud и скачать `credentials.json`.  
2. Дать этому аккаунту доступ к Excel-файлу на Google Drive.  
3. Подключить библиотеки  
4. Реализовать маршрут `/agent/chat` в FastAPI для чтения данных.  


### Для запуска
1. добавить .env с ключом для openai OPENAI_API_KEY=sk-....
2. положить свой credentials.json в корень
3. добавить env.example 

OPENAI_API_KEY=sk-
OPENAI_MODEL=gpt-4o-mini

**#Google service account (имя файла ключа)**

GOOGLE_APPLICATION_CREDENTIALS=credentials.json
