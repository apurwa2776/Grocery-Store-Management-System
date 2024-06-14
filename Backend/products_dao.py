import mysql.connector

cnx = mysql.connector.connect(user='root', password='Apurwa@2776',
                              host='127.0.0.1',
                              database='grocerry_store')
cursor = cnx.cursor()
query = "SELECT * FROM grocerry_store.products"
cursor.execute(query)

for (product_id, name, uom_id,price_per_unit) in cursor:
     print(product_id, name, uom_id,price_per_unit)

cnx.close()