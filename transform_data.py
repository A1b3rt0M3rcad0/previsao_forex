import pandas as pd
import numpy as np

def transform_data(df, medias=[7, 14, 21, 200], drop_columns=['open', 'high', 'low', 'tick_volume', 'spread', 'real_volume', 'time']):
    ## Criando métricas
    # Cria a variação do dia anterior com o atual
    df['close%'] = df['close']/df['close'].shift(1)
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

def transform_lstm_data(X, y, step):
    ## Transforma as tabelas em array
    X = np.array(X)
    y = np.array(y)
    X_lstm = []
    y_lstm = []
    for i in range(step, X.shape[0]):
        X_lstm.append(X[i-step:i])
        y_lstm.append(y[i])
    X_lstm = np.array(X_lstm)
    y_lstm = np.array(y_lstm)
    X_lstm = np.reshape(X_lstm, (X_lstm.shape[0], step, X.shape[1]))
    y_lstm = np.reshape(y_lstm, (y_lstm.shape[0],))
    return X_lstm, y_lstm