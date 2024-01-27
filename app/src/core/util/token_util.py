import secrets


class TokenUtil:
    @staticmethod
    def generateJWTSecret() -> str:
        secretId: str = secrets.token_urlsafe(32)
        print(secretId)



if __name__ == '__main__':
    print(TokenUtil.generateJWTSecret())