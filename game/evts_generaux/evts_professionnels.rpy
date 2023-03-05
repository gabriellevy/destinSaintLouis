init -5 python:
    import random
    from abs.religions import religion
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite import trait
    from abs.humanite import metier

    estPasGuerrierNivExtreme = condition.Condition(metier.Guerrier.NOM, trait.Trait.SEUIL_A_EXTREME, condition.Condition.INFERIEUR)
    estPasPolitiqueNivExtreme = condition.Condition(metier.Politique.NOM, trait.Trait.SEUIL_A_EXTREME, condition.Condition.INFERIEUR)
    estPasStrategeNivExtreme = condition.Condition(metier.Stratege.NOM, trait.Trait.SEUIL_A_EXTREME, condition.Condition.INFERIEUR)
    estPasGrandChasseur = condition.Condition(metier.Chasseur.NOM, 5, condition.Condition.INFERIEUR)

    estGuerrierAuMoinsNiv3 = condition.Condition(metier.Guerrier.NOM, trait.Trait.SEUIL_A_EXTREME, condition.Condition.SUPERIEUR_EGAL)

    def AjouterEvtsProfessionnels():
        global selecteur_
        # entrainement guerrier
        entrainementGuerrier = declencheur.Declencheur(proba.Proba(0.04, True), "entrainementGuerrier")
        entrainementGuerrier.AjouterCondition(estPasGuerrierNivExtreme)
        selecteur_.ajouterDeclencheur(entrainementGuerrier)
        adoubement = declencheur.Declencheur(proba.Proba(0.04, True), "entrainementGuerrier")
        adoubement.AjouterCondition(estGuerrierAuMoinsNiv3)
        adoubement.AjouterCondition(a19ans)
        selecteur_.ajouterDeclencheur(adoubement)
        # entrainement politique
        entrainementPolitique = declencheur.Declencheur(proba.Proba(0.04, True), "entrainementPolitique")
        entrainementPolitique.AjouterCondition(estPasPolitiqueNivExtreme)
        selecteur_.ajouterDeclencheur(entrainementPolitique)
        # entrainement chasse
        entrainementChasse = declencheur.Declencheur(proba.Proba(0.04, True), "entrainementChasse")
        entrainementChasse.AjouterCondition(estPasGrandChasseur)
        selecteur_.ajouterDeclencheur(entrainementChasse)
        # entrainement stratège/général
        entrainementStratege = declencheur.Declencheur(proba.Proba(0.04, True), "entrainementStratege")
        entrainementStratege.AjouterCondition(estPasStrategeNivExtreme)
        entrainementStratege.AjouterCondition(estPasRoi)
        selecteur_.ajouterDeclencheur(entrainementStratege)
        # éducation générale
        educationGenerale = declencheur.Declencheur(proba.Proba(0.1, True), "educationGenerale")
        educationGenerale.AjouterCondition(estEnfant)
        educationGenerale.AjouterCondition(estPasRoi)
        selecteur_.ajouterDeclencheur(educationGenerale)

label educationGenerale:
    # entrainement stratège/général
    scene bg education_saint_louis
    with dissolve
    menu:
        "Quelle est la chose dont vous avez le plus besoin pour votre éducation ?"
        "L'entrainement au combat":
            $ AjouterACarac(metier.Guerrier.NOM, 1)
            $ AjouterACarac(trait.Violence.NOM, 1)
        "L'apprentissage de la politique et de la diplomatie":
            $ AjouterACarac(metier.Politique.NOM, 1)
        "La religion et la morale":
            $ AjouterACarac(heros.Heros.C_SAINTETE, 1)
        "La culture":
            $ AjouterACarac(heros.Heros.C_EDUCATION, 1)
        "La stratégie militaire":
            $ AjouterACarac(metier.Stratege.NOM, 1)
    jump fin_cycle

label entrainementStratege:
    # entrainement stratège/général
    scene bg armee_franque
    with dissolve
    "Votre père Louis le lion a toujours insité sur le fait qu'un grand roi doit être un grand stratège."
    "Il ne perd pas une occasion de vous apprendre l'art de la guerre."
    $ AjouterACarac(metier.Stratege.NOM, 1)
    jump fin_cycle

