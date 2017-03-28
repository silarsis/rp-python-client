# swagger_client.LoginApi

All URIs are relative to *https://virtserver.swaggerhub.com/silarsis/repositpower/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_login_get**](LoginApi.md#auth_login_get) | **GET** /auth/login | return access token upon successful basic or html auth (use username/password, or use basic auth)


# **auth_login_get**
> InlineResponse200 auth_login_get(username=username, password=password)

return access token upon successful basic or html auth (use username/password, or use basic auth)

Send username and password either as basic auth, or as parameters in the GET request, and you will get back an RP-TOKEN value. Add that value to the Headers of all subsequent calls (see api_key security definition above) as your authenticated token. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoginApi()
username = 'username_example' # str | Username for access (optional)
password = 'password_example' # str | Password for access (optional)

try: 
    # return access token upon successful basic or html auth (use username/password, or use basic auth)
    api_response = api_instance.auth_login_get(username=username, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->auth_login_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username for access | [optional] 
 **password** | **str**| Password for access | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

