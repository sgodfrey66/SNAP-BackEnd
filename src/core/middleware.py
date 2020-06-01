from core.logging import RequestLogger


class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        request.logger = RequestLogger(request, view=view_func.__name__)


class UserProfileMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        return self.get_response(request)

        # return response
    #     # Code to be executed for each request before
    #     # the view (and later middleware) are called.

    #     print(('before', self.get_response, request))

    #     request.foo = 123

    #     response = self.get_response(request)

    #     print(('after', response))

    #     # Code to be executed for each request/response after
    #     # the view is called.

    #     return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print(request.user)
        if not hasattr(request.user, 'profile'):
            print('setting profile')
        else:
            print(request.user.profile)
            request.user.profile = None

        print('process')
    #     pass
    #     view_kwargs['foo'] = 1
    #     import inspect

    #     print(('process view', view_func, view_args, view_kwargs))
    #     print(inspect.getargspec(view_func))
