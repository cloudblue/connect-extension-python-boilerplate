# -*- coding: utf-8 -*-
#
# Copyright (c) {% now 'utc', '%Y' %}, {{ cookiecutter.author }}
# All rights reserved.
#
from connect.eaas.extension import (
    Extension,
    {%- if (
        cookiecutter.subscription_process_capabilities_1of6 == 'y' or 
        cookiecutter.subscription_process_capabilities_2of6 == 'y' or 
        cookiecutter.subscription_process_capabilities_3of6 == 'y' or 
        cookiecutter.subscription_process_capabilities_4of6 == 'y' or 
        cookiecutter.subscription_process_capabilities_5of6 == 'y' or 
        cookiecutter.subscription_process_capabilities_6of6 == 'y' or
        cookiecutter.tier_config_process_capabilities_1of2 == 'y' or 
        cookiecutter.tier_config_process_capabilities_2of2 == 'y') %}
    ProcessingResponse,
    {%- endif %}
    {%- if (
        cookiecutter.subscription_validation_capabilities_1of2 == 'y' or 
        cookiecutter.subscription_validation_capabilities_2of2 == 'y' or
        cookiecutter.tier_config_validation_capabilities_1of2 == 'y' or 
        cookiecutter.tier_config_validation_capabilities_2of2 == 'y') %}
    ValidationResponse,
    {%- endif %}
    {%- if cookiecutter.product_capabilities_1of2 == 'y' %}
    ProductActionResponse,
    {%- endif %}
    {%- if cookiecutter.product_capabilities_2of2 == 'y' %}
    CustomEventResponse,
    {%- endif %}
)


class {{ cookiecutter.project_name|title|replace(" ", "") }}Extension(Extension):
    {% if (
        cookiecutter.subscription_process_capabilities_1of6 == 'y' or 
        cookiecutter.subscription_process_capabilities_2of6 == 'y' or 
        cookiecutter.subscription_process_capabilities_3of6 == 'y' or 
        cookiecutter.subscription_process_capabilities_4of6 == 'y' or 
        cookiecutter.subscription_process_capabilities_5of6 == 'y' or 
        cookiecutter.subscription_process_capabilities_6of6 == 'y') %}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def process_asset_request(self, request):
        pass
    {% endif -%}

    {% if (
        cookiecutter.tier_config_process_capabilities_1of2 == 'y' or 
        cookiecutter.tier_config_process_capabilities_2of2 == 'y') %}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def process_tier_config_request(self, request):
        pass
    {% endif -%}

    {% if (
        cookiecutter.subscription_validation_capabilities_1of2 == 'y' or 
        cookiecutter.subscription_validation_capabilities_2of2 == 'y') %}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def validate_asset_request(self, request):
        pass
    {% endif -%}

    {% if (
        cookiecutter.tier_config_validation_capabilities_1of2 == 'y' or 
        cookiecutter.tier_config_validation_capabilities_2of2 == 'y') %}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def validate_tier_config_request(self, request):
        pass
    {% endif -%}

    {% if (
        cookiecutter.product_capabilities_1of2 == 'y' or 
        cookiecutter.product_capabilities_2of2 == 'y') %}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def process_product_request(self, request):
        pass
    {% endif -%}