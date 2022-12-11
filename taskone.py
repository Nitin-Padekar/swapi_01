import requests
from utils.randgen import random_list


r1 = 1
r2 = 5
a = random_list()
l = []


for i in range(r1, r2+1):
    l.append(next(a))


if __name__=="__main__":
    print(__name__)
    print("from taskone.py")


home_url="https://swapi.dev"
relative_url="/api/people/{0}"


for j in l:
    absolute_url= home_url+relative_url.format(j)
    print(f"fetch data {absolute_url}")
    result= requests.get(absolute_url)
    data= result.json()
    print(data)
    print("----"*25)