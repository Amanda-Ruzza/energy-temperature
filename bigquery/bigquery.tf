#---------bigquery/bigquery.tf-----------

# Creating a Data Set for the 2 different tables:

resource "google_bigquery_dataset" "temperature_energy_dataset" {
    dataset_id = "temperature_energy"
    friendly_name = "temperature_energy_dataset"
    description = "Dataset for the Temperature-Energy Project"
    location = "US"

    # labels = {
    #     project = "DataEngineering"
    # } #change this to the locals default_label later
}