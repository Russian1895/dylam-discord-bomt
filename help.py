from discord.ext import commands
import discord
class helpful(commands.HelpCommand):
    async def send_bot_help(self,mapping):
        ctx = self.context
        skip = await self.filter_commands(mapping[None])
        # print(mapping)
        helpful = discord.Embed(title = "Dylan's super cool help page")
        print(skip)
        luna = []
        for each in skip:
            luna.append('++' + each.name)

        helpful.add_field(name = 'Commands',value = '\n'.join(luna))

        lackey = ['Help page (duh)']
        for beach in skip:
            lackey.append(beach.description)

        helpful.add_field(name = 'Description', value = '\n'.join(lackey))
        await ctx.send(embed = helpful)

# async def help(ctx,*args):
#     # await ctx.send('NICE')
#     helpful = discord.Embed(title = "Dylan's super cool help page")
#     helpful.add_field(name = 'Commands',value = '++register/++reg\n++wish\n++next')
#
#     helpful.add_field(name = 'Description', value = 'Add your stuff to the database\nWish the current birthday person\nSo you know when the next brithday is')
#     await ctx.send(embed = helpful)
