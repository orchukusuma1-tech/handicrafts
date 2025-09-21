import streamlit as st

# -------------------------------
# Embedded product data
# (replace image values with base64 if you want)
# -------------------------------
products = [
    {
        "id": 1,
        "name": "Handmade Bamboo Basket",
        "description": "A strong eco-friendly basket made with love by rural artisans.",
        "price": 299,
        "image": "images/basket.png",  
        "category": "Basket",
        "owner": "Anitha Handicrafts",
        "manager": "Ravi Kumar"
    },
    {
        "id": 2,
        "name": "Terracotta Vase",
        "description": "Beautifully crafted terracotta vase, perfect for home decor.",
        "price": 599,
        "image": "images/vase.png",
        "category": "Vase",
        "owner": "Sita Pottery Works",
        "manager": "Lakshmi Devi"
    }
]

# -------------------------------
# Initialize session state (cart)
# -------------------------------
if "cart" not in st.session_state:
    st.session_state.cart = []

# -------------------------------
# Add to cart function
# -------------------------------
def add_to_cart(product):
    st.session_state.cart.append(product)
    st.success(f"{product['name']} added to cart!")

# -------------------------------
# Show cart
# -------------------------------
def show_cart():
    st.header("🛒 Your Cart")
    if not st.session_state.cart:
        st.info("Your cart is empty.")
        return

    total = 0
    for item in st.session_state.cart:
        st.image(item["image"], width=150)
        st.subheader(item["name"])
        st.write(item["description"])
        st.write(f"💰 Price: ₹{item['price']}")
        st.caption(f"Owner: {item['owner']} | Manager: {item['manager']}")
        total += item["price"]
        st.write("---")

    st.subheader(f"Total: ₹{total}")

    if st.button("Proceed to Checkout ✅"):
        st.success("Checkout complete! Thank you for supporting local artisans. 🙏")
        st.session_state.cart.clear()

# -------------------------------
# Main UI
# -------------------------------
def main():
    st.set_page_config(page_title="Handicrafts Store", layout="wide")
    st.title("🛍️ Welcome to Handicrafts Store")

    menu = ["Home", "Products", "Cart", "About"]
    choice = st.sidebar.selectbox("Navigate", menu)

    if choice == "Home":
        st.header("Discover Authentic Handmade Products")
        st.write("Browse our collection of eco-friendly and traditional handicrafts.")

    elif choice == "Products":
        st.header("Available Products")

        # Search bar
        search_query = st.text_input("🔍 Search Products", "").strip().lower()

        # Filter by category
        categories = ["All"] + sorted(list(set([p["category"] for p in products])))
        selected_category = st.selectbox("Filter by Category", categories)

        cols = st.columns(2)
        found = False
        for idx, product in enumerate(products):
            if ((selected_category == "All" or product["category"] == selected_category) and
                (search_query in product["name"].lower() or search_query in product["description"].lower())):

                found = True
                with cols[idx % 2]:
                    st.image(product["image"], use_container_width=True)
                    st.subheader(product["name"])
                    st.write(product["description"])
                    st.write(f"💰 Price: ₹{product['price']}")
                    st.caption(f"Owner: {product['owner']} | Manager: {product['manager']}")
                    if st.button(f"Add to Cart 🛒", key=product["id"]):
                        add_to_cart(product)

        if not found and search_query:
            st.warning("No products found matching your search.")

    elif choice == "Cart":
        show_cart()

    elif choice == "About":
        st.header("About Us")
        st.write("""
        🌸 Our mission is to support rural artisans by bringing their handmade crafts online.  
        Every purchase directly helps local communities grow and sustain their traditions.  
        """)

# -------------------------------
# Run the app
# -------------------------------
if __name__ == "__main__":
    main()






