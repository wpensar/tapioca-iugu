# coding: utf-8

RESOURCE_MAPPING = {
    'payment_token_create': {
        'resource': 'payment_token',
        'docs': 'https://iugu.com/referencias/api#criar-um-token',
        'methods': ['POST']
    },
    'charge_create': {
        'resource': 'charge',
        'docs': 'https://iugu.com/referencias/api#cobrança-direta',
        'methods': ['POST']
    },
    'customer_list': {
        'resource': 'customers',
        'docs': 'https://iugu.com/referencias/api#listar-os-clientes',
        'methods': ['GET']
    },
    'customer_create': {
        'resource': 'customers',
        'docs': 'https://iugu.com/referencias/api#criar-um-cliente',
        'methods': ['POST']
    },
    'customer_retrieve': {
        'resource': 'customers/{id}',
        'docs': 'https://iugu.com/referencias/api#buscar-um-cliente',
        'methods': ['GET']
    },
    'customer_update': {
        'resource': 'customers/{id}',
        'docs': 'https://iugu.com/referencias/api#alterar-um-cliente',
        'methods': ['PUT']
    },
    'customer_delete': {
        'resource': 'customers/{id}',
        'docs': 'https://iugu.com/referencias/api#remover-um-cliente',
        'methods': ['DELETE']
    },
    'customer_payment_method_list': {
        'resource': 'customers/{customer_id}/payment_methods',
        'docs': 'https://iugu.com/referencias/api#listar-as-formas-de-pagamento',
        'methods': ['GET']
    },
    'customer_payment_method_create': {
        'resource': 'customers/{customer_id}/payment_methods',
        'docs': 'https://iugu.com/referencias/api#criar-uma-forma-de-pagamento',
        'methods': ['POST']
    },
    'customer_payment_method_retrieve': {
        'resource': 'customers/{customer_id}/payment_methods/{id}',
        'docs': 'https://iugu.com/referencias/api#buscar-uma-forma-de-pagamento',
        'methods': ['GET']
    },
    'customer_payment_method_update': {
        'resource': 'customers/{customer_id}/payment_methods/{id}',
        'docs': 'https://iugu.com/referencias/api#alterar-uma-forma-de-pagamento',
        'methods': ['PUT']
    },
    'customer_payment_method_delete': {
        'resource': 'customers/{customer_id}/payment_methods/{id}',
        'docs': 'https://iugu.com/referencias/api#remover-uma-forma-de-pagamento',
        'methods': ['DELETE']
    },
    'invoice_list': {
        'resource': 'invoices',
        'docs': 'https://iugu.com/referencias/api#listar-as-faturas',
        'methods': ['GET']
    },
    'invoice_create': {
        'resource': 'invoices',
        'docs': 'https://iugu.com/referencias/api#criar-uma-fatura',
        'methods': ['POST']
    },
    'invoice_retrieve': {
        'resource': 'invoices/{id}',
        'docs': 'https://iugu.com/referencias/api#buscar-uma-fatura',
        'methods': ['GET']
    },
    'invoice_update': {
        'resource': 'invoices/{id}',
        'docs': 'https://iugu.com/referencias/api#alterar-uma-fatura',
        'methods': ['PUT']
    },
    'invoice_delete': {
        'resource': 'invoices/{id}',
        'docs': 'https://iugu.com/referencias/api#remover-uma-fatura',
        'methods': ['DELETE']
    },
    'invoice_capture': {
        'resource': 'invoices/{id}/capture',
        'docs': 'https://iugu.com/referencias/api#capturar-uma-fatura',
        'methods': ['POST']
    },
    'invoice_cancel': {
        'resource': 'invoices/{id}/cancel',
        'docs': 'https://iugu.com/referencias/api#cancelar-uma-fatura',
        'methods': ['PUT']
    },
    'invoice_refund': {
        'resource': 'invoices/{id}/refund',
        'docs': 'https://iugu.com/referencias/api#reembolsar-uma-fatura',
        'methods': ['POST']
    },
    'invoice_duplicate': {
        'resource': 'invoices/{id}/duplicate',
        'docs': 'https://iugu.com/referencias/api#segunda-via-de-fatura',
        'methods': ['POST']
    },
    'plan_list': {
        'resource': 'plans',
        'docs': 'https://iugu.com/referencias/api#listar-os-planos',
        'methods': ['GET']
    },
    'plan_create': {
        'resource': 'plans',
        'docs': 'https://iugu.com/referencias/api#criar-um-plano',
        'methods': ['POST']
    },
    'plan_retrieve': {
        'resource': 'plans/{id}',
        'docs': 'https://iugu.com/referencias/api#buscar-um-plano',
        'methods': ['GET']
    },
    'plan_retrieve_by_identifier': {
        'resource': 'plans/identifier/{identifier}',
        'docs': 'https://iugu.com/referencias/api#buscar-um-plano-pelo-identificador',
        'methods': ['GET']
    },
    'plan_update': {
        'resource': 'plans/{id}',
        'docs': 'https://iugu.com/referencias/api#alterar-um-plano',
        'methods': ['PUT']
    },
    'plan_delete': {
        'resource': 'plans/{id}',
        'docs': 'https://iugu.com/referencias/api#remover-um-plano',
        'methods': ['DELETE']
    },
    'subscription_list': {
        'resource': 'subscriptions',
        'docs': 'https://iugu.com/referencias/api#listar-as-assinaturas',
        'methods': ['GET']
    },
    'subscription_create': {
        'resource': 'subscriptions',
        'docs': 'https://iugu.com/referencias/api#criar-uma-assinatura',
        'methods': ['POST']
    },
    'subscription_retrieve': {
        'resource': 'subscriptions/{id}',
        'docs': 'https://iugu.com/referencias/api#buscar-uma-assinatura',
        'methods': ['GET']
    },
    'subscription_update': {
        'resource': 'subscriptions/{id}',
        'docs': 'https://iugu.com/referencias/api#alterar-uma-assinatura',
        'methods': ['PUT']
    },
    'subscription_delete': {
        'resource': 'subscriptions/{id}',
        'docs': 'https://iugu.com/referencias/api#remover-uma-assinatura',
        'methods': ['DELETE']
    },
    'subscription_suspend': {
        'resource': 'subscriptions/{id}/suspend',
        'docs': 'https://iugu.com/referencias/api#suspender-uma-assinatura',
        'methods': ['POST']
    },
    'subscription_activate': {
        'resource': 'subscriptions/{id}/activate',
        'docs': 'https://iugu.com/referencias/api#ativar-uma-assinatura',
        'methods': ['POST']
    },
    'subscription_change_plan': {
        'resource': 'subscriptions/{id}/change_plan/{plan_id}',
        'docs': 'https://iugu.com/referencias/api#alterar-o-plano-de-uma-assinatura',
        'methods': ['POST']
    },
    'subscription_add_credits': {
        'resource': 'subscriptions/{id}/add_credits',
        'docs': 'https://iugu.com/referencias/api#adicionar-créditos-a-assinatura',
        'methods': ['PUT']
    },
    'subscription_remove_credits': {
        'resource': 'subscriptions/{id}/remove_credits',
        'docs': 'https://iugu.com/referencias/api#remover-créditos-da-assinatura',
        'methods': ['PUT']
    },
    'subscription_remove_credits': {
        'resource': 'subscriptions/{id}/remove_credits',
        'docs': 'https://iugu.com/referencias/api#remover-créditos-da-assinatura',
        'methods': ['PUT']
    },
    'transfer_list': {
        'resource': 'transfers',
        'docs': 'https://iugu.com/referencias/api#listar-as-transferências',
        'methods': ['GET']
    },
    'transfer_create': {
        'resource': 'transfers',
        'docs': 'https://iugu.com/referencias/api#transferir-valor',
        'methods': ['POST']
    },
    'marketplace_account_list': {
        'resource': 'marketplace',
        'docs': 'https://iugu.com/referencias/api#marketplace',
        'methods': ['GET']
    },
    'marketplace_account_create': {
        'resource': 'marketplace/create_account',
        'docs': 'https://iugu.com/referencias/api#criar-sub-conta',
        'methods': ['POST']
    },
    'marketplace_account_request_verification': {
        'resource': 'accounts/{id}/request_verification',
        'docs': 'https://iugu.com/referencias/api#enviar-verificação-de-sub-conta',
        'methods': ['POST']
    },
    'marketplace_account_retrieve': {
        'resource': 'accounts/{id}',
        'docs': 'https://iugu.com/referencias/api#buscar-informações-de-sub-conta',
        'methods': ['GET']
    },
    'marketplace_account_configuration': {
        'resource': 'accounts/configuration',
        'docs': 'https://iugu.com/referencias/api#configurar-sub-conta',
        'methods': ['POST']
    },
    'marketplace_account_request_withdraw': {
        'resource': 'accounts/{id}/request_withdraw',
        'docs': 'https://iugu.com/referencias/api#pedido-de-saque',
        'methods': ['POST']
    },
    'marketplace_account_bank_verification': {
        'resource': 'bank_verification',
        'docs': 'https://iugu.com/referencias/api#atualização-de-dados-bancários',
        'methods': ['POST']
    },
    'withdraw_request_list': {
        'resource': 'withdraw_requests',
        'docs': 'https://iugu.com/referencias/api#listar-transferências',
        'methods': ['GET']
    },
    'withdraw_request_retrieve': {
        'resource': 'withdraw_requests/{id}',
        'docs': 'https://iugu.com/referencias/api#buscar-uma-transferência',
        'methods': ['GET']
    },
}
