# Étapes à suivre (phase métier uniquement)

Lister les fonctionnalités prévues (futures routes)

| Fonction     | Description                                                    |
| ------------ | -------------------------------------------------------------- |
| upload       | Charger un fichier, extraire le texte, chunker                 |
| index        | Créer des embeddings à partir du texte, indexer dans FAISS     |
| ask          | Poser une question, récupérer du contexte, générer une réponse |
| summarize    | Générer un résumé d’un ou plusieurs documents                  |
| generate-qcm | Générer un QCM à partir d’un document                          |

## Identifier les entités métier

À créer dans `domain/models/` :

* `Document` : nom, texte brut, liste de chunks
* `Chunk` ou `ContextChunk` : morceau de texte avec position, score, etc.
* `Query` : question utilisateur
* `Answer` : réponse générée (texte + sources éventuelles)
* `Summary` : résumé généré
* `QCM` : structure d’un QCM (questions, bonnes réponses, distracteurs)

## Définir les services métier

À créer dans `domain/services/` :

| Service             | Rôle métier                                                  |
| ------------------- | ------------------------------------------------------------ |
| `DocumentProcessor` | Lire un fichier, extraire le texte, découper en chunks       |
| `Embedder`          | Générer des embeddings pour chaque chunk                     |
| `Retriever`         | Rechercher les chunks pertinents pour une question           |
| `LLMHandler`        | Générer une réponse à partir d’un contexte et d’une question |
| `Summarizer`        | Résumer un ou plusieurs documents                            |
| `QCMGenerator`      | Générer un QCM depuis un document                            |

Chaque service doit contenir uniquement la signature et la description de la méthode principale.

Le but de cette phase est de coder uniquement ce qui relève du métier. Pas de usecase, pas d’implémentation, pas de route.
