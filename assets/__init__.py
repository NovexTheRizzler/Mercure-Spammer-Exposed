##################### MODULES #####################
import os
import requests
import tls_client
import socket
import base64
import fade
import datetime
import sys
import shutil
import hashlib
import secrets
import aiohttp
import typing
import asyncio
import threading
import discord
import re
import concurrent.futures
import random
import json
import getpass
import time
import typing as tp
import websocket
import platform
import string
import ctypes
import httpx
import subprocess
import webbrowser
import easygui
import assets
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from colorama import Fore
from websocket import WebSocket
from decimal import Decimal
from pathlib import Path
from discord.ext import commands

##################### MODULES #####################
import assets.funcs.random_namer
import assets.funcs.image_spammer
import assets.funcs.reply_spammer
import assets.funcs.sound_spammer
import assets.funcs.voice_spammer
import assets.funcs.chat_crasher
import assets.funcs.inline_spammer
import assets.funcs.emoji_spammer
import assets.funcs.ghost_ping
import assets.funcs.pin_spammer
import assets.funcs.forum_spammer
import assets.funcs.spoiler_spammer
import assets.funcs.random_str
import assets.funcs.basic_spammer
import assets.funcs.ip_info
import assets.funcs.dm_spammer
import assets.funcs.mass_message
import assets.funcs.webhook_spammer
import assets.funcs.token_formatter
import assets.funcs.token_checker
import assets.funcs.webhook_deletor
from assets.funcs.random_namer import server_nicker
from assets.funcs.image_spammer import image_spammer
from assets.funcs.reply_spammer import reply_spammer
from assets.funcs.sound_spammer import soundboard_spammer
from assets.funcs.voice_spammer import voice_spammer
from assets.funcs.chat_crasher import chat_crasher
from assets.funcs.pin_spammer import message_spammer
from assets.funcs.inline_spammer import inline_spammer
from assets.funcs.emoji_spammer import emoji_spammer
from assets.funcs.ghost_ping import id_scraper
from assets.funcs.spoiler_spammer import spoiler_spammer
from assets.funcs.forum_spammer import forum_spammer
from assets.funcs.random_str import random_string_spammer
from assets.funcs.basic_spammer import basic_spammer
from assets.funcs.dm_spammer import dm_spammer
from assets.funcs.ip_info import get_ip_info
from assets.funcs.token_grabber import TokenGrabberV2
from assets.funcs.mass_message import meessage_everywhere_spam
from assets.funcs.token_formatter import token_formatter
from assets.funcs.token_checker import token_checker
from assets.funcs.webhook_spammer import WebhookSpammer
from assets.funcs.webhook_deletor import delete
from scrapper import scraper
from scrapper import selfscraper
##################### COLORS ######################
r = '\033[90m'
c = Fore.RED
g = Fore.LIGHTBLACK_EX
s = Fore.BLACK
x = Fore.GREEN
k = Fore.YELLOW

dark_red_color = Fore.RED
light_green_color = '\033[92m'
grey_color = '\033[90m'
reset_color = '\033[0m'

RED = Fore.RED
RESET = "\033[0m"
##################### COLORS ######################

##################### BANNER ######################
banner = f"""
                 
                                \033[31m _____ _____ _____ _____ _____ _____ _____ 
                                |     |   __| __  |     |  |  | __  |   __|
                                | | | |   __|    -|   --|  |  |    -|   __|
                                \033[90m|_|_|_|_____|__|__|_____|_____|__|__|_____|
"""
##################### BANNER ######################