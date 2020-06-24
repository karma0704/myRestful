from django.http import JsonResponse


def json_response(code, msg, data):
    result = dict()
    result['status'] = code
    result['msg'] = msg or {}
    result['data'] = data or {}
    return JsonResponse(result, safe=False)

