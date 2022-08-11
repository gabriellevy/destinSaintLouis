init -20 python:
    from abs.religions import religion
    from abs.humanite.sante import pbsante
    from abs.univers import temps
    # from univers.geographie import quartier
    from abs.humanite import portrait
    from abs.humanite import pnj
    from abs.humanite import trait
    from abs.humanite import identite
    from abs.affichage import affichagePortrait
    from abs.humanite.amour import relationAmoureuse
    from abs.humanite import metier
    import random
    import logging

    class Situation(object):
        """
        Base class for defaulting stats and integrating with the store.

        Designed to be extended by just overloading the constants


        Example of extended class

        class EnemyStats(Situation):

            # Set the store.{prefix}.character_id value
            STORE_PREFIX = "enemy_stats"

            # Boolean toggle for validation - defaults both True
            VALIDATE_VALUES = True
            COERCE_VALUES = False

            STAT_DEFAULTS = {
                'element' : 'earth',
                'hp' : 50,
                'mp' : 40,
                'rarity' : 0.075,
            }

            ----

        Situation de jeu
        Etat d'une partie à un instant t avec toutes les informations nécessaires pour la sauvegarder et la recharger
        en particulier la liste intégrale des caractéristiques du perso (qui sont une sous catégorie de la situation de jeu)
        """

        STORE_PREFIX = "stats"
        VALIDATE_VALUES = False
        COERCE_VALUES = False # False pour l'instant => bloque l'affectation à des types différents de ceux de l'origine, à exploiter un jour

        STAT_DEFAULTS = {
            temps.Date.DATE: 0 # nb de jours au démarrage du jeu depuis an (ou jour ou autre) 0
        }

        def __init__(self, id, **kwargs):
            """
            Initialize values from store or kwargs or default

            @param id: A unique id to use in the store. Generally set to
            the Character reference to allow cross object lookups

            @param **kwargs: Setup values that are not default
            """

            if not isinstance(id, basestring):
                id = str(id) # should raise if not stringable

            self.__dict__['_id'] = id

            self.run_optional_method( '__pre_init__', id, **kwargs )

            store_name = "{prefix}.{suffix}".format(
                prefix = type(self).STORE_PREFIX,
                suffix = self.__dict__['_id'] )

            setattr(store, store_name, {})

            self.__dict__['_store'] = getattr(store, store_name)

            # We use:
                # Store value
                # else kwargs value
                # else default value

            for key, value in kwargs.items():

                if key not in self.__dict__['_store']:

                    setattr(self, key, value)

            for key, value in type(self).STAT_DEFAULTS.items():

                if key not in self.__dict__['_store']:

                    setattr(self, key, value)

        # def __init__(self, nbJoursDate):
        #     self.caracs_ = dict() # dictionnaire contenant toutes les caracs courantes de la partie
        #     self.valsMin_ = dict() # facultatif : dictionnaire contenant l'éventuelle valeur min de la carac en clé
        #     self.valsMax_ = dict() # facultatif : dictionnaire contenant l'éventuelle valeur max de la carac en clé
        #     date = temps.Date(nbJoursDate)
        #     self.caracs_[temps.Date.DATE] = date.nbJours_
        #     self.caracs_[temps.Date.AGE_ANNEES] = 0
            # self.collectionTraits = None
            # self.collectionMetiers = None
            # self.collectionBlessures = None
            # self.collectionMaladies = None
            # self.collectionQuartiers = None
            # self.collectionPnjs = {}
            self.inventaire_ = []

            self.run_optional_method( '__post_init__', id, **kwargs )


        def run_optional_method(self,
                                method_type='post_init',
                                *args,
                                **kwargs):
            """
            Run a method of the object if it exists
            """
            try:
                getattr( self, self.__dict__[ method_type ] )( *args,
                                                               **kwargs )
            except:
                pass


        def get_validated_value(self, key, value):
            """
            Return a value after validating where applicable
            """

            if not type(self).VALIDATE_VALUES:
                return value

            if not key in self.__dict__:
                return value

            default_type = type( self.__dict__[key] )

            if isinstance(value, default_type):
                return value

            if type(self).COERCE_VALUES:
                try:
                    return default_type(value)
                except:
                    pass

            raise TypeError, "Supplied value '{0}' for key '{1}' does not " \
                             "match the existing '{2}'".format(
                                value,
                                key,
                                default_type)


        def __setattr__(self, key, value):

            value = self.get_validated_value(key, value)

            self.__dict__[key] = value

            # Anything not recognized as an attribute of object
            # is placed into the store

            if key not in dir(object):

                self.__dict__['_store'][key] = value


        def __getattr__(self, key):

            try:

                return self.__dict__['_store'][key]

            except:

                if key in self.__dict__:

                    return self.__dict__[key]

                else:

                    try:

                        # try the character object
                        value = getattr(
                                    getattr( character, self._id ),
                                             key )

                        if key != 'name':

                            return value

                        # substitute the name (for interpolation/translations)
                        return renpy.substitutions.substitute(value)[0]

                    except:

                        pass

            # return "" # A FAIRE : fait déonner la sauvegarde : POURQUOI ?
            return super(Situation, self).__getattr__(key)


        def __getattribute__(self, key):

            # Check if the attribute is an @property first

            v = object.__getattribute__(self, key)

            if hasattr(v, '__get__'):

                return v.__get__(None, self)

            # Try the store if the attribute is not in base object

            if key not in dir(object):

                try:

                    return self.__dict__['_store'][key]

                except:

                    pass

            return super(Situation, self).__getattribute__(key)


        def __setstate__(self, data):
            self.__dict__.update(data)


        def __getstate__(self):
            return self.__dict__


        def __delattr__(self, key):
            del self.__dict__[key]

        def __getitem__(self, key): # cet override n'est pas forcément une bonne idée mais c'est pratique
            if not hasattr(self, key):
                setattr(self, key, "")
            return getattr(self, key)

        def __setitem__(self, key, val): # cet override n'est pas forcément une bonne idée mais c'est pratique
            setattr(self, key, val)

        def GetValCarac(self, idCarac):
            if not hasattr(self, idCarac):
                if idCarac == relationAmoureuse.RelA.C_AMOUREUSES:
                    setattr(self, idCarac, [])
                else:
                    setattr(self, idCarac, "")
            return getattr(self, idCarac)

        def GetValCaracInt(self, idCarac):
            if not hasattr(self, idCarac):
                setattr(self, idCarac, 0)
            elif getattr(self, idCarac) == "":
                setattr(self, idCarac, 0)
            return int(getattr(self, idCarac))

        def GetValCaracBool(self, idCarac):
            if not hasattr(self, idCarac):
                return False
            elif getattr(self, idCarac) == 1:
                return True
            return False

        def GetQuartier(self):
            valQuartierStr = self.GetValCarac(quartier.Quartier.C_QUARTIER)
            if valQuartierStr == "":
                return None
            return self.collectionQuartiers[valQuartierStr]

        def CreerCarac(self, idCarac, valCarac, valeurMin = "", valeurMax = ""):
            self.AjouterCarac(idCarac, valCarac)
            if valeurMin != "":
                self.valsMin_[idCarac] = valeurMin
            if valeurMax != "":
                self.valsMax_[idCarac] = valeurMax

        def SetCarac(self, idCarac, valCarac, valeurMin = "", valeurMax = ""):
            # si la carac n'existe pas encore, la créer
            if not hasattr(self, idCarac) or getattr(self, idCarac) == "":
                 self.CreerCarac(idCarac, valCarac, valeurMin, valeurMax)

            setattr(self, idCarac, valCarac)
            if valeurMin != "":
                self.valsMin_[idCarac] = valeurMin
            if valeurMax != "":
                self.valsMax_[idCarac] = valeurMax

        # def SetValCaracSiInferieur(self, idCarac, valCarac, valeurMin = "", valeurMax = ""):
            # """
            # ne modifie la valeur de carac que si elle était précédemment inférieur à la valeur qu'on veut lui donner
            # """
            # if not idCarac in self.caracs_ or self.caracs_[idCarac] == "":
            #     self.SetValCarac(idCarac, valCarac, valeurMin, valeurMax)
            # else:
            #     valCourante = self.GetValCaracInt(idCarac)
            #     if valCourante > valCarac:
            #         return

        # self.SetCarac(idCarac, valCarac, valeurMin, valeurMax)

        # def SetValCaracSiSuperieur(self, idCarac, valCarac, valeurMin = "", valeurMax = ""):
            # """
            # ne modifie la valeur de carac que si elle était précédemment inférieur à la valeur qu'on veut lui donner
            # """
            # if not idCarac in self.caracs_ or self.caracs_[idCarac] == "":
            #     self.SetValCarac(idCarac, valCarac, valeurMin, valeurMax)
            # else:
            #     valCourante = self.GetValCaracInt(idCarac)
            #     if valCourante < valCarac:
            #         return

            # self.SetCarac(idCarac, valCarac, valeurMin, valeurMax)

        def SetValCarac(self, idCarac, valCarac, valeurMin = "", valeurMax = ""):
            self.SetCarac(idCarac, valCarac, valeurMin, valeurMax)

        def GetMetier(self):
            valMetierStr = getattr(self, metier.Metier.C_METIER)
            if valMetierStr == "":
                return None
            return self.collectionMetiers[valMetierStr]

        def AjouterACarac(self, idCarac, valCarac):
            # si la carac n'existe pas encore, la créer
            if not hasattr(self, idCarac) or getattr(self, idCarac) == "":
                self.CreerCarac(idCarac, 0)

            valActuelleF = float(getattr(self, idCarac))
            finalVal = valActuelleF + float(valCarac)
            # if idCarac in self.valsMax_ and finalVal > self.valsMax_[idCarac]: # A FAIRE : refaire marcher les valsMax_ et valsMin_
            #     finalVal = self.valsMax_[idCarac]
            self.SetCarac(idCarac, finalVal)

        def RetirerACarac(self, idCarac, valCarac):
            # si la carac n'existe pas encore, la créer
            if not hasattr(self, idCarac) or getattr(self, idCarac) == "":
                self.CreerCarac(idCarac, 0)

            valActuelleF = float(getattr(self, idCarac))
            finalVal = valActuelleF - valCarac
            # if idCarac in self.valsMin_ and finalVal < self.valsMin_[idCarac]: # A FAIRE : refaire marcher les valsMax_ et valsMin_
            #     finalVal = self.valsMin_[idCarac]
            self.SetCarac(idCarac, finalVal)

        def GetTraits(self):
            """
            renvoi la liste des traits du perso sous forme de 'Trait'
            """
            traitsPerso = []
            for traitK in self.collectionTraits.lTraits_.keys():
                valTrait = self.GetValCarac(traitK)
                if valTrait != "" and valTrait != 0:
                    traitsPerso.append(self.collectionTraits[traitK])
            return traitsPerso

        def GetDicoTraits(self):
            """
            renvoi la liste des traits du perso sous forme d'un dico avec comme clé l'id du trait et comme valeur son contenu
            les traits à "" ou 0 ne sont pas renvoyés
            """
            traitsPerso = {}
            for traitK in self.collectionTraits.lTraits_.keys():
                valTrait = self.GetValCarac(traitK)
                if valTrait != "" and valTrait != 0:
                    trait = self.collectionTraits[traitK]
                    traitsPerso[trait.eTrait_] = valTrait
            return traitsPerso

