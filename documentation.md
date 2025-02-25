# Documentation:

##  Discord.py Events (Simplified Guide)

##  What Are Events?  
Events in Discord.py allow your bot to **automatically react** when something happens in a server.

---

##  1. Bot Events (General)
| **Event**           | **When It Happens** |
|---------------------|--------------------|
| `on_ready()`       | When the bot **starts and is ready**. |
| `on_connect()`     | When the bot **connects to Discord** (before it's fully ready). |
| `on_disconnect()`  | When the bot **disconnects from Discord**. |
| `on_resumed()`     | When the bot **reconnects after losing connection**. |

---

##  2. Message Events (Chat & Commands)
| **Event**                    | **When It Happens** |
|------------------------------|--------------------|
| `on_message(message)`        | When **someone sends a message** in a channel. |
| `on_message_edit(before, after)` | When **someone edits their message**. |
| `on_message_delete(message)` | When **a message gets deleted**. |

---

##  3. Reaction & Emoji Events
| **Event**                     | **When It Happens** |
|------------------------------|--------------------|
| `on_reaction_add(reaction, user)` | When **someone reacts to a message**. |
| `on_reaction_remove(reaction, user)` | When **someone removes their reaction**. |
| `on_reaction_clear(message, reactions)` | When **all reactions are removed** from a message. |

---

##  4. Member & User Events
| **Event**                     | **When It Happens** |
|------------------------------|--------------------|
| `on_member_join(member)`     | When **a new member joins the server**. |
| `on_member_remove(member)`   | When **a member leaves or gets kicked**. |
| `on_member_update(before, after)` | When **a member updates their profile (nickname, roles, etc.)**. |
| `on_user_update(before, after)` | When **a user updates their profile (avatar, username, etc.)**. |

---

##  5. Role & Permission Events
| **Event**                     | **When It Happens** |
|------------------------------|--------------------|
| `on_guild_role_create(role)`  | When **a new role is created**. |
| `on_guild_role_delete(role)`  | When **a role is deleted**. |
| `on_guild_role_update(before, after)` | When **a role is changed (permissions, name, color, etc.)**. |

---

##  6. Channel Events (Text & Voice)
| **Event**                      | **When It Happens** |
|--------------------------------|--------------------|
| `on_guild_channel_create(channel)` | When **a new channel is created**. |
| `on_guild_channel_delete(channel)` | When **a channel is deleted**. |
| `on_guild_channel_update(before, after)` | When **a channel is updated (name, topic, etc.)**. |

---

##  7. Voice Chat Events
| **Event**                        | **When It Happens** |
|----------------------------------|--------------------|
| `on_voice_state_update(member, before, after)` | When **someone joins/leaves a voice channel or mutes/unmutes**. |

---

##  8. Error & Exception Events
| **Event**                        | **When It Happens** |
|----------------------------------|--------------------|
| `on_error(event, *args, **kwargs)` | When **an error happens inside an event**. |
| `on_command_error(ctx, error)` | When **a command causes an error**. |

---

## Summary  
- **Bot events** → When the bot starts, connects, or disconnects.  
- **Message events** → When messages are sent, edited, or deleted.  
- **Reaction events** → When someone adds or removes reactions.  
- **Member events** → When people join, leave, or update their profiles.  
- **Role events** → When roles are created, deleted, or updated.  
- **Channel events** → When channels are created, deleted, or updated.  
- **Voice chat events** → When someone joins/mutes a voice channel.  
- **Error events** → When something goes wrong.  

---

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

