#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import orm
from models import User, Blog, Comment
import asyncio

loop = asyncio.get_event_loop()

async def test():
    await orm.create_pool(loop, user='root', password='133132', db='awesome')
    u = User(name='Test2', email='test2@example.com', passwd='1234567890', image='about:blank')
    await u.save()

loop.run_until_complete(test())
