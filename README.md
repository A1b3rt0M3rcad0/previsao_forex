# Previsão Forex com LSTM

## Coleta de Dados
Inicialmente, realizamos a etapa de coleta de dados. Onde poderíamos coletar os dados necessários? Utilizamos a API do MetaTrader5, amplamente utilizada para operações no mercado forex ou B3. Por que essa API? A API do MetaTrader5 nos permite coletar todos os dados necessários em tempo real. Portanto, se precisarmos testar o modelo com operações ao vivo, é mais simples de implementar, já que tudo está disponível em uma única API.

Para iniciar a coleta de dados, primeiro baixamos o MetaTrader5 e, em seguida, demos início à coleta. Você pode visualizar todo o processo de coleta de dados neste [notebook](https://github.com/A1b3rt0M3rcad0/previsao_forex/blob/main/Coletando%20dados.ipynb).

No mesmo notebook, também realizamos a etapa de Feature Engineering, onde criamos métricas que ajudarão em nossa previsão, como as médias móveis. O que são médias móveis? Basicamente, são as médias de um certo período N em nossos dados. Para calcular, pegamos o dado N em seu atributo X e calculamos a média de N até N-M, sendo M o número de períodos que desejamos calcular a média. Também foi criada uma métrica de variação percentual do dia anterior para o dia atual. O arquivo com as transformações realizadas está disponível [aqui](https://github.com/A1b3rt0M3rcad0/previsao_forex/blob/main/transform_data.py). Nossos dados ficaram assim:

![image](https://github.com/A1b3rt0M3rcad0/previsao_forex/assets/109180196/0cd2794d-59f1-4872-a9e5-f0ac9e8af4d7)

# Transformação dos Dados

Na próxima etapa, precisamos transformar os dados de maneira que nosso modelo LSTM consiga interpretar. Diferentemente de outros modelos de machine learning que aceitam vetores como entradas, o LSTM aceita matrizes de entradas, onde cada linha representa um período de tempo ou estado N e as colunas representam nossos atributos. O último registro dessa matriz representa o período N e cada registro N-1 representa um período no tempo ou estado anterior, e assim sucessivamente até o número de períodos desejados. Para isso, foi criada uma nova função que realiza esse processo para nós, disponível [aqui](https://github.com/A1b3rt0M3rcad0/previsao_forex/blob/main/transform_data.py).

# Criação e Avaliação do Modelo

Na criação de nossa rede neural, utilizamos 3 camadas ocultas, cada uma contendo 50 neurônios LSTM com ativação relu e uma camada Dense de saída com ativação linear, que nos retorna o valor de previsão dos nossos dados. Como função de perda, utilizamos MAE (Mean Absolute Error), e como otimizador, o Adam. Após a compilação do nosso modelo, obtivemos os seguintes parâmetros:

![image](https://github.com/A1b3rt0M3rcad0/previsao_forex/assets/109180196/5567f643-c8fa-4f0c-ba2f-286738d2eee6)

Dividindo nossos dados em treino e teste, e treinando nosso modelo, avaliamos as épocas obtendo o seguinte:

![image](https://github.com/A1b3rt0M3rcad0/previsao_forex/assets/109180196/1df38025-6af8-4fd2-b2a3-a650708602c6)

Acima, temos a medida de perda em azul e a medida de perda dos nossos dados de validação em laranja. Analisando o gráfico, observamos que nosso modelo não sofreu de overfitting nem underfitting. Também podemos observar que a partir da 5ª época, não houve mudança significativa no MAE, tanto nos dados de treino como nos dados de validação.

Agora, vamos avaliar nosso modelo nos dados de teste:

Realizando as previsões:

![image](https://github.com/A1b3rt0M3rcad0/previsao_forex/assets/109180196/9991bda0-55a3-4567-ba53-a37f4b8e816d)

Plotando um scatter plot entre nossas previsões e nossos valores reais, além de uma reta que indica onde os valores reais estão. Essa métrica gráfica é para avaliar o quanto nossos dados estão ajustados aos dados reais:

![image](https://github.com/A1b3rt0M3rcad0/previsao_forex/assets/109180196/27f789a4-751a-4c18-bba3-8bfa5119aef1)

Após avaliarmos o modelo, obtivemos os seguintes erros:

![image](https://github.com/A1b3rt0M3rcad0/previsao_forex/assets/109180196/fc6ec402-63a0-442d-833f-e2813682c7a7)

# Conclusão

Embora nossas previsões estejam muito próximas do real, ainda não são boas o suficiente para realizar operações em mercado real, visto que as variações são bem pequenas e nosso modelo não consegue identificar tão bem essas variações.
