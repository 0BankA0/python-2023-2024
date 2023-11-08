from cryptography.fernet import Fernet


atslega = Fernet.generate_key()

print(atslega)

a = Fernet(atslega)

teksts= b'slepeni dati'

kriptDati = a.encrypt(teksts)

print(kriptDati)

print(a.decrypt(kriptDati))