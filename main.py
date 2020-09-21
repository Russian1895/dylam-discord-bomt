import discord
from help import helpful
from discord.ext import commands, tasks

bday = commands.Bot(command_prefix = ['++'], case_insensitive = True, help_command = helpful())

@bday.event
async def on_ready():
    print('LIBERTY PRIME ONLINE')
    await bday.change_presence(activity = discord.Game('(Prefix is ++)'))

# @bday.command()
# async def homies(ctx,*args):
#     # await ctx.send('NICE')
#     helpful = discord.Embed(title = "Dylan's super cool help page")
#     helpful.add_field(name = 'Commands',value = '++register/++reg\n++wish\n++next')
#
#     helpful.add_field(name = 'Description', value = 'Add your stuff to the database\nWish the current birthday person\nSo you know when the next brithday is')
#     await ctx.send(embed = helpful)

@bday.command(hidden = False, description = 'shut up')
async def dylan(ctx,*args):
    await ctx.send('shut up')

@bday.command(hidden = True, description = 'secret')
async def die(ctx,*args):
    await ctx.send("I don't think so.")
    await ctx.send("https://youtu.be/MvsyxAHcGmo?t=38")






bday.run('NzU3NDA4NzI1NDAwMTU4MjQ5.X2f92A.dXieo499US-zuZHmhi88CE7MhUM')
