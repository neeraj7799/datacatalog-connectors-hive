#!/usr/bin/python
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import sys

from google.datacatalog_connectors.hive.sync import datacatalog_synchronizer

# Enable logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

datacatalog_synchronizer.DataCatalogSynchronizer(
    project_id='uat-env-1',
    location_id='us-central1',
    hive_metastore_db_host='localhost',
    hive_metastore_db_user='hive',
    hive_metastore_db_pass='hive',
    hive_metastore_db_name='metastore',
    hive_metastore_db_type='postgresql').run()
