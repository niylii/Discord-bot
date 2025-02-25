# Documentation:
##  Discord.py Decorators Made Simple

Decorators help your bot **do stuff** when something happens on Discord (like a user typing, bot starting up, etc.). 

---

### 1. `@bot.event` / `@client.event`
- **What it does**: Runs a function when something happens, like bot starting up, or receiving a message.
  
- **Example**:
    ```python
    @bot.event  # or @client.event if you're using discord.Client()
    async def on_ready():
        print('Bot is online!')
    ```

---

### 2. `@bot.command()` / `@commands.command()`
- **What it does**: Turns a function into a **command**. Users type it to make the bot do something.
  
- **Example**:
    ```python
    @bot.command()
    async def hello(ctx):
        await ctx.send('Hello!')
    ```

---

### 3. `@commands.has_permissions()`
- **What it does**: Only allows users with specific **permissions** (like admins) to use a command.
  
- **Example**:
    ```python
    @bot.command()
    @commands.has_permissions(administrator=True)
    async def admin_only(ctx):
        await ctx.send('This is for admins only!')
    ```

---

### 4. `@commands.cooldown()`
- **What it does**: Prevents users from spamming a command too much. Adds a **cooldown**.
  
- **Example**:
    ```python
    @bot.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def cool_command(ctx):
        await ctx.send('You can only use this every 10 seconds.')
    ```

---

### 5. `@commands.is_owner()`
- **What it does**: Makes a command available **only to the bot owner**.
  
- **Example**:
    ```python
    @bot.command()
    @commands.is_owner()
    async def owner_command(ctx):
        await ctx.send('Only the bot owner can use this!')
    ```

---

### **Client-Only Events** (Used with `discord.Client()`):
1. **`@client.event`**: Like `@bot.event`, but works when using `discord.Client()` instead of `commands.Bot()`. Used for handling events like new messages or when the bot goes offline.

- **Example**:
    ```python
    @client.event
    async def on_ready():
        print('Client is online!')
    ```

2. **`@client.event` (Error handling)**: Handles errors or disconnects.

- **Example**:
    ```python
    @client.event
    async def on_error(error):
        print(f'Error occurred: {error}')
    ```

---

###  Quick Recap:
- **`@bot.event` / `@client.event`**: Used for **events** like bot startup or new messages.
- **`@bot.command()`**: Makes a function a **command** users can use.
- **`@commands.has_permissions()`**: Makes sure only **admins** or certain users can use a command.
- **`@commands.cooldown()`**: Prevents **spam** by adding a cooldown between command uses.
- **`@commands.is_owner()`**: Only allows the **owner** of the bot to use a command.
- **`@client.event`** (client-specific): Used for events like when a message is sent or when the bot goes offline.

---

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
