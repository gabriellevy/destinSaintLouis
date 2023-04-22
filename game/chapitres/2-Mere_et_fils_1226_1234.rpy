
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

    a19ans = condition.Condition(temps.Date.AGE_ANNEES, 19, condition.Condition.SUPERIEUR_EGAL)

label regence:
    scene bg regence
    "Vous êtes maintenant roi, mais trop jeune pour régner. Votre mère Blanche prend les rènes avec énergie."
    show blanche at left
    with moveinleft
    bl "Mon fils, j'aimerais mieux vous voir mort que coupable d'un seul péché mortel."
    jump fin_cycle

label avenement:
    # royaume de Louis à son avènement
    "A FAIRE : afficher carte et décrire royaume"
    "Grâce à votre père mais surtout grace à Philippe Auguste votre grand-père votre domaine est très vaste."
    "Les caisses sont pleines, le royaume est riche, solide et bien organisé. À vous de vous rendre digne de cet héritage somptueux."
    # $ AfficherCarteActuelle()
    # with dissolve
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Roi.NOM)
    jump fin_cycle
