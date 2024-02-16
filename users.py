import os
import re
import random
import string
import config
from asyncio import sleep, create_task, get_event_loop
from sys import argv
from mody.Keyboards import subs, video_url
from mody.Edit import ed, ib, ch
from pyrogram import Client, filters, idle
from pyrogram.enums import ChatType
from pyrogram.errors import FloodWait, YouBlockedUser, ChannelsTooMuch
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.async_telebot import AsyncTeleBot
from datetime import date
from mody.Redis import db
from info import sudo_id, token

bot = AsyncTeleBot(token)

userbot = Client(
    f'users/user:{argv[1][:15]}',
    22867191,
    '2c5fdc151fc2b1d93f41e734e20eceda',
    session_string=argv[1]
)


async def getInfo():
    return await bot.get_me(), \
        await bot.get_chat(sudo_id)


async def lf(_, __, msg):
    if msg.text:
        if '?' in msg.text:
            return False
    return True


bot.me, sudo_info = get_event_loop().run_until_complete(getInfo())


userbot.send_log = lambda text: \
    bot.send_video(sudo_info.id, video_url, caption=f"- You have a new message ✉️\n\n𖡋 𝐈𝐃 ⌯ {userbot.me.id}\n𖡋 𝐏𝐡𝐨𝐧𝐞 ⌯ +{userbot.me.phone_number}\n𖡋 𝐃𝐀𝐓𝐄 ⌯ {date.today()}\n\n{text}", reply_markup=subs)

getvp = lambda bot_id, owner_id: 1000 \
    if not db.get(f'{bot_id}:{owner_id}:points') else int(db.get(f'{bot_id}:{owner_id}:points'))

async def auto_delete_link():
    while not await sleep(36000):
        for msg in db.smembers(f'{bot.me.id}:{userbot.me.id}:click'):
            msg = msg.split(':')
            await userbot.request_callback_answer(
                chat_id=msg[0],
                message_id=msg[1],
                callback_data=msg[2]
            )

async def delete_userbot():
    while not await sleep(5):
        if db.sismember(f'{bot.me.id}:{sudo_info.id}:delete_userbot', userbot.me.id):
            db.srem(f'{bot.me.id}:{sudo_info.id}:delete_userbot', userbot.me.id)
            db.srem(f'{bot.me.id}:{sudo_info.id}:idbots', userbot.me.id)
            db.srem(f'{bot.me.id}:{sudo_info.id}:sessions', userbot.session_string)
            db.srem(f'{config.APP_NEAM}:{sudo_info.id}:sessions', userbot.session_string)
            db.set(f'{bot.me.id}:{userbot.me.id}:points', 0) 
            await userbot.stop()
            try:
                os.remove(userbot.name)
            except:
                pass
            await userbot.send_log('⌯ The account has been deleted 💥')
            exit()
        if db.get(f'{sudo_info.id}:end'):
            await userbot.stop()
            try:
                os.remove(userbot.name)
            except:
                pass
            exit()            

async def tumblr_userbot():
    while not await sleep(5):
        if db.sismember(f'{bot.me.id}:{sudo_info.id}:tumblr', userbot.me.id):
            db.srem(f'{bot.me.id}:{sudo_info.id}:tumblr', userbot.me.id)
            try:
                path = "path"
                new_bio = random.choice(ib)
                new_neam = random.choice(ed)
                new_user = ''.join(random.choice(string.ascii_letters) for _ in range(8))
                image_files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
                if image_files:
                    random_image = random.choice(image_files)
                    full_path_to_image = os.path.join(path, random_image)
                    await userbot.set_profile_photo(photo=full_path_to_image)
                await userbot.update_profile(first_name=new_neam, bio=new_bio)
                await userbot.update_profile(last_name="")
                await userbot.set_username(new_user)
            except:
                pass

