def site_settings(request):
    return {
        "siteName": "Miners Online",
        "navigation": [
            {"name": "Home", "url": "/", "icon": "bi bi-house"},
            {"name": "News", "url": "/news/", "icon": "bi bi-newspaper"},
            {"name": "Wiki", "url": "/wiki/", "icon": "bi bi-book"},
        ]
    }
