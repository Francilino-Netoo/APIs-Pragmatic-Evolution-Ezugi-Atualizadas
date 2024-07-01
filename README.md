# DESCRIÇÃO
### - Essa API pega os resultados des 3 provedoras de games  Pragmatic Play, Evolution e Ezugi. Com elas você vai ter acesso a resultados de 217 games em tempo real, sendo 63 da Pragmatic, 99 da Evolution e 55 da Ezugi.

# COMO USAR A API
### - 1º Vai criar 3 Bots no Telegram usando o [BotFather](https://web.telegram.org/k/#@BotFather).

### - 2º Após criar os Bots, você vai mandar o @nome_do_seu_Bot para [Programador Java/Script](https://t.me/Python_Java_JavaScript), e vai falar qual API quer ativar, pois irei adicionar seu bot em um canal para ativar a API.

### - 3º Após isso, você vai usar o token dos seus Bots para ligar as APIs. Atenção user o LIGAR_API_PRAGMATIC.exe , LIGAR_API_EVOLUTION.exe e LIGAR_API_EZUGI.exe para ligar elas. O seus Bots não podem está em nenhum canal! A única funcionalidade dos Bots vai ser para ligar á API. O mesmo token do Bot não pode ser usado em 2 APIs ao mesmo tempo!

### - 4º Deixe os arquivos na mesma pasta correspondentes EX: API_PRAGMATIC e LIGAR_API_PRAGMATIC, na hora de ligar so vai precisar usar o LIGAR_API_PRAGMATIC, isso serve para as outras.

### - 5º Á API vai gerar arquivos Json com os resultados em tempo real dos games, em cada resultado tem um count é um número que sempre vai mudando quando um novo resultado sai. Isso serve para você identificar sempre que um resultado novo sai.

## OBSERVAÇÃO IMPORTANTE! 
### Á API da EVOLUTION vai pedir para você fazer login em uma casa de apostas. No caso tem que ter uma conta na [Vai de Bet](https://m.vaidebet.com/ptb)

# Windows
#### O Windowns pode tentar bloquear a execução dos arquivos .exe, geralmete você vai ter que da permição para o Windows executar esses arquivos. O Firewall ou outro dispositvo de segurança podem identificar arquivos .exe como ameaças, logo vai ta bloqueando eles.


## Ubuntu 24.04 
#### Se você esta usando uma máquina linux e quer executar o arquivo exe, não se preocupe, seguir os passos abaixo. Lembre-se de deixar os arquivos na mesma pasta!

```bash
sudo apt update

python LIGAR_API_NOMEAPI.py
```
