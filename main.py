from discord.ext import commands, tasks
import discord
from request import *
from randomUrl import *
import requests
from bs4 import BeautifulSoup
from list import *
from functions import *
import asyncio
import youtube_dl
from random import *
from time import *
import openai

openai.api_key = ""
bot = commands.Bot(command_prefix = "!", intents=discord.Intents.all())
musics = {}
ytdl = youtube_dl.YoutubeDL()

@bot.event
async def on_ready():
    print(f'Le bot est connectée comme: {bot.user}')
    changeStatus.start()
        
status = ["/ask-gpt", "!mot", "!invite"]

@tasks.loop(seconds = 360)
async def changeStatus():
	game = discord.Game(choice(status))
	await bot.change_presence(activity = game)

class Video:
    def __init__(self, link):
        video = ytdl.extract_info(link, download=False)
        video_format = video["formats"][0]
        self.url = video["webpage_url"]
        self.stream_url = video_format["url"]

#@bot.event
#async def on_message(message):
#	if message.content.lower() in tg:
#		await message.channel.send("Regarde toi avant d'insulté !")
#       await bot.process_commands(message)


@bot.command()
async def say(ctx, *args):
    await ctx.message.delete()
    await ctx.send(" ".join(args))

@bot.command()
async def ping(ctx):
	await ctx.send("pong !")

@bot.command()
async def nitro(ctx):
	await ctx.send(randomNitro())

@bot.command()
async def time(ctx):
	await ctx.send(heure())

@bot.command()
async def blague(ctx):
	await ctx.send(blagues[rdm()])

@bot.command()
async def gif(ctx, *args):
    url = str(gifs(" ".join(args)))
    await ctx.send(url)

@bot.command()
async def raid(ctx):
    await ctx.send(f"```Raid en cours...```")
    sleep(10)
    await ctx.send("https://media.tenor.com/x8v1oNUOmg4AAAAM/rickroll-roll.gif")

@bot.command()
async def gay(ctx, name= ""):
    a = name
    if a == "":
        
        embed = discord.Embed(title = "**Es-tu Gay ?**", 
        description = "** " + ctx.author.mention + " est gay à " + str(pourcent()) + " % :rainbow_flag: **")
        await ctx.send(embed = embed)
    else:
            if "@" in a:
                 
                embed = discord.Embed(title = "**Est-il Gay ?**", 
                description = "** " + name + " est gay à " + str(pourcent()) + " % :rainbow_flag: **")
                await ctx.send(embed = embed)
            else:
                await ctx.send("vous devez mentionner quelqu'un !")

@bot.command()
async def invite(ctx):
    embed = discord.Embed(url="https://discord.com/api/oauth2/authorize?client_id=1056723056862691350&permissions=8&scope=bot%20applications.commands", 
    title = "**Clique sur ce lien pour invité le bot sur ton serveur !**")
    await ctx.send(embed = embed)

@bot.command()
async def mot(ctx):
     c = mots[randint(0, (len(mots) - 1))]
     embed = discord.Embed(title= "**Trouve le bon mot**", description=f"**Trouve le mot dans le bon ordre:** *{word(c)}*\nTemps 30sec.")
     await ctx.send(embed = embed)
     sleep(30)
     await ctx.send("Temps écroulé !!! Le mot était ||" + c + "||")

@bot.command()
async def hack(ctx, nom : discord.User):
    msg = await ctx.send("```Hack de " + nom.name + " en cours...```")
    sleep(5)
    await msg.edit(content= "```Recherches de l'adresse mail...```")
    sleep(5)
    await msg.edit(content="```Adresse mail et mdp Trouvé !```")
    sleep(5)
    await msg.edit(content="```Adresse mail: " + nom.name + email[randint(0, 2)] + "\n Mdp: " + nom.name + "1234```")
    sleep(5)
    await msg.edit(content="```Recherches d'autres comptes...```")
    sleep(5)
    await msg.edit(content="```Compte " + account[randint(0, 11)] + " Trouvé !```")
    sleep(5)
    await msg.edit(content="```Hack de " + nom.name + " Réussi !```")

@bot.command()
async def ask(ctx, *args : str):
    firstEmbed = discord.Embed(title="> " + " ".join(args), description="Réponse en cours...")
    msg = await ctx.send(embed = firstEmbed)
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=" ".join(args),
    temperature=0.6,
    max_tokens=2000
    )
    result=response.choices[0].text
    embed = discord.Embed(title="> " + " ".join(args), description="```" + result + "```")
    await msg.edit(embed = embed)


#@bot.command()
#async def help(ctx):
#    embed = discord.Embed(title= "Listes des commandes du bot:", description= "**blaque:** envoie une blague aléatoire.\n**gay:** Vérifie si tu es gay ou non.\n**gif:** Envoie un gif.\n**play:** Mets de la musique\n**skip:** arrete la musique.\n**raid:** raid le serveur.\n**time:** Envoie l'heure et la date actuelle.\n**say:** Fais parlé le bot.\n**porn:** Envoie un gif.\n**hentai:** Envoie une photo.")

@bot.command()
async def porn(ctx):
     if ctx.channel.is_nsfw():
        await ctx.send(poorn())
     else:
          await ctx.send("Désolé mais cette commande est uniquement disponible dans des salons NSFW")
@bot.command()
async def hentai(ctx):
     if ctx.channel.is_nsfw():
        await ctx.send(hentaii())
     else:
          await ctx.send("Désolé mais cette commande est uniquement disponible dans des salons NSFW")

#Musique

@bot.command()
async def leave(ctx):
    client = ctx.guild.voice_client
    await client.disconnect()
    musics[ctx.guild] = []

@bot.command()
async def resume(ctx):
    client = ctx.guild.voice_client
    if client.is_paused():
        client.resume()


@bot.command()
async def pause(ctx):
    client = ctx.guild.voice_client
    if not client.is_paused():
        client.pause()


@bot.command()
async def skip(ctx):
    client = ctx.guild.voice_client
    client.stop()


def play_song(client, queue, song):
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(song.stream_url
        , before_options = "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"))

    def next(_):
        if len(queue) > 0:
            new_song = queue[0]
            del queue[0]
            play_song(client, queue, new_song)
        else:
            asyncio.run_coroutine_threadsafe(client.disconnect(), bot.loop)

    client.play(source, after=next)


@bot.command()
async def play(ctx, url):
    print("play")
    client = ctx.guild.voice_client

    if client and client.channel:
        video = Video(url)
        musics[ctx.guild].append(video)
    else:
        channel = ctx.author.voice.channel
        video = Video(url)
        musics[ctx.guild] = []
        client = await channel.connect()
        await ctx.send(f"Lancement de la vidéo : {video.url}")
        play_song(client, musics[ctx.guild], video)

bot.run('Token ici')
