import aws_iatk

iatk = aws_iatk.AwsIatk(region="us-east-1")

output = iatk.get_physical_id_from_stack(logical_resource_id="StockCheckerFunction",stack_name="sam-remote-invok-sfn")
print(output)
