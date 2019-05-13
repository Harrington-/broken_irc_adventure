import operator
import random
from collections import defaultdict
from threading import Lock
from time import time, sleep

from sqlalchemy import Boolean, Column, Integer, PrimaryKeyConstraint, String, Table, and_, desc
from sqlalchemy.sql import select

from cloudbot import hook
from cloudbot.event import EventType
from cloudbot.util import database
from cloudbot.util.formatting import pluralize_auto, truncate
from cloudbot.util.func_utils import call_with_args

table = Table(
    'broken_adventure_users',
    database.metadata,
    Column('nick', String),
    Column('quests', String),
    Column('deaths', String),
    Column('active_adventure', Boolean),
    Column('active_quest', Boolean),
    PrimaryKeyConstraint('name')
)

@hook.command("startadventure")
def start_adventure(nick, db):
    adventure_details = initialize_adventure_details(nick, db)
    return adventure_details

@hook.command("quitadventure")
def quit_adventure(nick, db):
    adventure_details = forfeit_adventure(nick, db)
    return adventure_details


    
def initialize_adventure_details(nick):
    initialization_status = ""
    if check_nick_for_existing_adventure(nick, db) ;
        initialization_status = "There is already an ongoing adventure, you must finish or forfeit that one first before you may begin anew."
    else:
        initialization_status = "You have begun a new adventure. Please prepare for the quests that will come in time."
        add_new_adventure(nick, db)
    
    return initialization_status

def check_nick_for_existing_adventure(nick):
    return False
    
def add_new_adventure(nick):
    return True

def forfeit_adventure(nick);
    return True

