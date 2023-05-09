import requests

def get_business_review_highlights(api_key, business_id):
    url = f'https://api.yelp.com/v3/businesses/{business_id}/reviews'
    headers = {'Authorization': f'Bearer {api_key}'}
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    
    review_highlights = []
    for review in data['reviews']:
        review_highlights.append({
            'user': review['user']['name'],
            'rating': review['rating'],
            'text': review['text']
        })
    
    return review_highlights

# Replace with your Yelp API key
api_key = 'ZSbcbAytMl1uddDiPVkghxYAtEYeAR62p_KSAyZgZGbo697YjFXLoSDDPJd4GMRcvcDYifoo72QfnzrB59XqzvcWNG8McqCyCPQYU8t_DHR4o-AYAC3qyaTHx19WZHYx'
# Replace with the business ID you want to get the review highlights for
business_id = 'iZfGDTEmPQXw8tOkrpEurQ'

# review_highlights = get_business_review_highlights(api_key, business_id)
# for idx, review in enumerate(review_highlights, start=1):
#     print(f"Review {idx}:")
#     print(f"User: {review['user']}")
#     print(f"Rating: {review['rating']}")
#     print(f"Text: {review['text']}\n")


# ビジネスレビューの抜粋を最大３つ取得するメソッド
def get_business_reviews(api_key, business_id):
    url = f'https://api.yelp.com/v3/businesses/{business_id}/reviews'
    headers = {'Authorization': f'Bearer {api_key}'}
        
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    
    reviews = []
    for review in data['reviews']:
        reviews.append({
            'user': review['user']['name'],
            'rating': review['rating'],
            'text': review['text']
        })
    
    return reviews

get_business_reviews = get_business_reviews(api_key, business_id)
for idx, review in enumerate(get_business_reviews, start=1):
    print(f"Review {idx}:")
    print(f"User: {review['user']}")
    print(f"Rating: {review['rating']}")
    print(f"Text: {review['text']}\n")
    
# if __name__ == '__main__':
#     main()