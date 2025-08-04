from pydantic_settings import BaseSettings, SettingsConfigDict

class ProjectSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', extra="ignore")

class SecuritySettings(ProjectSettings):
    OPENROUTER_API_KEY: str


@dataclass
class Settings:
    security: SecuritySettings

    @classmethod
    def load(cls):
        return Settings(security=SecuritySettings())