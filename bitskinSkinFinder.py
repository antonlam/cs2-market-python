import requests
from bs4 import BeautifulSoup
import webbrowser
from urllib.request import urlopen
import json
import time

chrome_path ="C:/Program Files/Google/Chrome/Application/chrome.exe %s"
requestUrl = "https://bymykel.github.io/CSGO-API/api/en/collections.json"

with open('info.json', 'r', encoding='utf-8-sig') as infoFile:
    data = json.load(infoFile)

with open('collectionName.json', 'r', encoding='utf-8-sig') as collectionFile:
    allCollection = json.load(collectionFile)
    
exteriorDic = data['exteriorDic']
categoryDic = data['categoryDic']
qualityDic = data['qualityDic']
collections = allCollection['collections']


def get_jsonparsed_data(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

def searchListGen(minfloat, maxfloat, exterior, category, quality, colID) :
    wantedDict = {}
    weaponName =[]
    
    with open('item.json', 'r', encoding='utf-8-sig') as itemCollectionFIle:
        itemCol = json.load(itemCollectionFIle)

    requiredDict = itemCol['collections'][colID]
    for i in range(len(requiredDict)):
        if(requiredDict[str(i+1)]['quality'] == qualityDic[str(quality)]):
            weaponName.append(requiredDict[str(i+1)]['name'])
    
    #list=[minfloat,maxfloat,exterior,category,quality, weaponName]
    return [minfloat, maxfloat, exterior, category, quality, weaponName]

def getSearchLink(searchList):
    for item in searchList[5]:

        skinInfo = {'minfloat':searchList[0],
                    'maxfloat':searchList[1],
                    'exterior':searchList[2],
                    'category':searchList[3],
                    'quality':searchList[4],
                    'skinName':item}
        searchlink = 'https://bitskins.com/market/cs2?search={"order":[{"field":"price","order":"ASC"}],"where":{"float_value_from":' +\
                str(skinInfo['minfloat'])+\
                ',"float_value_to":'+\
                str(skinInfo['maxfloat'])+\
                ',"exterior_id":['+\
                str(skinInfo['exterior'])+\
                '],"skin_name":"'+\
                skinInfo['skinName'].replace(" ","+")+\
                '","category_id":['+\
                str(skinInfo['category'])+\
                '],"quality_id":['+\
                str(skinInfo['quality'])+\
                ']}}'
        #webbrowser.get(chrome_path).open(searchlink)
        print(searchlink)

def filteredBitSkinUrl(searchList):
    urlList=[]
    for item in searchList[5]:
        if item == 'M4A4 | Magnesium' or item ==  'M4A4 | Poly Mag' or item == "M4A1-S | Emphorosaur-S" or item =="Glock-18 | Clear Polymer":
            pass
        else:
            skinInfo = {'minfloat':searchList[0],
                        'maxfloat':searchList[1],
                        'exterior':searchList[2],
                        'category':searchList[3],
                        'quality':searchList[4],
                        'skinName':item}

            auth_key = '5882298064b24660fd03f6c28bbd004e6d3b61b10b9ed814d6a0ee2cb0decb50'
            data = {
              "limit": 30,
              "offset": 0,
              "where": {
                "discount_from": 0, # 0% or more
                "float_value_from": searchList[0],
                "float_value_to": searchList[1],
                "exterior_id": [searchList[2]],
                "category_id": [searchList[3]],
                "quality_id":[searchList[4]],
                "skin_name": ("%"+skinInfo['skinName']+"%").replace(" ","%")
              }
            }

            headers = {'x-apikey': auth_key}
            res = requests.post('https://api.bitskins.com/market/search/730', headers=headers, json=data)
            response = json.loads(res.text)
            #print(response['list'])
            for item in response['list']:
                urlList.append("https://bitskins.com/item/cs2/"+item['id'])
    return urlList

def openWantedSkinWebsite(currentSearchList):
    for list in currentSearchList:
        for item in filteredBitSkinUrl(list):
            print(item)
            time.sleep(0.1)
            webbrowser.get(chrome_path).open(item)

def filteredSteamMarketUrl(searchList):
    urlList=[]
    for item in searchList[5]:
        skinInfo = {'minfloat':searchList[0],
                    'maxfloat':searchList[1],
                    'exterior':searchList[2],
                    'category':searchList[3],
                    'quality':searchList[4],
                    'skinName':item}

def print_dictionary(dicName, dicContent):
    print(f"\n{dic_name}:")
    for key, value in dicContent.items():
        print(f"'{key}' = '{value}'")

if __name__ == "__main__":
    try:
        with open('info.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        ary = []
        for dic_name, dic_content in data.items():
            ary.append(dic_content)
    except FileNotFoundError:
        print("Error: 'info.json' file not found!")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in 'info.json'!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    try:
        with open("collectionName.json", "r", encoding='utf-8') as file:
            data = json.load(file)
        ary2 = []
        for dic_name, dic_content in data.items():
            ary2.append(dic_content)
    except FileNotFoundError:
        print("Error: 'info.json' file not found!")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in 'collectionName.json'!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    currentSearchList = []
        
    searchNum = input("How many items do you want to find? ")
    while not(searchNum.isdigit()):
        print("it is not digit")
        searchNum = input("How many items do you want to find? ")
      
    for num in range(int(searchNum)):
        minfloat = input("Please enter the minimum float value (range: 0.0 - 1.0): ")
        try:
            minfloat = float(minfloat)
        except ValueError:
            while not(isinstance(minfloat, float)):
                print("Invalid float value")
                minfloat = input("Please enter the minimum float value (range: 0.0 - 1.0): ")
            
        maxfloat = input("Please enter the maximum float value (range: 0.0 - 1.0): ")
        try:
            maxfloat = float(maxfloat)
        except ValueError:
            while not(isinstance(maxfloat, float)):
                print("Invalid float value")
                maxfloat = input("Please enter the maximum float value (range: 0.0 - 1.0): ")
                
        while maxfloat <= minfloat:
            print("Maximum float must be greater than minimum float!")
            maxfloat = get_float_input("Please enter the maximum float value: ")
            
        print("For the Exterior list: ")
        for key, value in ary[0].items():
            print(value + " : " + key)
        exterior = input("Please enter the exterior represented value: ")

        try:
            exterior = int(exterior)
        except ValueError:
            while type(exterior) != int:
                print("Invalid int value")
                exterior = input("Please enter the exterior represented value: ")
                try:
                    exterior = int(exterior)
                except ValueError:
                    pass
        print("For the Category list: ")
        for key, value in ary[1].items():
            print(value + " : " + key)
        category = input("Please enter the category represented value: ")

        try:
            category = int(category)
        except ValueError:
            while type(category) != int:
                print("Invalid int value")
                category = input("Please enter the category represented value: ")
                try:
                    category = int(category)
                except ValueError:
                    pass
                
        print("For the Quality list: ")
        for key, value in ary[2].items():
            print(value + " : " + key)
        quality = input("Please enter the quality represented value: ")

        try:
            quality = int(quality)
        except ValueError:
            while type(quality) != int:
                print("Invalid int value")
                quality = input("Please enter the quality represented value: ")
                try:
                    quality = int(quality)  # Attempt conversion inside the loop
                except ValueError:
                    pass  # Continue loop if conversion fails

        print("For the Collection ID list: ")
        for key, value in ary2[0].items():
            print(value + " : " + key)
        colID = input("Please enter the Collection ID represented value: ")

        try:
            colID = int(colID)
        except ValueError:
            while type(colID) != int:
                print("Invalid int value")
                quality = input("Please enter the Collection ID represented value: ")
                try:
                    colID = int(colID)
                except ValueError:
                    pass
        currentSearchList.append(searchListGen(minfloat, maxfloat, exterior, category, quality, collections[str(colID-1)]))
        
    turnOnBrowser = input("Do you want the program open the page after complete searching? ")
    if(turnOnBrowser == 'y' or "yes" or 'Y' or "Yes"):
        openWantedSkinWebsite(currentSearchList)
    

