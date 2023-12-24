import uvicorn


if __name__ == '__main__':
    uvicorn.run('hw_5.task:app', port=80, reload=True)