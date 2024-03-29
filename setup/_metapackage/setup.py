import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-openspp-openspp-dms",
    description="Meta package for openspp-openspp-dms Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-spp_dms>=15.0dev,<15.1dev',
        'odoo-addon-spp_dms_security>=15.0dev,<15.1dev',
        'odoo-addon-spp_scanner_api>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
