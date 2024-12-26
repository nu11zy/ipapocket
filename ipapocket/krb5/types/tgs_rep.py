from ipapocket.krb5.types.kdc_rep import KdcRep
from ipapocket.krb5.asn1 import TgsRepAsn1


class TgsRep:
    _kdc_rep: KdcRep = None

    def __init__(self, kdc_rep: KdcRep = None):
        self._kdc_rep = kdc_rep

    @property
    def kdc_rep(self) -> KdcRep:
        return self._kdc_rep

    @kdc_rep.setter
    def kdc_rep(self, value) -> None:
        self._kdc_rep = value

    @classmethod
    def load(cls, data: TgsRepAsn1):
        if isinstance(data, TgsRep):
            data = data.to_asn1()
        return cls(KdcRep.load(data))

    def to_asn1(self) -> TgsRepAsn1:
        return TgsRepAsn1(self._kdc_rep)

    def dump(self) -> bytes:
        """
        Dump object to bytes (with ASN1 structure)
        """
        return self.to_asn1().dump()