resource "aws_s3_bucket" "pass" {
  bucket = "pass-bucket"

  tags = {
    "key" = "value"
  }
}

resource "aws_s3_bucket" "fail" {
  bucket = "fail-bucket"
}

