# -*- coding: utf-8 -*-
#
# Copyright (c) {% now 'utc', '%Y' %}, {{ cookiecutter.author }}
# All rights reserved.
#

import pytest

from connect.eaas.extension import OK, Reschedule, SKIP

from {{ cookiecutter.package_slug }}.extension import {{ cookiecutter.project_name|title|replace(" ", "") }}Extension
{% if (
    cookiecutter.subscription_process_capabilities_1of6 == 'y' or 
    cookiecutter.subscription_process_capabilities_2of6 == 'y' or 
    cookiecutter.subscription_process_capabilities_3of6 == 'y' or 
    cookiecutter.subscription_process_capabilities_4of6 == 'y' or 
    cookiecutter.subscription_process_capabilities_5of6 == 'y' or 
    cookiecutter.subscription_process_capabilities_6of6 == 'y') %}
{% if cookiecutter.use_asyncio == 'y' %}
@pytest.mark.asyncio
{%- endif %}
{% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def test_process_asset_request(sync_client_factory, response_factory, logger):
    config = {}
    request = {}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = {{ cookiecutter.project_name|title|replace(" ", "") }}Extension(client, logger, config)
    result = {% if cookiecutter.use_asyncio == 'y' %}await {% endif %}ext.process_asset_request(request)
    assert result == OK
{% endif -%}

{% if (
    cookiecutter.subscription_validation_capabilities_1of2 == 'y' or 
    cookiecutter.subscription_validation_capabilities_2of2 == 'y') %}
{% if cookiecutter.use_asyncio == 'y' %}
@pytest.mark.asyncio
{%- endif %}
{% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def test_validate_asset_request(sync_client_factory, response_factory, logger):
    config = {}
    request = {}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = {{ cookiecutter.project_name|title|replace(" ", "") }}Extension(client, logger, config)
    result = {% if cookiecutter.use_asyncio == 'y' %}await {% endif %}ext.validate_asset_request(request)
    assert result == OK
{% endif -%}

{% if (
    cookiecutter.tier_config_process_capabilities_1of2 == 'y' or 
    cookiecutter.tier_config_process_capabilities_2of2 == 'y') %}
{% if cookiecutter.use_asyncio == 'y' %}
@pytest.mark.asyncio
{%- endif %}
{% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def test_process_tier_config_request(sync_client_factory, response_factory, logger):
    config = {}
    request = {}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = {{ cookiecutter.project_name|title|replace(" ", "") }}Extension(client, logger, config)
    result = {% if cookiecutter.use_asyncio == 'y' %}await {% endif %}ext.process_tier_config_request(request)
    assert result == OK
{% endif -%}

{% if (
    cookiecutter.tier_config_validation_capabilities_1of2 == 'y' or 
    cookiecutter.tier_config_validation_capabilities_2of2 == 'y') %}
{% if cookiecutter.use_asyncio == 'y' %}
@pytest.mark.asyncio
{%- endif %}
{% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def test_validate_tier_config_request(sync_client_factory, response_factory, logger):
    config = {}
    request = {}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = {{ cookiecutter.project_name|title|replace(" ", "") }}Extension(client, logger, config)
    result = {% if cookiecutter.use_asyncio == 'y' %}await {% endif %}ext.validate_tier_config_request(request)
    assert result == OK
{% endif -%}

{% if (
    cookiecutter.product_capabilities_1of2 == 'y' or 
    cookiecutter.product_capabilities_2of2 == 'y') %}
{% if cookiecutter.use_asyncio == 'y' %}
@pytest.mark.asyncio
{%- endif %}
{% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def test_process_product_request(sync_client_factory, response_factory, logger):
    config = {}
    request = {}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = {{ cookiecutter.project_name|title|replace(" ", "") }}Extension(client, logger, config)
    result = {% if cookiecutter.use_asyncio == 'y' %}await {% endif %}ext.process_product_request(request)
    assert result == OK
{% endif -%}
