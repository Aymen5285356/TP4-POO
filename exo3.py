# Partie 1 : Classe Employe
class Employe:
    def __init__(self, nom, age, salaire):
        self._nom = nom
        self._age = age
        self._salaire = salaire

    def get_nom(self):
        return self._nom

    def set_nom(self, nom):
        self._nom = nom

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age > 0:
            self._age = age

    def get_salaire(self):
        return self._salaire

    def set_salaire(self, salaire):
        if salaire > 0:
            self._salaire = salaire

    def afficher_informations(self):
        print(f"Nom: {self._nom}, Âge: {self._age}, Salaire: {self._salaire}")


# Partie 2 :
class Manager(Employe):
    def __init__(self, nom, age, salaire, departement, subordonnes=None):
        super().__init__(nom, age, salaire)
        self._departement = departement
        self._subordonnes = subordonnes if subordonnes is not None else []

    def get_departement(self):
        return self._departement

    def set_departement(self, departement):
        self._departement = departement

    def get_subordonnes(self):
        return self._subordonnes

    def set_subordonnes(self, subordonnes):
        self._subordonnes = subordonnes

    def ajouter_subordonne(self, employe):
        """Ajoute un employé à la liste des subordonnés"""
        self._subordonnes.append(employe)
        print(f"{employe.get_nom()} a été ajouté comme subordonné de {self.get_nom()}")

    def afficher_informations(self):
        super().afficher_informations()
        print(f"Département: {self._departement}")
        print("Subordonnés:")
        if self._subordonnes:
            for sub in self._subordonnes:
                print(f"  - {sub.get_nom()}")
        else:
            print("  Aucun subordonné")


# Partie 3 :
employe1 = Employe("Jean", 30, 30000)
employe2 = Employe("Marie", 28, 32000)
employe3 = Employe("Pierre", 35, 35000)

manager = Manager("Sophie", 40, 50000, "Informatique")

print("Informations initiales:")
print("\nEmployé:")
employe1.afficher_informations()
print("\nManager:")
manager.afficher_informations()

print("\n--- Ajout des subordonnés ---")
manager.ajouter_subordonne(employe1)
manager.ajouter_subordonne(employe2)
manager.ajouter_subordonne(employe3)

print("\nInformations mises à jour du manager:")
manager.afficher_informations()