#!/bin/bash

aws s3 cp lab4.txt s3://ds2002met9krd/
aws s3 presign --expires-in 604800 s3://ds2002met9krd/lab4.txt

https://ds2002met9krd.s3.amazonaws.com/lab4.txt?AWSAccessKeyId=AKIA5FTZCZMGKZ5FCC7L&Signature=VdRHDe9099Ta%2BfAbAH3hBEn%2B8lM%3D&Expires=1709847583