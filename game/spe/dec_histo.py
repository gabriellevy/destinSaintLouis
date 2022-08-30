from abs import declencheur
from abs.univers import temps
from abs import proba
from abs import modifProba
from abs import condition

class DecHisto(declencheur.Declencheur):

    def __init__(self, aproba, labelGoTo, dateMin, dateMax = -1):
        """
        cette version du délencheur inclut 1 paramètre utile en mode "historique" :
         - une date minimum de déclenchement
        """
        declencheur.Declencheur.__init__(self, aproba, labelGoTo)
        self.selecteur_ = None # référence vers le sélecteur qui contient ce déclencheur

        conditionDateMin = condition.Condition(temps.Date.DATE_ANNEES, dateMin, condition.Condition.SUPERIEUR_EGAL)
        self.AjouterCondition(conditionDateMin)
        if dateMax != -1:
            conditionDateMax = condition.Condition(temps.Date.DATE_ANNEES, dateMax, condition.Condition.INFERIEUR_EGAL)
            self.AjouterCondition(conditionDateMax)

class DecHistoDatePrecise(declencheur.Declencheur):

    def __init__(self, aproba, labelGoTo, dateMin, dateMax = -1):
        """
        cette version du délencheur inclut 1 paramètre utile en mode "historique" : une date (en nb de jours)
         Arrive le jour donné ou après => à associer en général à ds probas très fortes pour que l'événement arrive quasiment le jour donné
        """
        declencheur.Declencheur.__init__(self, aproba, labelGoTo)
        self.selecteur_ = None # référence vers le sélecteur qui contient ce déclencheur

        conditionDateMin = condition.Condition(temps.Date.DATE, dateMin.nbJours_, condition.Condition.SUPERIEUR_EGAL)
        self.AjouterCondition(conditionDateMin)
        if dateMax != -1:
            conditionDateMax = condition.Condition(temps.Date.DATE, dateMax.nbJours_, condition.Condition.INFERIEUR_EGAL)
            self.AjouterCondition(conditionDateMax)

class DecHistoDatePreciseU(DecHistoDatePrecise):
    """
    U signifie 'Unique' => l'événement auquel on applique ce déclencheur ne peut s'exécuter qu'une fois maximum
    """

    def __init__(self, aproba, labelGoTo, dateMin, dateMax = -1):
        DecHistoDatePrecise.__init__(self, aproba, labelGoTo, dateMin, dateMax)

    def executer(self, situation):
        # cette exécution ne doit plus jamais arriver : on lui met une proba à 0 :
        # self.proba_ = proba.Proba(0)
        if self.selecteur_ is not None:
            self.selecteur_.declencheurs_.remove(self) # A FAIRE : ceci ne passera pas a la sauvegarde => a améliorer
        return self.labelGoTo_


class DecHistoU(DecHisto):
    """
    U signifie 'Unique' => l'événement auquel on applique ce déclencheur ne peut s'exécuter qu'une fois maximum
    """

    def __init__(self, aproba, labelGoTo, dateMin, dateMax = -1):
        """
        identique à la version historique mais ne se déclenche qu'une fois maximum quoiqu'il arrive
        """
        DecHisto.__init__(self, aproba, labelGoTo, dateMin, dateMax)

    def executer(self, situation):
        # cette exécution ne doit plus jamais arriver : on lui met une proba à 0 :
        # self.proba_ = proba.Proba(0)
        if self.selecteur_ is not None:
            self.selecteur_.declencheurs_.remove(self) # A FAIRE : ceci ne passera pas a la sauvegarde => a améliorer
        return self.labelGoTo_
