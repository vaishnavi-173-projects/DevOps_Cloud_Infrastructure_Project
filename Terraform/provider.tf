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
  subscription_id = "2f746031-d747-4853-9a47-46f15c87960c"
}