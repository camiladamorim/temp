from itemadapter import ItemAdapter
import sqlite3

class TemprojectPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('dados.db')
        self.curr = self.conn.cursor()

    def create_table(self):

        self.curr.execute(""" DROP TABLE IF EXISTS items_tb """)
        self.curr.execute("""
            create table items_tb(
                titulo text,
                descricao text,
                url text, 
                img text, 
                query text, 
                id_ text) """)
    
    def store_db(self, item):
        self.curr.execute(""" INSERT INTO items_tb VALUES (?,?,?,?,?,?) """ (item['titulo'],item['descricao'],item['url'],item['img'],item['query'],item['id_']))
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        print("\n\n\n\n\n\n\n"+item[titulo])
        return item

    