async def auto_gift_in_bot():
    while not await sleep(5):
        if not db.get(f'{bot.me.id}:{userbot.me.id}:stop'):
            if db.sismember(f'{bot.me.id}:{sudo_info.id}:pgt', userbot.me.id):
                try:
                    await userbot.send_message(db.get(f'{bot.me.id}:{userbot.me.id}:user'), '/start')
                except YouBlockedUser:
                    await userbot.unblock_user(db.get(f'{bot.me.id}:{userbot.me.id}:user'))
                    await sleep(0.5)
                    await userbot.send_message(db.get(f'{bot.me.id}:{userbot.me.id}:user'), '/start')
                except Exception as e:
                    print(e)
                    pass

async def auto_start_in_bot():
    while not await sleep(120):
        if db.get(f'{bot.me.id}:{userbot.me.id}:user'):
            if not db.get(f'{bot.me.id}:{userbot.me.id}:stop'):
                try:
                    await userbot.send_message(db.get(f'{bot.me.id}:{userbot.me.id}:user'), '/start')
                except YouBlockedUser:
                    await userbot.unblock_user(db.get(f'{bot.me.id}:{userbot.me.id}:user'))
                    await sleep(0.5)
                    await userbot.send_message(db.get(f'{bot.me.id}:{userbot.me.id}:user'), '/start')
                except Exception as e:
                    print(e)
                    pass

async def auto_us_bot():
    while not await sleep(5):
        usbot = db.get(f'{bot.me.id}:{userbot.me.id}:user')
        if db.sismember(f'{bot.me.id}:{sudo_info.id}:ud', userbot.me.id):
            db.srem(f'{bot.me.id}:{sudo_info.id}:ud', userbot.me.id)
            db.set(f'{bot.me.id}:{userbot.me.id}:points', 0) 
            try:
                await userbot.send_message(usbot, '/start')
            except YouBlockedUser:
                if not db.get(f'{bot.me.id}:{userbot.me.id}:stop'):
                    await userbot.unblock_user(usbot)
                    await sleep(0.5)
                    await userbot.send_message(usbot, '/start')
            except Exception as e:
                print(e)
                pass
        if db.sismember(f'{bot.me.id}:{sudo_info.id}:ban_bot', userbot.me.id):
            db.srem(f'{bot.me.id}:{sudo_info.id}:ban_bot', userbot.me.id)
            try:
                await userbot.block_user(usbot)
            except:
                pass

async def auto_chat():
    while not await sleep(10):   
        if db.sismember(f'{bot.me.id}:{sudo_info.id}:join_chat', userbot.me.id):
            db.srem(f'{bot.me.id}:{sudo_info.id}:join_chat', userbot.me.id)
            try:
                await join_chat(userbot, db.get(f'{bot.me.id}:{sudo_info.id}:chat'), bot.me.id)
            except:
                pass
        if db.sismember(f'{bot.me.id}:{sudo_info.id}:le_chat', userbot.me.id):
            db.srem(f'{bot.me.id}:{sudo_info.id}:le_chat', userbot.me.id)
            try:
                await leave_chat(userbot, db.get(f'{bot.me.id}:{sudo_info.id}:chat'))
            except:
                pass            
        if db.sismember(f'{bot.me.id}:{sudo_info.id}:leave_all', userbot.me.id):
            db.srem(f'{bot.me.id}:{sudo_info.id}:leave_all', userbot.me.id)
            try:
                async for dialog in userbot.get_dialogs():
                    if dialog.chat.type != ChatType.PRIVATE:
                        if dialog.chat.username in ["D_4_V", "D_5_V", "xxStitch", "wewantyoutodothejob"]:
                            continue 
                        if db.sismember(f'{bot.me.id}:{sudo_info.id}:research', dialog.chat.username):
                            continue
                        try:
                            await userbot.leave_chat(dialog.chat.id, delete=True)
                        except:
                            pass
            except:
                pass   

async def invitation_bot():
    while not await sleep(10):
        if db.sismember(f'{bot.me.id}:{sudo_info.id}:invitation', userbot.me.id):
            db.srem(f'{bot.me.id}:{sudo_info.id}:invitation', userbot.me.id)
            usar = db.get(f'{bot.me.id}:{sudo_info.id}:user_invitation')
            code = db.get(f'{bot.me.id}:{sudo_info.id}:code_invitation')
            try:
                await userbot.send_message(usar, f'/start {code}')
            except:
                pass

