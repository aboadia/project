
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# reading in data
parquet_file='/Users/lady/Desktop/fall2021_RA/aug_2.parquet'
df=pd.read_parquet(parquet_file,engine='auto')

#creating a new dataframe and attaching results
dar=pd.DataFrame()
dar['pxMid']=df['pxMid']
dar['bitstamp']=df['bitstamp']-df['pxMid']
dar['coinbase']=df['coinbase']-df['pxMid']
dar['gemini']=df['gemini']-df['pxMid']
dar['kraken']=df['kraken']-df['pxMid']
print(dar)

# plotting the data
plt.plot(dar.pxMid,dar.bitstamp,label='bitstamp')
plt.plot(dar.pxMid,dar.coinbase,label='coinbase')
plt.plot(dar.pxMid,dar.gemini,label='gemini')
plt.plot(dar.pxMid,dar.kraken,label='kraken')
plt.title('The difference between different exchanges and BTC-USD on Aug 4th')
plt.legend()
plt.show()

# creating summary statistics
dt=dar[['bitstamp','coinbase','gemini','kraken']].agg([np.mean,np.median,np.std,np.max,np.min,np.var])


# finding   q1,q2,q3, and q99 for bitstamp
s=dar.loc[:,'bitstamp'].values
p=np.quantile(s,[0.25,0.5,0.75,0.99],axis=0)


# finding   q1,q2,q3, and q99 for coinbase
y=dar.loc[:,'coinbase'].values
x=np.quantile(s,[0.25,0.5,0.75,0.99],axis=0)

# finding   q1,q2,q3, and q99 for gemini
f=dar.loc[:,'gemini'].values
r=np.quantile(s,[0.25,0.5,0.75,0.99],axis=0)

# finding   q1,q2,q3, and q99 for kraken
w=dar.loc[:,'kraken'].values
z=np.quantile(s,[0.25,0.5,0.75,0.99],axis=0)

