# swagger_client.CoursApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**courses_course_id_delete**](CoursApi.md#courses_course_id_delete) | **DELETE** /courses/{courseId} | Supprimer un cours
[**courses_course_id_get**](CoursApi.md#courses_course_id_get) | **GET** /courses/{courseId} | Obtenir un cours spécifique
[**courses_course_id_put**](CoursApi.md#courses_course_id_put) | **PUT** /courses/{courseId} | Mettre à jour un cours
[**courses_get**](CoursApi.md#courses_get) | **GET** /courses | Obtenir la liste des cours
[**courses_post**](CoursApi.md#courses_post) | **POST** /courses | Créer un nouveau cours


# **courses_course_id_delete**
> courses_course_id_delete(course_id)

Supprimer un cours

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoursApi()
course_id = NULL # object | 

try:
    # Supprimer un cours
    api_instance.courses_course_id_delete(course_id)
except ApiException as e:
    print("Exception when calling CoursApi->courses_course_id_delete: %s\n" % e)
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

# **courses_course_id_get**
> courses_course_id_get(course_id)

Obtenir un cours spécifique

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoursApi()
course_id = NULL # object | 

try:
    # Obtenir un cours spécifique
    api_instance.courses_course_id_get(course_id)
except ApiException as e:
    print("Exception when calling CoursApi->courses_course_id_get: %s\n" % e)
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

# **courses_course_id_put**
> courses_course_id_put(course_id)

Mettre à jour un cours

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoursApi()
course_id = NULL # object | 

try:
    # Mettre à jour un cours
    api_instance.courses_course_id_put(course_id)
except ApiException as e:
    print("Exception when calling CoursApi->courses_course_id_put: %s\n" % e)
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

# **courses_get**
> courses_get()

Obtenir la liste des cours

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoursApi()

try:
    # Obtenir la liste des cours
    api_instance.courses_get()
except ApiException as e:
    print("Exception when calling CoursApi->courses_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **courses_post**
> courses_post()

Créer un nouveau cours

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CoursApi()

try:
    # Créer un nouveau cours
    api_instance.courses_post()
except ApiException as e:
    print("Exception when calling CoursApi->courses_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

