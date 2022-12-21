import requests, bs4
import pandas as pd

# define the team owners and relevant url
dict = {
    'Nick': 'https://www.fleaflicker.com/nfl/leagues/328883/teams/1675064/schedule', 
    'Mark': 'https://www.fleaflicker.com/nfl/leagues/328883/teams/1675082/schedule', 
    'Sawyer': 'https://www.fleaflicker.com/nfl/leagues/328883/teams/1675152/schedule', 
    'Caleb': 'https://www.fleaflicker.com/nfl/leagues/328883/teams/1675380/schedule',
    'Daniel': 'https://www.fleaflicker.com/nfl/leagues/328883/teams/1675535/schedule',
    'Metch': 'https://www.fleaflicker.com/nfl/leagues/328883/teams/1717410/schedule',
    'Tonia': 'https://www.fleaflicker.com/nfl/leagues/328883/teams/1718460/schedule',
    'Dennis': 'https://www.fleaflicker.com/nfl/leagues/328883/teams/1723314/schedule'
}

# create empty df
luck_df = pd.DataFrame(index= range(15), columns = range(8))
for i in range(8):
    # use bs4 to pull the luck scores
    page = requests.get(list(dict.values())[i])
    soup = bs4.BeautifulSoup(page.content, "html.parser")
    luck = soup.find_all("span", class_ = "tt-content")
    # create empty list for manipulating scores
    luck_temp = []
    # pull only the score out and drop the html artifacts
    for j in luck:
        luck_temp.append(j.text)
    # remove the whitespaces and +'s    
    for k, ele in enumerate(luck_temp):
        luck_temp[k] = ele.replace(' ', '').replace('+', '')
    # remove anything that isn't a number
    for h, ele in enumerate(luck_temp):
        if luck_temp[h].isalpha() == True:
            del luck_temp[h]
    # there is some bug here that retains the last entry. this removes it
    luck_temp = luck_temp[0:len(luck_temp) - 1]
    # first week did not have all teams, this adds a 0 for that week only for those teams
    if len(luck_temp) == 14:
        luck_temp.insert(0, 0)
    # put list into the empty df
    luck_df[i] = luck_temp
# rename df columns    
luck_df.columns = list(dict.keys())

#TO DO: scrape scores, analysis