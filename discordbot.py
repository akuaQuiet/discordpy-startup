from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def akua(ctx):
    await ctx.send('ガノン窓副窓主')


@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('くーちゃんきゃわわ')


@client.event
async def on_message(message):
    if message.content.startswith('/50020'):
        role = discord.utils.get(message.guild.roles, name='全問正解者')
        await message.author.add_roles(role)
        reply = f'{message.author.mention} 全問正解です！役職を付与します。'
        await message.channel.send(reply)    
    
    
    
    
    
bot.run(token)
