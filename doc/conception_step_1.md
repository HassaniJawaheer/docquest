
## Définition du périmètre minimal

### Ce qu’il faut absolument pour que la démo tienne debout

#### Importation de documents

* Un système simple de dépôt de fichiers (PDF, DOCX, TXT).
* Interface drag-and-drop dans Streamlit, ou un bouton "Uploader".
* Traitement immédiat côté backend pour lancer la vectorisation.
* Pas de prétraitement complexe, juste ce qu’il faut pour que ça fonctionne.

#### Indexation locale

* Index créé et stocké en local avec FAISS.
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
* Utiliser LangChain pour orchestrer les appels RAG, mais ce n’est pas indispensable pour la première version.

#### Modèle de langage

* Utilisation prioritaire d’une API gratuite (Mistral API, etc.) pour gagner du temps.
* Option possible de charger un petit modèle quantifié localement (GPU 8Go, donc modèle léger).
* La tokenisation est gérée automatiquement par l'API dans le cas d'utilisation d'une API sinon il faudra s'en occuper nous meme si on veut utiliser des modèle en local.
* La vectorisation doit se faire via un modèle ultra lèger (oublier Qwen, etc), pourrais partir sur du `sentence-transformers/paraphrase-MiniLM-L6-v2`.

### Ce qu’on pourrait ajouter si on a du temps

* Génération automatique de QCM à partir des documents : on utilisera des prompt, pas de finetuning.
* Résumé automatique des documents (extraction ou abstraction) : on utilisera des prompt.
* Extraction et affichage séparé des tableaux et images.
* Support OCR pour les fichiers scannés ou images.
* Système multi-utilisateur ou gestion de comptes (hors périmètre pour le moment).



