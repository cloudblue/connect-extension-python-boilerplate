# -*- coding: utf-8 -*-
#
# Copyright (c) {% now 'utc', '%Y' %}, {{ cookiecutter.author }}
# All rights reserved.
#

import pytest

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

from {{ cookiecutter.package_slug }}.extension import {{ cookiecutter.project_name|title|replace(" ", "") }}Extension

{% if cookiecutter.subscription_process_capabilities_1of6 == 'y' %}
{% if cookiecutter.use_asyncio == 'y' %}
@pytest.mark.asyncio
{%- endif %}
{% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def test_process_asset_purchase_request(sync_client_factory, response_factory, logger):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = {{ cookiecutter.project_name|title|replace(" ", "") }}Extension(client, logger, config)
    result = {% if cookiecutter.use_asyncio == 'y' %}await {% endif %}ext.process_asset_purchase_request(request)
    assert result.status == 'success'
{% endif -%}


{% if cookiecutter.subscription_process_capabilities_2of6 == 'y' %}
{% if cookiecutter.use_asyncio == 'y' %}
@pytest.mark.asyncio
{%- endif %}
{% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def test_process_asset_change_request(sync_client_factory, response_factory, logger):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = {{ cookiecutter.project_name|title|replace(" ", "") }}Extension(client, logger, config)
    result = {% if cookiecutter.use_asyncio == 'y' %}await {% endif %}ext.process_asset_change_request(request)
    assert result.status == 'success'
{% endif -%}


{% if cookiecutter.subscription_process_capabilities_3of6 == 'y' %}
{% if cookiecutter.use_asyncio == 'y' %}
@pytest.mark.asyncio
{%- endif %}
{% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def test_process_asset_suspend_request(sync_client_factory, response_factory, logger):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = {{ cookiecutter.project_name|title|replace(" ", "") }}Extension(client, logger, config)
    result = {% if cookiecutter.use_asyncio == 'y' %}await {% endif %}ext.process_asset_suspend_request(request)
    assert result.status == 'success'
{% endif -%}


{% if cookiecutter.subscription_process_capabilities_4of6 == 'y' %}
{% if cookiecutter.use_asyncio == 'y' %}
@pytest.mark.asyncio
{%- endif %}
{% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def test_process_asset_resume_request(sync_client_factory, response_factory, logger):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = {{ cookiecutter.project_name|title|replace(" ", "") }}Extension(client, logger, config)
    result = {% if cookiecutter.use_asyncio == 'y' %}await {% endif %}ext.process_asset_resume_request(request)
    assert result.status == 'success'
{% endif -%}


{% if cookiecutter.subscription_process_capabilities_5of6 == 'y' %}
{% if cookiecutter.use_asyncio == 'y' %}
@pytest.mark.asyncio
{%- endif %}
{% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def test_process_asset_cancel_request(sync_client_factory, response_factory, logger):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = {{ cookiecutter.project_name|title|replace(" ", "") }}Extension(client, logger, config)
    result = {% if cookiecutter.use_asyncio == 'y' %}await {% endif %}ext.process_asset_cancel_request(request)
    assert result.status == 'success'
{% endif -%}


{% if cookiecutter.subscription_process_capabilities_6of6 == 'y' %}
{% if cookiecutter.use_asyncio == 'y' %}
@pytest.mark.asyncio
{%- endif %}
{% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def test_process_asset_adjustment_request(sync_client_factory, response_factory, logger):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = {{ cookiecutter.project_name|title|replace(" ", "") }}Extension(client, logger, config)
    result = {% if cookiecutter.use_asyncio == 'y' %}await {% endif %}ext.process_asset_adjustment_request(request)
    assert result.status == 'success'
{% endif -%}


{% if cookiecutter.subscription_validation_capabilities_1of2 == 'y' %}
{% if cookiecutter.use_asyncio == 'y' %}
@pytest.mark.asyncio
{%- endif %}
{% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def test_validate_asset_purchase_request(sync_client_factory, response_factory, logger):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = {{ cookiecutter.project_name|title|replace(" ", "") }}Extension(client, logger, config)
    result = {% if cookiecutter.use_asyncio == 'y' %}await {% endif %}ext.validate_asset_purchase_request(request)
    assert result.status == 'success'
    assert result.data == request
{% endif -%}


{% if cookiecutter.subscription_validation_capabilities_2of2 == 'y' %}
{% if cookiecutter.use_asyncio == 'y' %}
@pytest.mark.asyncio
{%- endif %}
{% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def test_validate_asset_change_request(sync_client_factory, response_factory, logger):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = {{ cookiecutter.project_name|title|replace(" ", "") }}Extension(client, logger, config)
    result = {% if cookiecutter.use_asyncio == 'y' %}await {% endif %}ext.validate_asset_change_request(request)
    assert result.status == 'success'
    assert result.data == request
{% endif -%}


{% if cookiecutter.tier_config_process_capabilities_1of2 == 'y' %}
{% if cookiecutter.use_asyncio == 'y' %}
@pytest.mark.asyncio
{%- endif %}
{% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def test_process_tier_config_setup_request(sync_client_factory, response_factory, logger):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = {{ cookiecutter.project_name|title|replace(" ", "") }}Extension(client, logger, config)
    result = {% if cookiecutter.use_asyncio == 'y' %}await {% endif %}ext.process_tier_config_setup_request(request)
    assert result.status == 'success'
{% endif -%}


{% if cookiecutter.tier_config_process_capabilities_2of2 == 'y' %}
{% if cookiecutter.use_asyncio == 'y' %}
@pytest.mark.asyncio
{%- endif %}
{% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def test_process_tier_config_change_request(sync_client_factory, response_factory, logger):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = {{ cookiecutter.project_name|title|replace(" ", "") }}Extension(client, logger, config)
    result = {% if cookiecutter.use_asyncio == 'y' %}await {% endif %}ext.process_tier_config_change_request(request)
    assert result.status == 'success'
{% endif -%}

{% if cookiecutter.tier_config_validation_capabilities_1of2 == 'y' %}
{% if cookiecutter.use_asyncio == 'y' %}
@pytest.mark.asyncio
{%- endif %}
{% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def test_validate_tier_config_setup_request(sync_client_factory, response_factory, logger):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = {{ cookiecutter.project_name|title|replace(" ", "") }}Extension(client, logger, config)
    result = {% if cookiecutter.use_asyncio == 'y' %}await {% endif %}ext.validate_tier_config_setup_request(request)
    assert result.status == 'success'
    assert result.data == request
{% endif -%}


{% if cookiecutter.tier_config_validation_capabilities_2of2 == 'y' %}
{% if cookiecutter.use_asyncio == 'y' %}
@pytest.mark.asyncio
{%- endif %}
{% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def test_validate_tier_config_change_request(sync_client_factory, response_factory, logger):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = {{ cookiecutter.project_name|title|replace(" ", "") }}Extension(client, logger, config)
    result = {% if cookiecutter.use_asyncio == 'y' %}await {% endif %}ext.validate_tier_config_change_request(request)
    assert result.status == 'success'
    assert result.data == request
{% endif -%}

{% if cookiecutter.product_capabilities_1of2 == 'y' %}
{% if cookiecutter.use_asyncio == 'y' %}
@pytest.mark.asyncio
{%- endif %}
{% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def test_process_product_action(sync_client_factory, response_factory, logger):
    config = {}
    request = {}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = {{ cookiecutter.project_name|title|replace(" ", "") }}Extension(client, logger, config)
    result = {% if cookiecutter.use_asyncio == 'y' %}await {% endif %}ext.execute_product_action(request)
    assert result.status == 'success'
    assert result.http_status == 200
    assert result.headers is None
    assert result.body is None
{% endif -%}

{% if cookiecutter.product_capabilities_2of2 == 'y' %}
{% if cookiecutter.use_asyncio == 'y' %}
@pytest.mark.asyncio
{%- endif %}
{% if cookiecutter.use_asyncio == 'y' %}async {% endif %}def test_process_product_custom_event(sync_client_factory, response_factory, logger):
    config = {}
    request = {}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = {{ cookiecutter.project_name|title|replace(" ", "") }}Extension(client, logger, config)
    result = {% if cookiecutter.use_asyncio == 'y' %}await {% endif %}ext.process_product_custom_event(request)
    assert result.status == 'success'
    assert result.http_status == 200
    assert result.headers is None
    assert result.body is None
{% endif -%}
