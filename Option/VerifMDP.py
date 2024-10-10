import re

def mdp_force(password):
    # Initialisation du score
    score = 0

    # Critère 1: Longueur du mot de passe (minimum 8 caractères)
    if len(password) >= 8:
        score += 1
    else:
        print("Le mot de passe est trop court. Il doit contenir au moins 8 caractères.")

    # Critère 2: Contient des lettres minuscules
    if re.search(r'[a-z]', password):
        score += 1

    # Critère 3: Contient des lettres majuscules
    if re.search(r'[A-Z]', password):
        score += 1

    # Critère 4: Contient des chiffres
    if re.search(r'[0-9]', password):
        score += 1

    # Critère 5: Contient des caractères spéciaux
    if re.search(r'[@$!%*?&]', password):
        score += 1

    # Évaluation de la force du mot de passe
    if score == 5:
        print("Mot de passe très fort")
    elif 3 <= score < 5:
        print("Mot de passe moyen")
    else:
        print("Mot de passe faible")

    # Retourne le score pour des utilisations ultérieures
    return score
