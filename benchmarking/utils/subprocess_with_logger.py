#!/usr/bin/env python3.6

##############################################################################
# Copyright 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
##############################################################################

import subprocess
from .custom_logger import getLogger


def processRun(*args, **kwargs):
    getLogger().info("Running: %s", ' '.join(*args))
    try:
        return subprocess.check_output(*args, **kwargs).decode("utf-8")
    except subprocess.CalledProcessError:
        getLogger().error("Command failed: %s", ' '.join(*args))
    except subprocess.TimeoutExpired:
        getLogger().error("Command timeout: %s", ' '.join(*args))
    return None