"""Custom storage backends for AWS S3."""

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticRootS3Boto3Storage(S3Boto3Storage):
    """
    Custom storage backend for static files on S3.
    """
    location = 'static'
    file_overwrite = True


class MediaRootS3Boto3Storage(S3Boto3Storage):
    """
    Custom storage backend for media files on S3.
    """
    location = 'media'
    file_overwrite = False
