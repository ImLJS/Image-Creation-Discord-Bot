import discord
import openai

intents = discord.Intents.default()
intents.message_content = True

openai.api_key = 'OPEN AI KEY'
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Check if the message starts with "!generate"
    if message.content.startswith("!img"):
       
        text = message.content[len("!img"):].strip()
        
        # Use the OpenAI API to generate an image
        response = openai.Image.create(
            prompt=text,
            n=1,
            size="1024x1024",
            response_format="url"
        )

        await message.channel.send(response["data"][0]["url"])

client.run('TOKEN')



