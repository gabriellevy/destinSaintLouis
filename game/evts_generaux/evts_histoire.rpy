init -5 python:
    import random
    from abs.religions import religion
    from spe import dec_clo
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite import trait
    from abs.humanite import metier

    def AjouterEvtsHistoire():
        global selecteur_
        # Odoacre
        histoireTheodoricOdoacre = dec_clo.DecClovisU(proba.Proba(0.03, True), "histoireTheodoricOdoacre", 493)
        selecteur_.ajouterDeclencheur(histoireTheodoricOdoacre)
        # Concile d'Orléans
        concileOrleans = dec_clo.DecClovisU(proba.Proba(0.03, True), "concileOrleans", 511)
        selecteur_.ajouterDeclencheur(concileOrleans)

label concileOrleans:
    "Vous organisez le premier concile qui ait eu lieu en Gaule. Il aura lieu à Orléans."
    jump fin_cycle

label histoireTheodoricOdoacre:
    # victoire et prières des païens et des chrétiens
    $ situation_.SetValCarac("histoireTheodoricOdoacre", 1)
    "Importantes nouvelles d'Italie !"
    "Théodoric le redoutable roi des Ostrogoths avait été envoyé en Italie il y a plusieurs années par l'empereur romain d'Orient Zénon."
    "Sa mission était de vaincre le roi des Hérules Odoacre qui avait conquis Rome et soumis l'empire romain d'Occident."
    "Cette mission est maintenant terminée : Théodoric a repris Rome puis Ravenne."
    "Il a invité le vaincu Odoacre à un banquet où il l'a égorgé de sa propre épée avant de faire massacrer toute sa famille."
    "Théodoric est maintenant roi de l'Italie et de la Dalmatie et un rival de poids qu'il faudra ménager car sa puissance est de loin supérieure à la vôtre."
    jump fin_cycle
