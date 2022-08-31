from pyrogram import Client, filters
import wget
import validators

bot =Client(
    "Instagram Project",
    api_id = 2365048,
    api_hash= "6a00ec6390ca64dda7d18c023fdb87e6",
    bot_token= "5589212202:AAEGRVSNTMTrvZlpT7OjHfW3m8ooEvrccPc"
)

@bot.on_message(filters.private)
async def hello(client, message):
    if validators.url(message.text) == True:
        wget.download(message.text)
        await message.reply('file downloaded succesfully')
    else:
        await message.reply('BSDK shi url de ye kaam nhi kar rha')
bot.run()
