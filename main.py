import discord
from help import helpful
from discord.ext import commands, tasks
from discord.utils import get
import openpyxl as xl
from person import person
from discord.ext.commands import Bot
import datetime
import random
import dotenv
import os
import asyncio
env_file = dotenv.dotenv_values()
# MOST OF WHAT I HAVE IMPORTED HERE IS ABSOLUTELY USELESS
import youtube_dl

# VERSION 1.18
# special thanks to Andres for teaching me about discord.py rewrite

bday = commands.Bot(command_prefix = ['='], case_insensitive = True, help_command = helpful())
#I don't actually think these vars do anything but I keep them cause they are cute
name1 = ''
name2 = ''
multiple = False

players = {}
# YEAH THESE ARE THE SONG FILES LISTEN I DONT OPTIMIZE CODE VERY WELL OK
choices = ['Akina Nakamori - Anata no Portrait.flac',
'Akina Nakamori - Fragile Afternoon.flac',
'Akina Nakamori - Hot Springs.flac',
'Akina Nakamori - Into the Azure Night.mp3',
'Akina Nakamori - Legend of the Galaxy.flac',
'Akina Nakamori - Mythology.mp3',
'Akina Nakamori - Shojo A.mp3',
'Akina Nakamori - Slow Motion.flac',
'Akina Nakamori - Shipwreck.mp3',
'Anri - SHYNESS BOY.flac',
'Anri - WINDY SUMMER.flac',
'Anri - YOU ARE NOT ALONE.flac',
'Hitomi Ishikawa - Alone.mp3',
'Hitomi Ishikawa - Heart Communication.mp3',
'Hitomi Ishikawa - Machibuse.mp3',
'Hitomi Ishikawa - Right to Right.mp3',
'Naoko Kawai - Control.mp3',
'Naughty Boys - Ongaku.mp3',
'Taeko Onuki - Desolation.flac',
'Taeko Onuki - Law of Nature.flac',
'Taeko Onuki - Metropolis.flac',
'Taeko Onuki - Summer Connection.flac',
'Tatsu Yamashita - Saucy Dog.flac',
'Tatsuro Yamashita - DAYDREAM.flac',
'Tatsuro Yamashita - Ride on Time.flac',
'Aqua City - Misty night Cruising.mp3',
'Aqua City - Reverside Hotel.mp3',
'CINDY - Believing in Ourselves.flac',
'i have no idea - Refrain.mp3',
'Ito Chieri - Merry Christmas.flac',
'Kingo Hamada - Dolphin in Town.mp3',
'Kingo Hamada - Midnight Cruisin.mp3',
'Mai Yamane - Tasogare.mp3',
# TASOGARE DOESNT WORK FOR SOME REASON PLS HELP
'Mariya Takeuchi - Once Again.flac',
'Mariya Takeuchi - Plastic Love.flac',
'Mariya Takeuchi - September.flac',
'Meiko Nakahara - Fantasy.flac',
'Meiko Nakahara - Friday Magic.flac',
'Meiko Nakahara - Gigolo.flac',
"Tomoko Aran - I'm In Love.flac",
'Yasuha - Flyby Chinatown.flac',
'Yasuha - Paul Pauly Paul.mp3',
'Yasuha - Short Story.flac',
'Yuming Matsutoya - No Side.mp3',
'Yuming Matsutoya - No-return.flac',
'Yuming Matsutoya - Refrain Something.flac',
'Yuming Matsutoya - Youthful Regret.mp3',
'Miki Matsubara - Stay with me.flac',
'Momoko Kikuchi - Ivory Coast.mp3',
"Momoko Kikuchi - Can't Meet You Anymore.mp3",
'Momoko Kikuchi - Natsuiro Kataomoi.mp3',
'Wink - Turn It Into Love.mp3'
]

# THIS BAD BOY HERE CHECKS TO SEE IF THE BOT ACTUALLY WORKS
@bday.event
async def on_ready():
    print('LIBERTY PRIME ONLINE')
    await bday.change_presence(activity = discord.Game('(Prefix is =)'))

