init -5 python:
    import random
    from abs.religions import religion
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite import trait
    from abs.humanite import metier
    from spe import dec_histo

    def AjouterEvtsFamille():
        global selecteur_
        # naissance des enfants
        naissanceBlanche = dec_histo.DecHistoU(proba.Proba(0.3, True), "naissanceBlanche", 1240)
        selecteur_.ajouterDeclencheur(naissanceBlanche)
        # majorité des enfants ??
        # majoThierry = dec_histo.DecHistoU(proba.Proba(0.3, True), "majoThierry", 498) # 485 naissance + 13
        # selecteur_.ajouterDeclencheur(majoThierry)

label naissanceBlanche:
    "Votre premier enfant, votre fille Blanche, vient de naître !"
    jump fin_cycle
