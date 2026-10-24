import sqlite3

DB = "placeready.db"


def _conn():
    c = sqlite3.connect(DB)
    c.row_factory = sqlite3.Row
    return c


def init():
    with _conn() as c:
        c.executescript("""
        create table if not exists users(id integer primary key, email text unique, name text, hash text);
        create table if not exists resumes(id integer primary key, user_id int, text text, ats int, skills text, created int default (strftime('%s','now')));
        create table if not exists interviews(id integer primary key, user_id int, question text, score real, created int default (strftime('%s','now')));
        """)


def query(sql, args=(), one=False):
    with _conn() as c:
        rows = c.execute(sql, args).fetchall()
    return (rows[0] if rows else None) if one else rows


def run(sql, args=()):
    with _conn() as c:
        return c.execute(sql, args).lastrowid
