from sqlalchemy import create_engine, text


engine = create_engine("postgresql://jarek:elo@localhost:5432/postgres")

with engine.connect() as connection:
    result = connection.execute(text("select * from my_table"))
    for row in result:
        print("first:", row.first_col)
        print("second:", row.second_col)
