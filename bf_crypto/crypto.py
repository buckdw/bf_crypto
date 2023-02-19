#
#!/usr/bin/env python3
#

__author__ = 'Diederick de Buck'
__version__ = '3.0.0'
__date__ = "$Jan 29, 2019 10:02:13 PM$"
__maintainer__ = 'Diederick de Buck'
__email__ = 'diederick.de.buck@blue-fez.com'

from fernet import Fernet

def encrypt(plaintext, fernetkey):
    try:
        fernet = Fernet(fernetkey)
    except:
        return None
    return fernet.encrypt(bytes(plaintext, "utf-8")).decode("utf-8")


def decrypt(cypher, fernetkey):
    try:
        fernet = Fernet(fernetkey)
    except:
        return None
    return fernet.decrypt(bytes(cypher, "utf-8")).decode("utf-8")