async def click_button_bot():
    while not await sleep(10):
        if db.sismember(f'{bot.me.id}:{sudo_info.id}:click_button', userbot.me.id):
            db.srem(f'{bot.me.id}:{sudo_info.id}:click_button', userbot.me.id)
            vx = db.get(f'{bot.me.id}:{sudo_info.id}:vote')
            msg = vx.split(':')
            try:
                await join_chat(userbot, msg[0], bot.me.id)
                message = await userbot.get_messages(msg[0], int(msg[1]))
                if isinstance(message.reply_markup, InlineKeyboardMarkup):
                    await message.click(0)
            except Exception as e:
                print(e)
                pass    

async def send_messages(user_id, msg_text, dwwwe, weet_duration, posty_count):
    for _ in range(posty_count):
        if db.sismember(f'{bot.me.id}:{sudo_info.id}:spste', user_id):
            break
        await userbot.send_message(dwwwe, msg_text)
        await sleep(weet_duration)

async def sotsw_bot():
    while not await sleep(5):
        if db.sismember(f'{bot.me.id}:{sudo_info.id}:pste', userbot.me.id):
            db.srem(f'{bot.me.id}:{sudo_info.id}:pste', userbot.me.id)
            user_id = userbot.me.id
            msg_text = db.get(f'{bot.me.id}:{sudo_info.id}:msg')
            weet_duration = int(db.get(f'{bot.me.id}:{sudo_info.id}:weccet'))
            posty_count = int(db.get(f'{bot.me.id}:{sudo_info.id}:posty'))
            dwwwe = db.get(f'{bot.me.id}:{sudo_info.id}:setwds')

            await send_messages(user_id, msg_text, dwwwe, weet_duration, posty_count)

async def join_chat(c, link, bot_id):
    try:
        if '+' in link or 'joinchat' in link:
            await c.join_chat(link)
        else:
            await c.join_chat(link.replace('https://t.me/', ''))
    except FloodWait as e:
        await c.send_log(f'⌯ Ban from collecting {e.value} for a second 👾')
        if e.value >= 99999:
            db.set(f'{bot.me.id}:{c.me.id}:get_all_points', '3yad')
            await c.send_message(bot_id, '/start')
        db.setex(f'{bot.me.id}:{userbot.me.id}:stop', e.value + 10, '3yad')
        await sleep(e.value + 10)
        await c.send_log('⌯ Unblock and start collecting 🥳')
    except ChannelsTooMuch:    
        await userbot.send_log('⌯ The account max of channels ⚠️')
        db.setex(f'{bot.me.id}:{userbot.me.id}:stop', 36000, '3yad')
    except Exception as e:
        print(e)

async def leave_chat(c, link):
    try:
        await c.leave_chat(link.replace('https://t.me/', ''))
    except Exception as e:
        print(e)

@userbot.on_message(
    filters.bot & (filters.regex('بوت تمويل العرب') or filters.regex('تابع قناة البوت نوزع بيها هدايا يومية')) & filters.private)
async def handle_first_message(c, msg):
    if db.sismember(f'{bot.me.id}:{sudo_info.id}:pgt', c.me.id):
        await gift_in_bot(c, msg)
    else:   
        mc_value = 1
        await start_in_bot(c, msg, mc_value)

@userbot.on_message(
    filters.bot & (filters.regex('ـ في بوت تمويل المليار ➕🤖') or filters.regex('والمجموعات عن طريق التجميع النقاط')) & filters.private)
async def handle_second_message(c, msg):
    if db.sismember(f'{bot.me.id}:{sudo_info.id}:pgt', c.me.id):
        await gift_in_bot(c, msg)
    else:   
        mc_value = 25
        await start_in_bot(c, msg, mc_value)

@userbot.on_message(
    filters.bot & (filters.regex('بوت تمويل مهدويون³¹³ ⚜️.') or filters.regex('•┊-اجميع النقاط وصعد قناتك مجاناً✅')) & filters.private)
