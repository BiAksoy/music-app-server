from fastapi import HTTPException, Header
import jwt


def auth_middleware(x_auth_token=Header()):
    try:
        if not x_auth_token:
            raise HTTPException(status_code=401, detail='Token not found')
        
        verified_token = jwt.decode(x_auth_token, 'secret', algorithms=['HS256'])

        if not verified_token:
            raise HTTPException(status_code=401, detail='Invalid token')
        
        user_id = verified_token.get('user_id')
        return {'user_id': user_id, 'token': x_auth_token}
    
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail='Invalid token')
