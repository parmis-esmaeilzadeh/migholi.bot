import telebot
from config import API_TOKEN
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import sqlite3

bot = telebot.TeleBot(API_TOKEN)

conn = sqlite3.connect('Namebot.db', check_same_thread=False)
cur = conn.cursor()


# cur.execute(
#     "CREATE TABLE IF NOT EXISTS Stray_Kids(id INTEGER PRIMARY KEY,name text,murl text,photo text,message_audio text)")
# cur.execute(
#     "CREATE TABLE IF NOT EXISTS BTS(id INTEGER PRIMARY KEY,name text,murl text,photo text,message_audio text)")
# cur.execute(
#     "CREATE TABLE IF NOT EXISTS Imagine_Dragons(id INTEGER PRIMARY KEY,name text,murl text,photo text,message_audio text)")
# cur.execute(
#     "CREATE TABLE IF NOT EXISTS Billie_Eilish(id INTEGER PRIMARY KEY,name text,murl text,photo text,message_audio text)")
# cur.execute(
#     "CREATE TABLE IF NOT EXISTS BLACKPINK(id INTEGER PRIMARY KEY,name text,murl text,photo text,message_audio text)")
#
# conn.commit()

# sk = """
# INSERT INTO Stray_Kids VALUES (1,"Chk Chk Boom", "https://dl.baarzesh.net/2024/07/Stray_Kids_Chk_Chk_Boom.mp3","https://vectorloo.com/wp-content/uploads/edd/2023/07/%D9%88%DA%A9%D8%AA%D9%88%D8%B1-%D9%85%DB%8C%D9%82%D9%88%D9%84%DB%8C-%D8%AF%D8%B1-%D8%AD%D8%A7%D9%84-%DA%AF%DB%8C%D8%AA%D8%A7%D8%B1-%D8%B2%D8%AF%D9%86-1.webp");
# INSERT INTO Stray_Kids VALUES (2,"LALALALA", "https://dl.baarzesh.net/2023/10/stray_kids_lalalala.mp3","https://vectorloo.com/wp-content/uploads/edd/2023/07/%D9%88%DA%A9%D8%AA%D9%88%D8%B1-%D9%85%DB%8C%D9%82%D9%88%D9%84%DB%8C-%D8%A8%D8%A7-%D8%AF%D9%85%D9%BE%D8%A7%DB%8C%DB%8C-1.webp");
# INSERT INTO Stray_Kids VALUES (3,"TOPLINE", "https://dl.baarzesh.net/2023/06/Stray_Kids_TOPLINE.mp3","https://vectorloo.com/wp-content/uploads/edd/2023/07/%D9%88%DA%A9%D8%AA%D9%88%D8%B1-%D9%85%DB%8C%D9%82%D9%88%D9%84%DB%8C-%D8%B1%DB%8C%D8%A7%D8%B6%DB%8C-1.webp");
# INSERT INTO Stray_Kids VALUES (4,"S-Class", "https://dl.baarzesh.net/2023/06/Stray_Kids_S_Class.mp3","https://vectorloo.com/wp-content/uploads/edd/2023/07/%D9%88%DA%A9%D8%AA%D9%88%D8%B1-%D9%85%DB%8C%D9%82%D9%88%D9%84%DB%8C-%D8%AF%D8%B1-%D8%AD%D8%A7%D9%84-%DA%86%D8%A7%DB%8C%DB%8C-%D8%AE%D9%88%D8%B1%D8%AF%D9%86-1.webp");
# """
# cur.executescript(sk)

#stray kids--------------------------------------------------
@bot.callback_query_handler(func=lambda call: call.data == 'Stray_Kids')
def view(call):
    cur.execute("SELECT * from Stray_Kids")
    sk0 = cur.fetchall()
    if sk0:
        for record in sk0:
            print(record)
            message_name = record[1]
            message_murl = record[2]
            message_photo = record[3]
            message_audio = record[4]
            # bot.send_photo(call.message.chat.id, message_photo,
            #                caption=(f"name :\n {message_name} \n link :\n{message_murl}"),
            #                )
            audio = open(message_audio, 'rb')
            # Send the MP3 file to the user
            bot.send_audio(call.message.chat.id, audio, title=message_name)


