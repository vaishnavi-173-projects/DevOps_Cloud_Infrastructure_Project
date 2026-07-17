variable "resource_group_name" {
  description = "Name of the Azure Resource Group"
  type        = string
  default     = "rg-student-result-notifier"
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "Southeast Asia"
}

variable "vnet_name" {
  description = "Virtual network name"
  type        = string
  default     = "vnet-srn"
}

variable "subnet_name" {
  description = "Subnet name"
  type        = string
  default     = "subnet-srn"
}

variable "acr_name" {
  description = "Azure Container Registry name (must be globally unique, alphanumeric only)"
  type        = string
  default     = "acrsrnterraform26"
}

variable "vm_name" {
  description = "Linux VM name"
  type        = string
  default     = "vm-srn-app"
}

variable "vm_size" {
  description = "VM size"
  type        = string
  default     = "Standard_B2s"
}

variable "admin_username" {
  description = "Admin username for the VM"
  type        = string
  default     = "azureadmin"
}

variable "admin_password" {
  description = "Admin password for the VM"
  type        = string
  sensitive   = true
}

variable "subscription_id" {
  description = "Azure Subscription ID"
  type        = string
}