# TEST COMMAND TO MAKE SURE THE BOT RESPONDS TO COMMANDS
@bday.command(hidden = False, description = 'shut up')
async def dylan(ctx,*args):
    await ctx.send('shut up')

# MY THANKS
@bday.command(hidden = True, description = 'yes')
async def thanks(ctx,*args):
    await ctx.send('Yeah no problem buddy.')

# CYCLES NAMES WHEN IT IS SOMEONE's BIRTHDAY TODAY
@tasks.loop(seconds = 10)
async def pain(ctx, mult, name1, name2 = '', cycle = 0):
    ctx = ctx.author
    await bday.wait_until_ready()
    if mult == False:
        await ctx.guild.me.edit(nick=name1)
    else:
        if cycle == 0:
            await ctx.guild.me.edit(nick=name1)
            cycle = 1
        if cycle == 1:
            await ctx.guild.me.edit(nick=name2)
            cycle = 0

# CHOOSES A RANDOM SONG FROM THE SONGS FOLDER TO GET FUNKY WITH
@bday.command(hidden = False, pass_context = True,description = 'Plays a random song.')
async def song(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
    else:
        await ctx.send("you aren't connected to a voice channel silly")
        return
    global vc
    try:
        vc=await channel.connect()
    except:
        TimeoutError
    if vc.is_playing():
        vc.stop()

    bum = random.randint(0,len(choices))
    last = choices[bum]
    current = discord.Embed(title = "Now Playing:")
    current.add_field(name = f'Song {bum + 1}/{len(choices)}', value = last)
    await ctx.send(embed = current)
    guild = ctx.message.guild
    voice_client = guild.voice_client
    player = vc.play(discord.FFmpegPCMAudio(f'songs\{last}'), after=lambda e: print('done', e))

@bday.command(hidden = False, pass_context = True,description = 'Pick a list song by #')
async def pick(ctx, num = 1):
    num = num - 1
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
    else:
        await ctx.send("you aren't connected to a voice channel dum dum")
        return
    global vc
    try:
        vc=await channel.connect()
    except:
        TimeoutError
    if vc.is_playing():
        vc.stop()
    last = choices[num]
    current = discord.Embed(title = "Now Playing:")
    current.add_field(name = f'Song {num + 1}/{len(choices)}', value = last)
    await ctx.send(embed = current)
    guild = ctx.message.guild
    voice_client = guild.voice_client
    player = vc.play(discord.FFmpegPCMAudio(f'songs\{last}'), after=lambda e: print('done', e))

# GIVES A SHITTY LIST OF ALL THE SONGS IN THE SONG FOLDER
@bday.command(hidden = False, pass_context = True,description = 'List for =song.')
async def slist(ctx):
    sorry = choices.copy()
    for each in sorry:
        sorry[sorry.index(each)] = f'{sorry.index(each) + 1}: {each}'
    # print(sorry)
    dog = discord.Embed(title = "List o' songs")
    dog.add_field(name = f'There are currently {len(sorry)} songs in the =song list.',value="Please tell me if any of this doesn't play properly")
    dog.set_footer(text='\n'.join(sorry))
    await ctx.send(embed = dog)

@bday.command(hidden = False, description = "List for =next")
async def blist(ctx,*args):
    guys = xl.load_workbook('homies.xlsx')
    yeet = guys['Sheet1']
    thing = yeet.cell(1, 1)
    people = []
    f = []
    l = []
    date = []

    for row in range(yeet.max_row):
        first = yeet.cell(row+1, 1)
        last = yeet.cell(row+1, 2)
        mon = yeet.cell(row+1, 3)
        day = yeet.cell(row+1, 4)
        yea = yeet.cell(row+1, 5)
        lamer = person(first.value,mon.value,day.value,yea.value,last.value)
        f.append(first.value)
        if last.value == None:
            l.append(' ')
        else:
            l.append(last.value)
        date.append(f'{str(mon.value)}/{str(day.value)}/{str(yea.value)}')
        people.append(lamer)

    pog = discord.Embed(title = "List o' Birthdays")
    pog.add_field(name = 'First Name',value = '\n'.join(f))
    pog.add_field(name = 'Last Name', value = '\n'.join(l))
    pog.add_field(name = 'M/D/Y', value = '\n'.join(date))
    pog.set_footer(text = f'There are currently {len(people)} people in the =next list.')
    await ctx.send(embed = pog)

# SECRET COMMAND FOR SECRET PEOPLE
@bday.command(hidden = True, pass_context = True,description = 'metal gear')
async def snake(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
    else:
        await ctx.send("you aren't connected to a voice channel silly")
        return
    global vc
    try:
        vc=await channel.connect()
    except:
        TimeoutError
    if vc.is_playing():
        vc.stop()

    bum = random.randint(0,28)
    last = choices[bum]
    current = discord.Embed(title = "Now (secretly) Playing:")
    current.add_field(name = 'Snake Eater.mp3', value = 'ladder moment')
    await ctx.send(embed = current)
    guild = ctx.message.guild
    voice_client = guild.voice_client
    player = vc.play(discord.FFmpegPCMAudio('songs\Snake Eater.mp3'), after=lambda e: print('done', e))


# STOPS WHATEVER THE BOT WAS PLAYING AND DISCONNECTS IT FROM THE VC
@bday.command(hidden = False, pass_context = True,description = 'Silence da bot.')
async def stop(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
    else:
        await ctx.send("the bot isn't in a voice channel dummy")
        return
    global vc
    try:
        await ctx.send("*rude*")
        vc.stop()
        await vc.disconnect()
    except:
        TimeoutError

# ANOTHER GLORIOUS SECRET COMMAND
@bday.command(hidden = True, description = 'secret')
async def die(ctx,*args):
    await ctx.send("I don't think so.")
    await ctx.send("https://youtu.be/MvsyxAHcGmo?t=38")

@bday.command(hidden = True, description = 'secret death')
async def kill(ctx,name):
    if name == 'dylan' or name == 'Dylan':
        await ctx.send(f'ah')
        await asyncio.sleep(0.5)
        await ctx.send(f'ah')
        await asyncio.sleep(0.5)
        await ctx.send(f'ah')
        await asyncio.sleep(0.5)
        await ctx.send(f'*not so fast*')
    else:
        chance = random.randint(0,1)
        if chance == 0:
            await ctx.send(f'{name} dies')
        else:
            await ctx.send(f'{name} had divine shield and lived!')

# SECRET COMMAND THAT MAY OR MAY NOT ACTUALLY WORK
@bday.command(hidden = True, description = 'yes')
async def funny(ctx,*args):
    await ctx.send("https://cdn.discordapp.com/attachments/729916916793081956/752758446767472640/video0-1.mp4")

# TELLS A RANDOM JOKE (sort of)
@bday.command(hidden = False, description = "Tells a joke.")
async def joke(ctx,*args):
    await ctx.send('*you*')

@bday.command(hidden = True, description = "Tells a joke.")
async def talk(ctx,*args):
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
    else:
        await ctx.send("Sorry, I can't seem to connect to your channel ):")
        return
    global vc
    try:
        vc=await channel.connect()
    except:
        TimeoutError
    if vc.is_playing():
        vc.stop()
    guild = ctx.message.guild
    voice_client = guild.voice_client
    player = vc.play(discord.FFmpegPCMAudio('songs\me.m4a'), after=lambda e: print('done', e))

# LITERALLY JUST BDAY FROM AP COMPUTER SCIENCE
@bday.command(hidden = False, description = "Who's birthday is next?")
async def next(ctx,*args):

    homies = xl.load_workbook('homies.xlsx')
    sheet = homies['Sheet1']
    thing = sheet.cell(1, 1)
    people = []
    parallel = []
    today = datetime.date.today()

    for row in range(sheet.max_row):
        first = sheet.cell(row+1, 1)
        last = sheet.cell(row+1, 2)
        mon = sheet.cell(row+1, 3)
        day = sheet.cell(row+1, 4)
        yea = sheet.cell(row+1, 5)
        gamer = person(first.value,mon.value,day.value,yea.value,last.value)
        people.append(gamer)

    for filter in range(len(people)):
        if people[filter].bdate.month == today.month:
            parallel.append(people[filter])

    if len(parallel) == 0:
        await ctx.send('There are no birthdays this month...')
        return
    else:
        closest = []
        othertemp = 0
        for h in range(len(parallel)):
            if (parallel[h].bdate.day > today.day) or (parallel[h].bdate.day == today.day):
                othertemp = othertemp + 1
        if othertemp == 0:
            await ctx.send('There are no more birthdays this month!')
            return

    chumpy = 0
    poopdex = 0
    peedex = 0

    for b in range(len(parallel)):
        if parallel[b].bdate.day == today.day:
            if chumpy == 0:
                chumpy = chumpy + 1
                poopdex = b
            if chumpy > 0:
                chumpy = chumpy + 1
                peedex = b
        if parallel[b].bdate.day > today.day:
            closest.append(parallel[b].bdate.day - today.day)

    bing = 'thing'
    ding = 'wing'
    ing = 'hell'

    if parallel[poopdex].lname == '':
        bing = ''
    else:
        bing = ' '
    if parallel[peedex].lname == '':
        ding = ''
    else:
        ding = ' '

    if chumpy == 2:
        await ctx.send(f"My boy {parallel[poopdex].fname}{bing}{parallel[poopdex].lname}'s birthday is today!")
        multiple = False
        name1 = (f"Birthday!: {parallel[poopdex].fname}{bing}{parallel[poopdex].lname}")
        pain.start(ctx,False,name1)
        return

    if chumpy > 1:
        await ctx.send(f"My boys {parallel[poopdex].fname}{bing}{parallel[poopdex].lname} and {parallel[peedex].fname}{ding}{parallel[peedex].lname}'s birthdays are today!")
        name1 = (f"Birthday!: {parallel[poopdex].fname}{bing}{parallel[poopdex].lname}")
        name2 = (f"Birthday!: {parallel[peedex].fname}{ding}{parallel[peedex].lname}")
        multiple = True
        pain.start(ctx,True,name1,name2)
        return

    min = 34
    index = 0
    twindex = 0
    twins = False

    for c in range(len(closest)):
        if closest[c] < min:
            min = closest[c]
            index = c
    for f in range(len(closest)):
        if closest[f] == min and f != index:
            twindex = f
            twins = True

    temp = today.year - parallel[index].bdate.year
    hemp = today.year - parallel[twindex].bdate.year

    if parallel[twindex].lname == '':
        ing = ''
    else:
        ing = ' '

    if (min == 1 and twins == False) or (min > 1 and twins == False):
        await ctx.send(f'My boy {parallel[index].fname}{bing}{parallel[index].lname} is turning {temp} in {min} day(s)!')
        pain.start(ctx)
        return
    if (min == 1 and twins == True) or (min > 1 and twins == True):
        await ctx.send(f"My boys {parallel[index].fname}{bing}{parallel[index].lname} and {parallel[twindex].fname}{ing}{parallel[twindex].lname} are turning {temp} and {hemp} in {min} day(s)!")
        pain.start(ctx)
        return

# GENERAL ERROR OUTPUT IN CASE YOU SUCK

@bday.event
async def on_command_error(ctx,error):
    print('YO MR. WHITE THERE WAS AN ERROR')
    await ctx.send('Jesse what are you talking about')
    await ctx.send('https://images-ext-1.discordapp.net/external/zVLE2_gnWhF5U9PkVBT5crntTeGuyQq2lAis6r6wvqE/%3Fwidth%3D1200%26format%3Djpeg/https/i.insider.com/5dadec34045a313a5926f727')

bday.run(env_file['TOKEN'])
