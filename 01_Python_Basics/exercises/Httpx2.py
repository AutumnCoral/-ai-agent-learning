import httpx
import asyncio
import time
import os

async def call_model(
    client: httpx.AsyncClient,
    model_name: str,
    api_key: str,
    prompt: str,
) -> dict:
    """调用单个 LLM 模型（带超时保护）"""
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model_name,
        "messages": [{"role": "user", "content": prompt}],
    }

    try:
        start = time.time()
        response = await client.post(url, json=payload, headers=headers, timeout=30)
        elapsed = time.time() - start

        if response.status_code == 200:
            data = response.json()
            return {
                "model": model_name,
                "content": data["choices"][0]["message"]["content"],
                "elapsed": elapsed,
                "status": "success"
            }
        else:
            return {
                "model": model_name,
                "error": f"HTTP {response.status_code}",
                "elapsed": elapsed,
                "status": "error"
            }
    except httpx.TimeoutException:
        return {
            "model": model_name,
            "error": "timeout",
            "elapsed": 30,
            "status": "error"
        }
    except Exception as e:
        return {
            "model": model_name,
            "error": str(e),
            "elapsed": 0,
            "status": "error"
        }


async def call_multi_model_race(prompt: str, api_key: str) -> dict:
    """多模型竞速：取最快响应"""
    models = ["gpt-4o-mini", "gpt-3.5-turbo", "gpt-4o"]

    async with httpx.AsyncClient() as client:
        tasks = [
            asyncio.create_task(call_model(client, model, api_key, prompt))
            for model in models
        ]

        print(f"🚀 已向 {len(models)} 个模型发出请求...")

        for coro in asyncio.as_completed(tasks):
            result = await coro
            if result.get("status") == "success":
                print(f"🏆 最快模型：{result['model']}（{result['elapsed']:.2f}s）")
                # 取消其他任务
                for task in tasks:
                    if not task.done():
                        task.cancel()
                return result
            else:
                print(f"❌ {result['model']} 失败：{result['error']}")

        return {"error": "所有模型都失败了"}


# 运行
if __name__ == "__main__":
    api_key = os.getenv("OPENAI_API_KEY", "sk-xxx")
    result = asyncio.run(call_multi_model_race("什么是 AI Agent？", api_key))
    print(result)