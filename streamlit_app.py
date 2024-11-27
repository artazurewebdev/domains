import streamlit as st
import time
import random

# Pricing details
pricing = {
    ".com": 16,
    ".net": 12,
    ".org": 9,
    ".dev": 20,
    ".co": 12,
    ".site": 16,
    ".go": 20,
    ".biz": 16,
    ".io": 30,
    ".lol": 70,
}
processing_fee = 5

# Title and introduction
st.title("ArtAzure Domains")
st.subheader("Find and purchase your perfect domain name!")

# Domain input section
domain_input = st.text_input("Enter a domain name (e.g., mydomain.com):")
if domain_input:
    base_domain, _, _ = domain_input.partition('.')
    
    # Show searching message and loading spinner
    with st.spinner(f"Searching for domains similar to `{domain_input}`..."):
        time.sleep(random.randint(2, 5))  # Simulate a delay of 2-5 seconds

    # Generate domain suggestions
    domain_choices = [f"{base_domain}{ext}" for ext in pricing.keys()]
    st.subheader("Available Domains:")
    selected_domain = st.radio(
        "Select your desired domain:",
        options=domain_choices,
        index=0,
    )

    # Show pricing for the selected domain
    if selected_domain:
        extension = "." + selected_domain.split('.')[-1]
        price = pricing[extension]
        total_price = price + processing_fee
        st.write(f"**Domain Price:** ${price}/yr")
        st.write(f"**Processing Fee:** ${processing_fee} (one-time)")
        st.write(f"**Total Price:** ${total_price}")

        # Checkout section
        st.subheader("Checkout:")
        card_number = st.text_input("Credit Card Number:")
        card_cvv = st.text_input("CVV:", type="password")
        if st.button("Checkout"):
            if card_number and card_cvv:
                st.success(f"Successfully purchased `{selected_domain}` for ${total_price}!")
                st.write("Proceed to connect your domain below.")
            else:
                st.error("Please enter a valid credit card number and CVV.")

# Domain connection section
if st.button("Connect Domain"):
    st.subheader("Connect Your Domain")
    connect_input = st.text_input("Enter the domain to connect (e.g., yourdomain.com):")
    if connect_input:
        st.success(f'Connected to "{connect_input}"!')
