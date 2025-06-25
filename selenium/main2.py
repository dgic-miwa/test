from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException # 要素が見つからなかった場合の例外
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By # 要素を見つけるためのByクラスをインポート
from selenium.webdriver.support.ui import WebDriverWait # 要素の待機処理に使う
from selenium.webdriver.support import expected_conditions as EC # 待機条件に使う
# from webdriver_manager.chrome import ChromeDriverManager
import argparse


def run_selenium():

    # argparse.ArgumentParserクラスをインスタンス化して、説明等を引数として渡す
    parser = argparse.ArgumentParser(
        prog="Get token",  # プログラム名
        usage="python3 main.py <file_name> <password>", # プログラムの利用方法
        description="Get token script.", # ヘルプの前に表示
        epilog="end", # ヘルプの後に表示
        add_help=True, # -h/–-helpオプションの追加
    )

    # 引数の設定
    parser.add_argument("-u", "--user", type=str, help="UserId")
    parser.add_argument("-p", "--passwd", type=str, help="Password")

    # 引数の解析
    args = parser.parse_args()

    print(f"UserId: {args.user}, Password: {args.passwd}")

    URL = 'https://atnd.ak4.jp/ja/login'

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = None # driver変数を初期化

    wait = WebDriverWait(driver=driver, timeout=30)
    try:
        # service = Service(ChromeDriverManager().install())
        service = Service()
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(URL)
        wait.until(EC.presence_of_all_elements_located)

        company_id = driver.find_element(By.ID, 'form_company_id')
        company_id.send_keys('DgicAkashi')
        login_id = driver.find_element(By.ID, 'form_login_id')
        login_id.send_keys('ka-miwa@dgic.co.jp')
        password = driver.find_element(By.ID, 'form_password')
        # password.send_keys('0ixT38LT')
        password.send_keys('LtCzp4yU')
        driver.find_element(By.ID, "submit-button").click()

        # search_box.submit() # フォームを送信（Enterキーを押すのと同じ）
        # search_box.send_keys(Keys.RETURN)
        # driver.find_element(By.NAME, "btnK").click()

        # 1. 特定の要素が表示されることを確認
        try:
            expected_element_locator = (By.CLASS_NAME, "category-list__item__name")
            expected_text_in_element = "マイページ"
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(expected_element_locator)
            )
            WebDriverWait(driver, 5).until(
                EC.text_to_be_present_in_element(expected_element_locator, expected_text_in_element)
            )
        except TimeoutException as e:
            print(f"画面遷移に失敗")
            raise



        URL_TOKENS = 'https://atnd.ak4.jp/ja/mypage/tokens'
        driver.get(URL_TOKENS)

        expected_element_locator = (By.CSS_SELECTOR, 'a[href="/ja/mypage/tokens/new"]')
        try:
            button_partial_text = 'APIトークン追加'
            btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, f"//p[contains(normalize-space(), '{button_partial_text}')]"))
            )
            print('aaaa')

            btn.click()

            print('bbb')
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, 'cooperate_api_token_access_token_before_encrypt'))
            )

            print('ccc')
            hoge = driver.find_element(By.ID, 'cooperate_api_token_access_token_before_encrypt').get_attribute('value')

            print(hoge)

            search_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "cooperate_api_token_comment"))
            )

            # 3. テキストボックスに文字を入力する
            search_box.send_keys("Py用")


            driver.find_element(By.NAME, "commit").click()

        except TimeoutException as e:
            class CustomError(Exception):
                pass
            raise CustomError("カスタムエラーに変換しました") from e
        except NoSuchElementException:
            print('要素が見つかりませんでした')
        except Exception as e:
            print(f'予期せぬエラーが発生しました: {e}')

        # href="/ja/mypage/tokens/new"

        # wait.until(EC.presence_of_all_elements_located)

        # text_to_find = "パスワードが間違っています"

        # try:

        #     if driver.find_element(By.XPATH, f"//*[contains(text(), '{text_to_find}')]").is_displayed():
        #         print("A")
        #     else:
        #         print("B")


        #     # element = driver.find_element(By.XPATH, f"//*[contains(text(), '{text_to_find}')]")
        #     # print(f"'{text_to_find}' を含む要素が見つかりました: {element.text}")

        #     # first_result_link = driver.find_element(By.CSS_SELECTOR, 'h3.LC20lb.MBeuO.DKV0Md')
        #     # first_result_link.click()
        # except NoSuchElementException:
        #     print(f"'{text_to_find}' を含む要素は見つかりませんでした。")

    except Exception as e:
        print(f"エラーが発生しました: {e}")
    finally:
        # ブラウザを閉じる
        if 'driver' in locals() and driver:
            print("ブラウザを閉じます。")
            driver.quit()
        else:
            print("ドライバが初期化されていないため、ブラウザを閉じることができませんでした。")

    print("Seleniumのテストが完了しました。")

# 関数を実行
if __name__ == "__main__":
    run_selenium()
