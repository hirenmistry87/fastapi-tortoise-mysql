from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `orders` ADD `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6);
        ALTER TABLE `orders` ADD `updated_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6);
        ALTER TABLE `order_items` ALTER COLUMN `quantity` DROP DEFAULT;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `orders` DROP COLUMN `created_at`;
        ALTER TABLE `orders` DROP COLUMN `updated_at`;
        ALTER TABLE `order_items` ALTER COLUMN `quantity` SET DEFAULT 1;"""


MODELS_STATE = (
    "eJztml1vmzAUhv9KlKtO6qo26z7vSJpu2Zpkauk2bZqQA05i1dgUzNpoyn+fbTDfsKRrFl"
    "C5anN8DtgPts/rA7+7NrUg9o6GtoPpCsLuu87vLgG2+CfXdtjpAseJW4SBgRmWzjD0klYw"
    "85gLTMYb5gB7kJss6JkuchiihFuJj7EwUpM7IrKITT5Btz40GF1AtoQub/jxk5sRseA9v3"
    "j407kx5ghiK9VfZIl7S7vBVo60jQg7l47ibjPDpNi3SezsrNiSksgbESasC0igCxgUl2eu"
    "L7ovehcOVY0o6GnsEnQxEWPBOfAxSwx3QwYmJYIf740nB7gQd3neOzl9ffrmxavTN9xF9i"
    "SyvF4Hw4vHHgRKAhO9u5btgIHAQ2KMufkedI2t4CUi/k5Q8apCqAwxw3je1AliDE3+zREb"
    "LIFbjEz5Z3jxLtaUlw3uDQzJgi35z5O3JxV0vmiXgw/a5QH3eiZGQ/naD3aFSdjUC9rSCF"
    "2Kt0Ko/B+EMFyT+yN4fLwJwePjcoKiLU0QeQbfZdGvAox9ymkBUrL5JeMyOGc8cFdTMtoY"
    "HwS0gl9/Or0QnbY97xZLw0jPcLwe94ccsMTLnRCD8cIWKWV+k9gchWEGzJs74FpGroX2aJ"
    "lvvsnu2VkLIGAhCYlxilGFmXbqWjLj5VJw0FCZf6lwaZNv45IvowzgPLozaCIb4GJ8UUyG"
    "oBUEHYXB9UwsFbTOhoPRWLvgO91hL7NO1QZ5mtsDTReK8RmAFVDkLQzZsBhjOjLLMgw9Uv"
    "/Uk2aXj8GaErwKZ34FXX00Hl7p2vhzaqM80/ShaOlJ6ypjPXiVSUfRRTpfR/qHjvjZ+T6d"
    "DCVB6rGFK+8Y++nfu6JPwGfUIPTOAFZikSqrApN6sL5jPfDBpiPbB7vXBxt2fp/HjT1ov0"
    "fIGjlRkkaY53dOXYgW5BNcSYwj3iNAzCKNF8qK6/AytcO3VjNAWeNeuOAuUh/JicFHx8cE"
    "g2wx0K4G2tmwuy7XcQnlwqDtFQjoMOz80yXEQI6gFKTUZyN+nXruJWU41zsXs5JJmaBVwP"
    "4iao3oAbXKtm57VJWyvfUBYYittqCXDHmqhSXHRWbBeb7yQBDFtAeCaNPYZtUmQ57uvKOW"
    "b7LtwKWDnhK6CnVGVbXmH+VZVPWpH8FNBVpyYRUrtIIp+AjoPsdXai689OLaVuDuUtspvA"
    "XKLkG+XNeFI2tFXeNEXfva659feyV7liOpw/uSSZgJa8hLsKqy1fCbnqpYKWoHY+3bs1TV"
    "6mI6ea/cE5QHF9N+q57bcnpbdW3L6U/lwUZ1uw3fV+fOxW21cxeKWJbSC+SwKrGXa2FRw2"
    "6FcOOEMLQBKnhvX66Eo4DHkcI757d7ITznNza2PVCkghoigv8Dy/ZLsP/+JVgmsz5GUq3l"
    "7N1LPtUgP5QtizJq2FKZU0Hs0ybVBiXVX3wZFZZFyvNBIqSZNabey5cbpAPuVZoOZFs6HY"
    "ilsQXE0L2ZAHfyZTW/I4Ok4Kj88Wo6Kal/xCEZkNeED/CHhUx22MHIYz/ribWCohh1da0u"
    "W5Y7TJ9zxQX6+/7Sev0HqwD53A=="
)
