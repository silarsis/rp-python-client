# swagger_client.LoginApi

All URIs are relative to *https://virtserver.swaggerhub.com/silarsis/repositpower/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_login_get**](LoginApi.md#auth_login_get) | **GET** /auth/login | return access token upon successful basic auth
[**auth_login_post**](LoginApi.md#auth_login_post) | **POST** /auth/login | return access token upon successful basic or html auth (use username/password, or use basic auth)


# **auth_login_get**
> InlineResponse200 auth_login_get()

return access token upon successful basic auth

Send username and password as basic auth and you will get back an RP-TOKEN value. Add that value to the Headers of all subsequent calls (see api_key security definition above) as your authenticated token. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.LoginApi()

try: 
    # return access token upon successful basic auth
    api_response = api_instance.auth_login_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->auth_login_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_login_post**
> InlineResponse200 auth_login_post(body=body)

return access token upon successful basic or html auth (use username/password, or use basic auth)

Post username and password and you will get back an RP-TOKEN value. Add that value to the Headers of all subsequent calls (see api_key security definition above) as your authenticated token. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoginApi()
body = swagger_client.AuthParams() # AuthParams |  (optional)

try: 
    # return access token upon successful basic or html auth (use username/password, or use basic auth)
    api_response = api_instance.auth_login_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->auth_login_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthParams**](AuthParams.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

