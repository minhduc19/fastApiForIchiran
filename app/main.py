from fastapi import FastAPI
import subprocess
app = FastAPI()


@app.get("/")
async def root():
    result = subprocess.check_output('docker exec -it ichiran-main-1 ichiran-cli -f "一覧は最高だぞ"', shell=True)
    result = result.decode('utf-8')
    return {"Nginx": result}
