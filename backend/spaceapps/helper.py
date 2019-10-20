import urllib.parse as urlparse
 
def query_params(query_string):
    query_params = dict(parse_qs(query_string))
    query_params = {k:v[0] for k, v in query_params.items()}
    return query_params