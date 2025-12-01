from product import product_details

def test_product_details():
    name = "Laptop"
    p_id = "E201"
    quantity = 4
    price = 55000

    expected_output = (
        "Product Name: Laptop\n"
        "Product ID: E201\n"
        "Quantity: 4\n"
        "Price: 55000"
    )

    assert product_details(name, p_id, quantity, price) == expected_output
