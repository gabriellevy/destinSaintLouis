#include <QApplication>
#include "moyenage.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    MoyenAge* av = new MoyenAge(ModeAffichage::ema_Jeu);
    av->m_Reglages.ChangeTaille(1280, 800);
    av->show();

    return a.exec();
}
