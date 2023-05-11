import sqlalchemy as db
from sqlalchemy import inspect

engine = db.create_engine("sqlite+pysqlite:///appdata.db") #,echo=True)
inspector = inspect(engine)
tables = inspector.get_table_names()
print(tables)

#conn = engine.connect()

metadata = db.MetaData()
metadata.reflect(bind=engine)


#conn.execute("SELECT * FROM User")
#conn.commit()

User = db.Table("user", metadata, autoload_with=engine)


#query = db.select([User.columns.state.distinct()])a

stmt = User.select()
with engine.connect() as conn:
    result = conn.execute(stmt)
    rows = result.fetchall()

for row in rows:
    print(row)

note = db.Table("note", metadata, autoload_with=engine)
stmt = note.select()
with engine.connect() as conn:
    result = conn.execute(stmt)
    rows = result.fetchall()
for row in rows:
    print(rows)

message = db.Table("message",metadata, autoload_with=engine)
stmt = message.select()
with engine.connect() as conn:
    result = conn.execute(stmt)
    rows = result.fetchall()
for row in rows:
    print(rows)

#stmt = select(*User.__table__.columns)
#rows = connection.execute(stmt)
#resutl = connection.execute(query).scalar()
#print(result)
