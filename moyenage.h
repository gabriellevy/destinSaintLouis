#ifndef MOYENAGE_H
#define MOYENAGE_H

#include <QWidget>
#include "../destinLib/univers.h"


class MoyenAge : public Univers
{
    Q_OBJECT
private:

protected:
    // pour les aventures qui n'utilisent pas le json mais du code :surclasser aventure et développer cette fonction
    virtual void GenererAventure();
    // génère toutes les caracs qui peuvent être visualisées par le joueur (d'autres caracs peuvent être générées et invisibles n'importe quand dans l'aventure)
    virtual void GenererCaracs();

public:
    MoyenAge(ModeAffichage modeAffichage = ModeAffichage::ema_Jeu, QWidget *parent = nullptr, QString premierEvt = "", QString premierEffet = "");
};

#endif // MOYENAGE_H
