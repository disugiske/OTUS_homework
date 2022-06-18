from typing import List

from jsonplaceholder_requests import get_userdata, get_posts
from models import Base, engine, User, Session, Post
from database import db


def init_table():
    with engine.begin() as conn:
        conn.run_sync(Base.metadata.drop_all)
        conn.run_sync(Base.metadata.create_all)


def create_users(session: AsyncSession):
    users_data: List[dict]
    posts_data: List[dict]
    users_data, posts_data = await asyncio.gather(
        get_userdata(),
        get_posts(),
    )
    for list_data in users_data:
        session.add(
            User(
                name=list_data.get("name"),
                username=list_data.get("username"),
                email=list_data.get("email"),
                # user_id=list_data.get('id')
            )
        )
    await session.commit()

    for post_dict_data in posts_data:
        session.add(
            Post(
                user_id=post_dict_data.get("userId"),
                title=post_dict_data.get("title"),
                body=post_dict_data.get("body"),
            )
        )
    await session.commit()


async def async_main():
    async with async_session() as session:
        await init_table()
        await create_users(session)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
