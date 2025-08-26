"""Git integration for versioning converted documents."""

from pathlib import Path
from typing import Dict, List, Optional
import git
from rich.console import Console

console = Console()


class GitManager:
    """Manages git operations for the word2wiki project."""
    
    def __init__(self, repo_path: Path = Path.cwd()):
        """Initialize git manager.
        
        Args:
            repo_path: Path to the git repository
        """
        self.repo_path = Path(repo_path)
        self.repo: Optional[git.Repo] = None
        
    def init_repository(self) -> bool:
        """Initialize a new git repository if one doesn't exist.
        
        Returns:
            True if repository was created or already exists
        """
        try:
            if (self.repo_path / '.git').exists():
                self.repo = git.Repo(self.repo_path)
                console.print("✓ Git repository found", style="green")
                return True
            else:
                self.repo = git.Repo.init(self.repo_path)
                console.print("✓ Git repository initialized", style="green")
                
                # Create initial .gitignore
                gitignore_path = self.repo_path / '.gitignore'
                if not gitignore_path.exists():
                    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
.venv/
.env/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Temporary files
*.tmp
~$*
"""
                    with open(gitignore_path, 'w') as f:
                        f.write(gitignore_content)
                    console.print("✓ Created .gitignore", style="green")
                
                return True
                
        except Exception as e:
            console.print(f"✗ Git initialization failed: {e}", style="red")
            return False
    
    def add_files(self, file_paths: List[Path]) -> bool:
        """Add files to git staging area.
        
        Args:
            file_paths: List of file paths to add
            
        Returns:
            True if files were added successfully
        """
        if not self.repo:
            console.print("✗ No git repository found", style="red")
            return False
            
        try:
            for file_path in file_paths:
                if file_path.exists():
                    # Convert to relative path from repo root
                    rel_path = file_path.relative_to(self.repo_path)
                    self.repo.index.add([str(rel_path)])
                    console.print(f"✓ Added {rel_path}", style="green")
                else:
                    console.print(f"✗ File not found: {file_path}", style="red")
            
            return True
            
        except Exception as e:
            console.print(f"✗ Failed to add files: {e}", style="red")
            return False
    
    def commit_changes(self, message: str, author_name: Optional[str] = None, author_email: Optional[str] = None) -> bool:
        """Commit staged changes.
        
        Args:
            message: Commit message
            author_name: Optional author name
            author_email: Optional author email
            
        Returns:
            True if commit was successful
        """
        if not self.repo:
            console.print("✗ No git repository found", style="red")
            return False
            
        try:
            # Check if there are any staged changes
            if not self.repo.index.diff("HEAD"):
                console.print("No changes to commit", style="yellow")
                return True
            
            # Set author if provided
            author = None
            if author_name and author_email:
                author = git.Actor(author_name, author_email)
            
            # Commit changes
            commit = self.repo.index.commit(message, author=author)
            console.print(f"✓ Committed: {commit.hexsha[:8]} - {message}", style="green")
            return True
            
        except Exception as e:
            console.print(f"✗ Commit failed: {e}", style="red")
            return False
    
    def create_version_tag(self, tag_name: str, message: Optional[str] = None) -> bool:
        """Create a version tag.
        
        Args:
            tag_name: Name of the tag
            message: Optional tag message
            
        Returns:
            True if tag was created successfully
        """
        if not self.repo:
            console.print("✗ No git repository found", style="red")
            return False
            
        try:
            if message:
                tag = self.repo.create_tag(tag_name, message=message)
            else:
                tag = self.repo.create_tag(tag_name)
                
            console.print(f"✓ Created tag: {tag_name}", style="green")
            return True
            
        except Exception as e:
            console.print(f"✗ Tag creation failed: {e}", style="red")
            return False
    
    def get_status(self) -> Dict[str, List[str]]:
        """Get repository status.
        
        Returns:
            Dictionary with status information
        """
        if not self.repo:
            return {"error": ["No git repository found"]}
            
        try:
            status = {
                "untracked": [item for item in self.repo.untracked_files],
                "modified": [item.a_path for item in self.repo.index.diff(None)],
                "staged": [item.a_path for item in self.repo.index.diff("HEAD")]
            }
            return status
            
        except Exception as e:
            return {"error": [str(e)]}
    
    def auto_commit_conversion(self, converted_files: List[Path], source_file: Path) -> bool:
        """Automatically commit converted files with a descriptive message.
        
        Args:
            converted_files: List of generated HTML files
            source_file: Original Word document path
            
        Returns:
            True if commit was successful
        """
        if not self.init_repository():
            return False
            
        # Add converted files
        if not self.add_files(converted_files):
            return False
            
        # Create commit message
        file_count = len(converted_files)
        message = f"Convert {source_file.name} to {file_count} HTML file{'s' if file_count != 1 else ''}"
        
        return self.commit_changes(message)