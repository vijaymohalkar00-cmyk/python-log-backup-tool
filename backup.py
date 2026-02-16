import shutil
import datetime
import os

def take_backup(source_folder, backup_folder):
    date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_name = os.path.join(backup_folder, f"backup_{date}")

    os.makedirs(backup_folder, exist_ok=True)
    shutil.make_archive(backup_name, 'zip', source_folder)

    print("Backup created:", backup_name + ".zip")
