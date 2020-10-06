HANGMAN = (
    """
     ------
     |    |
     |
     |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   -+-
     | 
     |   
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-
     |   
     |   
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |   
     |   
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |    |
     |   
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-+-/
     |    |
     |    |
     |   | 
     |   | 
     |   
    ----------
    """,
    """
     ______
     |    |
     |    O
     |  /-+-/
     |    |
     |    |
     |   | |
     |   | |
     |  
    ----------
    """)


def welcome():
    print("----------------------------------WISIELEC----------------------------------\n")
    print("Zasady są proste musisz odgadnąć wyraz inaczej zostaniesz powieszony. Powodzenia\n")


def show_char(used):
    return print("Wpisane już litery:", used)


def show_hangman(attempt):
    return print(HANGMAN[attempt])


def bad_char(attempt):
    print(HANGMAN[attempt])
    return print("\nNie ma tej litery, próbuj dalej!")


def chance(attempt):
    return print("Masz jeszcze ", 7 - attempt, " szans.")


def lose(word):
    print("\n--------------------------ZOSTAŁEŚ POWIESZONY!------------------------------")
    print(HANGMAN[7])
    return print("Szukany wyraz to", word)


def same_char():
    print("\nUżyłeś już tej litery lub wprowdziłeś cyfrę, wprowadź poprawnie !!")


def good_char(char):
    print("\nUdało ci się, litera "+char+" jest w haśle.")


def winner(word):
    print("\n---------------------------------WYGRAŁEŚ!!!--------------------------"
          "------\n--------------------------------GRATULACJĘ!!!-------------------------------")
    print("""                                 .''.
       .''.             *''*    :_\/_:     .
      :_\/_:   .    .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ : _\(/_  ':'* /\ *  : '..'.  -=:o:=-
 :_\/_:'.:::. /)\*''*  .|.* '.\'/.'_\(/_'.':'.'
 : /\ : :::::  '*_\/_* | |  -= o =- /)\    '  *
  '..'  ':::'   * /\ * |'|  .'/.\'.  '._____
      *        __*..* |  |     :      |.   |' .---"|
       _*   .-'   '-. |  |     .--'|  ||   | _|    |
    .-'|  _.|  |    ||   '-__  |   |  |    ||      |
    |' | |.    |    ||       | |   |  |    ||      |
 ___|  '-'     '    ""       '-'   '-.'    '`      |____
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
    print("                               Hasło to:", word, "\n")


def menu(nick):
    print("----------------------------------WYBIERZ:----------------"
          "------------------\n1.Zmień nick(" + nick + ")\n2.Graj\n3.Ranking\n4.Wyjście")


def ranking(text):
    x = 1
    y = 9
    for linia in text:
        if x == 1:
            print("*** " + linia + " ***")
        elif x == 5:
            print("** " + linia + " **")
        elif x == 9:
            print("* " + linia + " *")
        elif x % 4 == 1:
            print(str(x - y) + "." + linia)
            y += 3
        elif x % 4 == 2:
            print("Bilans: " + linia + "")
        elif x % 4 == 3:
            print("Wygrane: " + linia + "")
        else:
            print("Porażki: " + linia + "\n")
        x += 1
