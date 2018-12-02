#ifndef VIESAINTLOUIS_H
#define VIESAINTLOUIS_H

#include <QWidget>
#include "../destinLib/histoire.h"


class VieSaintLouis : public Histoire
{
    Q_OBJECT

public:
    VieSaintLouis(QWidget *parent = nullptr);

    virtual void GenererHistoire();

private:
    void GenererEvtsAccueil();
    virtual void GenererPersos();
};

#endif // VIESAINTLOUIS_H
