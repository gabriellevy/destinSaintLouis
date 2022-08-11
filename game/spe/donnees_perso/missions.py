from abs.donnees_perso import mission

# pas sûr que ça sauvegarde => à tester !!
class Missions(object):
    """
    Liste de toutes les missions. Utiles pour :
     - accéder de partout aux ids
     - trier les caracs de situations pour gérer affichage et données spcifiques
    """

    MISSION1 = 'mission1'

    def __init__(self):
        self.lMissions_ = dict()
        self.CreerMission(Missions.MISSION1, 'description de mission1', 95)

    def __getitem__(self, idMission):
        if not idMission in self.lMissions_:
            self.CreerMission(idMission)
        return self.lMissions_[idMission]

    def __setitem__(self, idMission, missionObj):
        self.SetMission(idMission, missionObj)

    def SetMission(self, idMission, missionObj):
        # si la mission n'existe pas encore, la créer
        if not idMission in self.lMissions_:
            self.CreerMission(idMission, missionObj.m_Description, missionObj.m_TmpsMin)

        self.lMissions_[idMission] = missionObj

    def CreerMission(self, idMission, description, tpsMin):
        missionObj = mission.Mission(idMission, description, tpsMin)
        self.lMissions_[idMission] = missionObj

    def __len__(self):
        return len(self.lMissions_)

    def __str__(self):
        """Affichage quand on affiche l'objet (print)"""
        if len(self.lMissions_) == 0:
            return "Aucune mission."
        str = u"Liste de toutes les missions : "
        for missionObj in self.lMissions_:
            str = str + missionObj + ","
        return str
