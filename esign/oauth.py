from docusign_esign import *
from . import ds_config
import os

def create_api_client():
    """Create api client and construct API headers"""
    api_client = ApiClient()
    api_client.host = ds_config.DS_JWT['base_path']
    api_client.set_base_path(ds_config.DS_JWT['authorization_server'])
    scopes = ['signature', 'impersonation']

    private_key_file = os.path.abspath('./private.key')
    with open(private_key_file) as private_key_file:
        private_key = private_key_file.read()
        private_key.encode("ascii").decode("utf-8")

    oauth_object = api_client.request_jwt_user_token(
        client_id=ds_config.DS_JWT['ds_client_id'],
        user_id=ds_config.DS_JWT['ds_impersonated_user_id'],
        oauth_host_name=ds_config.DS_JWT['authorization_server'],
        private_key_bytes=private_key,
        expires_in=3600,
        scopes=scopes
    )
    oauth_object = oauth_object.to_dict()
    access_token = oauth_object['access_token']
    api_client.set_default_header(header_name='Authorization', header_value=f'Bearer {access_token}')
    return api_client









