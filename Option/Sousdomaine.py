import dns.resolver

def sousdomaine():
    domain = input("Entrez le domaine cible ex(url.com): ")
    subdomains = ['www', 'mail', 'ftp', 'dev', 'admin']
    for sub in subdomains:
        try:
            result = dns.resolver.resolve(f'{sub}.{domain}', 'A')
            print(f'Sous-domaine trouvé : {sub}.{domain} - IP : {result[0]}')
        except dns.resolver.NXDOMAIN:
            pass
        except Exception as e:
            print(f'Erreur : {e}')