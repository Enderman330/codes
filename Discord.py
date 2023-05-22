import os
import discord
import openai

# Authenticate with the OpenAI API using your API key
openai.api_key = "YOUR_API_KEY"

# Connect to Discord using the bot token
client = discord.Client()

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return
    
    # Use Chat GPT to generate a response
    prompt = f"User: {message.content}\nChatbot:"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
    )
    reply = response.choices[0].text.strip()
    
    # Send the response back to the Discord server
    await message.channel.send(reply)

# Run the bot
client.run("YOUR_BOT_TOKEN")

#By Enderman330
