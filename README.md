# chaos4music

Un projet inspiré du concept de Reservoir Computing, chaos4music exploite des réservoirs pour générer de la musique de manière innovante. L'idée principale est d'utiliser un réservoir capable de sélectionner, parmi une banque de samples, celui qui sera joué, créant ainsi une expérience musicale unique et imprévisible.

## Présentation

- **But du projet :** Utiliser des réservoirs pour la création musicale en sélectionnant dynamiquement le sample à jouer.
- **Concept :** S'inscrire dans le paradigme du Reservoir Computing pour explorer la génération et la manipulation de sons.
- **Inspiration :** Ce projet s'inspire du projet ReMi de Hugo Chateau Laurent, et apporte une touche originale avec une approche chaotique.

## Installation

Pour installer l'environnement de développement et les dépendances nécessaires, suivez les étapes ci-dessous :

### Création de l'environnement virtuel

```
python -m venv musicvenv
source musicvenv/bin/activate
```

### Installation des dépendances

```
pip install -r requirements.txt
```

### Préparation des fichiers sons
```
cd samples
unzip OneShots-24bit-WAV.zip
unzip 808_drum_kit.zip
cd ..
```

## Utilisation

Après avoir configuré l'environnement, vous pouvez lancer le projet et expérimenter avec le réservoir. L'application lira les samples disponibles et, en fonction des paramètres du réservoir, sélectionnera le sample à jouer, vous permettant ainsi d'explorer des combinaisons sonores inédites et chaotiques.

En laissant ce code vous allez créer un réservoir qui va générer 16 notes en utilisant 2 samples (deux échantillons de son) :
```
python reservoir_2samples.py
```

## Contribuer

Les contributions sont les bienvenues ! N'hésitez pas à soumettre des issues ou des pull requests pour améliorer le code ou proposer de nouvelles fonctionnalités.

---

Plongez dans le chaos musical et laissez le réservoir guider vos découvertes sonores !
