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

user_table = Table(
    'broken_adventure_users',
    database.metadata,
    Column('nick', String),
    Column('quests', String),
    Column('deaths', String),
    Column('active_adventure', Boolean),
    Column('active_quest', Boolean),
    PrimaryKeyConstraint('nick')
)

quest_table = Table(
    "broken_adventure_quests",
    database.metadata,
    Column('name', String),
    Column('region', Integer),
    Column('desc', String),
    Column('difficulty', Integer),
    Column('id', Integer),
    PrimaryKeyConstraint('id')
)

region_table = Table(
    "broken_adventure_regions",
    database.metadata,
    Column("name", String),
    Column("location", Integer),
    Column("id", Integer),
    PrimaryKeyConstraint('id')
)

story_table = Table(
    "broken_adventure_story",
    database.metadata,
    Column("name", String),
    Column("text", String),
    Column("region", String),
    Column("order", Integer),
    Column("id", Integer),
    PrimaryKeyConstraint('id')
)

#the command used to initialize a new adventure if one is not already active
@hook.command("startadventure")
def start_adventure(nick, db):
    adventure_details = initialize_adventure_details(nick, db)
    return adventure_details

#the command used to stop an active adventure
@hook.command("quitadventure")
def quit_adventure(nick, db):
    adventure_details = forfeit_adventure(nick, db)
    return adventure_details

#this function will check the user table for any active adventures for the user and if none are found, then will update the table with the
#new user or update existing user with a new adventure
def initialize_adventure_details(nick):
    initialization_status = ""
    if check_nick_for_existing_adventure(nick, db)
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

