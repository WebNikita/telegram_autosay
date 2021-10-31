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

answer_dict = {

    1:'Привет, я автоответчки Froot.\nВ данный момент, мой хозяин занят, он ответит тебе позже.\n P.s: ЕСЛИ СРОЧНО НАБЕРИ МНЕ ',
    2:'Привет, я автоответчки Froot.\nВ данный момент, мой хозяин управляет ТС, он ответит тебе позже.\n P.s: ЕСЛИ СРОЧНО НАБЕРИ МНЕ ',
    3:'Привет, я автоответчки Froot.\nВ данный момент, мой хозяин зарабатывает бабосики, он ответит тебе позже.\n P.s: ЕСЛИ СРОЧНО НАБЕРИ МНЕ ',
    4:'Привет, я автоответчки Froot.\nВ данный момент, мой хозяин спит, он ответит тебе позже.\n P.s: ЕСЛИ СРОЧНО НАБЕРИ МНЕ ',
    5:'Привет, я автоответчки Froot.\nВ данный момент, мой хозяин разминает мозги, он ответит тебе позже.\n P.s: ЕСЛИ СРОЧНО НАБЕРИ МНЕ ',

}


status_counter = 0

user_list = []


@client.on(events.NewMessage)
async def my_event_handler(event):
    global status_counter
    global user_list
    
    if list(str(event.chat_id))[0] != '-' and str(event.from_id.user_id).split()[0] != '477643858':                  #Проверка что сообщение пришло от ползователя именно мне в чат
        if status_counter != 0 and str(event.from_id.user_id).split()[0] not in user_list:
            await event.reply(answer_dict[status_counter])
            user_list.append(str(event.from_id.user_id).split()[0])
        elif status_counter == 0:
            user_list = []
    try:
        if str(event.message.peer_id.channel_id).split()[0] == '1406135438':
            if event.message.message in command_dict:
                status_counter = command_dict[event.message.message]
            elif event.message.message == "/help":
                await event.reply('''/start
/stop
/start_car
/start_work
/start_sleep
/start_learning
''')
    except:
        pass

    
    print(status_counter)


client.start()

client.run_until_disconnected()