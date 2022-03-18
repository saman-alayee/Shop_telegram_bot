import logging
from telegram.ext import Updater, CommandHandler, filters
from telegram import ReplyKeyboardMarkup, chataction, message
from telegram import Update
from telegram.ext import MessageHandler
from telegram.ext import Updater, CommandHandler, updater
from telegram import Update
from telegram.ext import MessageHandler
from telegram.ext import CallbackContext
from telegram import  Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from telegram.ext.filters import Filters




#########################################################################

# MAKE YOUR BOT IN @BOTFATHER AND SAVE TOKEN
# INSTALL pip install python-telegram-bot
# REPLACE TOKEN IN LINE 225

#########################################################################


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
          
total_price = {}
tedad = 0
Wallet = {}
Wallet2 = {}
sabad = {}
prices = {
"ROG_PHONE5" : 2800000,
"APPLE_11PRO" : 3300000,
"XIOMI_9S" : 800000,
"SAMSUNG_S20" : 2700000,
"huawei_p30" : 1000000
}

total_price2 ={}
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(' بات فروشگاهی خوش امدید در منو پایین خدمات مورد نظر خود را انتخاب کنید لطفا یک گزینه از منو زیر انتخاب کنید')
    chat_id = update.message.chat_id
    fullname = update.message.from_user.full_name
    logging.info("({} - {}) وارد ربات شد.".format(fullname, chat_id))
    
    sabad[chat_id] = []
    Wallet[chat_id] = 0
    Wallet2[chat_id] = 0
    total_price[chat_id] = 0
    total_price2[chat_id] = 0
    


    
def guide(update: Update, context: CallbackContext):
    update.message.reply_text('این بات برای پروزه ساخت بات دانشگاه سمنان درست شده است و از کتابخانه python telegram bot استفاده شده است')

###############################################################################################################################################



##########################################################################################################################

def menu(update: Update, context: CallbackContext):
        Keyboard = ReplyKeyboardMarkup([['سبد خرید'], ['محصولات'], [
            'شارژ حساب'],   ['کد تخفیف ها']], one_time_keyboard=False, resize_keyboard=True)
        update.message.reply_text("لطفا از منو گزینه مورد نظر خود انتخاب کنید :", reply_markup=Keyboard)
#######################################################################################################################333
def menu2(update: Update, context: CallbackContext):       
        if update.message.text == "محصولات" :
          Keyboard = ReplyKeyboardMarkup([['SAMSUNG S20 '], ['APPLE 11PRO', 'XIOMI 9S'], [
            'HUAWEI P30', 'ROG PHONE 5'], ['بازگشت ']], one_time_keyboard=False, resize_keyboard=True)
          update.message.reply_text(" محصول مورد نظر خود را انتخاب کنید . در صورت تمایل با زدن گزینه بازگشت به منو اصلی برمگیدرد:", reply_markup=Keyboard)
######################################################################################################################33333333      
def menu21(update: Update, context: CallbackContext):
          if update.message.text == "SAMSUNG S20" :
            Keyboard = ReplyKeyboardMarkup([['اضافه کردن sam به سبد خرید '],['بازگشت  ']] ,
             one_time_keyboard=False, resize_keyboard=True)
            update.message.reply_text(f" گوشی SAMSUNG S20    تعداد موجود :0  \n :   2700000 :قیمت\n برای توضیحات بیشتر به لینک زیر مراجعه کنید.\n https://www.zoomit.ir/product/samsung-galaxy-s20/ ", reply_markup=Keyboard)
############################################################################################################################## 
def menu22(update: Update, context: CallbackContext):
          if update.message.text == "APPLE 11PRO" :
             Keyboard = ReplyKeyboardMarkup([['اضافه کردنapple به سبد خرید'],['بازگشت  ']] ,
              one_time_keyboard=False, resize_keyboard=True)
             update.message.reply_text(f" گوشی APPLE 11PRO    تعداد موجود :6   \n    3300000 :قیمت\n برای توضیحات بیشتر به لینک زیر مراجعه کنید.\n https://www.zoomit.ir/product/apple-iphone-11-pro/ ", reply_markup=Keyboard)
