from fastapi import FastAPI
from fastapi.params import Query
from starlette.responses import HTMLResponse


app = FastAPI(title="Hello Request", description="A simple FastAPI application to demonstrate request handling.", version="1.0.0")

@app.get("/")
async def root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": "Welcome to the Hello Request FastAPI application!"}

@app.get("/hello")
async def hello(name: str = "World"):
    """
    A simple endpoint that returns a greeting message.

    - **name**: The name of the person to greet. Defaults to "World".
    """
    return {"message": f"Hello, {name}!"}
# 返回HTML

@app.get("/", response_class=HTMLResponse)
async def root_html():
    return """
    <html>
        <head>
            <title>Hello Request</title>
        </head>
        <body>
            <h1>Welcome to the Hello Request FastAPI application!</h1>
            <p>Use the /hello endpoint to get a personalized greeting.</p>
        </body>
    </html>"""

# =======================================四种参数
#1.路径参数:路径参数写在路径中，使用大括号{}包裹参数名，FastAPI会自动将其解析为函数参数。
@app.get("/items/{item_id}")
async def read_item(item_id: int): #类型注解自动把字符串转换为int，注意：这个类型也可以是其他类型
    """
    Endpoint that demonstrates path parameters.

    - **item_id**: The ID of the item to retrieve.
    """
    return {"item_id": item_id}

# Path参数验证：使用Path类可以对路径参数进行验证和描述。

@app.get("/agents/{agent_id}")
async def get_agent(
    agent_id: int = Path(..., ge=1, le=99999, description="Agent ID"),
):
    return {"agent_id": agent_id}

#2.请求体参数：body参数通常用于POST请求，数据会被放在请求体中。FastAPI会自动将请求体解析为函数参数。

from pydantic import BaseModel, Field

# 定义请求模型，
#Filed 类型注解 ，Filed 可以设置默认值、验证规则等,
class CreateAgentRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=50) # Filed  类型注解 ，Filed 可以设置默认值、验证规则等, 
    model: str = Field(default="gpt-4o") #Field 可以设置默认值、验证规则等,
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    tools: list[str] = Field(default_factory=list)


class AgentResponse(BaseModel):
    id: int
    name: str
    model: str
    temperature: float
    tools: list[str]


@app.post("/agents", response_model=AgentResponse)   # ← response_model 控制输出
async def create_agent(agent: CreateAgentRequest):   # ← Pydantic 自动校验请求体
    # 假装保存到数据库...
    saved = AgentResponse(
        id=1,
        name=agent.name,
        model=agent.model,
        temperature=agent.temperature,
        tools=agent.tools,
    )
    return saved    # FastAPI 自动序列化为 JSON

# 3,。查询参数：查询参数通常用于GET请求，数据会被放在URL的查询字符串中。FastAPI会自动将查询参数解析为函数参数。
from typing import Optional

@app.get("/agents")
async def list_agents(
    page: int = 1,                      # 有默认值 → 可选查询参数
    page_size: int = 20,
    status: Optional[str] = None,       # Optional → 可以不传
    search: str = "",                    # 空字符串默认值
):
    """GET /agents?page=1&page_size=20&status=active&search=coder"""
    # FastAPI 不关心参数在 URL 中的顺序
    return {
        "page": page,
        "page_size": page_size,
        "status": status,
        "search": search,
        "results": f"假装这是第 {page} 页的结果，搜索词='{search}'",
    }
# 4.查询参数验证：使用 Query 类可以对查询参数进行更复杂的验证和描述。
@app.get("/agents")
async def list_agents_v2(
    page: int = Query(default=1, ge=1, description="页码，从 1 开始"),
    page_size: int = Query(default=20, ge=1, le=100, description="每页条数"),
    search: str = Query(default="", max_length=200, description="搜索关键词"),
):
    return {"page": page, "page_size": page_size, "search": search}