from check import *

# check requirement
check_library()

# import requirement
from genius_command import *
from tenor import *
from nsfw import *
from spotify import *
import os
from datetime import datetime
import pytz

# before run please don't forget to put bot token

description = "All Kasumi command is here"

# put all API key and bot token here

bot_token = os.getenv("DISCORD_BOT_TOKEN")
tenor_token = os.getenv("TENOR_TOKEN")

# You can change your prefix here

prefix = "k!"
presence_status = "k!help | Findind a star!"
streaming = discord.Streaming(platform="Twitch", name="k! | BanG Dream!",
                            detail="Premieres March 25, only on Netflix.",
                            url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                            game="k!help | BanG Dream!")

# First Config

nsfw_mode = True

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=prefix, description=description, intents=intents, help_command=None)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=streaming)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))


@bot.command()
async def genius(ctx):
    """I'm genius!"""
    await ctx.send("I'm online and I'm genius!")


@bot.command()
async def pfp(ctx):
    author = ctx.message.author
    embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
    embed.title = "This is"
    embed.description = "Your profile image"
    # embed.colour = "#FF5522"
    embed.set_author(name=author.display_name, url="https://youtu.be/dQw4w9WgXcQ", icon_url=author.avatar_url)
    embed.set_thumbnail(url=author.avatar_url)
    embed.set_footer(text="Hello! My name is Kasumi Toyama! My father is HelloYeew#2740.")
    await ctx.send(embed=embed)


@bot.command()
async def repeat(ctx, text: str, time: int):
    """Repeat a message x times"""
    for i in range(time):
        await ctx.send(text)


@bot.command()
async def ping(ctx):
    """ Check Ping"""
    embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
    embed.title = "🌟 I have caught a star that you throw to me!"
    embed.description = f"I catch it in {int(bot.latency * 1000)} milliseconds!"
    embed.set_footer(text="Hello! My name is Kasumi Toyama! My father is HelloYeew#2740.")
    await ctx.send(embed=embed)


@bot.command()
async def profile(ctx, member: discord.User):
    author = ctx.message.author
    embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
    if member.id == 729919152327753768:
        embed.title = f"🐵 {member.name + '#' + member.discriminator}'s Profile"
    elif member.bot:
        embed.title = f"🤖 {member.name + '#' + member.discriminator}'s Profile"
    else:
        embed.title = f"😃 {member.name + '#' + member.discriminator}'s Profile"
    embed.description = f"Request by {author.display_name}"
    embed.add_field(name="Display Name", value=member.display_name, inline=False)
    embed.add_field(name="ID", value=member.id, inline=False)
    embed.add_field(name="Create Account Time", value=f"{member.created_at} UTC", inline=False)
    embed.add_field(name="Bot?", value=member.bot, inline=False)
    embed.set_image(url=member.avatar_url)
    embed.set_footer(text="Hello! My name is Kasumi Toyama! My father is HelloYeew#2740.")
    await ctx.send(embed=embed)


@bot.command()
async def about(ctx):
    embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
    father_info = """
    My Father : HelloYeew#2740
    GitHub : https://github.com/HelloYeew
    Other SNS you can see in his Discord profiles.
    """
    embed.title = "About Kasumi"
    embed.description = "I'm Kasumi Toyama. I am finding a star that can make a music band with my friend."
    embed.add_field(name="GitHub Repositories", value="https://github.com/HelloYeew/kasumi", inline=False)
    embed.add_field(name="About My Father", value=father_info, inline=False)
    embed.set_thumbnail(url="https://github.com/HelloYeew/kasumi/blob/main/icon/kasumiicon.jpg?raw=true")
    embed.add_field(name="Under Development", value="I'm under development. My father have a lot of work to make "
                                                    "me. If you find something wrong about me you can DM my father!")
    await ctx.send(embed=embed)


@bot.command()
async def send(ctx, channel_id: int, *args):
    channel = bot.get_channel(channel_id)
    author = ctx.message.author
    message = " ".join(args[:])
    UTC = pytz.utc
    await ctx.send(f"✉️ Sending your message to channel {channel_id}...")
    embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
    embed.title = f"✉️ Message from {author.display_name}"
    embed.description = message
    embed.set_footer(text=f"Send by Kasumi | Time : {datetime.now(UTC)} UTC")
    try:
        await channel.send(embed=embed)
        await ctx.send("✅ Complete!")
    except:
        await ctx.send("❌ Error : Check your channel ID or I can't reach that channel because I'm not in that server.")


# help command

