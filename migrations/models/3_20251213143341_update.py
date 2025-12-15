from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `orders` DROP COLUMN `updated_at`;
        ALTER TABLE `orders` DROP COLUMN `created_at`;
        ALTER TABLE `orders` ADD CONSTRAINT `fk_orders_users_411bb784` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `orders` DROP FOREIGN KEY `fk_orders_users_411bb784`;
        ALTER TABLE `orders` ADD `updated_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6);
        ALTER TABLE `orders` ADD `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6);"""


MODELS_STATE = (
    "eJztmltz2jgUgP8Kw1N2JptJ2PSyfTOXbNkG6CROt9NOxyNsAZrIkmPLTZgO/30l2fLdLq"
    "QQ7KmfgHOxdT5L5xwJ/+ja1ILYOxvZDqZrCLvvOj+6BNjiS0532ukCx4k1QsDAHEtjGFpJ"
    "KZh7zAUm44oFwB7kIgt6poschijhUuJjLITU5IaILGORT9CDDw1Gl5CtoMsVX79xMSIWfO"
    "IXD38698YCQWylxosscW8pN9jakbIxYVfSUNxtbpgU+zaJjZ01W1ESWSPChHQJCXQBg+Ly"
    "zPXF8MXowlBVRMFIY5NgiAkfCy6Aj1ki3C0ZmJQIfnw0ngxwKe7yZ+/i8s3l279eX77lJn"
    "IkkeTNJggvjj1wlASmencj9YCBwEJijLn5HnSNneAlPH5OUPGqQqgEMcN43tQJYgxNfuaI"
    "DVbALUam7DO8+BBryssGTwaGZMlW/OfF3xcVdD5pN4P32s0Jt/pDREP52g+ywjRU9QJdGq"
    "FL8U4Ilf2zEIZr8ngEz8+3IXh+Xk5Q6NIEkWfwLIu+F2DsU04LkJLkl/TL4Jxzx0NNySgx"
    "PgtoBb/+bHYtBm173gOWgrGe4Xg36Y84YImXGyEG44UtSsriPpEchWAOzPtH4FpGTkN7tM"
    "w2r7J7dlYCCFhKQiJOEVVYaWeuJStergQHisr6S4VJW3wbV3wZZQDn0Q2hiWyAi/FFPhmC"
    "VuB0FjrXs7BU0BqOBuOJds0z3Wkvs05VgrzM5cCX716OUEr2MAlzOS6NMM/viroQLckHuJ"
    "YYx3xEgJhFJSPMUnfhZWqHb6NmgJLGo3DBY5TMkhODR8djgsHkG2i3A2046m7Ky0IiETJo"
    "ewX1OHS7+nADMZARlIKU6X7Mr1PrFZzDuTl4bZRMyuqjAvaTGmlED6gtlHXLUVWF8sEHhC"
    "G23oFe0uXl9qkXx2YYM3NcZBbsDSqbi8inbS6ijLHLkk26/K6HI45LLd9ku4FLO/1O6Cpa"
    "M6p2fr/Ym0U7yPoR3LY7Sy6s4vasYAruAd3H+ErNhZdeXLt2t4ds7BTegrYuQb68qQsjaz"
    "u6xnV07RH6Lx+hJ0eWI6nDp5JJmHFryIF6BT599FlPnf8qaicT7bMEaq9DzfVs+o8yT1Ae"
    "XM/6bfe83+7ZdKGIzwAFZXjINQzZsBhj2jPLMnQ9U1/qSbPLY7BmBK/DxVI1fceT0a2uTT"
    "6m5vBQ00dC00vNXyU9eZ1JFNFFOv+N9fcd8bPzZTYdSYLUY0tX3jG207+IlqkLfEYNQh8N"
    "YCWKiJIqMOkzV8d65oNNe7YP9qgPNjq02/K/r9y+uD3qPERHLM/RC9phdb5e3guLA+y2EW"
    "5cIwxtgAr+AyzvhCOH/bTCB+d3+EZ4wW9s7LqhSDk1pAl+AZbtWyUv/lZJprLuo6jWcvYe"
    "pZ5qkG/KVkUVNdRU1lQQ27RFtUFF9TtfRoXHIuX1IOHSzDOm3qtXW5QDblVaDqQuXQ7E0t"
    "gBYmjeTIAHeUuT35FBUrBV/vd2Ni05/4hdMiDvCA/wq4VMdtrByGPf6om1gqKIuvqsLnss"
    "d5re54oL9I/91ubmf58jyc4="
)
