init -5 python:
    import random
    from abs.religions import religion
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite import trait
    from abs.humanite import metier
    from spe import dec_clo

    def AjouterEvtsFamille():
        global selecteur_
        # majorité de Thierry
        majoThierry = dec_clo.DecClovisU(proba.Proba(0.3, True), "majoThierry", 498) # 485 naissance + 13
        selecteur_.ajouterDeclencheur(majoThierry)
        # majorité de Clodomir
        majoClodomir = dec_clo.DecClovisU(proba.Proba(0.3, True), "majoClodomir", 508) # 495 naissance + 13
        selecteur_.ajouterDeclencheur(majoClodomir)
        # majorité de Childebert
        majoChildebert = dec_clo.DecClovisU(proba.Proba(0.3, True), "majoChildebert", 510) # 497 naissance + 13
        selecteur_.ajouterDeclencheur(majoChildebert)
        # majorité de Clotaire
        majoClotaire = dec_clo.DecClovisU(proba.Proba(0.3, True), "majoClotaire", 511) # 498 naissance + 13
        selecteur_.ajouterDeclencheur(majoClotaire)

label majoClotaire:
    "Votre fils Clotaire a 13 ans. Ce n'est plus un enfant, vous lui remettez ses armes avec fierté. Bientôt il sera un grand meneur d'hommes."
    jump fin_cycle

label majoChildebert:
    "Votre fils Childebert a 13 ans. Ce n'est plus un enfant, vous lui remettez ses armes avec fierté. Bientôt il sera un grand meneur d'hommes."
    jump fin_cycle

label majoThierry:
    "Votre fils Thierry a 13 ans. Ce n'est plus un enfant, vous lui remettez ses armes avec fierté. Bientôt il sera un grand meneur d'hommes."
    jump fin_cycle

label majoClodomir:
    "Votre fils Clodomir a 13 ans. Ce n'est plus un enfant, vous lui remettez ses armes avec fierté. Bientôt il sera un grand meneur d'hommes."
    jump fin_cycle
