from unittest.mock import patch
from app.surveillance import surveiller
from app.notifications import envoyer_notification

def test_surveiller_taux_eleve():
    with patch("app.surveillance.envoyer_notification") as notifier:
        resultat = surveiller(0.15)

        assert resultat == "alerte"
        notifier.assert_called_once_with("Taux eleve")

def test_surveiller_taux_normal():
    with patch("app.surveillance.envoyer_notification") as notifier:
        resultat = surveiller(0.05)

        assert resultat == "ok"
        notifier.assert_not_called()
        
def test_surveiller_taux_limite():
    with patch("app.surveillance.envoyer_notification") as notifier:
        resultat = surveiller(0.10)

        assert resultat == "ok"
        notifier.assert_not_called()
        
def test_notification_service_indisponible():
    import pytest

    with pytest.raises(RuntimeError, match="Service non configure"):
        envoyer_notification("Test")
        
