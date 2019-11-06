from storages.backends.s3boto3 import S3Boto3Storage


# static/
def StaticS3Storage(): return S3Boto3Storage(location='static')

# media/
def MediaS3Storage(): return S3Boto3Storage(location='media')
