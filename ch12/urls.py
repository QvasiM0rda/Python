from urls_utils import gen_from_urls

urls = ('https://stepik.org', 'https://google.com', 'https://youtube.com')

for resp_len, status, url in gen_from_urls(urls):
    print(resp_len, '->', status, '->', url)
