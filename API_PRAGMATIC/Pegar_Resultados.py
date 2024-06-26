import json
import time

# AQUI É SO UM EXEMPLO SIMPLES E VOCÊS PODEM MODIFICAR DO JEITO QUE ACHAREM MELHOR


def ler_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
        return dados
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def escrever_json(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

def carregar_lista_resultados(results_id, result_data):
    
    if 'result' in result_data:
        results = result_data['result']
        banker = result_data['banker']
        palyer = result_data['player']
        print(f"GAME: {results_id}, RESULTADO: {results}, BANKER: {banker} | PLAYER: {palyer}")
    else:
        pass

def load_prever_resultados(filename):
    return ler_json(filename)

conta = 0
def carregar_resultados(current_results, prever_resultados, game_id):
    global conta
    if game_id in current_results:
        result_data = current_results[game_id]
        if game_id in prever_resultados:
            prever_resultados_hora = prever_resultados[game_id]
            if result_data['count'] != prever_resultados_hora['count']:
                carregar_lista_resultados(game_id, result_data)
                prever_resultados[game_id] = result_data
        else:
            carregar_lista_resultados(game_id, result_data)
            prever_resultados[game_id] = result_data
    else:
        pass
    return prever_resultados

def get_or_set_game_id():
    config_filename = "config.json"
    config_data = ler_json(config_filename)
    
    if "game_id" in config_data:
        game_id = config_data["game_id"]
    else:
        game_id = input("Entre com o ID do game que voce quer pegar: ")
        config_data["game_id"] = game_id
        escrever_json(config_filename, config_data)
    
    return game_id

def main():
    filename = "Bacara_Pragmatic_results.json"
    prever_resultados = {}
    
    game_id = get_or_set_game_id()

    while True:
        current_results = load_prever_resultados(filename)
        prever_resultados = carregar_resultados(current_results, prever_resultados, game_id)
        time.sleep(2)

if __name__ == "__main__":
    main()
