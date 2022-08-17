init -19 python:
    from abs.humanite import portrait
    from abs.univers import temps
    from abs.humanite.amour import relationAmoureuse
    from abs.humanite import identite
    import random
    import logging

    C_PERE = u"Père"
    C_MERE = u"Mère"

    class Pnj(object):

        STORE_PREFIX = "pnj"
        VALIDATE_VALUES = False
        COERCE_VALUES = False # False pour l'instant => bloque l'affectation à des types différents de ceux de l'origine, à exploiter un jour

        STAT_DEFAULTS = {
        }


        def __init__(self, sexeMasculin, **kwargs):
            """
            Initialize values from store or kwargs or default

            @param id: A unique id to use in the store. Generally set to
            the Character reference to allow cross object lookups

            @param **kwargs: Setup values that are not default
            """
            id = "id temp"
            if not isinstance(id, basestring):
                id = str(id) # should raise if not stringable

            self.__dict__['_id'] = id

            # self.run_optional_method( '__pre_init__', id, **kwargs )

            store_name = "{prefix}.{suffix}".format(
                prefix = type(self).STORE_PREFIX,
                suffix = self.__dict__['_id'] )

            setattr(store, store_name, {})

            self.__dict__['_store'] = getattr(store, store_name)

            for key, value in kwargs.items():
                if key not in self.__dict__['_store']:
                    setattr(self, key, value)

            for key, value in type(self).STAT_DEFAULTS.items():
                if key not in self.__dict__['_store']:
                    setattr(self, key, value)

            # self.__dict__['_nom_'] = ""
            self.CreerNomNeutre() # self.nom_
            self.sexeMasculin_ = sexeMasculin
            self.nbJours_ = -1
            self.traits_ = {} # dico contenant une liste de traits comme clés et leur valeur comme valeur
            self.portraitStr_ = ""
            self.relationAmoureuse_ = None
            self.vivant_ = True

        def Tuer(self):
            self.vivant_ = False

        # FONCTIONS GENERIQUES

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

            # return "" # A FAIRE : fait déconner la sauvegarde : POURQUOI ?
            return super(Pnj, self).__getattr__(key)


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

            return super(Pnj, self).__getattribute__(key)


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

        def __str__(self):
            """Affichage quand on affiche l'objet (print)"""
            str = u"Pnj : "
            for carac in self.__dict__.keys():
                str = "{} {} ({}), ".format(str, self.__dict__[carac], carac)
            return str
            """
            str = u"{}".format(self.nom_)

            if self.vivant_:
                nbJoursVecus = self.nbJours_
                if isinstance(nbJoursVecus, int):
                    nbAnnees = nbJoursVecus/365
                    nbJoursPasses = nbJoursVecus%365
                    nbMois = nbJoursPasses/30
                    if nbMois > 0:
                        str = u"{}\n{} ans, {} mois".format(str, nbAnnees, nbMois)
                    else:
                        str = u"{}\n{} ans".format(str, nbAnnees)
            else:
                if self.sexeMasculin_:
                    str = u"{}\nDécédé".format(str)
                else:
                    str = u"{}\nDécédée".format(str)

            return str
            """

        def MajPortrait(self, situation, metiers):
            """
            à appeler de temps en temps (changement de boulot, passage de dizaines en âge etc, je sais pas trop
            """
            portr = portrait.Portrait()
            ageNbAnnees = self.nbJours_/365
            cotObj = None
            metObj = None
            self.portraitStr_ = portr.DeterminerPortraits(situation, ageNbAnnees)

        def CreerNomNeutre(self):
            """
            TODO : adapter selon l'univers : ici ajouter les noms Francs
            """
            setattr(self, "nom_", "Sigebert (tmp)")

    def GenererPNJ(sexeMasculin, ageJours):
        """
        Génère un PNJ aléatoire avec un ensemble de caracs
        Il pourra ensuite être stocké dans la situation
        """
        global metiers_, collectionTraits_, collectionPnjs_

        ageAnnees = ageJours/360
        pnj = Pnj(sexeMasculin)

        pnj.nbJours_ = ageJours
        pnj.sexeMasculin_ = sexeMasculin
        pnj.portraitStr_ = ""
        # génération des traits :
        nbTraits = 2 + random.randint(0,5)
        m_Traits = []
        while nbTraits > 0:
            trait = collectionTraits_.getTraitAleatoire()
            if trait.PeutEtrePrisALaNaissance():
                pnj.traits_[trait.eTrait_] = trait.GetValeurALaNaissance()
                nbTraits = nbTraits - 1

        # pnj.MajPortrait(situation, metiers_)

        # ajouter ce nouveau pnj à la liste des pnjs de l'histoire
        # collectionPnjs_[pnj.nom_] = pnj

        return pnj

    def GenererPNJPapa(situation):
        nbJoursVecusPerso = temps.Date(getattr(situation, temps.Date.DATE)).nbJours_ - temps.Date(getattr(situation, temps.Date.DATE_NAISSANCE)).nbJours_
        ageJours = (30 + random.randint(0, 35)) * 12 *30 # âge 29 minimum (14 + 15 de l'âge du perso joué)
        return GenererPNJ(True, ageJours)

    def GenererPNJMaman(situation):
        nbJoursVecusPerso = temps.Date(getattr(situation, temps.Date.DATE)).nbJours_ - temps.Date(getattr(situation, temps.Date.DATE_NAISSANCE)).nbJours_
        ageJours = (30 + random.randint(0, 25)) * 12 *30 # âge 29 minimum (14 + 15 de l'âge du perso joué)
        pnj = GenererPNJ(False, ageJours)
        return pnj

    def GenererRelationAmoureuse(situation):
        nbJoursVecusPerso = temps.Date(getattr(situation, temps.Date.DATE)).nbJours_ - temps.Date(getattr(situation, temps.Date.DATE_NAISSANCE)).nbJours_
        ageAnnees = nbJoursVecusPerso/360 + (random.randint(0, 13) - random.randint(0, 15))
        if ageAnnees < 15:
            ageAnnees = 15
        ageJours = ageAnnees * 12 *30
        pnj = GenererPNJ(False, situation, ageJours)
        # calculer les niveaux d'intérêt des persos l'un envers l'autre
        interetPnjEnversJoueur = relationAmoureuse.CalculerAmabiliteHommePremierContact(situation.GetDicoTraits())
        interetJoueurEnversPnj = relationAmoureuse.CalculerAmabiliteFemmePremierContact(pnj.traits_)
        pnj.relationAmoureuse_ = relationAmoureuse.RelA(interetPnjEnversJoueur, interetJoueurEnversPnj)
        return pnj
