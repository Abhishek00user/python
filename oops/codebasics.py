# implementing without class
# import datetime
# virat={
#     'first_name':'virat',
#     'last_name':'kohli',
#     'birth_year':'1988',
#     'scores': []
# }
# virat['scores'].append(80)
# virat['scores'].append(0)
# virat['scores'].append(100)

# def get_avg_score(player):
#     return sum(player['scores'])/len(player['scores'])

# def get_age(player):
#     now=datetime.datetime.now()
#     # we need to typecast here 
#     return now.year - int(player['birth_year'])

# print(get_avg_score(virat))
# print(get_age(virat))




# now implementing the same with classes and objects 
import datetime
class CricketPlayer:
    def __init__(self,fname,lname,team,birth_year):
        self.fname=fname
        self.lname=lname
        self.birth_year=birth_year
        self.team=team
        self.scores=[]

    def get_age(self):
        now=datetime.datetime.now()
        return now.year - self.birth_year
    
    def add_score(self,score):
        self.scores.append(score)

    def get_avg_score(self):
        return sum(self.scores)/len(self.scores)
# operator oveloading
    def __lt__(self,other):
        my_score=self.get_avg_score()
        other_score=other.get_avg_score()
        return my_score < other_score
    
    def __str__(self): #fixed naming format
        return f'{self.fname} {self.lname}, the cricket player from {self.team}'

virat=CricketPlayer('virat','kohli','India',1988)
virat.add_score(80)
virat.add_score(0)
virat.add_score(100)

print(virat.get_age())
print(virat.get_avg_score())

david=CricketPlayer('david','warner','australia',1985)
david.add_score(37)
david.add_score(78)
david.add_score(9)

print(david.get_age())   

print(virat<david)
print(virat)
print(david)