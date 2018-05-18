from scrapy_splash import SplashRequest


class ParseUtil():

    @staticmethod
    def start_request(url, parse_func, meta):
        yield SplashRequest(url=url, callback=parse_func, meta=meta,
                            args={
                                # optional; parameters passed to Splash HTTP API
                                'wait': 5,

                                # 'url' is prefilled from request url
                                # 'http_method' is set to 'POST' for POST requests
                                # 'body' is set to request body for POST requests
                            })
