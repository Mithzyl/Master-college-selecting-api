def jwt_response_payload_handler(token, user=None, request=None):

    return {
        'message': 'success',
        'token': token,
        'id': user.id,
        'pk': user.pk,
        'mobile': user.mobile,
    }