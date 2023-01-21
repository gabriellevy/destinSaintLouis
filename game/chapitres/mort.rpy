label mort:
    scene bg priere
    play music roi_mort noloop
    menu:
        "C'est la fin. Vos derniers mots ?"
        "Sire Dieu, donnez-nous que nous puissions mépriser la prospérité de ce monde.":
            pass
    $ saintete = situation_.GetValCaracInt(heros.Heros.C_SAINTETE)
    $ print("Sainteté : {}".format(saintete))
    if saintete >= heros.Heros.C_VAL_SAINTETE_CANONISATION:
        "Félicitations vous avez accompli votre destin ! Vous êtes un Saint, pour le peuple et pour l'église !"
    elif saintete < 100:
        "Vous avez été loin, très loin de faire honneur à Jésus Christ et à la seule vraie religion chrétienne. Puissiez vous échapper à l'enfer."

    menu:
        "Fin de vie."
        "ok":
            pass
    return
