# Backend/patch_hfhub.py
import huggingface_hub as _hf

# If cached_download is missing, alias hf_hub_download => cached_download
if not hasattr(_hf, "cached_download") and hasattr(_hf, "hf_hub_download"):
    _hf.cached_download = _hf.hf_hub_download
