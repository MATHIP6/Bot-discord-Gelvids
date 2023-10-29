from time import *
from random import *

quoi = ["Quoi", "Quoi ?", "quoi", "quoi ?", "QUOI", "QUOIII", "Quoi ???"]

rouge = ["Rouge", "rouge", "ROUGE"]

oui = ["oui", "Oui", "OUI", "Oui ?", "oui ?"]

tg = ["tg", "Tg", "TG", "Ta gueule"]

blagues = ["Qui est jaune et qui attend ??? ||Jonathan || ", "Comment appelle-t-on une chauve-souris avec une perruque ??? || Une souris  ||", "Que fait un crocodile quand il rencontre une superbe femelle ??? || Il Lacost ||", "C'est l'histoire du ptit dej, tu la connais ??? || Pas de bol ||", 
"Que demande un footballeur à son coiffeur ??? ||La coupe du monde s’il vous plait||", "C'est l'histoire d'un pingouin qui respire par les fesses. Un jour il s’assoit et il meurt.", "Que dit un escargot quand il croise une limace ??? ||Oh un nutiste||", "Quel est le crustacé le plus léger de la mer ??? || La palourde ||", 
"Qu'est-ce qui n'est pas un steak ??? || Une pastèque. ||", "Pourquoi est-ce que Napoléon n'a pas voulu acheter de maison ??? || Parce qu’il avait déjà un Bonaparte ||", "Quelle est la mamie qui fait peur aux voleurs ??? || Mamie Traillette. ||", 
"Comment appelle-t-on un chien qui n'a pas de pattes ??? || On ne l’appelle pas, on va le chercher… ||", "Qu'est-ce qu'un tennisman adore faire ??? |||Rendre des services.|||", "Pourquoi est-ce que les livres ont-ils toujours chaud ??? |||Parce qu’ils ont une couverture.|||",
"Où est-ce que les super-héros vont-ils faire leurs courses ??? |||Au supermarché.|||", "Que se passe-t-il quand 2 poissons s'énervent ??? |||Le thon monte.|||", 
"Quel fruit est assez fort pour couper des arbres ??? |||Le citron.|||", "Quel est le jambon que tout le monde déteste ??? |||Le sale ami.|||", "Que fait un cendrier devant un ascenseur ??? |||Il veut des cendres.|||", 
"Que dit une imprimante dans l'eau ??? |||J’ai papier.|||", "Quel est l'aliment le plus hilarant ??? |||Le riz.|||", "Quel est le sport préféré des insectes ??? |||Le cricket.|||"]

mots = ["chien", "chat", "voiture", "camion", "bateau", "avion", "moto", "lapin", "tortue", "cahier", 
"portable", "table", "maison", "garçon", "pontalon", "livre", "dophin", "manette", "ordinateur", "fille", 
"tableau"]

account = ["Epic Game", "Steam", "Microsoft", "Tiktok", "Google", "Apple", "P*rnhub Premium", "Instagram", 
"Twitter", "Paypal", "Telegram", "Twitch"]

email = ["@gmail.com", "outlook.com", "email.com"]

def pourcent():
    a = randint(0, 100)
    return a

def rdm():
    chiffre = randint(0, (len(blagues) - 1))
    return chiffre

def heure():
    return ("Il est " + strftime("%H") + ":" + strftime("%M") + ":" + strftime("%S") + " et le " + strftime("%d") + "/" + strftime("%m") + "/" + strftime("%y"))

print(rdm())