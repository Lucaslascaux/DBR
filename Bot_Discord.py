import discord



#calsse qui permet de créer un client 
#intents = discord.Intents.default()
#intents.message_content = True
default_Intents = discord.Intents.default()
default_Intents.members = True
client = discord.Client(intents=default_Intents)



@client.event
async def on_ready():
    print("Le bot est prêt")

 #  @client.event
    #async def on_message(message):
       #if message.content.lower() = "ping":

@client.event
async def on_member_join(member):
    general_channel : discord.TextChannel = client.get_channel(1064552023263039543)
    await general_channel.send(content=f"Bienvenu sur le serveur {member.display_name}", delete_after=5)




client.run("MTA2NDU0ODk3Nzc1MzcyNzAxNg.Ghozlc.LhpnJRsXvvqrLA-UUPKUko0IQteCJsHHNvflr8")

