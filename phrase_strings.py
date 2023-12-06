# https://github.com/phrase/phrase-python
# Expects an environment variable named PHRASE_DISCOVERY_ACCESS_TOKEN to be set.

from __future__ import print_function

import os
import json
import phrase_api
from phrase_api.rest import ApiException
from pprint import pprint


project_id = '88ffd4d5abd6494131fabb1a271950b8'  # mkDocs

def load_configuration():
    # print('phrase_strings.py: load_configuration starting...')
    configuration = phrase_api.Configuration()
    # print('phrase_strings.py: configuration object created...')
    configuration.api_key_prefix['Authorization'] = 'token'
    # print('phrase_strings.py: configuration.api_key_prefix set...')
    configuration.host = "https://api.us.app.phrase.com/v2/"
    # print('phrase_strings.py: configuration.host set...')

    access_token = 'PHRASE_DISCOVERY_ACCESS_TOKEN'

    if access_token in os.environ:
        configuration.api_key['Authorization'] = os.environ[access_token]
        # print('access token: ' + str(configuration.api_key['Authorization']))
        # configuration.api_key['Authorization'] = 'd2dcdce2929a1f4f4b89f17b6e4a2d639aa5a94603d894341ade0c260a06e1f4'
        # print('access token: ' + str(configuration.api_key['Authorization']))
    else:
        print(f'{access_token} does not exist')
        exit(1)

    # print('phrase_strings.py: load_configuration ending...')

    return configuration


def load_locale(locale):
    print('phrase_strings.py: load_locale starting...')
    configuration = load_configuration()
    # print('configuration loaded: ' + str(configuration))
    # Enter a context with an instance of the API client
    with phrase_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = phrase_api.LocalesApi(api_client)
        id = locale
        x_phrase_app_otp = ''
        if_modified_since = ''
        if_none_match = ''
        branch = ''
        file_format = 'json'
        tags = ''
        tag = ''
        include_empty_translations = True
        exclude_empty_zero_forms = True
        include_translated_keys = True
        keep_notranslate_tags = True
        convert_emoji = True
        format_options = None
        encoding = ''
        skip_unverified_translations = False
        include_unverified_translations = True
        use_last_reviewed_version = False
        fallback_locale_id = ''
        source_locale_id = 'en'

        try:
            # Download a locale
            api_response = api_instance.locale_download(project_id, id,
                                                        x_phrase_app_otp=x_phrase_app_otp,
                                                        if_modified_since=if_modified_since,
                                                        if_none_match=if_none_match,
                                                        branch=branch, file_format=file_format,
                                                        tags=tags, tag=tag,
                                                        include_empty_translations=include_empty_translations,
                                                        exclude_empty_zero_forms=exclude_empty_zero_forms,
                                                        include_translated_keys=include_translated_keys,
                                                        keep_notranslate_tags=keep_notranslate_tags,
                                                        convert_emoji=convert_emoji,
                                                        format_options=format_options,
                                                        encoding=encoding,
                                                        skip_unverified_translations=skip_unverified_translations,
                                                        include_unverified_translations=include_unverified_translations,
                                                        use_last_reviewed_version=use_last_reviewed_version,
                                                        fallback_locale_id=fallback_locale_id,
                                                        source_locale_id=source_locale_id)
            f = open(api_response, 'r')
            data = json.load(f)
            return data
        except ApiException as e:
            print("Exception when calling LocalesApi->locale_download: %s\n" % e)

def list_locales():
    # print('phrase_strings.py: list_locales() starting...')
    configuration = load_configuration()
    # print('phrase_strings.py: list_locales() configuration loaded: ' + str(configuration))
    # Enter a context with an instance of the API client
    with phrase_api.ApiClient(configuration) as api_client:
        # print('phrase_strings.py: list_locales() with Api.Client()...')
        # Create an instance of the API class
        api_instance = phrase_api.LocalesApi(api_client)
        # print('phrase_strings.py: list_locales() instance of LocalesApi() created. api_instance: ' + str(api_instance))
        # sort_by = 'sort_by_example'  # str | Sort locales. Valid options are \"name_asc\", \"name_desc\", \"default_asc\", \"default_desc\".
        # branch = 'my-feature-branch'  # str | specify the branch to use

        try:
            # List locales
            # api_response = api_instance.locales_list(project_id, x_phrase_app_otp=x_phrase_app_otp, page=page,
            #                                          per_page=per_page, sort_by=sort_by, branch=branch)
            # List locales
            # print('phrase_strings.py: list_locales() project_id: ' + str(project_id))
            # print('Phrase dies here')
            api_response = api_instance.locales_list(str(project_id), page=1, per_page=99)
            # print('pprinting api_response...')
            # pprint(api_response)
            print('phrase_strings.py: list_locales() project_id: ' + str(project_id))
            # api_response = api_instance.locales_list(project_id)
            # print('phrase_strings.py: list_locales() api_response: ' + str(api_response))
        except ApiException as e:
            print("Exception when calling LocalesApi->locales_list: %s\n" % e)

        return api_response

