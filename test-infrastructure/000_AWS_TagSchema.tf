resource "aws_s3_bucket" "pass" {
  bucket = "pass-bucket"

  tags = {
    "resource" = "aws_s3_bucket"
    "service"  = "s3"
  }
}

resource "aws_s3_bucket" "soft_fail" {
  bucket = "pass-bucket"

  tags = {
    "key" = "value"
  }
}

resource "aws_s3_bucket" "fail" {
  bucket = "fail-bucket"
}

