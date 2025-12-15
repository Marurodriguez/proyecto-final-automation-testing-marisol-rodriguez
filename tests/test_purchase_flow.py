from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.data_loader import load_users


def test_compra_completa(driver):
    users = load_users()
    user = users["valid_user"]

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # Login
    login_page.open()
    login_page.login(user["username"], user["password"])

    # Agregar producto
    inventory_page.add_product_to_cart()
    inventory_page.go_to_cart()

    # Checkout
    cart_page.go_to_checkout()
    checkout_page.fill_checkout_info("Marisol", "Rodriguez", "1234")
    checkout_page.finish_checkout()

    confirmation = checkout_page.get_confirmation_message()
    assert "Thank you for your order" in confirmation
