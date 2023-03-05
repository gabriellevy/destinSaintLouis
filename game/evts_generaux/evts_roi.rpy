init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import modifProba
    from abs import condition
    from abs.humanite import trait
    from abs.humanite import metier
    from chapitres.classes import heros

    fidelitePeupleMoinsQue0 = condition.Condition(heros.Heros.C_FIDELITE_PEUPLE, 0, condition.Condition.INFERIEUR)
    fidelitePeupleMoinsQue2 = condition.Condition(heros.Heros.C_FIDELITE_PEUPLE, 2, condition.Condition.INFERIEUR)
    fidelitePeuplePlusQue0 = condition.Condition(heros.Heros.C_FIDELITE_PEUPLE, 0, condition.Condition.SUPERIEUR)
    fidelitePeuplePlusQue2 = condition.Condition(heros.Heros.C_FIDELITE_PEUPLE, 2, condition.Condition.SUPERIEUR)
    fidelitePeuplePlusQue3 = condition.Condition(heros.Heros.C_FIDELITE_PEUPLE, 3, condition.Condition.SUPERIEUR)
    richessePlusQue0 = condition.Condition(trait.Richesse.NOM, 0, condition.Condition.SUPERIEUR)
    armeeMoinsQue2 = condition.Condition(heros.Heros.C_MILITAIRE, 2, condition.Condition.INFERIEUR)
    armeeMoinsQue5 = condition.Condition(heros.Heros.C_MILITAIRE, 2, condition.Condition.INFERIEUR)

    def AjouterEvtsRoi():
        global selecteur_
        # remplacement de comte
        comtCritique = declencheur.Declencheur(proba.Proba(0.03, True), "comtCritique")
        comtCritique.AjouterCondition(estRoi)
        selecteur_.ajouterDeclencheur(comtCritique)
        # nommage de comte
        nommageComte = declencheur.Declencheur(proba.Proba(0.02, True), "nommageComte")
        nommageComte.AjouterCondition(estRoi)
        selecteur_.ajouterDeclencheur(nommageComte)
        # gestion du pillage
        gestionPillage = declencheur.Declencheur(proba.Proba(0.02, True), "gestionPillage")
        gestionPillage.AjouterCondition(estRoi)
        selecteur_.ajouterDeclencheur(gestionPillage)
        # recrutement
        probarecrutement = proba.Proba(0.02, True)
        modifProbarecrutement = modifProba.ModifProba(0.06, armeeMoinsQue2)
        probarecrutement.ajouterModifProba(modifProbarecrutement)
        recrutement = declencheur.Declencheur(probarecrutement, "recrutement")
        recrutement.AjouterCondition(richessePlusQue0)
        recrutement.AjouterCondition(armeeMoinsQue5)
        recrutement.AjouterCondition(estRoi)
        selecteur_.ajouterDeclencheur(recrutement)
        # impôts
        impots = declencheur.Declencheur(proba.Proba(0.05, True), "impots")
        impots.AjouterCondition(estRoi)
        selecteur_.ajouterDeclencheur(impots)
        # corruption
        corruption = declencheur.Declencheur(proba.Proba(0.05, True), "corruption")
        corruption.AjouterCondition(estRoi)
        selecteur_.ajouterDeclencheur(corruption)
        # revolte_impots
        revolte_impots = declencheur.Declencheur(proba.Proba(0.04, True), "revolte_impots")
        revolte_impots.AjouterCondition(estRoi)
        revolte_impots.AjouterCondition(fidelitePeupleMoinsQue0)
        selecteur_.ajouterDeclencheur(revolte_impots)
        # rentree_dimpots
        rentree_dimpots = declencheur.Declencheur(proba.Proba(0.04, True), "rentree_dimpots")
        rentree_dimpots.AjouterCondition(estRoi)
        rentree_dimpots.AjouterCondition(fidelitePeuplePlusQue0)
        selecteur_.ajouterDeclencheur(rentree_dimpots)

label rentree_dimpots:
    "Les impôts rentrent bien."
    menu:
        "Qu'allez-vous faire de cette rentrée d'argent."
        "Investir dans l'armée":
            $ AjouterACarac(heros.Heros.C_MILITAIRE, 1)
        "Garder cela dans vos coffres":
            $ AjouterACarac(trait.Richesse.NOM, 1)
        "Organiser des festivals pour le peuple":
            $ AjouterACarac(heros.Heros.C_FIDELITE_PEUPLE, 1)
    jump fin_cycle

