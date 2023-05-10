import sqlalchemy as db

engine = db.create_engine("sqlite:///appdata.db")
connection = engine.connect()
metadata = db.MetaData()
User = db.Table("User", metadata, autoload=True, autoload_with=engine)


query = db.select([User.columns.state.distinct()])
resutl = connection.execute(query).scalar()
print(result)
