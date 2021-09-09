from itemadapter import ItemAdapter
import sqlite3

class TemprojectPipeline(object):

    def process_item(self, items, spider):
        conn = sqlite3.connect('dados.db')
        curr = conn.cursor()
        curr.execute(""" DROP TABLE IF EXISTS items_tb """)
        curr.execute(""" CREATE TABLE items_tb(
                                titulo text,
                                descricao text,
                                url text, 
                                img text, 
                                query text, 
                                id_ text) """)
        #print("\n\nn\n\n\n\n\n\n\n\n\n\n", item['url'])
        curr.execute(""" INSERT INTO items_tb VALUES (?,?,?,?,?,?)""",(items['titulo'],items['descricao'],items['url'],items['img'],items['query'],items['id_']))
        #curr.execute(""" INSERT INTO items_tb VALUES ("a","a","a","a","a","a") """)
        conn.commit()
        return items

    