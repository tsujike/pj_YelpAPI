import time
import gspread
from google.oauth2.service_account import Credentials

def get_credentials():
    scope = ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive']

    service_account_info = {
        "type": "service_account",
        "project_id": "my-project-test-20200114",
        "private_key_id": "a372fd9a62b0050b09f099f44c7f6431c0721158",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDMiTz4Ux4PVL2b\n7vzBoixQsVfr7SiXY8Ra53w8w8Cea//bKOdMibMFMJoEy4TtgfN3KBfBLvtKQCek\n2+1jXInKfn/0h2S/H8FQzHVrDn2n71yK4ALREHTZYpZ77eujmilE6r4AQ2BaWTJw\nepNHDleNE2DykQ6XEvy27ta1ykvbRuxtwnpWPofclHQrCA4f2cNFWy+4OHxi+/QT\nc965wzSAdKwPOVJZJ5zutiKd2gLiGRWJ3YQVBwDg/ZdcSai81hjW/sXt2crk3MWZ\nhma1kkHlsvdIgI9GCev88GbpnQSSWv/noeD4kYbswQYyVo1EiHRyqBw5D4vUybhS\nlMFdyKSdAgMBAAECggEAP58ixXWJQKiR0CrPGWYaFcGMQTlEao7geYxO01HqnPyo\nGeJHzEF6247qIbqyrvRAqJxigzdbeBWrnza/ySv0OnYN1CC3YFH+3mSy02mvAWlN\npm8WwTQ2vJXTjFoN9ZZS5vqDvm42zvO24lDmdfBKoHnaKqmfWbPQwxBY3jQ+U0bW\nNt9kvjulNNvNybq9nnB67Nz5oacMdx6/mVkqPDRo4ZBpJGujzB2hak6n/i/z+mgC\nqn2LKt3UO39e7XVLcJJUnqDuiJQoVFIuG9IkPs6PB684sLQr39jcohXm+cn5ISL7\nvO4KQ33TXcujDkI2KFfAsiseuatWePBJ5dAb2fZlKwKBgQD1lxwWXobWMBhPXLW7\nRxNvS+2HMmOu/Qwspu1gfXwQD+4K8PCDGeeg3+00Rs6hELfn004D4j9EozDm69xx\nmjSP2sDWR6lQLHnimNLh4h/oVKo6Cl3KRycY+Yo7y92UF2GbSkkl0zhNDJdOfAoK\nUCQ/dCcm5klpum2n1rwb4DE2lwKBgQDVNKavJOo9k1TMQmtfUiIqfbpBa6IUTfRd\nvcc6b86/jKIY54WeYYJIrLAGW+rpVRs3o+JeYYVb6vjrU1VWdNtmU25dIq+67ebf\nIod6MKXe8pzMigtHZanfzeBuiy9GcpJOcdYLWmRl7WlbXL6rrFD0h2gQQam4Fdd+\nAbHvPHm46wKBgAdjyKCTr5L6V4Dr1TwRY3BR5I/Q4Fb/nkIps7LXk8gX8p25qkMH\noISiuEx+ZPFLw3ziStKrGCRElNAeAMAaV8KMXokUFvAmpnQ/DPlnCHbBNW4RqcjQ\nY0jJGXO7KquuGG3HynOs62DGJDdkXBj7WFvgbt0oyMS5q1sFhxt/n3t5AoGAZ3zm\nB4+wj3DrMTZwLdWNNfjPJqAbDSYFnlbW1JuezEV0DQicSBNmjOYdjwigzt97lZdb\n8pn9hG9aocdSXePc9x86K8UBbYe6j8aP4hSo/r3etD2xWdeUDEk/TgkLSnOkZqVE\n0z/uCbeiczFib6v1o6vyLCnjOrKHZedmugwtvT8CgYEA6sBaDpvW9XxbDOBE53t+\nZCmor+tsftHWf7OduZr7P4nqgXZfVP2eI6BixnVIf70s6b5ALgBU+v4RpoNlt4Az\njIFFAcm9PFT1MjxbjMXi/Y8/nOOEkbi2gF7JKRkIY/Bi/C3EQVcoVUngL0kCK2L/\nVk6uZyT9191FgimsbDN5SQw=\n-----END PRIVATE KEY-----\n",
        "client_email": "python@my-project-test-20200114.iam.gserviceaccount.com",
        "client_id": "115796843968907706748",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/python%40my-project-test-20200114.iam.gserviceaccount.com"
    }

    credentials = Credentials.from_service_account_info(service_account_info, scopes=scope)

    return credentials

def write_to_spreadsheet(spreadsheet_key, sheet_name, data):
    '''
    スプレッドシートに出力する関数
    '''
    credentials = get_credentials()
    gc = gspread.authorize(credentials)
    workbook = gc.open_by_key(spreadsheet_key)
    worksheet = workbook.worksheet(sheet_name)

    start_row = len(worksheet.col_values(1)) + 1

    table_range = f'A{start_row}'  # A列の最初の行という意味
    worksheet.append_rows(data, table_range=table_range)

def main():
    spreadsheet_key = '1uKjsH6qDm1DnWNn3732ngmr27MK3seyEYJu3AGVVcZQ'
    sheet_name = 'シート1'

    # 2次元配列を作成する
    data = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]

    # スプレッドシートに書き込む
    write_to_spreadsheet(spreadsheet_key, sheet_name, data)
    time.sleep(0.1)


if __name__ == "__main__":
    main()


