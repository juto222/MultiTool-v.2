import random


def generate_ipv6():
    ipv6 = ":".join(f"{random.randint(0, 65535):x}" for _ in range(8))
    print("Votre nouvelle IP générée est : ", ipv6)




