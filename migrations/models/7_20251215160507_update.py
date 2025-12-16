from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `orders` MODIFY COLUMN `user_id` INT NOT NULL;
        ALTER TABLE `orders` ADD INDEX `idx_orders_user_id_f00b6a` (`user_id`);
        ALTER TABLE `orders` ADD INDEX `idx_orders_created_cdc9e7` (`created_at`);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `orders` DROP INDEX `idx_orders_created_cdc9e7`;
        ALTER TABLE `orders` DROP INDEX `idx_orders_user_id_f00b6a`;
        ALTER TABLE `orders` MODIFY COLUMN `user_id` INT;"""


MODELS_STATE = (
    "eJztm21vmzAQx79KlFed1FVt1j2+I2m6ZWuSqaXbtGlCDjiJVbApmLXRlO8+2zyDoU1GOl"
    "h41eR8B74fNvfnSH93LWJA0z0aWrZJVhB233V+dzGw+Ifc2GGnC2w7HuEGCmamcIaBl7CC"
    "mUsdoFM2MAemC5nJgK7uIJsigpkVe6bJjURnjggvYpOH0a0HNUoWkC6hwwZ+/GRmhA14zw"
    "4efLVvtDmCppGaLzL4uYVdoytb2EaYngtHfraZphPTs3DsbK/okuDIG2HKrQuIoQMo5Ien"
    "jsenz2cXpBpm5M80dvGnmIgx4Bx4Jk2k+0gGOsGcH5uNKxJc8LM8752cvj598+LV6RvmIm"
    "YSWV6v/fTi3P1AQWCidtdiHFDgewiMMTfxN0dusASOHF3on4HHppyFF6IqoxcaYnzxkqmI"
    "nwXuNRPiBV2yrydvT0pofVEuBx+UywPm9YxnQ9gy9hf4JBjq+WMcaYzQIeZGCEP/rRAGy+"
    "vfETw+fgzB4+NignwsTRC5GrthoF8SjH3CaAFcsI+TcRmcMxa4qyUZ7fGtgJbw60+nF3zS"
    "luvemsIwUjMcr8f9IQMs8DInRGFyo8dMPRc62kZ3xUTEw7fGmuzuCu6OvKTMb6Q3R04kD/"
    "CcOBAt8Ce4EhxHbEYA67I1GBTR6+Aw9eO3DtdAaI0XtwPuojKbXBosPZYU9JfdQLkaKGfD"
    "roA4A/rNHXAMLUWTj5AeyVgi3/yQ1bOyFoDBQuTPs+BzDsBOHUOohJxs8QdKNQvhLq1gaZ"
    "xgoYQCM4/uDOrIAqYcXxSTIWj4QUdBcK33qIzW2XAwGisXrKQe9jIFIazEp7liqzuQ56cB"
    "KqHIRiiyoBxjOjLLMgg9Cj9UQ7Pq1clSMKbYXAWHLoGrjsbDK1UZf04V5DNFHfKRnrCuMt"
    "aDVxnZEx2k83Wkfujwr53v08lQACQuXTjijLGf+r3L5wQ8SjRM7jRgJCiE1pBUuuDbxpbX"
    "NR35NNe1ciXwv1zYYPI1F3I1LBpN0nEV43sCGZcQLhRaruRBLQg7/3QJTSAyKAQp5NmIHa"
    "ee95IinOuda1nBpEjPhsAe0LRadIFaYVu3e1SZsL31AKaIrjaglwzZp0f2ZHm0HaRL+kal"
    "zwNRTPs8EN00Ntm1yZD9XXfE8HS6Gbh00D6hK1FnJGzW/KU8i5o+9SP4WIGW3FhyhSZZgh"
    "Wg+xwfqbnw0purTn3KEK9E2SXIF+u6ILNW1DVO1LWvV//69WpyZjmSKrwvWISZsIa8bC1r"
    "Ww2/qamOVUjtYKx8e5bqWl1MJ+9D9wTlwcW036rnfe6mt13Xtp2+Xxc26tvlxN5Dfc5MM6"
    "3tdlapiEUrXSKHwxZ7sRbmPexWCDdOCEMLIMlr+2IlHAVUI4V3zm/3QnjOTqxt+kCRCmqI"
    "CH4Clu0vDqv5xeFWlTX1c/Ht62ryt+kNKqu53nsV8qJhDHYpLRTInk+XMnERjJTKCxD7tP"
    "qiQfriF9tH0g5RcWlMhDSz3dZ7+fIRlZF5FVZGMZaujHxrbAAxcG8mwJ38MwM7I4VY0jX4"
    "eDWdFLSC4pAMyGvMEvxhIJ0edkzk0p/1xFpCkWdd3rbMdigP04/8/AD9zaRG9eVl/QfIKb"
    "qF"
)
