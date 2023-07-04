#---------bigquery/bigquery.tf-----------

# Creating a Data Set for the 2 different tables:

resource "google_bigquery_dataset" "temperature_energy_dataset" {
    dataset_id = "temperature_energy"
    friendly_name = "temperature_energy_dataset"
    description = "Dataset for the Temperature-Energy Project"
    location = "US"

    labels = {
        project = "data-engineering"
    } #change this to the locals default_label later
}

resource "google_bigquery_table" "temperatures" {
  dataset_id = google_bigquery_dataset.temperature_energy_dataset.dataset_id
  table_id   = "temperatures"

  labels = {
    env = "data-engineering"
  }

  schema = <<EOF
[
  {
    "name": "month",
    "type": "STRING",
    "mode": "NULLABLE",
    "description": "Month of the Year"
  },
  {
    "name": "average_temperature",
    "type": "FLOAT",
    "mode": "NULLABLE",
    "description": "The average temperature's calculation"
  },
  {
    "name": "station_code",
    "type": "STRING",
    "mode": "NULLABLE",
    "description": "The measurement station's code"
  },
  {
    "name": "latitude",
    "type": "FLOAT",
    "mode": "NULLABLE",
    "description": "The measurement station's latitude"
  },
  {
    "name": "longitude",
    "type": "FLOAT",
    "mode": "NULLABLE",
    "description": "The measurement station's longitude"
  }
]
EOF

}
