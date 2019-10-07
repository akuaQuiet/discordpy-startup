from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))



@client.event
async def on_message(message):
    if message.content.startswith('/50020'):
        role = discord.utils.get(message.guild.roles, name='全問正解者')
        await message.author.add_roles(role)
        reply = f'{message.author.mention} 全問正解です！役職を付与します。'
        await message.channel.send(reply)    
    
    
    
    
    
bot.run(token)
