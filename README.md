# energy-temperature
Data Engineering Project using Google Cloud

<!-- BEGIN_TF_DOCS -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | >= 0.13.0 |
| <a name="requirement_google"></a> [google](#requirement\_google) | ~> 4.35 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_random"></a> [random](#provider\_random) | 3.5.1 |

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_bigquery"></a> [bigquery](#module\_bigquery) | ./bigquery | n/a |
| <a name="module_buckets"></a> [buckets](#module\_buckets) | ./buckets | n/a |

## Resources

| Name | Type |
|------|------|
| [random_id.bucket_prefix](https://registry.terraform.io/providers/hashicorp/random/latest/docs/resources/id) | resource |
| [random_integer.random](https://registry.terraform.io/providers/hashicorp/random/latest/docs/resources/integer) | resource |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_gcp_project"></a> [gcp\_project](#input\_gcp\_project) | Project to use for this config | `string` | `"cr-lab-aruzza-2706230354"` | no |
| <a name="input_gcp_region"></a> [gcp\_region](#input\_gcp\_region) | Region to use for GCP provider | `string` | `"us-central1"` | no |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_data_flow_bucket"></a> [data\_flow\_bucket](#output\_data\_flow\_bucket) | n/a |
| <a name="output_dataset_name"></a> [dataset\_name](#output\_dataset\_name) | n/a |
| <a name="output_default_label"></a> [default\_label](#output\_default\_label) | Using the output from the local variable to call the label on all modules and resources |
| <a name="output_raw_data_bucket"></a> [raw\_data\_bucket](#output\_raw\_data\_bucket) | Bucket Names |
<!-- END_TF_DOCS -->