import requests
from urllib.request import urlopen
import json
import os
import sys

requestUrl = "https://bymykel.github.io/CSGO-API/api/en/collections.json"

data = {
    "exteriorDic": {
        "1": "Factory New",
        "2": "Minimal Wear",
        "3": "Field-Tested",
        "4": "Well-Worn",
        "5": "Battle-Scarred",
        "6": "Not Painted"
    },
    "categoryDic": {
        "1": "Normal",
        "2": "★",
        "3": "StatTrak™",
        "4": "★ StatTrak™",
        "5": "Souvenir"
    },
    "qualityDic": {
        "1": "Consumer Grade",
        "2": "Industrial Grade",
        "3": "Mil-Spec Grade",
        "4": "Restricted",
        "5": "Classified",
        "6": "Covert",
        "7": "Contraband",
        "8": "Base Grade",
        "9": "High Grade",
        "10": "Remarkable",
        "11": "Exotic",
        "12": "Extraordinary",
        "13": "Distinguished",
        "14": "Exceptional",
        "15": "Superior",
        "16": "Master"
    }
}

def get_jsonparsed_data(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

def collectionNameJson():
    try:
        with open("collectionName.json", "w", encoding='utf-8') as file:
            file.write('{\n\t"collections": {\n')
            length = len(get_jsonparsed_data(requestUrl))
            for i in range(length):
                name = get_jsonparsed_data(requestUrl)[i]["name"]
                file.write(f'\t\t\"{str(i+1)}\": \"{name}\"')
                print(name)
                if(i!=length-1):
                    file.write(",\n")
            file.write("\t}\n}")
            file.close()
            print("Collection Update Completed")
    except Exception as e:
        print(f"An error occurred for collectionName.json: {str(e)}")

def infoJson():
    try:
        with open('info.json', 'w', encoding='utf-8') as json_file:
            # Using indent=4 for pretty printing with proper indentation
            json.dump(data, json_file, indent=4, ensure_ascii=False)
        print("JSON file 'item_data.json' has been created successfully!")
    except Exception as e:
        print(f"An error occurred for info.json: {str(e)}")

def itemJson():
    try:
        with open("info.json", "w", encoding='UTF-8') as file:
            length = len(get_jsonparsed_data(requestUrl))
            file.write('{\n\t\"collections\" : {')
            for i in range(length):
                name = get_jsonparsed_data(requestUrl)[i]["name"]
                contains = get_jsonparsed_data(requestUrl)[i]["contains"]
                print(str(i+1)+": Start getting "+name +" info")
                file.write('\n\t\t\"' + name+'\" : {\n')
                for j in range(len(contains)):
                    #print(contains[j]['name'], contains[j]['rarity']['name'])
                    file.write('\t\t\t\"'+ str(j+1) + '\": { \n\t\t\t\t\"name\" : \"' + contains[j]['name'] +'\" , \n\t\t\t\t\"quality\" : \"' + contains[j]['rarity']['name'] +'\" \n\t\t\t}')
                    if(j != len(contains)-1):
                        file.write(",\n")
                file.write("\n\t\t}")
                if(i != length-1):
                    file.write(',\n')
                print(name+" Done")
            file.write('\t}\n}')
    except Exception as e:
        print(f"An error occurred for item.json: {str(e)}")

if __name__ == "__main__":
    ans = input("Do u want to download the json file?")
    if(ans =='y' or ans == 'Y' or ans == 'yes' or ans == 'Yes'):
        infoJson()
        itemJson()
        collectionNameJson()
    else:
        print("The Json file download has been cancel")
        sys.exit()
