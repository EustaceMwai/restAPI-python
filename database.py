import click
from flask import g, current_app
import sqlite3

from flask.cli import with_appcontext


def connect_db():
    sql = sqlite3.connect('members.db')
    sql.row_factory = sqlite3.Row
    return sql


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db
