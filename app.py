from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS from flask_cors
from generate_personalised_ad import get_personal_ads

app = Flask(__name__)
CORS(app)

@app.route('/get_ads/<email>', methods=['GET'])
def get_ads(email):
    # In a real-world scenario, you would fetch user-specific ad data here
    # For this example, we'll return all ads for simplicity

    ads=get_personal_ads(email)
    # ads=[{"ad_id":8,"brand":"IKEA","category":"Home & Furniture","description":"Comfortable and stylish sofa for your living room.","image_url":"https://www.ikea.com/in/images/products/ektorp-3-seat-sofa-hallarp-grey__0818567_pe774489_s5.jpg?f=xl","link":"https://www.ikea.com/in/en/p/ektorp-3-seat-sofa-hallarp-grey-s19320049/?utm_source=google&utm_medium=surfaces&utm_campaign=shopping_feed&utm_content=free_google_shopping_clicks_Livingroomseating&gclid=CjwKCAjwjOunBhB4EiwA94JWsIB9LJx3cS7pEPXujovZlTwOpkCbmzLmLDVqNyd-9SD6bUEDBoYZ4hoCytEQAvD_BwE","personalizedText":"\n\"Treat yourself to the comfortable and stylish Ektorp Sofa from IKEA and relax in style to complete your living space after enjoying your new Ray-Ban Aviator Sunglasses, MacBook Pro and Samsung Galaxy S21!\"","price":499.99,"sub_category":"Sofas","tagline":"Relax in Style","title":"Ektorp Sofa"},{"ad_id":1,"brand":"BTS","category":"Music","description":"Latest album from BTS featuring hit songs.","image_url":"https://ibighit.com/bts/images/bts/discography/map_of_the_soul-7/img01.jpg","link":"https://ibighit.com/bts/eng/discography/detail/map_of_the_soul-7.html","personalizedText":"\nExperience the ultimate BTS experience with their latest album, Map of the Soul: 7, filled with hit songs just for you, Anand!","price":29.99,"sub_category":"K-Pop","tagline":"Get the Ultimate BTS Experience","title":"BTS - Map of the Soul: 7"},{"ad_id":9,"brand":"Apple","category":"Electronics","description":"Powerful laptop for creative professionals.","image_url":"https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/mba15-midnight-config-202306?wid=840&hei=508&fmt=jpeg&qlt=90&.v=1684340991333","link":"https://www.apple.com/in/shop/buy-mac/macbook-air/15-inch-midnight-apple-m2-chip-with-8-core-cpu-and-10-core-gpu-256gb","personalizedText":"\nWelcome to the world of Apple, Anand - unleash your creativity with the MacBook Pro, the powerful laptop for creative professionals.","price":1999.99,"sub_category":"Laptops","tagline":"Unleash Your Creativity","title":"MacBook Pro"}]
    return jsonify(ads)

if __name__ == '__main__':
    app.run(debug=True)

# data = get_personal_ads("anandverma6220@gmail.com")
# print(data)