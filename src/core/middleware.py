class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        pass
    #     # Code to be executed for each request before
    #     # the view (and later middleware) are called.

    #     print(('before', self.get_response, request))

    #     request.foo = 123

    #     response = self.get_response(request)

    #     print(('after', response))

    #     # Code to be executed for each request/response after
    #     # the view is called.

    #     return response


    # def process_view(self, request, view_func, view_args, view_kwargs):
    #     view_kwargs['foo'] = 1
    #     import inspect

    #     print(('process view', view_func, view_args, view_kwargs))
    #     print(inspect.getargspec(view_func))
