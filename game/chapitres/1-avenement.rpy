
init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite import trait
    from abs.humanite import pnj
    from abs.humanite import metier
    from abs.univers import temps
    # from geographie import quartier
    from abs.humanite import identite
    from spe import dec_histo

    estPasRoi = condition.Condition(metier.Metier.C_METIER, metier.Roi.NOM, condition.Condition.DIFFERENT)
    estRoi = condition.Condition(metier.Metier.C_METIER, metier.Roi.NOM, condition.Condition.EGAL)

    def AjouterEvtAvenement():
        global selecteur_
        avenement = dec_histo.DecHistoU(proba.Proba(0.6, False), "avenement", 481)
        avenement.AjouterCondition(estPasRoi)
        selecteur_.ajouterDeclencheur(avenement)

label avenement:
    scene bg priere
    with dissolve
    play music roi_mort noloop
    # A FAIRE : trouver un fond pour le couronnement
    show screen valeurs_traits
    $ childeric = situation_.GetValCarac(pnj.Pnj.C_PERE)
    $ childeric.Tuer()
    # enterrement de Childéric
    "Votre glorieux père Childéric vient de mourir."
    "Son enterrement est celui du grand roi guerrier invaincu qu'il est. Il porte son manteau pourpre de général romain tenu par une fibule d'or, au doigt son anneau qui lui servait à sceller les actes et porte l'inscription : Childéricus rex."
    "Ses armes sont enterrées à ses côtés. Puis dix grands chevaux de guerre sont sacrifiés et enterrés près de lui pour qu'il puisse chevaucher et combattre éternellement aux côtés de Wotan au Valhalla."

    # avènement
    "Vous avez à peine 15 ans mais êtes déjà un adulte digne d'être roi. Vous portez fièrement vos cheveux longs, symbole de votre origine divine."
    "Vous recevez la lance sacrée de votre père, symbole de votre autorité et de votre force. Vous devenez ainsi une vivante figure de Wotan, père et roi des Dieux."
    "Puis vos guerriers vous hissent sur le grand pavois du chef."
    # royaume de Clovis à son avènement
    $ AfficherCarteActuelle()
    with dissolve
    "Votre prestige est grand car votre père a été un grand roi invaincu à la guerre et fidèle à l'empire romain. Mais vous n'êtes que le roi des francs saliens de Tournai."
    "Et même si vos guerriers sont redoutables ils ne sont que quelques milliers ce qui est bien peu."
    "Cependant l'empire romain est en ruines, plein de peuples riches qui ne savent pas se battre. C'est la situation idéale pour qui saura saisir les opportunités."
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Roi.NOM)
    jump fin_cycle
