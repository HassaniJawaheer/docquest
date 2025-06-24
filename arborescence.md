docquest_backend/
├── domain/
│   ├── models/
│   │   ├── document.py          # Représentation métier d’un document (titre, texte, chunks, etc.)
│   │   ├── query.py             # Objet Question utilisateur (texte, options...)
│   │   ├── context_chunk.py     # Chunks extraits et scorés pour la génération
│   │   └── summary.py           # Représentation métier d’un résumé ou d’un QCM
│
│   └── services/
│       ├── document_processor.py   # Interface métier pour traitement et chunking des documents
│       ├── embedder.py            # Interface métier pour générer des embeddings et indexer
│       ├── retriever.py           # Interface métier pour récupérer les chunks les plus pertinents
│       ├── llm_handler.py         # Interface métier pour interagir avec le LLM (générer réponse, résumé, QCM)
│       └── summarizer.py          # Interface métier pour créer des synthèses/QCM à partir de documents

├── usecases/
│   ├── upload_document.py        # Cas d’usage : importer et prétraiter un document
│   ├── index_document.py         # Cas d’usage : indexer un document dans la base vectorielle
│   ├── ask_question.py           # Cas d’usage : traiter une question et générer une réponse
│   ├── generate_summary.py       # Cas d’usage : créer un résumé depuis un document indexé
│   └── generate_qcm.py           # Cas d’usage : générer un QCM depuis un document indexé

├── interfaces/
│   ├── routes/
│   │   ├── upload.py             # Route POST /upload
│   │   ├── index.py              # Route POST /index
│   │   ├── ask.py                # Route POST /ask
│   │   ├── summarize.py          # Route POST /summarize
│   │   └── qcm.py                # Route POST /generate-qcm
│
│   └── repositories/
│       ├── document_repository.py  # Abstraction pour accès aux documents (même si stockage temporaire)
│       ├── vector_store.py         # Abstraction pour accès à la base FAISS
│       └── llm_gateway.py          # Abstraction pour appeler le LLM (HF, OpenAI, etc.)
