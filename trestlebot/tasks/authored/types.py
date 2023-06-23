#!/usr/bin/python

#    Copyright 2023 Red Hat, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Trestle Bot constants"""

from enum import Enum


class AuthoredType(Enum):
    """Top-level OSCAL models that have authoring support"""

    CATALOG = "catalog"
    PROFILE = "profile"
    SSP = "ssp"
    COMPDEF = "compdef"


def check_authored_type(string):
    """Check if the string has a matching AuthoredType, if not raise an error"""
    try:
        item_type = AuthoredType[string.upper()]
        return item_type
    except KeyError:
        raise ValueError(f"Invalid item type: {string}")
