from fastapi import FastAPI
import subprocess

my_fastapi_app = FastAPI()


@my_fastapi_app.get("/")
async def root():
    result = subprocess.check_output('docker exec -it ichiran-main-1 ichiran-cli -f "一覧は最高だぞ"', shell=True)
    result = result.decode('utf-8')
    return {"Nginx": result}