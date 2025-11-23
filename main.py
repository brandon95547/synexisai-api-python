import os

import asyncpg
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from email_utils import send_email
# from other_script import some_function  # Optional: import your other Python logic

app = FastAPI()

# Allow frontend access (adjust origin in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use your domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------- Models ----------

class CommentIn(BaseModel):
    slug: str      # e.g. "the-creation-of-tome-weaver"
    body: str      # comment message text


# ---------- DB Pool ----------

@app.on_event("startup")
async def startup():
    app.state.db_pool = await asyncpg.create_pool(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "5432")),
    )


@app.on_event("shutdown")
async def shutdown():
    await app.state.db_pool.close()


# ---------- Routes ----------

@app.get("/")
def root():
    return {"message": "API is running"}


@app.post("/send-email")
async def email_endpoint(request: Request):
    try:
        data = await request.json()
        result = await send_email(data)
        return {"status": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/comments")
async def create_comment(comment: CommentIn):
    pool = app.state.db_pool

    async with pool.acquire() as conn:
        # 1) Look up the blog post by slug
        row = await conn.fetchrow(
            "SELECT id FROM blog_posts WHERE slug = $1 LIMIT 1",
            comment.slug,
        )
        if not row:
            raise HTTPException(status_code=404, detail="Blog post not found")

        blog_id = row["id"]

        # 2) Insert into comments table
        await conn.execute(
            """
            INSERT INTO comments (blog_id, author, body)
            VALUES ($1, $2, $3)
            """,
            blog_id,
            "Anonymous",     # since there is no name field on the form
            comment.body,
        )

    return {"status": "ok"}
