
from pydantic import BaseSettings


class Settings(BaseSettings):
    API_BASE_URL_V1: str = '/api/v1'
    API_BASE_URL: str = API_BASE_URL_V1
    DB_DATABASE_DRIVER: str
    DB_DATABASE_HOST: str
    DB_DATABASE_PORT: str
    DB_DATABASE_USER: str
    DB_DATABASE_PASSWD: str
    DB_DATABASE_NAME: str
    DB_DATABASE_URL: str   
    API_PAYBILL_BASE_URL: str
    API_PAYBILL_USERNAME: str
    API_PAYBILL_PASSWORD: str
    API_PAYBILL_TOKEN: str
    """
    JWT gerando o secret
    import secrets
    jwt_secret : str = secrets.token_urlsafe
    print(jwt_secret)
    """
    # JWT_SECRET: str = 'pVmI8hPubfDZU67FHq_Od4C8v3myl8J8Wka5y5z9R7EAIaB6hh3oqXRKmQQB5FlIAhPUgf50z3fiWmW4KGXBR1LLD_AS5Zi989UtLzSpgWZWzU4PO7_fHbs7ov3aTfMDr7laviMbMBtTFxWCjZMoCHPaY4ELJp-ODBS6iXbgRrDUVBKN-jULQRJ2hNooVqKzuIViNqlyhU6qlHM-4Dm_P1L6hOcR3ipQm5avwSyAgdwMukA-6nFcu0DENVWWh_J5WYyz_V_9JqKlR2BPx5m1vHug1J-jYX6C9I2oAJ1MsUeTTW_0O0hjdUwC5r8sPNgCFs-JqeYyiMG6r9evAQcVAw'
    JWT_SECRET_ID: str = 'afDjzmNF5Ppm6_SxlDvcVjvydWV3Hwb-ExjKbEVbd64'
    ALGORITHM: str = "HS256"
    # 60 minutos * 24 horas * 7 dias = valido por 7 dias
    # 60 minutos * 1 horas * 1 dia = valido por 1 hora
    ACCESS_TOKEN_EXPIRE_MINUTE: int = 60 * 1 * 1 

    class Config:
        case_sesitive = True
        env_file = './app/.env-settings'

settings: Settings = Settings()