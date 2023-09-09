import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import numpy as np
from prompts import get_gen_ai


cred = credentials.Certificate("friendfusion-1ade4-firebase-adminsdk-s9uyv-50f754cbca.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

top_ad_ids = np.load('top_ad_ids.npy', allow_pickle=True)
# print("65",top_ad_ids[14][3])
# print(top_ad_ids)
def get_data_from_ad(adId):
    # return {'age': 28, 'name': 'Anand', 'favorite_items': [4, 25, 6], 'user_id': 'u1', 'email': 'anandverma6220@gmail.com', 'bought_items': [8, 11, 21, 22, 19], 'cart_items': [20, 17, 7, 22]}
    ad_ref = db.collection('ads')
    query = ad_ref.where('ad_id', '==', adId)
    results = query.get()
    # print("18: ",results[0].to_dict())

    return results[0].to_dict()


def get_data_from_email(email):
    # return {'age': 28, 'name': 'Anand', 'favorite_items': [4, 25, 6], 'user_id': 'u1', 'email': 'anandverma6220@gmail.com', 'bought_items': [8, 11, 21, 22, 19], 'cart_items': [20, 17, 7, 22]}
    users_ref = db.collection('users')
    query = users_ref.where('email', '==', email)
    results = query.get()
    return results[0].to_dict()

def get_recommended_ad_ids(product_ids):
    add_dict = {}
    for x in product_ids:
        key = top_ad_ids[x-1][0]['ad_id']
        if key in add_dict:
            add_dict[key]+=top_ad_ids[x-1][0]['val']
        else :
            add_dict[key]=top_ad_ids[x-1][0]['val']
    sorted_dict_descending = dict(sorted(add_dict.items(), key=lambda item: item[1], reverse=True))
    first_3_items = dict(list(sorted_dict_descending.items())[:3])
    first_3_keys = list(first_3_items.keys())
    pd_dict = {}
    for ad_id in first_3_keys:
        pd_dict[ad_id]=[]
        for x in product_ids:
            for i in range(0,3):
                if top_ad_ids[x-1][i]['ad_id'] == ad_id:
                    pd_dict[ad_id].append(x)
    sliced_dict = {}
    for key, value in pd_dict.items():
        sliced_dict[key] = value[:3]
    return sliced_dict


def get_personal_ads(email):
    data=get_data_from_email(email)
    product_ids = data['favorite_items']+data['bought_items']+data['cart_items']
    product_ids=list(set(product_ids))
    dict = get_recommended_ad_ids(product_ids)
    username=data["name"]
    user_ads_gen_ai=[]
   
    user_products=[]
    # buyed_items = top_ad_ids[14][3]
    for key, values in dict.items():
        ad = get_data_from_ad(int (key))
        for value in values:
            user_products.append(top_ad_ids[value-1][3])
        personalizedText=get_gen_ai(username, user_products,ad)
        ad["personalizedText"]=personalizedText
        user_ads_gen_ai.append(ad)
    return user_ads_gen_ai



if __name__ == "__main__" :
    get_personal_ads('anandverma6220')