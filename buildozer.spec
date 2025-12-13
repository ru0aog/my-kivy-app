[app]
# Основная информация
title = Mobile App 001
package.name = mobileapp001
package.domain = org.example
version = 0.1
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Главный файл приложения (если не main.py — укажите)
# (по умолчанию — main.py, можно не указывать)

# Иконка и сплэш (рекомендуется добавить, чтобы не было ошибок)
# icon.filename = %(source.dir)s/icon.png
# splash.filename = %(source.dir)s/splash.png

# Ориентация и полноэкранный режим
orientation = portrait
fullscreen = 0

# Зависимости — упрощены для надёжной сборки
# numpy и sounddevice — тяжёлые, собираются долго и жрут место
requirements = python3,kivy,pyjnius

# ⚠️ ВАЖНО: sounddevice может не собираться или "вешать" процесс
# Если нужен — добавьте позже, отдельно, и только после проверки базовой сборки
# Для аудио на Android лучше использовать pyaudio или Android API через pyjnius

# Bootstrap — sdl2 подходит для Kivy
p4a.bootstrap = sdl2

# Архитектура: только arm64-v8a (экономит 50% места и времени)
# Раскомментируйте, если нужна поддержка старых устройств:
# android.arch = arm64-v8a,armeabi-v7a
android.arch = arm64-v8a

# API уровни
android.api = 34
android.minapi = 21
android.ndk = 23b
android.sdk = 34

# Режим отладки (для релиза: buildozer android release)
# debug = 1

# Уменьшаем размер APK: не копируем лишние файлы
p4a.ignore_setup_py = True
p4a.local_recipes = %(source.dir)s/recipes

# Дополнительные аргументы сборки
# (отключаем gdb — не нужен в CI)
p4a.args = --ignore-setup-py --no-compile-python-requirements

# Логирование
[buildozer]
log_level = 2
warn_on_root = 1

# Платформа
platform = android

# Указываем, что не нужно запускать приложение после установки (для CI)
buildozer.build_target = android

# Каталог сборки (можно очищать между запусками)
# build_dir = .buildozer

