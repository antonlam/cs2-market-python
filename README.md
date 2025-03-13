# cs2-market-python
These project is used to find the item that you are looking for on steam market or bitskin

step 0: install request and beautifulsoup on the environment
> pip install bs4

> pip install requests

**Not necessanary to download those json file**

**1: Run the updateJsonFile.py (run it whenever it is a new case or collection)**
![image](https://github.com/user-attachments/assets/276d5e03-4364-42ca-822d-f8622c39a5ae)

press "y" when the program ask the "it takes several minutes to run, please press [y] to confirm"
after that item.json, info.json and collectionName.json will be added

![image](https://github.com/user-attachments/assets/dbacdcb6-23d8-4bbd-a7b4-87b076977122)
 
**2: For steamSkinPriceFinder.py**
enter an url of a item from steam market

![image](https://github.com/user-attachments/assets/77dff0ca-9dfc-4859-9087-747a689a99dd)

![image](https://github.com/user-attachments/assets/fca898d1-8d20-4630-bb1d-160e98bf86b7)

**3: For bitskinSkinFinder.py**
*** it will help you to open the resulted item on the webpage automatically

**The program will ask several question **
1. How many items do you want to find?
> should be in integer format

2. Please enter the minimum float value (range: 0.0 - 1.0)
> should be in float format

3. Please enter the maximum float value (range: 0.0 - 1.0)
> should be in float format

4. Please enter the exterior represented value
> should be in integer format

| Condition        | Value |
|------------------|-------|
| Factory New      | 1     |
| Minimal Wear     | 2     |
| Field-Tested     | 3     |
| Well-Worn        | 4     |
| Battle-Scarred   | 5     |
| Not Painted      | 6     |

5.Please enter the category represented value 
> should be in integer format

| Category         | Value |
|------------------|-------|
| Normal           | 1     |
| ★                | 2     |
| StatTrak™        | 3     |
| ★ StatTrak™      | 4     |
| Souvenir         | 5     |

6. Please enter the quality represented value
> should be in integer format

| Rarity             | Value |
|--------------------|-------|
| Consumer Grade     | 1     |
| Industrial Grade   | 2     |
| Mil-Spec Grade     | 3     |
| Restricted         | 4     |
| Classified         | 5     |
| Covert             | 6     |
| Contraband         | 7     |
| Base Grade         | 8     |
| High Grade         | 9     |
| Remarkable         | 10    |
| Exotic             | 11    |
| Extraordinary      | 12    |
| Distinguished      | 13    |
| Exceptional        | 14    |
| Superior           | 15    |
| Master             | 16    |

7. Please enter the Collection ID represented value
> should be in integer format

| Collection                        | Value |
|-----------------------------------|-------|
| The Huntsman Collection           | 1     |
| The Arms Deal Collection          | 2     |
| The eSports 2013 Collection       | 3     |
| The Bravo Collection              | 4     |
| The Arms Deal 2 Collection        | 5     |
| The eSports 2013 Winter Collection| 6     |
| The Winter Offensive Collection   | 7     |
| The Arms Deal 3 Collection        | 8     |
| The Phoenix Collection            | 9     |
| The Breakout Collection           | 10    |
| The eSports 2014 Summer Collection| 11    |
| The Vanguard Collection           | 12    |
| The Chroma Collection             | 13    |
|             ...                   | 14    |

8. Do you want the program open the page after complete searching?
> should be response in 'y' or 'Y' or "yes" or "Yes" -> yes

> other response will be treat as no
   
