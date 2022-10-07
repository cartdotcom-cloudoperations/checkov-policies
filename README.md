# Checkov Policies

A repository to house custom Checkov policies for our Terraform code.

## Install

You must install the Checkov CLI tool in order to run these policies locally. You can reference the [documentation here](https://www.checkov.io/2.Basics/Installing%20Checkov.html) for instructions on how to install Checkov.

## Run

This custom policy repository acts as a test suite for our IaC modules. You can run custom policies against terraform resources in the `test-infrastructure` directory via the `./run-test-suite.sh` command. Alternatively, you can run a single policy test manually with the following command.

```
checkov -f test-infrastructure/<TEST_INFRASTRUCTURE_TERRAFORM_FILE>.tf --external-checks-dir policies -c CKV2_CART_<POLICY_NUMBER>
```

More information on the checkov CLI tool and how to use it can be found here:
https://www.checkov.io/2.Basics/CLI%20Command%20Reference.html
