"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
from typing import Dict

import aiohttp
import asyncio

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def get_userdata() -> Dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(USERS_DATA_URL) as resp:
            userdata: dict = await resp.json()
            return userdata


async def get_posts() -> Dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(POSTS_DATA_URL) as resp:
            postdata: dict = await resp.json()
            return postdata
