# Modèle d'embedding choisi

## Nom du modèle
`intfloat/e5-small-v2`

## Caractéristiques principales

| Caractéristique      | Valeur                                |
|----------------------|----------------------------------------|
| Créateur             | [intfloat](https://huggingface.co/intfloat) |
| Architecture         | Encoder type DistilBERT (bi-encoder)  |
| Dimensions des vecteurs | 384                              |
| Taille du modèle      | ~110 Mo                               |
| Licence              | Apache 2.0 (usage libre)              |
| Pré-entraînement     | MS MARCO, Natural Questions, WebQ     |
| Type d'encodage      | Contraste requête/document (bi-encoder) |
| Préfixes recommandés | `query: ...` / `document: ...`        |
| Langue principale    | Anglais (compréhension FR acceptable) |

## Notes d'utilisation

Pour une qualité optimale, il est recommandé de préfixer les textes avant encodage :
- Requêtes : `query: [texte]`
- Documents : `document: [texte]`

