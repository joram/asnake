#!/usr/bin/env python
from typing import List

import sentry_sdk
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import FileResponse

import settings
from enums import Directions
from models import Game, Board, Snake, Coord
from responses import RootResponse, MoveResponse
from utils import closest, direction

app = FastAPI()


def init_sentry():
    if settings.SENTRY_DSN is not None:
        sentry_sdk.init(dsn=settings.SENTRY_DSN)


init_sentry()


@app.middleware("http")
async def sentry_exception(request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        with sentry_sdk.push_scope() as scope:
            scope.set_context("request", request)
            sentry_sdk.capture_exception(e)
        raise e


@app.get('/')
async def root() -> RootResponse:
    return RootResponse(
        author="Arthur",
        color="#b04202",
        head="beluga",
        tail="hook",
    )


@app.get('/favicon.ico')
async def favicon():
    return FileResponse("./snake.png")


@app.post('/start')
async def start():
    return {}


class MoveRequest(BaseModel):
    game: Game
    turn:   int
    board: Board
    you: Snake


def moveFunc(request: MoveRequest) -> Directions:
    target = closest(request.you.head, request.board.food)
    if target:
        return direction(request.you.head, target)

    print(request.board)
    if request.you.head == Coord(x=0,y=0):
        return Directions.UP
    if request.you.head == Coord(x=0,y=request.board.height-1):
        return Directions.RIGHT
    if request.you.head == Coord(x=request.board.width-1,y=request.board.height-1):
        return Directions.DOWN
    if request.you.head == Coord(x=request.board.width-1,y=0):
        return Directions.LEFT

    if request.you.head.y == request.board.height-1:
        return Directions.RIGHT

    if request.you.head.x == request.board.width-1:
        return Directions.DOWN

    if request.you.head.x == 0:
        return Directions.UP

    if request.you.head.y == 0:
        return Directions.LEFT

    return Directions.DOWN


@app.post('/move')
async def move(request: MoveRequest) -> MoveResponse:
    move = moveFunc(request)
    print(f"({request.you.head.x}, {request.you.head.y}), {move}")
    return MoveResponse(move=move)


@app.post('/end')
async def end():
    return {}


if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=2303, reload=True)
