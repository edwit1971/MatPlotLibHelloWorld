############################################################
#
# App
#
############################################################

[app]

# (str) Title of your application
title = MPL_Hello

# (str) Package name
package.name = MatPlotLibHello

# (str) Package domain (needed for android/ios packaging)
package.domain = com.abc_apps

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py, png, atlas, db, ttf, md, json

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs = bin, __pycache__

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3==3.7.6, hostpython3==3.7.6, sqlite3, android, kivy==1.11.1, git+https://github.com/HeaTTheatR/KivyMD.git, pygments, matplotlib

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
#requirements.source.kivymd = ../../kivymd
requirements.source.kivymd = /home/edwit3/anaconda3/envs/myenv/lib/python3.7/site-packages/kivymd

# (list) Garden requirements
#garden_requirements = matplotlib

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/images/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/images/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = all


############################################################
#
# OSX Specific
#
############################################################

# author = © Copyright Info

# change the major version of python used by the app
osx.python_version = 3

# Kivy version to use
osx.kivy_version = 1.9.1


############################################################
#
# Android specific
#
############################################################

# (bool) Indicate if the application should be fullscreen or not
fullscreen = True

# (list) Permissions
android.permissions = WRITE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 29

# (int) Minimum API your APK will support. 21 = Lollipop v5.0
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 19c

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.arch = armeabi-v7a


############################################################
#
# Python for android (p4a) specific
#
############################################################

# (str) python-for-android fork to use, defaults to upstream (kivy)
#p4a.fork = edwit1971

# (str) python-for-android branch to use, defaults to master
#p4a.branch = develop


############################################################
#
# iOS specific
#
############################################################

# (str) Path to a custom kivy-ios folder
#ios.kivy_ios_dir = ../kivy-ios
# Alternately, specify the URL and branch of a git checkout:
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

# Another platform dependency: ios-deploy
# Uncomment to use a custom checkout
#ios.ios_deploy_dir = ../ios_deploy
# Or specify URL and branch
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.7.0


############################################################
#
# Buildozer
#
############################################################

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

