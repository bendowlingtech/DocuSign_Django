from docusign_esign import *
from . import create_envelope
from . import ds_config
from . import oauth

def embedded_signing():
    envelope_definition = create_envelope.create_envelope()
    api_client = oauth.create_api_client()
    envelope_api = EnvelopesApi(api_client)
    results = envelope_api.create_envelope(account_id='11254982', envelope_definition=envelope_definition)
    envelope_id = results.envelope_id

    #Recipient view Request
    recipient_view_request = RecipientViewRequest(
    authentication_method = "none",
    client_user_id = "12345",
    recipient_id = '1',
    return_url = ds_config.DS_CONFIG['redirect_uri'],
    user_name = ds_config.ENVELOPE_CONFIG['Name'],
    email = ds_config.ENVELOPE_CONFIG['Email']
    )


    results = envelope_api.create_recipient_view(
        account_id = ds_config.DS_CONFIG['account_id'],
        envelope_id=envelope_id,
        recipient_view_request=recipient_view_request
    )
    print(results)

    url = results.url
    return url

    #return {'envelope_id': envelope_id, 'redirect_url': url}