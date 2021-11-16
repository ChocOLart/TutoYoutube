# Importation du module discord

import asyncio
from random import randint
import discord

from discord.ext import commands

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(intents=intents, command_prefix=",")


@bot.event
async def on_ready():
    print("Bot prét")
    await bot.change_presence(activity=discord.Game(name="Rich Presence Here"))


@bot.command()
async def plugin(ctx):
    await ctx.send("INSTALLEZ LE PLUGIN DE <@523274732808830986> @everyone")


@bot.command()
async def devinelenom(ctx):
    n = randint(0, 2)
    print(n)
    await ctx.send("Choisis un site entre ces 3")
    await asyncio.sleep(0.5)
    await ctx.send("PornHub")
    await asyncio.sleep(0.5)
    await ctx.send("Tukif")
    await asyncio.sleep(0.5)
    await ctx.send("Reddit")
    msg = await bot.wait_for('message')
    message = msg.content
    if n == 0:
        reponse = "pornhub"
        if message.lower() == reponse.lower():
            await ctx.send("Bravo tu as trouvé le bon nom")
            await ctx.send("https://fr.pornhub.com/")
        else:
            await ctx.send("C'est raté retente ta chance !")
    if n == 1:
        reponse = "Tukif"
        Reponse = "tukif"
        if message.lower() == reponse.lower():
            await ctx.send("Bravo tu as trouvé le bon nom")
            await ctx.send("https://tukif.com/")

            
        else:
            await ctx.send("C'est raté retente ta chance !")
    elif n == 2:
        reponse = "Reddit"
        Reponse = "reddit"
        if message.lower() == reponse.lower():
            await ctx.send("Bravo tu as trouvé le bon nom")
            await ctx.send("https://www.reddit.com/r/hentai")

            
        else:
            await ctx.send("C'est raté retente ta chance !")


@bot.command()
async def bestwaifu(ctx, *message):
    if len(message) == 0:
        await ctx.send("Bah dis un nom frr")
    else:
        await ctx.send(f"La best waifu est bien sur {message}")


@bot.command()
async def clear(ctx):
    await ctx.channel.purge(limit=9999)
    await ctx.send("Le channel a bien était clear")
    await asyncio.sleep(3)
    await ctx.channel.purge(limit=1)


@bot.event
async def on_ready():
    print('Bot Prét')


@bot.event
async def on_member_join(member: discord.Member):
    channel = bot.get_channel(865359992307449917)
    await channel.send(f"QUI L'A INVITE ON DEVAIT EN INVITER AUCUN !!")


@bot.command()
async def ship(ctx, message, messagee):
    n = randint(1, 100)
    if 50 > n > 25:
        await ctx.send(f"Le taux de comptabilité entre {message} et {messagee} est de {n} %")
        await ctx.send("Ca peux le faire entre vous")

    elif 50 < n < 75:
        await ctx.send(f"Le taux de comptabilité entre {message} et {messagee} est de {n} %")
        await ctx.send("Ca marche bien en vrai")

    elif 95 > n > 75:
        await ctx.send(f"Le taux de comptabilité entre {message} et {messagee} est de {n} %")
        await ctx.send("Ca marche de ouf")

    elif 100 > n > 95:
        await ctx.send(f"Le taux de comptabilité entre {message} et {messagee} est de {n} %")
        await ctx.send("C'est plus que parfait la")

    elif 25 > n > 0:
        await ctx.send(f"Le taux de comptabilité entre {message} et {messagee} est de {n} %")
        await ctx.send("Garde espoir bg/blg")


@bot.command()
async def youtubezerox(ctx):
    await ctx.send("La chaine de ZeroX est https://www.youtube.com/channel/UCg-mYj8e1a2_MTSF3gH69aA")


@bot.command()
async def playlist(ctx):
    await ctx.send('Quelle genre de playlists veux tu ? \n"Rap" \n"Sad" \n"Rock" \n"Lil Nas X"')
    message = await bot.wait_for('message')
    msg = message.content
    if msg.lower() == 'sad':
        await ctx.send("Ca devrait te plaire https://www.youtube.com/playlist?list=PLRixXwtcDFrlWlZDYMoY7iOyVeeenjlgD")
    elif msg.lower() == 'rap':
        await ctx.send("Sorry on a pas encore de playlist rap")
    elif msg.lower() == 'rock':
        await ctx.send("")


@bot.command()
async def celib(ctx):
    await ctx.send("Bienvenue dans la team celib dont <@523274732808830986> fait partie mais plus pour longtemps")


@bot.command()
async def leche(ctx):
    await ctx.send("Est ce que t'a déja léééééché les DEUX boules d'un mec !?")


@bot.command()
async def foudroye(ctx):
    await ctx.send("Est ce que tu t'es déja fait fouuuudroyé ??")


@bot.command()
async def round(ctx):
    await ctx.send("Combien de round pour te mettre ko ?????")


@bot.command()
async def pourcombien(ctx):
    await ctx.send("Pour combien tu touche en bas la en baaaas !?!?")
    await asyncio.sleep(5)
    await ctx.send("Pour 10€")


@bot.command()
async def ptdrtki(ctx):
    await ctx.send("ptdr t ki https://www.youtube.com/watch?v=C6Ny4g0738Q")


@bot.command()
async def blc(ctx):
    await ctx.send("Bas les couilles frères")


@bot.command()
async def placedelafemme(ctx):
    await ctx.send("Dans la cuisine")


@bot.command()
async def placedelhomme(ctx):
    await ctx.send("Dans la cousine")


@bot.command()
async def disquette(ctx):
    value = randint(0, 4)
    if value == 0:
        await ctx.send("1 : Sol Do Mi")
    if value == 1:
        await ctx.send(
            "2 : Ton père travaillerais pas chez SNCF car j'attends la ligne vers ton coeur (Pas grave si elle est en "
            "retard) ")
    if value == 2:
        await ctx.send(
            "3 : Ton père serait pas un arabe parce qu'il a volé toutes les étoiles du monde pour les mettre dans tes "
            "yeux")
    if value == 3:
        await ctx.send("4 : Ton père travaillerait pas chez Nintendo parce que t'a un corps de déesse")
    if value == 4:
        await ctx.send("5 : Tu t'appellerais pas Ben Laden parce qu'avec avec toi  j'ai 2 tours d'avance pour te pécho")


jeton = "OTA4MDI5NjAxMDAxOTA2Mjc2.YYvydw.ymQ7TpOuaGhsHy5Lhhv5US8PbaI"

bot.run(jeton)
