import random
from abs.humanite import metier
from abs.humanite import portrait
from chapitres.classes import heros

class PortraitRoiClovis(portrait.Portrait):

    def DeterminerPortraitPersoPrincipal(self, situation, masculin):
        """
        retourne l'adresse du portrait à afficher pour le perso courant
        """
        ageAnnees = situation.AgeEnAnnees()
        traitsPerso = situation.GetDicoTraits()

        return self.DeterminerPortraits(situation, ageAnnees, "Clovis", traitsPerso, masculin)

    def DeterminerPortraits(self, situation, ageAnnees, nom, valeursTraits, masculin):
        """
        retourne l'adresse du portrait à afficher pour le perso courant
        valeursTraits : dico contenant en clé le nom des traits possédés par le personnage et en valeur leur niveau
        """
        portraits = []
        portraitCourant = situation.GetValCarac(portrait.Portrait.C_PORTRAIT)

        if nom == heros.Heros.C_NOM_CLOVIS:
            if ageAnnees >= 30 and ageAnnees <= 40:
                portraits.append("images/portraits/clovis30_40.png")
            if ageAnnees >= 16 and ageAnnees <= 30:
                portraits.append("images/portraits/clovis15_30.png")
            elif ageAnnees > 40:
                portraits.append("images/portraits/clovis40+.png")
            else:
                portraits.append("images/portraits/clovis_15.jpg")
        if nom == heros.Heros.C_NOM_BASINE:
            portraits.append("images/portraits/basine.jpg")
        if nom == heros.Heros.C_NOM_CHILDERIC:
            portraits.append("images/portraits/childeric.jpg")

        if len(portraits) == 0:
            portraits = ["images/portraits/inconnu.jpg"]

        if portraits.count(portraitCourant) == 0:
            portraitCourant = random.choice(portraits)

        return portraitCourant
