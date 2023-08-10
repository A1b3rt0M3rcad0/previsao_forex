import pandas as pd

def transform_data(df, medias=[7, 14, 21, 200], drop_columns=['open', 'high', 'low', 'tick_volume', 'spread', 'real_volume', 'time']):
    ## Criando métricas
    # Cria a variação do dia anterior com o atual
    df['close%'] = df['close'].shift(1)/df['close']
    # Cria médias móveis
    for mm in medias:
        df[f'mm{mm}'] = df['close'].rolling(mm).mean()
    # cria target
    df['target'] = df['close'].shift(-1)
    # refaz index
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df.index = df['time']
    # Retira colunas indesejadas
    df = df.drop(columns=drop_columns)
    # retirando coluans nulas
    df = df.dropna()
    return df