[app]
title = Мой первый APK
package.name = firstapp
package.domain = org.example

source.dir = .
source.include_exts = py
version = 0.1
requirements = python3,kivy==2.3.1

orientation = portrait
android.permissions = INTERNET
android.api = 34
android.minapi = 21
android.ndk = 25b
android.sdk = 34
android.arch = arm64-v8a
android.bootstrap = sdl2

[buildozer]
log_level = 2
bin_dir = .
