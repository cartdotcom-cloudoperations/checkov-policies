from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories


class CartCheck(BaseResourceCheck):
    def __init__(self):
        name = "Validate all AWS resources are following Cart.com naming conventions."
        id = "CKV_CART_001"
        supported_resources = ["aws_*"]
        categories = [CheckCategories.CONVENTION]
        super().__init__(name=name, id=id, categories=categories,
                         supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        self.details = ["""
          This resource is not following the required naming conventions for Cart.com Terraform resources.

          Please refer to this documentation for clarification on naming conventions:
          https://cartdotcom.atlassian.net/l/cp/gDjgH21R
        """]
        return CheckResult.FAILED


check = CartCheck()
