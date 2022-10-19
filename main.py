# ------- DEFINITION -------

class EtreVivant:
    ESPECE_ETRE_VIVANT = "(être vivant non identifié)"

    def AffichezInfosEtreVivant(self):
        print(f"Info être vivant: {self.ESPECE_ETRE_VIVANT}")


class Chat(EtreVivant):
    ESPECE_ETRE_VIVANT = "Chat(Mammifère - Félin)"


class Personne(EtreVivant):
    # var de classe une pour toutes les Personne
    ESPECE_ETRE_VIVANT = "Humain(Mammifère - Homo)"

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


class Etudiant(Personne):
    def __init__(self, nom, age, etudes):
        # création d'une variable d'instance : nom
        super().__init__(nom, age)
        self.etudes = etudes

    def sePresenter(self):
        super().sePresenter()
        print(f"Je suis etudiant en {self.etudes}")


# ------- UTILISATION -------
liste_personnes = [Personne("Jean", 30),
                   Personne("Paul", 15),
                   Personne("Zoe", 20)]

# Personne.ESPECE_ETRE_VIVANT = "Mutant"

for personne in liste_personnes:
    personne.sePresenter()
    personne.AffichezInfosEtreVivant()
    print()

chat = Chat()
chat.AffichezInfosEtreVivant()

etre_vivant = EtreVivant()
etre_vivant.AffichezInfosEtreVivant()

etudiant = Etudiant("Marc", 22, "Ecole d'ingénieur informatique")
etudiant.sePresenter()
etudiant.AffichezInfosEtreVivant()
