#Afichage de club
def all_clubs(clubs):
    for i in range(len(clubs)):
        print(f'{i+1}. {clubs[i]}')

#Ajout de club
def insert_club(clubs, club):
    clubs.append(club)

#Modifier clubs
def modify_club(clubs, index, club):
    index = index - 1
    for i in range(len(clubs)):
        if i == index:
            clubs[i]=club

#Suppression de de club
def del_club(clubs):
    print("Quel club voulez vous supprimer?")
    choix = int(input("Votre choix: "))
    for i in range(len(clubs)):
        if choix == i+1:
            clubs.pop(i)

def search_clubs(clubs, club):
    tab = []
    for i in clubs:
      if i.find(club)>=0:
        tab.append(i)
        for i in tab:
            print(i)

    

