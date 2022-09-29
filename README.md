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
This custom policy repository acts as a test suite for our IaC modules. The following commands can be used to run your policies against psuedo architecture located in the `test_infrastructure` directory.
```
checkov -d test_infrastructure/l2 --external-checks-dir l2/
checkov -d test_infrastructure/l3 --external-checks-dir l3/
checkov -d test_infrastructure/l4 --external-checks-dir l4/
```