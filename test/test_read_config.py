from mu_pipelines_interfaces.config_types.job_config import JobConfigItem

from mu_pipelines_configuration_provider.read_config import read_config


def test_read_config() -> None:
    config: list[JobConfigItem] = read_config(
        "./test/test_job_config.json", list[JobConfigItem]
    )

    first_item: JobConfigItem = config.pop(0)

    assert first_item["execution"][0]["type"] == "IngestCSV"
    assert first_item["destination"][0]["type"] == "jdbc"
