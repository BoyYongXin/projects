import redis
import svgwrite
from fastapi import FastAPI
from starlette.responses import FileResponse
import os

app = FastAPI()
client = redis.Redis(host="127.0.0.1", port=6379)


def write_text(file_name, pv):
    dwg = svgwrite.Drawing(file_name, (200, 200))
    paragraph = dwg.add(dwg.g(font_size=14))
    paragraph.add(dwg.text(f"当前访问量：{pv}", (10, 20)))
    dwg.save()


@app.get('/')
def index():
    return {'success': True}


@app.get('/pv/{user_id}')
def calc_pv(user_id):
    pv = client.hincrby('pv_count', user_id, 1)
    file_name = f'{user_id}.svg'
    write_text(file_name, pv)
    return FileResponse(file_name)

if __name__ == '__main__':
    #pip3 install uvicorn
    command = "uvicorn server_ceshi:app --host 0.0.0.0 --port 8889 --reload"
    os.system(command)