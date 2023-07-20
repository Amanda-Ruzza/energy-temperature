#---------bigquery/bigquery.tf-----------

# Data Set for the 2 different tables:

resource "google_bigquery_dataset" "temperature_energy_dataset" {
    dataset_id = "temperature_energy"
    friendly_name = "temperature_energy_dataset"
    description = "Dataset for the Temperature-Energy Project"
    location = "US"
    labels = var.default_label
    
}

resource "google_bigquery_table" "temperatures" {
  dataset_id = google_bigquery_dataset.temperature_energy_dataset.dataset_id
  table_id   = "temperatures"
  labels = var.default_label
  deletion_protection=false

  schema = <<EOF
[
  {
    "name": "station_id",
    "type": "STRING",
    "mode": "NULLABLE",
    "description": "The measurement station's code"
  },
  {
    "name": "station_name",
    "type": "STRING",
    "mode": "NULLABLE",
    "description": "The measurement station's location name"
  },
  {
    "name": "station_state",
    "type": "STRING",
    "mode": "NULLABLE",
    "description": "The measurement station's US State location"
  },
  {
    "name": "latitude",
    "type": "GEOGRAPHY",
    "mode": "NULLABLE",
    "description": "The measurement station's latitude"
  },
  {
    "name": "longitude",
    "type": "GEOGRAPHY",
    "mode": "NULLABLE",
    "description": "The measurement station's longitude"
  },
  {
    "name": "month",
    "type": "DATE",
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
    "name": "measurement_flag",
    "type": "STRING",
    "mode": "NULLABLE",
    "description": "The measurement flag, such as 'precipitation total'"
  },  
  {
    "name": "quality_flag",
    "type": "STRING",
    "mode": "NULLABLE",
    "description": "The quality flag, such as 'temperature too warm for snow'"
  }
  
]
EOF

}

resource "google_bigquery_table" "energy" {
  dataset_id = google_bigquery_dataset.temperature_energy_dataset.dataset_id
  table_id   = "energy"
  deletion_protection=false

  labels = var.default_label

  schema = <<EOF
[
  {
    "name": "location",
    "type": "STRING",
    "mode": "NULLABLE",
    "description": "Region where the energy consumption was measured"
  },
  {
    "name": "fuel_type",
    "type": "STRING",
    "mode": "NULLABLE",
    "description": "The type of fuel consumed"
  },
  {
    "name": "cons_level",
    "type": "FLOAT",
    "mode": "NULLABLE",
    "description": "The consumption level"
  }
  
]
EOF

}

resource "google_bigquery_table" "joined_data" {
  dataset_id = google_bigquery_dataset.temperature_energy_dataset.dataset_id
  table_id   = "joined_data"
  deletion_protection=false

  labels = var.default_label

  schema = <<EOF
[
  {
    "name": "location",
    "type": "STRING",
    "mode": "NULLABLE",
    "description": "The USA location"
  },
  {
    "name": "average_temperature",
    "type": "FLOAT",
    "mode": "NULLABLE",
    "description": "The average temperature's calculation"
  },
  {
    "name": "fuel_type",
    "type": "STRING",
    "mode": "NULLABLE",
    "description": "The type of fuel consumed"
  },
  {
    "name": "cons_level",
    "type": "FLOAT",
    "mode": "NULLABLE",
    "description": "The consumption level"
  }
]
EOF
}

output "temperature_energy_dataset_friendly_name" {
  value = google_bigquery_dataset.temperature_energy_dataset.friendly_name
}