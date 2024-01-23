import sqlite3
from pathlib import Path

from entities.customer import Customer

ROOT_DIR = Path(__file__).parent.parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'


def start():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute(
        f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
        '('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'name TEXT,'
        'email TEXT,'
        'phone TEXT'
        ')'
    )

    cursor.close()
    connection.close()


def insert(customer: Customer):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    insert_command = (f'INSERT INTO {TABLE_NAME}'
                      '(name, email, phone)'
                      'VALUES'
                      '(?, ?, ?)')

    cursor.execute(insert_command, (customer.name, customer.email, customer.phone))

    connection.commit()

    cursor.close()
    connection.close()


def select(id_: int):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    select_command = f'SELECT * FROM {TABLE_NAME} WHERE id = {id_}'

    cursor.execute(select_command)

    _id, name, email, phone = cursor.fetchone()
    customer = Customer(_id, name, email, phone)

    cursor.close()
    connection.close()

    return customer


def update(id_: int, customer: Customer):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    update_command = f'UPDATE {TABLE_NAME} SET name="{customer.name}", email="{customer.email}", phone="{customer.phone}" WHERE id = {id_}'

    print(update_command)

    cursor.execute(update_command)

    connection.commit()

    cursor.close()
    connection.close()


def delete(id: int):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE id = {id}')

    connection.commit()

    cursor.close()
    connection.close()
