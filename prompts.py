from langchain.llms import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_gen_ai(username, user_products,ad):
    llm = OpenAI(temperature=0.9)

    prompt_template = """
    Generate a personalized ad recommendation for user {} based on their search history. The user has shown interest in the following products: {}. Please provide an ad with the following details:
    - Title: {}
    - Brand: {}
    - Description: {}
    - Tagline: {}
    - Category: {}
    Ensure that the ad is personalized and pleasing to the user. The response should be within one sentence
    """

    # Fill in the placeholders using .format()
    prompt = prompt_template.format(
        username,
        ", ".join(user_products),
        ad["title"],
        ad["brand"],
        ad["description"],
        ad["tagline"],
        ad["category"]
    )
    return llm(prompt)
# if __name__ == "__main":
#     username = "Anand"
#     user_products = ["Apple Laptop", "ear buds"]
#     ad = {
#         "description": "Luxurious leather recliner for the ultimate relaxation.",
#         "tags": [
#             "furniture",
#             "recliner",
#             "Crate & Barrel",
#             "leather"
#         ],
#         "tagline": "Luxury at Home",
#         "product_id": 21,
#         "price": 599.99,
#         "link": "https://www.ebay.com/itm/295494303998?hash=item44ccd540fe:g:UJ4AAOSwybRj02Bk&amdata=enc%3AAQAIAAAA0FpePMCMFLbedpdH5gZTbBG2jPugzCyIpPoOFVSvhhQYH7ShnkM4Xiq18KZnu55HUV%2B8t4JaaO9%2BdyTCJ4adKtyRjf00EHmp%2F3n1c2CZFxe5t8PJmJ2iq1EdJw4Q97uBc7oqf0HGMFku0Rr9GM4FZLfJqe7jCusc9ak%2F%2B4qgsaftGXQMtXoriI%2F0sSYz1Kw7wuBS0V8w9YjQ7UfPETmAQT1%2FiiJmN7DsDXl1iKH3qz5ON3M1mzgpPBt%2F8i35R3bpDjjSv1Xt8cB6txga0UuskXQ%3D%7Ctkp%3ABFBMnMyHvc5i",
#         "title": "Leather Recliner",
#         "image_url": "https://i.ebayimg.com/images/g/UJ4AAOSwybRj02Bk/s-l1600.jpg",
#         "product": "Furniture",
#         "brand": "Crate & Barrel",
#         "sub_category": "Recliner",
#         "category": "Home & Living"
#     }


#     print (get_gen_ai(username,user_products,ad))