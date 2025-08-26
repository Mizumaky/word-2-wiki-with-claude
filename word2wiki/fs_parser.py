"""File system parser for FS document naming patterns."""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime
from .version_utils import version_sort_key


@dataclass
class FSDocument:
    """Represents an FS document with parsed metadata."""
    path: Path
    base_name: str
    version: Optional[str]
    date: Optional[str]
    full_version: str
    
    @property
    def display_name(self) -> str:
        """Human-readable display name."""
        # Convert underscores to spaces and title case
        return self.base_name.replace('_', ' ').title()
    
    @property
    def version_display(self) -> str:
        """Version for display purposes."""
        if self.version and self.date:
            return f"v{self.version} ({self.date})"
        elif self.version:
            return f"v{self.version}"
        elif self.date:
            return f"({self.date})"
        else:
            return "v1.0"


class FSParser:
    """Parser for FS document naming conventions."""
    
    # Regex patterns for different FS naming conventions
    PATTERNS = [
        # Pattern: HR_FS_Billing_Accounts_Receivables_CZ_00_03_at_2025_08_21.docx
        r'^(.+?)_(\d+_\d+)_at_(\d{4}_\d{2}_\d{2})\.docx$',
        # Pattern: HR_FS_Billing_Accounts_Receivables_CZ_at_2025_08_21.docx (no version)
        r'^(.+?)_at_(\d{4}_\d{2}_\d{2})\.docx$',
        # Pattern: HR_FS_Billing_Accounts_Receivables_CZ_00_03.docx (version only)
        r'^(.+?)_(\d+_\d+)\.docx$',
        # Pattern: HR_FS_Billing_Accounts_Receivables_CZ.docx (base name only)
        r'^(.+?)\.docx$'
    ]
    
    def __init__(self, source_dir: Path = Path("FS_source")):
        """Initialize parser with source directory.
        
        Args:
            source_dir: Directory containing FS documents
        """
        self.source_dir = Path(source_dir)
    
    def parse_filename(self, filename: str) -> Optional[FSDocument]:
        """Parse a single filename into FSDocument.
        
        Args:
            filename: Name of the file to parse
            
        Returns:
            FSDocument if parsing successful, None otherwise
        """
        file_path = self.source_dir / filename
        
        for pattern in self.PATTERNS:
            match = re.match(pattern, filename)
            if match:
                groups = match.groups()
                
                if len(groups) == 3:  # base_name, version, date
                    base_name, version, date = groups
                    full_version = f"{version}_{date}"
                elif len(groups) == 2:
                    # Could be base_name + date OR base_name + version
                    if re.match(r'\d{4}_\d{2}_\d{2}', groups[1]):
                        # It's a date
                        base_name, date = groups
                        version = None
                        full_version = date
                    else:
                        # It's a version
                        base_name, version = groups
                        date = None
                        full_version = version
                else:  # len(groups) == 1, base name only
                    base_name = groups[0]
                    version = None
                    date = None
                    full_version = "1.0"
                
                return FSDocument(
                    path=file_path,
                    base_name=base_name,
                    version=version,
                    date=date,
                    full_version=full_version
                )
        
        return None
    
    def find_all_fs_documents(self) -> List[FSDocument]:
        """Find all FS documents in the source directory.
        
        Returns:
            List of FSDocument objects, sorted by modification time (newest first)
        """
        if not self.source_dir.exists():
            return []
        
        documents = []
        for file_path in self.source_dir.glob("*.docx"):
            # Skip temporary files (starting with ~$)
            if file_path.name.startswith("~$"):
                continue
                
            doc = self.parse_filename(file_path.name)
            if doc:
                documents.append(doc)
        
        # Sort by modification time, newest first
        documents.sort(key=lambda d: d.path.stat().st_mtime, reverse=True)
        return documents
    
    def get_newest_document(self) -> Optional[FSDocument]:
        """Get the newest FS document.
        
        Returns:
            Newest FSDocument or None if no documents found
        """
        documents = self.find_all_fs_documents()
        return documents[0] if documents else None
    
    def group_by_base_name(self) -> Dict[str, List[FSDocument]]:
        """Group documents by their base name.
        
        Returns:
            Dictionary mapping base names to lists of documents
        """
        documents = self.find_all_fs_documents()
        groups = {}
        
        for doc in documents:
            if doc.base_name not in groups:
                groups[doc.base_name] = []
            groups[doc.base_name].append(doc)
        
        # Sort each group by version/date
        for base_name in groups:
            groups[base_name].sort(key=lambda d: self._version_sort_key(d), reverse=True)
        
        return groups
    
    def _version_sort_key(self, doc: FSDocument) -> Tuple:
        """Generate sort key for version ordering.
        
        Args:
            doc: FSDocument to generate key for
            
        Returns:
            Tuple for sorting (date, version)
        """
        date_key = 0
        version_key = (0, 0)
        
        if doc.date:
            try:
                # Parse date format YYYY_MM_DD
                date_str = doc.date.replace('_', '-')
                date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                date_key = date_obj.timestamp()
            except ValueError:
                pass
        
        if doc.version:
            try:
                # Parse version format XX_YY
                parts = doc.version.split('_')
                if len(parts) == 2:
                    version_key = (int(parts[0]), int(parts[1]))
            except ValueError:
                pass
        
        return (date_key, version_key)
    
    def find_existing_versions(self, base_name: str) -> List[str]:
        """Find existing converted versions for a base name.
        
        Args:
            base_name: Base name to search for
            
        Returns:
            List of version strings that have been converted
        """
        output_dir = Path("output")
        doc_dir = output_dir / base_name.replace('_', ' ').title().replace(' ', '_')
        
        if not doc_dir.exists():
            return []
        
        versions = []
        for version_dir in doc_dir.iterdir():
            if version_dir.is_dir() and version_dir.name.startswith('v'):
                versions.append(version_dir.name)
        
        return sorted(versions, key=version_sort_key, reverse=True)