##########################################################################################################################3##
def menu23(update: Update, context: CallbackContext):
          if update.message.text == "XIOMI 9S" :
            Keyboard = ReplyKeyboardMarkup([['اضافه کردن xiomi به سبد خرید '],['بازگشت  ']] ,
             one_time_keyboard=False, resize_keyboard=True)
            update.message.reply_text(f" گوشی XIOMI 9S    تعداد موجود :18   \n 800000 :قیمت\n برای توضیحات بیشتر به لینک زیر مراجعه کنید.\n https://www.zoomit.ir/product/xiaomi-redmi-note-9s/ ", reply_markup=Keyboard)
#############################################################################################################################################
def menu24(update: Update, context: CallbackContext):
          if update.message.text == "HUAWEI P30" :
            Keyboard = ReplyKeyboardMarkup([['اضافه کردن HUAWEI به سبد خرید '], [' بازگشت  ']] ,
            one_time_keyboard=False, resize_keyboard=True)
            update.message.reply_text(f" گوشی HUAWEI P30    تعداد موجود :13   \n 1000000 :قیمت\n برای توضیحات بیشتر به لینک زیر مراجعه کنید.\n https://www.zoomit.ir/product/huawei-p30/ ", reply_markup=Keyboard)
#############################################################################################################################################
def menu25(update: Update, context: CallbackContext):
          if update.message.text == "ROG PHONE 5" :
            Keyboard = ReplyKeyboardMarkup([['اضافه کردن rog به سبد خرید '],['بازگشت  ']] ,
            one_time_keyboard=False, resize_keyboard=True)
            update.message.reply_text(f" گوشی ROG PHONE 5    تعداد موجود :0\n "  + "  2800000 :قیمت\n برای توضیحات بیشتر به لینک زیر مراجعه کنید.\n https://www.zoomit.ir/product/asus-rog-phone-5/ ", reply_markup=Keyboard)
#############################################################################################################################################
def add_sam(update: Update, context: CallbackContext):
  

  if update.message.text == "اضافه کردن sam به سبد خرید":                                               
      update.message.reply_text("کالا موجود نمی باشد")
     
def add_rog(update: Update, context: CallbackContext):
    
    if update.message.text == "اضافه کردن rog به سبد خرید":
      update.message.reply_text("کالا موجود نمی باشد")
     
def add_xiomi(update: Update, context: CallbackContext):
    
    if update.message.text == "اضافه کردن xiomi به سبد خرید":
      chat_id = update.message.chat_id
      sabad[chat_id].append("XIOMI_9S")                                                
      update.message.reply_text("کالا با موفقیت وارد سبد شما شد")
      total_price[chat_id] += prices["XIOMI_9S"]
def add_apple(update: Update, context: CallbackContext):
    if update.message.text == "اضافه کردنapple به سبد خرید":
      chat_id = update.message.chat_id
      sabad[chat_id].append("huawei_p30")                                                
      update.message.reply_text("کالا با موفقیت وارد سبد شما شد")
      total_price[chat_id] += prices["huawei_p30"]
def add_HUAWEI(update: Update, context: CallbackContext):
    if update.message.text == "اضافه کردن HUAWEI به سبد خرید":
      chat_id = update.message.chat_id
      sabad[chat_id].append("huawei_p30")                                                
      update.message.reply_text("کالا با موفقیت وارد سبد شما شد")
      total_price[chat_id] += prices["huawei_p30"]
      
####################################################################################################################################3
def removeall1(update: Update, context: CallbackContext):
    if update.message.text == "پاک کردن سبد خرید":
      sabad.clear()                                                
      update.message.reply_text("کالا با موفقیت حذف شد")
      update.message.reply_text(f"سبد خرید : {sabad}")


