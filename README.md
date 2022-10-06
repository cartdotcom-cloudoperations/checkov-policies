# Checkov Policies
A repository to house custom Checkov policies for our Terraform code.

## Install
These policies are written in Python and therefore require a Python interpreter to be installed. You can install the `checkov` module via PIP. 
```
#MacOS via Homebrew
brew install python3

#Ubuntu/Debian
sudo apt-get install python3 python3-pip 

pip3 install checkov
```

## Run
This custom policy repository acts as a test suite for our IaC modules. The following commands can be used to run your policies against psuedo architecture located in the `test-infrastructure` directory.
```
checkov -d test-infrastructure/l2 --external-checks-dir policies/
```