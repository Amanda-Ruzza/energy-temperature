#---------variables/buckets.tf-----------

variable "bucket_prefix" {
    description = "Prefix for unique bucket names"
    default = "251"
}

variable "default_label" {
    description = "Default GCP label for buckets and all the project resources"
}