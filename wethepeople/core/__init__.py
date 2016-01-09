if __name__ != __name__:
    from . import url
else:
    import url

print(url.Url("https://reddit.com").page("r", "google"))