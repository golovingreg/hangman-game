import time
from hangman import Hangman


print("""

##     ##    ###    ##    ##  ######   ##     ##    ###    ##    ## 
##     ##   ## ##   ###   ## ##    ##  ###   ###   ## ##   ###   ## 
##     ##  ##   ##  ####  ## ##        #### ####  ##   ##  ####  ## 
######### ##     ## ## ## ## ##   #### ## ### ## ##     ## ## ## ## 
##     ## ######### ##  #### ##    ##  ##     ## ######### ##  #### 
##     ## ##     ## ##   ### ##    ##  ##     ## ##     ## ##   ### 
##     ## ##     ## ##    ##  ######   ##     ## ##     ## ##    ## 

""")

print("\nWelcome to Hangman game\n")
print("The game was originally made by DataFlair website,")
print("but I added some improvements\n")

lang: str
name: str
difficulty: str


def init():
    global lang
    global difficulty
    global name
    lang = input("For English enter 'en'/Для русского языка, введите 'ru': ")
    if lang == "ru":
        name = input("Введите ваше имя: ")
    elif lang == "en":
        name = input("Enter your name: ")
    else:
        print("Wrong language, enter again/Неправильный язык, повторите ввод")
        init()

# TODO: change difficulty and language without restart

    if lang == "ru":
        print("Приветствую, " + name + "!")
        difficulty = input("Выберите сложность: л - легко, с - средне, т - трудно: ")
        while difficulty not in ["л", "с", "т"]:
            difficulty = input("Выберите сложность: л - легко, с - средне, т - трудно: ")

        print("Правила просты:")
        print("Вам необходимо угадать слово буква за буквой. Если выбрять пять неверных букв, вас повесят.")
        print("Чтобы остановить игру, напишите 'стоп'.\n")
        time.sleep(1)
        print("Игра начинается!\n")
        time.sleep(1)

    elif lang == "en":
        print("Hello, " + name + "!")
        difficulty = input("Choose your difficulty: e - easy, m - medium, h - hard: ")
        while difficulty not in ["e", "m", "h"]:
            difficulty = input("Choose your difficulty: e - easy, m - medium, h - hard: ")

        print("The rules are simple:")
        print("You must guess a word letter by letter. If you choose 5 wrong letters, you'll get hung.")
        print("To give up, type 'stop'.\n")
        time.sleep(1)
        print("The game is about to start!\nLet's play Hangman!\n")
        time.sleep(1)

    return lang, difficulty


[lang, difficulty] = init()

hangman = Hangman(lang, difficulty)

hangman.main()

hangman.game()
