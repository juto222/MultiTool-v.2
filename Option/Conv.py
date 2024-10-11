import ipaddress

def convertir():
    
    ipv6_hex = input("Entrez une adresse IPv6 en hexadécimal (ex: 20010dbc29999999999999999999991) : ")

    try:
        ipv6_normal = ipaddress.IPv6Address(ipv6_hex)
        print("Adresse IPv6 au format normal :", ipv6_normal)
    except ValueError:
        print("Erreur : Adresse IPv6 invalide.")

