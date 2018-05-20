from scrapy_splash import SplashRequest


class ParseUtil():

    @staticmethod
    def start_request(url, parse_func, meta):
        yield SplashRequest(url=url, callback=parse_func, meta=meta,
                            args={
                                # optional; parameters passed to Splash HTTP API
                                'wait': 25,

                                # 'url' is prefilled from request url
                                # 'http_method' is set to 'POST' for POST requests
                                # 'body' is set to request body for POST requests
                            })

    @staticmethod
    def start_request_with_lua(url, parse_func, meta):
        script = '''
            function main(splash)
              assert(splash:go(splash.args.url))
              assert(splash:wait(0.5))
              local more_btn = splash:select('#house-online > div:nth-last-child(4) > div.all-list > span.more')
              if ( more_btn ~= nil )
              then  
              more_btn:mouse_click()
              assert(splash:wait(1))
              end  
              return splash:html()
            end
            '''

        yield SplashRequest(url=url, callback=parse_func, meta=meta, endpoint='execute',
                            args={
                                # optional; parameters passed to Splash HTTP API
                                'wait': 15,
                                # 'url': url,
                                # 'url' is prefilled from request url
                                # 'http_method' is set to 'POST' for POST requests
                                # 'body' is set to request body for POST requests
                                'lua_source': script
                            })

