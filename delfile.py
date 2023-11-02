"""
Utilitaires pour effacer l ensemble des fichiers d'un repertoire ormis ceux
referencé dans un fichier nommé "fichiers.txt"

Programme réalisé à la demande de TancredTerror(https://www.twitch.tv/tancredterror)
pour son MOD : Escape from Knox
"""

import os
import sys

# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    curDirectory = os.path.dirname(sys.executable)
elif __file__:
    curDirectory = os.path.dirname(__file__)

print (f"repertoire : {curDirectory}")

# recupere la liste des fichiers a conserver
listeProtect =["delfile.exe",
               "delfile.py",
               "fichiers.txt"]
try :
    with open('fichiers.txt', 'r') as f:
        for line in f:
            listeProtect.append(line.strip())
except:
    print('ERROR : Impossible de trouver le fichier "fichiers.txt" dans le repertoire.')
    exit(0)

# obtient la liste des fichier du repertoire a verifier
files = os.listdir(curDirectory)

# pour chaque fichier, test si les fichiers sont dans la liste de fichier à conserver sinon, efface
for file in files:
    if file not in listeProtect and file[0] != ".":
        os.remove(os.path.join(curDirectory, file))
        print(f"{file} effacé...")

# sort du script
print(f"Nettoyage du repertoire {curDirectory} effectué.")
