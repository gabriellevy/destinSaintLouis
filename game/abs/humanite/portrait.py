import random

class Portrait:

    C_PORTRAIT = u"Portrait"

    def DeterminerPortraitPersoPrincipal(self, situation):
        """
        retourne l'adresse du portrait à afficher pour le perso courant
        """
        ageAnnees = situation.AgeEnAnnees()

        return self.DeterminerPortraits(situation, ageAnnees)

    def DeterminerPortraits(self, situation, ageAnnees):
        """
        retourne l'adresse du portrait à afficher pour le perso courant
        """
        portraits = []
        portraitCourant = situation.GetValCarac(Portrait.C_PORTRAIT)

        # if ageAnnees >= 30 and ageAnnees <= 40:
        #    portraits.append("images/portraits/heros30_40.png")

        if len(portraits) == 0:
            portraits = ["images/portraits/inconnu.jpg"]

        if portraits.count(portraitCourant) == 0:
            portraitCourant = random.choice(portraits)

        return portraitCourant
