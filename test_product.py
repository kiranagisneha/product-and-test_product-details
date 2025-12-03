from product import product_info

def test_product_info():
    result = product_info("P101", "Laptop", 5, 60000)
    expected = (
        "Product ID: P101\n"
        "Name: Laptop\n"
        "Quantity: 5\n"
        "Price: 60000"
    )
    assert result == expected
