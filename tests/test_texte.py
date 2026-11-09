import pytest
from app.texte import nettoyer_texte


@pytest.mark.parametrize("entree, attendu", [
    (" BONJOUR ", "bonjour"),
    ("BONJOUR TOUT LE MONDE", "bonjour tout le monde"),
    ("  Bonjour   Tout   Le Monde  ", "bonjour tout le monde"),
    ("", ""),
    ("Python", "python")
])
def test_nettoyer_texte(entree, attendu):
    assert nettoyer_texte(entree) == attendu
    
@pytest.mark.parametrize("entree", [123, None])
def test_nettoyer_texte_type_invalide(entree):
    with pytest.raises(TypeError):
        nettoyer_texte(entree)
        
def test_nettoyer_texte_idempotence():
    texte = "  BONJOUR   TOUT LE MONDE  "
    resultat = nettoyer_texte(texte)

    assert nettoyer_texte(resultat) == resultat
    
