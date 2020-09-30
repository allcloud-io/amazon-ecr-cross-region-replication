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
    }
]