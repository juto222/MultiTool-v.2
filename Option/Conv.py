import ipaddress

def convertir():
    # Demande à l'utilisateur d'entrer une adresse IPv6 en hexadécimal
    ipv6_hex = input("Entrez une adresse IPv6 en hexadécimal (ex: 20010db8000000000000000000000001) : ")

    try:
        # Convertit la chaîne hexadécimale en adresse IPv6
        ipv6_normal = ipaddress.IPv6Address(ipv6_hex)
        print("Adresse IPv6 au format normal :", ipv6_normal)
    except ValueError:
        print("Erreur : Adresse IPv6 invalide.")

