> [!IMPORTATNT]
> This bot will have a lot of Troubleshooting, since it's not hosted, so it might not respond all the times.

# Discord-bot

A simple Silly Discord bot built using `discord.py` that responds to commands and messages in both servers and DMs.

---

## Features
- Responds to the `/ping` command with `Pong!`.
- Responds to messages in both servers and DMs with yes (to everything).

---

## Prerequisites
- Python 3.8 or higher.
- A Discord bot token from the [Discord Developer Portal](https://discord.com/developers/applications).

---

## Setup

### 1. Install Dependencies
1. Clone this repository or download the code.
2. Install the required dependencies:
   ```bash
   pip install discord.py
```
### 2.Set up the bot
1. Go to [Discord Developer Portal](https://discord.com/developers/applications).
2. Create a new application and add a bot then copy the bot token.

### 3. Configure the Bot
1. Open the `mybot.py` file.
2. Replace `'your token'` with your bot's token

### 4. Run the Bot
1. Start the bot: `python mybot.py`
2. Sync slash commands: In your Discord server, type !sync to register the slash commands.
---

## Usage

### Commands
- **`/ping`**: Responds with `Pong!`.
- **`!sync`**: sync done! (run this once after starting the bot).

### Messages
- The bot will respond to every message with `yes ma'am/sir`.
