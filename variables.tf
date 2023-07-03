#---------root/variables.tf-----------
variable "gcp_region" {
  type        = string
  description = "Region to use for GCP provider"
  default     = "us-central1"
}

variable "gcp_project" {
  type        = string
  description = "Project to use for this config"
  default     = "cr-lab-aruzza-2706230354"
}