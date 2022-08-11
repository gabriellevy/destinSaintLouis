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
    estPasGrandPretre = condition.Condition(metier.Pretre.NOM, 5, condition.Condition.INFERIEUR)

    def AjouterEvtsProfessionnels():
        global selecteur_
        # entrainement guerrier
        entrainementGuerrier = declencheur.Declencheur(proba.Proba(0.1, True), "entrainementGuerrier")
        entrainementGuerrier.AjouterCondition(estPasGuerrierNivExtreme)
        selecteur_.ajouterDeclencheur(entrainementGuerrier)
        # entrainement politique
        entrainementPolitique = declencheur.Declencheur(proba.Proba(0.06, True), "entrainementPolitique")
        entrainementPolitique.AjouterCondition(estPasPolitiqueNivExtreme)
        selecteur_.ajouterDeclencheur(entrainementPolitique)
        # entrainement chasse
        entrainementChasse = declencheur.Declencheur(proba.Proba(0.04, True), "entrainementChasse")
        entrainementChasse.AjouterCondition(estPasGrandChasseur)
        selecteur_.ajouterDeclencheur(entrainementChasse)
        # entrainement prêtre
        entrainementPretre = declencheur.Declencheur(proba.Proba(0.04, True), "entrainementPretre")
        entrainementPretre.AjouterCondition(estPasGrandPretre)
        entrainementPretre.AjouterCondition(estPasChretien)
        selecteur_.ajouterDeclencheur(entrainementPretre)
        # entrainement stratège/général
        entrainementStratege = declencheur.Declencheur(proba.Proba(0.1, True), "entrainementStratege")
        entrainementStratege.AjouterCondition(estPasStrategeNivExtreme)
        entrainementStratege.AjouterCondition(estPasRoi) # c'est Childéric qui fait la leçon
        selecteur_.ajouterDeclencheur(entrainementStratege)

label entrainementPretre:
    # entrainement prêtre
    scene bg chevauchee_paienne
    with dissolve
    "En tant que prince de sang divin vous être destiné à devenir un roi prêtre. Vous apprenez les rituels."
    $ AjouterACarac(metier.Pretre.NOM, 1)
    jump fin_cycle

label entrainementStratege:
    # entrainement stratège/général
    scene bg tolbiac
    with dissolve
    "Votre père Childéric vous emmène avec lui chaque fois qu'il part en campagne et ne perd pas une occasion de vous apprendre l'art de la guerre."
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
        $ nomCourtisan = gaulois_.CreerPrenom(True)
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
    scene bg cours_merovingienne
    with dissolve
    $ niveauExpertise = situation_.GetValCaracInt("entrainementPolitiqueNiv")
    if niveauExpertise == 0:
        $ situation_.SetValCarac("entrainementPolitiqueNiv", 1)
        "Votre père a toujours su contrôler les chefs de clans par un mélange de force et de diplomatie? Il vous a montré toutes ses astuces et manoeuvres. Vous suivez son exemple."
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

label entrainementGuerrier:
    # s'entraîne au combat
    scene bg francs
    with dissolve
    $ niveauExpertise = situation_.GetValCaracInt("entrainementGuerrierNiv")
    if niveauExpertise == 0:
        $ situation_.SetValCarac("entrainementGuerrierNiv", 1)
        "Il est capital pour un roi germanique de savoir manier la lance, symbole royal par excellence qui vous identifie à Wotan, père des dieux et seigneur des batailles. Ce sera donc votre première leçon au combat."
    elif niveauExpertise == 1:
        $ situation_.SetValCarac("entrainementGuerrierNiv", 2)
        "Aujourd'hui la leçon porte sur le maniement de la scramasax, le long couteau favori de vos guerriers. Il s'agit d'un long couteau dont la longueur peut varier entre 20 et 80 cm. Il s'agit autant d'une arme secondaire que d'un outil à tout faire."
        "Un prince de sang comme vous peut bien sûr se payer une épée longue mais il est bon à un vrai prince de savoir manier toutes les armes. Il force ainsi le respect de ses hommes et prouve ses dons divins."
    elif niveauExpertise == 2:
        $ situation_.SetValCarac("entrainementGuerrierNiv", 3)
        "Vous vous entrainez au maniement de la francisque, la lourde hache de lancer franque. Son maniement est subtil car il faut lui appliquer une forte rotation mais bien utilisée à une douzaine de mètres elle enfonce aisément les armures."
    elif niveauExpertise == 3:
        $ situation_.SetValCarac("entrainementGuerrierNiv", 4)
        "Vous vous entrainez au maniement de l'angon, la lance à crochet des francs. Son usage particulier est d'être lancée sur l'ennemi à bonne distance et, grâce à son crochet, d'être très difficile à extraire que ce soit d'un membre ou d'un bouclier."
    elif niveauExpertise == 4:
        $ situation_.SetValCarac("entrainementGuerrierNiv", 5)
        "Maintenant que vous maîtrisez toutes les armes du guerrier franc il est temps d'apprendre à les manier parfaitement à l'unisson."
        "Dans la mêlée, le Franc lance, quant il le faut, cet angon et si son arme atteint le corps le dard naturellement s'y enfonce, et ni celui qui a été frappé, ni personne ne peuvent aisément en retirer la pique,"
        "empêché qu'on se trouve par les pointes crochues ayant profondément pénétré dans les chairs, où elles causent de cruelles douleurs, de sorte que, même si l'ennemi n'a pas été sérieusement touché, il meurt tout de même de sa blessure."
        "Si le trait s'est fixé dans le bouclier, il y reste suspendu, promené partout avec lui, son extrémité traînant au sol. L'homme frappé ne peut retirer la pique à cause des crochets qui y ont pénétré, ni la couper avec l'épée parce que qu'il ne peut atteindre le bois sous l'écorce de fer."
        "Dès que le franc a vu son ennemi dans cet embarras, il met le pied sur le bout inférieur de l'angon et le retient; sous cet pression; le bouclier est entraîné, la main qui le porte cède et laisse nue la tête et la poitrine. Le Franc saisit alors son adversaire sans défense et le tue aisément avec son épée ou son scramasax."
    else:
        "Vous vous entrainez au combat."
    $ AjouterACarac(metier.Guerrier.NOM, 1)
    jump fin_cycle
