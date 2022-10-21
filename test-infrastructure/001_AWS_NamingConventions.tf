resource "aws_ec2_transit_gateway" "pass" {
    tags = merge(var.tags,
      tomap({
        "Name" = "${local.name_prefix}-${var.name}"
        "resource" = "aws_ec2_transit_gateway"
        "service" = "transit_gateway"
    }))
}

resource "aws_ec2_transit_gateway" "fail" {

}