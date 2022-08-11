# fichier où sont générés les phrases d'ambiance à afficher quand il ne se passe rien durant un mois particulier

init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite import trait
    from abs.univers import temps
    # from religions import religion
    # from geographie import quartier

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
        "evtRien13", "evtRien14", "evtRien15", "evtRien16", "evtRien17",
        "evtRien18", "evtRien19", "evtRien20"
        ]
        scenesParDefaut = []
        musiquesAEnquiller = []

        # selon religion
        religionActuelle = situation_.GetValCarac(religion.Religion.C_RELIGION)
        valChrist = situation_.GetValCarac(heros.Heros.C_CHRISTIANISME)
        if religionActuelle == religion.Christianisme.NOM:
            # evts
            evtsVides_.append("evtRien_saints")
            evtsVides_.append("evtRien_ChristianismeMerovingien_1")
            # images
            scenesParDefaut.append("bg crucifixion")
            # musiques
            musiquesAEnquiller.append("musique/journeytoabsolution.ogg")
        if religionActuelle == religion.Paien.NOM:
            evtsVides_.append("evtRien_paien1")
            evtsVides_.append("evtRien_paien2")
            evtsVides_.append("evtRien_paien3")
            evtsVides_.append("evtRien_paien4")
            evtsVides_.append("evtRien_paien5")
            evtsVides_.append("evtRien_paien6")
            scenesParDefaut.append("bg chevauchee_paienne")
            musiquesAEnquiller.append("musique/Quite An Adventure.ogg")
            if valChrist >= 8:
                evtsVides_.append("evtRien_paien_Christianisme_1")
                scenesParDefaut.append("bg crucifixion")

        # si gloire faible et pas marie
        marieAClothilde = situation_.GetValCarac(heros.Heros.C_MARIE_CLOTHILDE)
        if marieAClothilde != 1:
            evtRien_pasMarie = situation_.GetValCarac("evtRien_pasMarie")
            if evtRien_pasMarie != 1:
                evtsVides_.append("evtRien_pasMarie")

        # alboflède
        if situation_.GetValCaracInt(heros.Heros.C_ALBOFLEDE) == 1:
            evtsVides_.append("evtRien_alboflede")

        # loi salique promulguée
        if situation_.GetValCaracInt(heros.Heros.C_LOI_SALIQUE) == 1:
            evtsVides_.append("evtRien_loi_salique_1")
            evtsVides_.append("evtRien_loi_salique_2")

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

        # alamans
        if situation_.GetValCarac(germains.Alamans.C_VAINCU) != 1:
            evtsVides_.append("evtRien_alamans")


        # -----------------------------------------------------------------------------
        if len(evtsVides_) == 0:
            evtsVides_ = ["evtRien1", "evtRien2" ]

        if len(scenesParDefaut) == 0:
            sceneParDefaut = "bg cours_merovingienne"

        # ajoute une musique à la file au hasard :
        if len(musiquesAEnquiller) != 0:
            renpy.music.queue(random.choice(musiquesAEnquiller), clear_queue=False)

        # fond
        if sceneParDefaut != "":
            renpy.scene()
            renpy.show(random.choice(scenesParDefaut))
        # en lance un au hasard
        renpy.jump(random.choice(evtsVides_))

label evtRien_ChristianismeMerovingien_1:
    "Les conciles désapprouvent que les fidèles chantent des chansons d'amour dans les églises. Ils imposent le chant des psaumes."
    jump fin_cycle

label evtRien_loi_salique_1:
    $ femme = francs_.CreerPrenom(False)
    $ homme = francs_.CreerPrenom(True)
    "[femme] a été reconnue coupable de l'empoisonnement de [homme] par potion magique. Elle voulait apparemment le rendre stérile par vengeance."
    "Il est en piteux état mais se remet, espérons qu'il pourra encore procréer. La coupable doit lui payer l'énorme somme de 200 sous stipulée dans la loi salique."
    "Autrement il aura légalement le droit de se venger. Comme elle n'a pas les moyens de payer il inévitable que [homme] ou un membre de son clan se venge tôt ou tard."
    jump fin_cycle

label evtRien_loi_salique_2:
    $ perso1 = francs_.CreerPrenom(True)
    $ perso2 = francs_.CreerPrenom(True)
    "[perso1] a coupé la main de [perso2] dans une rixe d'ivrognes. [perso2] est grandement diminué et sa famille a le droit d'invoquer la faide (vendetta) pour se venger."
    "La loi salique stipule tout de même que [perso1] doit payer 100 sous de dédomagement et que si [perso2] accepte la faide est annulée."
    "Comme [perso2] est diminué et n'a qu'une famille faible et peu nombreuse il préfère accepter le dédomagement."
    jump fin_cycle

label evtRien_paien_Christianisme_1:
    scene bg crucifixion
    "Vous êtes de plus en plus intéressé par le christianisme mais la crucifixion du christ vous semble toujours aussi innaceptable."
    "Si vous et vos francs aviez été là vous auriez vengé cette injure. Alors pourquoi son père, un Dieu soit disant tout puissant n'a-t-il rien fait ?"
    jump fin_cycle

label evtRien_paien_Christianisme_2:
    scene bg crucifixion
    "Le tombeau de Saint Martin de Tours est devenu un lieu de pélerinage très populaire chez les chrétiens. Les miracles y sont nombreux."
    jump fin_cycle

