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

    def AjouterEvtsReligion():
        global selecteur_
        
        traduireLatin = dec_histo.DecHistoU(proba.Proba(0.1, True), "traduireLatin", 1214)
        traduireLatin.AjouterCondition(estRoi)
        selecteur_.ajouterDeclencheur(traduireLatin)

label traduireLatin:
    scene bg education_saint_louis
    "Vous savez lire et parler latin. Mais vous êtes conscient que ce n'est pas le cas de l'écrasante majorité du peuple, même ceux qui savent lire."
    menu:
        "Voulez vous obliger les prêtres à traduire des ouvrages d'histoires et des sermons en français, à destination du peuple laïc ?"
        "Oui.":
            "Vous faites e particulier les chroniques latines, véritable mémoire du royaume de France. Le français va se répandre de plus en plus dans le royaume."
            $ AjouterACarac(heros.Heros.C_AMOUR_PEUPLE, 1)

        "Non cela coûterait trop cher et pourrait déplaire aux éclesiastiques.":
            $ RetirerACarac(trait.Richesse.NOM, 1)

    jump fin_cycle