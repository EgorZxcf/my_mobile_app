[app]
# Название твоего приложения в меню телефона
title = My Mobile App

# Имя пакета (уникальный ID для Play Market, только латиница и точки)
package.name = my_mobile_app
package.domain = org.example

# Папка, где лежит исходный код (мы создавали src)
source.dir = src

# Какие расширения файлов включать в сборку
source.include_exts = py,html,js,css,png,jpg

# Версия приложения
version = 0.1

# Какие библиотеки нужны для работы приложения (requirements)
# Нам пока нужен только python3
requirements = python3, kivy

# Ориентация экрана (portrait, landscape или all)
orientation = portrait

# (Раздел для Android)
fullscreen = 0
android.archs = armeabi-v7a, arm64-v8a
android.allow_backup = True
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/27.3.13750724

# (list) Permissions
android.permissions = INTERNET
