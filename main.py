import os
import psycopg2

conn = psycopg2.connect(
    host=os.environ['DB_HOST'],
    dbname=os.environ['DB_NAME'],
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASSWORD']
)

with conn, conn.cursor() as cur:
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT NOW()
        );

        CREATE TABLE IF NOT EXISTS test(
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT NOW()

        );

        ALTER TABLE test ADD COLUMN IF NOT EXISTS healthy TEXT;
    """)
    cur.execute("INSERT INTO test (name,healthy) VALUES (%s,%s)", ("Test","all right"))
    cur.execute("SELECT count(*) FROM test")
    print("Строк в таблице:", cur.fetchone()[0])

conn.close()