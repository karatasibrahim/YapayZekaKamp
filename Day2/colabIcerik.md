``` python
#Colab erinde yapılan çalışma içeriği
!pip install ffmpeg
!pip install bar_chart_race
import pandas as pd 
df=pd.read_csv("corona_dat.csv")
df.head()
df2=df[["date","China","Italy","Brazil","Spain","US","United Kingdom","France","Turkey"]]

df.info()

#Çıktısı
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 112 entries, 0 to 111
Columns: 188 entries, date to Zimbabwe
dtypes: int64(187), object(1)
memory usage: 164.6+ KB

df2.set_index("date",inplace=True)
df2

df_total=df2.cumsum(axis=0) #Bir gun önce ve bir gun sonrayı toplar
df_total.head()

import bar_chart_race as bcr
bcr.bar_chart_race(df_total,filename="covid19.mp4",figsize=(8,5),title="İbrahim - Covid19 Verileri") #mp4 uzantılı dosya oluşturur

#Browser uzerinde goruntulememizi sağlar.
from IPython.display import HTML
from base64 import b64encode
mp4=open("covid19.mp4","rb").read()
data_url="data:video/mp4;base64,"+b64encode(mp4).decode()
HTML("""
<video width=400 controls>
  <source src="%s" type="video/mp4">
  </video> % data_url """)
```