# ---------------------------------- affichage des caracs dans l'interface
        def DescriptionTraits(self, traits):
            """
            Description des traits
            """
            str = u""
            for traitK in traits.lTraits_.keys():
                # la richesse (et de préférence les autres traits qui ne font pas partie de la personnalité du personnage) devraient être affichés différemment
                if traitK != trait.Richesse.NOM:
                    traitObj = traits[traitK]
                    descr = u"{}".format(traitObj.GetDescription(self))
                    if descr != "":
                        if str != "":
                            str = u"{}\n".format(str)
                        # str = u"{}{} ({})".format(str, descr, traitObj.eTrait_) # activer pour plus de détails sur els traits
                        str = u"{}{}".format(str, descr)
            return str

        def AffichageMetier(self):
            global metiers_

            strMetier = u""
            if not hasattr(self, metier.Metier.C_METIER):
                strMetier = u"Sans emploi"
                setattr(self, metier.Metier.C_METIER, u"")
            strMetier = getattr(self, metier.Metier.C_METIER)
            if strMetier == u"":
                strMetier = u"Sans emploi"

            # afficher les compétences (en métier) :
            strComp = u""
            for metierK in metiers_.lMetiers_.keys():
                valMetier = self.GetValCaracInt(metierK)
                if valMetier != "" and valMetier != 0:
                    txtDiscipline = metiers_.lMetiers_[metierK].GetDiscipline()
                    if txtDiscipline == "":
                        txtDiscipline = metierK

                    txtCompetence = metiers_.lMetiers_[metierK].GetTexteCompetence(valMetier)
                    strComp = u"{}\n - {} ({})".format(strComp, txtDiscipline, txtCompetence)

            if strComp != "":
                strMetier = u"{}\n\nCompétences : {}".format(strMetier, strComp)

            return strMetier

        def DescriptionBlessuresEtMaladies(self, blessures, maladies):
            """
            Description des blessures et maladies actuelles actuelles du personnage
            """
            str = u""
            # affichage des blessures
            for blessureK in blessures.lBlessures_.keys():
                blessure = blessures[blessureK]
                if self.GetValCarac(blessureK) != u"":
                    str = u"{}\n{}".format(str, blessure.nom_)

            # affichage des maladies
            for maladieK in maladies.lMaladies_.keys():
                maladie = maladies[maladieK]
                if self.GetValCarac(maladieK) != u"":
                    str = u"{}\n{}".format(str, maladie.nom_)

            # affichage des jours de convalescence
            nbJoursConvalescence = self.GetValCaracInt(pbsante.PbSante.C_JOURS_DHOPITAL)
            if nbJoursConvalescence > 0:
                str = u"{}\nJours de convalescence : {}".format(str, nbJoursConvalescence)

            # if str == "":
            #    str = "Sain"
            return str

        def DescriptionBioniques(self, bioniques):
            """
            Description des bioniques du personnage
            """
            str = u""
            # affichage des bioniques
            for bioniqueK in bioniques.lBioniques_.keys():
                bioniqueObj = bioniques[bioniqueK]
                if self.GetValCarac(bioniqueK) != u"":
                    str = u"{}\n{}".format(str, bioniqueObj.nom_)

            return str

        def AffichagePortraitPere(self):
            # père
            str = u""
            pere = self.GetValCarac(pnj.Pnj.C_PERE)
            if isinstance(pere, pnj.Pnj) :
                return pere.portraitStr_
            return ""

        def AffichagePortraitMere(self):
            # mère
            str = u""
            mere = self.GetValCarac(pnj.Pnj.C_MERE)
            if isinstance(mere, pnj.Pnj) :
                return mere.portraitStr_
            return ""

        def AffichageAmoureuses(self):
            """
            génère un tableau qui contient les éléments affichables du pnj
            """
            amoureuses = self.GetValCarac(relationAmoureuse.RelA.C_AMOUREUSES)
            affichageAmoureuses = []
            if isinstance(amoureuses, list) :
                if len(amoureuses) > 0:
                    if isinstance(amoureuses[0], pnj.Pnj) :
                        for amoureuse in amoureuses:
                            affichage = affichagePortrait.AffichagePortrait(amoureuse)
                            affichageAmoureuses.append(affichage)
            return affichageAmoureuses

        def AffichagePere(self):
            # père
            str = u""
            pere = self.GetValCarac(pnj.Pnj.C_PERE)
            if isinstance(pere, pnj.Pnj) :
                str = u"{}".format(pere)
            return str

        def AffichageMere(self):
            # mère
            str = u""
            mere = self.GetValCarac(pnj.Pnj.C_MERE)
            if isinstance(mere, pnj.Pnj) :
                str = u"{}".format(mere)
            return str

        def AffichageRichesse(self):
            if not hasattr(self, trait.Richesse.NOM):
                return u"Riche"
            strRichesse = self.collectionTraits[trait.Richesse.NOM].GetDescription(self)
            if strRichesse == "":
                strRichesse = u"Riche"
            return strRichesse

        def AffichagePossessions(self):
            strPossession = u""

            if strPossession == "":
                strPossession = u"Aucune possession"
            return strPossession

        def AffichageQuartier(self):
            if hasattr(self, quartier.Quartier.C_QUARTIER):
                return u"Pas d'habitation !!"
            return getattr(self, quartier.Quartier.C_QUARTIER)

        def AffichageReligion(self):
            if not hasattr(self, religion.Religion.C_RELIGION):
                return "Sans religion"
            return getattr(self, religion.Religion.C_RELIGION)

        def AffichagePatronyme(self):
            return u"{}".format(getattr(self, identite.Identite.C_NOM))

        def AffichageAge(self):
            nbJoursVecus = temps.Date(getattr(self, temps.Date.DATE)).nbJours_ - temps.Date(getattr(self, temps.Date.DATE_NAISSANCE)).nbJours_
            if isinstance(nbJoursVecus, int):
                nbAnnees = nbJoursVecus/365
                return "{} ans".format(nbAnnees)
                # nbJoursPasses = nbJoursVecus%365
                # nbMois = nbJoursPasses/30
                # return "{} ans, {} mois".format(nbAnnees, nbMois)
            return "??? nbJoursVecus pas int : {}".format(nbJoursVecus)

        def AgeEnAnnees(self):
            if isinstance(self.GetValCarac(temps.Date.DATE_NAISSANCE), int):
                nbJoursVecus = temps.Date(getattr(self, temps.Date.DATE)).nbJours_ - temps.Date(getattr(self, temps.Date.DATE_NAISSANCE)).nbJours_
                nbAnnees = nbJoursVecus/365
                return nbAnnees
            return 0

        def DeterminerPortrait(self):
            """
            récupérer une liste de portraits selon les caracs du perso et en choisir un aléatoirement
            celui est choisi est stocké dans une carac mais en cas de changement important (âge, métier, coterie...) on en recalcule un
            """
            portr = portrait.Portrait()
            portraitStr = portr.DeterminerPortraitPersoPrincipal(self)
            self.SetCarac(portrait.Portrait.C_PORTRAIT, portraitStr)
            return self.GetValCarac(portrait.Portrait.C_PORTRAIT)

        # FONCTIONS GENERIQUES
        def __str__(self):
            """Affichage quand on affiche l'objet (print)"""
            str = u"Situation actuelle : "
            for carac in self.__dict__.keys():
                str = "{} {} ({}), ".format(str, self.__dict__[carac], carac)
            return str

        def __format__(self, format):
            # if(format == 'age'):
            #     return '23'
            return str(self)

        def AjouterCarac(self, idCarac, val):
            setattr(self, idCarac, val)

    # DATES ET TEMPS QUI PASSE-----------------------------------------------------------------------------------------------------------
        def AffichageDate(self):
            dateDuJour = self.GetDateDuJour()
            dateStr = u"{}".format(dateDuJour.formatGregorien())
            return dateStr

        def GetDateDuJour(self):
            """
            à overrider si la date du jeu destin a été overridée
            """
            nbJours = getattr(self, temps.Date.DATE)
            return temps.Date(nbJours)

        def GetDate(self, dateEnJours):
            """
            à overrider si la date du jeu destin a été overridée
            """
            return temps.Date(dateEnJours)

        def AvanceDeXJours(self, nbJoursPasses):
            nouvelleDateEnJours = getattr(self, temps.Date.DATE) + nbJoursPasses
            setattr(self, temps.Date.DATE, nouvelleDateEnJours)
            setattr(self, temps.Date.DATE_ANNEES, self.GetDate(nouvelleDateEnJours).GetNbAnnees())
            setattr(self, temps.Date.MOIS_ACTUEL, self.GetDate(nouvelleDateEnJours).GetNumMois())
            if self.GetValCarac(temps.Date.AGE_ANNEES) != "":
                setattr(self, temps.Date.AGE_ANNEES, self.AgeEnAnnees())

            # application des jours passés aux pnjs :
            for pnjObj in self.collectionPnjs.values():
                nbAnneesAvant = pnjObj.nbJours_/360
                pnjObj.nbJours_ = pnjObj.nbJours_ + nbJoursPasses
                nbAnneesApres = pnjObj.nbJours_/360
                # si le perso a pris une année et que la nouvelle année est un multiple de 5 on lui change de portrait
                if nbAnneesApres > nbAnneesAvant:
                    if nbAnneesAvant%5 == 0:
                        pnjObj.MajPortrait(self)

            # avancée des caracs de jours qui passent :
            # jours de convalescence :
            nbJoursConvalescence = self.GetValCaracInt(pbsante.PbSante.C_JOURS_DHOPITAL)
            if nbJoursConvalescence > 0:
                nbJoursConvalescence = nbJoursConvalescence - nbJoursPasses
                if nbJoursConvalescence < 0:
                    nbJoursConvalescence = 0
                setattr(self, pbsante.PbSante.C_JOURS_DHOPITAL, nbJoursConvalescence)

        def TourSuivant(self):
            """
            Passage au "tour" suivant dans un destin extermis c'est à dire grosso modo à un mois un peu randomisé
            """
            nbJoursPasses = 20 + random.randint(0, 20)
            self.AvanceDeXJours(nbJoursPasses)

        def AvanceDeXMois(self, nbMois):
            """
            Passage au mois suivant grosso modo
            """
            nbJoursPasses = (28 + random.randint(0, 3))*nbMois
            self.AvanceDeXJours(nbJoursPasses)

    # --------------- INVENTAIRE --------------------------

        def AjouterObjet(self, id):
            global objets_
            for objet in objets_:
                print("Objet : {}".format(objet.id_))
                print("id : {}".format(id))
                if id == objet.id_:
                    self.inventaire_.append(objet)
                    return
            print("erreur dans AjouterObjet : {} introuvable dans collectionObjets !".format(id))
