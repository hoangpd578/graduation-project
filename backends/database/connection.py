import mysql.connector
from mysql.connector import Error
from utils import configs
from loguru import logger


def initialize_database():
    """
    Run this before including models and controller
    """
    create_table = '''
    CREATE TABLE employees (
        id int(20) NOT NULL AUTO_INCREMENT,
        user_id varchar(250) NOT NULL,
        check_in time NOT NULL,
        check_out time  NOT NULL,
        name  varchar(250) NOT NULL,
        work_date date NOT NULL,
        prediction_checkin float NOT NULL,
        prediction_checkout float NOT NULL,
        check_in_image varchar(250) NOT NULL,
        check_out_image varchar(250) NOT NULL,
        created_at timestamp NOT NULL,
        updated_at timestamp NOT NULL,
        PRIMARY KEY (id));

    CREATE TABLE users (
        id int(20) NOT NULL ATUO_INCREMENT,
        name varchar(255) NOT NULL,
        email varchar(255) NOT NULL,
        email_verified_at timestamp NULL,
        password varchar(255) NOT NULL,
        menuroles varchar(255) NOT NULL,
        remember_token varchar(100) NULL,
        created_at timestamp NOT NULL,
        updated_at timestampl NOT NULL,
        deleted_at timestampl NULL,
        PRIMARY KEY (id)),
        FOREIGN KEY (email);
    '''
    try:
        conn = mysql.connector.connect(
                    host="localhost", database="db", user="root"
                )
        db_Info = conn.get_server_info()
        logger.info("Successfully connected to existing DB.")
        logger.info("Connected to MySQL database ", db_Info)

    except Error as e:
        logger.error(e)

    # Check exist the employees tabel
    query = "SHOW TABLES LIKE 'employees'"
    c = conn.cursor()
    c.execute(query)
    result = c.fetchone()
    if not result:
        c.execute(create_table)
        conn.commit()

    return conn


conn = initialize_database()
