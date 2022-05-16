# # import psycopg2

# # connection = psycopg2.connect(
# #     database='db_practice',
# #     user='almazabdysalamov',
# #     password='1',
# #     host='localhost',
# #     port='5432'
# # )
# # print('Database successfully opened')

# # cursor = connection.cursor()

# # cursor.execute(
# #     '''create table company(
# #         id serial primary key,
# #         name varchar(100) not null,
# #         city varchar(50) not null
# #     )
# #     '''
# # )
# # print('Table successfully created')
# # connection.commit()
# # connection.close()

# # cursor = connection.cursor()
# # cursor.execute(
# #     '''
# #     insert into company(name, city) values('IBM', 'Los Angeles'), ('Apple', 'Cupertino'), ('HP', 'New York'), ('Dell', 'New Jersey')
# #     '''
# # )

# # connection.commit()
# # print('Inserted successfully')
# # connection.close()

# # cursor.execute(
# #     '''insert into company(name, city) values('Samsung', 'Seoul')
# #     '''
# # )
# # cursor.execute(
# #     '''insert into company(name, city) values('Toyota', 'Tokyo')
# #     '''
# # )
# # connection.commit()
# # print('Inserted successfully')
# # connection.close()



# # cursor.execute(
# #     'select * from company'
# # )
# # # print(cursor.fetchall())
# # data = cursor.fetchall()
# # for item in data:
# #     # print(f"id: {item[0]}, name: {item[1]}, city: {item[2]}")
# #     print(*item)
# # connection.close()

# # cursor.execute(
# #     "select name, city from company where id=2"
# # )
# # data = cursor.fetchone()
# # print(data)



# # cursor.execute(
# #     '''update company set city='New Mexico' where id = 2'''
# # )
# # connection.commit()
# # cursor.execute(
# #     '''
# #     select * from company order by id'''
# # )
# # data = cursor.fetchall()
# # for item in data:
# #     print(*item)
# # connection.close()


# # cursor = connection.cursor()
# # cursor.execute(
# #     '''
# #     delete from company where id=3
# #     '''
# # )
# # connection.commit()
# # print(f"Total count of deleted: {cursor.rowcount}")
# # cursor.execute(
# #     'select * from company order by id'
# # )
# # data = cursor.fetchall()
# # for item in data:
# #     print(*item)
# # connection.close()



# from sqlalchemy import create_engine

# engine = create_engine('postgresql+psycopg2://almazabdysalamov:123@localhost:5432/db_practice')

# # print('Database connected')

# from sqlalchemy import Column, Table, Integer, MetaData, String

# metadata = MetaData()
# students_table = Table(
#     'students', metadata,
#     Column('id', Integer, primary_key=True),
#     Column('name', String),
#     Column('last_name', String)
# )
# students_table.create(bind=engine)
# print('Successfully created table')

































