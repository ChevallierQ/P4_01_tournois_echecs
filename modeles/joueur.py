from time import sleep as sl
from vues.outils_vues import OutilsVues
from controleurs.outils_controleurs import OutilsControleurs
import json


class Joueur:

    def __init__(self, nom="", prenom="", date_de_naissance="", sexe="", classement=0):
        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.sexe = sexe
        self.classement = classement

        print("\n---------------------------")
        while len(nom) == 0:
            try:
                nom = str(input("\nNom : "))
            except ValueError:
                print("\nVous n'avez pas saisi un nom valide.")
                sl(2)
                continue

        print("\n---------------------------")
        while len(prenom) == 0:
            try:
                prenom = str(input("\nPrenom : "))
            except ValueError:
                print("\nVous n'avez pas saisi un prenom valide.")
                sl(2)
                continue

        print("\n---------------------------")
        while len(date_de_naissance) == 0:
            try:
                date_de_naissance = str(input("\nDate de naissance\nFormat : jj/mm/aaaa : "))
            except ValueError:
                print("\nVous n'avez pas saisi une date valide.")
                sl(2)
                continue
            test_date = OutilsControleurs.test_date(date_de_naissance)
            if test_date == 0:
                print("\nVous avez saisi une valeur trop grande.")
                date_de_naissance = ""
            if test_date == 1:
                print("\nVous avez saisi une valeur trop petite.")
                date_de_naissance = ""
            if test_date == 2:
                break
            if test_date == 3:
                print("\nVous avez saisi un format de date incorrect.")
                date_de_naissance = ""

        print("\n---------------------------")
        sexe_choix = 0
        while sexe_choix != 1 or sexe_choix != 2 or sexe_choix != 3:
            try:
                sexe_choix = int(input("\nSexe\n1 - Femme\n2 - Homme\n3 - Autre\n\nVotre choix : "))
            except ValueError:
                print("\nVous n'avez pas saisi une valeur valide.")
                sl(2)
                continue
            if sexe_choix == 1:
                sexe = "Femme"
                break
            if sexe_choix == 2:
                sexe = "Homme"
                break
            if sexe_choix == 3:
                sexe = "Autre"
                break

        print("\n---------------------------")
        while classement < 1 or classement > 8:
            try:
                classement = int(input("\nClassement : "))
            except ValueError:
                print("\nVous n'avez pas saisi une valeur valide.")
                sl(2)
                continue

        instance_class = OutilsVues()
        if instance_class.sauvegarde(nom, prenom, date_de_naissance, sexe, classement) == 1:
            instance_class_serialiser = OutilsControleurs()
            instance_class_serialiser.serialiser_instance_joueur(nom, prenom, date_de_naissance, sexe, classement)
            return

    def joueurs_alpha():
        with open('data/joueurs.json', 'r') as joueurs_data:
            data_dict = json.load(joueurs_data)
            nom_list = []
            nom = ''
            prenom = ''
            for joueur in data_dict.values():
                for num_joueur in joueur.values():
                    for cle, valeur in num_joueur.items():
                        if cle == 'nom':
                            nom = valeur
                        if cle == 'prenom':
                            prenom = valeur
                    nom_prenom = nom + ' ' + prenom + '\n'
                    nom_list.append(nom_prenom)
                    nom_list.sort()
            if len(nom_list) < 2:
                return 0
            if len(nom_list) >= 2:
                del nom_list[0]
                return nom_list

    def joueurs_classement():
        with open('data/joueurs.json', 'r') as joueurs_data:
            data_dict = json.load(joueurs_data)
            classement_nom_list = []
            nom = ''
            prenom = ''
            classement = ''
            for joueur in data_dict.values():
                for num_joueur in joueur.values():
                    for cle, valeur in num_joueur.items():
                        if cle == 'nom':
                            nom = valeur
                        if cle == 'prenom':
                            prenom = valeur
                        if cle == 'classement':
                            classement = 'Classement : ' + str(valeur)
                    nom_prenom_classement = classement + '\n    ' + nom + ' ' + prenom + '\n'
                    classement_nom_list.append(nom_prenom_classement)
                    classement_nom_list.sort()
            if len(classement_nom_list) < 2:
                return 0
            if len(classement_nom_list) >= 2:
                del classement_nom_list[0]
                return classement_nom_list

    def joueurs_tournoi():
        with open('data/joueurs.json', 'r') as joueurs_data:
            data_dict = json.load(joueurs_data)
            classement_nom_list = []
            indice_joueur = 0
            nom = ''
            prenom = ''
            classement = ''
            for joueur in data_dict.values():
                for num_joueur in joueur.values():
                    for cle, valeur in num_joueur.items():
                        if cle == 'nom':
                            nom = valeur
                        if cle == 'prenom':
                            prenom = valeur
                        if cle == 'classement':
                            classement = 'Classement : ' + str(valeur)
                    indice_nom_prenom_classement = 'Indice joueur : ' + str(indice_joueur) + '\n   ' + nom + \
                        ' ' + prenom + '\n   ' + classement + '\n'
                    classement_nom_list.append(indice_nom_prenom_classement)
                    indice_joueur += 1
            if len(classement_nom_list) < 9:
                return 0
            if len(classement_nom_list) >= 9:
                del classement_nom_list[0]
                return classement_nom_list

    def get_joueurs_tournoi(liste_indice_selection, liste_nom_joueurs):
        liste_nom_joueurs_selection = []
        liste_nom_joueurs_new = []
        for arg in liste_nom_joueurs:
            arg = str(arg).replace("\n", "")
            liste_nom_joueurs_new.append(arg)
        for indice in liste_indice_selection:
            liste_nom_joueurs_selection.append(liste_nom_joueurs_new[indice-1])
        return liste_nom_joueurs_selection

    def get_classement_joueur(joueur_selecion):
        with open('data/joueurs.json', 'r') as joueurs_data:
            data_dict = json.load(joueurs_data)
            for joueurs in data_dict.values():
                for num_joueurs in joueurs.values():
                    for cle, valeur in num_joueurs.items():
                        if cle == "nom":
                            nom = valeur
                        if cle == "prenom":
                            prenom = valeur
                    nom_prenom = nom + " " + prenom
                    if nom_prenom == joueur_selecion:
                        for cle, valeur in num_joueurs.items():
                            if cle == "classement":
                                joueur_selecion = valeur
                                return joueur_selecion