label evtRien_alamans:
    $ AfficherCarteActuelle()
    "Vous recevez régulièrement des rapports et des plaintes pour les exactions des alamans à l'est."
    "Les burgondes et les francs de l'Est les contiennent pour l'instant mais tôt ou tard il faudra les calmer."
    jump fin_cycle

label evtRien_paien1:
    scene bg chevauchee_paienne
    with dissolve
    "Parfois vous vous demandez pourquoi l'empire romain qui battit autrefois les francs et même tous les peuples germains, subit maintenant tant de défaites."
    "Certains disent que depuis que les romains sont devenus chrétiens et ont supprimé les autels de la déesse de la victoire au sénat, leurs dieux les ont abandonnés."
    "Mais si cela est vrai, pourquoi les goths, qui ont abandonné Wotan et sont devenus chrétiens ariens, sont pourtant aujourd'hui les plus puissants de vos rivaux ?"
    jump fin_cycle

label evtRien_paien2:
    scene bg chevauchee_paienne
    with dissolve
    "Chez les francs le roi reste seul sur son cheval blanc en première ligne au milieu de ses hommes à pied. Ainsi il inspire ses guerriers et prouve en s'exposant que Wotan le protège des traits ennemis."
    jump fin_cycle

label evtRien_paien3:
    scene bg chevauchee_paienne
    with dissolve
    "Les chrétiens désapprouvent fermement l'incinération des défunts que vos francs pratiquent régulièrement. Vous ne comprenez guère leurs arguments."
    jump fin_cycle

label evtRien_paien4:
    scene bg chevauchee_paienne
    with dissolve
    "Vous avez eu récemment une suite de coups du sort préocuppants. Ils pourrait s'agir de malédictions lancées par un de vos ennemis."
    "Vous faites fabriquer des objets marqués de runes par vos forgerons et vos magiciens."
    jump fin_cycle

label evtRien_paien5:
    scene bg chevauchee_paienne
    with dissolve
    "Les devins annoncent que cette année la fortune vous souriera."
    jump fin_cycle

label evtRien_paien6:
    scene bg chevauchee_paienne
    with dissolve
    "C'est jeudi. Les dieux exigent que ce soit un jour férié."
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

label evtRien_alboflede:
    scene bg cours_merovingienne
    with dissolve
    show alboflede at right
    with moveinright
    albo "Pas trop de soucis aujourd'hui mon frère ?"
    cl "Non, un jour calme et un temps trop mauvais pour la chasse. Mais par contre idéal pour passer la journée au coin du feu en famille."
    albo "Nous ne sommes donc que votre troisième choix. C'est déjà plutôt honorable je peux m'en contenter."
    "Sa finesse d'esprit et sa douceur font de votre grande soeur Alboflède le meilleur moyen d'illuminer une journée pluvieuse. Vous passez finalement une très bonne journée."
    jump fin_cycle

label evtRien1:
    with Dissolve(.5)
    $ romain = random.randint(0,1)
    $ nomPerso = gaulois_.CreerPrenom(True)
    $ nomFaction = "gaulois"
    if romain == 0:
        $ nomPerso = romains_.CreerPrenom(True)
        $ nomFaction = "romain"
    "[nomPerso], un riche [nomFaction] vient de mourir. Très pieux, il fait don de l'essentiel de sa fortune à l'église. Il a aussi affranchi une grande partie de ses esclaves."
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

label evtRien14:
    scene bg ludus
    with Dissolve(.5)
    "Après les avoir méprisés un temps les francs ont commencé à apprécier les multiples jeux des romains. Vous avez un faible pour le ludus duodecim scriptorum."
    jump fin_cycle

label evtRien15:
    with Dissolve(.5)
    $ nomEsclave = gaulois_.CreerPrenom(True)
    "Un esclave des cuisines nommé [nomEsclave] s'est enfui et a été rattrapé pour la 3ème fois !"
    "Le chef des cuisines a fini par perdre patience et lui a coupé l'oreille."
    jump fin_cycle

label evtRien16:
    with Dissolve(.5)
    $ nom = francs_.CreerPrenom(True)
    "Comme tous les mois la justice populaire franque est rendue sur le marlberg (tumulus)."
    "[nom], accusé et condamné pour vol, a refusé la sentence et s'est enfui. Il a été maudit par le conseil et tout le monde a maintenant le droit et le devoir de le poursuivre et de planter sa tête sur un pieu."
    jump fin_cycle

label evtRien17:
    with Dissolve(.5)
    "Les moulins à eau se multiplient dans vos campagnes. Cet édifice ingénieux utilise la force du courant pour actionner la meule."
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

label evtRien_pasMarie:
    with Dissolve(.5)
    # si pas marié à Clothilde
    $ situation_.SetValCarac("evtRien_pasMarie", 1)
    "C'est par la gloire militaire qu'un chef franc devient digne de faire un mariage prestigieux."
    "C'est parce que votre père Childéric était un grand guerrier que votre mère Basine a préféré abandonner son époux médiocre pour rejoindre votre père et vous donner naissance."
    "Seule la victoire à la guerre vous rendra digne d'eux."
    jump fin_cycle
