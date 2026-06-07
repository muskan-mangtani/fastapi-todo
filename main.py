from fastapi import FastAPI
app = FastAPI()

task_list = [ "study FastAPI" ]

@app.get("/tasks")
def get_tasks():
    return {"tasks": task_list}

@app.post("/tasks")
def add_task(task: str):
    task_list.append(task)
    return { "message " : "started",
              "task": task }

@app.put("/tasks")
def update_task(task: str, new_task: str):
    if task in task_list:
        index = task_list.index(task)
        task_list[index] = new_task
        return { "message": "updated",
                 "task": new_task }
    else:
        return { "message": "task not found" }  
    

@app.delete("/tasks")
def delete_task(task: str):
    if task in task_list:
        task_list.remove(task)
        return { "message": "deleted",
                 "task": task }
    else:
        return { "message": "task not found" }
    
    

    


