import requests
import mod_global

def search_businesses(api_key, location, term='restaurant', offset=0):
    '''
    ビジネスを検索する関数
    '''
    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': f'Bearer {api_key}'}
    params = {'location': location, 'term': term,'limit':50, 'offset':offset} # 1回のリクエストで取得する結果数（最大50）
 
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Request failed with status code {response.status_code}')


def main():
    api_key = mod_global.MyGlobal.API_KEY
    location = 'Taipei'
    json = search_businesses(api_key, location, term='Japanese', offset=0)
    # print(json)
    print(len(json['businesses'])) # 50


if __name__ == '__main__':
    main()