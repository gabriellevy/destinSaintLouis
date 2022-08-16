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
        # événements précis
        mongols_riazan = dec_histo.DecHisto(proba.Proba(0.4, True), "mongols_riazan", 1237)
        selecteur_.ajouterDeclencheur(mongols_riazan)
        mongols_rus = dec_histo.DecHisto(proba.Proba(0.4, True), "mongols_rus", 1239)
        selecteur_.ajouterDeclencheur(mongols_rus)
        # mongols, événements génériques post menace principale
        mongols = dec_histo.DecHisto(proba.Proba(0.2, True), "mongols", 1241)
        selecteur_.ajouterDeclencheur(mongols)

        delegation_mongols_diplo_cond = condition.Condition("delegation_mongols_diplo", 1, condition.Condition.EGAL)
        delegation_mongols_diplo = dec_histo.DecHistoU(proba.Proba(0.2, True), "delegation_mongols_diplo", 1241)
        delegation_mongols_diplo.AjouterCondition(delegation_mongols_diplo_cond)
        selecteur_.ajouterDeclencheur(delegation_mongols_diplo)

        delegation_mongols_relig_cond = condition.Condition("delegation_mongols_relig", 1, condition.Condition.EGAL)
        delegation_mongols_relig = dec_histo.DecHistoU(proba.Proba(0.2, True), "delegation_mongols_relig", 1241)
        delegation_mongols_relig.AjouterCondition(delegation_mongols_relig_cond)
        selecteur_.ajouterDeclencheur(delegation_mongols_relig)

label delegation_mongols_relig:
    scene bg chef_mongol
    "Vos envoyés diplomatiques sont revenus de la cours mongole."
    "Ils ont été accueillis noblement et bien traités. Ils ont pu participer à de nombreuses discussions religieuses en présence de prêtre musulmans, tengri, bouddhistes et juifs."
    "Ils n'ont néanmoins pas de nouvelles probantes à donner. Les khans mongols ont refusé de se convertir ou de prendre des engagements."
    "Certains de nos prêtres sont restés auprès des mongols pour continuer l'évangélisation. Espérons qu'ils obtiendront des résultats."
    jump fin_cycle

label delegation_mongols_diplo:
    scene bg chef_mongol
    "Vos envoyés diplomatiques sont revenus de la cours mongole."
    "Ils ont été accueillis noblement et bien traités mais leurs nouvelles sont mauvaises."
    "Les mongols ne conçoivent pas d'alliance, ils considèrent tous les rois d'Europe comme des êtres indignes d'être plus que leurs vassals et demandent la soumission de votre altesse."
    "A FAIRE : donner une possibilité de se soumettre ??"
    jump fin_cycle

label mongols_riazan:
    scene bg armee_mongole
    "Les mongols du terrible général Batu Khan ont rasé la ville russe de Riazan. On dit que le massacre fut tel qu'il n’y avait plus personne pour gémir et pleurer."
    jump fin_cycle

label mongols_rus:
    scene bg armee_mongole
    "Que Dieu nous protège ! Les mongols ont anéanti la principauté du Rus de Kiev. Ils ont pris les grandes villes de Kolomna, Moscou, et la capitale Wladimir !"
    "La famille royale a été exterminée, les villes rasées jusqu'aux fondations et les rares survivants réduits en esclavage."
    "Ils semblent invincibles, inarrêtables et ont juré d'atteindre la mer ultime, là où ils ne pourront aller plus loin et n'auront plus rien à conquérir."
    jump fin_cycle

label mongols:
    scene bg armee_mongole
    $ niveauMongols = situation_.GetValCaracInt("niveauMongols")
    if niveauMongols == 0:
        $ situation_.SetValCarac("niveauMongols", 1)
        "Les polonais ont repoussé vaillament l'invasion mongole."
        "On dit que les mongols s'apaisent et pourraient renoncer à l'invasion de l'Europe. On dit même que certains de leurs princes ont épousé des princesses chrétiennes nestoriennes."
        "Serait-ce finalement la fin d'une menace que nous croyions de taille à anéantir la chrétienté ?"
    if niveauMongols == 1:
        $ situation_.SetValCarac("niveauMongols", 2)
        "Beaucoup de vos conseillers continuent à être terrifiés par les mongols mais d'autres pensent qu'ils pourraient être une aide contre les sarrasins en les prenant à revers."
        "De plus ils sont païens et semblent ouverts au christianisme. Peut-être serait-ils réceptifs à la conversion ?"
        menu:
            "Souhaitez vous leur envoyer une délégation?"
            "Oui. Essentiellement diplomatique, pour tenter une alliance contre les turcs et autres sarasins.":
                $ RetirerACarac(trait.Richesse.NOM, 1)
                $ situation_.SetValCarac("delegation_mongols_diplo", 1)
            "Oui. Essentiellement religieuse. Pour tenter les convertir à la foi chrétienne.":
                $ RetirerACarac(trait.Richesse.NOM, 1)
                $ AjouterACarac(heros.Heros.C_SAINTETE, 1)
                $ situation_.SetValCarac("delegation_mongols_relig", 1)
            "Non":
                jump fin_cycle


    else:
        "Même si les mongols continuent à terrifier le peuple, ils ne semblent plus menaçants envers la chrétienté."
    jump fin_cycle
