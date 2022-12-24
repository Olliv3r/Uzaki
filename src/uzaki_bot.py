#!/bin/python3
#
# Por the oliver, novembro de 2020
#
# Versão 1: Adicionadas funçôes 'comandoDesconhecido()', 'novosMembros()', 'listaNegra()', 'regras()', 'cursosAcervos()'
#
#           A função 'comandoDesconhecido()' trata comandos que são inválidos a chatbot,
#           A função 'novosMembros()' recebe os usuários que se juntarem ao grupo
#           A função 'listaNegra()' é responsável por exibir uma lista de palavras que não são permitido a pronúncia
#           A função 'regras()' como o próprio nome diz, é responsável por exibir uma lista contendo regras do grupo
#           A função 'cursosAcervos()' é responsável por exibir uma lista com vários acervos contendo cursos
#
# Versão 2: Adicionada função 'membrosSairem' de despedida do grupo
#
#           A função 'membrosSairem()' é responsável por exibir uma mensagem no grupo de despedida do usuário que decidiu sair ou foi removido pelo adm
#
# Versão 3: Adicionado comando 'get_id' e ação 'digitando...' da chatbot
#
#           A função 'get_id()' responde o usuário com seu id
# Versão 4: Adicionada função 'job_minute()' de envio de aviso periodicamente sobre videos novos ao canal
#
# Objetivo do programa : Gerenciar grupos e canais do telegram
#
#

# Importando módulos necessários para o funcionamento correto do programa
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import telegram
import logging
from random import random
from time import sleep
from logging import INFO, basicConfig, getLogger

from time import localtime

# Importando módulos personalizados
from conf.settings import *

# Registro de log
basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=INFO)
logger = getLogger(__name__)


# Função para responder quando startarem ela
def start(update, context):
    context.bot.sendChatAction(
        chat_id=update.effective_chat.id,
        action=telegram.ChatAction.TYPING
    )
    sleep(random() * 2 + 3.)
    context.bot.sendMessage(
        chat_id=update.effective_chat.id,
        text="Olá {} ;)!".format(update.message.from_user.first_name)
    )

# Função para enviar mensagem de aviso caso o usuário enviar comandos desconhecidos

def comandoDesconhecido(update, context):
    context.bot.sendChatAction(
        chat_id=update.effective_chat.id,
        action=telegram.ChatAction.TYPING
    )
    sleep(random() * 2 + 3.)
    context.bot.sendMessage(
        chat_id=update.effective_chat.id,
        text="{} - Comando não está disponível no momento: {}".format(update.message.from_user.first_name, update.message.text)
    )

# Função para responder novos usuários que se juntarem ao grupo com mensagem de boas vindas
def novosMembros(update, context):
    context.bot.sendChatAction(
        chat_id=update.effective_chat.id,
        action=telegram.ChatAction.TYPING
    )
    sleep(random() * 2 + 3.)
    for usuario in update.message.new_chat_members:
        update.message.reply_text(messageWelcome.format(usuario['first_name']))
        
        # Verificar se o membro não tem nome de usuário
        if not usuario['username'] :
            context.bot.sendMessage(
                chat_id=update.effective_chat.id,
                text=messageRequireUsername.format(usuario['first_name'])
            )
        else:
            return

# Função para responder usuários que partiram do grupo
def membrosSairem(update, context):
    context.bot.sendChatAction(
        chat_id=update.effective_chat.id,
        action=telegram.ChatAction.TYPING
    )
    sleep(random() * 2 + 3.)
    context.bot.sendMessage(
        chat_id=update.effective_chat.id,
        text=messageFarewell
    )

# Função para responder com a lista negra
def listaNegra(update, context):
    context.bot.sendChatAction(
        chat_id=update.effective_chat.id,
        action=telegram.ChatAction.TYPING
    )
    sleep(random() * 2 + 3.)
    context.bot.sendMessage(
        chat_id=update.effective_chat.id,
        text=messageBlacklist.format(update.message.from_user.first_name)
    )

    
# Função para responder com as regras
def regras(update, context):
    context.bot.sendChatAction(
        chat_id=update.effective_chat.id,
        action=telegram.ChatAction.TYPING
    )
    sleep(random() * 2 + 3.)
    context.bot.sendMessage(
        chat_id=update.effective_chat.id,
        text=messageRules.format(update.message.from_user.first_name)
    )
    
# Função para responder com os cursos & acervos
def cursosAcervos(update, context):
    context.bot.sendChatAction(
        chat_id=update.effective_chat.id,
        action=telegram.ChatAction.TYPING
    )
    sleep(random() * 2 + 3.)

    context.bot.sendMessage(
        chat_id=update.effective_chat.id,
        text=messageAcervosCursos.format(update.message.from_user.first_name, update.message.chat_id)
    )

# Função para responder com o id do usuário
def get_id(update, context):
    context.bot.sendChatAction(
        chat_id=update.effective_chat.id,
        action=telegram.ChatAction.TYPING
    )
    sleep(random() * 2 + 3.)

    context.bot.sendMessage(
        chat_id=update.effective_chat.id,
        text=messageChatId.format(update.message.from_user.first_name, update.message.chat_id)
    )


def termux(update, context):
    context.bot.sendChatAction(
	chat_id=update.effective_chat.id,
	action=telegram.ChatAction.TYPING
    )
    sleep(random() * 2 + 3.)

    context.bot.sendMessage(
	chat_id=update.effective_chat.id,
	text=messageTermuxVersion.format(update.message.from_user.first_name, update.message.chat_id)
    )

# Token de acesso
updater = Updater(token=TOKEN, use_context=True)

# Função principal
def main():

    # Dispachante
    dispatcher = updater.dispatcher

    # handler start
    handler_start = CommandHandler("start", start)

    # Dispachar handler_start
    dispatcher.add_handler(handler_start)

    # handler novosMembros
    handler_novosMembros = MessageHandler(Filters.status_update.new_chat_members, novosMembros)
    # Dispachar handler_novosMembros
    dispatcher.add_handler(handler_novosMembros)

    # handler membrosSairem
    handler_membrosSairem = MessageHandler(Filters.status_update.left_chat_member, membrosSairem)
    # Dispachar handler_mombrosSairem
    dispatcher.add_handler(handler_membrosSairem)

    # handler termux
    handler_termux = CommandHandler("termux", termux)
    # Dispachar termux
    dispatcher.add_handler(handler_termux) 

    # handler regras
    handler_regras = CommandHandler("rules", regras)
    # Dispachar handler_regras
    dispatcher.add_handler(handler_regras)

    # handler listaNegra
    handler_listaNegra = CommandHandler("blacklist", listaNegra)
    # Dispachar handler_listaNegra
    dispatcher.add_handler(handler_listaNegra)

    # handler cursosAcervos
    handler_cursosAcervos = CommandHandler("courses", cursosAcervos)
    # Dispachar handler_cursosAcervos
    dispatcher.add_handler(handler_cursosAcervos)

    # handler_get_id
    handler_get_id = CommandHandler("get_id", get_id)
    # Dispachar get_id
    dispatcher.add_handler(handler_get_id)

    # handler comandoDesconhecido
    handler_comandoDesconhecido = MessageHandler(Filters.command, comandoDesconhecido)
    # Dispachar handler_comandoDesconhecido
    dispatcher.add_handler(handler_comandoDesconhecido)
    
    updater.start_polling()
    updater.idle()
    
if __name__ == "__main__" :
    print("Chatbot acordada")
    try:
        main()
    except telegram.error.NetworkError:
        print("ERRO NA CONEXÃO COM A INTERNET")

