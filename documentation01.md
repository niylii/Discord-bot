# Documentation:

# Quickstart with a simple Discord.py Bot :

1. **Import the Discord Library:**
   - `import discord` – Brings in the Discord.py library to make a bot.

2. **Set Up Intents:**
   - `intents = discord.Intents.default()` – Sets the default permissions.
   - `intents.message_content = True` – Gives the bot permission to **read message content** (necessary for detecting `$hello`).

3. **Create the Bot Client:**
   - `client = discord.Client(intents=intents)` – Creates the bot and gives it the set permissions (intents).

4. **Bot Event: When Bot Logs In:**
   - `@client.event` – A decorator to register events.
   - `async def on_ready()` – Runs when the bot is **online**.
   - `print(f'We have logged in as {client.user}')` – Prints the bot’s username to the console.

5. **Bot Event: When a Message is Sent:**
   - `@client.event` – A decorator for the message event.
   - `async def on_message(message)` – Runs every time a **message is sent** in the server.
   - `if message.author == client.user: return` – Prevents the bot from responding to its own messages.

6. **Check for `certen` Command:**
   - `if message.content.startswith('Basically anything you want it to detect'):` – Checks if the message.
   - `await message.channel.send('a response')` – Sends `"some response"` in response.

7. **Run the Bot:**
   - `client.run('token')` – Starts the bot with your **Discord token**.

---

## Summary:
- **Imports** Discord library.
- **Sets intents** to read messages.
- **Creates the bot** with the required permissions.
- **Handles events** for bot login (`on_ready`) and messages (`on_message`).
- **Replies with "somthing"** when someone types `something`.
- **Runs the bot** with your token.
