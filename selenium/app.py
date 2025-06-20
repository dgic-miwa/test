import subprocess

# 起動したいアプリケーションのパス (例: Notepad)
# 
# app_path = "C:\\Windows\\notepad.exe"
app_path = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"

try:
    # アプリケーションを起動
    result = subprocess.run([app_path], capture_output=True, text=True, check=True)

    # 正常終了した場合の処理 (必要に応じて)
    print("アプリケーション起動成功")
    print("出力:", result.stdout)

except subprocess.CalledProcessError as e:
    # アプリケーションがエラーで終了した場合の処理
    print("アプリケーション起動エラー")
    print("エラーコード:", e.returncode)
    print("エラー出力:", e.stderr)

except FileNotFoundError:
    # アプリケーションが見つからない場合の処理
    print(f"アプリケーションが見つかりません: {app_path}")

except Exception as e:
    # その他のエラー
    print(f"エラーが発生しました: {e}")
