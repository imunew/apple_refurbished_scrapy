# -*- coding: utf-8 -*-
import boto3
import os
from scrapy.conf import settings


class S3UploaderPipeline(object):
    BUCKET_NAME = 'apple-refurbished'
    OUTPUT_DIR = '.output'
    bucket = None

    def open_spider(self, spider):
        aws_access_key_id = settings.get('AWS_ACCESS_KEY_ID')
        aws_secret_access_key = settings.get('AWS_SECRET_ACCESS_KEY')
        region_name = settings.get('AWS_REGION_NAME')

        boto3.setup_default_session(aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key,
                                    region_name=region_name)
        s3 = boto3.resource('s3')
        self.bucket = s3.Bucket(self.BUCKET_NAME)

    def close_spider(self, spider):
        with open(os.path.join(self.OUTPUT_DIR, 'items.json'), 'rb') as f:
            self.bucket.put_object(Key='items.json', Body=f, ContentType='application/json', ACL='private')
