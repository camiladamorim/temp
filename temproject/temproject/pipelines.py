from itemadapter import ItemAdapter
import sqlite3

class TemprojectPipeline(object):
    def __init__(self):
        
        self.conn = sqlite3.connect('dados.db')
        self.curr = self.conn.cursor()
        self.curr.execute(""" DROP TABLE IF EXISTS items_tb """)
        self.curr.execute(""" CREATE TABLE items_tb(
                                titulo text,
                                descricao text,
                                url text, 
                                img text, 
                                query text, 
                                id_ text) """)



    def process_item(self, items, spider):
        
        # falta um for para iterar a linha abaixo e ir preenchendo as linhas da tabela sqlite3
        self.curr.execute(""" INSERT INTO items_tb VALUES (?,?,?,?,?,?)""",(items['titulo'],items['descricao'],items['url'],items['img'],items['query'],items['id_']))
        #curr.execute(""" INSERT INTO items_tb VALUES ("a","a","a","a","a","a") """)  #ex
        self.conn.commit()
        return items

    