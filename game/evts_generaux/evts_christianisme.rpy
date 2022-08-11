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

    def AjouterEvtsChristianisme():
        global selecteur_
        # rencontre de Vaast
        vaast = dec_clo.DecClovisU(proba.Proba(0.3, True), "vaast", 495)
        vaast.AjouterCondition(estPaien)
        vaast.AjouterCondition(alamansVaincus)
        selecteur_.ajouterDeclencheur(vaast)
        # rencontre de Saint Rémi
        remi = dec_clo.DecClovisU(proba.Proba(0.3, True), "remi", 496)
        remi.AjouterCondition(estPaien)
        selecteur_.ajouterDeclencheur(remi)

label remi:
    "Le plus cher voeu de Clothilde est votre conversion au catholicisme. Mais ses arguments ne vous ont jamais vraiment convaincu."
    "Elle a donc fait venir l'évèque Rémi de Reims. En secret car elle craint les réactions de vos guerriers francs païens."
    "Ce Rémi est un brave homme avec qui vous avez souvent correspondu. Il est de bon conseil et vous aide grandement à stabiliser sa région."
    menu:
        "Il est néanmoins dangereux de laisser se répandre le bruit que les gaulois tentent de vous convertir."
        "Accepter de lui parler en secret":
            "Rémi vous parle avec patience et douceur des heures durant. Imperciptiblement il vous énonce le Credo puis vous commencer le catéchuménat."
            $ AjouterACarac(heros.Heros.C_CHRISTIANISME, 4)
        "Le prendre comme conseiller":
            "Cette nomination fait beaucoup jaser. Beaucoup de francs, surtout nobles, affirment que vous êtes secrètement devenu chrétien et vivez sous la coupe de votre femme."
            $ AjouterACarac(heros.Heros.C_USURPATION, 2)
            "Rémi fait néanmoins un excellent conseiller. La gestion s'améliore et la fidélité de la Gaulle aussi."
            $ AjouterACarac(trait.Richesse.NOM, 1)
            $ AjouterACarac(heros.Heros.C_FIDELITE_PEUPLE, 2)
        "Le renvoyer dans son diocèse":
            "Rémi est dévôt mais raisonnable, il n'insiste pas malgré sa déception et part sur le champs."
            $ RetirerACarac(heros.Heros.C_CHRISTIANISME, 1)
    jump fin_cycle

label vaast:
    "Alors que vous chevauchez sur vos terres vous passez près d'une petite cabane en bordure de la forêt."
    "Un de vos leudes vous informe qu'il s'agit de la demeure de l'ermite Vaast."
    "C'est un sage franc converti au catholicisme qui vit retiré et prêche de temps à autre, surtout auprès de ses congénères francs qui le respectent beaucoup."
    $ niveauChrist = situation_.GetValCaracInt(heros.Heros.C_CHRISTIANISME)
    menu:
        "Voilà l'homme idéal pour discuter des troubles religieux. Les vôtres et ceux de vos sujets. De plus contrairement aux religieux gaulois il parle avec maîtrise votre langue germanique, le francique."
        "Vous parlez un peu de religion avec lui":
            "Vaast est un fervent croyant et en tant que franc il sait comment vous faire douter et vous convaincre. Vous sortez de la discussion ébranlé."
            $ AjouterACarac(heros.Heros.C_CHRISTIANISME, 1)
        "Vous lui parlez de votre intérêt pour le christianisme mais de votre doute sur la conversion" if niveauChrist > 7:
            "Vaast comprend vos doutes. Il est dur de rester roi des francs car il suffit d'un revers pour qu'ils vous renversent et remplacent par un autre."
            "C'est arrivé à votre propre père Childéric en son temps, même si il fut finalement restauré."
            "Renoncer à la religion de vos ancêtres vous ferait perdre votre titre de roi prêtre descendant des dieux."
            "Mais il affirme que les francs sont prêts à sauter le pas et qu'il fera tout son possible pour vous aider à les convaincre si vous vous faisiez baptiser."
            $ AjouterACarac(heros.Heros.C_CHRISTIANISME, 2)
            $ RetirerACarac(heros.Heros.C_USURPATION, 1)
        "Vous lui interdisez de convertir les francs":
            "Garder le contrôle de vos hommes est déjà assez dur sans qu'on les fasse douter de la religion dont vous êtes le prêtre de sang divin."
            "Vaast se soumet à votre volonté et devient ermite pour de bon."
            $ RetirerACarac(heros.Heros.C_CHRISTIANISME, 2)
            $ RetirerACarac(heros.Heros.C_USURPATION, 1)
        "Vous l'ignorez":
            pass

    jump fin_cycle
