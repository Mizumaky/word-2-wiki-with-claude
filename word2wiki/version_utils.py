"""Version comparison utilities for proper semantic version sorting."""


def version_sort_key(version_string: str):
    """Generate sort key for proper version ordering.
    
    Args:
        version_string: Version string like 'v00_02' or 'v00_03_2025_08_21'
        
    Returns:
        Tuple for sorting (version_parts, date_parts)
    """
    # Remove 'v' prefix
    version_without_v = version_string[1:] if version_string.startswith('v') else version_string
    
    # Split by underscores
    parts = version_without_v.split('_')
    
    version_parts = []
    date_parts = []
    
    # Extract version numbers (first parts that are numeric)
    for i, part in enumerate(parts):
        if part.isdigit():
            version_parts.append(int(part))
        else:
            # If we encounter a non-digit, treat remaining as date/metadata
            date_parts = parts[i:]
            break
    
    # If no version parts found, use 0
    if not version_parts:
        version_parts = [0]
    
    # Convert date parts to comparable format if possible
    date_key = 0
    if len(date_parts) >= 3 and all(p.isdigit() for p in date_parts[:3]):
        try:
            # Assume format YYYY_MM_DD
            year, month, day = int(date_parts[0]), int(date_parts[1]), int(date_parts[2])
            date_key = year * 10000 + month * 100 + day
        except (ValueError, IndexError):
            pass
    
    # Return tuple for sorting: version parts first, then date
    return (tuple(version_parts), date_key)