import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="web_automation"
    )

def insert_product(name, price, availability, rating):
    connection = connect_to_db()
    cursor = connection.cursor()
    query = """
    INSERT INTO search_results (name, price, availability, rating)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (name, price, availability, rating))
    connection.commit()
    cursor.close()
    connection.close()
