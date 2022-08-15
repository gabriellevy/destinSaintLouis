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

    def MajPortrait(self, situation):
        """
        à appeler de temps en temps (changement de boulot, passage de dizaines en âge etc, je sais pas trop
        """
        portr = portrait_saint_louis.PortraitRoiClovis()
        ageNbAnnees = self.nbJours_/365
        metObj = None
        if self.metier_ != "":
            metObj = situation.collectionMetiers[self.metier_]
        self.portraitStr_ = portr.DeterminerPortraits(situation, ageNbAnnees, self.prenom_, self.traits_, self.sexeMasculin_)

    def CreerNomNeutre(self, situation):
        self.nom_ = "tmp nom franc self.sexeMasculin_"

    def CreerPrenomNeutre(self, situation):
        self.prenom_ = "tmp prénom franc self.sexeMasculin_"

def GenererPNJ(sexeMasculin, situation, collectionPnjs, ageJours):
    """
    Génère un PNJ aléatoire avec un ensemble de caracs
    Il pourra ensuite être stocké dans la situation
    """
    ageAnnees = ageJours/360
    pnj = PnjSaintLouis(sexeMasculin, situation)
    nomStr = pnj.CreerNomNeutre(sexeMasculin)
    if nomStr is not None:
        pnj.nom_ = nomStr
    prenomStr = pnj.CreerPrenomNeutre(sexeMasculin)
    if prenomStr is not None:
        pnj.prenom_ = prenomStr

    pnj.nbJours_ = ageJours
    # métier :
    metierStr = ""
    if ageAnnees >= 20:
        # a un métier
        metier = situation.collectionMetiers.getMetierAleatoire(True, sexeMasculin, None)
        metierStr = metier.nom_
    pnj.metier_ = metierStr
    pnj.sexeMasculin_ = sexeMasculin
    pnj.portraitStr_ = ""
    # génération des traits :
    nbTraits = 2 + random.randint(0,5)
    m_Traits = []
    while nbTraits > 0:
        trait = situation.collectionTraits.getTraitAleatoire()
        if trait.PeutEtrePrisALaNaissance():
            pnj.traits_[trait.eTrait_] = trait.GetValeurALaNaissance()
            nbTraits = nbTraits - 1

    pnj.MajPortrait(situation)

    # ajouter ce nouveau pnj à la liste des pnjs de l'histoire
    collectionPnjs[pnj.prenom_] = pnj

    return pnj

def GenererPNJPapa(situation):
    nbJoursVecusPerso = temps.Date(situation.caracs_[temps.Date.DATE]).nbJours_ - temps.Date(situation.caracs_[temps.Date.DATE_NAISSANCE]).nbJours_
    ageJours = (30 + random.randint(0, 35)) * 12 *30 # âge 29 minimum (14 + 15 de l'âge du perso joué)
    pnj = GenererPNJ(True, situation, ageJours)
    pnj.metier_ = ""
    return pnj

def GenererPNJMaman(situation):
    nbJoursVecusPerso = temps.Date(situation.caracs_[temps.Date.DATE]).nbJours_ - temps.Date(situation.caracs_[temps.Date.DATE_NAISSANCE]).nbJours_
    ageJours = (30 + random.randint(0, 25)) * 12 *30 # âge 29 minimum (14 + 15 de l'âge du perso joué)
    pnj = GenererPNJ(False, situation, ageJours)
    pnj.metier_ = ""
    return pnj
