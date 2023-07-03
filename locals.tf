#---------root/local.tf-----------

#create a default label for all the resources here
locals {
  default_label = {
    project = "DataEngineering"
  }
}