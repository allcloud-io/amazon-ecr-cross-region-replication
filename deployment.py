import os
VERSION = os.environ['VERSION']

deployment_details = [
    {
        'product_name': 'ECR Cross Region Replication',
        'version': VERSION,
        'portfolio': 'AllCloud Portfolio - Utilities', # must exist in portfolio table!
        'location': './template.yaml',
        'template_constraint': None,
        's3_objects': None,
        'support_url': "https://allcloud.atlassian.net/wiki/spaces/AWSPRACTICE/pages/897744906/ECR+Cross-Region+Replication"
    }
]
