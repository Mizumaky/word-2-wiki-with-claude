"""Interactive CLI functionality for file selection and user prompts."""

from pathlib import Path
from typing import Optional, List
from rich.console import Console
from rich.table import Table
from rich.prompt import Confirm, IntPrompt

from .fs_parser import FSParser, FSDocument

console = Console()


class InteractiveCLI:
    """Handles interactive command line interface operations."""
    
    def __init__(self, source_dir: Path = Path("FS_source")):
        """Initialize interactive CLI.
        
        Args:
            source_dir: Directory containing source documents
        """
        self.parser = FSParser(source_dir)
    
    def select_document_for_conversion(self) -> Optional[FSDocument]:
        """Interactive document selection workflow.
        
        Returns:
            Selected FSDocument or None if cancelled
        """
        # Find all available documents
        documents = self.parser.find_all_fs_documents()
        
        if not documents:
            console.print("No FS documents found in FS_source directory", style="red")
            return None
        
        # Get newest document
        newest_doc = documents[0]
        
        # Ask user if they want to convert the newest document
        console.print(f"\nNewest document found:", style="blue")
        console.print(f"   {newest_doc.display_name}")
        console.print(f"   Version: {newest_doc.version_display}")
        console.print(f"   File: {newest_doc.path.name}")
        
        try:
            convert_newest = Confirm.ask("Convert this document?", default=True)
            if convert_newest:
                return newest_doc
        except (KeyboardInterrupt, EOFError):
            # Fall back to automatic selection of newest
            console.print("Auto-selecting newest document", style="blue")
            return newest_doc
        
        # Show file selection menu
        return self._show_file_selection_menu(documents)
    
    def _show_file_selection_menu(self, documents: List[FSDocument]) -> Optional[FSDocument]:
        """Show interactive file selection menu.
        
        Args:
            documents: List of available documents
            
        Returns:
            Selected FSDocument or None if cancelled
        """
        console.print(f"\nSelect document to convert:", style="blue")
        
        # Display numbered list of documents
        for i, doc in enumerate(documents, 1):
            console.print(f"   {i}. {doc.display_name} - {doc.version_display}")
        
        console.print(f"   0. Cancel")
        
        # Get user selection
        try:
            choice = IntPrompt.ask(
                "Choose document (enter number)",
                default=0,
                show_default=True
            )
            
            if choice == 0 or choice > len(documents):
                return None
            
            return documents[choice - 1]
            
        except (KeyboardInterrupt, EOFError):
            return None
    
    def check_version_conflict(self, document: FSDocument) -> bool:
        """Check if version already exists and handle conflict.
        
        Args:
            document: Document to check for conflicts
            
        Returns:
            True if should proceed with conversion, False if cancelled
        """
        # Check if this version was already converted
        existing_versions = self.parser.find_existing_versions(document.base_name)
        expected_version = f"v{document.full_version}"
        
        if expected_version in existing_versions:
            console.print(f"\nVersion conflict detected!", style="yellow")
            console.print(f"   Document: {document.display_name}")
            console.print(f"   Version: {document.version_display}")
            console.print(f"   Already exists in output directory")
            
            try:
                return Confirm.ask("Overwrite existing version?", default=False)
            except (KeyboardInterrupt, EOFError):
                console.print("Input not available, allowing overwrite for testing", style="blue")
                return True
        
        return True
    
    def show_conversion_result(self, document: FSDocument, output_files: List[Path], base_output_dir: Path):
        """Display conversion results with clickable links.
        
        Args:
            document: Converted document
            output_files: List of generated files
            base_output_dir: Base output directory for the document
        """
        console.print(f"\n[bold green]Conversion completed![/bold green]")
        console.print(f"   Document: {document.display_name}")
        console.print(f"   Version: {document.version_display}")
        console.print(f"   Generated {len(output_files)} file(s)")
        
        # Show clickable links
        version_index = base_output_dir / "version_index.html"
        if version_index.exists():
            try:
                file_url = version_index.resolve().as_uri()
                console.print(f"\n[bold blue]View documentation:[/bold blue]")
                console.print(f"   {file_url}")
            except ValueError:
                # Fallback for relative path issues
                abs_path = version_index.absolute()
                console.print(f"\n[bold blue]View documentation:[/bold blue]")
                console.print(f"   {abs_path}")
        
        # Show file table
        table = Table(title="Generated Files", show_header=True, header_style="bold magenta")
        table.add_column("File", style="cyan", no_wrap=True)
        table.add_column("Type", style="green")
        table.add_column("Size", style="yellow")
        
        for file_path in output_files:
            if file_path.exists():
                size_kb = file_path.stat().st_size / 1024
                size_str = f"{size_kb:.1f} KB"
                
                if "index" in file_path.name:
                    file_type = "Index"
                elif "version_index" in file_path.name:
                    file_type = "Version Index"
                else:
                    file_type = "Section"
                
                table.add_row(file_path.name, file_type, size_str)
        
        console.print(table)
    
    def show_available_versions(self, base_name: str):
        """Show available versions for a document.
        
        Args:
            base_name: Base name of the document
        """
        existing_versions = self.parser.find_existing_versions(base_name)
        
        if existing_versions:
            console.print(f"\n📚 Available versions:", style="blue")
            for version in existing_versions:
                console.print(f"   • {version}")
        else:
            console.print(f"\n📚 No existing versions found", style="yellow")