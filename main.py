# -*-coding:utf-8 -*
import sys
from app import controller, view
from app.models import clubs

def main():
    view.menu()
    while True:
        choix = int(input("Votre choix: "))
        if choix == 1:
            controller.all_clubs(clubs)
        elif choix == 2:
            club = str(input("Entrer le nom d'un club: "))
            controller.insert_club(clubs, club)
            controller.all_clubs(clubs)
        elif choix == 3:
            controller.all_clubs(clubs)
            index = int(input("Entre l'index de club à modifier: "))
            club = str(input("Modifier le club: "))
            controller.modify_club(clubs, index, club)
        elif choix == 4:
            club = str(input("Entrer le nom d'un club: "))
            controller.search_clubs(clubs, club)
        elif choix == 5:
            controller.all_clubs(clubs)
            controller.del_club(clubs)
            controller.all_clubs(clubs)
        elif choix == 6:
            print("vous avez choisi de quitter le programme")
            sys.exit()
        else:
            print("Choix inconnue")
    print("Bye Bye")

if __name__ == '__main__':
    main()