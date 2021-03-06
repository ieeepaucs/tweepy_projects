# -*- coding: utf-8 -*-
import tweepy
#BURADA TWEEPY KUTUPHANESINI PROJEMIZE DAHIL EDIYORUZ
#MyStreamListener class'ını olusturuyoruz
class MyStreamListener(tweepy.StreamListener):
    #on_status methodunu override ediyoruz
    def on_status(self, status):
        #burada gelen veriyi print ediyoruz
        print(status.text)
    # on_error methodunu override ediyoruz
    def on_error(self, status_code):
        # burada veri dinlerken bir hata alırsak False donduruyoruz
        if status_code==420:
            return False
#KEY VE TOKENLARI DEGISKENLERE ATIYORUZ AUTHENTICATION ISLEMINDE KULLANIMA HAZIR HALE GETIRMIS OLUYORUZ
cons_key="CONSUMER_KEY"
sec_key="SECRET_KEY"
acc_token="ACCESS_TOKEN"
sec_acc_token="SECRET_ACCESS_TOKEN"

#tweepy'ın OAuthHandler methodu bizim api'ya baglanmamıza yardım edıyor
auth=tweepy.OAuthHandler(consumer_key=cons_key,consumer_secret=sec_key)
#auth objesıne access token degerımızı set ediyoruz(ayarlıyoruz)
auth.set_access_token(acc_token,sec_acc_token)
#api objesını olusturuyoruz
api=tweepy.API(auth)

#MyStreamListener class'ının objesını olusturuyoruz
myStreamListener=MyStreamListener()

#tweepy kutuphanesının StreamListener Class'ının Constructoruna API nesnesi ve bizim kendi olusturdugumuz class'ın objesını yolluyoruz
myStream=tweepy.Stream(auth=api.auth,listener=myStreamListener)
#myStream objesinin filter methoduna track(takip[filtreleyecegi] edecegi kelime) async=True kısmı ise programın thread kullanarak daha hızlı calısmasını saglıyor
myStream_tmp=myStream.filter(track=['#paucscoding'],async=True)

#mertongngl

