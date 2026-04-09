from bson import ObjectId
from rest_framework import serializers

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value) if isinstance(value, ObjectId) else value
    def to_internal_value(self, data):
        return ObjectId(data) if isinstance(data, str) else data