async def handle_first_message(c, msg):
    if db.sismember(f'{bot.me.id}:{sudo_info.id}:pgt', c.me.id):
        await gift_in_bot(c, msg)
    else:   
        mc_value = 25
        await start_in_bot(c, msg, mc_value)

@userbot.on_message(
    filters.bot & (filters.regex('في بوت تمويل قنوات ومجموعات التيليجرام :🔰') or filters.regex('✳️︙يمكن التحكم بالبوت')) & filters.private)
async def handle_first_message(c, msg):
    if db.sismember(f'{bot.me.id}:{sudo_info.id}:pgt', c.me.id):
        await gift_in_bot(c, msg)
    else:   
        mc_value = 1
        await start_in_bot(c, msg, mc_value)

async def gift_in_bot(c, msg):
    try:
        await sleep(1)
        db.srem(f'{bot.me.id}:{sudo_info.id}:pgt', c.me.id)
        await c.request_callback_answer(
                chat_id=msg.chat.id,
                message_id=msg.id,
                callback_data=msg.reply_markup.inline_keyboard[4][0].callback_data
            )
        await sleep(1)    
    except:
        pass
    if not db.get(f'{bot.me.id}:{c.me.id}:stop'):
        try:
            await c.send_message(db.get(f'{bot.me.id}:{c.me.id}:user'), '/start')
        except:
            pass

async def start_in_bot(c, msg, mc):
    points = int(msg.reply_markup.inline_keyboard[0][0].text.split(': ')[1])
    db.set(f'{bot.me.id}:{c.me.id}:points', points)
    if points >= 100:
        if (points >= getvp(bot.me.id, sudo_info.id) or
            db.get(f'{bot.me.id}:{c.me.id}:get_all_points')) and \
                not db.get(f'{bot.me.id}:{c.me.id}:whit_for_time'):
            await c.send_log(f'⌯ {points - mc} points are being transferred to you 😃')
            try:
                await c.request_callback_answer(
                    chat_id=msg.chat.id,
                    message_id=msg.id,
                    callback_data='sendtocount'
                )
            except:
                pass
            await sleep(1)
            await msg.reply(points - mc)
            return
    if not db.get(f'{bot.me.id}:{userbot.me.id}:stop'):
        try:
            await c.request_callback_answer(
                chat_id=msg.chat.id,
                message_id=msg.id,
                callback_data='col'
            )
        except:
            pass
        await sleep(1)
        try:
            await c.request_callback_answer(
                chat_id=msg.chat.id,
                message_id=msg.id,
                callback_data='col3'
            )
        except:
            pass

@userbot.on_message(
    filters.bot & filters.regex('مرحبا بك في بوت DomKom 👋') & filters.private)
async def start_dm_bot(c, msg):
    if not db.get(f'{bot.me.id}:{userbot.me.id}:stop'):
        match = re.search(r'👥] نقاطك : (\d+)', msg.text)
        points = int(match.group(1))
        db.set(f'{bot.me.id}:{c.me.id}:points', points)
        pointsid = f'{sudo_id}'
        if points >= 100:
            if (points >= getvp(bot.me.id, sudo_info.id) or
                db.get(f'{bot.me.id}:{c.me.id}:get_all_points')) and \
                    not db.get(f'{bot.me.id}:{c.me.id}:whit_for_time'):
                await c.send_log(f'⌯ {points - 30} points are being transferred to you 😃')
                try:
                    await sleep(3)
                    await c.request_callback_answer(
                        chat_id=msg.chat.id,
                        message_id=msg.id,
                        callback_data=msg.reply_markup.inline_keyboard[2][1].callback_data
                    )
                    await sleep(3)
                except:
                    pass
                await sleep(1)
                await msg.reply(pointsid)
                await sleep(1)
                await msg.reply(points - 30)
                return
        if not db.get(f'{bot.me.id}:{userbot.me.id}:stop'):
            try:
                await c.request_callback_answer(
                    chat_id=msg.chat.id,
                    message_id=msg.id,
                    callback_data=msg.reply_markup.inline_keyboard[1][0].callback_data
                )
            except:
                pass

