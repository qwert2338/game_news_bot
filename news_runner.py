import asyncio
from main import bot, ADMIN_ID
from parsers import steam, playstation, xbox, epic, fortnite, roblox
from db.models import SessionLocal, News, init_db

init_db()

async def send_news(news_list):
    session = SessionLocal()
    for item in news_list:
        # проверяем, есть ли уже новость
        exists = session.query(News).filter_by(title=item["title"], url=item["url"]).first()
        if exists:
            continue

        # добавляем в базу
        new_entry = News(title=item["title"], url=item["url"])
        session.add(new_entry)
        session.commit()

        # отправляем в Telegram
        try:
            await bot.send_message(
                ADMIN_ID,
                f"📰 {item['title']}\nСсылка: {item['url']}"
            )
        except Exception as e:
            print("Ошибка отправки:", e)
    session.close()

async def check_all_news():
    all_news = []
    all_news.extend(steam.get_steam_news())
    all_news.extend(playstation.get_ps_news())
    all_news.extend(xbox.get_xbox_news())
    all_news.extend(epic.get_epic_news())
    all_news.extend(fortnite.get_fortnite_news())
    all_news.extend(roblox.get_roblox_news())
    await send_news(all_news)

async def scheduler():
    while True:
        await check_all_news()
        await asyncio.sleep(600)  # проверяем каждые 10 минут

if __name__ == "__main__":
    asyncio.run(scheduler())
