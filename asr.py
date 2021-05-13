from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5 import QtMultimedia
from PyQt5.QtCore import QUrl
import time
import difflib
import random
import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from asrInterface import *
import sys
import threading

import speech_recognition as sr

r = sr.Recognizer()


def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()


class myWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(myWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('icon/phone.png'))

    def cmd_recognition(self):

        # 在定时器执行函数内部重复构造定时器
        global timer
        timer = threading.Timer(10, self.cmd_recognition)
        timer.start()
        print("She is waiting to be woken")

        # Working with Microphones
        mic = sr.Microphone()

        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)  # 直到检测到静音时自动停止

        try:
            command = r.recognize_sphinx(audio)
        except:
            print("Unable to read content")
        else:
            print("Command: " + command)
            global similar
            similar = string_similar(command, "hey")
            print("Similarity: ", similar)

            if similar > 0.1:
                self.WakeSuccess()
            else:
                print("She is still asleep")

    def WakeSuccess(self):
        print("She is awake and waiting for order")

        self.label.setVisible(False)
        self.label_2.setVisible(True)

        file = QUrl.fromLocalFile('audio/welcome.wav')  # 音频文件路径
        content = QtMultimedia.QMediaContent(file)
        player = QtMultimedia.QMediaPlayer()
        player.setMedia(content)
        player.setVolume(50)
        player.play()
        time.sleep(2)

        global timer
        timer.cancel()
        # self.label_7.setVisible(False)
        # self.label_8.setVisible(False)
        # self.label_10.setVisible(True)
        # self.label_11.setVisible(True)

        mic = sr.Microphone()
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        try:
            command = r.recognize_sphinx(audio)
        except:
            print("Unable to read content")
        else:
            print("Command: " + command)
            cmd_list = [string_similar(command, "play"),
                        string_similar(command, "note"),
                        string_similar(command, "calculate")]

            max_value = max(cmd_list)  # 最大值
            max_index = cmd_list.index(max_value)  # 最大值的索引

            if max_index == 0:
                os.startfile(r"audio\music.mp3")
            elif max_index == 1:
                os.system("C:\\Windows\\System32\\notepad.exe")
            elif max_index == 2:
                os.system("C:\\Windows\\System32\\calc.exe")

        print("Cooling down")
        time.sleep(6.1)

        self.label.setVisible(True)
        self.label_2.setVisible(False)
        # self.label_7.setVisible(True)
        # self.label_8.setVisible(True)
        # self.label_10.setVisible(False)
        # self.label_11.setVisible(False)
        timer = threading.Timer(0.1, self.cmd_recognition)
        timer.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    application = myWindow()
    application.show()

    timer = threading.Timer(0.1, application.cmd_recognition)  # 第一次执行0.1s后开始
    timer.start()

    sys.exit(app.exec_())
