# Rago Bot - Créateur d'équipes League of Legends

Ce bot Discord permet de créer des équipes aléatoires pour le jeu League of Legends en utilisant une API.

## Fonctionnement

Ce bot propose une commande `create_team` qui récupère aléatoirement des champions pour former deux équipes (Blue Side et Red Side). Les champions sont récupérés à partir d'une API externe.

## Prérequis

Avant d'utiliser ce bot, assurez-vous d'avoir les éléments suivants :

- Python 3 installé sur votre système
- Les bibliothèques Discord.py et Flask installées (vous pouvez les installer en exécutant `pip install discord flask` dans votre terminal)
- Une clé d'API pour l'API externe (à configurer dans le code)

## Installation

1. Clonez ce dépôt sur votre machine locale.
2. Modifiez le fichier `config.py` pour ajouter votre clé d'API.
3. Exécutez le bot en exécutant `python main.py` dans votre terminal.

## Utilisation

Une fois le bot en ligne, vous pouvez interagir avec lui sur Discord en utilisant la commande `/create_team`.

## Contribution

Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce bot, n'hésitez pas à soumettre une demande de fusion.

## Licence

Ce projet est sous licence MIT. Pour plus d'informations, consultez le fichier LICENSE.md.
