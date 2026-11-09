def nettoyer_texte(texte):
    if not isinstance(texte, str):
        raise TypeError("Le texte doit être une chaîne")

    return " ".join(texte.lower().split())

