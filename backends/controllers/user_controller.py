from mysql.connector import Error
from utils import configs
from database.connection import conn
from loguru import logger
import time


def create_user(user):
    c = conn.cursor()
    user.created_at = time.strftime("%Y-%m-%d %H:%M:%S")
    user.updated_at = time.strftime("%Y-%m-%d %H:%M:%S")
    try:
        query = ("INSERT INTO users (id, name, email, password,"
                 " menuroles, created_at, updated_at)"
                 " VALUES (%s, %s, %s, %s, %s, %s, %s)")

        task = (user.id, user.name, user.email, user.password,
                user.menuroles, user.created_at, user.updated_at)

        c.execute(query, task)

        conn.commit()
        logger.info("Record inserted successfully into Users table.")
    except Error as e:
        logger.error(e)

    return
