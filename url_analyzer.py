import re
from urllib.parse import urlparse

class URLAnalyzer:
    @staticmethod
    def analyze_structure(url: str) -> tuple[int, list[str]]:
        score = 0
        flags = []
        
        # Clean url string for parsing
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
            
        try:
            parsed = urlparse(url)
            domain = parsed.netloc
            
            # 1. Check for IP address instead of domain
            ip_pattern = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
            if ip_pattern.match(domain.split(':')[0]):
                score += 35
                flags.append("Uses raw IP address instead of a domain name")
                
            # 2. Check for excessive length
            if len(url) > 75:
                score += 15
                flags.append("URL length is unusually long")
                
            # 3. Check for multiple subdomains
            if domain.count('.') > 3:
                score += 20
                flags.append("Excessive number of subdomains")
                
            # 4. Check for suspicious keywords in URL
            suspicious_keywords = ['login', 'verify', 'secure', 'bank', 'update', 'free', 'paypal']
            for keyword in suspicious_keywords:
                if keyword in url.lower():
                    score += 15
                    flags.append(f"Contains suspicious keyword: '{keyword}'")
                    break
                    
        except Exception:
            score += 20
            flags.append("Failed to cleanly parse URL structure")
            
        return score, flags