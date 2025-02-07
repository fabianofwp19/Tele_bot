import telebot
import time
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Import loader and bot starter
from utils.env_loader import load_env
from utils.bot_starter import iniciar_bot

# Load API key
API_KEY = load_env()

# Inicia API key
bot = telebot.TeleBot(API_KEY)

# /start
@bot.message_handler(commands=["start"])
def start_command(message):
    text = (   
        "🤖 **Bem-vindo ao Meu Primeiro Bot!**\n\n"
        "Estou aqui para tornar sua experiência com logs na nuvem mais simples, rápida e eficiente.\n\n"
        "Com recursos interativos e fáceis de usar, você pode gerenciar informações e consultar logs sem complicação.\n\n"
        "🚀 **O que eu posso fazer por você?**\n"
        "- 📌 **Consultas Rápidas**: Acesse logs instantaneamente com um clique.\n"
        "- 🔒 **Segurança e Confiabilidade**: Gerencie suas informações com total segurança.\n"
        "- ⚡ **Facilidade de Uso**: Interface intuitiva para uma experiência fluida e prática.\n\n"
        "👨‍💻 Criado por [fabianofwp19](https://github.com/fabianofwp19). Faça parte da comunidade e explore todas as possibilidades!"
    )



    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Sobre", callback_data="sobre"))
    markup.add(InlineKeyboardButton("Comandos", callback_data="comandos"))
    markup.add(InlineKeyboardButton("GitHub Oficial", url="https://github.com/fabianofwp19"), InlineKeyboardButton("Criador", url="https://t.me/Thazfwp_bot"))

    bot.send_message(message.chat.id, text, reply_markup=markup, parse_mode='Markdown')


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
   
    

    if call.data == "sobre":
        sobre_markup = InlineKeyboardMarkup()
        sobre_markup.add(InlineKeyboardButton("Voltar", callback_data="voltar"))
        sobre_text = (
            "Com este bot, você tem a liberdade de criar e personalizar sua própria experiência. 🔧\n\n"
            "🎯 **Principais Recursos**:\n"
            "- Adicione novas funções conforme necessário.\n"
            "- Crie e personalize botões interativos.\n"
            "- Modifique textos, mensagens e crie respostas exclusivas para os usuários.\n\n"
            "💡 Este bot é altamente flexível, permitindo que você adapte as interações e funcionalidades ao seu gosto!\n"
            "Seja para automatizar processos, facilitar consultas ou criar comandos personalizados, o Telegram_Interactive_Button faz tudo isso e muito mais!\n\n"
            "🚀 **Por que escolher o Telegram_Interactive_Button?**\n"
            "- Rápido e eficiente na recuperação de logs e informações.\n"
            "- Fácil de personalizar e expandir.\n"
            "- Perfeito para integrar funções na nuvem às tarefas diárias.\n\n"
            "Orgulhosamente criado por [fabianofwp19!](https://github.com/fabianofwp19). Explore e descubra o poder da personalização!"
        )

        bot.edit_message_text(sobre_text, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=sobre_markup, parse_mode='Markdown')

    elif call.data == "comandos":
        comandos_markup = InlineKeyboardMarkup()
        comandos_markup.add(InlineKeyboardButton("/start", callback_data="start_command"))
        comandos_markup.add(InlineKeyboardButton("/comandos", callback_data="comandos_comando"))
        comandos_markup.add(InlineKeyboardButton("Voltar", callback_data="voltar"))
        bot.edit_message_text("Aqui estão os comandos disponíveis:", chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=comandos_markup)

    elif call.data == "start_command":
        start_markup = InlineKeyboardMarkup()
        start_markup.add(InlineKeyboardButton("Voltar", callback_data="comandos"))
        bot.edit_message_text("O comando /start permite iniciar o bot", chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=start_markup)

    elif call.data == "comandos_comando":
        comandos_comand_markup = InlineKeyboardMarkup()
        comandos_comand_markup.add(InlineKeyboardButton("Voltar", callback_data="comandos"))
        bot.edit_message_text("O comando /comandos exibe os comandos disponíveis.", chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=comandos_comand_markup)

    elif call.data == "voltar":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        start_command(call.message)

# /comandos
@bot.message_handler(commands=['comandos'])
def lista_comandos(message):
    response = (
        "📋 *Comandos Disponíveis:*\n\n"
        "`/start` - Inicia o bot e exibe os módulos disponíveis.\n"
        "`/comandos` - Mostra esta lista de comandos.\n"
    )

    bot.reply_to(message, response, parse_mode='Markdown')
   
comandos_validos =[
# Lista de comandos válidos
    "/start", "/comandos"
]

# Captura de comandos válidos
@bot.message_handler(func=lambda message: message.text.startswith('/') and not message.text.split()[0] in comandos_validos)
def invalid_command(message):
    response = bot.reply_to(message, "Este comando não existe. Digite /comandos para ver quais comandos você pode usar. Esta mensagem será apagada em 10 segundos")
    time.sleep(10)

    try:
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        bot.delete_message(chat_id=response.chat.id, message_id=response.message_id)
    except Exception as e:
        print(f"Erro ao tentar apagar mensagens: {e}")

if __name__ == '__main__':
    iniciar_bot(bot)
