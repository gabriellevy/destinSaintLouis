from abs.donnees_perso import possession

class ObjetSpe(possession.Possession):
    def __init__(self, id, image):
        possession.Possession.__init__(self, id, image)

class EpeeTemplier(ObjetSpe):
    ID = u"Épée de templier"
    def __init__(self):
        ObjetSpe.__init__(self, EpeeTemplier.ID, "images/objets/epee_templier.png")
