import os
VERSION = os.environ['VERSION']

deployment_details = [
    {
        'product_name': 'ECR Cross Region Replication',
        'version': VERSION,
        'portfolio': 'Premium - Utilities', # must exist in portfolio table!
        'location': './template.yml',
        'template_constraint': None,
        's3_objects': None,
    }
]