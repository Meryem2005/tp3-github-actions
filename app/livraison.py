def frais_livraison(montant) : 
    if montant < 0 : 
        raise ValueError("Montant Négatif")
    if montant >= 300 : 
        return 0
    return 25
