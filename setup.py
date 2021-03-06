from setuptools import setup, find_packages

setup(
    name='ytbeetdl',
    version='0.0.2',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    scripts=[],

    entry_points={
        'console_scripts': [
            'ytbeetdl = ytbeetdl.application:main'
        ]
    },

    install_requires=[
        "beets>=1.4.9",
        "confuse>=1.3.0",
        "pyyaml>=5.3.1",
        "youtube-dl>=2021.3.25",
    ],

    package_data={
        'ytbeetdl': ['default_config.yaml']
    },

    python_requires='>=3.5.10',

    zip_safe=False,
    description='Download music from youtube-dl and autotag with beets',
    author='Daniel Lovegrove',
    author_email='Daniel.Lovegrove@umanitoba.ca',
    license='MIT',
)