######################################################################################################################################
def menu3(update: Update, context: CallbackContext):
        if update.message.text == "کد تخفیف ها" :
            Keyboard = ReplyKeyboardMarkup([['بازگشت']], one_time_keyboard=False, resize_keyboard=True)
            update.message.reply_text("کد تخفیف شماره 1 \n نام : 1400 \n 20% :درصد \n تعداد نامحدود  \n \n کد تخفیف شماره 2 \n نام : saman \n درصد :30 % \n نامحدود \n\n کد تخفیف شماره 3 \n نام : bot \n درصد : 25 \n تعداد نامحدود  \n نام کد مورد نظر را وارد کنید 👇 :" , reply_markup=Keyboard)


def code_1400(update: Update, context: CallbackContext):
      chat_id = update.message.chat_id
      if update.message.text == '1400' :
              total_price[chat_id] = total_price[chat_id] * (80/100)
              update.message.reply_text("کد تخفیف با موفقیت اعمال شد")

def code_saman(update: Update, context: CallbackContext):
      chat_id = update.message.chat_id
      if update.message.text == 'saman' :
              total_price[chat_id] = total_price[chat_id] * (70/100)         
              update.message.reply_text("کد تخفیف با موفقیت اعمال شد")
              
def code_bot(update: Update, context: CallbackContext):
      chat_id = update.message.chat_id
      if update.message.text == 'bot' :
              total_price[chat_id] = total_price[chat_id] * (75/100)         
              update.message.reply_text("کد تخفیف با موفقیت اعمال شد")
###############################################################################################################################33          
def menu4(update: Update, context: CallbackContext):
      
        if update.message.text == "شارژ حساب" :
            fullname = update.message.from_user.full_name
            Keyboard = ReplyKeyboardMarkup([['بازگشت'],['پنج میلیون'],['ده میلیون'],
            ['بیست میلیون'],['سی میلیون']], one_time_keyboard=False, resize_keyboard=True)
            update.message.reply_text(f'سلام {fullname}\nموجودی حساب شما بر حساب تومان  :{Wallet2}\n شما میتوانید با وارد کردن دکمه مبلغ مورد نظر حساب خود را شارژ کنید ', reply_markup=Keyboard)  
def menu41(update: Update, context: CallbackContext): 
          chat_id = update.message.chat_id
          global Wallet2
          if update.message.text == "پنج میلیون" :
            chat_id = update.message.chat_id
            Wallet2[chat_id] = Wallet[chat_id] + 5000000
            Keyboard = ReplyKeyboardMarkup([['بازگشت  ']], one_time_keyboard=False, resize_keyboard=True)
            update.message.reply_text(f"موجودی شما {Wallet2[chat_id]}"   ,reply_markup=Keyboard)         
          elif update.message.text == "ده میلیون" :
            chat_id = update.message.chat_id
            Wallet2[chat_id] = Wallet[chat_id] + 10000000
            Keyboard = ReplyKeyboardMarkup([['بازگشت  ']], one_time_keyboard=False, resize_keyboard=True)
            update.message.reply_text(f"موجودی شما {Wallet2[chat_id]}"   ,reply_markup=Keyboard) 
          elif update.message.text == "بیست میلیون" :
            chat_id = update.message.chat_id
            Wallet2[chat_id] = Wallet[chat_id] + 20000000
            Keyboard = ReplyKeyboardMarkup([['بازگشت  ']], one_time_keyboard=False, resize_keyboard=True)
            update.message.reply_text(f"موجودی شما {Wallet2[chat_id]}"   ,reply_markup=Keyboard) 
          elif update.message.text == "سی میلیون" :
            chat_id = update.message.chat_id
            Wallet2[chat_id] = Wallet[chat_id] + 30000000
            Keyboard = ReplyKeyboardMarkup([['بازگشت  ']], one_time_keyboard=False, resize_keyboard=True)
            update.message.reply_text(f"موجودی شما {Wallet2[chat_id]}"   ,reply_markup=Keyboard)

