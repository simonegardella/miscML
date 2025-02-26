telegram_token = '7975245244:AAEG_innjJwD_SwLHVMeuiQPjxKsWGU8RjI'

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from okey import *
import  openai
openai.api_key = OPENAI_API_KEY

def gestiscirisposta (domanda):
    risposta = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": domanda
            }
        ]
    )
    print (risposta)

    return risposta['choices'][0]['message']['content']

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    
    risposta = gestiscirisposta (update.message.text)
    await update.message.reply_text(risposta)


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(telegram_token).build()


    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()