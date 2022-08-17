init -18 python:
    import random
    from abs.univers import temps
    from abs.humanite.amour import relationAmoureuse
    from abs.humanite import identite
    from spe.humanite import portrait_saint_louis

    class PnjSaintLouis(Pnj):

        # Set the store.{prefix}.character_id value
        STORE_PREFIX = "pnj_saint_louis"

        # Boolean toggle for validation - defaults both True
        VALIDATE_VALUES = False
        COERCE_VALUES = False

        STAT_DEFAULTS = {
        "nom_": "sans nom"
        }

        def __init__(self, sexeMasculin, **kwargs):
            Pnj.__init__(self, sexeMasculin, **kwargs)
            # self.CreerPrenomNeutre(sexeMasculin) # self.prenom_
            # self.nbJours_ = -1
            # self.metier_ = ""

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

        def CreerNomNeutre(self):
            setattr(self, "nom_", "tmp nom franc self.sexeMasculin_")

        def CreerPrenomNeutre(self, sexeMasculin):
            self.prenom_ = "tmp prénom franc self.sexeMasculin_ "

    def GenererPNJ(sexeMasculin, ageJours):
        """
        Génère un PNJ aléatoire avec un ensemble de caracs
        Il pourra ensuite être stocké dans la situation
        """
        global situation_, collectionPnjs_
        global metiers_, traits_
        ageAnnees = ageJours/360
        pnj = PnjSaintLouis(sexeMasculin)
        nomStr = pnj.CreerNomNeutre()
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
            metier = metiers_.getMetierAleatoire(True, sexeMasculin, None)
            metierStr = metier.nom_
        pnj.metier_ = metierStr
        pnj.sexeMasculin_ = sexeMasculin
        pnj.portraitStr_ = ""
        # génération des traits :
        """
        nbTraits = 2 + random.randint(0,5)
        m_Traits = []
        while nbTraits > 0:
            trait = traits_.getTraitAleatoire()
            if trait.PeutEtrePrisALaNaissance():
                pnj.traits_[trait.eTrait_] = trait.GetValeurALaNaissance()
                nbTraits = nbTraits - 1
        """

        # pnj.MajPortrait(situation_, metiers_)

        # ajouter ce nouveau pnj à la liste des pnjs de l'histoire
        # collectionPnjs_[pnj.prenom_] = pnj

        return pnj

    def GenererPNJPapa():
        global situation_
        joursDateActuelle = situation_.GetValCarac(temps.Date.DATE)
        joursDateNaissanceHeros = situation_.GetValCarac(temps.Date.DATE_NAISSANCE)
        nbJoursVecusPerso = joursDateActuelle - joursDateNaissanceHeros
        ageJours = (30 + random.randint(0, 35)) * 12 *30 # âge 29 minimum (14 + 15 de l'âge du perso joué)
        pnj = GenererPNJ(True, ageJours)
        # pnj.metier_ = ""
        return pnj

    def GenererPNJMaman():
        global situation_
        joursDateActuelle = situation_.GetValCarac(temps.Date.DATE)
        joursDateNaissanceHeros = situation_.GetValCarac(temps.Date.DATE_NAISSANCE)
        nbJoursVecusPerso = joursDateActuelle - joursDateNaissanceHeros
        ageJours = (30 + random.randint(0, 25)) * 12 *30 # âge 29 minimum (14 + 15 de l'âge du perso joué)
        # pnj = GenererPNJ(False, ageJours)
        pnj.metier_ = ""
        return pnj
