#---------root/backend.tf-----------
terraform {
  backend "gcs" {
    bucket = "june-d65d567369d76280-bucket-tfstate"
    prefix = "terraform/state"
  }
}
