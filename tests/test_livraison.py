from app.livraison import frais_livraison

def test_livraison_panier_ordinaire():
    
    montant = 120 #Arrange : Préparation des données
    
    resultat = frais_livraison(montant) #Act : Executer fonction
    
    assert resultat == 25 # Assert : Vérifier le résultat

def test_livraison_299():
    assert frais_livraison(299) == 25
    
def test_livraison_300():
    assert frais_livraison(300) == 0
    
def test_livraison_301():
    assert frais_livraison(301) == 0

def test_livraison_zero():
    assert frais_livraison(0) == 25

def test_livraison_montant_negatif():
    import pytest
    with pytest.raises(ValueError):
        frais_livraison(-10)