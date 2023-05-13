import discord
import bot_mantik

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# istemci (client) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith("$şifre"):
        await message.channel.send(bot_mantik.gen_pass(10))
    elif message.content.startswith("$yazıtura"):
        await message.channel.send(bot_mantik.yazi_tura)
    else:
        await message.channel.send(message.content)

client.run("Bot Token Here")
