import show
import wisielec

show.welcome()

nick = input("Podaj nazwę użytkownika: ")
show.menu(nick)
choose = 0

while choose != 4:
    choose = int(wisielec.valid_input(4))
    if choose == 1:
        nick = input("Podaj nazwę użytkownika: ")
        show.menu(nick)
    elif choose == 2:
        wisielec.ranking_point(nick, wisielec.game())
        show.menu(nick)
    elif choose == 3:
        show.ranking(wisielec.ranking_sort())
        show.menu(nick)
    elif choose == 4:
        print("Dowidzenia!")
