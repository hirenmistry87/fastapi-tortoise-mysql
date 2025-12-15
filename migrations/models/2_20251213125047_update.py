from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `order_items` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `quantity` INT NOT NULL DEFAULT 1,
    `price` DECIMAL(10,2) NOT NULL,
    `order_id` INT NOT NULL,
    `product_id` INT NOT NULL,
    CONSTRAINT `fk_order_it_orders_b892ad0e` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_order_it_products_aebdc7ef` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS `order_items`;"""


MODELS_STATE = (
    "eJztmltP2zAUgP9K1SeQGIIOGNtbWsrooC2CsCEQitzEbS0cOyQOUCH++2znfoUyStORpz"
    "bnkvh8jn1OTvLUNKkBsbPZNS1MZxA2fzSemgSY4k9Gt9FoAsuKNELAwAhLY+hbSSkYOcwG"
    "OuOKMcAO5CIDOrqNLIYo4VLiYiyEVOeGiEwikUvQnQs1RieQTaHNFdc3XIyIAR/5yf1D61"
    "YbI4iNxHiRIa4t5RqbWVLWI+xQGoqrjTSdYtckkbE1Y1NKQmtEmJBOIIE2YFCcntmuGL4Y"
    "nR9qEJE30sjEG2LMx4Bj4GIWC/eVDHRKBD8+GkcGOBFX+dLa3vm2s/91b2efm8iRhJJvz1"
    "54UeyeoyQwUJvPUg8Y8Cwkxoib60BbmwtezONlggGvMoSBIGIY3TdVghhBk78ZYp0psPOR"
    "BfYpXnyIFeVlgkcNQzJhU364/X27hM5v5axzpJytcat1EQ3la9/bFQa+quXpkghtiudCGN"
    "i/CaG/JpdHcGvrNQS3tooJCl2SIHI0vsui+xyMbcppAVKw+cX9UjhH3HFRt2S4Mb4JaAm/"
    "9nB4IgZtOs4dloKemuJ40W93OWCJlxshBqOFLVLK+Da2OQrBCOi3D8A2tIyGtmiRbVZlts"
    "y0BBAwkYREnCIqP9MObUNmvEwK9hSl+ZcKkzr51sm3ijvhO+deRhnAWWIHUEcmwPnUQp8U"
    "M8Nz2vSdq5mMS+gcdDu9vnLCs8NGK7W3BUllJ5M3dBuK+DTAcihyDUMmzMeY9Eyz9F03gz"
    "/VpNnkMRhDgmf+Yiihq/b63XNV6Z8mksuBonaFpiWls5R0bS+VwsOTNP701KOGOGxcDQdd"
    "SZA6bGLLK0Z26lVTjAm4jGqEPmjAiG1sgTQAk5hY1zLeOLFJz3pilzqxcvBzFCWxNMyg6e"
    "RUg77b4fEZxEByzc5yvNjo8fNUc5Kfgzs3kMZ5LbQyk0yKqrMA2AsVmhZOUF2mVa/EKC7T"
    "7lxAGGKzOejFXT6uS7K9bIYRM8tGes6TaWmZFvrUZVq4Y8yzZOMun7U1Z9nUcHU2H7ik02"
    "dCl6kzUjdgFuIhtSGakGM4kyx7fEiA5C7bdP+iegSLygkutsFDmEETC4sHyMOC3vLtKOcd"
    "5aDbzLsF3wHdaXSm1YWXXFz5+JbTcgvw5pR1MfLFRZ0fWV3RrVxFV7/A+ecXOPGRZUiq8L"
    "HgJky5rcjrnLJmQvdSTfQRAmprfeVyPdFLOBkOfgbmMcqdk2G7rp7rJmfdC6ubnJ9lYt/e"
    "5Ex10upW53tWxBdO/jtoKS+thcWLyboQXrlCGJoA5bxNLa6EQ4f3KYUXzm/xhfCYX1ib94"
    "Ei4bQiRfAHsKy/afqvvmlSIH8mmeYlFF9TmlJAZFPnlBXKKfe8EsjtChRvhzGX1WyxtHZ3"
    "X7EbcqvC3VDqkruhWBpzQPTNVxPgQj6R5VdkkOQ8Kf46Hw4KHv8jlxTIC8IDvDaQzjYaGD"
    "nspppYSyiKqMtbVemu1EbyMU+coL3s9PL8F0RXOyI="
)
