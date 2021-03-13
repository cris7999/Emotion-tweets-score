import json
import pandas as pd
#TO DO METER PANDAS PARA TENER PALABRA -> VALOR DE CADA TWEET Y PODER HACER LA MEDIA Y SUMA FACIL 

def obtencion_sentimientos(archivo_sentimientos):
    sentimientos = open(archivo_sentimientos) 
    valores = {} 
    for linea in sentimientos: 
        termino, valor = linea.split("\t") 
        valores[termino] = int(valor)
    return valores

def valoracion_tweet(archivo_tweets , ruta_sentimientos):
     
    valores = obtencion_sentimientos(ruta_sentimientos)

    ristraTweets = []
    tweets = open(archivo_tweets)
    for tweet in tweets:
        if "text" in tweet:
            linea = json.loads(tweet)
            ristraTweets.append(linea["text"])

    for tweet in ristraTweets:
        df = pd.DataFrame()
        splitted_tweet = tweet.split()
        count=0
        ristraPalabras=[]
        palabras_sin_ponderacion=[]
        sentimiento_encontrado=False
        for word in splitted_tweet:
            
            if word in valores:
                
                valueSerie =pd.Series([word,valores[word]])
                dataFrameValue = pd.DataFrame([valueSerie])
                
                count=count + valores[word]
                ristraPalabras.append(word)
                sentimiento_encontrado=True
            else:
                valueSerie =pd.Series([word,int(0)])
                dataFrameValue = pd.DataFrame([valueSerie])
                
                palabras_sin_ponderacion.append(word)
            
            df = pd.concat([df,dataFrameValue])
            df[1] = df[1].mask(df[1]==0,df[1].mean())
            
        if sentimiento_encontrado:
            if len(palabras_sin_ponderacion)>0:
                valor_palabras = len(splitted_tweet)

            print("Tweet:",tweet)
            print(df)
            print("Analisis del tweet: puntuación final:",df[1].sum()," palabras reconocidas:",ristraPalabras,"\n")
        


print("Analisis de un conjunto de tweets basado en sentimientos.")
"""
print("Introduzca la ruta con el diccionario de los sentimientos ponderados")
ruta_sentimientos = input()
while(not os.path.isfile(ruta_sentimientos)):
    print("Ruta incorrecta o archivo incorrecto, introducela de nuevo");
    ruta_sentimientos = input()

print("Introduzca la ruta con el conjunto de Tweets")
ruta_tweets = input()
while(not os.path.isfile(ruta_tweets)):
    print("Ruta incorrecta o archivo incorrecto, introducela de nuevo");
    ruta_tweets = input()

print("Procesando tweets...")"""
valoracion_tweet("Tweets.txt","Sentimientos.txt")