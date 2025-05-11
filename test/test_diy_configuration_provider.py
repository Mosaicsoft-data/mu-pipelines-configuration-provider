from mu_pipelines_interfaces.config_types.connection_properties import (
    ConnectionProperties,
)
from mu_pipelines_interfaces.config_types.global_properties.global_properties import (
    GlobalProperties,
)
from mu_pipelines_interfaces.config_types.job_config import JobConfigItem
from mu_pipelines_interfaces.config_types.secrets.secrets_config import SecretsConfig
from mu_pipelines_interfaces.configuration_provider import ConfigurationProvider

from mu_pipelines_configuration_provider.diy_configuration_provider import (
    DIYConfigurationProvider,
)
from mu_pipelines_configuration_provider.read_config import read_config


def test_DIYConfigurationProvider():
    config_provider: ConfigurationProvider = DIYConfigurationProvider(
        job_config=read_config("test/test_job_config.json", list[JobConfigItem]),
        global_properties=read_config(
            "test/test_global_properties.json", GlobalProperties
        ),
        connection_config=read_config(
            "test/test_connection_properties.json", ConnectionProperties
        ),
        secrets_config=read_config("test/test_secrets_config.json", SecretsConfig),
    )

    assert config_provider.job_config[0]["execution"][0]["type"] == "IngestCSV"
    assert config_provider.job_config[0]["destination"][0]["type"] == "jdbc"

    assert config_provider.global_properties["library"] == "Mock"

    assert config_provider.connection_config["connections"][0]["type"] == "postgres"

    assert config_provider.secrets_config["secrets"][0]["provider"] == "hardcoded"
