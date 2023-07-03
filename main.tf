#---------root/main.tf-----------

# the random integer will always assign a new number to a resource name
resource "random_integer" "random" {
  min = 1
  max = 100
}

# creates a random id for the buckets
resource "random_id" "bucket_prefix" {
  byte_length = 4
}

module "buckets" {
  source        = "./buckets"
  bucket_prefix = random_id.bucket_prefix.hex
  default_label = local.default_label

}