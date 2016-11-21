# coding=utf-8
"""
The MIT License (MIT)

Copyright (c) 2016 AraHaan

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
import asyncio
"""
    sasync - Simplified asyncio for simplicity.

    Goal: shortcuts for using asyncio without the pains of importing asyncio directly if you use Python 3.4
    coroutine syntax. Sadly this means this requires use of ``yield from`` keywords.
"""

__all__ = []


def export(defn):
    globals()[defn.__name__] = defn
    __all__.append(defn.__name__)
    return defn


@export
def iscoroutinefunction(coro):
    return asyncio.iscoroutinefunction(coro)


@export
def coroutine(coro):
    return asyncio.coroutine(coro)


@export
def async(coro):
    """
        shorthand for asyncio.coroutine.
    """
    if not iscoroutinefunction(coro):
        coro = coroutine(coro)
    return coro

# event loops.


@export
def Event(*kwargs):
    return asyncio.Event(*kwargs)


@export
def get_event_loop():
    """
    Gets event loop from asyncio.

    Unlike asyncio which does not check if the event loop is closed from within their get_event_loop mine does and
    if it is closed it creates a new event loop to help simplify user code.
    :return: Event loop.
    """
    loop = asyncio.get_event_loop()
    if loop.is_closed():
        loop = new_event_loop()
    return loop


@export
def new_event_loop():
    """
    Creates a new event loop.
    :return: Event loop.
    """
    return asyncio.new_event_loop()

# Tasks


@export
class Task:
    @export
    def all_tasks():
        return asyncio.Task.all_tasks()

@export
def gather(*kwargs):
    return asyncio.gather(*kwargs)


@export
@async
def wait_for(*kwargs):
    ret =  yield from asyncio.wait_for(*kwargs)
    return ret


@export
@async
def wait(*kwargs):
    ret = yield from asyncio.wait(*kwargs)
    return ret

# lock part of Tasks?


@export
def Lock(*kwargs):
    return asyncio.Lock(*kwargs)


@export
def Queue(*kwargs):
    return asyncio.Queue(*kwargs)

# Future


@export
def Future(*kwargs):
    return asyncio.Future(*kwargs)

# Sleep


@export
@async
def sleep(value):
    ret = yield from asyncio.sleep(value)
    return ret
