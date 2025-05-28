import asyncio
from stockmarketsearch.main import search, get_stock_data
from datetime import datetime, timedelta

async def search_company(query: str):
    # Search for stock information
    results = await search(query)

    today = datetime.today().strftime("%Y-%m-%d")
    five_years_ago = (datetime.today() - timedelta(days=5*365)).strftime("%Y-%m-%d")

    # Check Yahoo Finance
    yahoofinance = results.get("yahoofinance", [])
    if yahoofinance:
        url = yahoofinance[0].get("url")
        if url:
            return await get_stock_data(url=url, start_date=five_years_ago, end_date=today)

    # Check NGInvesting
    nginvesting = results.get("nginvesting", [])
    if nginvesting:
        url = nginvesting[0].get("url")
        if url:
            return await get_stock_data(url=url, start_date=five_years_ago, end_date=today)

    # Check AfricanMarkets
    africanmarkets = results.get("africanmarkets", [])
    if africanmarkets:
        url = africanmarkets[0].get("url")
        if url:
            return await get_stock_data(url=url, start_date=five_years_ago, end_date=today)

    return {"error": "no results found"}

if __name__ == "__main__":
    data = asyncio.run(search_company('apple'))
    print(data)
