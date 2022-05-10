# -*- coding: utf-8 -*-

# This file is part of the Ingram Micro Cloud Blue Connect Report Python Boilerplate.
# Copyright (c) 2019-2021 Ingram Micro. All Rights Reserved.

import json
import shutil


STATUSES = [
    'draft',
    'tiers_setup',
    'pending',
    'inquiring',
    'approved',
    'failed',
]

REQUESTS_SCHEDULED_ACTION_STATUSES = [
    'scheduled',
    'revoking',
    'revoked',
]

TIER_ACCOUNT_UPDATE_STATUSES = [
    'pending',
    'accepted',
    'ignored',
]

USAGE_FILE_STATUSES = [
    'draft',
    'uploading',
    'uploaded',
    'invalid',
    'processing',
    'processed',
    'ready',
    'rejected',
    'pending',
    'accepted',
    'closed',
]

CHUNK_FILE_STATUSES = [
    'draft',
    'ready',
    'closed',
    'failed',
]


def remove_github_actions():
    shutil.rmtree('.github')


def subscription_processing_capabilities(descriptor):
    if '{{ cookiecutter.subscription_process_capabilities_1of6 }}'.lower() == 'y':
        descriptor['capabilities'][
            'asset_purchase_request_processing'
        ] = STATUSES + REQUESTS_SCHEDULED_ACTION_STATUSES

    if '{{ cookiecutter.subscription_process_capabilities_2of6 }}'.lower() == 'y':
        descriptor['capabilities'][
            'asset_change_request_processing'
        ] = STATUSES + REQUESTS_SCHEDULED_ACTION_STATUSES

    if '{{ cookiecutter.subscription_process_capabilities_3of6 }}'.lower() == 'y':
        descriptor['capabilities'][
            'asset_suspend_request_processing'
        ] = STATUSES + REQUESTS_SCHEDULED_ACTION_STATUSES

    if '{{ cookiecutter.subscription_process_capabilities_4of6 }}'.lower() == 'y':
        descriptor['capabilities'][
            'asset_resume_request_processing'
        ] = STATUSES + REQUESTS_SCHEDULED_ACTION_STATUSES

    if '{{ cookiecutter.subscription_process_capabilities_5of6 }}'.lower() == 'y':
        descriptor['capabilities'][
            'asset_cancel_request_processing'
        ] = STATUSES + REQUESTS_SCHEDULED_ACTION_STATUSES

    if '{{ cookiecutter.subscription_process_capabilities_6of6 }}'.lower() == 'y':
        descriptor['capabilities']['asset_adjustment_request_processing'] = STATUSES


def subscription_validation_capabilities(descriptor):
    if '{{ cookiecutter.subscription_validation_capabilities_1of2 }}'.lower() == 'y':
        descriptor['capabilities']['asset_purchase_request_validation'] = STATUSES

    if '{{ cookiecutter.subscription_validation_capabilities_2of2 }}'.lower() == 'y':
        descriptor['capabilities']['asset_change_request_validation'] = STATUSES


def tierconfig_processing_capabilities(descriptor):
    if '{{ cookiecutter.tier_config_process_capabilities_1of3 }}'.lower() == 'y':
        descriptor['capabilities']['tier_config_setup_request_processing'] = STATUSES

    if '{{ cookiecutter.tier_config_process_capabilities_2of3 }}'.lower() == 'y':
        descriptor['capabilities']['tier_config_change_request_processing'] = STATUSES

    if '{{ cookiecutter.tier_config_process_capabilities_3of3 }}'.lower() == 'y':
        descriptor['capabilities']['tier_config_adjustment_request_processing'] = STATUSES


def tierconfig_validation_capabilities(descriptor):
    if '{{ cookiecutter.tier_config_validation_capabilities_1of2 }}'.lower() == 'y':
        descriptor['capabilities']['tier_config_setup_request_validation'] = STATUSES

    if '{{ cookiecutter.tier_config_validation_capabilities_2of2 }}'.lower() == 'y':
        descriptor['capabilities']['tier_config_change_request_validation'] = STATUSES


def product_capabilities(descriptor):
    if '{{ cookiecutter.product_capabilities_1of2 }}'.lower() == 'y':
        descriptor['capabilities']['product_action_execution'] = []

    if '{{ cookiecutter.product_capabilities_2of2 }}'.lower() == 'y':
        descriptor['capabilities']['product_custom_event_processing'] = []


def process_tier_account_update_capabilities(descriptor):
    if '{{cookiecutter.tier_account_update_request}}'.lower() == 'y':
        descriptor['capabilities'][
            'tier_account_update_request_processing'
        ] = TIER_ACCOUNT_UPDATE_STATUSES


def process_usage_file_capabilities(descriptor):
    if '{{cookiecutter.usage_file_process}}'.lower() == 'y':
        descriptor['capabilities'][
            'usage_file_request_processing'
        ] = USAGE_FILE_STATUSES
    if '{{cookiecutter.usage_chunk_file_process}}'.lower() == 'y':
        descriptor['capabilities'][
            'part_usage_file_request_processing'
        ] = CHUNK_FILE_STATUSES


def process_schedule_example(descriptor):
    if '{{cookiecutter.include_schedules_example}}'.lower() == 'y':
        descriptor['schedulables'] = [{
            'name': 'Schedulable method mock',
            'description': 'It can be used to test DevOps scheduler.',
            'method': 'execute_scheduled_processing',
        }]


def process_variables_example(descriptor):
    if '{{cookiecutter.include_variables_example}}'.lower() == 'y':
        descriptor['variables'] = [
            {
                'name': 'VAR_NAME_1',
                'initial_value': 'VAR_VALUE_1',
                'secure': False
            },
            {
                'name': 'VAR_NAME_N',
                'initial_value': 'VAR_VALUE_N',
                'secure': True,
            }
        ]


def main():
    if '{{ cookiecutter.use_github_actions }}'.lower() == 'n':
        remove_github_actions()

    descriptor = json.load(open('{{ cookiecutter.package_slug }}/extension.json'))

    process_schedule_example(descriptor)
    process_variables_example(descriptor)
    subscription_processing_capabilities(descriptor)
    subscription_validation_capabilities(descriptor)
    tierconfig_processing_capabilities(descriptor)
    tierconfig_validation_capabilities(descriptor)
    product_capabilities(descriptor)
    process_tier_account_update_capabilities(descriptor)
    process_usage_file_capabilities(descriptor)

    json.dump(descriptor, open('{{ cookiecutter.package_slug }}/extension.json', 'w'), indent=2)

    with open('{{ cookiecutter.package_slug }}/extension.py', 'r') as fh:
        data = fh.read()

    with open('{{ cookiecutter.package_slug }}/extension.py', 'w') as fh:
        if data:
            fh.write(data.rstrip() + '\n')

    print('Done! Your extension project is ready to go!')


if __name__ == '__main__':
    main()
