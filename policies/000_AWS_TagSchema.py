from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories


class CartCheck(BaseResourceCheck):
    def __init__(self):
        name = "Validate all AWS resources have tags that follow the proper schema."
        id = "CKV_CART_000"
        supported_resources = ["aws_*"]
        categories = [CheckCategories.CONVENTION]
        super().__init__(name=name, id=id, categories=categories,
                         supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        if 'tags' in conf.keys():
            self.details = [conf['tags']]
            return CheckResult.PASSED

        self.details = ["""
          This resource is insufficiently configured.

          Each AWS resource must have a 'tags' block configured as follows:

          tags = {
            "resource" = <resource_name>      (i.e. "aws_s3_bucket")
            "service"  = <resource_service>   (i.e. "s3")
          }

          Please make the required fixes in order to pass this check.
        """]
        return CheckResult.FAILED


check = CartCheck()
