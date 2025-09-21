import json
import streamlit as st

# -------------------
# Load product data
# -------------------
def load_products():
    with open("products.json", "r") as f:
        return json.load(f)

# -------------------
# Display product card
# -------------------
def display_product(product):
    st.image(product["image"], width=250)
    st.subheader(product["name"])
    st.write(product["description"])
    st.write(f"💰 Price: ₹{product['price']}")
    st.write(f"👤 Owner: {product['owner']}")
    st.write(f"📋 Manager: {product['manager']}")

    # Add to Cart button
    if st.button(f"🛒 Add {product['name']} to Cart", key=product["id"]):
        st.session_state["cart"].append(product)
        st.success(f"{product['name']} added to cart!")

# -------------------
# Main App
# -------------------
def main():
    st.title("🛍️ Handicraft Marketplace")
    st.write("Welcome to our handicraft store! Buy unique handmade products.")

    # Initialize cart
    if "cart" not in st.session_state:
        st.session_state["cart"] = []

    # Load products
    products = load_products()

    # Sidebar
    st.sidebar.header("Filters")
    search = st.sidebar.text_input("🔎 Search Product")
    categories = ["All"] + list(set([p["category"] for p in products]))
    selected_category = st.sidebar.selectbox("📂 Category", categories)

    st.sidebar.subheader("🛒 Cart")
    if st.session_state["cart"]:
        for item in st.session_state["cart"]:
            st.sidebar.write(f"- {item['name']} (₹{item['price']})")
        total = sum([item["price"] for item in st.session_state["cart"]])
        st.sidebar.write(f"**Total: ₹{total}**")
        st.sidebar.button("Proceed to Checkout")
    else:
        st.sidebar.write("Cart is empty.")

    # Filter logic
    filtered_products = products
    if search:
        filtered_products = [p for p in filtered_products if search.lower() in p["name"].lower()]
    if selected_category != "All":
        filtered_products = [p for p in filtered_products if p["category"] == selected_category]

    # Display products
    for product in filtered_products:
        st.markdown("---")
        display_product(product)

if __name__ == "__main__":
    main()
