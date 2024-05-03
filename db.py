import psycopg2
import utils

conn = psycopg2.connect(databse="task8",
                        dbname="task8@localhos",
                        user="postgres",
                        host="localhost",
                        password=110,
                        port=5432)

cur = conn.cursor()

create_user_table = """
CREATE TABLE IF NOT EXISTS users (
      id SERIAL PRIMARY KEY,
      usename VARCHAR(255) NOT NULL UNIQUE,
      password VARCHAR(255) NOT NULL,
      role VARCHAR(20),
      status VARCHAR(25),
      login_try_count INT NOT NULL
      );
"""

create_todo_table = """
CREATE TABLE IF NOT EXISTS todos(
    id serial PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    todo_type VARCHAR(100) NOT NULL,
    user_id INT REFERENCES users(id),
);
"""


def commit(func):
    def wrapper(*args, **kwargs):
        func()
        conn.commit()

        return wrapper


@commit
def create_tables():
    cur.execute(create_user_table)
    cur.execute(create_todo_table)


@commit
def migrate():
    insert_admin_query = """insert into users (usename, password, role, status,login_try_count)
          values (%s,%s,%s,%s,%s)
     """
    insert_data_params = ('admin', utils.hash_password('123'), 'ADMIN', 'ACTIVE', 0)
    cur.execute(insert_admin_query, insert_data_params)


def init():
   create_tables()
   migrate()


if __name__ == '__main__':
   init()