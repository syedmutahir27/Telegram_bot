'''
{
   {chat_id1 : { "event1" : ["date","chat_id"],
                "event2" : ["date","chat_id"]
                .....}

    chat_id2 : { "event1" : ["date","chat_id],
                "event2" : ["date","chat_id"]
                .....}
    ....

}
'''
from datetime import datetime
import json
import random

import commands


def timenow():
    '''this function returns current date and time '''
    return datetime.now()

def remindme(context):
    '''this function reminds the current event as well as missed events  '''
    today = timenow()
    with open("reminder.json","r") as f:
        outr_dict = json.load(f)
    d_id =list(outr_dict.keys())
    for user_id in d_id:
        d_innr = outr_dict[user_id]
        d_event = list(d_innr.keys())
        for i_event in d_event:
            d_eventlist = d_innr[i_event]
            d_date = d_eventlist[0]
            d_cid = d_eventlist[1]
            e_date = datetime.strptime(d_date,'%d/%m/%Y')
            ts_event = e_date.timestamp()
            ts_current = today.timestamp()
            if (today.year == e_date.year) and (today.month == e_date.month) and (today.day == e_date.day):
                context.bot.send_message(d_cid, f"@[user](tg://user?id={user_id})  event'{i_event}'today",parse_mode="Markdown")
            elif ts_event < ts_current:
                context.bot.send_message(d_cid,f"@[user](tg://user?id={user_id}) missed event'{i_event}'on {d_date}",parse_mode= "Markdown")

def create_dict(event,date_str,chat_id,user_id):
    '''this function creates as well as updates the dictionary with user id,chat id,event name and event time'''
    with open("reminder.json","r") as f :
        outr_dict=json.load(f)
        user_id = str(user_id)
        chat_id = str(chat_id)

        if user_id in outr_dict.keys():
            innr_dict = outr_dict[user_id]
            print(innr_dict)
            innr_dict.update({event:[date_str,chat_id]})
            outr_dict.update({user_id:innr_dict})
        else:
            innr_dict = {event:[date_str,chat_id]}
            outr_dict.update({user_id:innr_dict})

    with open("reminder.json","w") as f:
        json.dump(outr_dict, f, indent=4)

if __name__ == '__main__':
    remindme("fri")
    #create_dict("mon",'3/10/2022',123,456)
    #print(display)
