import json

import uvicorn
from fastapi import FastAPI, Request, Form, Response
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from QASystem.retgen import get_result


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/generate_response")
async def generate_response(request: Request, questions: str = Form(...)):
    print(questions)
    answer = get_result(questions)
    response_data = jsonable_encoder(json.dumps({"answer": answer}))

    return Response(response_data)


if __name__ == '__main__':
    uvicorn.run("app:app", host='0.0.0.0', port=8000, reload=True)