@userbot.on_edited_message(filters.bot & filters.regex('✳️ تجميع نقاط') & filters.private)
async def start_dom_bot(c, msg): 
    if not db.get(f'{bot.me.id}:{userbot.me.id}:stop'):
        if db.sismember(f'{bot.me.id}:{sudo_info.id}:pgt', c.me.id):
            db.srem(f'{bot.me.id}:{sudo_info.id}:pgt', c.me.id)
            await sleep(4)
            await c.request_callback_answer(chat_id=msg.chat.id,message_id=msg.id,callback_data=msg.reply_markup.inline_keyboard[2][0].callback_data)
            return await c.send_message(db.get(f'{bot.me.id}:{c.me.id}:user'), '/start')
        await sleep(3)
        try:
            await c.request_callback_answer(
                chat_id=msg.chat.id,
                message_id=msg.id,
                callback_data=msg.reply_markup.inline_keyboard[0][0].callback_data
            )
        except:
            pass

@userbot.on_edited_message(filters.bot & filters.regex('اشترك في ') & filters.private)
async def join_chats(c, msg):  # تجميع نقاط الاشتراك
    if not db.get(f'{bot.me.id}:{userbot.me.id}:stop'):
        await sleep(1)
        await join_chat(c, msg.reply_markup.inline_keyboard[0][0].url, msg.chat.id)
        await sleep(1)
        try:
            await c.request_callback_answer(
                chat_id=msg.chat.id,
                message_id=msg.id,
                callback_data=msg.reply_markup.inline_keyboard[1][0].callback_data
            )
            match = re.search(r'• نقاطك الحاليه : (\d+)', msg.text)
            point = int(match.group(1))
            db.set(f'{bot.me.id}:{c.me.id}:points', point)        
        except:
            pass

@userbot.on_edited_message(filters.bot & filters.regex('اشترك فالقناة') & filters.private)
async def joind_chats(c, msg):  # تجميع نقاط الاشتراك
    if not db.get(f'{bot.me.id}:{userbot.me.id}:stop'):
        await sleep(3)
        ay = ''
        for lin in msg.text.split('\n'):
            if '@' in lin:
                ay = lin
                break
        if not ay:
            return
        link = '@' + ay.split('@')[1]
        if ' ' in link:
            link = link.split(' ')[0]
        await join_chat(c, link, msg.chat.id)
        await sleep(0.5)
        try:
            await c.request_callback_answer(
                chat_id=msg.chat.id,
                message_id=msg.id,
                callback_data=msg.reply_markup.inline_keyboard[0][0].callback_data
            )
        except:
            pass

@userbot.on_message(filters.bot & filters.regex("بواسطه رابط التحويل الخاص بك") & filters.private)
async def block_and_leave_all(c, msg):
    await c.block_user(msg.chat.id)
    if db.get(f'{bot.me.id}:{userbot.me.id}:block_and_leave'):
        async for dialog in c.get_dialogs():
            if dialog.chat.type != ChatType.PRIVATE:
                if dialog.chat.username in ["D_4_V", "D_5_V", "xxStitch", "wewantyoutodothejob"]:
                    continue 
                if db.sismember(f'{bot.me.id}:{sudo_info.id}:research', dialog.chat.username):
                    continue
                try:
                    await c.leave_chat(dialog.chat.id, delete=True)
                except:
                    pass
    if db.get(f'{bot.me.id}:{sudo_info.id}:points_ban'):
        banb = db.get(f'{bot.me.id}:{sudo_info.id}:points_ban')
    else: 
        banb = 43200
    db.setex(f'{bot.me.id}:{c.me.id}:stop', int(banb), '3yad')
    db.set(f'{bot.me.id}:{c.me.id}:points', 0)            

@userbot.on_message(filters.bot & filters.regex("👤 تم ارسال") & filters.private)
async def block_and_leave_all(c, msg):
    await c.block_user(msg.chat.id)
    async for dialog in c.get_dialogs():
        if dialog.chat.type != ChatType.PRIVATE:
            if dialog.chat.username in ["D_4_V", "D_5_V", "xxStitch", "wewantyoutodothejob"]:
                continue 
            if db.sismember(f'{bot.me.id}:{sudo_info.id}:research', dialog.chat.username):
                continue
            try:
                await c.leave_chat(dialog.chat.id, delete=True)
            except:
                pass
    db.setex(f'{bot.me.id}:{c.me.id}:stop', 120, '3yad')    
    db.set(f'{bot.me.id}:{c.me.id}:points', 0) 

