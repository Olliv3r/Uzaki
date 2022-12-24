#!/bin/python3
# settings.py
#
# Por the oliver, 26 de novembro
#
# Versão : ?
#
# Objetivo do programa : carregar as variáveis de ambiente

# Importando módulos necessários para o funcionamento do programa
import os
import dotenv

dotenv.load_dotenv()

TOKEN = os.getenv('API_TOKEN')
messageWelcome = os.getenv('welcome')
messageFarewell = os.getenv('farewell')
messageRules = os.getenv('rules')
messageUnknown = os.getenv('unknown')
messageBlacklist = os.getenv('blacklist')
messageTermuxVersion = os.getenv('termuxMessage');
messageAcervosCursos = os.getenv('acervosCursos')
messageRequireUsername = os.getenv('requireUsername')

messageChatId = os.getenv('chatId')
