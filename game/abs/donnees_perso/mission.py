# pas sûr que ça sauvegarde => à tester !!
class Mission(object):
    """
    Classe très basique qui sert de cadre pour les missions, en particulier à temps limité
    """

    def __init__(self, id, description, tmpsMin):
        self.m_Id = id
        self.m_Description = description
        self.m_TmpsMin = tmpsMin

    def __str__(self):
        """Affichage quand on entre cet objet dans l'interpréteur"""
        return "Mission {} ({} minutes): {}".format(
            self.m_Id, self.m_TmpsMin, self.m_Description)

    def AvanceDeXMinutes(self, nbMinutesPassees):
        self.m_TmpsMin = self.m_TmpsMin - nbMinutesPassees
