import os
from loguru import logger
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    logger.info(f"Ready, logged in as {bot.user} (ID: {bot.user.id})")


# Runs every message
@bot.event
async def on_message(message: discord.Message):
    # Ignore own messages
    if message.author == bot.user:
        return

    # Check whether bot is summoned
    if str(bot.user.id) in message.content:
        return await message.reply("WIP!")

    # Check if message is a command, otherwise leave
    if not message.content.startswith('!'):
        return

    # Message is a command
    logger.info(f'Channel {message.channel}:Author {message.author}:Content {message.content}')

    # Check if command exists
    ctx = await bot.get_context(message)
    if ctx.valid:
        logger.debug('Command was valid')
        await bot.invoke(ctx)
    else:
        logger.debug(f'Command {message.content} was invalid')
        await message.channel.send(f'Hi {message.author.mention}! I don\'t know this command.')


@bot.command(pass_context=True)
async def ping(ctx):
    """Test command"""
    await ctx.reply('Pong!')


if __name__ == '__main__':
    bot.run(os.getenv('BOT_TOKEN'))
