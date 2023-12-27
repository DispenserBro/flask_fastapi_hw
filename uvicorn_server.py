import uvicorn


if __name__ == '__main__':
    uvicorn.run('hw_6.task_3:app', port=80, reload=True)