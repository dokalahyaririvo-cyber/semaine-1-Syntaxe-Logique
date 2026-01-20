def calculate_ttc(prixttc:float, taux_tava: float=0.20)-> float:
    prixttc  = prixttc * (1 + taux_tava)
    return prixttc