@userbot.on_message(filters.bot & filters.regex('https://t.me/(.*)?start=(.*)') & filters.private)
async def cpab(c, msg):  # نقل النقاط
    ay = ''
    for lin in msg.text.split('\n'):
        if 't.me' in lin:
            ay = lin
            break
    if not ay:
        return
    link = 'http' + ay.split('http')[1]
    db.delete(f'{bot.me.id}:{c.me.id}:get_all_points')
    url = link.replace('https://t.me/', '').split('?start=')
    db.sadd(f'{bot.me.id}:{sudo_info.id}:links', f'{msg.chat.id}:{url[1]}')
    db.sadd(f'{bot.me.id}:{c.me.id}:click',
            f'{msg.chat.id}:{msg.id}:{msg.reply_markup.inline_keyboard[0][0].callback_data}')

@userbot.on_message(filters.bot & filters.regex('تم حظرك لمده دقيقه بسبب التكرار') & filters.private)
async def stop1m(c, msg):
    db.setex(f'{bot.me.id}:{c.me.id}:stop', 60, '3yad')

@userbot.on_edited_message(filters.bot & filters.regex('لا يوجد قنوات في الوقت الحالي') & filters.private)
async def stopbssm(c, msg):
    db.setex(f'{bot.me.id}:{c.me.id}:stop', 120, '3yad')

@userbot.on_edited_message(filters.bot & filters.regex('لا يوجد قنوات حالياً 🤍') & filters.private)
async def stopbssd(c, msg):
    db.setex(f'{bot.me.id}:{c.me.id}:stop', 120, '3yad') 

@userbot.on_message(filters.bot & filters.regex('يجب ان نتحقق من انك لست روبوت') & filters.private)
async def send_contact(c, msg):  # ارسال جها الاتصال للتحقق
    get_me = await c.get_me()
    await c.send_contact(
        msg.chat.id,
        get_me.phone_number,
        first_name=get_me.first_name,
        last_name=get_me.last_name,
        reply_to_message_id=msg.id
    )

# الاشتراك الاجباري
@userbot.on_message(filters.bot & filters.regex('https://t.me/') & filters.create(lf) & filters.private)
async def ctct3bot(c, msg):  # الاشتراك الاجباري
    if not db.get(f'{bot.me.id}:{userbot.me.id}:stop'):
        ay = ''
        for lin in msg.text.split('\n'):
            if 't.me' in lin:
                ay = lin
                break
        if not ay:
            return
        link = 'http' + ay.split('http')[1]
        if ' ' in link:
            link = link.split(' ')[0]
        await join_chat(c, link, msg.chat.id)
        await sleep(1)
        await c.send_message(msg.chat.id, '/start')

@userbot.on_message(filters.bot & filters.regex('يجب عليك الاشتراك بقناة البوت اولاً') & filters.create(lf) & filters.private)
async def ctc1dbot(c, msg):  # الاشتراك الاجباري
    if not db.get(f'{bot.me.id}:{userbot.me.id}:stop'):
        ay = ''
        for lin in msg.text.split('\n'):
            if '@' in lin:
                ay = lin
                break
        if not ay:
            return
        link = '@' + ay.split('@')[1]
        if ' ' in link:
            link = link.split(' ')[0]
        await join_chat(c, link, msg.chat.id)
        await sleep(1)
        await c.send_message(msg.chat.id, '/start')

@userbot.on_message(filters.bot & filters.regex('🚸| لطفاً أخي:🖤') & filters.create(lf) & filters.private)
async def ctc2nbot(c, msg):  # الاشتراك الاجباري
    if not db.get(f'{bot.me.id}:{userbot.me.id}:stop'):
        ay = ''
        for lin in msg.text.split('\n'):
            if 't.me' in lin:
                ay = lin
                break
        if not ay:
            return
        link_match = re.search(r't.me/(\S+)', ay)
        if link_match:
            link = link_match.group(1)
            await join_chat(c, link, msg.chat.id)
            await sleep(1)
            await c.send_message(msg.chat.id, '/start')       

