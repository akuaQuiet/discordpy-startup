from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

    
@bot.command()
async def うんち(ctx):
    await ctx.send(':poop:')
    

    import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='!')


@bot.group(
    pass_context=True
)
async def role(ctx: commands.Context):
    """
    役職を管理するコマンド
    例：!role set テスト
    """
    if ctx.invoked_subcommand is None:
        await bot.say("サブコマンドset, unsetのどちらかを呼んでください。")


@role.command(
    name="set",
    pass_context=True
)
async def set_role(ctx: commands.Context, *roles: discord.Role):
    """
    役職を得るコマンド
    例：!role set テスト
    """
    if not roles:
        await bot.say("不正な入力です。")
        return

    user = ctx.message.author
    await bot.add_roles(user, *roles)
    await bot.say("役職を追加しました。")


@role.command(
    name="unset",
    pass_context=True
)
async def unset_role(ctx: commands.Context, *roles: discord.Role):
    """
    役職を消すコマンド
    例：!role unset テスト
    """
    if not roles:
        await bot.say("不正な入力です。")
        return

    user = ctx.message.author
    await bot.remove_roles(user, *roles)
    await bot.say("役職を解除しました。")

bot.run(token)
