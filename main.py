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

db = redis.StrictRedis(
    host=config.host,
    port=config.port,
    password=config.password,
    decode_responses=True
)

async def check(users_py_path):
    for process in psutil.process_iter():
        try:
            if process.name() == "python3" and users_py_path in process.cmdline():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

async def main():
    try:
        from info import token
    except:
        with open('info.py', 'a') as file:
            file.write(f'token = \'{config.token}\'\n')
            file.close()
    try:
        from info import sudo_id
    except:
        with open('info.py', 'a') as file:
            file.write(f'sudo_id = {config.sudo_id}\n')
            file.close()
    
    while not await sleep(10):
        for session in db.smembers(f'{config.APP_NEAM}:{config.sudo_id}:sessions'):
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
