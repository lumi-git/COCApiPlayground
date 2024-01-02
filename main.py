from cocapi import Player
from cocapi import loadToken

loadToken("TOKEN") # this is the path of a file you locately created containing you api token

player = Player("#VPJY8CVG") # tag of player luminawight

members = player.getClan().getMembers()
playerlist = []

for member in members:
    playerlist.append( member.get("tag"))

print(playerlist)