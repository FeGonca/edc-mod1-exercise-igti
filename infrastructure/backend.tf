# Backend configuration require a AWS storage bucket.
terraform {
  backend "s3" {
    bucket = "terraform-state-igti-felipe"
    key    = "state/igti/edc/mod1/desafio_final/terraform.tfstate"
    region = "sa-east-1"
  }
}