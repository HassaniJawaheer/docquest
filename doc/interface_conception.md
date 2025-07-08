
# Conception de l’interface DocQuest avec Gradio

## Zone principale (chat)

* Grande zone centrale verticale qui affiche l’historique des messages de la conversation en cours.
* En bas de cette zone :

  * Zone de saisie permettant de taper une question libre lorsqu’un mode question est actif (VectorDB ou base centrale). La zone est désactivée lorsqu’un mode non interactif est sélectionné (Résumé ou QCM).
  * Sous la zone de saisie, quatre boutons horizontaux et centrés permettant de sélectionner le mode d’interaction :

    * Résumé
    * QCM
    * Question sur base vectorielle
    * Question sur base centrale
  * Ces boutons sont exclusifs, un seul peut être actif à la fois. Le mode actif détermine à la fois le type de traitement demandé et l’affectation des documents uploadés.
* Les réponses apparaissent toujours dans la même zone principale, avec un rendu adapté au mode :

  * Résumé sous forme de texte structuré en Markdown.
  * QCM sous forme d’un bloc interactif permettant de sélectionner des réponses et affichant la correction finale.
  * Réponses aux questions sous forme de texte structuré en Markdown.

## Panel latéral gauche

* Panel fixe positionné à gauche de l’écran.
* En haut du panel :

  * Liste des conversations existantes avec des titres reflétant le type d’interaction ou la première action effectuée dans la conversation. Par exemple :

    * Résumé 1, Résumé 2, etc. si la première action était un résumé.
    * QCM 1, QCM 2, etc. si la première action était un QCM.
    * La première question posée si la conversation débute par une question libre.
  * Bouton « New Conversation » permettant de vider la zone principale et d’initier une nouvelle conversation tout en maintenant la session démo active côté serveur.
* En bas du panel :

  * Zone de drag and drop permettant d’uploader un ou plusieurs documents. Les documents uploadés sont automatiquement associés au mode actif sélectionné.

## Comportements attendus

* Lorsqu’un mode nécessitant des documents (Résumé ou QCM) est activé mais qu’aucun document n’est présent, un message indique à l’utilisateur qu’il doit d’abord uploader des documents.
* Lorsqu’un document est uploadé, il est enregistré dans le workspace correspondant au mode sélectionné.
* En mode Résumé et QCM, la zone de saisie est désactivée puisque la génération est déclenchée automatiquement. En mode question, la zone de saisie reste active pour permettre la saisie libre.

## Style général

* Interface sobre et claire.
* Un logo DocQuest centré dans la zone principale lorsqu’aucune conversation n’est encore affichée.
* Tous les éléments sont agencés pour maximiser la lisibilité et la simplicité d’usage.
