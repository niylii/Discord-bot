# Rei Discord Bot

## Overview

This Discord bot, built using `discord.py`, responds to user messages and commands with fun phrases.

## Features

- Replies to DMs and mentions with random responses.
- Includes a `/ping` command for creative replies.
- Syncs command tree with `!sync`.
- also `!miss` if you need to let someone know that you miss them without actually telling them

## Requirements

- Python 3.8+
- `discord.py` library (version 2.0 or higher)

the installation instructions are already mentioned in the main branch
## Features

- Replies to DMs and mentions with random responses.
- Includes a `/ping` command for creative replies.
- Syncs command tree with `!sync`.
- Missing command `!miss`

## Commands

- **`!sync`**: Syncs commands with Discord.
- **`/ping`**: Responds with a random pong message.
- **`!miss`**: you basically tag someone after the command and it says that the @user misses @the*_taged*_user

## Customization

Modify the response lists in the code:

```python
resp = [...]
resp_sp = [...]
```
## License
This project is licensed under the MIT License.
