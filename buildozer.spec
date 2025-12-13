[app]
title = Mobile App 001
package.name = mobileapp001
package.domain = org.example

source.dir = .
version = 0.1
requirements = python3,kivy,numpy,sounddevice,pyjnius

fullscreen = 0
orientation = portrait
android.api = 34
android.minapi = 21
android.ndk_api = 21

p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1
platform = android


