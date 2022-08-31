# toutes les datas d'état du jeu (sauvegardées etc)
default situation_ = SituationSpe("situation_")

# --------------------------------------------
# ------------------ Persos ------------------
# --------------------------------------------
define narrator = Character(color="#fafad8", what_italic=True)
 # personnage standard remplacé selon les situations. (son nom est mis à jour avant utilisation)
define std = Character('Perso standard...', color="#B22222")
define bl = Character('Blanche de Castille', color="#800000")

# Musiques
define audio.roi_mort = "musique/akingisdead.ogg"
define audio.turexgloriae = "musique/turexgloriae.ogg" # baptème etc
define audio.christ1 = "musique/journeytoabsolution.ogg"
define audio.youpi_paien = "musique/Quite An Adventure.ogg"
define audio.paien_sombre = "musique/Woe Alas And Alack.ogg"
define audio.printemps = "musique/Sea Season.ogg"
define audio.hiver = "musique/Dark Season.ogg"
define audio.ete = "musique/Fire Season.ogg"
define audio.guerre1 = "musique/saladinbesiegejerusalem.ogg"
define audio.guerre2 = "musique/siegeofkerak.ogg"
define audio.epique_principale = "musique/hornsofhattinandaftermath.ogg"
define audio.conquetes = "musique/marchtoholyland.ogg" # marche vers la terre sainte (crusader king II)
define audio.danger = "musique/Danger.ogg"

init -10 python:
    from abs import selecteur
    import random

    selecteur_ = selecteur.Selecteur()
    def determinationEvtCourant(situation):
        global selecteur_
        return selecteur_.determinationEvtCourant(situation)

init -1 python:
    from abs import selecteur
    from spe.donnees_perso import missions
    from abs.donnees_perso import mission
    from abs.donnees_perso import possession
    from spe.donnees_perso import objet_spe
    import random

    AjouterEvtsProfessionnels()
    AjouterEvtsRoi()
    AjouterEvtAvenement()
    AjouterEvtsRien()
    AjouterEvtsDiplomatie()
    AjouterEvtsHistoire()
    AjouterEvtsFamille()
    AjouterEvtsMongols()

# Le jeu commence ici
label start:
    scene bg priere
    # play music musique_menu
    queue music [ epique_principale, conquetes ] # pseudo liste de lecture temporaire
    jump init_secondary_data

label init_secondary_data:
    python:
        traits_ = trait.CollectionTraits()
        # situation_.collectionTraits = traits_
        blessures_ = pbsante.CollectionBlessures()
        # situation_.collectionBlessures = blessures_
        maladies_ = pbsante.CollectionMaladies()
        # situation_.collectionMaladies = maladies_
        metiers_ = metier.CollectionMetiers()
        # situation_.collectionMetiers = metiers_
        missions_ = missions.Missions()

        collectionPnjs_ = {}
        debug_ = True
        # situation_.debug_ = debug_
    jump naissance

label debut_cycle:
    show screen valeurs_traits
    $ prochainEvt = determinationEvtCourant(situation_)
    $ renpy.jump(prochainEvt)

label fin_cycle:
    # "Fin d'un cycle."
    # jump mort # tmp test

    $ situation_.TourSuivant()

    if situation_["Santé"] != "Mort":
        jump debut_cycle


label labelGoTo_pasFait:
    "Ce sélecteur d'énévement n'a pas de label go to on dirait"

label pas_evt_trouve:
    " ERREUR : pas d'événement trouvé à ce cycle"

label probaAbsoluesSup100:
    "Le total des probas absolues dépasse 100%% !"
