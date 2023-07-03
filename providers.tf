#---------root/providers.tf-----------

terraform {
  required_version = ">= 0.13.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 4.35"
    }
  }
}

provider "google" {
  region  = var.gcp_region
  project = var.gcp_project

}