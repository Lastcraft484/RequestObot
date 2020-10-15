import discord
from discord.ext import commands
import aiohttp
import asyncio
import os
import json



bot = commands.Bot(command_prefix='.')

token = open("token.txt","r").read()



@bot.command()
async def reqlist(ctx):
    with open('req.txt') as f:
        await ctx.send(f.read())



@bot.command()
async def req(ctx, req: str):    
        with open('req.txt','a') as f:
           f.write(f'\n{req}')
        await ctx.send("You submitted {} ".format(req))


@bot.command()
async def reqitem(ctx, *, search):
    with open('req.txt') as f:
        for line in f:
            if line.startswith(f'{search}'):
                await ctx.send(line)
                break
            
        else:
                
                await ctx.send("No request under that name, to create a new request type .req (item)")

@bot.command()
async def refill(ctx, test: str):    
        with open('req.txt','a') as f:
           f.write(f'\n{req}')
        await ctx.send("You added {} ".format(req))

        
@bot.command()
async def reqfile(ctx):
    await ctx.send(file=discord.File('req.txt'))



@bot.event
async def on_ready():
    print("Bot is ready!")
    print(token)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Request any thing with .req !"))

bot.run(token)
