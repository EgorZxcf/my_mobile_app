import os
import sys

# Пробуем импортировать FastAPI и Uvicorn
try:
    from fastapi import FastAPI
    import uvicorn
    
    app = FastAPI()

    @app.get("/")
    def read_root():
        return {"status": "working", "message": "AI Chat Backend is running successfully!"}

    @app.post("/chat")
    def chat_endpoint(data: dict):
        user_message = data.get("message", "")
        return {"response": f"Сервер онлайн! Получено сообщение: {user_message}"}

except ImportError as e:
    print(f"Ошибка импорта зависимостей: {e}")
    sys.exit(1)

if __name__ == "__main__":
    # Render всегда передает порт в переменную окружения PORT
    port = int(os.environ.get("PORT", 8000))
    print(col := f"Старт сервера на порту {port}...")
    
    # Запускаем uvicorn напрямую через python-код
    uvicorn.run(app, host="0.0.0.0", port=port)
