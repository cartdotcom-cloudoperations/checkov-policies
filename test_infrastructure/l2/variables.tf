variable "deployment_name" {
  type        = string
  description = "The name of the current Terraform deployment."
}

variable "name" {
  type        = string
  description = "(Required) The resource name."
}

variable "region" {
  type        = string
  description = "(Required) The resource's geographical region."
}
