# Powered By @BikashHalder @AdityaHalder
# Ā©ļø Copy Right By Bikash Halder Or Aditya Halder
# Any Problem To Report @Bgt_Chat or @AdityaDiscus
# Bot Owner @BikashHalder Or @AdityaHalder

from pyrogram import filters
from pyrogram.types import Message

from Bikash.config import BANNED_USERS, adminlist
from Bikash.strings import get_command
from Bikash import app
from Bikash.utils.database import (delete_authuser, get_authuser,
                                       get_authuser_names,
                                       save_authuser)
from Bikash.utils.decorators import AdminActual
from Bikash.utils.formatters import int_to_alpha

# Command
AUTH_COMMAND = get_command("AUTH_COMMAND")
UNAUTH_COMMAND = get_command("UNAUTH_COMMAND")
AUTHUSERS_COMMAND = get_command("AUTHUSERS_COMMAND")


@app.on_message(
    filters.command(AUTH_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminActual
async def auth(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("**š„ ššš©š„š² ššØ š šš¬šš«'š¬ ššš¬š¬šš š šš« šš¢šÆš šš¬šš«š§šš¦š/šš¬šš« šš āØ ...**")
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        user_id = message.from_user.id
        token = await int_to_alpha(user.id)
        from_user_name = message.from_user.first_name
        from_user_id = message.from_user.id
        _check = await get_authuser_names(message.chat.id)
        count = len(_check)
        if int(count) == 20:
            return await message.reply_text("**š„ ššØš® ššš§ šš§š„š² šššÆš šš šš¬šš«š¬\nš¢š§ ššØš®š« šš«šØš®š© šš®š­š”šØš«š¢š¬šš šš¬šš«š¬\nšš¢š¬š­ (ššš) āØ ...**")
        if token not in _check:
            assis = {
                "auth_user_id": user.id,
                "auth_name": user.first_name,
                "admin_id": from_user_id,
                "admin_name": from_user_name,
            }
            get = adminlist.get(message.chat.id)
            if get:
                if user.id not in get:
                    get.append(user.id)
            await save_authuser(message.chat.id, token, assis)
            return await message.reply_text("**ā ššššš ššØ šš®š­š”šØš«š¢š¬šš šš¬šš«š¬\nšš¢š¬š­ šš ššØš®š« šš«šØš®š© āØ ...**")
        else:
            await message.reply_text("**ā šš„š«šššš² š¢š§ šš”š šš®š­š”šØš«š¢š¬šš\nšš¬šš«š¬ šš¢š¬š­ š ...**")
        return
    from_user_id = message.from_user.id
    user_id = message.reply_to_message.from_user.id
    user_name = message.reply_to_message.from_user.first_name
    token = await int_to_alpha(user_id)
    from_user_name = message.from_user.first_name
    _check = await get_authuser_names(message.chat.id)
    count = 0
    for smex in _check:
        count += 1
    if int(count) == 20:
        return await message.reply_text("**š„ ššØš® ššš§ šš§š„š² šššÆš šš šš¬šš«š¬\nš¢š§ ššØš®š« šš«šØš®š© šš®š­š”šØš«š¢š¬šš šš¬šš«š¬\nšš¢š¬š­ (ššš) āØ ...**")
    if token not in _check:
        assis = {
            "auth_user_id": user_id,
            "auth_name": user_name,
            "admin_id": from_user_id,
            "admin_name": from_user_name,
        }
        get = adminlist.get(message.chat.id)
        if get:
            if user_id not in get:
                get.append(user_id)
        await save_authuser(message.chat.id, token, assis)        
        return await message.reply_text("**ā ššššš ššØ šš®š­š”šØš«š¢š¬šš šš¬šš«š¬\nšš¢š¬š­ šš ššØš®š« šš«šØš®š© āØ ..**")
    else:
        await message.reply_text("**ā šš„š«šššš² š¢š§ šš”š šš®š­š”šØš«š¢š¬šš\nšš¬šš«š¬ šš¢š¬š­ š ...**")


@app.on_message(
    filters.command(UNAUTH_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminActual
async def unauthusers(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("**š„ ššš©š„š² ššØ š šš¬šš«'š¬ ššš¬š¬šš š šš« šš¢šÆš šš¬šš«š§šš¦š/šš¬šš« šš āØ ...**")
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        token = await int_to_alpha(user.id)
        deleted = await delete_authuser(message.chat.id, token)
        get = adminlist.get(message.chat.id)
        if get:
            if user.id in get:
                get.remove(user.id)
        if deleted:            
            return await message.reply_text("**ā ššš¦šØšÆšš šš«šØš¦ šš®š­š”šØš«š¢š¬šš\nšš¬šš«š¬ šš¢š¬š­ šš ššØš®š« šš«šØš®š© āØ ..**")
        else:
            return await message.reply_text("**ā ššš«š šš­šš šš¬šš« š¢š¬ ššØš­ šš§ \nšš®š­š”šØš«š¢š¬šš šš¬šš«ā....**")
    user_id = message.reply_to_message.from_user.id
    token = await int_to_alpha(user_id)
    deleted = await delete_authuser(message.chat.id, token)
    get = adminlist.get(message.chat.id)
    if get:
        if user_id in get:
            get.remove(user_id)
    if deleted:        
        return await message.reply_text("**ā ššš¦šØšÆšš šš«šØš¦ šš®š­š”šØš«š¢š¬šš\nšš¬šš«š¬ šš¢š¬š­ šš ššØš®š« šš«šØš®š© āØ **")
    else:
        return await message.reply_text("**Ā» ā ššš«š šš­šš šš¬šš« š¢š¬ ššØš­ šš§ \nšš®š­š”šØš«š¢š¬šš šš¬šš«ā...**")


@app.on_message(
    filters.command(AUTHUSERS_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
async def authusers(client, message: Message, _):
    _playlist = await get_authuser_names(message.chat.id)
    if not _playlist:
        return await message.reply_text("**ā ššØ šš®š­š”šØš«š¢š¬šš šš¬šš«š¬ ššØš®š§š\nš¢š§ ššØš®š« šš«šØš®š© ā**")
    else:
        j = 0
        mystic = await message.reply_text("**š šš„ššš¬š ššš¢š­, ššš­šš”š¢š§š  šš„š„\nšš®š­š”šØš«š¢š¬šš šš¬šš«š¬ āØ ...**")
        text = "**š§ø šš®š­š”šØš«š¢š¬šš šš¬šš«š¬ šš¢š¬š­ :**\n\n"
        for note in _playlist:
            _note = await get_authuser(message.chat.id, note)
            user_id = _note["auth_user_id"]
            admin_id = _note["admin_id"]
            admin_name = _note["admin_name"]
            try:
                user = await app.get_users(user_id)
                user = user.first_name
                j += 1
            except Exception:
                continue
            text += f"{j}ā¤ {user}[`{user_id}`]\n"
            text += f"   {'ā ššššš šš² :-'} {admin_name}[`{admin_id}`]\n\n"
        await mystic.delete()
        await message.reply_text(text)
