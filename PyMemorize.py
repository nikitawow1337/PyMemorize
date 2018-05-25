__author__ = "nikitawow"
__copyright__ = "Copyright (C) 2018 Bazhenov Nikita"
__license__ = "GNU General Public License v3.0"
__version__ = "1.0"

import random


class Dict:
    dict_path = ""
    dict_name = ""
    dict1 = list()
    dict2 = list()
    words = 0


def __init__():
    parse()


def parse(*path):
    Dict.dict_path = "dict-example.txt"
    if path and path != ():
        Dict.dict_path = path[0]
    print("file_path: ", Dict.dict_path)
    f = open(file=Dict.dict_path, mode="r")

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
        else:
            print("Cannot find '\t' in line", Dict.words + 1)
            return
        Dict.words += 1

    f.close()

    print("First dictionary: ", Dict.dict1)
    print("Second dictionary: ", Dict.dict2)
    print(Dict.words)


def srandom(percentage):
    samplerand = random.sample(list(range(0, Dict.words)), int(Dict.words * percentage))
    print("Sample length: ", len(samplerand))
    return samplerand


def memorize(x):
    index = 1
    for i in x:
        print(index, Dict.dict2[i], "-", Dict.dict1[i])
        input()
        index += 1


def check(x):
    correct = 0
    for i in x:
        print("Word: ", Dict.dict2[i])
        s = input()
        if s == Dict.dict1[i]:
            correct += 1
            print("+ ", Dict.dict1[i])
        else:
            print("- ", Dict.dict1[i])

    for i in x:
        print(Dict.dict2[i], " - ", Dict.dict1[i])

    print("Correct: ", correct, "/", x.__len__())


def dic_name():
    print("Dictionary name: ", Dict.dict_name)


def dic_words():
    print("Words in dictionary: ", Dict.words)


def dic_swap():
    Dict.dict1, Dict.dict2 = Dict.dict2, Dict.dict1
    print("Swapped..\nDict1: ", Dict.dict1, "\nDict2: ", Dict.dict2)


def dic_load():
    s = input()
    parse(s)


def play_memorization_game():
    print("Percentage?")
    s = float(input())
    x = srandom(s)
    memorize(x)


def play_test_your_skills_game():
    print("Percentage?")
    s = float(input())
    x = srandom(s)
    check(x)


def play_watch_and_learn_game():
    print("Percentage?")
    s = float(input())
    x = srandom(s)
    memorize(x)
    for _ in x:
        print("|\n")
    check(x)


def enter(argument):
    if argument == '1':
        dic_name()
    elif argument == '2':
        dic_words()
    elif argument == '3':
        dic_swap()
    elif argument == '4':
        dic_load()
    elif argument == '5':
        play_memorization_game()
    elif argument == '6':
        play_test_your_skills_game()
    elif argument == '7':
        play_watch_and_learn_game()
    elif argument == '0':
        exit(0)


def menu():
    while True:
        print("Menu:\n"
            "1) Dictionary name\n"
            "2) Words in dictionary\n"
            "3) Swap dictionaries\n"
            "4) Load dictionary\n"
            "5) Play 'Memorization' game\n"
            "6) Play 'Test your skills' game\n"
            "7) Play 'Watch and learn' game\n"
            "0) Exit\n"
            "Enter: ")
        s = input()
        enter(s)
        print("Press any button to continue...")
        input()


def main():
    __init__()
    menu()


if __name__ == '__main__':
    main()
