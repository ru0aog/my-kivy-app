[app]
title = Mobile App 001
package.name = mobileapp001
package.domain = org.example

source.dir = .
version = 0.1
requirements = python3,kivy==2.3.1

osx.python_version = 3
osx.kivy_version = 2.3.1

fullscreen = 0
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
warn_on_root = 1

