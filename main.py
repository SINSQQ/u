import os
import DRGLIB
import redis
import asyncio
import shutil
import subprocess
import psutil 
import config
from asyncio import get_event_loop
from asyncio import sleep
from mody.Redis import db

async def check(users_py_path):
    for process in psutil.process_iter():
        try:
            if process.name() == "python3" and users_py_path in process.cmdline():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

async def main():
    r = redis.StrictRedis(
        host="monorail.proxy.rlwy.net",
        port=31189,
        password="C5k6l4LcGn2aH36H6lIjCKOFI1IoAgB1",
        decode_responses=True
    )
    try:
        from info import token
    except:
        token = r.get(f'{config.Bot_id}:bote')
        with open('info.py', 'a') as file:
            file.write(f'token = \'{token}\'\n')
            file.close()
    try:
        from info import sudo_id
    except:
        code = r.get(f'{config.Bot_id}:code')
        va = code.split(':')
        sudo_id = va[3]    
        with open('info.py', 'a') as file:
            file.write(f'sudo_id = {sudo_id}\n')
            file.close()

    while not await sleep(10):
        for session in db.smembers(f'{config.APP_NEAM}:{sudo_id}:sessions'):
            folder_name = session[:50]
            folder_path = os.path.join('sessions', folder_name)

            if not os.path.exists(folder_path):
                os.makedirs(folder_path, exist_ok=True)
                users_py_path = os.path.join(folder_path, 'users.py')

                if not os.path.exists(users_py_path):
                    shutil.copy('users.py', users_py_path)

                    if not await check(users_py_path):
                        subprocess.Popen(['python3', users_py_path, session])

if __name__ == '__main__':
    DRGLIB.client.loop.run_until_complete(main())
