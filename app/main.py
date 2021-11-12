from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from fastapi.middleware.cors import CORSMiddleware
from .config import settings

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]  # for public API(every domain)
# origins = ["https://www.google.com", "https://www.youtube.com"]  # Only for these 2 websites

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Successfully deployed from CI?CD pipeline"}
