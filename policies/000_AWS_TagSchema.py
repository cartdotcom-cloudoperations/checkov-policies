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
            tags_object = conf['tags'][0]
            resource_correct = False
            service_correct = False

            # self.details = [self.entity_type]

            if 'resource' in tags_object:
                if (tags_object['resource'] == self.entity_type):
                    resource_correct = True

            if 'service' in tags_object:
                if (tags_object['service'] == self.entity_type.split("_")[1]):
                    service_correct = True

            if service_correct and resource_correct:
                return CheckResult.PASSED

        self.details = ["""
          This resource is insufficiently configured.

          Each AWS resource must have a 'tags' block configured as follows:

          tags = {
            "resource" = <resource_name>
            "service"  = <resource_service>
          }

          <resource_name> should be identical to the terraform resource name.
          - "aws_s3_bucket"
          - "aws_ec2_transit_gateway"
          - etc. . .

          <resource_service> should be the service to which a resource belongs.
          It's typically the first token past the 'aws_' substring.
          - "aws_s3_bucket" -> "s3"
          - "aws_ec2_transit_gateway" -> "ec2"
          - etc. . .

          Please make the required fixes in order to pass this check.
        """]
        return CheckResult.FAILED


check = CartCheck()
