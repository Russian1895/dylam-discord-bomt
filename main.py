import discord
from help import helpful
from discord.ext import commands, tasks
import openpyxl as xl
from person import person
import datetime

# VERSION 1.0

bday = commands.Bot(command_prefix = ['++'], case_insensitive = True, help_command = helpful())

@bday.event
async def on_ready():
    print('LIBERTY PRIME ONLINE')
    await bday.change_presence(activity = discord.Game('(Prefix is ++)'))

@bday.command(hidden = False, description = 'shut up')
async def dylan(ctx,*args):
    await ctx.send('shut up')

# @bday.command(hidden = False, description = 'Plays a random so')

@bday.command(hidden = True, description = 'secret')
async def die(ctx,*args):
    await ctx.send("I don't think so.")
    await ctx.send("https://youtu.be/MvsyxAHcGmo?t=38")

@bday.command(hidden = False, description = "Who's birthday is next?")
async def next(ctx,*args):

    homies = xl.load_workbook('homies.xlsx')
    sheet = homies['Sheet1']
    thing = sheet.cell(1, 1)
    # await ctx.send(thing.value)

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

    # print(people[1].bdate.month)
    for filter in range(len(people)):
        if people[filter].bdate.month == today.month:
            parallel.append(people[filter])

    if len(parallel) == 0:
        await ctx.send('There are no birthdays this month...')
    else:
        closest = []
        othertemp = 0
        for h in range(len(parallel)):
            if (parallel[h].bdate.day > today.day) or (parallel[h].bdate.day == today.day):
                othertemp = othertemp + 1
        if othertemp == 0:
            await ctx.send('There are no more birthdays this month!')

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

    if chumpy > 1:
        await ctx.send(f"My boys {parallel[poopdex].fname}{bing}{parallel[poopdex].lname} and {parallel[peedex].fname}{ding}{parallel[peedex].lname}'s birthdays are today!")

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
    if (min == 1 and twins == True) or (min > 1 and twins == True):
        await ctx.send(f"My boys {parallel[index].fname}{bing}{parallel[index].lname} and {parallel[twindex].fname}{ing}{parallel[twindex].lname} are turning {temp} and {hemp} in {min} day(s)!")
    # await ctx.send(people)

# @bday.event
# async def on_command_error(ctx,error):
#     print('YO MR. WHITE THERE WAS AN ERROR')
#     await ctx.send('Jesse what are you talking about')
#     await ctx.send('https://i.insider.com/5dadec34045a313a5926f727?width=1200&format=jpeg')



bday.run('NzU3NDA4NzI1NDAwMTU4MjQ5.X2f92A.dXieo499US-zuZHmhi88CE7MhUM')
