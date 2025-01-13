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

# 開始時間を追跡するための辞書
start_times = {}

while True:
    data = None
    for proc in psutil.process_iter():
        # プロセスの名前を小文字にしてマッチング
        match proc.name().lower():
            case "reaper.exe":
                pid = proc.pid  # プロセスIDを取得
                # プロセスが新しく検出された場合、start_time を設定
                if pid not in start_times:
                    start_times[pid] = time.time()
                start_time = start_times[pid]
                data = {
                    "state": state_message,
                    "start": start_time,  # 起動時間を記録
                    "large_image": large_image,
                }
                break

    if data:
        rpc.update(**data)
    else:
        rpc.clear()

    # プロセスの終了を検出して開始時間をリセット
    current_pids = {proc.pid for proc in psutil.process_iter()}
    start_times = {pid: st for pid, st in start_times.items() if pid in current_pids}

    time.sleep(15)  # リッチプレゼンスの更新は15秒に一度に制限されています
