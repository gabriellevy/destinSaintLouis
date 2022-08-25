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
        # Inquisition
        creationInquisition = dec_histo.DecHistoU(proba.Proba(0.3, True), "creationInquisition", 1233)
        selecteur_.ajouterDeclencheur(creationInquisition)
        # fin de l'ordalie
        ordalie = dec_histo.DecHistoU(proba.Proba(0.1, True), "ordalie", 0)
        ordalie.AjouterCondition(estRoi)
        selecteur_.ajouterDeclencheur(ordalie)
        # Saint Dominique
        cannonisationSaintDominique = dec_histo.DecHistoU(proba.Proba(0.3, True), "cannonisationSaintDominique", 1234, 1234)
        selecteur_.ajouterDeclencheur(cannonisationSaintDominique)
        # Saint François
        cannonisationSaintFrancois = dec_histo.DecHistoU(proba.Proba(0.3, True), "cannonisationSaintFrancois", 1228, 1228)
        selecteur_.ajouterDeclencheur(cannonisationSaintFrancois)

label cannonisationSaintFrancois:
    "Feu Saint François d'Assise est un chrétien illustre, fondateur de l'ordre des moines mendiants 'les Mineurs'."
    "Il vient d'être cannonisé par l'église. Bientôt son ordre sera rebaptisé les Franciscains, en son honneur."
    jump fin_cycle

label cannonisationSaintDominique:
    "Le célèbre moine espagnol Dominique de Calaruega, mort en 1221 quand vous étiez enfant, vient d'être cannonisé."
    "Il a fondé l'ordre des moines mendiant 'les frères pêcheurs'. Bientôt ceux ci seront rebaptisés de son nom : les Dominicains."
    jump fin_cycle

label creationInquisition:
    scene bg inquisition
    "Le pape Grégoire IX a institué l'inquisition, une organisation d'enquêteurs religieux spécialisé dans le combat contre l'hérésie."
    "Il attend la coopération de tous les bons catholiques pour extirper une bonne foi pour toutes les graines de l'hérésie, en particulier les restes des cathares."
    jump fin_cycle

label ordalie:
    "L'ordalie, ou jugement de Dieu, a été interdite par le 4ème concile de Latran en 1215."
    "Il est néanmoins très difficile de l'éradiquer. Les brutales épreuves par le fer, l'eau et le fer rouge s'estompent."
    "Mais le jugement de Dieu par combat est encore très populaire parmi les nombreux guerriers du royaume et malgré les ravages qu'il cause, vous ne parvenez pas à l'éradiquer."
    jump fin_cycle

label ecuDOr:
    "Votre royaume est plus riche que jamais. Vous pouvez enfin accomplir un vieux rêve des rois de France."
    "La monnaie d'or n'était plus frappée depuis Charlemagne. Vous la rétablissez enfin en Occident en créant l'Écu d'or."
    jump fin_cycle
