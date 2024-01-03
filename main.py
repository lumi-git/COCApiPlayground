from cocapiwrapper import application
from cocapiwrapper import Player
from cocapiwrapper import Clan
from cocapiwrapper import tokenLoader
from cocapiwrapper import clanService

#this code will retrieve all the names and tags of all the player in the same clan as luminawight.

tokenLoader.fromFile("TOKEN") # this is the path of a file you've locally created containing you api token
application.createApplication()

myClanService = clanService()

player = Player("#VPJY8CVG") # tag of player luminawight 
clan = Clan(player.getClanTag())

print("Members of clan : " + clan.getInfos().get("name"))

for member in myClanService.getMembersOfClan(clan,True):
    print(f"--------{member.getInfos().get('name')}----------")
    print("tag: "+member.getTag())
    #print(str(member.getInfos().get("donations")) + " troops donated during this season")
    #print(str([ach for ach in member.getInfos().get("achievements") if ach["name"] == "Gold Grab"][0]['value']) + " gold stolen")

if player.verify("game-api-token"): # this token can be found in the game parameters under "API TOKEN", usefull to authanticate an account that exists
    print("Player verified " + player.getInfos().get("name", "No Name"))
else:
    print("Player not verified")

application.destroyApplication()