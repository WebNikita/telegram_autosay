from telethon import TelegramClient, events
import config


client = TelegramClient('Froot', config.api_id, config.api_hash)

command_dict = {
    '/start': 1,
    '/stop': 0,
    '/start_car': 2,
    '/start_work': 3,
    '/start_sleep': 4,
    '/start_learning': 5,
}

status_counter = 0

user_list = []


@client.on(events.NewMessage)
async def my_event_handler(event):
    global status_counter
    if str(event.message.peer_id.channel_id).split()[0] == '1406135438':
        if event.message.message in command_dict:
            status_counter = command_dict[event.message.message]

    elif list(str(event.chat_id))[0] != '-' and str(event.from_id.user_id).split()[0] != '477643858':                  #Проверка что сообщение пришло от ползователя именно мне в чат
        print(event)
    
    print(status_counter)


client.start()

client.run_until_disconnected()