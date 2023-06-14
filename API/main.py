from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from spleeter.separator import Separator
import os

app = FastAPI()

# 분리 모델 (5개의 음원: bass, drums, other, piano, vocals)
model_name = 'spleeter:5stems'

# 분리 모델 로드
separator = Separator(model_name)

# 분리된 음원을 저장할 디렉토리 경로
output_dir = './output'


# 음원 분리 라우팅
@app.post("/audio")
async def audio(file: UploadFile = File(...)):
    # 파일 저장
    file_path = f"{output_dir}/{file.filename}"
    file_name = os.path.splitext(file.filename)[0]
    with open(file_path, "wb") as f:
        f.write(await file.read())
    # 분리 작업 수행
    separator.separate_to_file(file_path, output_dir)

    # 파일 다운로드 링크 생성
    download_links = {}
    for instrument in ["vocals", "drums", "bass", "piano", "other"]:
        result_file_name = f"{output_dir}/{file_name}/{instrument}.wav"
        download_links[instrument] = result_file_name

    return {
        "message": "Success",
        "filename": file_name,
        "download_links": download_links
            }


# 파일 데이터 제공
@app.get("/output/{file_name}/{instrument}")
async def get_audio(file_name: str, instrument: str):
    file_path = f"{output_dir}/{file_name}/{instrument}"
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        return {"message": "File not found"}
