import os
import psycop2

dbname = os.env.get('')



cur.execute("""CREATE TABLE IF NOT EXISTS users(
        id int PRIMARY KEY,
        username varchar(20) NOT NULL,
        email varchar(90) NOT NULL,
        password varchar(90) NOT NULL,

)"""")


cur.execute("""CREATE TABLE IF NOT EXISTS products(
        id INT PRIMARY KEY,
        name varchar(20) NOT NULL,
        quantity INT NOT NULL,
        price INT NOT NULL,
        description varchar(70) NOT NULL
)"""")
