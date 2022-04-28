import sqlite3

class ScrappingPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()
    
    def create_connection(self):
        self.connection = sqlite3.connect('movies.db')
        self.cursor = self.connection.cursor()
        
    def create_table(self):
        self.cursor.execute("DROP TABLE IF EXISTS 'movie'")

        self.cursor.execute("""
                CREATE TABLE 'movie' (
                    'index' INT PRIMARY KEY,
                    'title' TEXT,
                    'size' TEXT,
                    'views' TEXT,
                    'seeds' TEXT,     
                    'link' TEXT
                )
               """)
        self.connection.commit()
    
    
    def process_item(self, item, spider):
        self.store_database(item)
        return item

    def store_database(self, item):
        self.cursor.execute("""
                INSERT INTO 'movie' VALUES (?,?,?,?,?,?)""", (
                    item['index'],
                    item['title'],
                    item['size'],
                    item['views'],
                    item['seeds'],
                    item['link']
                )
            )
        
        self.connection.commit()
