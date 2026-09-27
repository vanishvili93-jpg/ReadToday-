import os
import re
import telebot
from telebot import types

BOT_TOKEN = re.sub(r"\s+", "", os.environ["TELEGRAM_BOT_TOKEN"])
WEB_APP_URL = os.environ.get("https://vanishvili93-jpg.github.io/tg-webapp/gb.html", "").strip()

bot = telebot.TeleBot(BOT_TOKEN)

try:
    if WEB_APP_URL:
        bot.set_chat_menu_button(menu_button=types.MenuButtonWebApp(type="web_app", text="Open", web_app=types.WebAppInfo(url=https://vanishvili93-jpg.github.io/tg-webapp/gb.html)))
except Exception as e:
    print("Menu button error: " + str(e))


def open_button():
    if WEB_APP_URL:
        return types.InlineKeyboardButton(text="📰 Open Daily Digest", web_app=types.WebAppInfo(url=WEB_APP_URL))
    return types.InlineKeyboardButton(text="📰 Open Daily Digest", url="https://vanishvili93-jpg.github.io/tg-webapp/gb.html")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Headlines today", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))
    text = ("📰 *Welcome to Daily Digest.*\n\n"
        "Every day a curated selection of culture, "
        "travel, cuisine, science and technology, "
        "to read at your own pace in chat.\n\n"
        "To begin, tap *Headlines today*.")
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "headlines")
def headlines(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(text="🎨 Culture — autumn exhibitions", callback_data="culture"),
        types.InlineKeyboardButton(text="🍳 Cuisine — classic recipes", callback_data="cuisine"),
        types.InlineKeyboardButton(text="🏠 Travel — five hidden villages", callback_data="travel"),
        types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))
    text = ("📋 *Headlines today*\n\n"
        "Three stories selected for today. "
        "Each one complete in chat.\n\n"
        "*Culture* — autumn exhibitions: five "
        "must-visit shows at world-class museums.\n\n"
        "*Cuisine* — classic recipes: four "
        "traditional dishes worth trying.\n\n"
        "*Travel* — five hidden villages to "
        "discover on a long weekend.\n\n"
        "Tap a title to open the full story.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "culture")
def culture(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Headlines today", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))
    text = ("🎨 *Autumn exhibitions: five must-visit shows*\n\n"
        "Museums reopen with a new season.\n\n"
        "*London — modern masters*\n"
        "A major retrospective at the Tate Modern "
        "brings together works from the greatest "
        "painters of the last century. Rare sketches "
        "and unpublished photographs.\n\n"
        "*Paris — impressionism rediscovered*\n"
        "The Musee d'Orsay presents restored "
        "masterpieces with details invisible "
        "for over a century.\n\n"
        "*New York — photography and the city*\n"
        "MoMA hosts black and white reportages "
        "of post-war Manhattan. Documentary "
        "and poetic at once.\n\n"
        "*Tokyo — contemporary sculpture*\n"
        "New installations in the outdoor spaces "
        "of the Mori Art Museum. Works dedicated "
        "to water and light.\n\n"
        "*Rome — Renaissance drawings*\n"
        "Rare notebooks of great masters shown "
        "alongside contemporary works inspired "
        "by the same tradition.\n\n"
        "_Check museum websites for timings._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "cuisine")
def cuisine(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Headlines today", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))
    text = ("🍳 *Classic recipes: four traditional dishes*\n\n"
        "Four recipes from different corners "
        "of the world.\n\n"
        "*Italian risotto*\n"
        "Arborio rice, butter, parmesan and "
        "a good broth. Stir slowly for twenty "
        "minutes. The secret is patience.\n\n"
        "*Thai green curry*\n"
        "Coconut milk, green curry paste, "
        "chicken and Thai basil. Ready in "
        "fifteen minutes. Fresh and fragrant.\n\n"
        "*French onion soup*\n"
        "Caramelised onions, beef broth, "
        "a slice of bread and melted gruyere. "
        "Comfort food at its finest.\n\n"
        "*Japanese miso soup*\n"
        "Dashi stock, white miso paste, tofu "
        "and spring onions. Simple, warm "
        "and ready in five minutes.\n\n"
        "_Adjust quantities to your own taste._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "travel")
def travel(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="📋 Headlines today", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))
    text = ("🏠 *Five hidden villages for a long weekend*\n\n"
        "Away from the crowds, five villages "
        "that reward the unhurried traveller.\n\n"
        "*Hallstatt (Austria)*\n"
        "A lakeside village surrounded by "
        "mountains. Salt mines, pastel houses "
        "and mirror-still water.\n\n"
        "*Colmar (France)*\n"
        "Half-timbered houses along canals. "
        "Wine tastings in Alsace and quiet "
        "cobblestone streets.\n\n"
        "*Reine (Norway)*\n"
        "Red fishing cabins beneath dramatic "
        "peaks. The Lofoten Islands at their "
        "most photogenic.\n\n"
        "*Alberobello (Italy)*\n"
        "Trulli houses with cone-shaped roofs. "
        "A UNESCO site that feels like "
        "a fairy tale.\n\n"
        "*Shirakawa-go (Japan)*\n"
        "Traditional thatched-roof farmhouses "
        "in a mountain valley. Stunning in "
        "every season.\n\n"
        "_Book accommodation in advance._")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "summary")
def summary(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.add(types.InlineKeyboardButton(text="📋 Headlines today", callback_data="headlines"))
    markup.row(types.InlineKeyboardButton(text="📖 Glossary", callback_data="glossary"), types.InlineKeyboardButton(text="❓ FAQ", callback_data="faq"))
    markup.row(types.InlineKeyboardButton(text="✏️ Contact", callback_data="contact"), types.InlineKeyboardButton(text="🏛 About", callback_data="about"))
    text = ("🏛 *Summary*\n\n"
        "From this menu you can:\n\n"
        "• Read *headlines today* and our articles.\n"
        "• Browse sections: Culture, Travel, "
        "Cuisine, Science.\n"
        "• Check the glossary and FAQ.\n"
        "• Learn about us and get in touch.\n\n"
        "For the full edition, use the button.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "glossary")
def glossary(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 Headlines today", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))
    text = ("📖 *A short glossary*\n\n"
        "*Newsroom* — the team that selects "
        "and prepares stories.\n\n"
        "*Editorial* — an opinion piece that "
        "opens a section.\n\n"
        "*Photojournalism* — storytelling built "
        "around photographs.\n\n"
        "*Evergreen content* — stories whose "
        "relevance does not depend on the news "
        "of the day.\n\n"
        "*Correspondent* — a journalist reporting "
        "from the field.\n\n"
        "*Column* — a recurring section dedicated "
        "to a specific topic.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "faq")
def faq(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 Headlines today", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"))
    text = ("❓ *Frequently asked questions*\n\n"
        "*Is this bot official?*\n"
        "Daily Digest is an independent "
        "editorial project.\n\n"
        "*How often is it updated?*\n"
        "The selection is refreshed seasonally.\n\n"
        "*How do I mute notifications?*\n"
        "From Telegram chat settings.\n\n"
        "*Can I share a story?*\n"
        "Yes, using Telegram sharing options.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "contact")
def contact(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"), types.InlineKeyboardButton(text="🏛 About", callback_data="about"))
    text = ("✏️ *Contact*\n\n"
        "For editorial correspondence:\n"
        "• E-mail: hello@dailydigest.com\n\n"
        "*Publisher*\n"
        "Daily Digest Media Ltd.\n"
        "London, United Kingdom\n\n"
        "Reader feedback on working days.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "about")
def about(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.row(types.InlineKeyboardButton(text="🏛 Summary", callback_data="summary"), types.InlineKeyboardButton(text="✏️ Contact", callback_data="contact"))
    text = ("🏛 *About Daily Digest*\n\n"
        "Daily Digest is an independent editorial "
        "project dedicated to culture, travel, "
        "cuisine and technology.\n\n"
        "The editorial team selects quality content "
        "every day for an informed break from "
        "the daily routine.\n\n"
        "This Telegram edition is designed for "
        "comfortable reading in chat.")
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_all(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(open_button())
    markup.add(types.InlineKeyboardButton(text="📋 Headlines today", callback_data="headlines"))
    bot.send_message(message.chat.id, "📰 Welcome! Tap *Headlines today* to begin.", parse_mode="Markdown", reply_markup=markup)


print("Daily Digest Bot is running...")
bot.infinity_polling()
