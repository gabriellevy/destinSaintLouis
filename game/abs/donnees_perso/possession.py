class Possession(object):
    """
    Objets du personnage
    """

    def __init__(self, id, image):
        self.id_ = id
        self.image_ = image
        # self.description_ = ""

    def __str__(self):
        """Affichage quand on entre cet objet dans l'interpréteur"""
        return "Objet {}, adresse image :  {}".format(
            self.id_, self.image_)
