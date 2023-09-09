import firebase_admin
import pandas as pd
from firebase_admin import credentials
from firebase_admin import firestore
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import numpy as np
import pickle
import json



cred = credentials.Certificate("friendfusion-1ade4-firebase-adminsdk-s9uyv-50f754cbca.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Fetch product details from Firestore
products_ref = db.collection('products')
products = products_ref.stream()

product_data = []
for product in products:
    product_data.append(product.to_dict())

products_df = pd.DataFrame(product_data)
products_df["Attributes"] = products_df["category"] + " " + products_df["sub_category"] + " " + products_df["brand"] + " " + products_df["title"]

ads_ref = db.collection('ads')
ads = ads_ref.stream()

ad_data = []
for ad in ads:
    ad_data.append(ad.to_dict())

ads_df = pd.DataFrame(ad_data)
ads_df["Attributes"] = ads_df["category"] + " " + ads_df["sub_category"] + " " + ads_df["brand"] + " " + ads_df["title"]



tfidf_vectorizer = TfidfVectorizer()
tfidf_products = tfidf_vectorizer.fit_transform(products_df["Attributes"])
tfidf_ads = tfidf_vectorizer.transform(ads_df["Attributes"])


cosine_similarities = linear_kernel(tfidf_products, tfidf_ads)


top_ad_ids = []

# Loop through each product in Type 1
for i in range(len(products_df)):
    # Get the cosine similarities for the current Type 1 product with all Type 2 products
    similarities = cosine_similarities[i]
    
    # Use argsort to get the indices of the top three similar products in Type 2
    top_indices = np.argsort(similarities)[-3:][::-1]
    
    # Get the ad_ids for the top three similar products
    top_ad_ids.append([{"ad_id":ads_df.iloc[j]['ad_id'],"val":cosine_similarities[i][j]} for j in top_indices])

for x in product_data:
    top_ad_ids[x["product_id"]-1].append(x["title"])
    top_ad_ids[x["product_id"]-1].append(x["category"])

print(top_ad_ids[0])

np.save('top_ad_ids.npy', top_ad_ids)

# Now, top_ad_ids is a dictionary where keys are Type 1 ad_ids, and values are lists of the top three Type 2 ad_ids