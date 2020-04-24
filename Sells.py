import pandas as pd
from datetime import datetime
#Needed to use pandas read html for some reason
import ssl
ssl._create_default_https_context = ssl._create_unverified_context



def getSells():

    startTime = datetime.now()
    NumPages = 3
    finaldf = pd.DataFrame()
    transactiontypes = ['buying','sales']
    pagesscraped = 0
    for t in transactiontypes:
        for i in range(NumPages):
            url = f"https://www.insidearbitrage.com/insider-{t}/?desk=yes&pagenum={i+1}"
            df = pd.read_html(url)
            df = df[2]
            columns = df.iloc[0]
            df.columns = columns
            df.drop(df.columns[0],axis=1,inplace=True) #axis 1 chooses the columns
            df = df[1:]
            if t == 'buying':
                df['Type'] = "buy"
            else:
                df['Type'] = "sell"
            frames = [finaldf,df]
            finaldf = pd.concat(frames)
            pagesscraped+=1
            print(f'{pagesscraped} Pages Scraped : Total Elapsed time = {datetime.now() - startTime}')

    finaldf.to_csv('Insider.csv')
    print(f'CSV File Created - Execution Time: {datetime.now() - startTime}')



