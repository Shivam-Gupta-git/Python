import requests

def fetch_random_api():
    url = "https://api.freeapi.app/api/v1/public/randomproducts"

    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        product = data["data"]["data"][1]

        return {
            "Title": product["title"],
            "Description": product["description"],
            "Price": product["price"],
            "Discount %": product["discountPercentage"],
            "Rating": product["rating"],
            "Stock": product["stock"],
            "Brand": product["brand"],
            "Category": product["category"]
        }

def main():
    try:
        product = fetch_random_api()

        print("\n" + "=" * 50)
        print("🛒 PRODUCT DETAILS")
        print("=" * 50)

        print(f"📌 Title       : {product['Title']}")
        print(f"🏷️  Brand       : {product['Brand']}")
        print(f"📂 Category    : {product['Category']}")
        print("-" * 50)
        print(f"📝 Description : {product['Description']}")
        print("-" * 50)
        print(f"💰 Price       : ₹{product['Price']}")
        print(f"🔻 Discount    : {product['Discount %']}%")
        print(f"⭐ Rating      : {product['Rating']}")
        print(f"📦 Stock       : {product['Stock']}")
        print("=" * 50)

    except Exception as ex:
        print("❌ Error:", str(ex))

if __name__ == "__main__":
    main()