label revolte_impots:
    "Il est de plus en plus dur de lever des impôts. Cete fois les paysans se rebellent et refusent de payer."
    $ testCombat = testDeCarac.TestDeCarac(heros.Heros.C_MILITAIRE, 3, situation_)
    $ testPolitique = testDeCarac.TestDeCarac(metier.Politique.NOM, 6, situation_)
    menu:
        "Comment gérez-vous cette révolte ?"
        "Leur accorder une dispense exceptionnelle.":
            $ RetirerACarac(trait.Richesse.NOM, 1)
            $ AjouterACarac(heros.Heros.C_FIDELITE_PEUPLE, 1)
        "Envoyer l'armée les réprimer [testCombat.affichage_]":
            $ reussi = testCombat.TesterDifficulte(situation_)
            if reussi:
                "Après quelques exécutions et granges brûlées les paysans sont vite calmés."
            else:
                "Les rebelles sont étonnament coriaces. Non seulement ils ne payent pas mais ils humilient vos soldats durant quelques escarmouches sanglantes."
                $ RetirerACarac(heros.Heros.C_GLOIRE, 1)
        "Négocier avec les notables pour calmer les tensions [testPolitique.affichage_]":
            $ reussi = testPolitique.TesterDifficulte(situation_)
            if reussi:
                "Après quelques dures négociations la révolte se calme pacifiquement."
            else:
                "Les rebelles pendent un de vos négociateurs et trainent votre nom dans la boue."
                $ RetirerACarac(heros.Heros.C_GLOIRE, 1)
    jump fin_cycle

label corruption:
    scene bg cours
    with dissolve
    $ testImpots = testDeCarac.TestDeCarac([metier.Politique.NOM, heros.Heros.C_FIDELITE_PEUPLE], 5, situation_)
    menu:
        " "
        "Administrer le pays [testImpots.affichage_]":
            $ reussi = testImpots.TesterDifficulte(situation_)
            if reussi:
                "Votre administration est fiable et la corruption très faible."
            else:
                "Vos fonctionnaires vous volent vous en êtes sûr. Il va falloir sévir."
                $ RetirerACarac(trait.Richesse.NOM, 1)
    jump fin_cycle

label recrutement:
    scene bg cours
    with dissolve
    menu:
        "Vous êtes assez riche pour renforcer vos armées avec des mercenaires si vous le souhaitez."
        "Oui":
            $ RetirerACarac(trait.Richesse.NOM, 1)
            $ AjouterACarac(heros.Heros.C_MILITAIRE, 1)
        "Non":
            pass

    jump fin_cycle

label impots:
    scene bg cours
    with dissolve
    $ testImpots = testDeCarac.TestDeCarac([metier.Politique.NOM, heros.Heros.C_FIDELITE_PEUPLE], 5, situation_)
    menu:
        "Allez vous réussir à pousser les paysans à vous payer des impôts ?"
        "[testImpots.affichage_]":
            $ reussi = testImpots.TesterDifficulte(situation_)
            if reussi:
                "Grâce à vos efforts en sa faveur le peuple vous est favorable et suit vos lois. Les impôts rentrent."
                $ AjouterACarac(trait.Richesse.NOM, 1)
            else:
                "Les paysans sont sournois et désobéissants. Malgré vos efforts les rendements des impôts sont médiocres."
                menu:
                    "Voulez vous autoriser vos soldats à piller quelques villes pour leur apprendre à obéir ?"
                    "Oui":
                        "Les pillages vous rapportent et défoulent vos soldats mais le peuple vous déteste encore plus."
                        $ AjouterACarac(trait.Richesse.NOM, 1)
                        $ RetirerACarac(heros.Heros.C_FIDELITE_PEUPLE, 2)
                        $ RetirerACarac(heros.Heros.C_SAINTETE, 5)
                        $ AjouterACarac(heros.Heros.C_FIDELITE_ARMEE, 1)
                    "Non":
                        pass
    jump fin_cycle

