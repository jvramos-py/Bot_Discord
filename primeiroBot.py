import discord
from distutils.log import error
import random
from time import sleep
import datetime
import requests
import config as cfg
import random
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Estou pronto! Estou conectado como {bot.user}')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "Andrew" in message.content:
        await message.channel.send('Andrew? Muito gay esse cara')
        sleep(360)

    if "Diogo" in message.content:
        await message.channel.send(f'Falando com mendigos de novo {message.author.name}?!')

    await bot.process_commands(message)

    if "cinema" in message.content:
        await message.channel.send('Cinema no Japão é só desenho. O Japão é um dos países mais avançados que tem, e já descobriram a vantagem do desenho a muito tempo.')

    if "hospital" in message.content:
        await message.channel.send(f'Hospital é um perigo, {message.author.name}. Você atropela uma pessoa e ela tá bem. Você leva para o hospital, lá ela morre.')

    if "Nevermind" in message.author.name:
        await message.channel.send(f'cala a boca Andrew')

@bot.command(name="oi")
async def send_hello(ctx):
    name = ctx.author.name
    answer = f'Olá, {name}! Tudo bem?'
    await ctx.send(answer)


@bot.command(name="data")
async def current_time(ctx):
    now = datetime.datetime.now()
    now = now.strftime("%d/%m/%Y")

    await ctx.send(f'Data Atual: {now}')


@bot.command(name='hora')
async def current_time(ctx):
    now = datetime.datetime.now()
    now = now.strftime("%H:%M:%S")

    await ctx.send(f'Hora Atual: {now}')


@bot.command(name="calcular")
async def calculate_express(ctx, *expression):
    expression = ''.join(expression)
    response = eval(expression)

    await ctx.send(f'A resposta é {response}')


@bot.command()
async def binance(ctx, coin, base):
    try:
        response = requests.get(
            f'https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}')

        data = response.json()
        price = data.get('price')

        if price:
            await ctx.send(f'A cotação de {coin.upper()} para {base.upper()} está em: {price}.')
        else:
            await ctx.send(f'O par {coin}/{base} está errado.')

    except:
        await ctx.send("Não consegui fazer essa porra não")
        print(error)


@bot.command(name='frases')
async def phrases(ctx):
    answer = (cfg.frases[random.randint(0, 10)])
    await ctx.send(answer)


@bot.command(name='squirtleFoda')
async def get_random_image(ctx):
    url_image = 'https://i.pinimg.com/280x280_RS/cf/26/e9/cf26e931688d813198a6ed5b5218a219.jpg'

    embed = discord.Embed(
        title="Squirtle muito foda bebendo skol e comendo coxinha",
        description="Não precisa de descrição, só é muito foda",
        color=0xfb75fb
    )

    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)

    embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)

    embed.set_image(url=url_image)

    await ctx.send(embed=embed)


bot.run(cfg.token)
