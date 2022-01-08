# Import Discord Package

import discord
from discord.ext import commands

# Client (our bot)
Client = commands.Bot(command_prefix='--')


@Client.event
async def on_command_error(context, error):
    if isinstance(error, commands.MissingPermissions):
        await context.send("You don't have Permissions")
        # await context.message.delete()
    elif isinstance(error, commands.MissingRequiredArgument):
        await context.send("Please enter all the required argument")
        # await context.message.delete()


# bot version
@Client.command(name='version')
async def version(context):
    general_channel = Client.get_channel(646292969397288964)

    myEmbed = discord.Embed(title="Current Version", description="The bot is in Version 1.0", color=0x00ff00)
    myEmbed.add_field(name="Version Code", value="v1.0.0", inline=False)
    myEmbed.add_field(name="Date Released:", value="jan 3th, 2022", inline=False)
    myEmbed.set_footer(text="This is a sample footer")
    myEmbed.set_author(name="Ishaan sharma")

    await context.message.channel.send(embed=myEmbed)


@Client.event
async def on_ready():
    # DO STUFF....

    general_channel = Client.get_channel(646292969397288964)
    await general_channel.send('Hello world')

    await Client.change_presence(status=discord.Status.idle, activity=discord.Game('Listening to ishaan!'))


@Client.event
async def on_disconnect():
    general_channel = Client.get_channel(646331919830876223)
    await general_channel.send('Goodbye!')


@Client.event
async def on_message(message):
    if message.content == 'what is the version':
        general_channel = Client.get_channel(646331919830876223)

        myEmbed = discord.Embed(title="Current Version", description="The bot is in Version 1.0", color=0x00ff00)
        myEmbed.add_field(name="Version Code", value="v1.0.0", inline=False)
        myEmbed.add_field(name="Date Released:", value="sep 19th, 2021", inline=False)
        myEmbed.set_footer(text="This is a sample footer")
        myEmbed.set_author(name="ishaan sharma")

        await general_channel.send(embed=myEmbed)

    await Client.process_commands(message)


# welcome

# [moderation and admin commands]
@Client.command(aliases=['c'])
@commands.has_permissions(manage_messages=True)
async def clear(context, amount=2):
    await context.channel.purge(limit=amount)


@Client.command(aliases=['m'])
@commands.has_permissions(kick_members=True)
async def warn(context, member: discord.Member):
    muted_role = context.guild.get_role(766243336033665025)

    await member.add_roles(muted_role)

    await context.send(member.mention + "has been muted")


@Client.command(aliases=['m'])
@commands.has_permissions(kick_members=True)
async def mute(context, member: discord.Member):
    muted_role = context.guild.get_role(766243336033665025)

    await member.add_roles(muted_role)

    await context.send(member.mention + "has been muted")


@Client.command(aliases=['um'])
@commands.has_permissions(kick_members=True)
async def unmute(context, member: discord.Member):
    muted_role = context.guild.get_role(766243336033665025)

    await member.remove_roles(muted_role)

    await context.send(member.mention + "has been unmuted")


@Client.command(aliases=['k'])
@commands.has_permissions(kick_members=True)
async def kick(context, member: discord.Member, *, reason="No reason provided"):
    try:
        await member.send("you have been kicked from The works and tests, Because:" + reason)
    except:
        await context.send(member.name + "has been kicked from The coding community, Because:" + reason)
        await context.send("The member has Their dms closed.")

    await member.kick(reason=reason)


@Client.command(aliases=['b'])
@commands.has_permissions(ban_members=True)
async def ban(context, member: discord.Member, *, reason="No reason provide"):
    try:
        await member.send("you have been baned from The works and tests, Because:" + reason)
    except:
        await context.send(member.name + " has been baned from The works and tests, Because:" + reason)
        await context.send("The member has Their dms closed.")

    await member.ban(reason=reason)


@Client.command(aliases=['ub'])
@commands.has_permissions(ban_members=True)
async def unban(context, *, member):
    banned_users = await context.guild.bans()
    member_name, member_discriminator = member.split('#')

    for banned_entry in banned_users:
        user = banned_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await context.guild.unban(user)
            await context.send(member_name + "has been unbanned!")
            return
    await context.send(member + "was not found")


# Run the Client on the server
Client.run('')
