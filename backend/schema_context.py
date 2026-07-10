SCHEMA_DESCRIPTION = """
Table: customers(customer_id, name, email, city, signup_date)

Table: products(product_id, name, category, price)

Table: orders(order_id, customer_id, product_id, quantity, order_date)

orders.customer_id references customers.customer_id

orders.product_id references products.product_id
"""
