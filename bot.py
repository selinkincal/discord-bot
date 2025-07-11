import discord
import os

intents = discord.Intents.default()
intents.message_content = True  # Mesaj içeriğini okuyabilmek için

client =discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Bot online ")
    activity = discord.Game(name = "şu anda bunu yapıyor.")
    await client.change_presence(activity=activity)

@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    
    await message.channel.send(message.content)  


client.run(os.getenv ("DISCORD_TOKEN"))


