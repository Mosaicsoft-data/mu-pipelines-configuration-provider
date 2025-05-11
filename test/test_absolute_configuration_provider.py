from mu_pipelines_interfaces.config_types.global_properties.global_properties import (
    GlobalProperties,
)
from mu_pipelines_interfaces.configuration_provider import ConfigurationProvider

from mu_pipelines_configuration_provider.absolute_configuration_provider import (
    AbsoluteConfigurationProvider,
)


def test_AbsoluteConfigurationProvider():
    config_provider: ConfigurationProvider = AbsoluteConfigurationProvider(
        job_config_path="test/test_job_config.json",
        global_properties_path="test/test_global_properties.json",
        connection_config_path="test/test_connection_properties.json",
        secrets_config_path="test/test_secrets_config.json",
    )

    assert config_provider.job_config[0]["execution"][0]["type"] == "IngestCSV"
    assert config_provider.job_config[0]["destination"][0]["type"] == "jdbc"

    assert config_provider.global_properties["library"] == "Mock"

    assert config_provider.connection_config["connections"][0]["type"] == "postgres"

    assert config_provider.secrets_config["secrets"][0]["provider"] == "hardcoded"


def test_AbsoluteConfigurationProvider_load_supporting_artifact():
    config_provider: ConfigurationProvider = AbsoluteConfigurationProvider(
        job_config_path="test/test_job_config.json",
        global_properties_path="test/test_global_properties.json",
        connection_config_path="test/test_connection_properties.json",
        secrets_config_path="test/test_secrets_config.json",
    )

    supporting_artifact: GlobalProperties | None = (
        config_provider.load_job_supporting_artifact(
            "test_global_properties.json", GlobalProperties
        )
    )

    assert supporting_artifact is not None
    assert supporting_artifact["library"] == "Mock"
