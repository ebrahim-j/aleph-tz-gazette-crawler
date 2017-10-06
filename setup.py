from setuptools import setup

setup(
    name='aleph_tz_gazette_crawler',
    entry_points={
        'aleph.crawlers': [
            'TZ_gazettes = aleph_tz_gazette_crawler.crawler:Crawler',
        ]
    },
    version='0.2',
    description='Aleph crawler to index Tanzania government gazettes archived at https://s3-eu-west-1.amazonaws.com/cfa-gazeti-archive/gazettes/TANZANIA/',
    url='https://github.com/gazeti/aleph-tz-gazette-crawler',
    author='Code For Africa',
    author_email='info@codeforafrica.org',
    license='MIT',
    packages=["aleph_tz_gazette_crawler"],
    zip_safe=False
)