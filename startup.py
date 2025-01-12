import os
import subprocess
from win32com.client import Dispatch

def create_shortcut_and_execute():
    # スクリプト直下にある "reaper discord status.exe" の相対パス
    exe_name = "main/reaper discord status.exe"
    exe_path = os.path.join(os.getcwd(), exe_name)

    # 実行ファイルが存在するか確認
    if not os.path.exists(exe_path):
        print(f"実行ファイルが見つかりません: {exe_path}")
        return

    # ショートカットを作成するパス（スタートアップフォルダ）
    startup_folder = os.path.join(os.getenv('APPDATA'), r"Microsoft\Windows\Start Menu\Programs\Startup")
    shortcut_name = "reaper discord status.lnk"
    shortcut_path = os.path.join(startup_folder, shortcut_name)

    # ショートカット作成
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortcut(shortcut_path)
    shortcut.TargetPath = exe_path
    shortcut.WorkingDirectory = os.path.dirname(exe_path)
    shortcut.IconLocation = exe_path
    shortcut.save()

    print(f"ショートカットが作成されました: {shortcut_path}")

    # 実行ファイルを起動
    try:
        subprocess.Popen([exe_path], shell=True)
        print(f"{exe_name} を実行しました。")
    except Exception as e:
        print(f"{exe_name} の実行中にエラーが発生しました: {e}")

if __name__ == "__main__":
    create_shortcut_and_execute()
