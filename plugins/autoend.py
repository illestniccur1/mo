# # Powered By @BikashHalder @AdityaHalder
# Ā©ļø Copy Right By Bikash Halder Or Aditya Halder
# Any Problem To Report @Bgt_Chat or @AdityaDiscus
# Bot Owner @BikashHalder Or @AdityaHalder IF You Fresh Any Problem To Contact The BgtRobot Owner

from pyrogram import filters

from Bikash import config
from Bikash.strings import get_command
from Bikash import app
from Bikash.misc import SUDOERS
from Bikash.utils.database import autoend_off, autoend_on
from Bikash.utils.decorators.language import language

# Commands
AUTOEND_COMMAND = get_command("AUTOEND_COMMAND")


@app.on_message(filters.command(AUTOEND_COMMAND) & SUDOERS)
async def auto_end_stream(client, message):
    usage = "š° šš¬šš š š° :\n\n/autoend [enable|disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "š° šš®š­šØ šš§š šš­š«ššš¦ šš§ššš„šš ā.\n\nš„ šš š­ šš®š¬š¢š ššØš­ šš¬š¬š¢š¬š­šš§š­ šš¢š„š„ šš®š­šØ ššššÆš šš”š ššØš¢šš šš”šš­ šš”šš§ šš§š²šØš§š ššØ ššÆš­š¢šÆš šš”š ššØš¢šš šš”šš­ šš§š ššØš­ ššš§š š ššššÆš ššš¬š¬šš š š."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("š° šš®š­šØ šš§š šš­š«ššš¦ šš¢š¬ššš„šš ā.")
    else:
        await message.reply_text(usage)
