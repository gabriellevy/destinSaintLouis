# fichier où sont générés les phrases d'ambiance à afficher quand il ne se passe rien durant un mois particulier

init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import testDeCarac
    from abs import condition
    from abs.humanite import trait
    from abs.univers import temps
    from abs.humanite import identite
    from chapitres.classes import heros
    from abs.religions import religion

    def genererDateNaissance(ageActuel=15):
        global situation_
        nbJoursDateNaissance = situation_.GetValCaracInt(temps.Date.DATE) - 365*ageActuel
        situation_[temps.Date.DATE_NAISSANCE] = nbJoursDateNaissance

    def genererLouis(tousLesTraits):
        global situation_
        # situation[trait.Violence.NOM] = trait.Trait.SEUIL_A_EXTREME
        # situation[trait.Opportunisme.NOM] = trait.Trait.SEUIL_A_EXTREME
        # situation[trait.Assurance.NOM] = trait.Trait.SEUIL_A_EXTREME
        # situation[trait.Observation.NOM] = trait.Trait.SEUIL_A
        # situation[trait.Cupidite.NOM] = trait.Trait.SEUIL_A_EXTREME
        # situation[trait.Courage.NOM] = trait.Trait.SEUIL_A
        # situation[trait.Ruse.NOM] = trait.Trait.SEUIL_A
        # situation[trait.Ambition.NOM] = trait.Trait.SEUIL_A
        # situation[trait.Rancune.NOM] = trait.Trait.SEUIL_A_EXTREME
        # situation[trait.Franchise.NOM] = trait.Trait.SEUIL_A_PAS
        # situation[trait.Altruisme.NOM] = trait.Trait.SEUIL_A_PAS
        situation_[trait.Richesse.NOM] = trait.Trait.SEUIL_A_PAS

        situation_[metier.Metier.C_METIER] = u"Prince"

        # compétences professionnelles
        situation_[metier.Politique.NOM] = trait.Trait.SEUIL_A
        situation_[metier.Guerrier.NOM] = trait.Trait.SEUIL_A
        situation_[metier.Chasseur.NOM] = trait.Trait.SEUIL_A

        # caracs spécifiques
        situation_[heros.Heros.C_SAINTETE] = 0
        # situation[heros.Heros.C_MILITAIRE] = 0
        # situation[heros.Heros.C_DIPLOMATIE] = 0
        # situation.SetValCarac(heros.Heros.C_GLOIRE, 0)

        # famille
        # situation.SetValCarac(heros.Heros.C_ALBOFLEDE, 1)

        # légalisme
        # situation.SetValCarac(heros.Heros.C_LOI_SALIQUE, 1)

        situation_[identite.Identite.C_NOM] = heros.Heros.C_NOM

        # situation[heros.Heros.CARTE_ACTUELLE] = "bg carte481"
        return

    def genererParents():
        global situation_
        pere = GenererPNJPapa()
        # pere.ageJours = 36 * 12 *30 + 24
        # pere.prenom_ = heros.Heros.C_NOM_LOUISVIII
        # pere.nom_ = ""
        # pere.sexeMasculin_ = True
        # pere.portraitStr_ = "images/portraits/louisVIII.jpg"
        situation_.SetValCarac(C_PERE, pere)

        # mere = GenererPNJMaman()
        # mere.ageJours = 35 * 12 *30 + 297
        # mere.prenom_ = heros.Heros.C_NOM_BLANCHE
        # mere.nom_ = ""
        # mere.sexeMasculin_ = False
        # mere.portraitStr_ = "images/portraits/blanche_de_castille.jpg"
        # situation_.SetValCarac(C_MERE, mere)

label naissance:
    $ genererDateNaissance(9) # à la mort de Philippe Auguste 14 juillet 1223
    $ genererLouis(traits_)
    $ genererParents() # A FAIRE : si on décommente cette partie la sauvegarde ne fonctionne plus, trouver pourquoi (probablement parce que PNJ n'est pas un type sauvable picckle truc)
    jump intro
