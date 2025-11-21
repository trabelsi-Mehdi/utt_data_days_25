import requests
import json

# URL du serveur MCP (à adapter selon votre configuration)
MCP_SERVER_URL = "http://localhost:5000"

# 1. Récupérer la liste des outils disponibles
def get_available_tools():
    response = requests.get(f"{MCP_SERVER_URL}/tools")
    if response.status_code == 200:
        return response.json()
    else:
        return f"Erreur: {response.status_code}"

# 2. Exécuter un outil
def run_tool(tool_name, parameters={}):
    data = {
        "name": tool_name,
        "parameters": parameters
    }
    response = requests.post(f"{MCP_SERVER_URL}/run_tool", json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Erreur: {response.status_code}"

# Exemples d'utilisation (à exécuter une fois le serveur lancé)
def test_mcp_client():
    print("Outils disponibles:")
    tools = get_available_tools()
    print(json.dumps(tools, indent=2))

    print("\\nHeure actuelle:")
    time_result = run_tool("get_current_time")
    print(time_result)

    print("\\nCalcul mathématique:")
    calc_result = run_tool("calculate", {"expression": "42 * 3 - 15"})
    print(calc_result)

    print("\\nMétéo à Paris:")
    weather_result = run_tool("get_weather", {"city": "Paris"})
    print(weather_result)

# Décommentez pour tester une fois le serveur lancé
test_mcp_client()