[Yapay Zeka Kampı - Python Giriş]

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./src/Images/Project/nodered1.png">
  <source media="(prefers-color-scheme: light)" srcset="https://drive.google.com/file/d/1fMAAIkjt8tGszKtQL9ZJfvh3nyAzBOtQ/view?usp=sharing">
  <img alt="" src="https://user-images.githubusercontent.com/25423296/163456779-a8556205-d0a5-45e2-ac17-42d089e3c3f8.png">
</picture>


``` python

# ARİTMETİK OPERATÖRLER
#Toplama	 	
sonuc = x + y

#Çıkarma	 	
sonuc = x - y

#Çarpma	 	
sonuc = x * y

#Bölme	 	
sonuc = x / y	

#Mod Alma	 	
sonuc = y % x	0

#Tam Bölme	 	
sonuc = x // y	4

#Üs alma	 	
sonuc = 2 ** 3	8

#ATAMA OPERATÖRLERİ
x=20 y=5
#x = y                              #x += y		                     
x = y                               x = x + y
x= 5                                x= 25 

#x -= y	                            #x *= y	
x = x - y                           x = x * y
x= 15                               x= 100

#x /= y                             #x %= y 	
x = x / y                           x = x % y	
x= 4.0                              x= 0

#x **= y                            #x //= y	
x = x ** 2                          x = x // y	
x= 400                              x= 4

#KARŞILAŞTIRMA OPERATÖRLERİ
	
# ==	eşit mi?	
10 == 10  True
5 == 4	  False
 	
x = 5 y = 5

x == y  True

# !=	eşit değil mi?	
10 != 9     True
10 != 10	False

# >	Büyük mü ?	
10 > 5	True

# <	Küçük mü ?	
10 < 5	False

# >=	Büyük eşit mi ?	
5 >= 5	True

# <=	Küçük eşit mi ?	
5 <= 5	True

#MANTIKSAL OPERATÖRLER
# and operatörü	
(8 < 10) and (6 > 5) True

# or operatörü	
(5 == 5) or (6 == 5) True

# not	değil operatörü	
not(5 == 5)  False

import pandas as pd
#/ veri okuma paketini import ediyoruz
df=pd.read_csv("train.csv") #/ İçerisinde data olan dosyamız

df.head()
#İlk 5 veriyi getirir

df.tail()
#Son 5 veriyi getirir

df.sample(3) 
#Random 3 veriyi getirir

df.info()
#Her bir sutunda kaç veri ve hangi veri tipinde değerler olduğunu gösterir

df.isnull().sum()
#Boş olan sunların bilgisini gösterir

df["Sex"].value_counts()
#Cinsiyet bilgisinde yer alan sunlara karşılık gelen değerleri gösterir

df["Age"].hist()
#Yaş bilgilerinin histogram grafik uzerinde dağılımını gösterir

import seaborn as sns #/ Grafik paketiniimport ediyoruz

sns.pairplot(df, hue="Survived") #/ Hayatta kalanların dağılım grafiği

df[(df["Age"]<18) & (df["Pclass"]==3)] #/ Yaşı 18 den k ve sınıfı 3 olanlar

# ls komutu dosya bilgilerini aldığımız bilgisayar dosyalarını listeleyen linux komutudur.

df=pd.read_excel("sales-funnel.xlsx")
#xlsx uzantılı dosya açma

df.describe()
#Boş olmayan değerlerin sayısı. ortalama - mean değer döndurur.

pip install gtts
#text to speach özelliği kazandırdığımız paketi indiriyoruz

from gtts import gTTS
text="Welcome to our best data science class"
kayit=gTTS(text=text,lang="en", slow=False)
kayit.save("konusma.mp3")
#text içerisinde ki metni ingilizce dilinde okutarak konusma.mp3 adlı dosya formatında kayıt ediyoruz.
```