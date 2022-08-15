import random
from abs.humanite import metier
from abs.humanite import portrait
from chapitres.classes import heros

class PortraitSpe(portrait.Portrait):

    def DeterminerPortraitPersoPrincipal(self, situation, masculin):
        """
        retourne l'adresse du portrait à afficher pour le perso courant
        """
        ageAnnees = situation.AgeEnAnnees()
        traitsPerso = situation.GetDicoTraits()

        return self.DeterminerPortraits(situation, ageAnnees, "Saint Louis", traitsPerso, masculin)

    def DeterminerPortraits(self, situation, ageAnnees, nom, valeursTraits, masculin):
        """
        retourne l'adresse du portrait à afficher pour le perso courant
        valeursTraits : dico contenant en clé le nom des traits possédés par le personnage et en valeur leur niveau
        """
        portraits = []
        portraitCourant = situation.GetValCarac(portrait.Portrait.C_PORTRAIT)

        if nom == heros.Heros.C_NOM:
            if ageAnnees >= 30 and ageAnnees <= 40:
                portraits.append("images/portraits/saint_louis30_40.png")
            if ageAnnees >= 16 and ageAnnees <= 30:
                portraits.append("images/portraits/saint_louis15_30.png")
            elif ageAnnees > 40:
                portraits.append("images/portraits/saint_louis40+.png")
            else:
                portraits.append("images/portraits/saint_louis_15.jpg")
        if nom == heros.Heros.C_NOM_BLANCHE:
            portraits.append("images/portraits/blanche_de_castille.jpg")
        if nom == heros.Heros.C_NOM_LOUISVIII:
            portraits.append("images/portraits/louisVIII.jpg")

        if len(portraits) == 0:
            portraits = ["images/portraits/inconnu.jpg"]

        if portraits.count(portraitCourant) == 0:
            portraitCourant = random.choice(portraits)

        return portraitCourant
