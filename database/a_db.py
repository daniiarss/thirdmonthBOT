import aiosqlite
from database import sql_queries


class DaniiarDatabase:
    def __init__(self, db_path="db.sqlite3"):
        self.db_path = db_path

    async def create_tables(self):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(sql_queries.CREATE_USER_TABLE_QUERY)
            await db.execute(sql_queries.CREATE_PROFILE_TABLE_QUERY)
            await db.execute(sql_queries.CREATE_LIKE_DISLIKE_TABLE_QUERY)
            await db.execute(sql_queries.CREATE_REFERENCE_TABLE_QUERY)

            try:
                await db.execute(sql_queries.ALTER_TABLE_USER_TABLE_V1)
                await db.execute(sql_queries.ALTER_TABLE_USER_TABLE_V2)
            except aiosqlite.OperationalError:
                pass


            await db.commit()
            print("Database created successfully")

    async def execute_query(self, query, params=None, fetch="none"):
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(query, params or ())


            if fetch == "none":
                await db.commit()
                return
            elif fetch == "one":
                data = await cursor.fetchone()
                return dict(data) if data else None
            elif fetch == "all":
                data = await cursor.fetchall()
                return [dict(row) for row in data] if data else None