label gestionPillage:
    scene bg cours
    with dissolve
    $ nom = francs_.CreerPrenom(True)
    "Le bourgmestre [nom] vient à vous se plaindre humblement des pillages causés par vos guerriers et vous demande d'y mettre un terme."
    menu:
        "Interdire le pillage sous peine de mort":
            "Les soldats prennent très mal cet affront à leurs habitues. Ils doivent acheter et entretenir leur propre matériel. À quoi bon si ils ne peuvent pas se payer sur les vaincus ?"
            $ RetirerACarac(heros.Heros.C_FIDELITE_ARMEE, 2)
            $ AjouterACarac(heros.Heros.C_FIDELITE_PEUPLE, 2)
            jump fin_cycle
        "Réprimander les soldats":
            "Les guerriers prennent mal la réprimande. Ils doivent acheter et entretenir leur propre matériel. À quoi bon si ils ne peuvent pas se payer sur les vaincus ?"
            $ RetirerACarac(heros.Heros.C_FIDELITE_ARMEE, 1)
            $ AjouterACarac(heros.Heros.C_FIDELITE_PEUPLE, 1)
            jump fin_cycle
        "Le renvoyer sèchement. Vae Victis !":
            $ RetirerACarac(heros.Heros.C_FIDELITE_PEUPLE, 1)
            jump fin_cycle
        "L'exécuter pour son insolence":
            $ RetirerACarac(heros.Heros.C_FIDELITE_PEUPLE, 2)
            $ RetirerACarac(heros.Heros.C_SAINTETE, 10)
            jump fin_cycle

    jump fin_cycle

label comtCritique:
    scene bg cours
    with dissolve
    $ nomComte = francs_.CreerPrenom(True)
    "Le comte [nomComte] à votre service se comporte paraît-til comme un brigand. Il vole et frappe ses sujets et les plaintes s'accumulent."
    "Il est par contre d'une fidélité à toute épreuve envers vous et fait rentrer les impôts très efficacement."
    menu:
        "Le réprimander publiquement":
            "Les galloromains apprécident de voir que leurs demandes sont entendues. Le comte [nomComte] n'ose plus les pressurer autant qu'avant."
            $ AjouterACarac(heros.Heros.C_FIDELITE_PEUPLE, 1)
            $ RetirerACarac(trait.Richesse.NOM, 1)
            jump fin_cycle

        "Le faire exécuter":
            "Le peuple est satisfait de voir son tourmenteur mort, mais les autres comtes sont terrifiés de voir que la fidélité envers vous ne leur garantit pas votre clémence."
            $ RetirerACarac(trait.Richesse.NOM, 1)
            $ RetirerACarac(heros.Heros.C_FIDELITE_NOBLES, 1)
            $ AjouterACarac(heros.Heros.C_FIDELITE_PEUPLE, 2)
            jump fin_cycle

        "le laisser agir à sa guise tant que les impôts entrent":
            "Le peuple est écrasé mais l'argent coule à flot."
            $ AjouterACarac(trait.Richesse.NOM, 1)
            $ RetirerACarac(heros.Heros.C_FIDELITE_PEUPLE, 2)
            jump fin_cycle

        "le remplacer discrètement":
            "Les galloromains apprécident de voir que leurs demandes sont entendues."
            $ AjouterACarac(heros.Heros.C_FIDELITE_PEUPLE, 1)
            $ RetirerACarac(trait.Richesse.NOM, 1)
            jump nommageComte
    jump fin_cycle


label nommageComte:
    scene bg cours
    with dissolve
    $ nomComte1 = francs_.CreerPrenom(True)
    $ nomComte2 = francs_.CreerPrenom(True)
    $ nomComte3 = francs_.CreerPrenom(True)
    $ nomComte4 = francs_.CreerPrenom(True)
    "Le bailli est un fonctionnaire de haut rang responsable entre autres de la collecte des impôts."
    menu:
        "Qui allez vous nommer ?"
        "[nomComte1], un noble juste et intransigeant":
            $ AjouterACarac(heros.Heros.C_FIDELITE_NOBLES, 1)
            jump fin_cycle
        "[nomComte2], un bourgeois notable respecté":
            $ AjouterACarac(heros.Heros.C_FIDELITE_PEUPLE, 1)
            jump fin_cycle
        "[nomComte3], un roturier malin et dévoué qui saura faire rentrer les impôts":
            "[nomComte3] est en effet doué et efficace mais il se fait vite détester par tout le royaume."
            $ RetirerACarac(heros.Heros.C_FIDELITE_PEUPLE, 1)
            $ RetirerACarac(heros.Heros.C_FIDELITE_NOBLES, 1)
            $ AjouterACarac(trait.Richesse.NOM, 1)
            jump fin_cycle
        "[nomComte4], un ancien officier, spécialiste du recrutement":
            $ AjouterACarac(heros.Heros.C_MILITAIRE, 1)
            $ AjouterACarac(heros.Heros.C_FIDELITE_ARMEE, 1)
            jump fin_cycle
    jump fin_cycle
