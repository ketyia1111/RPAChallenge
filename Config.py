import configparser

class Config:
    def __init__(self, config_file):
      # コンストラクタで設定ファイルを読み込む
      self.config_file = config_file
      self.config_data = self.load_config()

    def load_config(self):
      # 設定ファイルを読み込み、辞書として返す
      config = configparser.ConfigParser()
      config.read(self.config_file)
      return config

    def get(self, section, key):
      # 指定されたセクションとキーの設定値を取得する
      return self.config_data.get(section, key)