# fichier où sont générés les phrases d'ambiance à afficher quand il ne se passe rien durant un mois particulier

init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite import trait
    from abs.univers import temps

    def AjouterEvtsRien():
        global selecteur_, situation_
        selecteurDEvenementVide = declencheur.Declencheur(1.0, "selecteurDEvenementVide")
        selecteur_.ajouterDeclencheur(selecteurDEvenementVide)

    def LancerEvtVide(situation):
        sceneParDefaut = ""
        # régénère les événements compatibles avec la situation
        evtsVides_ = [
        "evtRien1", "evtRien2", "evtRien3", "evtRien4", "evtRien5", "evtRien6", "evtRien7",
        "evtRien8", "evtRien9", "evtRien10", "evtRien11", "evtRien12",
        "evtRien13",
        "evtRien18", "evtRien19", "evtRien20"
        ]
        scenesParDefaut = []
        musiquesAEnquiller = []

        # selon religion
        # evts
        evtsVides_.append("evtRien_saints")
        # images
        scenesParDefaut.append("bg crucifixion")
        # musiques
        musiquesAEnquiller.append("musique/journeytoabsolution.ogg")

        # saison
        saison = situation.GetDateDuJour().GetSaison()
        if saison == temps.Date.PRINTEMPS:
            evtsVides_.append("evtRien1_printemps")
            musiquesAEnquiller.append("musique/Sea Season.ogg")
        if saison == temps.Date.HIVER:
            musiquesAEnquiller.append("musique/Dark Season.ogg")
        if saison == temps.Date.ETE:
            musiquesAEnquiller.append("musique/Fire Season.ogg")
        if saison == temps.Date.AUTOMNE:
            evtsVides_.append("evtRien1_automne")
            evtsVides_.append("evtRien2_automne")
            evtsVides_.append("evtRien3_automne")


        # -----------------------------------------------------------------------------
        if len(evtsVides_) == 0:
            evtsVides_ = ["evtRien1", "evtRien2" ]

        if len(scenesParDefaut) == 0:
            sceneParDefaut = "bg priere"

        # ajoute une musique à la file au hasard :
        if len(musiquesAEnquiller) != 0:
            renpy.music.queue(random.choice(musiquesAEnquiller), clear_queue=False)

        # fond
        if sceneParDefaut != "":
            renpy.scene()
            renpy.show(random.choice(scenesParDefaut))
        # en lance un au hasard
        renpy.jump(random.choice(evtsVides_))

label evtRien1_automne:
    "C'est l'époque des semailles d'orge."
    jump fin_cycle

label evtRien2_automne:
    "C'est l'époque des semailles de froment."
    jump fin_cycle

label evtRien3_automne:
    "C'est l'époque des semailles de seigle."
    jump fin_cycle

label evtRien1_printemps:
    "C'est l'époque des semailles d'avoine."
    jump fin_cycle

label selecteurDEvenementVide:
    $ LancerEvtVide(situation_)

label evtRien1:
    with Dissolve(.5)
    $ nomPerso = francs_.CreerPrenom(True)
    "[nomPerso], un riche propriétaire vient de mourir. Très pieux, il fait don de l'essentiel de sa fortune à l'église."
    jump fin_cycle

label evtRien2:
    with Dissolve(.5)
    "La production de cervoise est en plein essor."
    jump fin_cycle

label evtRien3:
    with Dissolve(.5)
    "Aujourd'hui le cuisinier vous a préparé un plat exotique méditerrannéen à base de fruits et qu'on appelle dattes."
    jump fin_cycle

label evtRien4:
    with Dissolve(.5)
    "Votre cuisinier prépare le mouton à merveille. Mais le sommet du repas reste le fromage avec le vin."
    jump fin_cycle

label evtRien5:
    with Dissolve(.5)
    "Aujourd'hui vous avez dû rédiger une importante lettre de votre main. Vous scellez la lettre de votre sceau grâce à votre anneau sigillaire."
    jump fin_cycle

label evtRien6:
    with Dissolve(.5)
    "Les gaulois sont peu combatifs et donc souvent méprisés par votre peuple car soumis et failes à dominer."
    "Vous devez néanmoins reconnaître qu'en artisanat et architecture ils sont largement supérieurs."
    "Ce sont des céramistes gaulois que vous chargez de la fabrication des bouteilles, cruches, bols et assiettes de votre palais car leur qualité est nettement supérieure."
    jump fin_cycle

label evtRien7:
    scene bg chasse
    with Dissolve(.5)
    "Vous vous faites construire un palais secondaire en bordure de forêt. Ainsi vous pourrez facilement aller chasser dès que l'envie vous en prendra."
    jump fin_cycle

label evtRien8:
    with Dissolve(.5)
    "Parmi les coutumes romaines les jeux de cirque sont toujours aussi populaires, même chez les francs."
    "Certes ceux qui se donnent en Gaule de nos jours sont loin d'être somptueux comme à Rome. Mais vous avez les moyens d'organiser des courses de char et même des combats de gladiateurs."
    jump fin_cycle

label evtRien9:
    with Dissolve(.5)
    "Les marchands du sud amènent dans vos marchés des machandises exotiques prisées : huile d'olives, soieries, épices..."
    jump fin_cycle

label evtRien10:
    with Dissolve(.5)
    "Les marchands du nord, de plus en plus nombreux, amènent sur vos marchés du bois, des tissus, des esclaves..."
    jump fin_cycle

label evtRien11:
    with Dissolve(.5)
    "Sur le modèle de l'empire romain vos serviteurs tiennent des comptes écris détaillés des opérations financières du royaume."
    jump fin_cycle

label evtRien12:
    with Dissolve(.5)
    "Les pirates esclavagistes ont du avoir de beaux succès en ratissant les côtes de la manche. Il y a une énorme quantité d'esclaves angles et saxons sur les marchés cette année."
    jump fin_cycle

label evtRien13:
    with Dissolve(.5)
    "Pour vous distraire et vous détendre vous vous prenez l'habitude de jouer aux osselets avec votre famille et vos amis."
    jump fin_cycle

label evtRien18:
    with Dissolve(.5)
    $ femmeFranque = francs_.CreerPrenom(False)
    "[femmeFranque] a été accusée de vol. Elle a accepté de subir l'ordalie."
    "Elle a plongé sa main dans un chaudron d'eau bouillante. Supportant la souffrance elle a réussi à saisir l'anneau qui s'y trouvait. Les juges ont ensuite attendu 3 jours et constaté que sa cicatrice est belle et bien formée."
    "[femmeFranque] est donc déclarée innocente du vol."
    jump fin_cycle

label evtRien19:
    with Dissolve(.5)
    "Depuis que les huns ont été repoussés de Gaule par vos ancêtres ils sont devenus bien moins agressifs et bien plus commerçants."
    "Ils ont introduit dans votre cour des objets d'orphèvrerie que vos propres artisans sont incapables de réaliser. Vous les poussez à apprendre à reproduire ces techniques."
    jump fin_cycle

label evtRien20:
    with Dissolve(.5)
    "La consignation de vos actes royaux et les formulaires de toute sortes nécessitent de fortes importations de papyrus d'Orient."
    jump fin_cycle
