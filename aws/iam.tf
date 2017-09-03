
resource "aws_iam_user" "ohr-sls" {
  name = "ohr-sls"
}

resource "aws_iam_user_policy" "ohr-sls" {
  name = "ohr-sls-policy"
  user = "${aws_iam_user.ohr-sls.name}"
  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "*",
      "Resource": "*"
    }
  ]
}
EOF
}
