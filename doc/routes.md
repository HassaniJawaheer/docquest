### Route `POST /upload`

* **Objectif** : Permettre à un utilisateur d’uploader un ou plusieurs fichiers dans un `workspace` donné (`mcq`, `summarize`, `user_rag`).
* **Use Case appelé** : `UploadDocuments`


### Route `POST /generate_mcq`

* **Objectif** : Générer un QCM à partir des documents uploadés dans le `workspace` `mcq`.
* **Use Case appelé** : `GenerateMCQ`


### Route `POST /summarize`

* **Objectif** : Générer un résumé à partir des documents du `workspace` `summarize`.
* **Use Case appelé** : `SummarizeDocuments`


### Route `POST /query/user_vector_db`

* **Objectif** : Interroger les documents personnels d’un utilisateur, dans le `workspace` `user_rag`.
* **Use Case appelé** : `QueryUserVectorDB`


### Route `POST /query/central_vector_db`

* **Objectif** : Interroger la base de connaissances publique (générale, non liée à une session).
* **Use Case appelé** : `QueryCentralVectorDB`

