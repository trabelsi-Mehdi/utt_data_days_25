# Atelier IA Agentique avec MCP

Ce projet contient un ensemble de trois notebooks Jupyter qui vous guident à travers la création et l'utilisation d'agents IA avec le Model Context Protocol (MCP).

## Contenu

### Notebook 1: Introduction aux LLMs et SLMs

Ce premier notebook vous permet de prendre en main les modèles de langage locaux (SLM) en utilisant LiquidAI. Vous apprendrez à:
- Installer et configurer LiquidAI
- Charger et utiliser un modèle de langage local
- Interagir avec le modèle via une API
- Comprendre les paramètres d'inférence

### Notebook 2: IA Agentique et Model Context Protocol (MCP)

Le deuxième notebook explore les concepts fondamentaux de l'IA agentique et du Model Context Protocol. Vous apprendrez à:
- Comprendre ce qu'est un agent IA et son architecture
- Explorer le Model Context Protocol (MCP)
- Créer un serveur MCP simple avec Flask
- Développer des outils MCP personnalisés
- Intégrer un modèle de langage avec des outils MCP

### Notebook 3: Applications Concrètes avec Serveurs MCP

Le troisième notebook vous montre créer une application concrète. Vous apprendrez à:
- Créer un serveur MCP pour Google Agenda
- Configurer l'authentification OAuth pour les API Google
- Implémenter des outils pour gérer un agenda
- Développer un assistant de planification intelligent
- Créer une interface interactive pour votre agent

## Prérequis

- Python 3.8 ou supérieur
- Jupyter Notebook ou JupyterLab

## Installation

1. Clonez ce dépôt:
   ```
   git clone https://github.com/atrefab/utt_data_days_25.git
   cd utt_data_days_25
   ```

2. Installez les dépendances:
   ```
   setup.bat
   ```

3. Lancez Jupyter:
   ```
   start_jupyter.bat
   ```

4. Lancez le server local:
   ```
   start_liquid.bat
   ```
   
5. Ouvrez les notebooks dans l'ordre (01, 02, 03) et suivez les instructions.

## Structure du projet

```
utt_data_days_25/
├── 01_introduction_llm.ipynb
├── 02_introduction_mcp.ipynb
├── 03_applications_MCP_Google_Agenda.ipynb
└── README.md
```

---

Créé dans le cadre d'un atelier sur l'IA agentique et le Model Context Protocol.

© 2023 Dr ATREVI D. Fabrice - atrevifabrice@gmail.com - Tous droits réservés.