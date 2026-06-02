from flask import Flask, request, jsonify
from flask_cors import CORS  # Нужен, чтобы мобильное приложение могло делать запросы к серверу
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)  # Разрешаем запросы со всех устройств (включая твой телефон)

ai_client = OpenAI(
    api_key=os.getenv("AI_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

# Проверочный маршрут, чтобы убедиться, что сервер на Render работает
@app.route('/')
def home():
    return "AI Chat Backend is running on Render!"

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({'response': 'Сообщение не может быть пустым.'}), 400

    try:
        chat_completion = ai_client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "https://render.com",
                "X-Title": "AI Mobile Chat",
            },
            messages=[
                {"role": "system", "content": "Ты полезный ИИ-ассистент в мобильном приложении."},
                {"role": "user", "content": user_message}
            ],
            model="openrouter/auto", 
        )
        ai_response = chat_completion.choices[0].message.content
        
    except Exception as e:
        print(f"Ошибка API: {e}")
        ai_response = f"Ошибка сервера: {e}"

    return jsonify({'response': ai_response})

if __name__ == '__main__':
    # Локальный запуск для тестов
    app.run(host='0.0.0.0', port=8080)
