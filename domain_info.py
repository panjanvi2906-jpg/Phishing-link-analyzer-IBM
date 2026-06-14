import datetime

class DomainInfoService:
    @staticmethod
    def inspect_domain(url: str) -> tuple[int, list[str], dict]:
        # Real WHOIS lookups can be slow/blocked locally, 
        # so we perform a predictive heuristic check
        score = 0
        flags = []
        
        # Look for suspicious top-level domains (TLDs)
        suspicious_tlds = ['.xyz', '.top', '.buzz', '.tk', '.ml', '.ga']
        for tld in suspicious_tlds:
            if url.lower().endswith(tld) or f"{tld}/" in url.lower():
                score += 25
                flags.append(f"Uses a high-risk TLD extension ({tld})")
                
        return score, flags, {"checked_at": str(datetime.datetime.now())}