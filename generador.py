from PIL import Image
from sample_metadata import metadata_template, attrbute
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import random
import math
import os
import copy

import json

BACKGROUNDS = "./img/background"
MAIN = "./img/main"
EXTRAS = "./img/extra"


arreglo_backgrounds = os.listdir(f"{BACKGROUNDS}/")
arreglo_mains = os.listdir(f"{MAIN}/")
arreglo_extras = os.listdir(f"{EXTRAS}/")

arre_weights_backgrounds = [1,1,1,1,1,1,1,1] # Hay 8
arre_weights_mains = [
    1,1,1,1,1,1,1,1,1,1,
    1,1,1,1,1,1,1,1,1,1,
    1,1,1,1,1,1,1,1,1,1,
    1,1,1,1,1,1,1,1,1,1,
    1,1,1,1] # Hay 44
arre_weights_extras = [1,1,1,1,1,1] #Hay 6

def genera_imagenes(num = 10, rng_seed = 1):
    random.seed(rng_seed)
    print(random.random())
    #aux = arreglo_backgrounds[math.floor((len(arreglo_backgrounds)*random.random()))]
    if not os.path.exists("./ret"):
        os.makedirs("./ret")
    if not os.path.exists("./metadata"):
        os.makedirs("./metadata")
    i = 0
    while i < num:
        noms_items = ""
        arre_items = []
        atr = copy.deepcopy(attrbute)
        atr['trait_type'] = "Background"
        #aux = arreglo_backgrounds[math.floor((len(arreglo_backgrounds)*random.random()))]
        aux = random.choices(arreglo_backgrounds, arre_weights_backgrounds,k=1)[0]
        bckgnd = Image.open(f"{BACKGROUNDS}/{aux}")
        aux4 = bckgnd.filename.split('/')[-1]
        atr['value'] = aux4[:len(aux4)-4]
        arre_items.append(atr)
        # pega main, todo misma proba 
        #aux2 = Image.open(f"{MAIN}/{arreglo_mains[math.floor((len(arreglo_mains)*random.random()))]}")
        aux2 = Image.open(f"{MAIN}/{random.choices(arreglo_mains, arre_weights_mains,k=1)[0]}")
        atr = copy.deepcopy(attrbute)
        atr['trait_type'] = "Main"
        aux5 = aux2.filename.split('/')[-1]
        atr['value'] = aux5[:len(aux5)-4]
        arre_items.append(atr)
        bckgnd.paste(aux2, mask=aux2)
        # pega extras, todo misma proba 
        proba = 1/2
        for ii in range(len(arreglo_extras)):
            if(probabilidad(proba)):
                img2 = Image.open(f"{EXTRAS}/{arreglo_extras[ii]}")
                atr = copy.deepcopy(attrbute)
                atr['trait_type'] = ii
                aux3 = img2.filename.split('/')[-1]
                atr['value'] = aux3[:len(aux3)-4]
                arre_items.append(atr)
                noms_items = noms_items + aux3[:len(aux3)-4] + "_"
                bckgnd.paste(img2, mask=img2)
        pte1 = bckgnd.filename.split('/')[-1]
        pte2 = aux2.filename.split('/')[-1]
        metadata_filename = f"./metadata/{pte1[:len(pte1)-4]}__{noms_items}_{pte2[:len(pte2)-4]}"
        metadata_filename = metadata_filename.replace(" ","-")
        if Path(metadata_filename).exists():
            print("Image already exists")
        else:
            collectible_metadata = metadata_template
            collectible_metadata["attributes"] = arre_items
            collectible_metadata["name"] = f"Collectible {i}"
            bckgnd.save(f"./ret/{metadata_filename[11:]}.png", "PNG")
            with open(f"{metadata_filename}.json", "w") as file:
                json.dump(collectible_metadata, file)
            i=i+1



def probabilidad(num):
    return num > random.random()

def histograma_rng(num=100,rng_seed=1,cant=8):
    arre = []
    random.seed(rng_seed)
    for i in range(num):
        arre.append(math.floor(random.random()*cant))
    plt.hist(arre, bins=cant)
    plt.show() 


def probas_por_objeto():
    arre_nombres = os.listdir(f"./metadata/")
    dict_mains = {}
    dict_extras = {}
    dict_bkgnds = {}
    for i in range(len(arre_nombres)):
        arre_nombres[i] = arre_nombres[i][0:len(arre_nombres[i])-4]
    for nom in arre_nombres:
        arre = nom.split("__")
        #Backgrounds
        if arre[0] in dict_bkgnds:
            dict_bkgnds[arre[0]] = dict_bkgnds[arre[0]] + 1
        else:
            dict_bkgnds[arre[0]] =  1
        #Mains
        if arre[-1][0] == "_":
            arre[-1] = arre[-1][1:]
        if arre[-1] in dict_mains:
            dict_mains[arre[-1]] = dict_mains[arre[-1]] + 1
        else:
            dict_mains[arre[-1]] =  1
        extras = arre[1].split("_")
        #Extras
        if extras[0] != "":
            for extra in extras:
                if extra in dict_extras:
                    dict_extras[extra] = dict_extras[extra] + 1
                else:
                    dict_extras[extra] =  1
    graph_dict(dict_mains)
    graph_dict(dict_extras)
    graph_dict(dict_bkgnds)
    
def graph_dict(dicti):
    myList = dicti.items()
    myList = sorted(myList) 
    x, y = zip(*myList) 
    plt.plot(x, y)
    plt.xticks(rotation=90, fontsize=6)
    plt.show()
    

#histograma_rng(num=10000,rng_seed=2,cant=44)
#genera_imagenes(num = 100, rng_seed=1)
#print(len(arreglo_backgrounds))
#print(len(arreglo_extras))
#print(len(arreglo_mains))
probas_por_objeto()

