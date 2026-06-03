import sys
import os

# Сразу перехватываем любые ошибки импорта и пишем в лог, чтобы приложение не вылетало молча
try:
    from kivy.app import App
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.label import Label
    from kivy.uix.textinput import TextInput
    from kivy.uix.button import Button
    from kivy.uix.scrollview import ScrollView
    from kivy.network.urlrequest import UrlRequest
    import json
except Exception as e:
    # Если даже Kivy не может загрузиться, запишем в файл лога
    with open("critical_error.txt", "w") as f:
        f.write(str(e))
    sys.exit(1)

class ChatScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)
        
        # Окно истории чата
        self.scroll = ScrollView(size_hint=(1, 0.8))
        self.chat_history = Label(
            text="[System]: Добро пожаловать в ИИ Чат!\n", 
            markup=True, 
            size_hint_y=None, 
            halign='left', 
            valign='top'
        )
        self.chat_history.bind(texture_size=self.chat_history.setter('size'))
        self.scroll.add_widget(self.chat_history)
        self.add_widget(self.scroll)
        
        # Поле ввода и кнопка
        input_layout = BoxLayout(size_hint=(1, 0.2), spacing=10)
        self.user_input = TextInput(hint_text="Введите сообщение...", multiline=False)
        send_btn = Button(text="Отправить", size_hint=(0.3, 1))
        send_btn.bind(on_press=self.send_message)
        
        input_layout.add_widget(self.user_input)
        input_layout.add_widget(send_btn)
        self.add_widget(input_layout)

    def send_message(self, instance):
        text = self.user_input.text.strip()
        if text:
            self.chat_history.text += f"\n[Вы]: {text}"
            self.user_input.text = ""
            
            # Отправка запроса на твой Render-сервер
            # Использование UrlRequest из Kivy НЕ блокирует главный поток (приложение не зависнет)
            url = "https://my-unique-ai-chat.onrender.com/chat"
            headers = {'Content-Type': 'application/json'}
            data = json.dumps({"message": text})
            
            UrlRequest(
                url, 
                req_body=data, 
                req_headers=headers,
                on_success=self.on_api_success, 
                on_failure=self.on_api_failure, 
                on_error=self.on_api_error
            )

    def on_api_success(self, req, result):
        response_text = result.get("response", "Пустой ответ")
        self.chat_history.text += f"\n[ИИ]: {response_text}"

    def on_api_failure(self, req, result):
        self.chat_history.text += f"\n[Ошибка сервера]: Код {req.resp_status}"

    def on_api_error(self, req, error):
        self.chat_history.text += f"\n[Ошибка сети]: Не удалось связаться с сервером"


class AIChatApp(App):
    def build(self):
        try:
            return ChatScreen()
        except Exception as e:
            # Если упадет инициализация интерфейса, покажем текст ошибки вместо вылета
            box = BoxLayout()
            box.add_widget(Label(text=f"Критическая ошибка интерфейса:\n{str(e)}"))
            return box

if __name__ == "__main__":
    try:
        AIChatApp().run()
    except Exception as main_error:
        with open("main_crash.txt", "w") as f:
            f.write(str(main_error))