@bot.command()
async def help(ctx):
    help = f'''
    I'm here to help you!
    
    **General Command**
    - {prefix}pfp : Sender's profile picture
    - {prefix}genius : I'm genius! (Test Command)
    - {prefix}repeat (text_or_sth) (x) : Spam a text x time(s) (You cannot stop it)
    - {prefix}ping : Check ping
    - {prefix}profile (user) : Show full user's profile
    - {prefix}send (channel_id) (message) : Send a message to a specific channel by a bot (You can target every channel that a bot can access)
    - {prefix}gif (keyword) : Send first GIF search result of a keyword
    - {prefix}about : About me
    
    **Genius Command**
    - {prefix}roots2 (float_x^1) (float_x^0) : Calculate a roots of one-dimension polynomial (two numbers)
    - {prefix}roots3 (float_x^2) (float_x^1) (float_x^0) : Calculate a roots of one-dimension polynomial (three numbers)
    
    **Spotify Command (Beta)**
    - {prefix}spotify (keyword) : Get first search result from Spotify
    
    **NSFW Command**
    - {prefix}pornhub (keyword) : Get first search result from Pornhub
    - {prefix}nhentai (keyword) : Get first search result from Nhentai
    - {prefix}nhentai random : Get random hentai from Nhentai
    '''
    embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
    embed.title = "❓ Help"
    embed.description = help
    embed.set_footer(text="Hello! My name is Kasumi Toyama! My father is HelloYeew#2740.")
    await ctx.send(embed=embed)


# genius command zone

@bot.command()
async def roots2(ctx, n1: float, n2: float):
    """Root an poly"""
    author = ctx.message.author
    num = [n1, n2]
    answer = numpy.roots(num)
    embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
    embed.set_author(name=author.display_name, url="https://youtu.be/dQw4w9WgXcQ", icon_url=author.avatar_url)
    embed.title = "🧮 Calculation"
    # embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/762347346993348659/335e22e0f77a6bb717502981f57221e2.png")
    embed.description = "A roots of one-dimension polynomial (two numbers)"
    embed.add_field(name="Input", value=str(numpy.poly1d(num)), inline=False)
    embed.add_field(name="Results", value=str(answer), inline=False)
    embed.set_footer(text="Hello! My name is Kasumi Toyama! My father is HelloYeew#2740.")
    await ctx.send(embed=embed)


@bot.command()
async def roots3(ctx, n1: float, n2: float, n3: float):
    """Root an poly"""
    author = ctx.message.author
    num = [n1, n2, n3]
    answer = numpy.roots(num)
    embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
    embed.set_author(name=author.display_name, url="https://youtu.be/dQw4w9WgXcQ", icon_url=author.avatar_url)
    embed.title = "🧮 Calculation"
    # embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/762347346993348659/335e22e0f77a6bb717502981f57221e2.png")
    embed.description = "A roots of one-dimension polynomial (three numbers)"
    embed.add_field(name="Input", value=str(numpy.poly1d(num)), inline=False)
    embed.add_field(name="Results", value=str(answer), inline=False)
    embed.set_footer(text="Hello! My name is Kasumi Toyama! My father is HelloYeew#2740.")
    await ctx.send(embed=embed)


@bot.command()
async def roots4(ctx, n1: float, n2: float, n3: float, n4: float):
    """Root an poly"""
    author = ctx.message.author
    num = [n1, n2, n3, n4]
    answer = numpy.roots(num)
    embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
    embed.set_author(name=author.display_name, url="https://youtu.be/dQw4w9WgXcQ", icon_url=author.avatar_url)
    embed.title = "🧮 Calculation"
    # embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/762347346993348659/335e22e0f77a6bb717502981f57221e2.png")
    embed.description = "A roots of one-dimension polynomial (four numbers)"
    embed.add_field(name="Input", value=str(numpy.poly1d(num)), inline=False)
    embed.add_field(name="Results", value=str(answer), inline=False)
    embed.set_footer(text="Hello! My name is Kasumi Toyama! My father is HelloYeew#2740.")
    await ctx.send(embed=embed)


# tenor command zone

