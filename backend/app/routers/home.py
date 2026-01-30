#!/user/bin/env python3
# -*- coding: utf-8 -*-

from fastapi import APIRouter
import json

router = APIRouter(prefix="/api/home", tags=["home"])

HOME_CONTENT = {
    "title": "GEP应用平台",
    "subtitle": "生态系统生产总值核算成果应用",
    "hero": """GEP核算已从理论走向实践，生态价值正在变为"真金白银"。从四川巴州的GEP质押贷款，到湖北神农架-襄阳的"水质对赌"补偿，再到重庆开州-宣汉的跨省生态指标交易，全国各地已涌现出融资信贷、生态补偿、市场交易、损害赔偿等多个领域的成功案例，证明了GEP核算能带来实实在在的收益。

当前，虽然国家层面统一的制度设计尚在完善，地方实践也因支持力度不同而进展不一，但"绿水青山就是金山银山"的理念已深入人心。随着国家生态文明建设的深化，更多标准化、市场化的政策工具必将出台，GEP核算的应用前景广阔。率先探索的地方，不仅将获得生态与经济的双重回报，更将在未来的绿色发展格局中占据先机。""",
    "stats": [
        {"label": "应用领域", "value": "5+", "icon": "Grid"},
        {"label": "成功案例", "value": "100+", "icon": "TrendCharts"},
        {"label": "覆盖省份", "value": "20+", "icon": "MapLocation"}
    ]
}

from fastapi import Depends
from app.core.cache import get_redis

@router.get("/")
async def get_home(redis=Depends(get_redis)):   # 注入生命周期连接
    cache_key = "home:content"
    cached = await redis.get(cache_key)
    if cached:
        return json.loads(cached)

    await redis.setex(cache_key, 300, json.dumps(HOME_CONTENT))
    return HOME_CONTENT