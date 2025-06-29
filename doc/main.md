# À faire dans main.py
- Initialiser toutes les routes de l’API (inclure les nouvelles si besoin).

- Ajouter UpdateCentralVectorDB dans app.state pour qu’il soit accessible globalement.

- Ajouter FAISS (base vectorielle centrale) et Retriever central dans app.state.

- Créer une tâche de vérification périodique du corpus central  à l’aide d’APScheduler.
**Implémenter :**
```python
from apscheduler.schedulers.background import BackgroundScheduler
from server.usecases.update_central_vector_db import UpdateCentralVectorDB

scheduler = BackgroundScheduler()

def update_if_needed():
    usecase = app.state.update_usecase  # ou récupéré via dépendance
    usecase.run(corpus_path="/path/to/central_corpus")

scheduler.add_job(update_if_needed, 'interval', minutes=5)
scheduler.start()
```

- Penser à définir le chemin du corpus central (corpus_path) via .env.

- Ajouter une route simple pour vérifier que l’API est active.