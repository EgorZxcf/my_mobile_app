from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

app = Flask(__name__, 
            template_folder='www', 
            static_folder='www', 
            static_url_path='')

# НАСТРОЙКА ПОД OPENROUTER
ai_client = OpenAI(
    api_key=os.getenv("AI_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({'response': 'Сообщение не может быть пустым.'}), 400

    try:
        # Запрос к OpenRouter
        chat_completion = ai_client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "http://localhost:8080",
                "X-Title": "AI Chat App",
            },
            messages=[
                {
                    "role": "system",
                    "content": "Ты полезный и вежливый ИИ-ассистент в мобильном приложении. Отвечай кратко и дружелюбно на языке пользователя."
                },
                {
                    "role": "user",
                    "content": user_message,
                }
            ],
            # Используем универсальный роутер OpenRouter, который сам подберет доступную модель, 
            # либо можешь попробовать конкретную актуальную "google/gemma-2-9b-it:free"
            model="openrouter/auto", 
        )
        ai_response = chat_completion.choices[0].message.content
        
    except Exception as e:
        print(f"Ошибка API: {e}")
        ai_response = f"Извини, возникла ошибка при запросе к OpenRouter. Ошибка: {e}"

    return jsonify({'response': ai_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
