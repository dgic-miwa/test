from selenium import webdriver
from selenium.webdriver.firefox.service import Service # Firefoxの場合、Serviceを使うとより良い
from selenium.webdriver.firefox.options import Options # Optionsクラスをインポート
from selenium.webdriver.common.by import By # 要素を見つけるためのByクラスをインポート
from selenium.webdriver.support.ui import WebDriverWait # 要素の待機処理に使う
from selenium.webdriver.support import expected_conditions as EC # 待機条件に使う
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time

def run_firefox_selenium_example():
    # --- WebDriverのパス設定 ---
    executable_path_value = None # PATHにある場合はNone
    # 例: Windowsの場合 (r'C:\path\to\geckodriver.exe' のようにrをつけてraw文字列にするのがおすすめ)
    # executable_path_value = r'C:\Users\your_user\Downloads\geckodriver.exe'
    # 例: macOS/Linuxの場合
    # executable_path_value = '/Users/your_user/path/to/geckodriver'
    
    geckodriver_service = None
    try:
        binary_path = r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe'
        options = Options()
        options.binary_location = binary_path

        if executable_path_value:
            geckodriver_service = Service(executable_path=executable_path_value)
            driver = webdriver.Firefox(service=geckodriver_service, options=options)
        else:
            # GeckoDriverがPATHにある場合はServiceオブジェクトを直接渡さなくても動作します
            driver = webdriver.Firefox(options=options)

        driver.get('https://atnd.ak4.jp/ja/login')

        # ページのタイトルを出力
        page_title = driver.title
        print(f"ページのタイトル: '{page_title}'")

        # ページの読み込みを少し待つ (必要に応じて調整)
        time.sleep(3)

        company_id = driver.find_element(By.ID, 'form_company_id')
        company_id.send_keys('DgicAkashi')
        login_id = driver.find_element(By.ID, 'form_login_id')
        login_id.send_keys('ka-miwa@dgic.co.jp')
        password = driver.find_element(By.ID, 'form_password')
        password.send_keys('0ixT38LT')
        driver.find_element(By.ID, "submit-button").click()

        # search_box.submit() # フォームを送信（Enterキーを押すのと同じ）
        # search_box.send_keys(Keys.RETURN)
        # driver.find_element(By.NAME, "btnK").click()

        time.sleep(3)

        print(f"検索後のタイトル: {driver.title}")
        print(f"現在のURL: {driver.current_url}")

        try:
            first_result_link = driver.find_element(By.CSS_SELECTOR, 'h3.LC20lb.MBeuO.DKV0Md')
            print(f"リンクをクリックします: {first_result_link.text}")
            first_result_link.click()
            time.sleep(3) # ページの遷移を待つ
            print(f"リンク先のタイトル: {driver.title}")
        except Exception as e:
            print(f"最初の検索結果のリンクが見つかりませんでした: {e}")


    except Exception as e:
        print(f"エラーが発生しました: {e}")
    finally:
        # ブラウザを閉じる
        if 'driver' in locals() and driver:
            print("ブラウザを閉じます。")
            driver.quit()
        else:
            print("ドライバが初期化されていないため、ブラウザを閉じることができませんでした。")

    print("SeleniumのFirefoxテストが完了しました。")

# 関数を実行
if __name__ == "__main__":
    run_firefox_selenium_example()
