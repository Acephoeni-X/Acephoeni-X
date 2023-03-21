import requests, json, urllib.request

class generateGraph():
    __url = "https://api.github.com/users/Rishi-Sharma2002/repos"

    def getData(self, url = __url):
        # print(urllib.request.getproxies())
        data = requests.get(url).json()
        return data

    def getContributors(self):
        data = self.getData(self.__url)
        json_data = []
        for i in data:
            cont = self.getData(i['contributors_url'])
            summ = 0

            print(cont)
            # for j in range(len(cont)):
            #     summ += cont[j]['contributions']
            #     print(summ)

        #     json_ = {
        #                 "name": i['name'],
        #                 "contributions": summ
        #             }
        #     json_data.append(json_)
        # return json_data

graph = generateGraph()
myLang = graph.getContributors()
print(json.dumps(myLang, indent=4))

