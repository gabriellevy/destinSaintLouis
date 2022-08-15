init -10 python:
    from spe.humanite import pnj_saint_louis

    def GenererPNJ(sexeMasculin, collectionPnjs, ageJours):
        """
        Génère un PNJ aléatoire avec un ensemble de caracs
        Il pourra ensuite être stocké dans la situation
        """
        global situation_
        global metiers_, traits_
        ageAnnees = ageJours/360
        pnj = pnj_saint_louis.PnjSaintLouis(sexeMasculin, situation_)
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
            metier = metiers_.getMetierAleatoire(True, sexeMasculin, None)
            metierStr = metier.nom_
        pnj.metier_ = metierStr
        pnj.sexeMasculin_ = sexeMasculin
        pnj.portraitStr_ = ""
        # génération des traits :
        nbTraits = 2 + random.randint(0,5)
        m_Traits = []
        while nbTraits > 0:
            trait = traits_.getTraitAleatoire()
            if trait.PeutEtrePrisALaNaissance():
                pnj.traits_[trait.eTrait_] = trait.GetValeurALaNaissance()
                nbTraits = nbTraits - 1

        pnj.MajPortrait(situation_, metiers_)

        # ajouter ce nouveau pnj à la liste des pnjs de l'histoire
        collectionPnjs[pnj.prenom_] = pnj

        return pnj

    def GenererPNJPapa():
        global collectionPnjs_
        global situation_
        joursDateActuelle = situation_.GetValCarac(temps.Date.DATE)
        joursDateNaissanceHeros = situation_.GetValCarac(temps.Date.DATE_NAISSANCE)
        nbJoursVecusPerso = joursDateActuelle - joursDateNaissanceHeros
        ageJours = (30 + random.randint(0, 35)) * 12 *30 # âge 29 minimum (14 + 15 de l'âge du perso joué)
        pnj = GenererPNJ(True, collectionPnjs_, ageJours)
        pnj.metier_ = ""
        return pnj

    def GenererPNJMaman():
        global collectionPnjs_
        global situation_
        joursDateActuelle = situation_.GetValCarac(temps.Date.DATE)
        joursDateNaissanceHeros = situation_.GetValCarac(temps.Date.DATE_NAISSANCE)
        nbJoursVecusPerso = joursDateActuelle - joursDateNaissanceHeros
        ageJours = (30 + random.randint(0, 25)) * 12 *30 # âge 29 minimum (14 + 15 de l'âge du perso joué)
        pnj = GenererPNJ(False, collectionPnjs_, ageJours)
        pnj.metier_ = ""
        return pnj
