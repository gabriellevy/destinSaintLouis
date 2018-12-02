#include "viesaintlouis.h"
#include "ui_aventure.h"
#include "saintlouis.h"

VieSaintLouis::VieSaintLouis(QWidget *parent):Histoire(parent)
{

}

void VieSaintLouis::GenererHistoire()
{
    m_Themes.append("Moyen-âge");

    GenererEvtsAccueil();
}


void VieSaintLouis::GenererPersos()
{
    SaintLouis saint_louis( "saint_louis", "Saint Louis", "", ":/images/perso/saint_louis.jpg");
    IPerso::AjouterPersoJouable(saint_louis);
}

void VieSaintLouis::GenererEvtsAccueil()
{
    Evt* Debut = AjouterEvt("Debut", "Test début saint louis");
    Effet* intro = Debut->AjouterEffetNarration(
                "Vous êtes Saint Louis");

}

