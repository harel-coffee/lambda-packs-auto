# automatically generated by the FlatBuffers compiler, do not modify

# namespace: CalTableFlatBuffers

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()


class KeyValue(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsKeyValue(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = KeyValue()
        x.Init(buf, n + offset)
        return x

    # KeyValue
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # KeyValue
    def Key(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # KeyValue
    def Value(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


def KeyValueStart(builder):
    builder.StartObject(2)


def KeyValueAddKey(builder, key):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(key), 0)


def KeyValueAddValue(builder, value):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0)


def KeyValueEnd(builder):
    return builder.EndObject()
