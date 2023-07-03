#---------buckets/buckets.tf-----------
# Build 2 different buckets: #1 for the Raw Data, #2 for 'dataflow'
# variable "bucket_prefix" {
#   description = "Prefix for unique bucket names"
# }

resource "google_storage_bucket" "raw_data_bucket" {
  name          = "raw-data-${var.bucket_prefix}"
  force_destroy = false
  location      = "US"
  storage_class = "STANDARD"

  labels = var.default_label
  versioning {
    enabled = true
  }
}

resource "google_storage_bucket" "data_flow_bucket" {
  name          = "data-flow-${var.bucket_prefix}"
  force_destroy = false
  location      = "US"
  storage_class = "STANDARD"

  labels = var.default_label
  versioning {
    enabled = true
  }
}