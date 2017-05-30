# coding: utf-8

"""
    RepositPower External

    Unofficial RepositPower External API  This API is built by hand from the description at https://api.repositpower.com/docs/  It should not be mistaken for official in any way shape or form, it's simply my attempt to document the API and build some client libraries from that.  This API is demonstrably wrong around authentication - please read the official docco at the link above for accurate details. It will login, but all the login options are not captured - I wasn't clear how to write up both basic and token login being available on all URLs (ie. how to make auth an either/or rather than a both).  This API is also not completed yet. I've note tested a bunch of 200 responses, and some that I have don't have accurate enums in them because I don't know all the possible values.  Also, I haven't quite figured out how to wrap the whole thing in unit tests.  This version (1.0.0) matches version 11/03/2016 of the official docs (as at 30/5/2017) 

    OpenAPI spec version: 1.0.0
    Contact: kevin@littlejohn.id.au
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import sys
from setuptools import setup, find_packages

NAME = "swagger_client"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="RepositPower External",
    author_email="kevin@littlejohn.id.au",
    url="",
    keywords=["Swagger", "RepositPower External"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Unofficial RepositPower External API  This API is built by hand from the description at https://api.repositpower.com/docs/  It should not be mistaken for official in any way shape or form, it&#39;s simply my attempt to document the API and build some client libraries from that.  This API is demonstrably wrong around authentication - please read the official docco at the link above for accurate details. It will login, but all the login options are not captured - I wasn&#39;t clear how to write up both basic and token login being available on all URLs (ie. how to make auth an either/or rather than a both).  This API is also not completed yet. I&#39;ve note tested a bunch of 200 responses, and some that I have don&#39;t have accurate enums in them because I don&#39;t know all the possible values.  Also, I haven&#39;t quite figured out how to wrap the whole thing in unit tests.  This version (1.0.0) matches version 11/03/2016 of the official docs (as at 30/5/2017) 
    """
)

