# -*- coding: utf-8 -*-
#
# Copyright (c) {% now 'utc', '%Y' %}, {{ cookiecutter.author }}
# All rights reserved.
#
from connect.eaas.extension import (
    {%- if cookiecutter.product_capabilities_2of2 == 'y' %}
    CustomEventResponse,
    {%- endif %}
    Extension,
    {%- if (
        cookiecutter.subscription_process_capabilities_1of6 == 'y' or 
        cookiecutter.subscription_process_capabilities_2of6 == 'y' or 
        cookiecutter.subscription_process_capabilities_3of6 == 'y' or 
        cookiecutter.subscription_process_capabilities_4of6 == 'y' or 
        cookiecutter.subscription_process_capabilities_5of6 == 'y' or 
        cookiecutter.subscription_process_capabilities_6of6 == 'y' or
        cookiecutter.tier_config_process_capabilities_1of3 == 'y' or 
        cookiecutter.tier_config_process_capabilities_2of3 == 'y' or
        cookiecutter.tier_config_process_capabilities_3of3 == 'y') %}
    ProcessingResponse,
    {%- endif %}
    {%- if cookiecutter.product_capabilities_1of2 == 'y' %}
    ProductActionResponse,
    {%- endif %}
    {%- if cookiecutter.include_schedules_example == 'y' %}
    ScheduledExecutionResponse,
    {%- endif %}
    {%- if (
        cookiecutter.subscription_validation_capabilities_1of2 == 'y' or 
        cookiecutter.subscription_validation_capabilities_2of2 == 'y' or
        cookiecutter.tier_config_validation_capabilities_1of2 == 'y' or 
        cookiecutter.tier_config_validation_capabilities_2of2 == 'y') %}
    ValidationResponse,
    {%- endif %}
)


class {{ cookiecutter.project_name|title|replace(" ", "") }}Extension(Extension):

    {% if cookiecutter.subscription_process_capabilities_1of6 == 'y' -%}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def process_asset_purchase_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ProcessingResponse.done()

    {% endif -%}

    {% if cookiecutter.subscription_process_capabilities_2of6 == 'y' -%}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def process_asset_change_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ProcessingResponse.done()

    {% endif -%}

    {% if cookiecutter.subscription_process_capabilities_3of6 == 'y' -%}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def process_asset_suspend_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ProcessingResponse.done()

    {% endif -%}

    {% if cookiecutter.subscription_process_capabilities_4of6 == 'y' -%}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def process_asset_resume_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ProcessingResponse.done()

    {% endif -%}

    {% if cookiecutter.subscription_process_capabilities_5of6 == 'y' -%}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def process_asset_cancel_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ProcessingResponse.done()

    {% endif -%}

    {% if cookiecutter.subscription_process_capabilities_6of6 == 'y' -%}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def process_asset_adjustment_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ProcessingResponse.done()

    {% endif -%}

    {% if cookiecutter.tier_config_process_capabilities_1of3 == 'y' -%}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def process_tier_config_setup_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ProcessingResponse.done()

    {% endif -%}

    {% if cookiecutter.tier_config_process_capabilities_2of3 == 'y' -%}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def process_tier_config_change_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ProcessingResponse.done()

    {% endif -%}

    {% if cookiecutter.tier_config_process_capabilities_3of3 == 'y' -%}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def process_tier_config_adjustment_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ProcessingResponse.done()

    {% endif -%}

    {% if cookiecutter.subscription_validation_capabilities_1of2 == 'y' -%}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def validate_asset_purchase_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ValidationResponse.done(request)

    {% endif -%}

    {% if cookiecutter.subscription_validation_capabilities_2of2 == 'y' -%}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def validate_asset_change_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ValidationResponse.done(request)

    {% endif -%}

    {% if cookiecutter.tier_config_validation_capabilities_1of2 == 'y' -%}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def validate_tier_config_setup_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ValidationResponse.done(request)

    {% endif -%}

    {% if cookiecutter.tier_config_validation_capabilities_2of2 == 'y' -%}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def validate_tier_config_change_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ValidationResponse.done(request)

    {% endif -%}

    {% if cookiecutter.product_capabilities_1of2 == 'y' -%}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def execute_product_action(self, request):
        self.logger.info(f"Obtained product custom action with following data: {request}")
        return ProductActionResponse.done()

    {% endif -%}

    {% if cookiecutter.product_capabilities_2of2 == 'y' -%}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def process_product_custom_event(self, request):
        self.logger.info(f"Obtained custom event with following data: {request}")
        return CustomEventResponse.done()

    {% endif -%}

    {% if cookiecutter.usage_file_process == 'y' -%}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def process_usage_file(self, request):  # pragma: no cover
        self.logger.info(
            f"Received event for usage file {request['id']} "
            f"in status {request['status']}",
        )
        return ProcessingResponse.done()

    {% endif -%}

    {% if cookiecutter.usage_chunk_file_process == 'y' -%}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def process_usage_chunk_file(self, request):  # pragma: no cover
        self.logger.info(
            f"Received event for usage chunks file {request['id']} "
            f"in status {request['status']}",
        )
        return ProcessingResponse.done()

    {% endif -%}

    {% if cookiecutter.tier_account_update_request == 'y' -%}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def process_tier_account_update_request(self, request):  # pragma: no cover
        self.logger.info(
            f"Received event for tier account request  {request['id']}, type {request['type']} "
            f"in status {request['status']}",
        )
        return ProcessingResponse.done()

    {% endif -%}

    {% if cookiecutter.include_schedules_example == 'y' -%}
    {% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def execute_scheduled_processing(self, schedule):  # pragma: no cover
        self.logger.info(
            f"Received event for schedule  {schedule['id']}",
        )
        return ScheduledExecutionResponse.done()

    {% endif -%}