import requests
from bs4 import BeautifulSoup


for it in [0, 1, 2, 3, 4, 5]:
  filename = open('savedURL.txt',"r")
  for i,line in enumerate(filename):
    line = line.replace("\n", "")
    if i == it:
        myUrl = line

        #myUrl ='https://www.ligastavok.ru/bets/popular/soccer/rossiia-id-350/rossiiskaia-premer-liga-id-5271/tcska-moskva-krasnodar-id-10139610'
        myUrl2 ='https://www.ligastavok.ru/bets/my-line/soccer/rossiia-id-350/rossiiskaiapremer-liga-id-5271'
        class TeamStat():
            def __init__(self, teamName, scoredGoal, missedGoal):
                self.teamName = teamName
                self.scoredGoal = scoredGoal
                self.missedGoal = missedGoal

        page = requests.get(myUrl)
        soup = BeautifulSoup(page.content, 'html.parser')

        # событие на победу, для того чтоб взять имена команд
        event = soup.find(style = "order:101") 
        event = event.find_all(class_ = "bui-outcome__title-457ff4")
        teamName1   = event[0].get_text()
        teamName2   = event[2].get_text()

        # событие команда 1 забьет
        event = soup.find_all('div', title = "КОМ1 забьет")
        event = event[0].parent
        event = event.find_all(itemprop = "price")
        
        team1Goal   = event[0].get_text()
        team1NoGoal = event[1].get_text()

        # событие команда 2 забьет
        event = soup.find_all('div', title = "КОМ2 забьет")
        event = event[0].parent
        event = event.find_all(itemprop = "price")
        team2Goal   = event[0].get_text()
        team2NoGoal = event[1].get_text()

        team1 = TeamStat("getname1", team1Goal, team2NoGoal)

        team2 = TeamStat("getname2", team2Goal, team1NoGoal)



        print(teamName2)
        print(team2.scoredGoal)
        print(team2.missedGoal)
        print("----")
        print('----')
        print(teamName1)
        print(team1.scoredGoal)
        print(team1.missedGoal)


