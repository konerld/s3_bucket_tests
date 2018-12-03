#!/usr/bin/env python
import boto3
from botocore.client import Config
from botocore.client import ClientError


def main(url,
         access_key,
         secret_key,
         bucket_name,
         old_local_path,
         new_local_path,
         cleanup):
    s3 = boto3.resource('s3',
                        endpoint_url=url,
                        aws_access_key_id=access_key,
                        aws_secret_access_key=secret_key)

    bucket = s3.Bucket(bucket_name)
    # Create bucket if it no exist
    if not bucket in s3.buckets.all():
        bucket.create()
        print("Bucket was created")

    bucket.upload_file(old_local_path,'test_s3_file.txt')
    print('Uploaded file to bucket - ok')

    bucket.download_file('test_s3_file.txt', new_local_path)
    print('Downloaded file from bucket')

    if cleanup == True:
        objects = bucket.objects.all()
        objects.delete()
        print('Objects in bucket was deleted!')

        bucket.delete()
        print('Bucket deleted!')
    print('Done!!!')

if __name__ == '__main__':
    main(url='http://10.2.124.6:9007',
        access_key='akey6',
        secret_key = 'privkey6',
        bucket_name = 'mytestbucket',
        old_local_path = './test_s3_file.txt',
        new_local_path='./new_test_s3_file.txt',
         cleanup = True)