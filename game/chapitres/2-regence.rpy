

label regence:
    scene bg regence
    show blanche at left
    with moveinleft
    bl "Mon fils, j'aimerais mieux vous voir mort que coupable d'un seul péché mortel."
    jump fin_cycle

label avenement:
    # royaume de Louis à son avènement
    "A FAIRE : afficher carte et décrire royaume"
    "Grâce à votre père mais surtout grace à Philippe Auguste votre grand-père votre domaine est très vaste."
    "Les caisses sont pleines, le royaume est riche, solide et bien organisé. À vous de vous rendre digne de cet héritage somptueux."
    # $ AfficherCarteActuelle()
    # with dissolve
    $ situation_.SetValCarac(metier.Metier.C_METIER, metier.Roi.NOM)
    jump fin_cycle
