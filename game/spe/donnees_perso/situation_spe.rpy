init -10 python:
    from abs.religions import religion
    from chapitres.classes import heros
    from spe.humanite import portrait_saint_louis
    from abs.humanite import portrait
    from abs.humanite import metier
    from abs.humanite import trait
    import random

    class SituationSpe(Situation):

        # Set the store.{prefix}.character_id value
        STORE_PREFIX = "stats_spe"

        # Boolean toggle for validation - defaults both True
        VALIDATE_VALUES = False
        COERCE_VALUES = False

        STAT_DEFAULTS = {
        }

        def __init__(self, id, **kwargs):
            Situation.__init__(self, id, **kwargs)
            date = temps.Date(365 * 1210) # A FAIRE : déterminer une date de début d'histoire
            self.SetValCarac(temps.Date.DATE, date.nbJours_)

        # def __init__(self):
        #     situation.Situation.__init__(self, 175000)

        # ------------------------------------------------AFFICHAGE---------------------------------------
        def AffichageFideliteGaule(self):
            global debug_
            str = u""
            val = self.GetValCaracInt(heros.Heros.C_FIDELITE_PEUPLE)
            if val < 0:
                str = u"Détesté par les gaulois"
            elif val <= 2:
                str = u"Connu des gaulois"
            elif val <= 4:
                str = u"Accepté par les gaulois"
            elif val <= 7:
                str = u"Apprécié par les gaulois"
            elif val <= 10:
                str = u"Adoré par les gaulois"
            else:
                str = u"Vénéré par les gaulois"
            if self.debug_:
                return u"{} ({})".format(str, val)
            return str

        def AffichageArmee(self):
            global debug_
            # armée
            str = u""
            val = self.GetValCaracInt(heros.Heros.C_MILITAIRE)
            if val < 0:
                str = u"Armée insignifiante"
            elif val <= 2:
                str = u"Armée faible"
            elif val <= 4:
                str = u"Bonne armée"
            elif val <= 7:
                str = u"Armée puissante"
            elif val <= 10:
                str = u"Armée redoutable"
            else:
                str = u"Armée invincible"
            if self.debug_:
                return u"{} ({})".format(str, val)
            return str

        def AffichageDiplomatie(self):
            global debug_
            str = u""
            val = self.GetValCaracInt(heros.Heros.C_DIPLOMATIE)
            if val < 0:
                str = u"Roi méprisé par les autres souverains"
            elif val <= 2:
                str = u"Roi respecté à l'étranger"
            elif val <= 4:
                str = u"Roi reconnu à qui les souverains font confiance"
            else:
                str = u"Roi le plus respecté d'Europe"
            if self.debug_:
                return u"{} ({})".format(str, val)
            return str

        def AffichageReligion(self):
            if self.GetValCarac(religion.Religion.C_RELIGION) == religion.Paien.NOM:
                valPretre = self.GetValCaracInt(metier.Pretre.NOM)
                strPretre = u""
                if valPretre > 0:
                    strPretre = u" - Prêtre roi"
                str =  u"Païen{}".format(strPretre)
                if self.debug_:
                    str = u"{} ({})".format(str, self.caracs_[heros.Heros.C_CHRISTIANISME])
                return str
            if self.caracs_[religion.Religion.C_RELIGION] == religion.Christianisme.NOM:
                if self.debug_:
                    return u"{} ({})".format(self.caracs_[religion.Religion.C_RELIGION], self.caracs_[heros.Heros.C_CHRISTIANISME])

            return self.caracs_[religion.Religion.C_RELIGION]

        def AffichageGloire(self):
            val = self.GetValCarac(heros.Heros.C_GLOIRE)
            if self.debug_:
                return u"Gloire : {}".format(val)
            return u""

        def AffichageUsurpation(self):
            val = self.GetValCarac(heros.Heros.C_USURPATION)
            if self.debug_:
                return u"Risques d'usurpation : {}".format(val)
            return u""

        def AffichageRichesse(self):
            strRichesse = self.collectionTraits[trait.Richesse.NOM].GetDescription(self)
            if ( trait.Richesse.NOM not in self.caracs_):
                if self.debug_:
                    strRichesse = u"Riche (0)"
                strRichesse = u"Riche"

            val = self.GetValCarac(trait.Richesse.NOM)
            if val <= trait.Trait.SEUIL_A_PAS_EXTREME:
                strRichesse = u"Misérable" # val <= -13
            elif val <= -8:
                strRichesse = u"Pauvre" # -8 >= val > -13
            elif val <= trait.Trait.SEUIL_A_PAS:
                strRichesse = u"En difficulté financière" # -3 >= val > -8
            elif val <= trait.Trait.SEUIL_A:
                strRichesse = u"Riche" # 1 >= val > -3
            elif val <= 6:
                strRichesse = u"Très Riche" # 6 >= val > 1
            elif val <= trait.Trait.SEUIL_A_EXTREME:
                strRichesse = u"Incroyablement riche" # 11 >= val > 1
            else:
                strRichesse = u"Fabuleusement riche" # val > 11

            if strRichesse == "":
                strRichesse = u"Riche"
            if self.debug_:
                strRichesse = u"{} ({})".format(strRichesse, self.collectionTraits[trait.Richesse.NOM].GetVal(self))
            return strRichesse

        def DeterminerPortrait(self):
            """
            récupérer une liste de portraits selon les caracs du perso et en choisir un aléatoirement
            celui est choisi est stocké dans une carac mais en cas de changement important (âge, métier, coterie...) on en recalcule un
            """
            portr = portrait_saint_louis.PortraitSpe()
            portraitStr = portr.DeterminerPortraitPersoPrincipal(self, True)
            self.SetCarac(portrait.Portrait.C_PORTRAIT, portraitStr)
            return self.GetValCarac(portrait.Portrait.C_PORTRAIT)

        # ------------------------------------------------- PNJ ---------------------------------------------------

        def AffichagePortraitPere(self):
            # père
            str = u""
            pere = self.GetValCarac(pnj.Pnj.C_PERE)
            if isinstance(pere, PnjSaintLouis) :
                return pere.portraitStr_
            return ""

        def AffichagePortraitMere(self):
            # mère
            str = u""
            mere = self.GetValCarac(pnj.Pnj.C_MERE)
            if isinstance(mere, PnjSaintLouis) :
                return mere.portraitStr_
            return ""

        def AffichagePere(self):
            # père
            str = u""
            pere = self.GetValCarac(pnj.Pnj.C_PERE)
            if isinstance(pere, PnjSaintLouis) :
                str = u"{}".format(pere)
            return str

        def AffichageMere(self):
            # mère
            str = u""
            mere = self.GetValCarac(pnj.Pnj.C_MERE)
            if isinstance(mere, PnjSaintLouis) :
                str = u"{}".format(mere)
            return str

        # -------------------------------------------------- temps -------------------------------------------------

        def TourSuivant(self):
            """
            Passage au "tour" suivant c'est à dire grosso modo à un mois et demi un peu randomisé
            """
            nbJoursPasses = 38 + random.randint(0, 20)
            self.AvanceDeXJours(nbJoursPasses)