@bot.command()
async def gif(ctx, *args):
    """Return first GIF search result"""
    word = " ".join(args[:])
    author = ctx.message.author
    try:
        result = tenor(tenor_token, word, 1)
        if result is not None:
            embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
            embed.set_author(name=author.display_name, url="https://youtu.be/dQw4w9WgXcQ", icon_url=author.avatar_url)
            embed.title = f"🔎 Result of GIF search '{word}'"
            embed.description = f"First GIF search result of *{word}*"
            embed.set_footer(text="Hello! My name is Kasumi Toyama! My father is HelloYeew#2740.")
            embed.set_image(url=result)

        else:
            embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
            embed.set_author(name=author.display_name, url="https://youtu.be/dQw4w9WgXcQ", icon_url=author.avatar_url)
            embed.title = f"🥲 No result of GIF search '{word}'"
            embed.set_footer(text="Hello! My name is Kasumi Toyama! My father is HelloYeew#2740.")
            embed.description = "Sad"
        await ctx.send(embed=embed)
    except:
        await ctx.send("🔎 No search result!")


# Spotify Command

@bot.command()
async def spotify(ctx, *args):
    keyword = " ".join(args[:])
    search = spotify_first_search(keyword)
    embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
    embed.title = f"🔎 Result of Spotify search '{keyword}'"
    embed.description = f"First Spotify search result of *{keyword}*"
    embed.add_field(name="Name", value=search['name'], inline=False)
    embed.add_field(name="Artist", value=search['artist_name'], inline=False)
    embed.add_field(name="Album Name", value=search['album_name'], inline=False)
    embed.add_field(name="Available Country", value=search['available_country'], inline=False)
    embed.add_field(name="Release Date", value=search['release_date'], inline=True)
    embed.add_field(name="Popularity", value=search['popularity'], inline=True)
    embed.add_field(name="Preview", value=search['preview_url'], inline=False)
    embed.set_footer(
        text=f"Total result : {search['total_result']} | Hello! My name is Kasumi Toyama! My father is HelloYeew#2740.")
    embed.set_image(url=search["image_url"])
    await ctx.send(embed=embed)


# NSFW Command

@bot.command()
async def pornhub(ctx, *args):
    """Return first search pornhub results"""
    word = " ".join(args[:])
    if nsfw_mode == False:
        await ctx.send("You must enable NSFW command by **!nsfw on**")
    else:
        result = pornhub_search(word)
        embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
        embed.title = f"🔎 Result of Pornhub search '{word}'"
        embed.description = f"First GIF search result of *{word}*"
        embed.add_field(name="Name", value=result[1], inline=False)
        embed.add_field(name="Link", value=result[0], inline=False)
        embed.add_field(name="Duration", value=result[2], inline=True)
        embed.add_field(name="Rating", value=result[3], inline=True)
        embed.set_image(url=result[4])
        embed.set_footer(text="Hello! My name is Kasumi Toyama! My father is HelloYeew#2740.")
        await ctx.send(embed=embed)


@bot.command()
async def nhentai(ctx, *args):
    """Return first search pornhub results"""
    keyword = " ".join(args[:])
    if nsfw_mode == False:
        await ctx.send("You must enable NSFW command by **!nsfw on**")
    else:
        if keyword == "random":
            result = nhentai_random()
            embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
            embed.title = f"🔎 You have request random hentai from me?"
            embed.description = f"You have it!"
            embed.add_field(name="Title", value=result.title, inline=False)
            embed.add_field(name="Second Title", value=result.secondary_title, inline=False)
            embed.add_field(name="Tags", value=result.tags, inline=False)
            embed.add_field(name="Artists", value=result.artists, inline=False)
            embed.add_field(name="Characters", value=result.characters, inline=False)
            embed.add_field(name="Parodies", value=result.parodies, inline=False)
            embed.add_field(name="Group", value=result.parodies, inline=False)
            embed.add_field(name="Language", value=result.languages, inline=True)
            embed.add_field(name="Categories", value=result.categories, inline=True)
            embed.set_image(url=result.images[0])
            embed.set_footer(text="Hello! My name is Kasumi Toyama! My father is HelloYeew#2740.")
            await ctx.send(embed=embed)
        else:
            result = nhentai_search(keyword)
            embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
            embed.title = f"🔎 Result of Nhentai search '{keyword}'"
            embed.description = f"First Nhentai search result of *{keyword}*"
            embed.add_field(name="Title", value=result.title, inline=False)
            embed.add_field(name="Data Tag", value=result.data_tags, inline=False)
            embed.add_field(name="Title ID", value=result.id, inline=True)
            embed.add_field(name="Language", value=result.lang, inline=True)
            embed.set_image(url=result.cover)
            embed.set_footer(text="Hello! My name is Kasumi Toyama! My father is HelloYeew#2740.")
            await ctx.send(embed=embed)


bot.run(bot_token)
