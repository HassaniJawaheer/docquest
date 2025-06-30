# Modèle LLM choisi

## Nom du modèle principal

`groq/mixtral-8x7b` *(via Groq API)*

## Caractéristiques principales

| Caractéristique      | Valeur                                       |
| -------------------- | -------------------------------------------- |
| Fournisseur API      | [Groq](https://console.groq.com/)            |
| Modèle               | Mixtral-8x7B (Mixture of Experts) ou LLaMA 3 |
| Fenêtre contextuelle | Jusqu’à **131 072 tokens**                   |
| Tarification         | **Gratuit** (en bêta)                        |
| Vitesse              | Très élevée (inférence sur LPU Groq)         |
| Support JSON         | Oui (format structuré via prompt)            |
| Authentification     | Clé API (accès immédiat via console)         |
| Langues supportées   | Multilingue (FR très bien géré)              |
| Hébergement          | 100 % cloud (pas d’auto-hébergement)         |

## Notes d'utilisation

* Appels via endpoint Groq, par exemple :

```http
POST https://api.groq.com/openai/v1/chat/completions
Authorization: Bearer <clé>
```

* Compatible avec les prompts structurés (JSON, QCM, résumé, etc.)
* Aucun coût pour le moment, parfait pour démo ou usage itératif à forte charge
* Modèle recommandé pour **résumés longs**, **génération de QCM**, **réponses contextuelles**

---

## Modèle backup

`openrouter/<model>` *(via OpenRouter.ai)*

## Caractéristiques principales

| Caractéristique      | Valeur                                    |
| -------------------- | ----------------------------------------- |
| Fournisseur API      | [OpenRouter.ai](https://openrouter.ai/)   |
| Modèles disponibles  | Mistral, LLaMA, Claude, Gemma, etc.       |
| Fenêtre contextuelle | Jusqu’à **128 K tokens** (selon modèle)   |
| Tarification         | Mixte : certains modèles gratuits ou test |
| API unique           | Oui (une seule clé pour tous les modèles) |
| Authentification     | Clé API (connexion requise)               |
| Hébergement          | 100 % cloud, pas d’auto-hébergement       |

## Notes d'utilisation

* Utilisé comme **backup**, en cas d’indisponibilité de Groq ou pour tester d’autres architectures
* Certains modèles nécessitent une carte bancaire même pour test
* Utile pour benchmark croisé (QCM / résumé / style de réponse)
