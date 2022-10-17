# Checkov Policies

A repository to house custom Checkov policies and the Checkov configuration for the CloudOps team's IaC modules.

## Install

You must install the Checkov CLI tool in order to run these policies locally. You can reference the [documentation here](https://www.checkov.io/2.Basics/Installing%20Checkov.html) for instructions on how to install Checkov.

## Run

This custom policy repository acts as a test suite for our IaC modules. You can run custom policies against terraform resources in the `test-infrastructure` directory via the `./run-test-suite.sh` command. Alternatively, you can run a single policy test manually with the following command.

`checkov -f test-infrastructure/<TEST_INFRASTRUCTURE_TERRAFORM_FILE>.tf --external-checks-dir policies -c CKV2_CART_<POLICY_NUMBER>`

More information on the checkov CLI tool and how to use it can be found here:
https://www.checkov.io/2.Basics/CLI%20Command%20Reference.html

## Contribute

You can contribute custom policies to this repository by referencing [this documentation.](https://www.checkov.io/3.Custom%20Policies/YAML%20Custom%20Policies.html)

Policies are located in the `policies` directory and adhere to the following naming schema:

`<Sequential 3 Digit Number>_<Provider Targeted>_<Simple Policy Name>.yaml`

You can create a test infrastructure file in the `test-infrastructure` directory that matches the name of your custom policy.

## Config File

A configuration file outlining the specifics of the Checkov configuration used in our module pipelines can be found at `./config.yaml`.