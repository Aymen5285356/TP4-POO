# Partie 1 :
class Personne:
    def __init__(self, nom, age, adresse):
        self._nom = nom
        self._age = age
        self._adresse = adresse

    def get_nom(self):
        return self._nom

    def set_nom(self, nom):
        self._nom = nom

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age > 0:
            self._age = age

    def get_adresse(self):
        return self._adresse

    def set_adresse(self, adresse):
        self._adresse = adresse


# Partie 2 :
class Etudiant(Personne):
    def __init__(self, nom, age, adresse, matricule, classe):
        super().__init__(nom, age, adresse)
        self._matricule = matricule
        self._classe = classe

    def get_matricule(self):
        return self._matricule

    def set_matricule(self, matricule):
        self._matricule = matricule

    def get_classe(self):
        return self._classe

    def set_classe(self, classe):
        self._classe = classe

    def afficher_informations(self):
        print(f"Nom: {self._nom}")
        print(f"Âge: {self._age}")
        print(f"Adresse: {self._adresse}")
        print(f"Matricule: {self._matricule}")
        print(f"Classe: {self._classe}")


# Partie 3 :
etudiant = Etudiant("Karim", 20, "12 Rue de Paris", "2024001", "DEV 101")

print("Informations initiales:")
etudiant.afficher_informations()

print("\nAprès modification de l'adresse:")
etudiant.set_adresse("45 Boulevard Voltaire, Marseille")
etudiant.afficher_informations()