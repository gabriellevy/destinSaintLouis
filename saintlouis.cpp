#include "saintlouis.h"
#include "viesaintlouis.h"

SaintLouis::SaintLouis(QString id, QString nom, QString description, QString imagePortrait)
    :DPerso(id, nom, description)
{
    m_ImagePortrait.load(imagePortrait);

    //m_CaracsAAfficher.append(Run::pv);
}
