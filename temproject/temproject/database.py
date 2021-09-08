import sqlite3

conn = sqlite3.connect('dados.db')
curr = conn.cursor()


curr.execute("""
        create table items_tb(
            titulo text,
            descricao text,
            url text, 
            img text, 
            query ext, 
            id_ text)
            """)

conn.commit()
conn.close()