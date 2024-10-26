from aomaker.base.base_api import BaseApi


class DemoApi(BaseApi):
    
    def demo_get(self):
        """this is a demo get api"""
        http_data = {
            'api_path': '/test',
            'method': 'get',
            'params': {'name': 'aomaker'}
        }
        response = self.send_http(http_data)
        return response
    
    def demo_post(self):
        """this is a demo post api"""
        body = {
            'name': 'aomaker',
            'version': 'v2'
        }
        http_data = {
            'api_path': '/test',
            'method': 'get',
            'params': {'name': 'aomaker'},
            'data': body
        }
        response = self.send_http(http_data)
        return response
    