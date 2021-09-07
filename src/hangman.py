import random
import time
import words


class Hangman:
    lang: str
    difficulty: str
    words_to_guess: list[str]
    count: int
    display: str
    word: str
    already_tried: []
    length: int
    play_game: str

    def __init__(self, lang: str, diff: str):
        self.lang = lang
        self.difficulty = diff
        if self.lang == "en":
            if self.difficulty in ["e", "E"]:
                self.words_to_guess = words.words_en_easy
            elif self.difficulty in ["m", "M"]:
                self.words_to_guess = words.words_en_medium
            elif self.difficulty in ["h", "H"]:
                self.words_to_guess = words.words_en_hard
            else:
                print("Invalid difficulty chosen. Default difficulty is 'Hard'")
                self.words_to_guess = words.words_en_hard
        elif self.lang == "ru":
            if self.difficulty in ["л", "Л"]:
                self.words_to_guess = words.words_ru_easy
            elif self.difficulty in ["с", "С"]:
                self.words_to_guess = words.words_ru_medium
            elif self.difficulty in ["т", "Т"]:
                self.words_to_guess = words.words_ru_hard
            else:
                print("Выбрана неверная сложность. Сложность по умолчанию - 'трудно'")
                self.words_to_guess = words.words_en_hard

    def main(self):
        self.word = random.choice(self.words_to_guess)
        self.length = len(self.word)
        self.count = 0
        self.display = '_' * self.length
        self.already_tried = []
        self.play_game = ""
        self.game()

    def play_loop(self):
        if self.lang == "ru":
            self.play_game = input("Хотите сыграть снова? д = да, н = нет \n")
        else:
            self.play_game = input("Do You want to play again? y = yes, n = no \n")
        while self.play_game.lower() not in ["y", "n", "yes", "no", "д", "н", "да", "нет"]:
            if self.lang == "ru":
                self.play_game = input("Хотите сыграть снова? д = да, н = нет \n")
            else:
                self.play_game = input("Do You want to play again? y = yes, n = no \n")
        if self.play_game.lower() in ["y", "yes", "д", "да"]:
            self.main()
        elif self.play_game.lower() in ["n", "no", "н", "нет"]:
            if self.lang == "ru":
                print("Спасибо за игру! Ждем вас в другой раз!")
            else:
                print("Thanks For Playing! We expect you back again!")
            exit()

    def game(self):
        length = self.length

        limit = 5
        if self.lang == "ru":
            guess = input("Загаданное слово: " + self.display + ". Введите букву (или напишите 'стоп' для остановки "
                                                                "игры): \n")
        else:
            guess = input("This is the Hangman Word: " + self.display + ". Enter your guess (or type 'stop' to stop "
                                                                        "playing): \n")

        guess = guess.strip()

        if guess in ["stop", "стоп"]:
            self.play_loop()
        elif len(guess) == 0 or len(guess) >= 2 or not guess.isalpha():
            if self.lang == "ru":
                print("Неверный символ, введите букву\n")
            else:
                print("Invalid Input, Try a letter\n")
            self.game()
        elif guess in self.already_tried:
            if self.lang == "ru":
                print("Буква уже использовалась, попробуйте другую.\n")
            else:
                print("Letter already used, try another one.\n")
        elif guess in self.word:
            while guess in self.word:
                self.already_tried.extend([guess])
                index = self.word.find(guess)
                self.word = self.word[:index] + "_" + self.word[index + 1:]
                self.display = self.display[:index] + guess + self.display[index + 1:]
            print(self.display + "\n")
        else:
            self.already_tried.extend([guess])
            self.count += 1
            if self.count == 1:
                time.sleep(1)
                print("\n"
                      "  |\n"
                      "  |\n"
                      "  |\n"
                      "  |\n"
                      "  |\n"
                      "  |\n"
                      "__|__\n")
                if self.lang == "ru":
                    print("Неверная буква. Осталось " + str(limit - self.count) + " попыток.\n")
                else:
                    print("Wrong guess. " + str(limit - self.count) + " guesses remaining\n")
            elif self.count == 2:
                time.sleep(1)
                print("   _____\n"
                      "  |\n"
                      "  |\n"
                      "  |\n"
                      "  |\n"
                      "  |\n"
                      "  |\n"
                      "__|__\n")
                if self.lang == "ru":
                    print("Неверная буква. Осталось " + str(limit - self.count) + " попытки.\n")
                else:
                    print("Wrong guess. " + str(limit - self.count) + " guesses remaining\n")
            elif self.count == 3:
                time.sleep(1)
                print("   _____ \n"
                      "  |     |\n"
                      "  |     |\n"
                      "  |\n"
                      "  |\n"
                      "  |\n"
                      "  |\n"
                      "__|__\n")
                if self.lang == "ru":
                    print("Неверная буква. Осталось " + str(limit - self.count) + " попытки.\n")
                else:
                    print("Wrong guess. " + str(limit - self.count) + " guesses remaining\n")
            elif self.count == 4:
                time.sleep(1)
                print("   _____ \n"
                      "  |     |\n"
                      "  |     |\n"
                      "  |     O\n"
                      "  |\n"
                      "  |\n"
                      "  |\n"
                      "__|__\n")
                if self.lang == "ru":
                    print("Неверная буква. Осталась " + str(limit - self.count) + " попытка.\n")
                else:
                    print("Wrong guess. " + str(limit - self.count) + " last guess remaining\n")
            elif self.count == 5:
                time.sleep(1)
                print("   _____ \n"
                      "  |     |\n"
                      "  |     |\n"
                      "  |     O\n"
                      "  |    /|\\\n"
                      "  |    / \\\n"
                      "  |\n"
                      "__|__\n")
                if self.lang == "ru":
                    print("Неверная буква. Вас повесили!\n")
                    print("Вы пробовали эти буквы:", self.already_tried)
                else:
                    print("Wrong guess. You are hanged!\n")
                    print("You tried these letters:", self.already_tried)
                while "_" in self.word:
                    index = self.word.find("_")
                    self.word = self.word[:index] + self.display[index] + self.word[index + 1:]

                if self.lang == "ru":
                    print("Загаданное слово:", self.word)
                else:
                    print("The word was:", self.word)

                self.play_loop()

        if self.word == '_' * length:
            if self.lang == "ru":
                print(f"Поздравляю! Вы отгадали слово '{self.display}'!")
            else:
                print(f"Congrats! You have guessed the word '{self.display}' correctly!")

            self.play_loop()

        elif self.count != limit:
            self.game()