#BTS-----------------------------------------------------
@bot.callback_query_handler(func=lambda call: call.data == 'BTS')
def view1(call):
    cur.execute("SELECT * from BTS")
    sk0 = cur.fetchall()
    if sk0:
        for record in sk0:
            print(record)
            message_name = record[1]
            message_murl = record[2]
            message_photo = record[3]
            message_audio = record[4]
            #bot.send_photo(call.message.chat.id, message_photo,
            #               caption=(f"name :\n {message_name} \n link :\n{message_murl}"),
            #               )
            audio = open(message_audio, 'rb')
            # Send the MP3 file to the user
            bot.send_audio(call.message.chat.id, audio, title=message_name)

#Imagine_Dragons---------------------------------------------------------
@bot.callback_query_handler(func=lambda call: call.data == 'Imagine_Dragons')
def view32(call):
    cur.execute("SELECT * from Imagine_Dragons")
    sk0 = cur.fetchall()
    if sk0:
        for record in sk0:
            print(record)
            message_name = record[1]
            message_murl = record[2]
            message_photo = record[3]
            message_audio = record[4]
            #bot.send_photo(call.message.chat.id, message_photo,
            #               caption=(f"name :\n {message_name} \n link :\n{message_murl}"),
            #               )
            audio = open(message_audio, 'rb')
            # Send the MP3 file to the user
            bot.send_audio(call.message.chat.id, audio, title=message_name)

#Billie_Eilish--------------------------------------------------------------
@bot.callback_query_handler(func=lambda call: call.data == 'Billie_Eilish')
def view21(call):
    cur.execute("SELECT * from Billie_Eilish")
    sk0 = cur.fetchall()
    if sk0:
        for record in sk0:
            print(record)
            message_name = record[1]
            message_murl = record[2]
            message_photo = record[3]
            message_audio = record[4]
            #bot.send_photo(call.message.chat.id, message_photo,
            #               caption=(f"name :\n {message_name} \n link :\n{message_murl}"),
            #               )
            audio = open(message_audio, 'rb')
            # Send the MP3 file to the user
            bot.send_audio(call.message.chat.id, audio, title=message_name)

#BLACKPINK------------------------------------------------------------------------
@bot.callback_query_handler(func=lambda call: call.data == 'Billie_Eilish')
def view2(call):
    cur.execute("SELECT * from BLACKPINK")
    sk0 = cur.fetchall()
    if sk0:
        for record in sk0:
            print(record)
            message_name = record[1]
            message_murl = record[2]
            message_photo = record[3]
            message_audio = record[4]
            #bot.send_photo(call.message.chat.id, message_photo,
            #               caption=(f"name :\n {message_name} \n link :\n{message_murl}"),
            #               )
            audio = open(message_audio, 'rb')
            # Send the MP3 file to the user
            bot.send_audio(call.message.chat.id, audio, title=message_name)

#     if photo:
#         bot.send_photo(call.message.chat.id, photo, caption=message_text, parse_mode='Markdown')
#     else:
#         bot.send_message(call.message.chat.id, message_text, parse_mode='Markdown')
# else:
#     bot.send_message(call.message.chat.id, "?????")


# Command handler for /sendmp3
# @bot.message_handler(commands=['sendmp3'])
# def send_mp3(message):
#     # Replace 'yourfile.mp3' with the path to your MP3 file
#     audio = open('yourfile.mp3', 'rb')
#
#     # Send the MP3 file to the user
#     bot.send_audio(message.chat.id, audio, title="Sample MP3")
def main_menu():
    markup = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton(text="K-pop music", callback_data="K-pop music")
    b2 = InlineKeyboardButton(text="Pop music", callback_data="Pop music")
    b3 = InlineKeyboardButton(text="Rock & Roll music", callback_data="Rock & Roll music")
    b4 = InlineKeyboardButton(text="Rap music", callback_data="Rap music")
    markup.add(b1, b2, b3, b4)

    return markup


def submenu1():
    markup = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton('Stray Kids', callback_data='Stray_Kids')

    button2 = InlineKeyboardButton('BTS', callback_data='BTS')

    button3 = InlineKeyboardButton('BLACKPINK', callback_data='BLACKPINK')

    return_button = InlineKeyboardButton('Return', callback_data='return_to_main')
    markup.add(button1, button2, button3, return_button)
    return markup


def submenu2():
    markup = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton('Billie Eilish', callback_data='Billie_Eilish')
    button2 = InlineKeyboardButton('...', callback_data='submenu1-2')
    return_button = InlineKeyboardButton('Return', callback_data='return_to_main')
    markup.add(button1, button2, return_button)
    return markup


