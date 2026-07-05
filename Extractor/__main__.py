import asyncio
import importlib
from pyrogram import idle
from Extractor.modules import ALL_MODULES


async def sumit_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("Extractor.modules." + all_module)

    print("» ʙᴏᴛ ᴅᴇᴘʟᴏʏ sᴜᴄᴄᴇssғᴜʟʟʏ ✨ 🎉")
    await idle()
    print("» ɢᴏᴏᴅ ʙʏᴇ ! sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ.")


if __name__ == "__main__":
    # BUG FIX: removed asyncio.run(main()) — main() was never defined (NameError crash).
    # BUG FIX: replaced deprecated loop.run_until_complete() with asyncio.run().
    asyncio.run(sumit_boot())
