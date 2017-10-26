# swagger_client.DefaultApi

All URIs are relative to *https://api.repositpower.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_login_post**](DefaultApi.md#auth_login_post) | **POST** /auth/login/ | return access token (session id) upon successful basic or html auth (use username/password, or use basic auth) 
[**auth_logout_get**](DefaultApi.md#auth_logout_get) | **GET** /auth/logout | de-authenticate the token (always returns success)
[**deployments_userkey_battery_capacity_get**](DefaultApi.md#deployments_userkey_battery_capacity_get) | **GET** /deployments/{userkey}/battery/capacity | battery capacity in kWh
[**deployments_userkey_battery_historical_soc_get**](DefaultApi.md#deployments_userkey_battery_historical_soc_get) | **GET** /deployments/{userkey}/battery/historical/soc | state of charge of a battery in kWh
[**deployments_userkey_components_get**](DefaultApi.md#deployments_userkey_components_get) | **GET** /deployments/{userkey}/components | installed components and their overall status
[**deployments_userkey_cost_historical_get**](DefaultApi.md#deployments_userkey_cost_historical_get) | **GET** /deployments/{userkey}/cost/historical | energy cost in $
[**deployments_userkey_generation_historical_p_get**](DefaultApi.md#deployments_userkey_generation_historical_p_get) | **GET** /deployments/{userkey}/generation/historical/p | solar generation data as negative real_power in kW
[**deployments_userkey_gridcredits_historical_get**](DefaultApi.md#deployments_userkey_gridcredits_historical_get) | **GET** /deployments/{userkey}/gridcredits/historical | earned gridcredits
[**deployments_userkey_house_historical_get**](DefaultApi.md#deployments_userkey_house_historical_get) | **GET** /deployments/{userkey}/house/historical | house consumption in kW
[**deployments_userkey_inverter_historical_p_get**](DefaultApi.md#deployments_userkey_inverter_historical_p_get) | **GET** /deployments/{userkey}/inverter/historical/p | the battery inverter data as real_power in kW
[**deployments_userkey_meter_historical_p_get**](DefaultApi.md#deployments_userkey_meter_historical_p_get) | **GET** /deployments/{userkey}/meter/historical/p | real power measurements in kW at the grid connection
[**userkeys_get**](DefaultApi.md#userkeys_get) | **GET** /userkeys/ | all userkeys/battery system identifiers for the current user


# **auth_login_post**
> InlineResponse200 auth_login_post(reposit_auth=reposit_auth)

return access token (session id) upon successful basic or html auth (use username/password, or use basic auth) 

Post username and password and you will get back an RP-TOKEN value. Add that value to the Headers of all subsequent calls (see api_key security definition above) as your authenticated token. 

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
api_instance = swagger_client.DefaultApi()
reposit_auth = 'API' # str |  (optional) (default to API)

try: 
    # return access token (session id) upon successful basic or html auth (use username/password, or use basic auth) 
    api_response = api_instance.auth_login_post(reposit_auth=reposit_auth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->auth_login_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reposit_auth** | **str**|  | [optional] [default to API]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_logout_get**
> InlineResponse2001 auth_logout_get()

de-authenticate the token (always returns success)

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try: 
    # de-authenticate the token (always returns success)
    api_response = api_instance.auth_logout_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->auth_logout_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deployments_userkey_battery_capacity_get**
> InlineResponse2004 deployments_userkey_battery_capacity_get(userkey)

battery capacity in kWh

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
userkey = 'userkey_example' # str | User Key from /userkeys

try: 
    # battery capacity in kWh
    api_response = api_instance.deployments_userkey_battery_capacity_get(userkey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->deployments_userkey_battery_capacity_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userkey** | **str**| User Key from /userkeys | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deployments_userkey_battery_historical_soc_get**
> InlineResponse2008 deployments_userkey_battery_historical_soc_get(userkey, delta_t=delta_t, start=start, end=end, format=format)

state of charge of a battery in kWh

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
userkey = 'userkey_example' # str | User Key from /userkeys
delta_t = 56 # int | downsample interval (optional)
start = 56 # int | Start time (optional)
end = 56 # int | End time (optional)
format = 'format_example' # str |  (optional)

try: 
    # state of charge of a battery in kWh
    api_response = api_instance.deployments_userkey_battery_historical_soc_get(userkey, delta_t=delta_t, start=start, end=end, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->deployments_userkey_battery_historical_soc_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userkey** | **str**| User Key from /userkeys | 
 **delta_t** | **int**| downsample interval | [optional] 
 **start** | **int**| Start time | [optional] 
 **end** | **int**| End time | [optional] 
 **format** | **str**|  | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deployments_userkey_components_get**
> InlineResponse2003 deployments_userkey_components_get(userkey)

installed components and their overall status

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
userkey = 'userkey_example' # str | User Key from /userkeys

try: 
    # installed components and their overall status
    api_response = api_instance.deployments_userkey_components_get(userkey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->deployments_userkey_components_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userkey** | **str**| User Key from /userkeys | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deployments_userkey_cost_historical_get**
> InlineResponse20010 deployments_userkey_cost_historical_get(userkey, delta_t=delta_t, start=start, end=end, format=format)

energy cost in $

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
userkey = 'userkey_example' # str | User Key from /userkeys
delta_t = 56 # int | downsample interval (optional)
start = 56 # int | Start time (optional)
end = 56 # int | End time (optional)
format = 'format_example' # str |  (optional)

try: 
    # energy cost in $
    api_response = api_instance.deployments_userkey_cost_historical_get(userkey, delta_t=delta_t, start=start, end=end, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->deployments_userkey_cost_historical_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userkey** | **str**| User Key from /userkeys | 
 **delta_t** | **int**| downsample interval | [optional] 
 **start** | **int**| Start time | [optional] 
 **end** | **int**| End time | [optional] 
 **format** | **str**|  | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deployments_userkey_generation_historical_p_get**
> InlineResponse2005 deployments_userkey_generation_historical_p_get(userkey, delta_t=delta_t, start=start, end=end, format=format)

solar generation data as negative real_power in kW

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
userkey = 'userkey_example' # str | User Key from /userkeys
delta_t = 56 # int | downsample interval (optional)
start = 56 # int | Start time (optional)
end = 56 # int | End time (optional)
format = 'format_example' # str |  (optional)

try: 
    # solar generation data as negative real_power in kW
    api_response = api_instance.deployments_userkey_generation_historical_p_get(userkey, delta_t=delta_t, start=start, end=end, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->deployments_userkey_generation_historical_p_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userkey** | **str**| User Key from /userkeys | 
 **delta_t** | **int**| downsample interval | [optional] 
 **start** | **int**| Start time | [optional] 
 **end** | **int**| End time | [optional] 
 **format** | **str**|  | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deployments_userkey_gridcredits_historical_get**
> InlineResponse20011 deployments_userkey_gridcredits_historical_get(userkey, delta_t=delta_t, start=start, end=end, format=format)

earned gridcredits

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
userkey = 'userkey_example' # str | User Key from /userkeys
delta_t = 56 # int | downsample interval (optional)
start = 56 # int | Start time (optional)
end = 56 # int | End time (optional)
format = 'format_example' # str |  (optional)

try: 
    # earned gridcredits
    api_response = api_instance.deployments_userkey_gridcredits_historical_get(userkey, delta_t=delta_t, start=start, end=end, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->deployments_userkey_gridcredits_historical_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userkey** | **str**| User Key from /userkeys | 
 **delta_t** | **int**| downsample interval | [optional] 
 **start** | **int**| Start time | [optional] 
 **end** | **int**| End time | [optional] 
 **format** | **str**|  | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deployments_userkey_house_historical_get**
> InlineResponse2007 deployments_userkey_house_historical_get(userkey, delta_t=delta_t, start=start, end=end, format=format)

house consumption in kW

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
userkey = 'userkey_example' # str | User Key from /userkeys
delta_t = 56 # int | downsample interval (optional)
start = 56 # int | Start time (optional)
end = 56 # int | End time (optional)
format = 'format_example' # str |  (optional)

try: 
    # house consumption in kW
    api_response = api_instance.deployments_userkey_house_historical_get(userkey, delta_t=delta_t, start=start, end=end, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->deployments_userkey_house_historical_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userkey** | **str**| User Key from /userkeys | 
 **delta_t** | **int**| downsample interval | [optional] 
 **start** | **int**| Start time | [optional] 
 **end** | **int**| End time | [optional] 
 **format** | **str**|  | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deployments_userkey_inverter_historical_p_get**
> InlineResponse2006 deployments_userkey_inverter_historical_p_get(userkey, delta_t=delta_t, start=start, end=end, format=format)

the battery inverter data as real_power in kW

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
userkey = 'userkey_example' # str | User Key from /userkeys
delta_t = 56 # int | downsample interval (optional)
start = 56 # int | Start time (optional)
end = 56 # int | End time (optional)
format = 'format_example' # str |  (optional)

try: 
    # the battery inverter data as real_power in kW
    api_response = api_instance.deployments_userkey_inverter_historical_p_get(userkey, delta_t=delta_t, start=start, end=end, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->deployments_userkey_inverter_historical_p_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userkey** | **str**| User Key from /userkeys | 
 **delta_t** | **int**| downsample interval | [optional] 
 **start** | **int**| Start time | [optional] 
 **end** | **int**| End time | [optional] 
 **format** | **str**|  | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deployments_userkey_meter_historical_p_get**
> InlineResponse2009 deployments_userkey_meter_historical_p_get(userkey, delta_t=delta_t, start=start, end=end, format=format)

real power measurements in kW at the grid connection

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
userkey = 'userkey_example' # str | User Key from /userkeys
delta_t = 56 # int | downsample interval (optional)
start = 56 # int | Start time (optional)
end = 56 # int | End time (optional)
format = 'format_example' # str |  (optional)

try: 
    # real power measurements in kW at the grid connection
    api_response = api_instance.deployments_userkey_meter_historical_p_get(userkey, delta_t=delta_t, start=start, end=end, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->deployments_userkey_meter_historical_p_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userkey** | **str**| User Key from /userkeys | 
 **delta_t** | **int**| downsample interval | [optional] 
 **start** | **int**| Start time | [optional] 
 **end** | **int**| End time | [optional] 
 **format** | **str**|  | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **userkeys_get**
> InlineResponse2002 userkeys_get()

all userkeys/battery system identifiers for the current user

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try: 
    # all userkeys/battery system identifiers for the current user
    api_response = api_instance.userkeys_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->userkeys_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

