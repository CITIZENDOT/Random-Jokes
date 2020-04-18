import requests
import json
url = "https://sv443.net/jokeapi/v2/joke/"
print("Which Category of jokes you like: ")
print("The available categories are: ")
print("1. Any")
print("2. Miscellaneous")
print("3. Programming")
print("4. Dark")
dic = {1: "any", 2: "Miscellaneous", 3: "Programming", 4: "Dark"}
print("Choose index of the category: ")
n = int(input())
n = 3
if 1<=n<=4:
    error = False
else:
    error = True
if error:
    while error:
        print("You had choosen the wrong Category, Choose it again")
        print("Which Category of jokes you like: ")
        print("The available categories are: ")
        print("1. Any")
        print("2. Miscellaneous")
        print("3. Programming")
        print("4. Dark")
        print("Choose index of the category: ")
        n = int(input())
url+=dic[n]
string =""
print("(Optional) Do you want to blacklist any category or type?, Below are the types")
print("1. Not Safe for Work")
print("2. Religious")
print("3. Political")
print("4. Racist")
print("5. Sexist")
print("Choose index of the category to blacklist: ")
print("If you want to ignore, choose -1")
black = {1: "nsfw", 2: "religious", 3: "political", 4: "racist", 5: "sexist"}
choice = int(input())
if choice!=-1 and 1<=choice<=5:
    url+=("?blacklistFlags=" + black[choice])
print("(Optional) Do you want to search joke that contains a string: ")
print("Press Enter if don't want")
string = input()
if len(string)>0:
    if choice!=-1 and 1<=choice<=5:
        url+='&'
    else:
        url+='?'
    url+=("contains=" + string)
r = requests.get(url)
json_content = json.loads(r.content)
print("JOKE: ")
if json_content["error"]==False:
    if json_content["type"]=="single":
        print(json_content["joke"])
    elif json_content["type"]=="twopart":
        print("{:<10}".format("setup:") + json_content["setup"])
        print("{:<10}".format("delivery:") + json_content["delivery"])
else:
    print("{:<16}".format("message:") + json_content["message"])
    print("{:<16}".format("causedBy:") + json_content["causedBy"][0])
    for i in range(1, len(json_content["causedBy"])):
        print("{:<16}".format(" ") + json_content["causedBy"][i])
    print("{:<16}".format("additionalInfo: ") + json_content["additionalInfo"])
