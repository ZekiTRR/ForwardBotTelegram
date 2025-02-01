from pyrogram import Client, filters

api_id = "Your ID"
api_hash = "Your Hash"
chanel = "ID chanel"
photo = "https://imgur.com/gallery/women-of-world-selection-of-19th-century-depictions-of-women-around-world-from-british-librarys-digitised-historical-books-FGtvgBp#/t/images" # a example 
app = Client("my_account", api_id, api_hash)

#app.start()
#app.set_chat_photo(chanel,photo="photo.png")
#app.stop()
@app.on_message(~filters.me,~filters.channel)

async def my_handler(client,message):
       await message.forward(chanel)
app.run()