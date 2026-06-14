from urllib.parse import urlparse

class SSLChecker:
    @staticmethod
    def check_ssl(url: str) -> tuple[int, list[str], dict]:
        score = 0
        flags = []
        
        is_https = url.lower().startswith("https://")
        
        if not is_https:
            score = 30
            flags.append("Website does not use HTTPS encryption (unsecured)")
            
        return score, flags, {"https_enabled": is_https}