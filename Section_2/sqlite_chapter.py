#SQLite is a self-contained, server-less, config-free transactional SQL database engine.
import sqlite3

conn = sqlite3.connect('mydatabase.db')  #or use :memory: to store it in RAM

cursor = conn.cursor()

#create a table
# cursor.execute("""CREATE TABLE albums
#                   (title text, artist text, release_date text,
#                    publisher text, media_type text)
#                """)

#Delete records so I can rerun this, not part of the chapter
cursor.execute("""delete from albums""")
conn.commit()

# insert some data
cursor.execute("""INSERT INTO albums
                  VALUES ('Glow', 'Andy Hunter', '7/24/2012',
                 'Xplore Records', 'MP3')"""
              )

#save data
conn.commit()

#insert multiple records using the more secure "?" method
albums = [('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
          ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
          ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012', 'TF\Kmusic', 'CD'),
          ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')]
cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)", albums)
conn.commit()

#Update records

sql = """
         update albums
            set artist = 'John Doe'
          where artist = 'Andy Hunter'
      """
cursor.execute(sql)
conn.commit()

#Delete records

sql = """
         delete from albums
          where artist = 'John Doe'
      """
cursor.execute(sql)
conn.commit()

#sample queries to get data
sql = """
      select * from albums where artist = ?
      """
cursor.execute(sql, [("Red")])
print(cursor.fetchall()) #Or use fetchone()

print("\nHere's a listing of all the records in the table:\m")
for row in cursor.execute("select rowid, * from albums order by artist"):
    print(row)

print("\nResults from a 'like' query\n")
sql = """
      select *
        from albums
       where title like 'The%'
      """

cursor.execute(sql)
print(cursor.fetchall(                                                                                                                          ))