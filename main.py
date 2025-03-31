import telebot import undetected_chromedriver as uc from selenium.webdriver.common.by import By import time import os

Get bot token and user ID from Railway environment variables

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") USER_ID = int(os.getenv("USER_ID"))

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN) driver = None

Start Bot Command

@bot.message_handler(commands=['start']) def start_bot(message): if message.chat.id != USER_ID: bot.reply_to(message, "Unauthorized access.") return bot.reply_to(message, "Starting Pocket Option bot...") start_trading()

def start_trading(): global driver driver = uc.Chrome() driver.get("https://pocketoption.com/en/cabinet/demo-account/") time.sleep(5) bot.send_message(USER_ID, "Log in manually and type /trade to start trading.")

@bot.message_handler(commands=['trade']) def trade(message): if message.chat.id != USER_ID: bot.reply_to(message, "Unauthorized access.") return

bot.reply_to(message, "Executing trade...")
execute_trade()

def execute_trade(): global driver try: buy_button = driver.find_element(By.XPATH, "//button[contains(@class, 'trade-button__call')]") buy_button.click() bot.send_message(USER_ID, "Trade placed successfully!") except Exception as e: bot.send_message(USER_ID, f"Error placing trade: {str(e)}")

Stop Bot Command

@bot.message_handler(commands=['stop']) def stop_bot(message): global driver if message.chat.id != USER_ID: bot.reply_to(message, "Unauthorized access.") return

bot.reply_to(message, "Stopping bot...")
if driver:
    driver.quit()

Run the bot

bot.polling()


