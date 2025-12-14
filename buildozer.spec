[app]
title = Mobile App 001
package.name = mobileapp001
package.domain = org.example
version = 0.1
source.dir = .
source.include_exts = py,kv,png,jpg
pre_build_cmd = /bin/bash -c "cd .buildozer/android/platform/build-{arch}/build/other_builds/libffi/{arch}__ndk_target_21/libffi && autoreconf -fiv"

orientation = portrait
fullscreen = 0

# Только одна архитектура — экономим место
android.archs = arm64-v8a


# API
android.api = 34
android.minapi = 21

# Ключевое: NDK r25b
android.ndk = 25b

# Bootstrap
p4a.bootstrap = sdl2

# Современные требования
requirements = python3,kivy,pyjnius

# Ускорение сборки
p4a.ignore_setup_py = True
p4a.args = --ignore-setup-py

[buildozer]
log_level = 2
platform = android


