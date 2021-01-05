from mysql.connector import Error
import mysql.connector
from utils import configs
from database.connection import conn
from loguru import logger


def create_employee(employee):
    c = conn.cursor()

    try:
        query = ("INSERT INTO employees(name, user_id, check_in, check_out,"
                 " work_date, prediction_checkin, prediction_checkout,"
                 " created_at, updated_at, check_in_image, check_out_image)"
                 " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

        task = (employee.name, employee.user_id, employee.check_in,
                employee.check_out, employee.work_date,
                employee.prediction_checkin, employee.prediction_checkout,
                employee.created_at, employee.updated_at,
                employee.check_in_image, employee.check_out_image)

        c.execute(query, task)
        conn.commit()
        logger.info("Record inserted successfully into Employees table.")
    except Error as e:
        logger.error(e)

    return


def check_employee(employee):
    c = conn.cursor()
    query_check = "SELECT *FROM employees WHERE user_id=%s AND work_date=%s"
    input = (employee.user_id, employee.work_date)

    c.execute(query_check, input)
    result = c.fetchone()
    if result:
        logger.info("Employee's information is existing on DB.")
        return True

    return False


def update_database(employee):
    conn_ = mysql.connector.connect(
                    host="localhost", database="db", user="root"
                )
    c = conn_.cursor()
    try:
        query = '''UPDATE employees SET updated_at = %s, check_out = %s,
                 check_out_image = %s, prediction_checkout = %s
                 WHERE user_id = %s AND work_date = %s'''

        input = (employee.updated_at, employee.updated_at,
                 employee.check_out_image, employee.prediction_checkout,
                 employee.user_id, employee.work_date)
        c.execute(query, input)
        conn_.commit()
        logger.info("Successfully in updated information of check out.")
        
    except Error as e:
        logger.error(e)

    return
