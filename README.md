# Checkov Policies
A repository to house custom Checkov policies for our Terraform code.

## Installation

Developing custom policy checks doesn't necessarily require you to install anything, as they are run entirely in our GitHub Action pipelines via the official Checkov action (https://github.com/bridgecrewio/checkov-action). However,if you want proper intellisense or code completion to operate via your IDE, you can install the `checkov` module via PIP.

```
#MacOS via Homebrew
brew install python3

#Ubuntu/Debian
sudo apt-get install python3-pip 

pip3 install checkov
```