from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    
    element: str


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/sum1n/{number}")
def sum_numbers(number: int):
     sum = 0
     for i in range(1, number + 1):
        sum=sum+i
     return {"result":sum}

@app.get("/fibo")
def fibo(n: int):
    n1, n2 = 0, 1
    i = 0
    while i < n - 2:
        next = n1 + n2
        n1 = n2
        n2 = next
        i = i + 1
    return {"result": n2}

@app.post("/reverse")
def reverse(word: str = Header(None)):
    return{"result": word[:: -1]}

names = []
elements = []
@app.put("/list")
async def update_list(item: Item):
    elements.append(item.element)
    return {"result": elements}
    
@app.get("/list")
def show_list():
    return {"result": elements}

@app.post("/calculator")
async def calculator(calculator: str):
    arr = calculator.split(',')
    num1 = int(arr[0])
    num2 = int(arr[2])
    op = arr[1]
    result = -1
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            raise HTTPException(status_code=403, detail={"error": "zerodiv"})
        result = int(num1 / num2)
    else:
        raise HTTPException(status_code=400, detail="Bad Request")
    return {"result": result}

    