#---------root/locals.tf-----------
#default label for all resources 
locals {
  default_label = {
    project     = "data-engineering"
    assignement = "temperature-energy"
    environment = "development"
  }
}