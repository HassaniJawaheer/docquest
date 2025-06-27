### Route `POST /upload`

* **Objectif** : Permettre à un utilisateur d’uploader un ou plusieurs fichiers dans un `workspace` donné (`qcm`, `summarize`, `personal_rag`).
* **Use Case appelé** : `UploadDocumentsUseCase`


### Route `POST /generate_qcm`

* **Objectif** : Générer un QCM à partir des documents uploadés dans le `workspace` `qcm`.
* **Use Case appelé** : `GenerateQCMUseCase`


### Route `POST /summarize`

* **Objectif** : Générer un résumé à partir des documents du `workspace` `summarize`.
* **Use Case appelé** : `SummarizeDocumentsUseCase`


### Route `POST /query/personal`

* **Objectif** : Interroger les documents personnels d’un utilisateur, dans le `workspace` `personal_rag`.
* **Use Case appelé** : `QueryPersonalDocumentsUseCase`


### Route `POST /query/core`

* **Objectif** : Interroger la base de connaissances publique (générale, non liée à une session).
* **Use Case appelé** : `QueryCoreKnowledgeUseCase`

