from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck


class NamingSchema(BaseResourceCheck):
    def __init__(self):
        name = "Validate all Google resource names according to schema."
        id = "CKV_GCP_1000"
        supported_resources = ["google_*"]
        categories = [CheckCategories.CONVENTION]
        super().__init__(name=name, id=id, categories=categories,
                         supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        if 'labels' in conf.keys():
            return CheckResult.PASSED

        self.details.append(
            """ No 'labels' block was defined for the Google resource!
                Labels are utilized for dynamic tagging and are required
                for auditing purposes. The schema for resource labels can be
                found in the organization README file.
            """)
        return CheckResult.FAILED


scanner = NamingSchema()