####################################################################################################################
def sabadd(update: Update, context: CallbackContext):
   if update.message.text == "سبد خرید" :
     chat_id = update.message.chat_id
     Keyboard = ReplyKeyboardMarkup([['نهایی کردن خرید'], ['پاک کردن سبد خرید'],['بازگشت']], one_time_keyboard=False, resize_keyboard=True)
     update.message.reply_text(f"{sabad[chat_id]} سبد خرید شما:",reply_markup=Keyboard)
     update.message.reply_text(f"{total_price[chat_id]} هزینه قابل پرداخت:",reply_markup=Keyboard)   
def finish(update: Update, context: CallbackContext):
          chat_id = update.message.chat_id
          update.message.reply_text(f"رسید به شرح زیر می باشد :\n نام محصولات :{sabad[chat_id]} \n تعداد : {len(sabad[chat_id])} \n  هزینه پرداخت شده : {total_price}" )
          if update.message.text == "نهایی کردن خرید" :
                if Wallet2[chat_id] >= total_price[chat_id] :
                      fullname = update.message.from_user.full_name
                      logging.info("({} - {} - {} - {}).".format(fullname, chat_id,sabad, total_price))
                      Wallet2[chat_id] -= total_price[chat_id]
                      total_price[chat_id] -= total_price[chat_id] 
                      sabad[chat_id].clear()
                      update.message.reply_text("خرید شما انجام شد" )
                      
                      
                else:
                      update.message.reply_text("موجودی شما کافی نمیباشد")
            
            



###########################################################################################
def main():
    
    updater = Updater("TOKEN")
    dp = updater.dispatcher
   
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("guide", guide))
    dp.add_handler(CommandHandler("menu", menu))
    dp.add_handler(MessageHandler(Filters.regex("محصولات"), menu2))
    dp.add_handler(MessageHandler(Filters.regex("کد تخفیف ها"), menu3))
    dp.add_handler(MessageHandler(Filters.regex("شارژ حساب"), menu4))
    dp.add_handler(MessageHandler(Filters.regex("SAMSUNG S20"), menu21))
    dp.add_handler(MessageHandler(Filters.regex("APPLE 11PRO"), menu22))
    dp.add_handler(MessageHandler(Filters.regex("XIOMI 9S"), menu23))
    dp.add_handler(MessageHandler(Filters.regex("HUAWEI P30"), menu24))
    dp.add_handler(MessageHandler(Filters.regex("ROG PHONE 5"), menu25))
    dp.add_handler(MessageHandler(Filters.regex(" بازگشت به محصولات"), menu2))
    dp.add_handler(MessageHandler(Filters.regex("بازگشت"), menu))
    dp.add_handler(MessageHandler(Filters.regex("پنج میلیون"), menu41))
    dp.add_handler(MessageHandler(Filters.regex("ده میلیون"), menu41))
    dp.add_handler(MessageHandler(Filters.regex("بیست میلیون"), menu41))
    dp.add_handler(MessageHandler(Filters.regex("سی میلیون"), menu41))
    dp.add_handler(MessageHandler(Filters.regex("اضافه کردن rog به سبد خرید"), add_rog))
    dp.add_handler(MessageHandler(Filters.regex("اضافه کردن sam به سبد خرید"), add_sam))
    dp.add_handler(MessageHandler(Filters.regex("اضافه کردن xiomi به سبد خرید"), add_xiomi))
    dp.add_handler(MessageHandler(Filters.regex("اضافه کردنapple به سبد خرید"), add_apple))
    dp.add_handler(MessageHandler(Filters.regex("اضافه کردن HUAWEI به سبد خرید"), add_HUAWEI))
    dp.add_handler(MessageHandler(Filters.regex("پاک کردن سبد خرید"), removeall1))
    dp.add_handler(MessageHandler(Filters.regex("1400"), code_1400))
    dp.add_handler(MessageHandler(Filters.regex("saman"), code_saman)) 
    dp.add_handler(MessageHandler(Filters.regex("bot"), code_bot))



   
    
    dp.add_handler(MessageHandler(Filters.regex("سبد خرید"), sabadd))
    dp.add_handler(MessageHandler(Filters.regex("نهایی کردن خرید"), finish))
    
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
   