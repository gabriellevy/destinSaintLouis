init -5 python:
    import random
    from abs.religions import religion
    from spe import dec_histo
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite import trait
    from abs.humanite import metier

    def AjouterEvtsHistoire():
        global selecteur_
        # Écu d'or
        ecuDOr = dec_histo.DecHistoU(proba.Proba(0.3, True), "ecuDOr", 1226)
        selecteur_.ajouterDeclencheur(ecuDOr)

label ecuDOr:
    scene bg ecu
    "Votre royaume est plus riche que jamais. Vous pouvez enfin accomplir un vieux rêve des rois de France."
    "La monnaie d'or n'était plus frappée depuis Charlemagne. Vous la rétablissez enfin en Occident en créant l'Écu d'or."
    menu:
        "tmp ecuDOr"
        "ok":
            pass
    jump fin_cycle
