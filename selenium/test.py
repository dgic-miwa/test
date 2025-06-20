from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options # Optionsクラスをインポート
import time

# GeckoDriverのパスをここに正確に記述してください
# 例: Windowsの場合: r'C:\path\to\geckodriver.exe'
# 例: macOS/Linuxの場合: '/path/to/geckodriver'
GECKODRIVER_PATH = r'C:\Users\ka-miwa\work\apps\webdriver\geckodriver.exe' # <-- ここを修正！
# GECKODRIVER_PATH = r'/c/Users/ka-miwa/work/repo/test/selenium/geckodriver' # <-- ここを修正！

driver = None # driver変数を初期化

try:
    print(f"GeckoDriverのパス: {GECKODRIVER_PATH}")
    # Serviceオブジェクトを使ってドライバを起動
    # GeckoDriverのPATHが通っている場合は executable_path を指定しなくてもOK

    # binary_path = r'"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"'
    binary_path = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
    # binary_path = r'"/c/Program Files (x86)/Mozilla Firefox/firefox.exe"'

    # FirefoxOptionsオブジェクトを作成
    options = Options()
    # Firefoxの実行ファイルのパスを設定
    options.binary_location = binary_path
    
    # service = Service() でも動作する
    service = Service(executable_path=GECKODRIVER_PATH)
    driver = webdriver.Firefox(service=service, options=options)
    print("Firefoxブラウザが正常に起動しました。")
    print("3秒待機します...")
    time.sleep(3) # 起動したのを確認できるように少し待つ
    print("ブラウザを閉じます。")

except Exception as e:
    print(f"エラーが発生しました: {e}")
    print("考えられる原因:")
    print("1. GeckoDriverのパスが間違っている。")
    print("2. GeckoDriverのバージョンがFirefoxのバージョンと互換性がない。")
    print("3. Firefoxブラウザがインストールされていない、または破損している。")
    print("4. GeckoDriverに実行権限がない（macOS/Linuxの場合）。")
finally:
    if driver: # driverがNoneでないことを確認
        driver.quit()
