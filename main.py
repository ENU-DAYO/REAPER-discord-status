import time
import psutil
import pypresence
import configparser

# 設定ファイルを読み込む
config = configparser.ConfigParser()
config.read('setting.ini')

# 設定ファイルから state を取得
state_message = config.get('RPC', 'state', fallback="EVALUATION LICENSE")  # state の内容

client_id = "1279434241607733339"  # Application ID を直接指定
large_image = "reaper_logo"  # 固定の大きな画像名

rpc = pypresence.Presence(client_id)
rpc.connect()

# 開始時間を記録
start_time = time.time()

while True:
    data = None
    for proc in psutil.process_iter():
        # プロセスの名前を小文字にしてマッチング
        match proc.name().lower():
            case "reaper.exe":
                data = {
                    "state": state_message,
                    "start": start_time,  # 経過時間を表示
                    "large_image": large_image,
                }
                break

    if data:
        rpc.update(**data)
    else:
        rpc.clear()

    time.sleep(15)  # リッチプレゼンスの更新は15秒に一度に制限されています
