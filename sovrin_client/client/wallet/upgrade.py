from plenum.common.txn import TXN_TYPE, NAME, VERSION
from plenum.common.types import Identifier
from sovrin_common.generates_request import GeneratesRequest
from sovrin_common.txn import POOL_UPGRADE, ACTION, SCHEDULE, SHA256, TIMEOUT
from sovrin_common.types import Request


class Upgrade(GeneratesRequest):
    def __init__(self, name: str, version: str, action: str, schedule: dict,
                 sha256: str, timeout, trustee: Identifier):
        self.name = name
        self.version = version
        self.action = action
        self.schedule = schedule
        self.sha256 = sha256
        self.timeout = timeout
        self.trustee = trustee
        self.seqNo = None

    def _op(self):
        op = {
            TXN_TYPE: POOL_UPGRADE,
            NAME: self.name,
            VERSION: self.version,
            ACTION: self.action,
            SCHEDULE: self.schedule,
            SHA256: self.sha256,
            TIMEOUT: self.timeout
        }
        return op

    @property
    def key(self):
        return '.'.join([self.name, self.version, self.action])

    def ledgerRequest(self):
        if not self.seqNo:
            return Request(identifier=self.trustee, operation=self._op())
