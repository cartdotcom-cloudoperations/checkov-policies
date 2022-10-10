# Database
resource "aws_db_instance" "pass" {
  db_name = "pass"

  tags = {
    "resource" = "aws_db_instance"
    "service"  = "db"
  }
}

resource "aws_db_instance" "fail_wrong_tag_values" {
  db_name = "fail"

  tags = {
    "resource" = "aws_db_instance"
    "service"  = "rds"
  }
}

# Bucket
resource "aws_s3_bucket" "pass" {
  bucket = "pass"

  tags = {
    "resource" = "aws_s3_bucket"
    "service"  = "s3"
  }
}

resource "aws_s3_bucket" "fail_wrong_tag_values" {
  bucket = "fail_wrong_tag_values"

  tags = {
    "resource" = "wrongValue"
    "service"  = "wrongValue2"
  }
}

resource "aws_s3_bucket" "fail_wrong_tag_keys" {
  bucket = "fail_wrong_tag_keys"

  tags = {
    "wrongKey"  = "aws_s3_bucket"
    "wrongKey2" = "s3"
  }
}

resource "aws_s3_bucket" "fail_no_tags" {
  bucket = "fail_no_tags"
}
