terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = ">= 4.35.0"
    }
    google-beta = {
      source  = "hashicorp/google-beta"
      version = ">= 4.35.0"
    }
    cloudflare = {
      source  = "cloudflare/cloudflare"
      version = ">= 3.23.0"
    }
  }
}
