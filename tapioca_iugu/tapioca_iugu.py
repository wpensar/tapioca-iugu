# coding: utf-8

from tapioca import (
    TapiocaAdapter, generate_wrapper_from_adapter, JSONAdapterMixin)

from requests.auth import HTTPBasicAuth


from .resource_mapping import RESOURCE_MAPPING


class IuguClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    api_root = 'https://api.iugu.com/v1/'
    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(IuguClientAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs)

        params['auth'] = HTTPBasicAuth(
            api_params.get('user'), api_params.get('password'))

        return params

    def get_iterator_list(self, response_data):
        return response_data

    def get_iterator_next_request_kwargs(self, iterator_request_kwargs,
                                         response_data, response):
        if 'params' not in iterator_request_kwargs:
            iterator_request_kwargs['params'] = {}

        start = iterator_request_kwargs['params'].get('start', 0)
        total_items = response_data.get('totalItems')
        items = len(response_data.get('items')) + start
        if total_items > items:
            iterator_request_kwargs['params']['start'] = start + items
            return iterator_request_kwargs


Iugu = generate_wrapper_from_adapter(IuguClientAdapter)
