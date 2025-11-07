from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

incident_query_parameters = [
    openapi.Parameter(
        'status',
        openapi.IN_QUERY,
        description="Фильтр по статусу",
        type=openapi.TYPE_STRING,
        enum=['open', 'in_progress', 'resolved'],
        example='open'
    ),
    openapi.Parameter(
        'limit',
        openapi.IN_QUERY,
        description="Сколько записей вернуть",
        type=openapi.TYPE_INTEGER,
        example=20
    ),
    openapi.Parameter(
        'offset',
        openapi.IN_QUERY,
        description="С какой записи начинать",
        type=openapi.TYPE_INTEGER,
        example=0
    ),
]

incident_post_schema = swagger_auto_schema(
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['description', 'status', 'source'],
        properties={
            'description': openapi.Schema(type=openapi.TYPE_STRING, example="Самокат завис на месте"),
            'status': openapi.Schema(
                type=openapi.TYPE_STRING,
                enum=['open', 'in_progress', 'resolved']
            ),
            'source': openapi.Schema(
                type=openapi.TYPE_STRING,
                enum=['operator', 'monitoring', 'partner']
            ),
        }
    )
)

incident_get_schema = swagger_auto_schema(
    manual_parameters=incident_query_parameters
)
