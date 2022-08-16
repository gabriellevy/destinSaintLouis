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

    def AjouterEvtsMongols():
        global selecteur_
        # mongols, événements classiques
        mongols = dec_histo.DecHisto(proba.Proba(0.2, True), "mongols", 1240)
        selecteur_.ajouterDeclencheur(mongols)

label mongols:
    $ niveauMongols = situation_.GetValCaracInt("niveauMongols")
    if niveauMongols == 0:
        $ situation_.SetValCarac("niveauMongols", 1)
        "Les impôts rentrent bien."
    else:
        "Même si les mongols continuent à terrifier le peuple, ils ne semblent plus menaçants envers la chrétienté."
    jump fin_cycle
