import json

import gif_acess
import pic_acess
import reminder

def start_command(update,context):
    update.message.reply_text('hello there ! I\'m a bot.Nice to meet u!')

def help_command(update,context):
    update.message.reply_text('type anything')

def custom_command(update,context):
    update.message.reply_text('hello there ! custom command!')

def wallpaper_command(update,context):
    resp = update.message.text.replace("/wallpaper","")
    resp = resp.strip()
    if resp =="":
        update.message.reply_text("enter category and orientation separated by '-' after wallpaper command\n"
                                  "orientation are of three types supported by bot\n"
                                  "1.landscape\n"
                                  "2.portrait\n"
                                  "3.squarish\n"
                                  "for example `/wallpaper futuristic-landscape` \n"
                                  "gives you a futuristic landscape wallpaper")
    else:
        resp = resp.split("-")
        category = resp[0]
        orientation = resp[1]
        category = category.strip()
        orientation = orientation.strip()
        orlist=["landscape",'portrait',"squarish"]
        if orientation not in orlist:
            orientation = orlist[0]
        img_dict = pic_acess.get_image(category,orientation)
        #update.message.reply_text(f"powered by unsplash \n"
         #                         f"credtits :{img_dict['author']}")
        context.bot.send_photo( update.effective_chat.id,img_dict['url'])


def gif_command(update,context):
    resp = update.message.text.replace("/gif","")
    resp = resp.strip()
    if resp == "":
        update.message.reply_text("enter category \n"
                                 "for example `/gif excited` \n"
                                "gives u a excited gif")
    else:
        category = resp
        category = category.strip()
        img_dict = gif_acess.get_gif(category)
        context.bot.send_video(update.effective_chat.id, img_dict['url'])


def reminder_command(update,context):
    first_name = update.message.from_user['first_name']
    last_name = update.message.from_user['last_name']
    chat_id = update.message['chat_id']
    print(first_name)
    print(last_name)
    print(chat_id)
    user_id = update.message.from_user['id']
    #update.message.reply_text(f"@[{first_name} {last_name}](tg://user?id={user_id})",parse_mode="Markdown")
    resp = update.message.text.replace("/reminder","")
    resp = resp.strip()
    if resp == "":
        update.message.reply_text("enter event name and  separated by '-' date in 'dd/mm/yyyy' to set a reminder\n"
                                  "for example : exam-03/24/2022")
    else:
        resp = resp.split("-")
        event = resp[0].strip()
        date_str = resp[1].strip()
        reminder.create_dict(event,date_str,chat_id,user_id)
        update.message.reply_text(f"reminder set for {event} on {date_str}")






