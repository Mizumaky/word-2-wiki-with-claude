"""Configuration module for future extensibility including Obsidian support."""

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Any, Optional
import json


@dataclass
class ConversionConfig:
    """Configuration for document conversion."""
    
    # Output formats
    html_output: bool = True
    markdown_output: bool = False  # Future Obsidian support
    
    # HTML-specific settings
    split_by_headers: bool = True
    header_level: int = 1
    create_toc: bool = True
    toc_depth: int = 3
    embed_resources: bool = True
    
    # Markdown-specific settings (for future Obsidian support)
    obsidian_vault_path: Optional[Path] = None
    obsidian_links_format: str = "wikilink"  # "wikilink" or "markdown"
    obsidian_image_format: str = "embed"     # "embed" or "link"
    
    # Media handling
    media_dir: str = "media"
    extract_media: bool = True
    
    # Git settings
    auto_commit: bool = False
    commit_message_template: str = "Convert {filename} to {format}"
    
    # File naming
    output_name_pattern: str = "{stem}_{index:02d}_{title}"
    sanitize_filenames: bool = True
    max_filename_length: int = 50
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert config to dictionary."""
        result = {}
        for field_name, field_value in self.__dict__.items():
            if isinstance(field_value, Path):
                result[field_name] = str(field_value)
            else:
                result[field_name] = field_value
        return result
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ConversionConfig':
        """Create config from dictionary."""
        # Convert string paths back to Path objects
        if 'obsidian_vault_path' in data and data['obsidian_vault_path']:
            data['obsidian_vault_path'] = Path(data['obsidian_vault_path'])
        
        return cls(**data)
    
    def save_to_file(self, config_path: Path) -> None:
        """Save configuration to JSON file."""
        config_path.parent.mkdir(parents=True, exist_ok=True)
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(self.to_dict(), f, indent=2)
    
    @classmethod
    def load_from_file(cls, config_path: Path) -> 'ConversionConfig':
        """Load configuration from JSON file."""
        if not config_path.exists():
            return cls()  # Return default config
        
        with open(config_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        return cls.from_dict(data)


class ObsidianConfig:
    """Configuration helpers for future Obsidian integration."""
    
    @staticmethod
    def get_obsidian_pandoc_args(vault_path: Path, config: ConversionConfig) -> list[str]:
        """Get Pandoc arguments for Obsidian-compatible markdown.
        
        This method prepares arguments for future Obsidian markdown conversion.
        """
        args = [
            '--to=markdown',
            '--wrap=none',
            '--atx-headers',
        ]
        
        # Obsidian-specific formatting
        if config.obsidian_links_format == "wikilink":
            # Future: Add filter for converting links to [[wikilink]] format
            pass
        
        # Image handling for Obsidian
        if config.obsidian_image_format == "embed":
            args.append(f'--extract-media={vault_path / "attachments"}')
        
        return args
    
    @staticmethod
    def convert_html_links_to_wikilinks(content: str) -> str:
        """Convert HTML links to Obsidian wikilinks format.
        
        This is a placeholder for future implementation.
        """
        # Future implementation:
        # - Convert <a href="file.html">Title</a> to [[file|Title]]
        # - Handle internal document links
        # - Convert image references to Obsidian format
        return content
    
    @staticmethod
    def setup_obsidian_vault_structure(vault_path: Path) -> None:
        """Set up Obsidian vault directory structure.
        
        This is a placeholder for future implementation.
        """
        vault_path.mkdir(parents=True, exist_ok=True)
        (vault_path / "attachments").mkdir(exist_ok=True)
        (vault_path / ".obsidian").mkdir(exist_ok=True)
        
        # Future: Create Obsidian configuration files
        # - workspace.json
        # - app.json
        # - appearance.json
        # etc.


def get_default_config_path() -> Path:
    """Get default configuration file path."""
    return Path.cwd() / "word2wiki_config.json"


def load_config(config_path: Optional[Path] = None) -> ConversionConfig:
    """Load configuration from file or return default."""
    if config_path is None:
        config_path = get_default_config_path()
    
    return ConversionConfig.load_from_file(config_path)