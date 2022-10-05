from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck


class AWSTagSchemaDuplicate(BaseResourceCheck):
    def __init__(self):
        name = "Validate all AWS resources have tags that follow the proper schema. (Duplicate)"
        id = "CKV_CART_0001"
        supported_resources = ["aws_*"]
        categories = [CheckCategories.CONVENTION]
        super().__init__(name=name, id=id, categories=categories,
                         supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        if 'tags' in conf.keys():
            return CheckResult.PASSED
        else:
            self.details.clear()
            self.details.append("""
            No 'tags' block was defined for the AWS resource!
            Tags are required for auditing purposes.
            The schema for resource labels can be found in the 
            `cartdotcom-cloudoperations` organization README file.
            """)
            return CheckResult.FAILED


scanner = AWSTagSchemaDuplicate()
