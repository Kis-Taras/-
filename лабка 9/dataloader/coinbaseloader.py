import json
from datetime import datetime
from enum import Enum

import aiohttp
import asyncio
import logging


class Granularity(Enum):
    ONE_MINUTE = 60
    FIVE_MINUTES = 300
    FIFTEEN_MINUTES = 900
    ONE_HOUR = 3600
    SIX_HOURS = 21600
    ONE_DAY = 86400


class CoinbaseLoader:
    def __init__(self, endpoint="https://api.exchange.coinbase.com"):
        self.endpoint = endpoint
        self._logger = logging.getLogger("COINBASE")
        self._logger.info("created")

    async def _get_req(self, path, params=None):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.endpoint}{path}", params=params) as response:
                return await response.text()

    async def get_pairs(self) -> list[dict[str, any]]:
        self._logger.debug("get pairs")
        data = await self._get_req("/products")
        return json.loads(data)

    async def get_stats(self, pair: str) -> dict[str, any]:
        self._logger.debug(f"get pair {pair} stats")
        data = await self._get_req(f"/products/{pair}")
        return json.loads(data)

    async def get_historical_data(self, pair: str, begin: str, end: str, granularity: Granularity) -> list[dict[str, any]]:
        self._logger.debug(f"get pair {pair} history")
        params = {
            "start": begin,
            "end": end,
            "granularity": granularity.value
        }
        # retrieve needed data from Coinbase
        data = await self._get_req(f"/products/{pair}/candles", params)
        # parse response and create DataFrame from it
        return json.loads(data)


async def main():
    logging.basicConfig(level=logging.INFO)
    loader = CoinbaseLoader()
    data = await loader.get_pairs()
    print(data[0:5])  # Вивести перші 5 елементів списку
    data = await loader.get_stats("btc-usdt")
    print(data)
    data = await loader.get_historical_data("btc-usdt", "2023-01-01", "2023-06-30", granularity=Granularity.ONE_DAY)
    print(data[0:5])  # Вивести перші 5 елементів списку


if __name__ == "__main__":
    asyncio.run(main())