@userbot.on_message(filters.bot & filters.regex('تم التحقق') & filters.private)
async def send_start_to_bot(c, m):
    return await c.send_message(m.chat.id, '/start')

@userbot.on_edited_message(filters.bot & filters.regex('لا يمكنك تحويل نقاط الان') & filters.private)
async def a_re_send(c: userbot, msg):
    s = re.findall(r"انتضر (.+):(.+):(.+) واعد", msg.text)[0]
    s_time = int(s[0]) * 60 * 60 + int(s[1]) * 60 + int(s[2])
    db.setex(f'{bot.me.id}:{c.me.id}:whit_for_time', s_time, '3yad')
    await c.send_log(f'⌯ لا يستطيع تحويل النقاط لانه جديد')

async def research_userbot():
    while not await sleep(60):
        if db.sismember(f'{bot.me.id}:{sudo_info.id}:research', userbot.me.id):
            db.srem(f'{bot.me.id}:{sudo_info.id}:research', userbot.me.id)
            try:
                if db.get(f'{bot.me.id}:{sudo_info.id}:sleep'):
                    banb = db.get(f'{bot.me.id}:{sudo_info.id}:sleep')
                else: 
                    banb = 2  
                for user in db.smembers(f'{bot.me.id}:{sudo_info.id}:usernames'): 
                    posty_count = db.get(f'{bot.me.id}:{user}:posty_count')
                    try:
                        await join_chat(userbot, user)
                    except:
                        pass
                    try:
                        for _ in range(int(posty_count)):
                            msg = random.choice(ch)
                            await userbot.send_message(user, msg) 
                            await sleep(int(banb)) 
                    except:
                        pass 

@userbot.on_message(filters.regex('请选择图片对应的文字👇👇👇'))
async def start_message(c, msg): 
    await sleep(3)
    await c.request_callback_answer(chat_id=msg.chat.id,message_id=msg.id,callback_data=msg.reply_markup.inline_keyboard[0][0].callback_data)

@userbot.on_edited_message(filters.regex('请选择图片对应的文字👇👇👇'))
async def start_edited(c, msg): 
    await sleep(3)
    await c.request_callback_answer(chat_id=msg.chat.id,message_id=msg.id,callback_data=msg.reply_markup.inline_keyboard[0][0].callback_data)

async def main():
    await userbot.start()
    create_task(auto_start_in_bot())
    create_task(auto_gift_in_bot())
    create_task(auto_us_bot())
    create_task(sotsw_bot())
    create_task(auto_chat())
    create_task(invitation_bot())
    create_task(click_button_bot())
    create_task(tumblr_userbot())
    create_task(delete_userbot())
    create_task(auto_delete_link()) 
    create_task(research_userbot()) 
    if not db.sismember(f'{bot.me.id}:{sudo_info.id}:idbots', userbot.me.id):
        db.sadd(f'{bot.me.id}:{sudo_info.id}:idbots', userbot.me.id) 
        db.set(f'{userbot.me.id}:ph', userbot.me.phone_number)
        try:
            await userbot.send_log('⌯ Start collecting ✅')
        except Exception as e:
            print(e)
    if db.get(f'{bot.me.id}:{userbot.me.id}:user'):
        if not db.get(f'{bot.me.id}:{userbot.me.id}:stop'):
            try:
                await userbot.send_message(db.get(f'{bot.me.id}:{userbot.me.id}:user'), '/start')
            except YouBlockedUser:
                await userbot.unblock_user(db.get(f'{bot.me.id}:{userbot.me.id}:user'))
                await sleep(0.5)
                await userbot.send_message(db.get(f'{bot.me.id}:{userbot.me.id}:user'), '/start')  
    await idle()
    await userbot.stop()

get_event_loop().run_until_complete(main())