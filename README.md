# Image-Creation-Discord-Bot

A discord Bot which sends an image to the discord channel based on user prompt.

# How to Use

1. Copy the Code from the Github repo.
2. Change 'OpenAI Api Key' with your OpenAi Api Key. You can get the APi Key from OpenAI Website.
3. Change 'TOKEN' with your Discord Bot Token
4. Run the Program
5. In Discord, type '!img' along with your prompt and the image gets sent to your discord channel

# Warnings

Use the program as a local copy since Discord bot Token and OpenAi Secret Key are public. To prevent this you can create an .env file which includes your 
Token and Secret key.

.env file
```
DISCORD_TOKEN = YOUREDISCORDTOKEN
OPENAI_TOKEN = YOUROPENAISECRETKEY
```
After doing this, replace the TOKEN in main file with DISCORD_TOKEN and likewise to OpenAI secret key

```
openai.api_key = OPENAI_TOKEN
client.run(DISCORD_TOKEN)
```

Also include 'import dotenv' package and add these lines after the import package.

```
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

```