def submenu3():
    markup = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton('...', callback_data='submenu1-1')
    button2 = InlineKeyboardButton('Imagine Dragons', callback_data='Imagine_Dragons')
    return_button = InlineKeyboardButton('Return', callback_data='return_to_main')
    markup.add(button1, button2, return_button)
    return markup


def submenu4():
    markup = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton('...', callback_data='submenu1-1')
    button2 = InlineKeyboardButton('...', callback_data='submenu1-2')
    return_button = InlineKeyboardButton('Return', callback_data='return_to_main')
    markup.add(button1, button2, return_button)
    return markup


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,
                     "welcome to SONG bot ... :)\nin this bot you can find your favorite song's!\nHow can I help you?",
                     reply_markup=main_menu())
    # bot.reply_to(message,"wow this song is wonderful 😍")
    # bot.register_next_step_handler(message, process_song)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'K-pop music':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="You are in K-pop singer's menu", reply_markup=submenu1())
        if call.data == 'Stray_Kids':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="music's", reply_markup=view())

        elif call.data == 'BTS':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="music's", reply_markup=view1())

        elif call.data == 'BLACKPINK':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="music's", reply_markup=view2())

    elif call.data == 'Pop music':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="You are in Pop singer's menu", reply_markup=submenu2())
        if call.data == 'Stray_Kids':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="music's", reply_markup=view21())

    elif call.data == 'Rock & Roll music':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="You are in Rock & Roll singer's menu", reply_markup=submenu3())
        if call.data == 'Imagine_Dragons':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="music's", reply_markup=view32())

    elif call.data == 'Rap music':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="You are in Rap singer's menu", reply_markup=submenu4())
    elif call.data == 'return_to_main':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="You are in main menu. Choose an option:", reply_markup=main_menu())


# @bot.callback_query_handler(func=lambda message: True)
# def chek_button(call):
#     if call.data == "btn1":
#         bot.answer_callback_query(call.id,"K-pop music selected.",show_alert=True)
#     elif call.data == "btn2":
#         bot.answer_callback_query(call.id,"Pop selected.",show_alert=True)
#     elif call.data == "btn3":
#         bot.answer_callback_query(call.id,"Rock & Roll music selected.",show_alert=True)
#     elif call.data == "btn4":
#         bot.answer_callback_query(call.id, "Rap music selected.", show_alert=True)
#     elif call.data == "btn5":
#         bot.answer_callback_query(call.id, "Movie and series songs selected.", show_alert=True)
#     elif call.data == "btn6":
#         bot.answer_callback_query(call.id, "Iranian songs selected.", show_alert=True)


# def process_song(message):
#     song = message.text
#     if song=="chk chk Boom":
#         bot.send_message(message.chat.id,f"{song}:\n{Chk_Chk_Boom}")
#     elif song=="lalalala":
#         bot.send_message(message.chat.id,f"{song}:\n{LALALALA}")
#     elif song=="topline":
#         bot.send_message(message.chat.id,f"{song}:\n{TOPLINE}")
#     elif song=="s-class":
#         bot.send_message(message.chat.id,f"{song}:\n{SClass}")
#     elif song=="hall of fame":
#         bot.send_message(message.chat.id,f"{song}:\n{Hall_of_Fame}")
#     elif song=="item":
#         bot.send_message(message.chat.id,f"{song}:\n{ITEM}")
#     elif song=="super bowl":
#         bot.send_message(message.chat.id,f"{song}:\n{Super_Bowl}")
#     elif song=="dlc":
#         bot.send_message(message.chat.id,f"{song}:\n{DLC}")
#     elif song=="collision":
#         bot.send_message(message.chat.id,f"{song}:\n{Collision}")
#     elif song=="fnf":
#         bot.send_message(message.chat.id,f"{song}:\n{FNF}")
#     elif song=="youtiful":
#         bot.send_message(message.chat.id,f"{song}:\n{Youtiful}")
#     else:
#         pass


####################################

@bot.message_handler(commands=['help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, "welcome to SONG bot \n"
                                      "you can find your favorite song's in this bot \n"
                                      "for find your favorite song you need to know only the name of song.\n"
                                      "this is wonderful I know...\nwell you can type the name of that song and get that song in 1 second")


bot.polling()
