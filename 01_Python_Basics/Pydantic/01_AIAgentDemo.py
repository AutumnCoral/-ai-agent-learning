from pydantic import BaseModel, Field, ConfigDict, field_validator
from datetime import datetime
from typing import Optional
from enum import Enum


# ===== 枚举类型 ：这就像给Agent装了一个"状态指示灯"，任何时候你问它"你在干嘛？"，它只能回答这六种情况之一。=====
class AgentStatus(str, Enum):
    """Agent 运行状态"""
    IDLE = "idle" #空闲 Agent什么都没做，在等指令
    THINKING = "thinking" #思考中 Agent正在"动脑子"想怎么回答（调用LLM）
    EXECUTING = "executing"# 执行中	Agent正在执行某个工具（比如调用API、查数据库）
    WAITING_USER = "waiting_user"#等待用户	Agent需要用户进一步输入（比如问"你确认吗？"） 
    COMPLETED = "completed"#已完成	Agent的任务全部做完了
    ERROR = "error"#错误	Agent出错了

#消息是谁发的
class MessageRole(str, Enum):
    """消息角色"""
    SYSTEM = "system" #系统	这条消息是"系统设定"（比如"你是一个AI助手"）
    USER = "user" #用户	这条消息是用户发的
    ASSISTANT = "assistant" #助手	这条消息是AI助手发的
    TOOL = "tool" #工具	这条消息是工具返回的结果（比如"天气查询工具返回了'晴'）

#1.创建会话请求
# ===== 请求模型 ：用户发个系统的数据=====
class CreateSessionRequest(BaseModel):
    """创建 Agent 会话请求"""
    model_config = ConfigDict(extra="forbid") #model_config	模型配置	就是这个模型的"设置面板，extra="forbid"	多余字段="禁止"	如果你多传了没定义的字段，直接报错（严格模式）

    user_message: str = Field( #Field(...)	字段配置	...（三个点）表示"必填"，必须要有值
        ...,
        min_length=1,
        max_length=10000,
        description="用户的初始消息",
    )
    agent_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Agent 名称",
    )
    model: str = Field(
        default="gpt-4o",#default	默认值	如果你不传，就默认用gpt-4o
        pattern=r"^(gpt-4o|gpt-3.5-turbo|claude-3|deepseek-v3)$",#pattern	正则表达式	只允许这四种模型名称，其他的一律报错
        description="使用的模型",#r"^(...)$"	正则字符串	^开头，$结尾，中间用|表示"或"（懂正则就行）
    )
    temperature: float = Field(#temperature	温度	控制AI回答的"创造性"，越高越随机
        default=0.7,
        ge=0.0,#greater equal	大于等于	温度不能小于0
        le=2.0,#less equal	小于等于	温度不能大于2
    )
    system_prompt: Optional[str] = Field( #system_prompt	系统提示词	就是"AI的角色设定"，比如"你是一个帮助用户写代码的助手"，Optional[str]	可选字符串	可以传，也可以不传（传None）
        default=None, #default=None	默认值=空	如果你不传，它就是空的
        max_length=8000,
        description="自定义系统提示（可选）",
    )
#自定义验证器：检查消息不能全是空格
    @field_validator("user_message")#@field_validator	字段验证器装饰器	给user_message加一个"自定义检查"
    @classmethod #@classmethod	类方法装饰器	这个方法是属于"类本身"的，不是属于某个对象的
    def message_not_empty(cls, v: str) -> str: #cls  类本身	就是CreateSessionRequest这个类，v	字段值	就是user_message的值,value的缩写
        if v.strip() == "":#如果去掉空格后是空	strip()会去掉字符串首尾的空格
            raise ValueError("消息不能全是空白字符") #抛出值错误	主动报错，告诉调用者"你传的不对"
        return v.strip() #返回去掉空格后的值	顺便把首尾空格自动清掉

# ===== 模型2：请求模型 ：发送消息到已有会话 =====
class SendMessageRequest(BaseModel):
    """发送消息到已有会话"""
    model_config = ConfigDict(extra="forbid")

    session_id: str = Field(
        ...,
        pattern=r"^sess-[a-zA-Z0-9]{8}$",
        description="会话 ID",
    )
    message: str = Field(
        ...,
        min_length=1,
        max_length=10000,
        description="用户消息",
    )


# ===== 模型3：响应模型 =====
class MessageResponse(BaseModel):#消息响应	"我返回给你的是一条消息"
    """单条消息响应"""
    role: MessageRole #角色	这条消息是谁发的（用上面定义的MessageRole枚举）
    content: str #内容	消息的正文
    timestamp: datetime = Field(default_factory=datetime.now) #时间戳	消息的时间，默认是现在，默认工厂	每次创建对象时，调用datetime.now()生成当前时间

# 模型4：工具调用记录
class ToolCallResponse(BaseModel):#工具调用响应	Agent调用了一个工具后的记录
    """工具调用记录"""
    tool_name: str #工具名	比如"get_weather"（查天气）
    params: dict = Field(default_factory=dict) #	参数	调用时传的参数，比如{"city":"成都"}
    result: Optional[str] = None
    success: bool = False
    duration_ms: float = 0.0 #耗时	调用工具花了多少毫秒
    timestamp: datetime = Field(default_factory=datetime.now) #时间戳	调用工具的时间，默认是现在

# ===== 模型5：响应模型 ：会话详情、会话列表、错误响应 =====
class SessionResponse(BaseModel):
    """会话详情响应"""
    session_id: str  # 会话 ID
    agent_name: str#Agent 名称
    model: str#使用的模型
    status: AgentStatus#Agent 运行状态
    messages: list[MessageResponse] = Field(default_factory=list)#消息列表	这个会话里所有的消息，默认是空列表
    tool_calls: list[ToolCallResponse] = Field(default_factory=list)#工具调用记录列表	这个会话里所有的工具调用记录，默认是空列表
    created_at: datetime#创建时间	这个会话什么时候创建的
    updated_at: datetime = Field(default_factory=datetime.now)#更新时间	这个会话最后一次更新的时间，默认是现在
    token_usage: int = Field(default=0, description="累计 token 消耗")#累计 token 消耗	这个会话里所有消息和工具调用的 token 总消耗，默认是 0

# 模型6：会话列表响应
class SessionListResponse(BaseModel):
    """会话列表响应"""
    total: int #总数	总共有多少个会话
    sessions: list[SessionResponse]#会话列表	这个列表里是所有的会话详情
    page: int = 1#页码	当前是第几页，默认是 1
    page_size: int = 20#每页大小	每页显示多少个会话，默认是 20


# 模型7：错误响应
class ErrorResponse(BaseModel):
    """统一错误响应"""
    error_code: str
    message: str
    detail: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.now)