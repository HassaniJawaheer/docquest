# Note sur comment utiliser Gradio

Gradio est une bibliothèque Python open source qui permet de créer rapidement des interfaces web interactives pour vos modèles et fonctions Python.

## Concepts de base

### Interface

* La classe **`Interface`** est la manière la plus simple de construire une interface.
* Vous lui passez une fonction Python, une liste de composants d’entrée (`Textbox`, `Image`, etc.) et de sortie, et Gradio génère automatiquement la page.

Exemple :

```python
import gradio as gr

def greet(name):
    return f"Hello {name}!"

iface = gr.Interface(fn=greet, inputs=gr.Textbox(), outputs=gr.Textbox())
iface.launch()
```

### Blocks

* **`Blocks`** est un système plus flexible et modulaire pour créer des interfaces complexes.
* On utilise un `with` contextuel pour composer des éléments (rows, columns, composants) et définir explicitement les interactions.
* Idéal quand votre UI est plus qu’une simple fonction entrée/sortie.

### Row et Column

* Utilisés pour organiser les composants visuellement en lignes (`Row`) et colonnes (`Column`) dans un layout flexible.

### State

* Objet pour stocker des variables persistantes pendant une session utilisateur.
  (Exemple : garder un historique de chat, compteur…)


## Interface vs. Blocks : quand utiliser ?

| Critère                        | Interface             | Blocks                              |
| ------------------------------ | --------------------- | ----------------------------------- |
| Simplicité                     | ✅ Très simple         | ❌ plus verbeux                      |
| Complexité UI                  | ❌ limité              | ✅ layouts complexes                 |
| Contrôle précis sur la logique | ❌                     | ✅                                   |
| Cas d’usage                    | démos simples, protos | apps multi-étapes, chatbots évolués |

Utilisez `Interface` pour une démonstration rapide et `Blocks` dès que vous avez plus d’un flux ou des dépendances complexes entre composants.


## Principaux composants

Gradio fournit de nombreux composants prêts à l’emploi pour affichage et interaction :

| Composant                 | Rôle                                 |
| ------------------------- | ------------------------------------ |
| **Textbox**               | Champ texte (entrée ou sortie)       |
| **Image**                 | Entrée ou sortie d’image             |
| **File** / **FileUpload** | Téléverser ou télécharger un fichier |
| **Chatbot**               | Widget conversationnel               |
| **Dropdown**              | Sélecteur dans une liste             |
| **Slider**                | Valeur numérique sur une échelle     |
| **Checkbox**, **Radio**   | Sélections multiples ou uniques      |
| **Gallery**               | Afficher des images en grille        |
| **Dataframe**             | Tableau interactif                   |

Ces composants sont combinables et peuvent être chaînés.


## Connecter des callbacks Python

Avec `Blocks`, vous définissez explicitement quelles actions utilisateur déclenchent quelles fonctions Python grâce à `.click()`, `.change()`, `.submit()`, etc.

Exemple :

```python
def reply(message, history):
    history = history + [(message, f"Echo: {message}")]
    return "", history

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    state = gr.State([])

    msg.submit(reply, [msg, state], [msg, chatbot])

demo.launch()
```

Ici :

* La soumission du `Textbox` appelle `reply()`
* Elle met à jour le chatbot et efface la textbox.

##  Bonnes pratiques pour organiser votre code

* **Séparer logique et interface** : définissez vos fonctions métiers dans un module séparé.
* **Utiliser Blocks pour les projets sérieux** : plus maintenable et flexible.
* **Nommer clairement vos composants** pour éviter les erreurs.
* **Modulariser** : créez des fonctions pour construire des sous-interfaces réutilisables.
* **Documenter vos callbacks** : clarifiez ce qui est attendu en entrée et en sortie.
* **Tester hors Gradio d’abord** : assurez-vous que vos fonctions Python fonctionnent seules.
