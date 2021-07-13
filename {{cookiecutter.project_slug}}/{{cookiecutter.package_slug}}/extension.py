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
    {% if cookiecutter.subscription_process_capabilities_1of6 == 'y' %}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def process_asset_purchase_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ProcessingResponse.done()
    {% endif -%}

    {% if cookiecutter.subscription_process_capabilities_2of6 == 'y' %}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def process_asset_change_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ProcessingResponse.done()
    {% endif -%}

    {% if cookiecutter.subscription_process_capabilities_3of6 == 'y' %}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def process_asset_suspend_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ProcessingResponse.done()
    {% endif -%}

    {% if cookiecutter.subscription_process_capabilities_4of6 == 'y' %}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def process_asset_resume_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ProcessingResponse.done()
    {% endif -%}

    {% if cookiecutter.subscription_process_capabilities_5of6 == 'y' %}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def process_asset_cancel_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ProcessingResponse.done()
    {% endif -%}

    {% if cookiecutter.subscription_process_capabilities_6of6 == 'y' %}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def process_asset_adjustment_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ProcessingResponse.done()
    {% endif -%}

    {% if cookiecutter.tier_config_process_capabilities_1of2 == 'y' %}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def process_tier_config_setup_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ProcessingResponse.done()
    {% endif -%}

    {% if cookiecutter.tier_config_process_capabilities_2of2 == 'y' %}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def process_tier_config_change_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ProcessingResponse.done()
    {% endif -%}

    {% if cookiecutter.subscription_validation_capabilities_1of2 == 'y' %}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def validate_asset_purchase_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ValidationResponse.done(request)
    {% endif -%}

    {% if cookiecutter.subscription_validation_capabilities_2of2 == 'y' %}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def validate_asset_change_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ValidationResponse.done(request)
    {% endif -%}

    {% if cookiecutter.tier_config_validation_capabilities_1of2 == 'y' %}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def validate_tier_config_setup_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ValidationResponse.done(request)
    {% endif -%}

    {% if cookiecutter.tier_config_validation_capabilities_2of2 == 'y' %}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def validate_tier_config_change_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ValidationResponse.done(request)
    {% endif -%}

    {% if cookiecutter.product_capabilities_1of2 == 'y' %}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def execute_product_action(self, request):
        self.logger.info(f"Obtained product custom action with following data: {request}")
        return ProductActionResponse.done()
    {% endif -%}

    {% if cookiecutter.product_capabilities_2of2 == 'y' %}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def process_product_custom_event(self, request):
        self.logger.info(f"Obtained custom event with following data: {request}")
        return CustomEventResponse.done()
    {% endif -%}
