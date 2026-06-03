import os
import sys

# Пример базового сервера (если у тебя FastAPI/Flask)
# Если у тебя другой фреймворк, этот блок инициализации адаптируется,
# но главное — блок запуска в самом низу файла!

try:
    from fastapi import FastAPI
    import uvicorn
    app = FastAPI()
    
    @app.get("/")
    def read_root():
        return {"status": "working", "message": "AI Chat Backend is running!"}
        
    @app.post("/chat")
    def chat_endpoint(data: dict):
        # Логика твоего ИИ-чата
        return {"response": "Привет! Я твой ИИ-ассистент."}
except ImportError:
    # Если это простой скрипт на Flask или бот
    app = None

if __name__ == "__main__":
    print("Запуск сервера...")
    # Render передает порт в переменную окружения PORT. 
    # Если ее нет (запуск на телефоне), используем 8000 по умолчанию.
    port = int(os.environ.get("PORT", 8000))
    
    # Если используем uvicorn (FastAPI)
    if 'uvicorn' in sys.modules and app:
        uvicorn.run(app, host="0.0.0.0", port=port)
    else:
        # Резервный вариант, если это другой скрипт
        print(sys.argv)
        # Если у тебя здесь был свой специфичный запуск бота/сервера, 
        # убедись, что он слушает host 0.0.0.0 и динамический port
