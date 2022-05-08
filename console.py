# Remote Discord Bot Console
# Use this to login to a discord bot, and use commands using the console.
# You can also create your own commands if you want.
# Dm Vp#0001 on discord for help.
#
#
# Copyright (C) 2022 Vp (https://github.com/herravp)
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
    import discord
    from discord.ext import commands
    from dpyConsole import Console
    from colorama import Fore
except ModuleNotFoundError:
    install("discord")
    install("dpyConsole")
    install("colorama")


client = discord.Client()
console = Console(client)

print(f"{Fore.GREEN}------------- Remote Bot Console ------------ \t\n")
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
    print(f"{Fore.GREEN} - deletechannels: Tries to delete all the channels.\n")
    print(f"{Fore.GREEN} - deletemessages: Tries to delete all the messages.\n")
    print(f"{Fore.GREEN} - deleteroles: Tries to delete all the roles.\n")
    print(f"{Fore.GREEN} - spam: Spams the given amount of messages.\n")
    print(f"{Fore.GREEN} - massnickname: Changes the nickname of all the members.\n")


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
        print(f"{Fore.RED}Error: " + error)

@console.command()
async def fetchpermissions():
    try:
        for guild in client.guilds:
            for role in guild.roles:
                print(f"{Fore.GREEN} Guild: {guild.name} \n")
                print(f"{Fore.GREEN} Roles: {role.name} \n")
                for perm in role.permissions:
                    print(f"{Fore.GREEN} Role perms: {perm}\n")
    except Exception as e:
        print(f"{Fore.RED} {e} {Fore.GREEN}\n")

@console.command()
async def fetchwebhooks():
    wlist = []
    try:
        print(f"{Fore.GREEN}Fetching webhooks... \n")
        for guild in client.guilds:
            for channel in guild.channels:
                if isinstance(channel, discord.TextChannel):
                    for webhook in channel.webhooks:
                        wlist.append(webhook)
        print(f"{Fore.GREEN} Webhooks: \n")
        for webhook in wlist:
            print(f"{Fore.GREEN} Webhook Name: {webhook.name} \n")
            print(f"{Fore.GREEN} Webhook URL: {webhook.url} \n")
            print(f"{Fore.GREEN} Webhook ID: {webhook.id} \n")
            print(f"{Fore.GREEN} Webhook Channel: {webhook.channel} \n")
    except Exception as e:
        print(Fore.RED + e + Fore.GREEN)                    


@console.command()
async def fetchmessages():
    try:
        print("Fetching messages... \n")
        for channel in client.get_all_channels():
            if isinstance(channel, discord.TextChannel):
                messages = await channel.history(limit=None).flatten()
                for message in messages:
                    with open("messages.txt", "a") as f:
                        f.write(str(message.author) + " || " + str(message.content) + "\n")
    except Exception as e:
        print(Fore.RED + e + Fore.GREEN)

@console.command()
async def fetchchannels():
    try:
        print("Fetching channels... \n")
        for channel in client.get_all_channels():
            if isinstance(channel, discord.TextChannel):
                print(channel.name + " || " + channel.id)
    except Exception as e:
        print(Fore.RED + e + Fore.GREEN)

@console.command()
async def fetchroles():
    try:
        print("Fetching roles... \n")
        for guild in client.guilds:
            for role in guild.roles:
                print(role.name + " || " + role.id)
    except Exception as e:
        print(Fore.RED + e + Fore.GREEN)        

@console.command()
async def say(message):
    try:
        print("Sending message... \n")
        for channel in client.get_all_channels():
            if isinstance(channel, discord.TextChannel):
                print("Message sent to: " + channel.name)
                await channel.send(message)
    except Exception as e:
        print(Fore.RED + e + Fore.GREEN)

@console.command()
async def deletechannels():
    try:
        print("Deleting channels... \n")
        for channel in client.get_all_channels():
            if isinstance(channel, discord.TextChannel):
                print("Deleted channel: " + channel.name)
                await channel.delete()
    except Exception as e:
        print(Fore.RED + e + Fore.GREEN)

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
        print(Fore.RED + e + Fore.GREEN)  

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
        print(Fore.RED + e + Fore.GREEN)         

@console.command()
async def spam(message, amount):
    try:
        print("Spamming... \n")
        for channel in client.get_all_channels():
            if isinstance(channel, discord.TextChannel):
                for i in range(1, int(amount) + 1):
                    print("Spammed channel: " + channel.name)
                    await channel.send(str(message))
    except Exception as e:
        print(Fore.RED + e + Fore.GREEN)

@console.command()
async def massnickname(nickname):
    try:
        print("Changing nickname... \n")
        member = discord.Member
        for member in client.get_all_members():
            if isinstance(member, discord.Member):
                print("Changed the nickname of: " + member.name)
                await member.edit(nick=nickname)
    except Exception as e:
        print(Fore.RED + e + Fore.GREEN)
                                
                



# Login
console.start()
client.run(token)
