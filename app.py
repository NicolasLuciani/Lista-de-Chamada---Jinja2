from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

app = FastAPI()

context = {}

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="item.html", context={"id": id}
    )

@app.get("/")
async def home(request: Request):

    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"context":context}
    )


@app.post("/add")
async def adicionar(request: Request):
    form = await request.form()

    context[f"{len(context)+1}"] = form.get("nome")
    
    return RedirectResponse(url="/", status_code=303)