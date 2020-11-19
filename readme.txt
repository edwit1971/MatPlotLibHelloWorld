KivyMD #257 Bug vs MatPlotLib, one or the other???

There is a BUG in KivyMD #257 regarding icons showing on the PC when you run your App but after building with BUILDOZER the icons no longer show in the App when you run it. The solution was to go to the Python-4-Android Repository on Github and FORK it, etc.
Then you now have two lines you have to add in your Buildozer.spec file:

(comment out) (str) python-for-android fork to use, defaults to upstream (kivy)
p4a.fork = (your username)

(comment out) (str) python-for-android branch to use, defaults to master
p4a.branch = develop

Here's the problem...
When you do the above to fix the Icon-Bug-Problem in KivyMD, you now create a NEW Bug where MatPlotLib will not compile.

I have a sample project, 1 file, main.py, that is a Hello-World-MatPlotLib program in a Public Repository on GitHub:
https://github.com/edwit1971/MatPlotLibHelloWorld

in the Buildozer.spec file if you do NOT comment these two lines out:
p4a.fork = (your username)
p4a.branch = develop

and type: buildozer android debug

you will get a MatPlotLib error and it won't compile an APK file.

if you comment these two lines out:
(comment out) p4a.fork = (your username)
(comment out) p4a.branch = develop

it will compile an APK file.

So you get one or the other but not both?

run: buildozer android debug
https://github.com/edwit1971/MatPlotLibHelloWorld

