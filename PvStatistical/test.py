import redis
import svgwrite
from fastapi import FastAPI
from starlette.responses import FileResponse
import os

app = FastAPI()
client = redis.Redis(host="127.0.0.1", port=6379)
pv = client.hincrby('pv_count', "yang", 1)

def write_text(file_name, pv):
    dwg = svgwrite.Drawing(file_name, (200, 200))
    paragraph = dwg.add(dwg.g(font_size=14))
    paragraph.add(dwg.text(f"当前访问量：{pv}", (10, 20)))
    dwg.save()

write_text('pv.svg', 10)


