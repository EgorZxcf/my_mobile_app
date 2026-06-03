[app]
title = AI Chat
package.name = aichat
package.domain = org.test

# Ссылка на исходный код
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Версии компонентов (Стабильный стек для Android)
version = 0.1
requirements = python3,kivy==2.3.0,kivymd==1.2.0,requests,urllib3,certifi

# Настройки экрана
orientation = portrait
fullscreen = 0

# Разрешения и системные настройки
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk_api = 21

# Архитектуры процессоров (ВАЖНО: arm64-v8a обязателен для новых Android)
android.archs = arm64-v8a, armeabi-v7a

# Включаем логирование ошибок p4a
android.logcat_filters = *:S python:D

[buildozer]
log_level = 2
warn_on_root = 1
