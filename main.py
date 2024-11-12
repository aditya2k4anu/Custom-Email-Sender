from fastapi import FastAPI, Form, Request, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from email_service import send_email  # Assuming you have a send_email function in email_service.py

app = FastAPI()

# Adding session middleware to handle sessions for logged-in users
app.add_middleware(SessionMiddleware, secret_key="your-secret-key")

templates = Jinja2Templates(directory="templates")  # Assuming you have an HTML template directory

# Login page route
@app.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login")
async def login(request: Request, email: str = Form(...), password: str = Form(...)):
    print("Received email:", email)
    print("Received password:", password)
    if email == "your-email@example.com" and password == "your-password":
        request.session['logged_in'] = True
        return RedirectResponse("/dashboard", status_code=302)
    else:
        return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid credentials"})


# Dashboard page route (email sending page)
@app.get("/dashboard")
async def dashboard(request: Request):
    if request.session.get("logged_in"):
        return templates.TemplateResponse("dashboard.html", {"request": request})
    else:
        return RedirectResponse("/login")

# Email sending function
from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="your-secret-key")

templates = Jinja2Templates(directory="templates")

@app.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(request: Request, email: str = Form(...), password: str = Form(...)):
    print("Received email:", email)  # For debugging
    print("Received password:", password)  # For debugging
    # Simple authentication check (replace with actual authentication logic)
    if email == "your-email@example.com" and password == "your-password":
        request.session['logged_in'] = True
        return RedirectResponse("/dashboard", status_code=302)
    else:
        return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid credentials"})

