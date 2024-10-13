# constants.py

# ウェブサイトのURL
TARGET_URL = "web_url"

# データファイル名と形式
TARGET_FILE = "target_file"
RECORD = "records"

# 使用ブラウザ
USE_BROWSER = "use_browser"

# 設定タグとコンフィグファイル
SETTING = 'settings'
CONFIG_INI = 'config.ini'

# サポートされているブラウザのリスト
CHROME = '0'
EDGE = '1'

# データカラム名
COLUMN_FIRST_NAME = '名前'
COLUMN_LAST_NAME = '苗字'
COLUMN_COMPANY_NAME = '会社名'
COLUMN_DEPARTMENT = '部署'
COLUMN_ADDRESS = '住所'
COLUMN_EMAIL = 'メールアドレス'
COLUMN_PHONE_NUMBER = '電話番号'

# 入力制御
SUBMIT_BUTTON_SELECTOR = "input[type='submit'][class*='uiColorButton']"
START_BUTTON_CLASS = "uiColorButton"
INPUT_SELECTOR_TEMPLATE = "input[ng-reflect-name*='{}']"

# フィールド名の定数
FIELD_FIRST_NAME = "labelFirstName"  # 名前
FIELD_LAST_NAME = "labelLastName"  # 苗字
FIELD_COMPANY_NAME = "labelCompanyName"  # 会社名
FIELD_DEPARTMENT = "labelRole"  # 部署
FIELD_ADDRESS = "labelAddress"  # 住所
FIELD_EMAIL = "labelEmail"  # メールアドレス
FIELD_PHONE_NUMBER = "labelPhone"  # 電話番号

# その他の定数
PROMPT_CLOSE_BROWSER = "Press Enter to close the browser..."  # ブラウザを閉じるプロンプト
MAIN_FUNCTION_NAME = "__main__"  # メイン関数名
