#!/usr/bin/env python3

from mitmproxy import http
from mitmproxy import ctx


def request(flow: http.HTTPFlow) -> None:
    ctx.log.info('{} {}'.format(flow.request.method, flow.request.url))
    flow.kill()
