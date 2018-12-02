#include <QApplication>
#include "moyenage.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    MoyenAge* av = new MoyenAge(ModeAffichage::ema_Jeu);
    av->show();

    return a.exec();
}
