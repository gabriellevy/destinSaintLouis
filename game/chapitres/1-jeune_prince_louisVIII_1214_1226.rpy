
init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite import trait
    from abs.humanite import metier
    from abs.univers import temps
    # from geographie import quartier
    from abs.humanite import identite
    from spe import dec_histo

    estPasRoi = condition.Condition(metier.Metier.C_METIER, metier.Roi.NOM, condition.Condition.DIFFERENT)
    estRoi = condition.Condition(metier.Metier.C_METIER, metier.Roi.NOM, condition.Condition.EGAL)

    def AjouterEvtAvenement():
        global selecteur_
        # croisadeAlbigeois
        croisadeAlbigeois = dec_histo.DecHistoDatePreciseU(proba.Proba(1.0, False), "croisadeAlbigeois", temps.DateGregorienne(30, 1, 1226))
        selecteur_.ajouterDeclencheur(croisadeAlbigeois)
        # croisadeAlbigeois_2
        croisadeAlbigeois_2 = dec_histo.DecHistoDatePreciseU(proba.Proba(1.0, False), "croisadeAlbigeois_2", temps.DateGregorienne(1, 8, 1226))
        selecteur_.ajouterDeclencheur(croisadeAlbigeois_2)
        # croisadeAlbigeois_3
        croisadeAlbigeois_3 = dec_histo.DecHistoDatePreciseU(proba.Proba(1.0, False), "croisadeAlbigeois_3", temps.DateGregorienne(1, 10, 1226))
        selecteur_.ajouterDeclencheur(croisadeAlbigeois_3)
        # mort_louis_VIII
        mort_louis_VIII = dec_histo.DecHistoDatePreciseU(proba.Proba(1.0, False), "mort_louis_VIII", temps.DateGregorienne(8, 11, 1226))
        selecteur_.ajouterDeclencheur(mort_louis_VIII)

label croisadeAlbigeois:
    scene bg chevaliers
    play music epique_principale
    "Votre père Louis VIII le lion a courageusement pris la croix pour aller extirper l'hérésie cathare du Sud. Il est en route vers la Provence"
    jump fin_cycle

label croisadeAlbigeois_2:
    scene bg chevaliers
    "Votre vaillant père Louis vient de capturer la ville d'Avignon qui résistait à sa croisade. Il envahit maintenant le Languedoc pour obtenir sa soumission."
    jump fin_cycle

label croisadeAlbigeois_3:
    scene bg chevaliers
    "Avec l'aide de Dieu le roi Louis a obtenu la soumission de la Provence et du Languedoc. L'hérésie cathare est éliminée."
    "Mais sur le chemin du retour il est tombé gravement malade."
    jump fin_cycle

label mort_louis_VIII:
    scene bg priere
    with dissolve
    play music roi_mort noloop
    "Votre glorieux père est mort des suites de la maladie qu'il a contracté lors de sa croisade. Il était bien jeune à 39 ans et vous l'avez peu connu."
    # enterrement de Louis VIII
    "Vous n'avez vous-même que 12 ans qu'allez vous devenir ?"
    jump mort_louis_VIII_2

label mort_louis_VIII_2:
    # A FAIRE : trouver un fond pour le couronnement
    show screen valeurs_traits
    $ papa = situation_.GetValCarac(C_PERE)
    $ papa.Tuer()
    bl "Sois courageux, Louis. Ton père est mort. Mais nul doute qu'après toutes ses bonnes actions et sa piété, le Saint père l'accueillera à ses côtés."
    bl "Tu es trop jeune pour devenir roi mais ne crains rien. Les conseillers de ton père sont des hommes bons et nobles, ils vont faire au mieux."
    bl "Ton oncle Philippe Hurepel ne peut ni ne doit être roi, c'est ta destinée de fils aîné. Pour éviter qu'il ne prenne trop d'importance il ne sera pas régent du royeaume, sinon il risquerait de prendre ton dû."
    bl "C'est moi, ta mère, qui vait prendre la tête du royaume en attendant ta majorité. Je te formerai et j'écouterai les sages des conseillers."
    menu:
        "As tu bien compris ?"
        "Oui":
            "A FAIRE"
            jump regence
        "Non":
            "A FAIRE"
            jump regence
    jump regence
