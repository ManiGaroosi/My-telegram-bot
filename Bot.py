import telebot

bot = telebot.TeleBot("5865831239:AAFj-XiJIUJkvT1m-Apyv3ZybTnPf8FQTUw")

mainKeyboard= telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
mainKeyboard.add('بسته های موجود🛍','خرید بسته🛒','پشتیبانی📞','استعلام حجم باقی مانده🔋','دانلود برنامه📥')

@bot.message_handler(commands=['start'])
def first_message(message):
    bot.send_message(message.chat.id , 'خوش آمدید . چه کمکی می تونیم بکنم؟', reply_markup=mainKeyboard)

@bot.message_handler()
def main_ketboard(message):
        if message.text == 'خرید بسته🛒':
            bot.send_message(message.chat.id , """
برای خرید بسته ابتدا مبلغ را به شماره کارت :
6037 9975 0571 2688

به اسم :
مانی گروسی 

واریز کرده و رسید آن را به @ULinternet_admin ارسال کنید 

⭕️توجه : مبلغ پرداخت شده حتما باید جزو بسته های موجود باشد .  رسید حتما باید به آیدی بالا ارسال شود⭕️
                    """)
        elif message.text == 'بسته های موجود🛍':
            bot.send_message(message.chat.id , """
《 تعرفه سرویس های (آلمان 🇩🇪 ) 》

پر سرعت 🚀   با امنیت بالا 💣

حجمی 🔋               
یک‌ماهه 

۱ ماهه ۱۵ گیگ ۵۰ هزار تومان
۱ ماهه ۳۰ گیگ ۸۰ هزار تومان 
۱ ماهه ۴۵ گیگ  ۹۰ هزار تومان 
۱ ماهه ۶۵ گیگ ۱۳۰ هزار تومان 
۱ ماهه ۹۰ گیگ ۱۷۰ هزار تومان 
〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️

بسته های نامحدود(۳ کاربره) ♾

۱ ماهه نامحدود ۱۹۰ هزار تومان 
۲ ماهه نامحدود ۲۱۰ هزار تومان 
۳ ماهه نامحدود ۳۳۰ هزار تومان 

〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️
▫️توجه : سرویس های حجمی هیچگونه محدودیت کاربری نداره به هرچند نفر خواستید می تونید اشتراک بگذارید . با همه اپراتور ها سازگار و عملکرد خوبی داره . ▫️

جهت خرید :
@ULinternet_admin 


Join us: 《@unlimitedinternetIR》
""")
        elif message.text == 'استعلام حجم باقی مانده🔋':
            bot.send_message(message.chat.id, "بزودی فعال می شود")

        elif message.text == 'دانلود برنامه📥':
            btn1 = telebot.types.InlineKeyboardButton("دانلود v2rayNG برنامه اندروید", url='https://t.me/unlimitedinternetIR/14')
            btn2 = telebot.types.InlineKeyboardButton("دانلود برنامه V2raN ویندوز", url='https://t.me/unlimitedinternetIR/77')
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(btn1,btn2)
            bot.send_message(message.chat.id, "طبق سیستم عمال مورد نظر خود برنامه را دانلود کنید (سیستم عامل ایفون باید از خود اپل استور دانلود شود)",reply_markup=markup)
             

bot.infinity_polling()
