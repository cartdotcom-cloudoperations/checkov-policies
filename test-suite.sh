#!/usr/bin/env bash

for policy in policies/*.py; do
  file_name=${policy:9}
  policy_number=${file_name:0:3}
  
  if [[ $file_name == "__init__.py" ]]; then
    continue
  else
    checkov -f test-infrastructure/${file_name%.py}.tf --external-checks-dir policies -c CKV_CART_${policy_number}
  fi
done