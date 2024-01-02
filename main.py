from cocapi import Player
from cocapi import Clan
from cocapi import loadToken
from cocapi import clanService
#this code will retrieve all the names and tags of all the player in the same clan as luminawight.

myClanService = clanService()

loadToken("TOKEN") # this is the path of a file you've locally created containing you api token

player = Player("#VPJY8CVG") # tag of player luminawight 
clan = Clan(player.getClanTag())

print("Members of clan : " + clan.getInfos().get("name"))

for member in myClanService.getMembersOfClan(player.getClanTag(),True):
    print(member.getInfos().get("name"),member.getInfos().get("tag"))

if player.verify("game-api-token"): # this token can be found in the game parameters under "API TOKEN", usefull to authanticate an account that exists
    print("Player verified " + player.global_info.get("name", "No Name"))
else:
    print("Player not verified")