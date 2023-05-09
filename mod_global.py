# Yelp Fusion no longer uses OAuth as of December 7, 2017.
# You no longer need to provide Client ID to fetch Data
# It now uses private keys to authenticate requests (API Key)
# You can find it on
# https://www.yelp.com/developers/v3/manage_app

class MyGlobal:
    # クラス変数としてカプセル化
    API_KEY= "ZSbcbAytMl1uddDiPVkghxYAtEYeAR62p_KSAyZgZGbo697YjFXLoSDDPJd4GMRcvcDYifoo72QfnzrB59XqzvcWNG8McqCyCPQYU8t_DHR4o-AYAC3qyaTHx19WZHYx"
    SPREADSHEET_KEY = '1uKjsH6qDm1DnWNn3732ngmr27MK3seyEYJu3AGVVcZQ'
    
    # メソッド
    def say_hello(self):
        print(f"Hello, {self.name}!")