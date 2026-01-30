#!/user/bin/env python3
# -*- coding: utf-8 -*-

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

import asyncio
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from app.db.base import Base
from app.models.content import Content

# 数据库配置（与 app/db/session.py 一致）
DATABASE_URL = "sqlite+aiosqlite:///./gep.db"
engine = create_async_engine(DATABASE_URL, echo=True)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# 5个模块的内容数据
contents_data = [
    {
        "slug": "financing",
        "title": "融资信贷",
        "subtitle": "GEP价值质押，绿色金融支持",
        "content": "融资信贷是指核算出的GEP（生态系统生产总值）价值作为质押或还款保障，向银行等金融机构申请贷款。实践的经验和教训显示，"
                   "各地在操作流程、质押登记、额度核定上均无统一标准，实际落地高度依赖对地方政策、银行偏好及项目特性的精准把握与设计，"
                   "需进行深度定制化的方案对接。",
        "icon": "Money",
        "sort_order": 1
    },
    {
        "slug": "compensation",
        "title": "生态补偿",
        "subtitle": "双向补偿机制，生态价值回报",
        "content": "生态补偿是依据GEP核算的生态价值，由受益方或上级财政向保护方提供资金或政策支持的核心机制。它主要通过两种路径实现："
                   "在横向市场化补偿中，生态受益方（如下游地区）直接向保护方（如上游地区）进行支付。这类补偿协议的成功关键，在于对触发条件、"
                   "考核指标、动态支付标准等核心条款的周密设计，其复杂性在跨行政区协商中尤为突出，高度依赖精准的利益平衡、科学的成效计量"
                   "与稳固的制度保障。在纵向财政补偿中，则由中央或省级财政基于区域生态功能重要性，通过专项转移支付对重点生态保护区进行定向支持。"
                   "这两种路径共同构成了生态价值回报的完整制度框架，但其具体落地均需结合宏观政策与地方实际进行深度定制化设计。",
        "icon": "ScaleToOriginal",
        "sort_order": 2
    },
    {
        "slug": "trading",
        "title": "市场交易",
        "subtitle": "生态产品市场化，价值实现新路径",
        "content": "市场交易是指将GEP核算出的生态功能量（如碳汇、水质净化量）转化为可交易的标准化产品或权益，在特定市场平台进行买卖的行为。"
                   "此类交易的难点在于，需要构建一套涵盖产品确权、核算核证、定价机制、交易规则、登记结算和监管的完整市场体系。目前国家层面"
                   "尚无统一规范，地方试点在交易标的、规则及流动性上各不相同，实质落地不仅需要严谨的核算基础，更依赖于对交易制度、金融工具"
                   "及潜在买方需求的深入理解和创新设计。",
        "icon": "ShoppingCart",
        "sort_order": 3
    },
    {
        "slug": "damage",
        "title": "生态损害赔偿",
        "subtitle": "损害量化追责，生态修复保障",
        "content": "生态损害赔偿是指在发生生态环境破坏事件后，依据GEP核算等方法，对生态系统服务功能期间损失进行量化，并以此作为向责任方"
                   "提出赔偿诉求的科学依据。其核心挑战在于，损失的科学量化、因果关系的认定、赔偿标准的确定以及赔偿资金的使用监管等环节"
                   "均缺乏细化的操作规范和技术导则。能否成功索赔并获得法院或行政部门支持，极大程度上取决于损害评估方法的权威性、法律程序"
                   "的适配性以及修复方案的可执行性，整个过程需进行高度专业化和个案化的技术准备与司法衔接。",
        "icon": "FirstAidKit",
        "sort_order": 4
    },
    {
        "slug": "others",
        "title": "其它应用",
        "subtitle": "考核规划评估，管理决策支撑",
        "content": "GEP核算在融资信贷等成熟应用外，其成果正深度融入政府决策与绩效考核体系。一是作为生态考核<strong>，纳入地方政府绿色发展评价"
                   "与领导干部离任审计，将保护成效量化可比。二是成为空间规划<strong>，在国土空间规划中明确生态保护与开发边界，"
                   "保障发展不逾越生态阈值。三是支撑项目<strong>，为大型工程建设、产业布局提供生态成本效益预评估，推动优化选址与方案。"
                   "这些应用正推动GEP从核算工具转变为基础性管理标尺。",
        "icon": "Management",
        "sort_order": 5
    }
    ]


# 初始化函数
async def init():
    async with engine.begin() as conn:
        # 确保表存在
        await conn.run_sync(Base.metadata.create_all)

    async with async_session_maker() as session:
        # 清空现有数据（可选，取消注释下行启用）
        # await session.execute(delete(Content))

        for data in contents_data:
            content = Content(**data)
            session.add(content)

        await session.commit()
        print(f"Initialized {len(contents_data)} content records")


# 入口点
if __name__ == "__main__":
    asyncio.run(init())