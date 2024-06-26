import json
import time
import os
import telebot

bot = telebot.TeleBot('TOKEN DE SEU BOT')

user_id = -100# ID DO SEU CANAL DO TELEGRAM AQUI

def check_and_create_file(filename, initial_value=0):
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            file.write(str(initial_value))

check_and_create_file("green.txt")
check_and_create_file("branco.txt")
check_and_create_file("red.txt")
check_and_create_file("consecutivas.txt")

def tempo():
    time.sleep(10)

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

lista = []
greenn = 0
brancoo = 0
redd = 0
assertividade = 0
cont_placar = 0
contador = 0
consecutivas = 0

def carregar_lista_resultados(results_id, result_data):
    global greenn, brancoo, redd, cont_placar, contador, consecutivas, vermelho1, azul1
    if 'results' in result_data:
        results = result_data['results'][0]
        
        
        color = results
        print(f"GAME: {results_id}, RESULTADO: {color}")
        
        
        if color:
            lista.append(color)
            if len(lista) > 10:
                del (lista[0:1])
            print(lista)
            

            def azul3():
                bot.edit_message_text(chat_id=user_id,text="<b>🤖 ROBÔ FOOTBALL STUDIO 🤖</b>\n<i>🟩 APOSTAR NO AZUL 🔵</i>\n<i>🟩 PROTEGER EMPATE 🟠</i>\n<i>🟩 BATEU A META? SE SIM 👇</i>\n<i>🟩 SAI DO MERCADO, VOLTE AMANHÃ</i>",message_id=int(azul1), parse_mode='HTML',disable_web_page_preview=True)

            def azul5():
                bot.edit_message_text(chat_id=user_id,text="<b>🤖 ROBÔ FOOTBALL STUDIO 🤖</b>\n<i>🟩 APOSTAR NO VERMELHO 🔴</i>\n<i>🟩 PROTEGER EMPATE 🟠</i>\n<i>🟩 BATEU A META? SE SIM 👇</i>\n<i>🟩 SAI DO MERCADO, VOLTE AMANHÃ</i>",message_id=int(vermelho1), parse_mode='HTML',disable_web_page_preview=True)
            
            def azul6():
                bot.edit_message_text(chat_id=user_id,text="<b>🤖 ROBÔ FOOTBALL STUDIO 🤖</b>\n<i>🟥 APOSTAR NO VERMELHO 🔴</i>\n<i>🟥 PROTEGER EMPATE 🟠</i>\n<i>🟥 RECUPERAÇÃO NO PRÓXIMO SINAL</i>\n<i>🟥 OU SAI DO MERCADO, VOLTE AMANHÃ</i>",message_id=int(vermelho1), parse_mode='HTML',disable_web_page_preview=True)

            def azul7():
                bot.edit_message_text(chat_id=user_id,text="<b><a href='https://instagram.com/programador_afobado?igshid=ZDdkNTZiNTM='>🤖 ROBÔ FOOTBALL STUDIO 🤖</a></b>\n<i>🟥 APOSTAR NO AZUL 🔵</i>\n<i>🟥 PROTEGER EMPATE 🟠</i>\n<i>🟥 RECUPERAÇÃO NO PRÓXIMO SINAL</i>\n<i>🟥 OU SAI DO MERCADO, VOLTE AMANHÃ</i>",message_id=int(azul1), parse_mode='HTML',disable_web_page_preview=True)
