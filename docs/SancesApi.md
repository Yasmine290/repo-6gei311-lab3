# swagger_client.SancesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**courses_course_id_sessions_get**](SancesApi.md#courses_course_id_sessions_get) | **GET** /courses/{courseId}/sessions | Obtenir les séances d&#39;un cours
[**courses_course_id_sessions_post**](SancesApi.md#courses_course_id_sessions_post) | **POST** /courses/{courseId}/sessions | Créer une nouvelle séance pour un cours
[**courses_course_id_sessions_session_id_put**](SancesApi.md#courses_course_id_sessions_session_id_put) | **PUT** /courses/{courseId}/sessions/{sessionId} | Mettre à jour une séance


# **courses_course_id_sessions_get**
> courses_course_id_sessions_get(course_id)

Obtenir les séances d'un cours

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SancesApi()
course_id = NULL # object | 

try:
    # Obtenir les séances d'un cours
    api_instance.courses_course_id_sessions_get(course_id)
except ApiException as e:
    print("Exception when calling SancesApi->courses_course_id_sessions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_course_id_sessions_post**
> courses_course_id_sessions_post(course_id)

Créer une nouvelle séance pour un cours

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SancesApi()
course_id = NULL # object | 

try:
    # Créer une nouvelle séance pour un cours
    api_instance.courses_course_id_sessions_post(course_id)
except ApiException as e:
    print("Exception when calling SancesApi->courses_course_id_sessions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_course_id_sessions_session_id_put**
> courses_course_id_sessions_session_id_put(course_id, session_id)

Mettre à jour une séance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SancesApi()
course_id = NULL # object | 
session_id = NULL # object | 

try:
    # Mettre à jour une séance
    api_instance.courses_course_id_sessions_session_id_put(course_id, session_id)
except ApiException as e:
    print("Exception when calling SancesApi->courses_course_id_sessions_session_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | [**object**](.md)|  | 
 **session_id** | [**object**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

