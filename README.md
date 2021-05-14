# Voice Recognition Assistant

1852141 Li Detao

Human-Computer Interaction Assignment 1, 2021 Spring

Github: https://github.com/needle1989/Voice-Assistant

[TOC]

## Environment

* Please note that the project is in Project.zip and it may be better to run program contained in which if you want to run Glados.

* How to install Glados?

  Unzip source code and run asr.py. Make sure Qt Designer version matches PyQt5.

* Necessary Packages:

  PyQt5

  pyqt5-tools

  Qt Designer

  PyAudio

  PocketSphinx

  SpeechRecognition

* The program is developed by PyCharm.

## User Walkthrough

* Welcome UI:

  <img src="README.assets/image-20210514103000179.png" alt="image-20210514103000179" style="zoom:50%;" />

  Once open Glados, she will be waiting for wake word "hey". I choose this word so chances for her to wake are greatly improved.

* Woken UI:

  <img src="README.assets/image-20210514103703345.png" alt="image-20210514103703345" style="zoom:50%;" />

  Once wakened, Glados will say a welcome message and wait for further instruction. Three commands are installed as following: play some music, open note book and open calculator. The voice recognition model I'm using is not accurate so the command is set to be as simple as it can be. 

  | COMMAND   | Function            |
  | --------- | ------------------- |
  | hey       | Wake Glados up      |
  | play      | Play some music     |
  | note      | Open the note book  |
  | calculate | Open the calculator |

## Function Implementation

* def cmd_recognition

  The main logic is to monitor voice input constantly for wake word and after waken procedure, commands.

  ```python
  global timer
  timer = threading.Timer(10, self.cmd_recognition)
  timer.start()
  print("She is waiting to be woken")
  ```

  To recognize commands more accurately, I use a  similarity function to determine which command is more likely to be the correct one.

  ```python
  return difflib.SequenceMatcher(None, s1, s2).quick_ratio()
  ```

* def audio_play

  ```python
  file = QUrl.fromLocalFile('audio/welcome.wav')  # Audio source
  content = QtMultimedia.QMediaContent(file)
  player = QtMultimedia.QMediaPlayer()
  player.setMedia(content)
  player.setVolume(50)
  player.play()
  time.sleep(2)
  ```

* def waken_success

  To avoid multiple wrongly recognized commands execution, I use a cool-down procedure which locks the program for 2 seconds and make Glados asleep again until the next wake word recognized. 

  ```python
  print("Cooling down")
  time.sleep(6.1)
  self.label.setVisible(True)
  self.label_2.setVisible(False)
  timer = threading.Timer(0.1, self.cmd_recognition)
  timer.start()
  ```

## Accuracy and Possible Improvement

* The model I'm using does not perform well in voice recognition. The accuracy is practically terrible. To improve accuracy, it may be better that I try another voice recognition API like Baidu API or Google API.

