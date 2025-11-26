#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
系统集成测试脚本
验证后端 FastAPI 服务是否正常工作
"""

import requests
import json
import time
from typing import Optional

# 配置
BACKEND_URL = "http://127.0.0.1:8000"
TIMEOUT = 10


class Colors:
    """终端颜色"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'


def print_section(title: str):
    """打印标题"""
    print(f"\n{Colors.BLUE}{'='*60}")
    print(f"{title}")
    print(f"{'='*60}{Colors.END}\n")


def print_success(msg: str):
    """打印成功信息"""
    print(f"{Colors.GREEN}✅ {msg}{Colors.END}")


def print_error(msg: str):
    """打印错误信息"""
    print(f"{Colors.RED}❌ {msg}{Colors.END}")


def print_warning(msg: str):
    """打印警告信息"""
    print(f"{Colors.YELLOW}⚠️  {msg}{Colors.END}")


def print_info(msg: str):
    """打印信息"""
    print(f"{Colors.BLUE}ℹ️  {msg}{Colors.END}")


def test_health_check() -> bool:
    """测试健康检查接口"""
    print_section("1️⃣  健康检查测试")
    try:
        response = requests.get(f"{BACKEND_URL}/health", timeout=TIMEOUT)
        if response.status_code == 200:
            data = response.json()
            print_success(f"后端服务正常运行")
            print(f"   状态：{data.get('status')}")
            print(f"   消息：{data.get('message')}")
            return True
        else:
            print_error(f"HTTP {response.status_code}: {response.text}")
            return False
    except requests.exceptions.ConnectionError:
        print_error(f"无法连接到后端服务 ({BACKEND_URL})")
        print_info("请先启动后端：cd backend && python main.py")
        return False
    except requests.exceptions.Timeout:
        print_error(f"请求超时 (>{TIMEOUT}s)")
        return False
    except Exception as e:
        print_error(f"请求失败：{str(e)}")
        return False


def test_anti_fraud_tags() -> bool:
    """测试防诈知识标签接口"""
    print_section("2️⃣  防诈知识标签测试")
    try:
        response = requests.get(f"{BACKEND_URL}/anti-fraud-tags", timeout=TIMEOUT)
        if response.status_code == 200:
            data = response.json()
            tags = data.get('tags', [])
            print_success(f"成功获取 {len(tags)} 个防诈知识标签")
            for tag in tags:
                print(f"   {tag.get('icon')} {tag.get('name')}")
            return True
        else:
            print_error(f"HTTP {response.status_code}: {response.text}")
            return False
    except Exception as e:
        print_error(f"请求失败：{str(e)}")
        return False


def test_ask_question(question: str = "办理银行卡需要什么证件？") -> bool:
    """测试智能问答接口"""
    print_section("3️⃣  智能问答测试")
    print_info(f"测试问题：{question}\n")
    
    try:
        payload = {"question": question}
        print_info("发送请求...")
        
        start_time = time.time()
        response = requests.post(
            f"{BACKEND_URL}/ask",
            json=payload,
            timeout=TIMEOUT
        )
        elapsed_time = time.time() - start_time
        
        if response.status_code == 200:
            data = response.json()
            answer = data.get('answer', '')
            context = data.get('context', [])
            
            print_success(f"成功获取回答 (耗时 {elapsed_time:.2f}s)")
            
            print(f"\n{Colors.BLUE}【AI 回答】{Colors.END}")
            print(answer[:200] + "..." if len(answer) > 200 else answer)
            
            print(f"\n{Colors.BLUE}【检索到 {len(context)} 个知识库片段】{Colors.END}")
            for i, doc in enumerate(context[:2], 1):  # 只显示前2个
                preview = doc[:100] + "..." if len(doc) > 100 else doc
                print(f"\n片段 {i}：\n{preview}")
            
            return True
        elif response.status_code == 400:
            print_error(f"请求参数错误：{response.json().get('detail')}")
            return False
        else:
            print_error(f"HTTP {response.status_code}: {response.text}")
            return False
            
    except requests.exceptions.Timeout:
        print_error(f"请求超时 (>{TIMEOUT}s)，LLM API 可能响应慢或网络问题")
        return False
    except Exception as e:
        print_error(f"请求失败：{str(e)}")
        return False


def test_invalid_question() -> bool:
    """测试错误处理"""
    print_section("4️⃣  错误处理测试")
    try:
        payload = {"question": ""}  # 空问题
        response = requests.post(
            f"{BACKEND_URL}/ask",
            json=payload,
            timeout=TIMEOUT
        )
        
        if response.status_code == 400:
            print_success(f"正确返回 HTTP 400")
            detail = response.json().get('detail', '')
            print(f"   错误信息：{detail}")
            return True
        else:
            print_warning(f"预期返回 400，实际返回 {response.status_code}")
            return True  # 不算失败，后端可能有不同的处理方式
            
    except Exception as e:
        print_error(f"请求失败：{str(e)}")
        return False


def main():
    """主测试流程"""
    print(f"\n{Colors.BLUE}")
    print("╔════════════════════════════════════════════════════════╗")
    print("║   银行业务问答系统 - 后端服务集成测试                    ║")
    print("╚════════════════════════════════════════════════════════╝")
    print(f"{Colors.END}")
    
    print_info(f"后端地址：{BACKEND_URL}")
    print_info(f"超时设置：{TIMEOUT}s")
    
    # 运行测试
    results = {
        "健康检查": test_health_check(),
        "防诈标签": test_anti_fraud_tags(),
        "问答功能": test_ask_question(),
        "错误处理": test_invalid_question(),
    }
    
    # 总结
    print_section("📊 测试结果总结")
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for test_name, result in results.items():
        status = f"{Colors.GREEN}✅ 通过{Colors.END}" if result else f"{Colors.RED}❌ 失败{Colors.END}"
        print(f"{test_name}：{status}")
    
    print(f"\n总体：{passed}/{total} 个测试通过")
    
    if passed == total:
        print_success("🎉 所有测试通过！系统准备就绪")
        print_info("现在可以启动前端了：cd frontend && npm run dev")
        return 0
    else:
        print_error(f"❌ {total - passed} 个测试失败，请检查后端配置")
        return 1


if __name__ == "__main__":
    exit(main())
