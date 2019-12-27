import pandas as pd
from datetime import datetime

def getSells():
    startTime = datetime.now()
    df = pd.read_html("https://www.insidearbitrage.com/insider-sales/?desk=yes")
    df = df[2]
    columns = df.iloc[0]
    df.columns = columns
    df.drop(df.columns[0],axis=1,inplace=True) #axis 1 chooses the columns
    df = df[1:]
    df.to_csv('Insider.csv')
    print(f'CSV File Created - Execution Time: {datetime.now() - startTime}')