#################################################################################
            

            possivel_sinal = [['R','R'],['L','L'],['L','R','L'],['R','L','R']]
            for i in possivel_sinal:
                if lista == i:

                        msg = f'''<b>🤓💻❗❗❗ATENÇÃO❗❗❗💻🤓</b>\n\n<i>🤑ANALISANDO POSSIVÉL SINAL🤑</i>'''
                        message_ids = bot.send_message(user_id, msg,parse_mode='HTML').message_id
                        tempo()
                        bot.delete_message(user_id, message_ids, timeout=8000)
            
            apagar = [['Tie'], ['R', 'Tie'], ['L', 'Tie'],['L','L','Tie'],['L','R','Tie'],['R','L','Tie']]
            for i in apagar:
                if lista == i:
                    lista.clear()
            
            apagar = [['R','R','Tie'],['L','L','Tie'],['L','R','L','Tie'],['R','L','R','Tie']]
            for i in apagar:
                if lista == i:
                    msg = f'''<b>❗❗❗ NÃO CONFIRMOU ❗❗❗</b>'''
                    message_ids = bot.send_message(user_id, msg,parse_mode='HTML').message_id
                    lista.clear()
                    tempo()
                    bot.delete_message(user_id, message_ids, timeout=8000)
            
            apagar = [['R','R','L'],['L','L','R']]
            for i in apagar:
                if lista == i:
                    msg = f'''<b>❗❗❗ NÃO CONFIRMOU ❗❗❗</b>'''
                    message_ids = bot.send_message(user_id, msg,parse_mode='HTML').message_id
                    lista.clear()
                    tempo()
                    bot.delete_message(user_id, message_ids, timeout=8000)
            
            
            apagar = [['L','R','R'],['R','L','L']]
            for i in apagar:
                if lista == i:
                    del (lista[0:2])
            
        
                    
            #VERMELHO
            vermelho = [['L','L','L'],['L','R','L']]
            for i in vermelho:
                if lista == i:

                    msg = f'''<b>🤖 ROBÔ FOOTBALL STUDIO 🤖</b>\n<i>➡ APOSTAR NO VERMELHO 🔴</i>\n<i>➡ PROTEGER EMPATE 🟠</i>\n<i>➡ REALIZAR 2 GALES</i>\n➡<a href='https://blaze.com/pt/games/football-studio/fun'><b>♣♦ Football Studio ♠♥</b></a>'''
                    vermelho1 = bot.send_message(user_id, msg, parse_mode='HTML',disable_web_page_preview=True).message_id

            gale1_v = [['L','L','L','R'],['L','R','L','R']]
            for i in gale1_v:
                if lista == i:
                    msg = f'''<b>❗❗❗ 1º GALE ❗❗❗</b>'''
                    message_ids = bot.send_message(user_id, msg,parse_mode='HTML').message_id
                    tempo()
                    bot.delete_message(user_id, message_ids, timeout=8000)
        


            gale2_v = [['L','L','L','R','R'],['L','R','L','R','R']]
            for i in gale2_v:
                if lista == i:
                    msg = f'''<b>❗❗❗ 2º GALE ❗❗❗</b>'''
                    message_ids = bot.send_message(user_id, msg,parse_mode='HTML').message_id
                    tempo()
                    bot.delete_message(user_id, message_ids, timeout=8000)



            green1_v = [['L','L','L','L'],['L','R','L','L']]
            for i in green1_v:
                if lista == i:
                    greenn = 1
                    consecutivas += 1
                    cont_placar += 1
                    azul5()
                    msg = f'''<b>🍀 GREEN SEM GALE 🍀</b>'''
                    bot.send_message(user_id, msg, parse_mode='HTML',reply_to_message_id = int(vermelho1))
                    del (lista[0:2])



            green2_v = [['L','L','L','R','L'],['L','R','L','R','L']]
            for i in green2_v:
                if lista == i:
                    greenn = 1
                    consecutivas += 1
                    cont_placar += 1
                    azul5()
                    msg = f'''<b>✅ GREEN GALE 1 ✅</b>'''
                    bot.send_message(user_id, msg, parse_mode='HTML', reply_to_message_id = int(vermelho1))
                    del (lista[0:3])


            green3_v = [['L','L','L','R','R','L'],['L','R','L','R','R','L']]
            for i in green3_v:
                if lista == i:
                    greenn = 1
                    consecutivas += 1
                    cont_placar += 1
                    azul5()
                    msg = f'''<b>✅✅ GREEN GALE 2 ✅✅</b>'''
                    bot.send_message(user_id, msg, parse_mode='HTML', reply_to_message_id = int(vermelho1))
                    del (lista[0:4])
                        

            empate_v = [['L','L','L','Tie'],['L','R','L','Tie'],['L','L','L','R','Tie'],['L','R','L','R','Tie'],['L','L','L','R','R','Tie'],['L','R','L','R','R','Tie']]
            for i in empate_v:
                if lista == i:
                    greenn = 1
                    consecutivas += 1
                    brancoo = 1
                    cont_placar += 1
                    azul5()
                    msg = f'''<b>🟠GREEN NO EMPATE🟠</b>'''
                    bot.send_message(user_id, msg, parse_mode='HTML',reply_to_message_id=int(vermelho1))
                    lista.clear()


            red = [['L','L','L','R','R','R'],['L','R','L','R','R','R']]
            for i in red:
                if lista == i:

                    consec = 0
                    consecutivas = 0
                    if consec == 0:
                        with open("consecutivas.txt", "w") as arquivo:
                            arquivo.write(str(consec))
                            
                    redd = 1
                    cont_placar += 1
                    azul6()
                    msg = f'''<b>❌❌💔 RED 💔❌❌</b>\n\n<i>😮‍💨RESPIRA FUNDO😮‍💨</i>\n\n<i>🤗ESPERE O PRÓXIMO SINAL🤗</i>\n\n<i>❗NÃO FIQUE DESESPERADO❗</i>'''
                    bot.send_message(user_id, msg, parse_mode='HTML',reply_to_message_id=int(vermelho1))
                    lista.clear()

            #AZUL
            azul = [['R','R','R'],['R','L','R']]
            for i in azul:
                if lista == i:

                    msg = f'''<b>🤖 ROBÔ FOOTBALL STUDIO 🤖</b>\n<i>➡ APOSTAR NO AZUL 🔵</i>\n<i>➡ PROTEGER EMPATE 🟠</i>\n<i>➡ REALIZAR 2 GALES</i>\n➡<a href='https://blaze.com/pt/games/football-studio/fun'><b>♣♦ Football Studio ♠♥</b></a>'''
                    azul1 = bot.send_message(user_id, msg, parse_mode='HTML',disable_web_page_preview=True).message_id


            gale1_a = [['R','R','R','L'],['R','L','R','L']]
            for i in gale1_a:
                if lista == i:
                    
                    msg = f'''<b>❗❗❗ 1º GALE ❗❗❗</b>'''
                    message_ids = bot.send_message(user_id, msg,parse_mode='HTML').message_id
                    tempo()
                    bot.delete_message(user_id, message_ids, timeout=8000)
            
        

            gale2_a = [['R','R','R','L','L'],['R','L','R','L','L']]
            for i in gale2_a:
                if lista == i:

                    msg = f'''<b>❗❗❗ 2º GALE ❗❗❗</b>'''
                    message_ids = bot.send_message(user_id, msg,parse_mode='HTML').message_id
                    tempo()
                    bot.delete_message(user_id, message_ids, timeout=8000)
            
            

            green1_a = [['R','R','R','R'],['R','L','R','R']]
            for i in green1_a:
                if lista == i:
                    greenn = 1
                    consecutivas += 1
                    cont_placar += 1
                    azul3()
                    msg = f'''<b>🍀 GREEN SEM GALE 🍀</b>'''
                    bot.send_message(user_id, msg, parse_mode='HTML', reply_to_message_id = int(azul1))
                    del (lista[0:2])



            green2_a = [['R','R','R','L','R'],['R','L','R','L','R']]
            for i in green2_a:
                if lista == i:
                    greenn = 1
                    consecutivas += 1
                    cont_placar += 1
                    azul3()
                    msg = f'''<b>✅ GREEN GALE 1 ✅</b>'''
                    bot.send_message(user_id, msg, parse_mode='HTML', reply_to_message_id = int(azul1))
                    del (lista[0:3])



            green3_a = [['R','R','R','L','L','R'],['R','L','R','L','L','R']]
            for i in green3_a:
                if lista == i:
                    greenn = 1
                    consecutivas += 1
                    cont_placar += 1
                    azul3()
                    msg = f'''<b>✅✅ GREEN GALE 2 ✅✅</b>'''
                    bot.send_message(user_id, msg, parse_mode='HTML', reply_to_message_id = int(azul1))
                    del (lista[0:4])



            empate_a = [['R','R','R','Tie'],['R','L','R','Tie'],['R','R','R','L','Tie'],['R','L','R','L','Tie'],['R','R','R','L','L','Tie'],['R','L','R','L','L','Tie']]
            for i in empate_a:
                if lista == i:
                    greenn = 1
                    consecutivas += 1
                    brancoo = 1
                    cont_placar += 1
                    azul3()
                    msg = f'''<b>🟠GREEN NO EMPATE🟠</b>'''
                    bot.send_message(user_id, msg, parse_mode='HTML', reply_to_message_id = int(azul1))
                    lista.clear()


            red = [['R','R','R','L','L','L'],['R','L','R','L','L','L']]
            for i in red:
                if lista == i:

                    consec = 0
                    consecutivas = 0
                    if consec == 0:
                        with open("consecutivas.txt", "w") as arquivo:
                            arquivo.write(str(consec))

                    redd = 1
                    cont_placar += 1
                    azul7()
                    msg = f'''<b>❌❌💔 RED 💔❌❌</b>\n\n<i>😮‍💨RESPIRA FUNDO😮‍💨</i>\n\n<i>🤗ESPERE O PRÓXIMO SINAL🤗</i>\n\n<i>❗NÃO FIQUE DESESPERADO❗</i>'''
                    bot.send_message(user_id, msg, parse_mode='HTML', reply_to_message_id = int(azul1))
                    lista.clear()




            if cont_placar > 0:

                with open("green.txt", "r+") as arquivo:
                    gren = int(arquivo.read())

                with open("branco.txt", "r+") as arquivo:
                    branca = int(arquivo.read())

                with open("red.txt", "r+") as arquivo:
                    red = int(arquivo.read())
                
                with open("consecutivas.txt", "r+") as arquivo:
                    consec = int(arquivo.read())
                
                
                g = greenn + brancoo + branca + gren
                t = greenn + brancoo + redd + red + gren + branca
                asserti = (g / t) * 100

                asserti = f'{asserti:.2f}'
                msg = f'''<b>📋🖊️ RELATÓRIO ATUAL 📋🖊️</b>\n<i>✅GREEN✅ 👉</i> {greenn + gren}\n<i>🟧EMPATE🟧 👉</i> {branca+brancoo}\n💔 RED 💔 👉 {red+redd}\n\n<b>📈Consecutivas📈 👉</b> {consecutivas + consec}\n\n<i>🎯Assertividade🎯 👉</i> {asserti}%'''
                bot.send_message(user_id, msg, parse_mode='HTML')


                valor = gren+greenn
                valor2 = branca+brancoo
                valor3 = red+redd
                valor4 = consecutivas + consec
                with open("green.txt", "w+") as arquivo:
                    arquivo.write(str(valor))

                with open("branco.txt", "w+") as arquivo:
                    arquivo.write(str(valor2))

                with open("red.txt", "w+") as arquivo:
                    arquivo.write(str(valor3))
                
                with open("consecutivas.txt", "w+") as arquivo:
                    arquivo.write(str(valor4))
                
                greenn = 0
                brancoo = 0
                redd = 0
                consecutivas = 0

                cont_placar = 0
                
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
        game_id = input("Enter the name of the game ID you want to monitor: ")
        config_data["game_id"] = game_id
        escrever_json(config_filename, config_data)
    
    return game_id

def main():
    filename = "./BacBo_FootbalStudio_Evolution_results.json"
    prever_resultados = {}
    
    game_id = get_or_set_game_id()

    while True:
        current_results = load_prever_resultados(filename)
        prever_resultados = carregar_resultados(current_results, prever_resultados, game_id)
        time.sleep(2)

if __name__ == "__main__":
    main()
