# Powered By @BikashHalder @AdityaHalder
# ÂŠī¸ Copy Right By Bikash Halder Or Aditya Halder
# Any Problem To Report @Bgt_Chat or @AdityaDiscus
# Bot Owner @BikashHalder Or @AdityaHalder

import asyncio

from pyrogram import filters

from Bikash import config
from Bikash.strings import get_command
from Bikash import app
from Bikash.misc import SUDOERS
from Bikash.utils.database.memorydatabase import get_video_limit
from Bikash.utils.formatters import convert_bytes

VARS_COMMAND = get_command("VARS_COMMAND")


@app.on_message(filters.command(VARS_COMMAND) & SUDOERS)
async def varsFunc(client, message):
    mystic = await message.reply_text(
        "đˇ đđĨđđđŦđ đđđĸđ­ đđđ­đ­đĸđ§đ  đđ¨đŽđĢ đđ¨đ§đđĸđ  đˇ"
    )
    v_limit = await get_video_limit()
    bot_name = config.MUSIC_BOT_NAME
    up_r = f"[đđđŠđ¨ đŽđŗ]({config.UPSTREAM_REPO})"
    up_b = config.UPSTREAM_BRANCH
    auto_leave = config.AUTO_LEAVE_ASSISTANT_TIME
    yt_sleep = config.YOUTUBE_DOWNLOAD_EDIT_SLEEP
    tg_sleep = config.TELEGRAM_DOWNLOAD_EDIT_SLEEP
    playlist_limit = config.SERVER_PLAYLIST_LIMIT
    fetch_playlist = config.PLAYLIST_FETCH_LIMIT
    song = config.SONG_DOWNLOAD_DURATION
    play_duration = config.DURATION_LIMIT_MIN
    cm = config.CLEANMODE_DELETE_MINS
    auto_sug = config.AUTO_SUGGESTION_TIME
    if config.AUTO_LEAVING_ASSISTANT == str(True):
        ass = "đđđŦ â"
    else:
        ass = "đđ¨ â"
    if config.PRIVATE_BOT_MODE == str(True):
        pvt = "đđđŦ â"
    else:
        pvt = "đđ¨ â"
    if config.AUTO_SUGGESTION_MODE == str(True):
        a_sug = "đđđŦ â"
    else:
        a_sug = "đđ¨ â"
    if config.AUTO_DOWNLOADS_CLEAR == str(True):
        down = "đđđŦ â"
    else:
        down = "đđ¨ â"

    if not config.GITHUB_REPO:
        git = "đđ¨ â"
    else:
        git = f"[đđđŠđ¨ đŽđŗ]({config.GITHUB_REPO})"
    if not config.START_IMG_URL:
        start = "đđ¨ â"
    else:
        start = f"[đđĻđđ đ đŽđŗ]({config.START_IMG_URL})"
    if not config.SUPPORT_CHANNEL:
        s_c = "đđ¨ â"
    else:
        s_c = f"[đđĄđđ§đ§đđĨ đĄ]({config.SUPPORT_CHANNEL})"
    if not config.SUPPORT_GROUP:
        s_g = "đđ¨ â"
    else:
        s_g = f"[đđŽđŠđŠđ¨đĢđ­ đĨ]({config.SUPPORT_GROUP})"
    if not config.GIT_TOKEN:
        token = "đđ¨ â"
    else:
        token = "đđđŦ â"
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        sotify = "đđ¨ â"
    else:
        sotify = "đđđŦ â"
    owners = [str(ids) for ids in config.OWNER_ID]
    owner_id = " ,".join(owners)
    tg_aud = convert_bytes(config.TG_AUDIO_FILESIZE_LIMIT)
    tg_vid = convert_bytes(config.TG_VIDEO_FILESIZE_LIMIT)
    text = f"""**đŽđŗ đđđđđ đđ¨đ­ đđ¨đ§đđĸđ  đĄ:**
                    
                â° đđĸđ¤đđŦđĄ âī¸ đđĨđđ˛đđĢ âą
                    
**<u>đˇ đđđŦđĸđ đđ¨đ§đđĸđ  đđđĢđŦ đˇ:</u>**
**đē đđĸđ¤đđŦđĄ đđ¨đ­ đđđĻđ** : `{bot_name}`
**âąī¸ đđŽđĢđđ­đĸđ¨đ§ ** : `{play_duration} đđĸđ§đŽđ­đđŦ`
**đĩ đđ¨đ§đ  đđ¨đ°đ§đđ¨đđ đđŽđĢđđ­đĸđ¨đ§ ** :` {song} đđĸđ§đŽđ­đđŦ`
**âī¸ đđ°đ§đđĢ đĸđ** : `{owner_id}`
    
**<u>đˇ đđđŠđ¨ đđ¨đ§đđĸđ  đđđĢđŦ đˇ:</u>**
**đĄ đđŠđŦđ­đĢđđđĻ đđđŠđ¨** : `{up_r}`
**đˇ đđŠđŦđ­đĢđđđĻ đđĢđđ§đđĄ** : `{up_b}`
**đē đđĸđ­đĄđŽđ đđđŠđ¨** :` {git}`
**đē đđĸđ­ đđ¨đ¤đđ§**:` {token}`


**<u>đĨ đđ¨đ­ đđ¨đ§đđĸđ  đđđĢđŦ đĨ:</u>**
**đļââī¸ đđŽđ­đ¨ đđđđ¯đĸđ§đ  đđŦđŦđĸđŦđ­đđ§đ­** : `{ass}`
**đļââī¸ đđŽđ­đ¨ đđđđ¯đ đđĸđĻđ** : `{auto_leave} đđđđ¨đ§đđŦ`
**đļââī¸ đđŽđ­đ¨ đđŽđ đ đđŦđ­đĸđ¨đ§ đđ¨đđ** :` {a_sug}`
**đļââī¸ đđŽđ­đ¨ đđŽđ đ đđŦđ­đĸđ¨đ§ đđĸđĻđ** : `{auto_sug} đđđđ¨đ§đđŦ`
**đļââī¸ đđŽđ­đ¨ đđ¨đ°đ§đĨđ¨đđ ** : `{down}`
**đ đđĢđĸđ¯đđ­đ đđ¨đ­ đđ¨đđ ** : `{pvt}`
**đē đđ đđđĸđ­ đđĨđđđŠ ** : `{yt_sleep} đđđđ¨đ§đđŦ`
**đĨ đđđĨđđ đĢđđĻ đđđĸđ­ đđĨđđđŠ** :` {tg_sleep} đđđđ¨đ§đđŦ`
**â đđĨđđđ§đĻđ¨đ đđĸđ§đŦ** : `{cm} đđĸđ§đŽđ­đđŦ`
**đē đđĸđđđ¨ đđ­đĢđđđĻ đđĸđĻđĸđ­ ** : `{v_limit} đđĄđđ­`
**đŽđŗ đđđ¯đđĢ đđĨđđ˛đĨđĸđŦđ­ đđĸđĻđĸđ­ ** :` {playlist_limit}`
**â đđĨđđ˛đĨđĸđŦđ­ đđđ­đđĄ đđĸđĻđĸđ­** :` {fetch_playlist}`

**<u>đĨ đđŠđ¨đ­đĸđđ˛ đđ¨đ§đđĸđ  đđđĢđŦ đĨ:</u>**
**đĸ đđŠđ¨đ­đĸđđ˛ đđĨđĸđđ§đ­ đĸđ** :` {sotify}`
**đĸ đđŠđ¨đ­đĸđđ˛ đđĨđĸđđ§đ­ đđđđĢđđ­** : `{sotify}`

**<u>đ° đđĨđđ˛ đđĸđŗđ đđ¨đ§đđĸđ  đđđĢđŦ đĨ:</u>**
**đē đđ  đđŽđđĸđ¨ đđĸđĨđ đđĸđŗđ đđĸđĻđĸđ­** :` {tg_aud}`
**đē đđ  đđĸđđđ¨ đđĸđŗđ đđĸđĻđĸđ­ ** :` {tg_vid}`

**<u>đĨ đđąđ­đĢđ đđ¨đ§đđĸđ  đđđĢđŦ đĨ:</u>**
**đŦđŽđŠđŠđ¨đĢđ­_đđĄđđ§đ§đđĨ** : `{s_c}`
**đđŽđŠđŠđ¨đĢđ­_đđĢđ¨đŽđŠ** : ` {s_g}`
**đđ­đđĢđ­_đđĻđ _đđĢđĨ** : ` {start}`
    """
    await asyncio.sleep(1)
    await mystic.edit_text(text)
