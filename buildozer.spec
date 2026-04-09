[app]
title = Conciergerie App
package.name = conciergerie
package.domain = org.demo
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
# On inclut PyMySQL pour la BDD
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pymysql

# iOS Specific
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
target = ios