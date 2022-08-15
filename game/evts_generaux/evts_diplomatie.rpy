init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite import trait
    from abs.humanite import metier
    from chapitres.classes import heros
    from spe import dec_histo

    diplomatieSup0 = condition.Condition(heros.Heros.C_DIPLOMATIE, 0, condition.Condition.SUPERIEUR)
    def AjouterEvtsDiplomatie():
        global selecteur_
        # joueur de citharède
        # citharede = dec_histo.DecHistoU(proba.Proba(0.08, True), "citharede", 483)
        # citharede.AjouterCondition(estRoi)
        # citharede.AjouterCondition(diplomatieSup0)
        # selecteur_.ajouterDeclencheur(citharede)

# label citharede:
    # scene bg citharede
    # "Théodoric vous a envoyé comme présent un joueur de citharède, un instrument à corde très rare en Gaule."
    # "Voilà qui égayera vos repas et réceptions, et augmentera le prestige de votre cour."
    # $ AjouterACarac(heros.Heros.C_GLOIRE, 1)
    # jump fin_cycle
