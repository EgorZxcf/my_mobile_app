import os
import sys

# Проверяем наличие необходимых библиотек
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
        # Здесь будет логика обработки сообщения твоим ИИ
        return {"response": f"Получил твое сообщение: '{user_message}'. Сервер работает!"}

except ImportError as e:
    print(f"Критическая ошибка импорта: {e}")
    print("Убедитесь, что все зависимости указаны в requirements.txt")
    sys.exit(1)

if __name__ == "__main__":
    print("Инициализация запуска сервера на Render...")
    # Получаем порт от Render
    port = int(os.environ.get("PORT", 8000))
    
    # Запускаем сервер прямо из python-скрипта
    uvicorn.run(app, host="0.0.0.0", port=port)
