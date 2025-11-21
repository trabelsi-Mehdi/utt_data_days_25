from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

# Définition des outils disponibles
TOOLS = [
    {
        "name": "get_current_time",
        "description": "Obtient l'heure et la date actuelles",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "calculate",
        "description": "Effectue un calcul mathématique",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "L'expression mathématique à évaluer"
                }
            },
            "required": ["expression"]
        }
    },
    {
        "name": "get_weather",
        "description": "Obtient la météo pour une ville donnée",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "Le nom de la ville"
                }
            },
            "required": ["city"]
        }
    }
]


@app.route('/tools', methods=['GET'])
def get_tools():
    return jsonify(TOOLS)


@app.route('/run_tool', methods=['POST'])
def run_tool():
    data = request.json
    tool_name = data.get('name')
    parameters = data.get('parameters', {})

    if tool_name == "get_current_time":
        result = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return jsonify({"result": result})

    elif tool_name == "calculate":
        expression = parameters.get('expression')
        try:
            # Attention: eval peut être dangereux en production
            result = eval(expression)
            return jsonify({"result": f"Le résultat de {expression} est {result}"})
        except Exception as e:
            return jsonify({"error": f"Erreur de calcul: {str(e)}"}), 400

    elif tool_name == "get_weather":
        city = parameters.get('city')
        # Dans un cas réel, vous utiliseriez une API météo
        # Ici, nous simulons une réponse
        weather_data = {
            "Paris": "21°C, Ensoleillé",
            "New York": "18°C, Nuageux",
            "Tokyo": "25°C, Pluie légère",
            "London": "15°C, Brouillard"
        }
        result = weather_data.get(city, f"Données météo non disponibles pour {city}")
        return jsonify({"result": result})

    return jsonify({"error": "Outil non reconnu"}), 400


if __name__ == '__main__':
    app.run(debug=True, port=5000)