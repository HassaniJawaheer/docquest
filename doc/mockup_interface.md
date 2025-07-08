# Mockup textuel de l’interface DocQuest

## Écran général

* Organisation en deux colonnes principales :

  * Colonne gauche : panel latéral fixe
  * Colonne droite : zone principale (chat)

---

## Panel latéral gauche

**Contenu, du haut vers le bas :**

* Titre du panel : « Conversations »
* Liste des conversations existantes sous forme de boutons cliquables :

  * Résumé 1
  * QCM 1
  * Première question (texte tronqué si nécessaire)
  * Etc.
* Bouton « Nouvelle conversation » (reset de la zone principale, conserve la session)
* Séparateur visuel
* Titre secondaire : « Documents »
* Zone de drag and drop avec texte d’indication :

  * « Glissez-déposez vos documents ici »
  * Formats supportés : PDF, DOCX, TXT

---

## Zone principale (chat)

**Contenu initial (avant toute interaction) :**

* Logo DocQuest centré verticalement et horizontalement, avec un sous-texte éventuel « Prêt à interagir »

**Après sélection d’une conversation ou création d’une nouvelle :**

* Zone verticale affichant l’historique des échanges

  * Messages utilisateur alignés à droite
  * Réponses alignées à gauche
  * Mise en forme en fonction du type de réponse (texte markdown ou QCM interactif)

**Bas de la zone principale :**

* Zone de saisie (input) centrée horizontalement

  * Champ de texte large pour taper une question libre
  * Bouton envoyer à droite du champ
  * Champ désactivé si le mode actif est Résumé ou QCM

**Sous la zone de saisie :**

* Ligne de boutons horizontaux centrés pour le choix du mode

  * Bouton « Résumé »
  * Bouton « QCM »
  * Bouton « Question VectorDB »
  * Bouton « Question Base Centrale »
* Les boutons sont exclusifs (un seul actif à la fois), le bouton actif est visuellement mis en évidence

---

## Comportements dynamiques

* Si aucun document n’est présent et que l’utilisateur choisit Résumé ou QCM, un message s’affiche dans la zone principale pour inviter à uploader des documents.
* Les documents déposés dans la zone de drag and drop sont associés automatiquement au mode actif.
* Lors d’un QCM, un bloc interactif remplace l’habituel fil de chat pour présenter les questions et options de réponses.
* Le bouton « Nouvelle conversation » vide la zone principale et ajoute une nouvelle entrée dans la liste des conversations à gauche.
