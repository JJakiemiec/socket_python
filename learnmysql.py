import mysql.connector
import os


DATABASE = "test"
TABLE = "graboble"


def detuple(t):
    r = []
    for item in t:
        r.extend(item)
    return r

def get_id_list(id_cursor):
    cursor.execute(f"SELECT id from {TABLE}")
    return detuple(id_cursor.fetchall())


db = mysql.connector.connect(
    host='localhost',
    user='Admin',
    password = os.environ.get("SQL_ADMIN_PASSWORD"),
    database = DATABASE
)
cursor = db.cursor()


cursor.execute(f"SHOW TABLES IN {DATABASE}")
tables = detuple(cursor.fetchall())
cursor.execute("SHOW DATABASES")
print(detuple(cursor.fetchall()))


# create table
if TABLE not in tables:
    cursor.execute(f"CREATE TABLE {DATABASE}.{TABLE} (id INT, name VARCHAR(255), address VARCHAR(255))")
    print(f"{TABLE} created")
else:
    print(f"{TABLE} already exists")


# add primary key to table
cursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS where TABLE_SCHEMA = 'test' and column_key = 'PRI' and table_name = '{TABLE}';")
primary = detuple(cursor.fetchall())
if primary == []:
    cursor.execute(f"ALTER TABLE {TABLE} ADD PRIMARY KEY (id)")
    print(f"added primary key to {TABLE}")
else:
    print(f"primary key already exists in {TABLE}")



# add row into table
id=1
sql = f"INSERT INTO {TABLE} (id, name, address) VALUES (%s, %s, %s)"
val = (id, "jim", "around the corner")
id_list = get_id_list(cursor)

if(id not in id_list):
    cursor.execute(sql, val)
    db.commit()
    print(f"added row to {TABLE}")
else:
    print(f"row already added to {TABLE}")


#add multiple rows into table
vals = []
addresses = ["around the corner", "McDonalds", "near the rock", "down the road"]
sql = f"INSERT INTO {TABLE} (id, name, address) VALUES (%s, %s, %s)"

id_list = get_id_list(cursor)
for i in range(2, 10):
    if i not in id_list:
        vals.append((i, f"jongo #{i}", addresses[i % len(addresses)]))
if vals != []:
    cursor.executemany(sql, vals)
    db.commit()
    print(f"added {len(vals)} rows to {TABLE}")
else:
    print(f"all rows already in {TABLE}")


#select statement
cursor.execute(f"SELECT name, address FROM {TABLE} WHERE address = 'McDonalds'")
selectall = cursor.fetchall()
print(selectall)

cursor.execute(f"SELECT name, address FROM {TABLE} WHERE address like '%the%'")
selectall = cursor.fetchall()
print(selectall)


#delete from table
sql = f"DELETE FROM {TABLE} WHERE ID = '%s'"
val = (7,)
cursor.execute(sql, val)
db.commit()
print(f"{cursor.rowcount} records got deleted from {TABLE}")


#join statements
ltable = "fungo"
rtable = "pringo"
join = "INNER JOIN"

sql = f"select {ltable}.name as fname, {ltable}.number as fnum, {rtable}.location as ploc, {rtable}.funnumber as pnum \
    FROM {ltable} {join} {rtable} \
    ON {ltable}.pringo = {rtable}.ID"
cursor.execute(sql)
result = cursor.fetchall()

print(f"{join}:")
for x in result:
    print(x)

join = "LEFT JOIN"
sql = f"select {ltable}.name as fname, {ltable}.number as fnum, {rtable}.location as ploc, {rtable}.funnumber as pnum \
    FROM {ltable} {join} {rtable} \
    ON {ltable}.pringo = {rtable}.ID"
cursor.execute(sql)
result = cursor.fetchall()

print(f"{join}:")
for x in result:
    print(x)

join = "RIGHT JOIN"
sql = f"select {ltable}.name as fname, {ltable}.number as fnum, {rtable}.location as ploc, {rtable}.funnumber as pnum \
    FROM {ltable} {join} {rtable} \
    ON {ltable}.pringo = {rtable}.ID"
cursor.execute(sql)
result = cursor.fetchall()

print(f"{join}:")
for x in result:
    print(x)

print(f"last command: {cursor.lastrowid}")