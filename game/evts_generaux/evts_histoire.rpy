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
        ecuDOr.AjouterCondition(estRoi)
        selecteur_.ajouterDeclencheur(ecuDOr)
        # fin de l'ordalie
        ordalie = dec_histo.DecHistoU(proba.Proba(0.1, True), "ordalie", 0)
        ordalie.AjouterCondition(estRoi)
        selecteur_.ajouterDeclencheur(ordalie)

label ordalie:
    menu:
        "tmp ordalie"
        "ok":
            pass
    "L'ordalie, ou jugement de Dieu, a été interdite par le 4ème concile de Latran en 1215."
    "Il est néanmoins très difficile de l'éradiquer. Les brutales épreuves par le fer, l'eau et le fer rouge s'estompent."
    "Mais le jugement de Dieu par combat est encore très populaire parmi les nombreux guerriers du royaume et malgré les ravages qu'il cause, vous ne parvenez pas à l'éradiquer."
    jump fin_cycle

label ecuDOr:
    "Votre royaume est plus riche que jamais. Vous pouvez enfin accomplir un vieux rêve des rois de France."
    "La monnaie d'or n'était plus frappée depuis Charlemagne. Vous la rétablissez enfin en Occident en créant l'Écu d'or."
    jump fin_cycle
