import time
import mod_global
import mod_search_businesses as sb
import spreadsheet as sp

# 空のリスト
json_list = []

# レストランを検索する
for offset in range(1001,1101, 50):
    json = sb.search_businesses(mod_global.MyGlobal.API_KEY, 'Taiwan',term='Japanese', offset=offset)

    # 50軒分のレストラン情報を取得する
    restaurants = json['businesses']

    # json_listに追加する
    json_list.extend(restaurants)
    time.sleep(2)

# 空のリスト
data = []

# json_listから必要なプロパティ名を指定する
for restaurant in json_list:
    
    # 必要なプロパティ名
    keys =['id', 'alias', 'name', 'image_url', 'is_closed',  'url','review_count', 'rating', 'phone', 'display_phone', 'distance']
    data.append([restaurant[key] for key in keys])

# スプレッドシートに書き込む
sheet_name = 'シート1'

# スプレッドシートに書き込む
sp.write_to_spreadsheet(mod_global.MyGlobal.SPREADSHEET_KEY, sheet_name, data)
time.sleep(0.1)

