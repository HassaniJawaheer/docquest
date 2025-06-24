
## Définition du périmètre minimal (MVP)

### Ce qu’il faut absolument pour que la démo tienne debout

#### Importation de documents

* Un système simple de dépôt de fichiers (PDF, DOCX, TXT).
* Interface drag-and-drop dans Streamlit, ou un bouton "Uploader".
* Traitement immédiat côté backend pour lancer la vectorisation.
* Pas de prétraitement complexe, juste ce qu’il faut pour que ça fonctionne.

#### Indexation locale

* Index créé et stocké en local avec FAISS ou ChromaDB.
* Pas de base de données distante.
* Embeddings générés localement ou via une API gratuite si disponible.
* Par défaut, on part sur du local, sauf blocage technique.

#### Interface conversationnelle

* Interface de chat dans Streamlit.
* L’utilisateur pose des questions, les réponses s’affichent directement.
* L’historique des messages est visible dans la même interface.
* Pas de système d’authentification complet. Juste un token généré au chargement et stocké en sessionStorage. Cela suffit pour une session temporaire.

#### Backend simple et propre

* FastAPI avec trois routes principales :

  * `/upload` pour envoyer les fichiers
  * `/create_vector_db` pour lancer l’indexation
  * `/generate` pour envoyer une question et recevoir une réponse
* Possibilité d’utiliser LangChain pour orchestrer les appels RAG, mais ce n’est pas indispensable pour la première version.

#### Modèle de langage

* Utilisation prioritaire d’une API gratuite (OpenRouter, Mistral API, etc.) pour gagner du temps.
* Option possible de charger un petit modèle quantifié localement (GPU 8Go, donc modèle léger).
* La tokenisation est gérée automatiquement par la librairie ou le modèle, pas besoin de la coder soi-même.

---

### Ce qu’on pourrait ajouter si on a du temps

* Génération automatique de QCM à partir des documents.
* Résumé automatique des documents (extraction ou abstraction).
* Extraction et affichage séparé des tableaux et images.
* Support OCR pour les fichiers scannés ou images.
* Système multi-utilisateur ou gestion de comptes (hors périmètre pour le moment).

---

### À propos du local vs cloud

* L’application doit pouvoir tourner entièrement en local (backend, frontend, base vectorielle).
* L’usage d’APIs externes gratuites est autorisé si cela permet d’éviter des implémentations longues.
* Pas d’utilisation de bases de données cloud ou d’outils payants, sauf solution gratuite et fiable.
* Pas besoin de Docker pour la première démo, mais on peut le prévoir pour les tests si nécessaire.


