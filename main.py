import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import requests, json

class generateGraph():
    __url = "https://api.github.com/users/Rishi-Sharma2002/repos"

    def getData(self):
        data = requests.get(self.__url).json()
        myLang = {
            "Python":0,
            "C++":0,
            "JavaScript":0,
            "Vim script":0,
            "C":0,
            "Jupyter Notebook": 0
        }
        for i in data:
            for j in list(myLang.keys()):
                if i['language'] == j:
                    myLang[j]+=1
        
        return myLang

graph = generateGraph()
myLang = graph.getData()
lang = list(myLang.keys())
values = list(myLang.values())
print(graph.getData())
# plt.rcParams.update({
#     "lines.color": "white",
#     "patch.edgecolor": "white",
#     "text.color": "black",
#     "axes.facecolor": "white",
#     "axes.edgecolor": "lightgray",
#     "axes.labelcolor": "white",
#     "xtick.color": "white",
#     "ytick.color": "white",
#     "grid.color": "lightgray",
#     "figure.facecolor": "black",
#     "figure.edgecolor": "black",
#     "savefig.facecolor": "black",
#     "savefig.edgecolor": "black"
#     })

# plt.bar(lang, values)
# plt.show()