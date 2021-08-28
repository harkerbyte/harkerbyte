const Telegraf = require('telegraf');

const bot = new Telegraf('1969279863:AAF-4vEZjTW-j2sGyYyyOLuYDaO2NoFqph0');

import csv, io

test_data = [[1, 2, 3], ["please", "follow", "me"]]

# csv module can write data in io.StringIO buffer only
s = io.StringIO()
csv.writer(s).writerows(test_data)
s.seek(0)

# python-telegram-bot library can send files only from io.BytesIO buffer
# we need to convert StringIO to BytesIO
buf = io.BytesIO()

# extract csv-string, convert it to bytes and write to buffer
buf.write(s.getvalue().encode())
buf.seek(0)

# set a filename with file's extension
buf.name = f'secret_report_for_cool_guys.csv'

# send the buffer as a regular file
context.bot.send_document(chat_id=update.message.chat_id, document=buf)
