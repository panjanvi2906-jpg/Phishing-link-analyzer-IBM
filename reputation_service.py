from app.services.url_analyzer import URLAnalyzer
from app.services.ssl_checker import SSLChecker
from app.services.domain_info import DomainInfoService

class ReputationService:
    @staticmethod
    def evaluate_url(url: str) -> dict:
        struct_score, struct_flags = URLAnalyzer.analyze_structure(url)
        ssl_score, ssl_flags, ssl_details = SSLChecker.check_ssl(url)
        domain_score, domain_flags, domain_details = DomainInfoService.inspect_domain(url)
        
        # Aggregate scores (capped at 100)
        total_score = min(struct_score + ssl_score + domain_score, 100)
        all_flags = struct_flags + ssl_flags + domain_flags
        
        # Consider phishing if score is greater than 40
        is_phishing = total_score >= 40
        
        return {
            "url": url,
            "is_phishing": is_phishing,
            "risk_score": total_score,
            "flags": all_flags,
            "details": {**ssl_details, **domain_details}
        }