#Create-Insert
#Read-select
#Update-update
#Delete-delete
#sql 
import psycopg2
from example_config.config import load_config  # Импорт функции load_config из указанного пути

conn = psycopg2.connect(
    host='localhost',
    dbname='students',
    user='postgres',
    password='1234'
)


#курсор
cur = conn.cursor()

#table
cur.execute("""CREATE TABLE students_data (
            name VARCHAR(255),
            id VARCHAR(255) PRIMARY KEY,
            study_year INT,
            phone_number VARCHAR(20)
            
            
);
""")

conn.commit()
#
cur.execute("""INSERT INTO students_data (name, id, study_year, phone_number) VALUES
            ('Ruslan', '24B202424', '1', '+77029996546'),
            ('Baha', '24B202425', '1', '+77029496546')
""")

conn.commit()




