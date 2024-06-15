import mysql.connector

def get_all_products():
    # Establish the connection
    cnx = mysql.connector.connect(
        user='root', 
        password='Apurwa@2776',
        host='127.0.0.1',
        database='grocerry_store'
    )
    cursor = cnx.cursor()

    # Define your query
    query = (
        "SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name "
        "FROM products "
        "INNER JOIN uom ON products.uom_id = uom.uom_id"
    )

    # Execute the query
    cursor.execute(query)

    response = []

    # Fetch and process the results
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'product_id': product_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })

    # Close the cursor and connection
    cursor.close()
    cnx.close()

    return response

if __name__ == '__main__':
    products = get_all_products()
    for product in products:
        print(product)
