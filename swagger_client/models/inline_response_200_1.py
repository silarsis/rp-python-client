# coding: utf-8

"""
    RepositPower External

    Unofficial RepositPower External API  This API is built by hand from the description at https://api.repositpower.com/docs/  It should not be mistaken for official in any way shape or form, it's simply my attempt to document the API and build some client libraries from that.  This API is demonstrably wrong around authentication - please read the official docco at the link above for accurate details. It will login, but all the login options are not captured - I wasn't clear how to write up both basic and token login being available on all URLs (ie. how to make auth an either/or rather than a both).  This API is also not completed yet. I've note tested a bunch of 200 responses, and some that I have don't have accurate enums in them because I don't know all the possible values.  Also, I haven't quite figured out how to wrap the whole thing in unit tests. 

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

from pprint import pformat
from six import iteritems
import re


class InlineResponse2001(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, msg=None, status=None):
        """
        InlineResponse2001 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'msg': 'str',
            'status': 'str'
        }

        self.attribute_map = {
            'msg': 'msg',
            'status': 'status'
        }

        self._msg = msg
        self._status = status


    @property
    def msg(self):
        """
        Gets the msg of this InlineResponse2001.


        :return: The msg of this InlineResponse2001.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """
        Sets the msg of this InlineResponse2001.


        :param msg: The msg of this InlineResponse2001.
        :type: str
        """

        self._msg = msg

    @property
    def status(self):
        """
        Gets the status of this InlineResponse2001.


        :return: The status of this InlineResponse2001.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this InlineResponse2001.


        :param status: The status of this InlineResponse2001.
        :type: str
        """

        self._status = status

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
