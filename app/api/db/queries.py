query1 = """CREATE TABLE IF NOT EXISTS products (
        product_id serial PRIMARY KEY,
        name varchar(20) NOT NULL,
        quantity integer NOT NULL,
        description varchar(70) NOT NULL,
        date_created timestamp with time zone DEFAULT ('now'::text)::date NOT NULL);
        """

query2 = """CREATE TABLE IF NOT EXISTS users (
        id serial PRIMARY KEY NOT NULL,
        name varchar(20) NOT NULL,
        email varchar(100) NOT NULL,
        password varchar(300) NOT NULL,
        date_created timestamp with time zone DEFAULT ('now'::text)::date NOT NULL);
        """
# CREATE TABLE IF NOT EXISTS sales(
#         id serial PRIMARY KEY,
#         product_id INT NOT NULL,
#         quantity INT NOT NULL,
#         remains INT NOT NULL,
#         price numeric NOT NULL,
#         name varchar,
#         date_created TIMESTAMP,
#         FOREIGN KEY (product_id) REFERENCES products(product_id)
#         );
#


queries= [query1,query2]
