init python:
    from abs import carac
    from spe.cultures import francs
    from abs.humanite import trait
    from abs.humanite import metier
    from abs.univers import temps
    from abs.humanite.sante import pbsante
    from chapitres.classes import heros
    import random
    
    interfaceMode_ = 0
    nbInterfaceMode_ = 2
    # cultures
    francs_ = francs.Francs()

    # text fade system
    time_ = 2.0 # seconds of fade
    x_debut = 100
    y_debut = 10
    x_fin = 650
    y_fin = 10

    def SetValCaracInt(caracId, num):
        global situation_
        valCourant = situation_.GetValCaracInt(caracId)
        if num > valCourant:
            AjouterACarac(caracId, num - valCourant)
        elif num < valCourant:
            RetirerACarac(caracId,num - valCourant)

    def AjouterACarac(caracId, num):
        global situation_
        textChangtCarac = u"{} + {}".format(caracId, num)
        renpy.show_screen("fading_text", textChangtCarac, time_, x_debut, y_debut, x_fin, y_fin, color="#4f4", size=24, alpha=1.0)
        renpy.pause(time_)
        renpy.hide_screen("fading_text")
        situation_.AjouterACarac(caracId, num)

    def GetValCarac(caracId):
        """
        simple racourci
        """
        global situation_
        return situation_.GetValCarac(caracId)

    def GetValCaracInt(caracId):
        """
        simple racourci
        """
        global situation_
        return situation_.GetValCaracInt(caracId)

    def RetirerACarac(caracId, num):
        global situation_
        textChangtCarac = u"{} - {}".format(caracId, num)
        renpy.show_screen("fading_text", textChangtCarac, time_, x_debut, y_debut, x_fin, y_fin, color="#e11", size=24, alpha=1.0)
        renpy.pause(time_)
        renpy.hide_screen("fading_text")
        situation_.RetirerACarac(caracId, num)

    def InterfaceSuivante():
        global interfaceMode_, nbInterfaceMode_
        interfaceMode_ = interfaceMode_ + 1
        if interfaceMode_ >= nbInterfaceMode_:
            interfaceMode_ = 0
        print(interfaceMode_)

    def AfficherCarteActuelle():
        global situation_
        derniereCarte = situation_.GetValCarac(heros.Heros.CARTE_ACTUELLE)
        renpy.scene()
        renpy.show(derniereCarte)
