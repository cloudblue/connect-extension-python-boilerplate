# -*- coding: utf-8 -*-

# This file is part of the Ingram Micro Cloud Blue Connect Report Python Boilerplate.
# Copyright (c) 2019-2021 Ingram Micro. All Rights Reserved.

import json
import os
import shutil


STATUSES = [
    'draft',
    'tiers_setup',
    'pending',
    'inquiring',
    'approved',
    'failed',
]

def remove_github_actions():
    shutil.rmtree('.github')

def subscription_processing_capabilities(descriptor):
    if '{{ cookiecutter.subscription_process_capabilities_1of6 }}'.lower() == 'y':
        descriptor['capabilities']['asset_purchase_request_processing'] = STATUSES
    
    if '{{ cookiecutter.subscription_process_capabilities_2of6 }}'.lower() == 'y':
        descriptor['capabilities']['asset_change_request_processing'] = STATUSES
    
    if '{{ cookiecutter.subscription_process_capabilities_3of6 }}'.lower() == 'y':
        descriptor['capabilities']['asset_suspend_request_processing'] = STATUSES
    
    if '{{ cookiecutter.subscription_process_capabilities_4of6 }}'.lower() == 'y':
        descriptor['capabilities']['asset_resume_request_processing'] = STATUSES
    
    if '{{ cookiecutter.subscription_process_capabilities_5of6 }}'.lower() == 'y':
        descriptor['capabilities']['asset_cancel_request_processing'] = STATUSES
    
    if '{{ cookiecutter.subscription_process_capabilities_6of6 }}'.lower() == 'y':
        descriptor['capabilities']['asset_adjustment_request_processing'] = STATUSES

def subscription_validation_capabilities(descriptor):
    if '{{ cookiecutter.subscription_validation_capabilities_1of2 }}'.lower() == 'y':
        descriptor['capabilities']['asset_purchase_request_validation'] = STATUSES
    
    if '{{ cookiecutter.subscription_validation_capabilities_2of2 }}'.lower() == 'y':
        descriptor['capabilities']['asset_change_request_validation'] = STATUSES

def tierconfig_processing_capabilities(descriptor):
    if '{{ cookiecutter.tier_config_process_capabilities_1of2 }}'.lower() == 'y':
        descriptor['capabilities']['tier_config_setup_request_processing'] = STATUSES
    
    if '{{ cookiecutter.tier_config_process_capabilities_2of2 }}'.lower() == 'y':
        descriptor['capabilities']['tier_config_change_request_processing'] = STATUSES

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

def main():    
    if '{{ cookiecutter.use_github_actions }}'.lower() == 'n':
        remove_github_actions()
    
    descriptor = json.load(open('{{ cookiecutter.package_slug }}/extension.json'))
    
    subscription_processing_capabilities(descriptor)
    subscription_validation_capabilities(descriptor)
    tierconfig_processing_capabilities(descriptor)
    tierconfig_validation_capabilities(descriptor)
    product_capabilities(descriptor)
    
    json.dump(descriptor, open('{{ cookiecutter.package_slug }}/extension.json', 'w'), indent=2)
    
    print('Done! Your extension project is ready to go!')

if __name__ == '__main__':
    main()
