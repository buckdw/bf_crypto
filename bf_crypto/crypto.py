from fernet import Fernet


def encrypt(plaintext, fernetkey):
    fernet = Fernet(fernetkey)
    return fernet.encrypt(bytes(plaintext, "utf-8")).decode("utf-8")


def decrypt(cypher, fernetkey):
    fernet = Fernet(fernetkey)
    return fernet.decrypt(bytes(cypher, "utf-8")).decode("utf-8")