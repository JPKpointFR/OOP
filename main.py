

# ------- DEFINITION -------
class Personne:
    def __init__(self, nom="", age=0):
        # création d'une variable d'instance : nom
        self.nom = nom
        self.age = age
        if nom == "":
            self.demanderNom()
        print(f"Constructeur personne {self.nom}")

    def sePresenter(self):
        info_personne = f"Bonjour, je m'appelle {self.nom}"
        if self.age != 0:
            info_personne += f", j'ai {self.age} ans"

        print(info_personne)

        if self.age != 0:
            if self.estMajeur():
                print(f"Je suis majeur")
            else:
                print(f"Je suis mineur")

    def estMajeur(self):
        return self.age >= 18
        """if self.age >= 18:
            return True
        return False"""

    def demanderNom(self):
        self.nom = input("Quel est votre nom ? ")


# ------- UTILISATION -------
personne1 = Personne("Jean", 30)  # Je crée une personne
personne2 = Personne("Paul", 15)  # Je crée une personne
personne3 = Personne()
personne4 = Personne(age=17)


# Personne.sePresenter(personne1)
personne1.sePresenter()
personne2.sePresenter()
personne3.sePresenter()
personne4.sePresenter()

# print(f"Est majeur: {personne1.estMajeur()}")
# print(f"Est majeur: {personne2.estMajeur()}")

"""def afficher_informations_personne(nom, age):
    print(f"La personne s'appelle {nom}, son âge est {age}ans ")


def demander_nom_personne():
    nom = input("Quel est votre nom ? ")
    return nom
    # age = input("Quel est votre âge ? ")
    # afficher_informations_personne(nom, age)


nom1 = "Jean"
age1 = 30
nom2 = "Paul"
age2 = 25

afficher_informations_personne(nom1, age1)
afficher_informations_personne(nom2, age2)
 

nom3 = demander_nom_personne()
age3 = 18
afficher_informations_personne(nom3, age3)"""
