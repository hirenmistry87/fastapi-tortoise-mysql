from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `employees` ADD CONSTRAINT `fk_employee_users_65d34571` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `employees` DROP FOREIGN KEY `fk_employee_users_65d34571`;"""


MODELS_STATE = (
    "eJztm21vozgQx79KlFddqVe1ue7D3TuSpre5bZJVS+9Wu1ohB5zEqrEpmG2jVb772eYZDG"
    "2ySQNXXjUZz4Dnh838GdKfXZtaEHsnQ9vBdAVh98/Ozy4BtvhQGDvudIHjJCPCwMAMS2cY"
    "ekkrmHnMBSbjA3OAPchNFvRMFzkMUcKtxMdYGKnJHRFZJCafoHsfGowuIFtClw98+87NiF"
    "jwkR88/OrcGXMEsZWZL7LEuaXdYCtH2kaEXUpHcbaZYVLs2yRxdlZsSUnsjQgT1gUk0AUM"
    "isMz1xfTF7MLU40yCmaauARTTMVYcA58zFLpPpOBSYngx2fjyQQX4iy/9c7O359/+P3d+Q"
    "fuImcSW96vg/SS3INASWCid9dyHDAQeEiMCTf5t0BusASuGl3kn4PHp5yHF6GqohcZEnzJ"
    "ktkRPxs8GhiSBVvyr2d/nFXQ+ke7HnzUro+41xuRDeXLOFjgk3CoF4wJpAlCl+KNEEb+Wy"
    "EMl9fhCJ6ePofg6Wk5QTGWJYg8g98w0A8Fxj7ltAAp2cfpuBzOGQ/c15KM9/hWQCv49afT"
    "KzFp2/PusTSM9BzH23F/yAFLvNwJMZje6AlT34OusdFdMRXx9K2xJrt7B3dHUVLmd8qboy"
    "BSBHhJXYgW5BNcSY4jPiNATNUaDIvobXiY+vFbR2sgsiaL2wUPcZlNLw2eHk8KBstuoN0M"
    "tIthV0KcAfPuAbiWkaEpRmiP5iyxb3HI7tl5CyBgIfMXWYg5h2CnriVVQkG2BAOVmoUKl1"
    "awNE6wMMoALqK7gCayAVbji2NyBK0g6CQMrvUeVdG6GA5GY+2Kl9TjXq4gRJX4vFBsTReK"
    "/AzAFBT5CEM2VGPMRuZZhqEn0Yd60uzyHKwpwatw5VfQ1Ufj4Y2ujT9nKvKFpg/FSE9aVz"
    "nr0buc7okP0vl3pH/siK+dr9PJUBKkHlu48oyJn/61K+YEfEYNQh8MYKU2aWSNwGQrvmNt"
    "eWGzke2FPeiFDSd/SCV3gIeM/5OQe3l8L6DjUsqFQdtTPKmFYZefriEGMoNSkFKfjfhx6n"
    "kvKcO53ruYlUzKBG0E7AlRa8QXqFW2dbtHVSnbex8QhthqA3rpkNf0zJ4uj46LTEXjqPKB"
    "II5pHwjim8YmuzYd8nrXHbV8k20GLhv0mtBVqDMadWt+UZ7FXZ/6EXyuQEtvLLVCUyzBHa"
    "D7nBypufCym6tOjcoIr0LZpciX67ows1bUNU7Ute9Xf/n9anpmBZI6fCxZhLmwhrxtrWpb"
    "Db/omY5VRO1orH15k+laXU0nf0XuKcqDq2m/Vc9tO73turbt9NdyYeO+XUHsPdXnzDXT2m"
    "7nLhWxbKUr5HDUYi/XwqKH3QrhxglhaAOkeG9froTjgN1I4b3z278QnvMTG5s+UGSCGiKC"
    "X4Bl+5PD3fzkcKvKmvm9+PZ1Nf3j9AaV1ULvfRfyopb7+CDKQoP88XSp0hbhSKW6AIlPKy"
    "8aJC9+8G2kbBCVV8ZUSDO7bb23b59RGLlXaWGUY9nCKLbGBhBD92YC3Ms/M/AzMkgUTYO/"
    "b6aTkk5QEpIDeUt4gt8sZLLjDkYe+15PrBUURdbVXct8g/I4+8QvDtDfTGnsvrys/wPFCb"
    "qF"
)
