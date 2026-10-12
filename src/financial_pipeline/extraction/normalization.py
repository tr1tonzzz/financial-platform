"""Explicit VND monetary scales; unknown declarations never default to dong."""
import re
import unicodedata

UNIT_MULTIPLIERS = {'VND': 1, 'nghìn đồng': 1000, 'triệu đồng': 1000000, 'tỷ đồng': 1000000000}
SCALES = {
    'nghin': 'nghìn đồng', 'ngan': 'nghìn đồng', 'thousand': 'nghìn đồng',
    'thousands': 'nghìn đồng', '1000': 'nghìn đồng',
    'trieu': 'triệu đồng', 'million': 'triệu đồng', 'millions': 'triệu đồng', '1000000': 'triệu đồng',
    'ty': 'tỷ đồng', 'ti': 'tỷ đồng', 'billion': 'tỷ đồng', 'billions': 'tỷ đồng', '1000000000': 'tỷ đồng',
}
CURRENCIES = {'vnd', 'dong', 'dongvietnam'}


def monetary_unit(text):
    """Return a canonical unit, None for unrelated text, or reject a declaration."""
    folded = ''.join(c for c in unicodedata.normalize('NFD', text.casefold().replace('đ', 'd').replace('₫', 'dong'))
                     if not unicodedata.combining(c))
    prefix = re.match(r'^\s*(?:don\s*vi\s*(?:tinh|tien\s*te)?|dvt|units?(?:\s+of\s+measurement)?|currency)\b\s*[:=]?\s*', folded)
    body = folded[prefix.end():] if prefix else folded
    compact = ''.join(c for c in body if c.isalnum())
    if compact in CURRENCIES:
        return 'VND'
    for scale, canonical in SCALES.items():
        if any(compact in {scale+currency, currency+scale} for currency in CURRENCIES):
            return canonical
    if compact in SCALES and not compact.isdigit():
        raise ValueError('Scale has no currency; do not assume unscaled VND')
    foreign = re.fullmatch(r'(?:nghin|ngan|trieu|ty|ti|thousands?|millions?|billions?)?(?:usd|eur|gbp|jpy|cny|hkd|aud|sgd)', compact)
    if (prefix and compact) or foreign:
        raise ValueError('Unsupported or ambiguous monetary unit: '+text)
    return None
