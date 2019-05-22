# Copyright 2018/2019 ducandu GmbH. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from rlgraph.utils.specifiable import Specifiable


class SyncRules(Specifiable):
    """
    Describes a synchronization schedule, used to update the target value weights. The target values are gradually
    updates using exponential moving average as suggested by the paper.
    """
    def __init__(self, sync_every_n_updates=4, sync_tau=None):
        """
        Args:
            sync_every_n_updates (int): Every how many updates (calls to `Agent.update()`) do we update the target?
            sync_tau (int): The smoothing constant to use in the averaging. Setting to 1 replaces the values each iteration.
        """
        super(SyncRules, self).__init__()

        self.sync_every_n_updates = sync_every_n_updates
        self.sync_tau = sync_tau