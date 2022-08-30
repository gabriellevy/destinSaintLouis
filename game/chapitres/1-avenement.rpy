
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
        croisadeAlbigeois = dec_histo.DecHistoDatePreciseU(proba.Proba(0.9, False), "croisadeAlbigeois", temps.DateGregorienne(30, 1, 1226))
        croisadeAlbigeois.AjouterCondition(estPasRoi)
        selecteur_.ajouterDeclencheur(croisadeAlbigeois)
        # avènement
        avenement = dec_histo.DecHistoU(proba.Proba(0.6, False), "avenement", 1226)
        avenement.AjouterCondition(estPasRoi)
        selecteur_.ajouterDeclencheur(avenement)

label croisadeAlbigeois:
    menu:
        "croisade albigeois"
        "ok":
            pass
    "Votre père Louis VIII le lion a courageusement pris la croix pour aller extirper l'hérésie cathare du Sud."

    jump fin_cycle


label avenement:
    scene bg priere
    with dissolve
    play music roi_mort noloop
    # A FAIRE : trouver un fond pour le couronnement
    show screen valeurs_traits
    $ papa = situation_.GetValCarac(C_PERE)
    $ papa.Tuer()
    # enterrement de Louis VIII
    "Votre glorieux père Louis vient de mourir." # Louis VIII le lion
    "A FAIRE : avènement"
    # avènement => maman régente

    # royaume de Louis à son avènement
    "A FAIRE : afficher carte et décrire royaume"
    "Grâce à votre père mais surtout grace à Philippe Auguste votre grand-père votre domaine est très vaste."
    "Les caisses sont pleines, le royaume est riche, solide et bien organisé. À vous de vous rendre digne de cet héritage somptueux."
    # $ AfficherCarteActuelle()
    # with dissolve

    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Roi.NOM)
    jump fin_cycle
