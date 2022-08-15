import random
from abs.univers import temps
from abs.humanite.amour import relationAmoureuse
from abs.humanite import identite
from abs.humanite import pnj
from spe.humanite import portrait_saint_louis

class PnjSaintLouis(pnj.Pnj):

    def __init__(self, sexeMasculin, situation):
        pnj.Pnj.__init__(self, sexeMasculin, situation)
        self.CreerPrenomNeutre(situation) # self.prenom_
        self.nbJours_ = -1
        self.metier_ = ""

    def __str__(self):
        str = u"{} {}".format(self.prenom_, self.nom_)

        nbJoursVecus = self.nbJours_
        if isinstance(nbJoursVecus, int):
            nbAnnees = nbJoursVecus/365
            nbJoursPasses = nbJoursVecus%365
            nbMois = nbJoursPasses/30
            if nbMois > 0:
                str = u"{}\n{} ans, {} mois".format(str, nbAnnees, nbMois)
            else:
                str = u"{}\n{} ans".format(str, nbAnnees)

        if self.metier_ != "":
            str = u"{}\n{}".format(str, self.metier_)
        return str

    def MajPortrait(self, situation, metiers):
        """
        à appeler de temps en temps (changement de boulot, passage de dizaines en âge etc, je sais pas trop
        """
        portr = portrait_saint_louis.PortraitSpe()
        ageNbAnnees = self.nbJours_/365
        metObj = None
        if self.metier_ != "":
            metObj = metiers[self.metier_]
        self.portraitStr_ = portr.DeterminerPortraits(situation, ageNbAnnees, self.prenom_, self.traits_, self.sexeMasculin_)

    def CreerNomNeutre(self, situation):
        self.nom_ = "tmp nom franc self.sexeMasculin_"

    def CreerPrenomNeutre(self, situation):
        self.prenom_ = "tmp prénom franc self.sexeMasculin_"
