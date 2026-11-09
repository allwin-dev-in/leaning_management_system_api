from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination

class CustomPagination(PageNumberPagination):
    page_size=5
    page_query_param="page_num"

class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit=3
    max_limit =5