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
        naissanceBlanche = dec_histo.DecHistoU(proba.Proba(0.6, True), "naissanceBlanche", 1240)
        selecteur_.ajouterDeclencheur(naissanceBlanche)
        naissanceIsabelle = dec_histo.DecHistoU(proba.Proba(0.6, True), "naissanceIsabelle", 1242)
        selecteur_.ajouterDeclencheur(naissanceIsabelle)
        naissanceLouis = dec_histo.DecHistoU(proba.Proba(0.6, True), "naissanceLouis", 1244)
        selecteur_.ajouterDeclencheur(naissanceLouis)
        naissancePhilippe = dec_histo.DecHistoU(proba.Proba(0.6, True), "naissancePhilippe", 1245)
        selecteur_.ajouterDeclencheur(naissancePhilippe)
        naissanceJean = dec_histo.DecHistoU(proba.Proba(0.6, True), "naissanceJean", 1248)
        selecteur_.ajouterDeclencheur(naissanceJean)
        naissanceJeanTristan = dec_histo.DecHistoU(proba.Proba(0.6, True), "naissanceJeanTristan", 1250)
        selecteur_.ajouterDeclencheur(naissanceJeanTristan)
        naissancePierre = dec_histo.DecHistoU(proba.Proba(0.6, True), "naissancePierre", 1251)
        selecteur_.ajouterDeclencheur(naissancePierre)
        naissanceBlanche = dec_histo.DecHistoU(proba.Proba(0.6, True), "naissanceBlanche2", 1253)
        selecteur_.ajouterDeclencheur(naissanceBlanche)
        naissanceMarguerite = dec_histo.DecHistoU(proba.Proba(0.6, True), "naissanceMarguerite", 1254)
        selecteur_.ajouterDeclencheur(naissanceMarguerite)
        naissanceRobert = dec_histo.DecHistoU(proba.Proba(0.6, True), "naissanceRobert", 1257)
        selecteur_.ajouterDeclencheur(naissanceRobert)
        naissanceAgnes = dec_histo.DecHistoU(proba.Proba(0.6, True), "naissanceAgnes", 1260)
        selecteur_.ajouterDeclencheur(naissanceAgnes)
        # majorité des enfants ??
        # majoThierry = dec_histo.DecHistoU(proba.Proba(0.3, True), "majoThierry", 498) # 485 naissance + 13
        # selecteur_.ajouterDeclencheur(majoThierry)
        # marriage des enfants ??

label naissanceBlanche:
    "Votre premier enfant, votre fille Blanche, vient de naître !"
    jump fin_cycle

label naissanceIsabelle:
    "Votre fille Isabelle vient de naître !"
    jump fin_cycle

label naissanceLouis:
    "Votre fils héritier Louis vient de naître !"
    jump fin_cycle

label naissancePhilippe:
    "Votre fils Philippe vient de naître !"
    jump fin_cycle

label naissanceJean:
    "Votre fils Jean vient de naître, malheureusement il est mort peu de temps après."
    jump fin_cycle

label naissanceJeanTristan:
    "Votre fils Jean Tristan vient de naître. Son nom reflète al tristesse de votre condition de captif."
    jump fin_cycle

label naissancePierre:
    "Votre fils Pierre vient de naître."
    jump fin_cycle

label naissanceBlanche2:
    "Votre fille Blanche vient de naître."
    jump fin_cycle

label naissanceMarguerite:
    "Votre fille Marguerite vient de naître."
    jump fin_cycle

label naissanceAgnes:
    "Votre fille Agnès vient de naître."
    jump fin_cycle

label naissanceRobert:
    "Votre fils Robert vient de naître."
    jump fin_cycle
