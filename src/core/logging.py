import uuid
import logging
from itertools import chain

logger = logging.getLogger('app')


def instance_to_dict(instance):
    opts = instance._meta
    data = {}
    for f in chain(opts.concrete_fields, opts.private_fields):
        data[f.name] = f.value_from_object(instance)
    for f in opts.many_to_many:
        data[f.name] = [i.id for i in f.value_from_object(instance)]
    return data


class RequestLogger():
    def __init__(self, request, **kwargs):
        self.request = request
        self.kwargs = kwargs
        self.correlation_id = uuid.uuid4()

    def get_extra(self):
        extra = {
            'correlation_id': self.correlation_id,
        }
        try:
            extra['user'] = {
                'id': self.request.user.id,
                'username': self.request.user.username,
            }
        except Exception as err:
            extra['user'] = str(err)

        for key, value in self.kwargs.items():
            extra[key] = instance_to_dict(value)

        return extra

    def debug(self, *args, **kwargs):
        logger.debug(*args, **kwargs, extra=self.get_extra())

    def info(self, *args, **kwargs):
        logger.info(*args, **kwargs, extra=self.get_extra())

    def warning(self, *args, **kwargs):
        logger.warning(*args, **kwargs, extra=self.get_extra())


def with_context(**kwargs):
    return logger
