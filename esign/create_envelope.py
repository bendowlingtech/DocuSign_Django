from docusign_esign import *
from . import oauth
from . import ds_config

def create_envelope():

    # Create the document model
    document = Document(  # create the DocuSign document object
        document_base64=ds_config.DS_Base64['base_64'],
        name='Example document',  # can be different from actual file name
        file_extension='pdf',  # many different document types are accepted
        document_id=1  # a label used to reference the doc
    )

    # Create the signer recipient model
    signer = Signer(  # The signer
        email=ds_config.ENVELOPE_CONFIG['Email'], name=ds_config.ENVELOPE_CONFIG['Name'],
        recipient_id='1', routing_order='1',
        # Setting the client_user_id marks the signer as embedded
        client_user_id='12345'
    )

    # Create a sign_here tab (field on the document)
    sign_here = SignHere(  # DocuSign SignHere field/tab
        anchor_string='/sn1/', anchor_units='pixels',
        anchor_y_offset='10', anchor_x_offset='20'
    )

    # Add the tabs model (including the sign_here tab) to the signer
    # The Tabs object wants arrays of the different field/tab types
    signer.tabs = Tabs(sign_here_tabs=[sign_here])

    # Next, create the top level envelope definition and populate it.
    envelope_definition = EnvelopeDefinition(
        email_subject="Please sign this document sent from the Python SDK",
        documents=[document],
        # The Recipients object wants arrays for each recipient type
        recipients=Recipients(signers=[signer]),
        status="sent"  # requests that the envelope be created and sent.
    )

    return envelope_definition

