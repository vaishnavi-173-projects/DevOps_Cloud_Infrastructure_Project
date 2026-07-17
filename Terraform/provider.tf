terraform {
  required_version = ">= 1.5.0"

  required_providers {
    azurerm = {
    source  = "hashicorp/azurerm"
    version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
  subscription_id = "0c9ca277-e8b7-4078-ab3b-dc4b0d2d0f1b"
}