label entrainementChasse:
    # entrainement chasse
    scene bg chasse
    with dissolve
    $ niveauExpertise = situation_.GetValCaracInt("entrainementChasseNiv")
    if niveauExpertise == 0:
        $ situation_.SetValCarac("entrainementChasseNiv", 1)
        "Vous chassez aussi souvent que possible comme tout prince franc se doit de le faire."
    elif niveauExpertise == 1:
        $ situation_.SetValCarac("entrainementChasseNiv", 2)
        "Quand ce n'est pas à la guerre que vous menez vos leudes c'est à la chasse. Car la chasse en plus de vous ravitailler en viande et cuir est un bon entrainement à la guerre."
    elif niveauExpertise == 2:
        $ situation_.SetValCarac("entrainementChasseNiv", 3)
        "Aujourd'hui vous avez tué un énorme sanglier à la chasse."
    elif niveauExpertise == 3:
        $ situation_.SetValCarac("entrainementChasseNiv", 4)
        "Aujourd'hui vous avez tué un superbe cerf à la chasse dans la gigantesque forêt des ardennes."
    elif niveauExpertise == 4:
        $ situation_.SetValCarac("entrainementChasseNiv", 5)
        "Aujourd'hui vous avez tué un buffle massif après uen chasse mémorable dans les vosges."
    elif niveauExpertise == 5:
        $ situation_.SetValCarac("entrainementChasseNiv", 6)
        $ nomCourtisan = francs_.CreerPrenom(True)
        "Un courtisan nommé [nomCourtisan] venant de l'est des royaumes francs vous a offert un arc remarquable fait de plusieurs matériaux avec des extrémités en os."
        "Il appelle cela un 'arc rélexe' et affirme que c'est l'arc de prédilection des huns et des avars."
        "Il est bien plus puissant que les arcs francs. Vous récompensez chaudement [nomCourtisan] et allez immédiatement vous entraîner pour la prochaine chasse."
        $ AjouterACarac(metier.Guerrier.NOM, 1)
    else:
        "Vous chassez aussi souvent que possible comme tout prince franc se doit de le faire."
    $ AjouterACarac(metier.Chasseur.NOM, 1)
    jump fin_cycle

label entrainementPolitique:
    # s'entraîne à la politique
    scene bg cours
    with dissolve
    $ niveauExpertise = situation_.GetValCaracInt("entrainementPolitiqueNiv")
    if niveauExpertise == 0:
        $ situation_.SetValCarac("entrainementPolitiqueNiv", 1)
        "Votre père a toujours su contrôler les chefs de clans par un mélange de force et de diplomatie. Il vous a montré toutes ses astuces et manoeuvres. Vous suivrez son exemple."
    elif niveauExpertise == 1:
        $ situation_.SetValCarac("entrainementPolitiqueNiv", 2)
        "Vous entretenez de bons rapports avec les sénateurs romains. Malgré leur mollesse ils sont plein de bon sens et leur système de loi romaine devrait faciliter votre domination et la rentrée des impôts."
    elif niveauExpertise == 2:
        $ situation_.SetValCarac("entrainementPolitiqueNiv", 3)
        "Les évèques sont très respectés par le peuple, leurs avis sont révérés. En écoutant leurs conseils vous gagnez en compréhnsion sur la Gaulle et donc en influence."
    elif niveauExpertise == 3:
        $ situation_.SetValCarac("entrainementPolitiqueNiv", 4)
        "Encouragé par les sénateurs romains et les fonctionnaires vous adaptez progressivement les formulaires pour enregistrer les actes administratifs."
        "Vente de terre, achat et affranchissement d'esclave, divorce, nomination de fonctionnaire... mieux vaut garder une trace de tout cela."
    else:
        "Vous perfectionnez vos talents politiques."
    $ AjouterACarac(metier.Politique.NOM, 1)
    jump fin_cycle

label adoubement:
    scene bg armee_franque
    with dissolve
    "Vous êtes enfin adoubé chevalier."
    jump fin_cycle

label entrainementGuerrier:
    # s'entraîne au combat
    scene bg armee_franque
    with dissolve
    $ niveauExpertise = situation_.GetValCaracInt("entrainementGuerrierNiv")
    if niveauExpertise == 0:
        $ situation_.SetValCarac("entrainementGuerrierNiv", 1)
        "Avant de pouvoir manier les armes, un roi chevalier doit devenir un cavalier émérite. Vous apprenez à chevaucher dès l'âge de cinq ans et prenez goût aux beaux et puissants destriers dès que vous avez l'âge de les monter."
    elif niveauExpertise == 1:
        $ situation_.SetValCarac("entrainementGuerrierNiv", 2)
        "L'épée a une valeur symbolique pour un chevalier même si elle est moins utilisée au combat que la lance. Vous apprenez à la manier avec els meilleurs maîtres."
    elif niveauExpertise == 2:
        $ situation_.SetValCarac("entrainementGuerrierNiv", 3)
        "Maintenant que vous êtes un bon cavalier et un bon bretteur vous êtes formé à l'essence de la chevallerie : le combat monté, et en particulier le maniement de la lance."
    else:
        "Vous vous entrainez au combat."
    $ AjouterACarac(metier.Guerrier.NOM, 1)
    jump fin_cycle
