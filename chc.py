from telethon.errors.rpcerrorlist import YouBlockedUserError
import asyncio
from userbot import bot
from userbot.utils import admin_cmd

@bot.on(admin_cmd(pattern="chc ?(.*)"))
async def sed(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("__Please input cc who want to check!..__")
    await event.edit(f"```Checking Charge 1$ {query}```")
    async with bot.conversation("@MarioChkBot") as conv:
        try:
            jemboed = await conv.send_message(f"!chc {query}")
            await asyncio.sleep(10)
            asu = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)			
        except YouBlockedUserError:
            return await event.reply("Unblock @MarioChkBot or chat first")
        if asu.text.startswith("Wait for result..."):
            return await event.edit(f"Charge 1$ {query} Invalid!")
        else:
            await event.edit(asu.message)
            await event.client.delete_messages(conv.chat_id, [jemboed.id, asu.id])