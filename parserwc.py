import requests, re
import matplotlib.pyplot as plt

# - Descargar contenido del sitio -
url="http://boomopolis.com/2018/04/17/pet-influencers/"
contenido=requests.get(url).text

ligas=re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+',contenido)

catalogo={'youtube':0,'facebook':0,'twitter':0,'instagram':0}

dicionario = [{'RedSocial':'youtube', 'Contador':0},
              {'RedSocial':'facebook', 'Contador':0},
              {'RedSocial':'twitter', 'Contador':0},
              {'RedSocial':'instagram', 'Contador':0}]

for liga in ligas:
    if re.search('youtube', liga):
        catalogo['youtube']+=1
        dicionario[0]['Contador']+=1
    elif re.search('facebook', liga):
        catalogo['facebook']+=1
        dicionario[1]['Contador']+=1
    elif re.search('twitter', liga):
        catalogo['twitter']+=1
        dicionario[2]['Contador']+=1
    elif re.search('instagram', liga):
        catalogo['instagram']+=1
        dicionario[3]['Contador']+=1

print("Redes Sociales: YouTube: {}, Facebook {}, Twitter {}, Instagram {}".format(dicionario[0]['Contador'],dicionario[1]['Contador'],dicionario[2]['Contador'],dicionario[3]['Contador']))

plt.bar(range(len(catalogo)), catalogo.values(), align='center')
plt.xticks(range(len(catalogo)), catalogo.keys())
plt.show()