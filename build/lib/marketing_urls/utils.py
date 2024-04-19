import base64
import uuid


def new_key(prefix=None):
    r_uuid = str(base64.urlsafe_b64encode(uuid.uuid4().bytes).decode())
    if prefix is not None:
        return '%s_%s' % (prefix, r_uuid.replace('=', '').replace('_', ''))
    else:
        return r_uuid.replace('=', '').replace('_', '')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
