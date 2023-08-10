# Previsão Forex LSTM

Os códigos apresentados são para a previsão de ativos no mercado forex, o symbol utilizado foi 'EURUSD', com timeframe de 1 Hora.
Na pasta "models" você encontrará ja o modelo salvo caso queira utilizar e fazer alguns testes.
Os datasets utilizados foram coletados do MetaTrader5 para o symbol e timeframe ja mencionados.
O projeto inteiro contem anotações e pensamentos que foram feitos no decorrer do projeto.

# Para rodar o projeto 
Em seu computador crie um arquivo "config.py" com as seguintes informações

USERNAME = SEU_USERNAME<br/>
PASSWORD = SUA_SENHA<br/>
SYMBOL = SYMBOL_DESEJADO<br/>
TIMEFRAME = SEU_TIMEFRAME<br/>
CANDLES = N_CANDLES_DESEJADAS<br/>

Libs:
- tensorflow 2.13.0
- pandas 2.0.3
- sklearn 1.3.0
- numpy 1.24.3
- matplotlib 3.7.2
- MetaTrader5 5.0.45
- pickle

## Competências aplicadas:
- Deep Learning
- Feature Engineering
