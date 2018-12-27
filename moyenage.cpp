#include "moyenage.h"
#include "../destinLib/perso.h"
#include "ui_univers.h"
#include "viesaintlouis.h"

MoyenAge::MoyenAge(ModeAffichage modeAffichage,
                   QWidget *parent,
                   QString premierEvt,
                   QString premierEffet)
: Univers(parent, modeAffichage, true)
{
    m_Perso = new IPerso(ui->persoWidget);
    m_Histoire = new VieSaintLouis(ui->histoireWidget);
    this->setWindowTitle("Vie de Saint Louis");

    // positionner l'interface
    ui->persoWidget->layout()->addWidget(m_Perso);
    //m_Perso->show();
    ui->histoireWidget->layout()->addWidget(m_Histoire);

    GenererAventure();

    if ( premierEvt != "" )
        m_Histoire->SetCurrentEvtId( premierEvt ) ;
    if ( premierEffet!= "" )
        m_Histoire->SetEffetIndex(m_Histoire->DeterminerIndexEffet(premierEffet) );

    m_EtatPartie = EP_Deroulement;

    // tmp
    m_Reglages.m_SonOn = false;
    //fin tmp

    LancerEvtEtOuEffetCourant();
}

void MoyenAge::GenererAventure()
{
    GenererCaracs();

    m_Histoire->GenererPersos();

    m_Histoire->GenererHistoire();

    m_Perso->RafraichirAffichage();
}

void MoyenAge::GenererCaracs()
{
    //m_Histoire->m_Caracs.append(new Jauge(Run::pv, "PV", 0, 8,8,"", ""));
}
