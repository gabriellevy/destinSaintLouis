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
        "evtRien1", "evtRien2", "evtRien3", "evtRien4", "evtRien5", "evtRien6", "evtRien7"
        ]
        scenesParDefaut = []
        musiquesAEnquiller = []

        # rien selon époque / âge
        ageLouis = situation.AgeEnAnnees()
        # evts rien de l'enfance
        if ageLouis <= 18:
            evtsVides_.append("evtRien_enfant1")
            evtsVides_.append("evtRien_enfant2")
            evtsVides_.append("evtRien_enfant3")
            evtsVides_.append("evtRien_enfant4")
            evtsVides_.append("evtRien_enfant5")
            evtsVides_.append("evtRien_enfant6")

        # christianisme
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

label evtRien_enfant1:
    "Aujourd'hui encore, alors que votre petit frère Charles vous a brutalisé, votre mère prend sa défense. Pourquoi le préfère-t'elle à vous qui êtes tellement plus sage ?"
    jump fin_cycle

label evtRien_enfant2:
    "Votre père est un grand chevalier dont vous êtes fier. Mais il passe tellement de temps à guerroyer que vous le voyez très rarement."
    jump fin_cycle

label evtRien_enfant3:
    scene bg education_saint_louis
    "Vos maîtres vous apprennent les rudiments du savoir. Vous avez des précepteurs de lecture, écriture, et calcul."
    jump fin_cycle

label evtRien_enfant4:
    scene bg education_saint_louis
    "Vos maîtres en arts libéraux vous apprennent la grammaire, la rhétorique, la philosophie et la logique."
    jump fin_cycle

label evtRien_enfant5:
    scene bg education_saint_louis
    "Vous adorez vous promener dans les bois. Vous aimez aussi les jeux sur l'eau, comme de ramer sur les rivières."
    jump fin_cycle

label evtRien_enfant6:
    scene bg enfant_louis_a_la_messe
    "Vous suivez la messe avec attention, comme votre mère Blanche le souhaite."
    jump fin_cycle

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
    "Les marchands du sud amènent dans les marchés des marchandises exotiques prisées : huile d'olives, soieries, épices..."
    jump fin_cycle

label evtRien7:
    scene bg galaad
    with Dissolve(.5)
    "La légende des chevaliers de la table ronde est devenue très célèbre et très populaire grâces aux fabuleux romans de chrétien de Troyes. Tout bon chevalier rêve d'atteindre les idéaux qu'elle décrit."
    jump fin_cycle
    
