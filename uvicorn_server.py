import uvicorn


if __name__ == '__main__':
    uvicorn.run('hw_6.task_6:app', port=80, reload=True)