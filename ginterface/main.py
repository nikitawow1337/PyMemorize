import sys
import random
import json

from PySide2.QtCore import QObject, Signal, Property, QUrl
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine


class Dict:
    dict_path = ""
    dict_name = ""
    dict1 = list()
    dict2 = list()
    len1 = list()
    len2 = list()
    words = 0
    randst = True
    cur = 0


def load_config():
    with open("config.json", "r") as write_file:
        d = json.loads(write_file, encoding="utf-8")
    print(d)


def randomize():
    # percentage = float(input("Enter sample percentage"))
    percentage = 1
    samplerand = random.sample(list(range(0, Dict.words)), int(Dict.words * percentage))
    print("Sample length: ", len(samplerand))
    print("Samplerand: ", samplerand)
    # randomize
    temp1 = Dict.dict1
    temp2 = Dict.dict2
    for i in range(len(samplerand)):
        Dict.dict1.insert(i, temp1[samplerand[i]])
        Dict.dict2.insert(i, temp2[samplerand[i]])


def parse(*path):
    # Dict.dict_path = "dictionaries/dict3000rev.txt"
    Dict.dict_path = "jap-dir.txt"
    if path and path != ():
        Dict.dict_path = path[0]
    print("file_path: ", Dict.dict_path)
    f = open(file=Dict.dict_path, mode="r", encoding="utf-8")

    Dict.dict_name = f.readline()[:-1]

    tab = "\t"

    if Dict.dict1 or Dict.dict2:
        Dict.dict1[:] = []
        Dict.dict2[:] = []
        Dict.words = 0

    for line in f:
        if tab in line:
            # new_line = line.find(tab)
            # new_line = line[new_line:]
            if line[-1] == "\n":
                line = line[0:-1]
            Dict.dict1.append(line[line.find(tab) + 1:])
            Dict.dict2.append(line[:line.find(tab)])
            # extra
            Dict.len1.append(len(line[line.find(tab) + 1:]))
            Dict.len2.append(len(line[:line.find(tab)]))
        else:
            print("Cannot find '\t' in line", Dict.words + 1)
            return
        Dict.words += 1

    f.close()

    print("First dictionary: ", Dict.dict1)
    print("First length: ", Dict.len1)
    print("Second dictionary: ", Dict.dict2)
    print("Second length: ", Dict.len2)
    print(Dict.words)


class Backend(QObject):
    textChanged = Signal(str)

    def changed(self):
        print("changed")
        if len(self.m_text2) == self.m_len2:
            if self.m_text2 == Dict.dict2[Dict.cur]:
                Dict.cur += 1
                print(Dict.cur)
                # ++
            else:
                self.m_red = 1
        else:
            self.m_red = 0
        return 1

    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self.m_text1 = Dict.dict1[Dict.cur]
        self.m_text2 = Dict.dict2[Dict.cur]

        self.m_cur = 0
        self.m_word = ""

        self.m_len1 = str(len(Dict.dict1[Dict.cur]))
        self.m_len2 = str(len(Dict.dict2[Dict.cur]))
        print(self.m_len1, self.m_len2)

        self.m_red = str(0)

    @Property(str, notify=textChanged)
    def text1(self):
        return self.m_text1

    @Property(str, notify=textChanged)
    def text2(self):
        return self.m_text2

    @Property(str, notify=textChanged)
    def word(self):
        return self.m_word

    @Property(str, notify=textChanged)
    def len1(self):
        return self.m_len1

    @Property (str, notify=textChanged)
    def len2(self):
        return self.m_len2

    @Property(str, notify=textChanged)
    def red(self):
        return self.m_red

    @Property(str, notify=textChanged)
    def cur(self):
        return str(self.m_cur + 1)


    @word.setter
    def setText(self, word):
        if self.m_word == word:
            return
        self.m_word = word
        self.textChanged.emit(self.m_word)
        # print("LEN: ", len(self.m_word), len(Dict.dict2[Dict.cur]))
        if len(self.m_word) == len(Dict.dict2[Dict.cur]):
            if self.m_word == Dict.dict2[Dict.cur]:
                # m_cur in case of order (or random)
                self.m_cur += 1
                if self.m_cur == Dict.words:
                    self.m_cur = 0
                Dict.cur = self.m_cur
                self.m_text1 = Dict.dict1[Dict.cur]
                self.m_text2 = Dict.dict2[Dict.cur]
                self.m_len1 = str(len(Dict.dict1[Dict.cur]))
                self.m_len2 = str(len(Dict.dict2[Dict.cur]))
                self.m_word = ""
                self.m_red = str(0)
            else:
                self.m_red = str(1)
        else:
            self.m_red = str(0)


def __init__():
    load_config()
    parse()
    randomize()


if __name__ == '__main__':
    __init__()
    app = QGuiApplication(sys.argv)
    backend = Backend()

    # backend.textChanged.connect(lambda text: print(text))
    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("backend", backend)
    engine.load(QUrl.fromLocalFile('main.qml'))
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
