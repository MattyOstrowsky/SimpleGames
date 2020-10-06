import random
import show
import re


def valid_input(rang):
    """
    fukcja do sprawdzenia poprawności wprowadzeń
    :param rang:
    :return: do jakiej liczby można wprowadzić w wyborze
    """
    while True:
        try:
            a = int(input())
            if a <= rang:
                break
            else:
                print("Wprowadź poprawnie wybór!!!")
        except ValueError:
            print("Wprowadź poprawnie wybór!!!")

    return a


def check_char_game(comp_word, unknown, word):
    """
    sprawdza wprowadzone litery w grze
    :param comp_word: word bierzący stan słowa
    :param unknown: litera wpisana
    :param word: słowo zagadka
    :return:
    """
    new = ""
    if unknown in word:
        for i in range(len(word)):
            if unknown == word[i]:
                new += unknown
            else:
                new += comp_word[i]
        comp_word = new
        return comp_word
    else:
        return False


def category():
    """
    otwiera plik z kategorią
    :return:
    """
    print("Kategorie z której będzie wylosowane hasło:\n1.Geografia\n2.Biologia \n3.Religia\n4.Fizyka\n5.Różne(expert)")
    print("Podaj kategorie:")
    cat = valid_input(5)
    if cat == 1:
        plik = open('geografia')
    elif cat == 2:
        plik = open('biologia')
    elif cat == 3:
        plik = open('religia')
    elif cat == 4:
        plik = open('fizyka')
    else:
        plik = open('rozne')
    text = []
    try:
        for linia in plik:
            linia = linia.strip()
            text.append(linia)
    finally:
        plik.close()
        return text


def game():
    """
    gra, losowanie, sprawdźa czy wyraz posiada litere, czy wygrana/przegrana, dodaje do listy użytych juz wyrazów
    attempt: licznik nie trafionych liter
    used_char: lista użytych liter
    camp_word: bierzący stan słowa
    unknown: litera wpisana
    word: słowo zagadka
    :return:
    """
    MAX_WRONG = 7

    WORDS = category()
    word = random.choice(WORDS)
    comp_word = re.sub(re.compile(r'[^\s]'), '*', word)

    attempt = 0
    used_char = []

    show.show_hangman(attempt)
    print(comp_word)

    while attempt < MAX_WRONG and comp_word != word:
        print("----------------------------------------------------------------------------")
        show.show_char(used_char)
        unknown = input("Podaj literę: ")
        unknown = unknown.lower()

        while unknown in used_char:
            show.same_char()
            unknown = input("\nPodaj nową literę: ")
            unknown = unknown.lower()
        used_char.append(unknown)

        if check_char_game(comp_word, unknown, word):
            comp_word = check_char_game(comp_word, unknown, word)
            show.good_char(unknown)
            print(comp_word)
        else:
            attempt += 1
            show.bad_char(attempt)
            show.chance(attempt)
            print(comp_word)

    if attempt == MAX_WRONG:
        show.lose(word)
        return False
    else:
        show.winner(comp_word)
        return True


def ranking_point(nick, score):
    """
    po zakończonej grze przypisuje punkty
    :param nick: nazwa użytkownika
    :param score: score wynik gry true/false
    :return:
    """
    plik = open('ranking')
    text = []
    try:
        for linia in plik:
            linia = linia.strip()
            text.append(linia)
    finally:
        plik.close()
    counter = 0
    if score:
        if nick in text:
            for x in text:
                if x == nick:
                    fast = int(text[counter + 2])
                    text[counter + 2] = fast + 1
                    text[counter + 1] = int(text[counter + 2]) - int(text[counter + 3])
                counter += 1
        else:
            text.append(nick)
            text.append("1")
            text.append("1")
            text.append("0")

        plik = open('ranking', 'w')
        try:
            for linia in text:
                plik.write(str(linia))
                plik.write('\n')
        finally:
            plik.close()
    else:
        if nick in text:
            for x in text:
                if x == nick:
                    fast = int(text[counter + 3])
                    text[counter + 3] = fast + 1
                    text[counter + 1] = int(text[counter + 2]) - int(text[counter + 3])
                counter += 1
        else:
            text.append(nick)
            text.append("-1")
            text.append("0")
            text.append("1")

        plik = open('ranking', 'w')
        try:
            for linia in text:
                plik.write(str(linia))
                plik.write('\n')
        finally:
            plik.close()


def ranking_sort():
    """
    sortuje ranking wg bilansu
    :return:
    """
    plik = open('ranking')
    text = []

    try:
        for linia in plik:
            linia = linia.strip()
            text.append(linia)
    finally:
        plik.close()

    for x in range(1, len(text), 4):
        for y in range(5, len(text), 4):
            if int(text[y - 4]) < int(text[y]):
                buff = text[y - 1]
                text[y - 1] = text[y - 5]
                text[y - 5] = buff

                buff = text[y]
                text[y] = text[y - 4]
                text[y - 4] = buff

                buff = text[y + 1]
                text[y + 1] = text[y - 3]
                text[y - 3] = buff

                buff = text[y + 2]
                text[y + 2] = text[y - 2]
                text[y - 2] = buff
    return text
