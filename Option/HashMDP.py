import hashlib

def hasher_mot_de_passe(mot_de_passe):
    mot_de_passe = input("Entrez le mot de passe à hasher : ")
    mot_de_passe_hash = hasher_mot_de_passe(mot_de_passe)
    mot_de_passe_bytes = mot_de_passe.encode()
    hash_object = hashlib.sha256(mot_de_passe_bytes)
    return hash_object.hexdigest()
    print(f"Le mot de passe hashé est : {mot_de_passe_hash}")
