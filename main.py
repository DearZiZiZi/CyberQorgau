from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError
import asyncio

# First account
api_id_1 = ''
api_hash_1 = ''
phone_number_1 = ''
client1 = TelegramClient('session_name_1', api_id_1, api_hash_1)

# Second account
api_id_3 = ''
api_hash_3 = ''
phone_number_3 = ''
client3 = TelegramClient('session_name_3', api_id_3, api_hash_3)

# Third account
api_id_2 = ''
api_hash_2 = ''
phone_number_2 = ''
client2 = TelegramClient('session_name_2', api_id_2, api_hash_2)


# Fouth account
api_id_4 = ''
api_hash_4 = ''
phone_number_4 = ''
client4 = TelegramClient('session_name_4', api_id_4, api_hash_4)

# Fifth account
api_id_5 = ''
api_hash_5 = ''
phone_number_5 = ''
client5 = TelegramClient('session_name_5', api_id_5, api_hash_5)

# Sixth account
api_id_6 = ''
api_hash_6 = ''
phone_number_6 = ''
client6 = TelegramClient('session_name_6', api_id_6, api_hash_6)

# Seventh account
api_id_7 = ''
api_hash_7 = ''
phone_number_7 = ''
client7 = TelegramClient('session_name_7', api_id_7, api_hash_7)

# EItenth account
api_id_8 = ''
api_hash_8 = ''
phone_number_8 = ''
client8 = TelegramClient('session_name_8', api_id_8, api_hash_8)

async def authorize_client(client, phone_number):
    await client.start(phone=phone_number)
    print("Client Created")
    if not await client.is_user_authorized():
        await client.send_code_request(phone_number)
        try:
            await client.sign_in(phone_number, input('Enter the code for ' + phone_number + ': '))
        except SessionPasswordNeededError:
            await client.sign_in(password=input('Password for ' + phone_number + ': '))

async def send_message_from_client1():
    await authorize_client(client1, phone_number_1)
    await asyncio.sleep(5)  # Wait for 5 seconds before sending the message
    await client1.send_message('bushpulbek', 'Салем, есть что')
    await client1.send_message('bushpulbek', 'срочно нужно')

async def send_message_from_client2():
    await authorize_client(client2, phone_number_2)
    await asyncio.sleep(5)
    await client2.send_message('bushpulbek', 'Хай, есть ход')

async def send_message_from_client3():
    await authorize_client(client3, phone_number_3)
    await client3.send_message('bushpulbek', 'Хай, есть что')

async def send_message_from_client4():
    await authorize_client(client4, phone_number_4)
    await asyncio.sleep(12)
    await client4.send_message('bushpulbek', 'Не бар?')

async def send_message_from_client5():
    await authorize_client(client5, phone_number_5)
    await asyncio.sleep(15)
    await client5.send_message('bushpulbek', 'Каншадан?')

async def send_message_from_client6():
    await authorize_client(client6, phone_number_6)
    await asyncio.sleep(18)
    await client6.send_message('bushpulbek', 'че есть')

async def send_message_from_client7():
    await authorize_client(client7, phone_number_7)
    await asyncio.sleep(11)
    await client7.send_message('bushpulbek', 'Срочно нужно?')

async def send_message_from_client8():
    await authorize_client(client8, phone_number_8)
    await asyncio.sleep(12)
    await client8.send_message('bushpulbek', 'Скинь прайс?')

async def main():
    await asyncio.gather(
        send_message_from_client1(),
        send_message_from_client2(),
        send_message_from_client3(),
        send_message_from_client4(),
        send_message_from_client5(),
        send_message_from_client6(),
        send_message_from_client7(),
        send_message_from_client8()

    )

with client1, client2, client3, client4, client5, client6, client7, client8:
    client1.loop.run_until_complete(main())
    