#---------root/outputs.tf-----------

# Using the output from the local variable to call the label on all modules and resources
output "default_label" {
  value = local.default_label
}

# Bucket Names
output "raw_data_bucket" {
  value = module.buckets.raw_data_bucket_name
}

output "data_flow_bucket" {
  value = module.buckets.data_flow_bucket_name
}

output "dataset_name" {
    value = module.bigquery.temperature_energy_dataset_friendly_name
}