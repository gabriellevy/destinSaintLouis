screen valeurs_traits():
    tag interface_personnage
    $ descriptionTrait = situation_.DescriptionTraits(traits_)
    $ descriptionBlessures = situation_.DescriptionBlessuresEtMaladies(blessures_, maladies_)
    $ strMetier = situation_.AffichageMetier()
    $ strMissions = DescriptionMissionsActives()
    $ strDate = situation_.AffichageDate()
    $ strIndices = situation_.AffichageIndices()
    frame:
        xpos 5 ypos 5
        vbox:
            textbutton _("Description suivante"):
                action Function(InterfaceSuivante)
            if interfaceMode_ == 0: # résumé des données importantes du perso
                text _(u"[strMetier]")
                text _(u"[descriptionBlessures]")
                text _(u"[descriptionTrait]")
            elif interfaceMode_ == 1: # données d'enquête ??
                text _(u"[strDate]")
                text _(u"[strMissions]")
                text _(u"[strIndices]")
            elif interfaceMode_ == 2: # inventaire
                hbox:
                    for i in situation_.inventaire_:
                        # On crée une frame...
                        frame:
                            xpadding 10
                            ypadding 10
                            xmargin 10
                            ymargin 10
                            # Contenant l'image attachée à chaque item.
                            add i.image_ size(60,60)
