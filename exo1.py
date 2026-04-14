# Partie 1 :
class Personne:
    def __init__(self, nom, age):
        self._nom = nom
        self._age = age

    def afficher_informations(self):
        print(f"Nom: {self._nom}, Âge: {self._age}")

    def get_nom(self):
        return self._nom

    def set_nom(self, nom):
        self._nom = nom

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age > 0:
            self._age = age


# Partie 2 :
class Employe(Personne):
    def __init__(self, nom, age, poste, salaire):
        super().__init__(nom, age)
        self._poste = poste
        self._salaire = salaire

    def afficher_informations(self):
        super().afficher_informations()
        print(f"Poste: {self._poste}, Salaire: {self._salaire}")

    def get_poste(self):
        return self._poste

    def set_poste(self, poste):
        self._poste = poste

    def get_salaire(self):
        return self._salaire

    def set_salaire(self, salaire):
        if salaire > 0:
            self._salaire = salaire


# Partie 3 :
personne = Personne("Alice", 30)
employe = Employe("Bob", 25, "Développeur", 35000)

print("Informations initiales:")
personne.afficher_informations()
employe.afficher_informations()

print("\nAprès modification:")
employe.set_nom("Robert")
employe.set_age(26)
employe.set_poste("Lead Développeur")
employe.set_salaire(45000)
employe.afficher_informations()