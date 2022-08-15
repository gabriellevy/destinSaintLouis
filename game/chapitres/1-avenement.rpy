
init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite import trait
    from abs.humanite import pnj
    from abs.humanite import metier
    from abs.univers import temps
    # from geographie import quartier
    from abs.humanite import identite
    from spe import dec_histo

    estPasRoi = condition.Condition(metier.Metier.C_METIER, metier.Roi.NOM, condition.Condition.DIFFERENT)
    estRoi = condition.Condition(metier.Metier.C_METIER, metier.Roi.NOM, condition.Condition.EGAL)

    def AjouterEvtAvenement():
        global selecteur_
        avenement = dec_histo.DecHistoU(proba.Proba(0.6, False), "avenement", 1226)
        avenement.AjouterCondition(estPasRoi)
        selecteur_.ajouterDeclencheur(avenement)

label avenement:
    scene bg priere
    with dissolve
    play music roi_mort noloop
    # A FAIRE : trouver un fond pour le couronnement
    show screen valeurs_traits
    $ papa = situation_.GetValCarac(pnj.Pnj.C_PERE)
    $ papa.Tuer()
    # enterrement de Louis VIII
    "Votre glorieux père Louis vient de mourir."
    "A FAIRE : avènement"
    # avènement => maman régente

    # royaume de Louis à son avènement
    "A FAIRE : afficher carte et décrire royaume"
    # $ AfficherCarteActuelle()
    # with dissolve

    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Roi.NOM)
    jump fin_cycle
