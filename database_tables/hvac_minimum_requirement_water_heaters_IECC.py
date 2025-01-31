import sqlite3

from database_tables.hvac_minimum_requirement_water_heaters import (
    HVACMinimumRequirementWaterHeaters,
)

TABLE_NAME = "hvac_minimum_requirement_water_heaters_IECC"


class HVACMinimumRequirementWaterHeatersIECCTable(HVACMinimumRequirementWaterHeaters):
    def __init__(self):
        super(HVACMinimumRequirementWaterHeatersIECCTable, self).__init__(
            table_name=TABLE_NAME,
            initial_data_directory=f"database_files/{TABLE_NAME}",
        )
