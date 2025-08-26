"""Command line interface for Word to Wiki converter."""

from pathlib import Path
from typing import Optional
import click
from rich.console import Console
from rich.table import Table
from rich.prompt import IntPrompt, Confirm
import shutil

from .converter import WordToWikiConverter
from .git_manager import GitManager
from .version_converter import VersionAwareConverter
from .interactive_cli import InteractiveCLI
from .fs_parser import FSParser
from .version_utils import version_sort_key

console = Console()


@click.group()
@click.version_option(version="1.0.0")
def cli():
    """Word to Wiki Converter - Convert Word documents to HTML wiki format.
    
    This tool converts Word documents (.docx) to clean HTML5 with:
    • Header-based document splitting (configurable h1/h2 levels)
    • Media extraction and proper referencing  
    • Version management with diff comparison
    • Index generation for navigation
    • Git integration for versioning
    
    Commands:
        convert      Convert Word documents to HTML wiki format
        convert-all  Convert all FS documents in source directory
        status       Show conversion status and available documents  
        browse       Open converted documents in your browser
        clear        Clear output directory (remove all converted files)
        reset        Clear output and convert all documents fresh
        init-git     Initialize git repository for version control
        commit       Commit files to git with custom message
    
    Examples:
        python main.py convert document.docx           # Convert with interactive selection
        python main.py convert -f document.docx        # Convert specific file
        python main.py convert-all                     # Convert all documents  
        python main.py convert-all --skip-existing     # Only convert new documents
        python main.py status                          # Check conversion status
        python main.py browse                          # Open documents in browser
        python main.py clear                           # Remove all converted files
        python main.py reset                           # Clean rebuild everything
        python main.py init-git                        # Initialize git repository
        python main.py commit files -m "Updated docs"  # Commit with message
    """
    pass


@cli.command()
@click.option('--input-file', '-f', type=click.Path(exists=True, path_type=Path), default=None,
              help='Specific input file to convert (skips interactive selection)')
@click.option('--output-dir', '-o', type=click.Path(path_type=Path), default=Path('output'),
              help='Base output directory for converted files')
@click.option('--no-split', is_flag=True, default=False,
              help='Do not split by headers, create single file')
@click.option('--header-level', '-h', type=int, default=1,
              help='Header level to split on (1-6)')
@click.option('--git-commit', is_flag=True, default=False,
              help='Automatically commit converted files to git')
def convert(
    input_file: Optional[Path],
    output_dir: Path,
    no_split: bool,
    header_level: int,
    git_commit: bool
):
    """Convert Word documents to HTML wiki format with version management.
    
    Features:
    • Converts .docx files to clean HTML5 using Pandoc
    • Splits documents by headers (configurable level)
    • Extracts and manages media files
    • Creates version-aware output with diff comparison
    • Generates navigation indexes
    • Optional git integration
    
    If no input file is specified, launches interactive mode to select from FS_source directory.
    Output is organized by document name and version in the specified directory.
    
    Examples:
        python main.py convert                         # Interactive mode
        python main.py convert -f my_document.docx     # Convert specific file
        python main.py convert --no-split             # Don't split by headers
        python main.py convert -h 2                   # Split on h2 instead of h1
        python main.py convert --git-commit           # Auto-commit to git
    """
    try:
        # Initialize interactive CLI
        interactive_cli = InteractiveCLI()
        
        # Select document to convert
        if input_file:
            # Parse the specified file
            parser = FSParser()
            document = parser.parse_filename(input_file.name)
            if not document:
                raise click.ClickException(f"Could not parse FS document: {input_file}")
            # Update path to actual file
            document.path = input_file
        else:
            # Interactive document selection
            document = interactive_cli.select_document_for_conversion()
            if not document:
                console.print("No document selected", style="red")
                return
        
        console.print(f"\nConverting [bold]{document.display_name}[/bold] {document.version_display}", style="blue")
        
        # Check for version conflicts
        if not interactive_cli.check_version_conflict(document):
            console.print("Conversion cancelled", style="yellow")
            return
        
        # Initialize version-aware converter
        converter = VersionAwareConverter(
            base_output_dir=output_dir,
            split_by_headers=not no_split,
            header_level=header_level
        )
        
        # Perform conversion
        output_files = converter.convert_document(document)
        
        # Get document directory for navigation
        doc_dir = output_dir / document.display_name.replace(' ', '_')
        
        # Display results
        interactive_cli.show_conversion_result(document, output_files, doc_dir)
        
        # Git integration
        if git_commit:
            console.print("\nCommitting to git...", style="blue")
            git_manager = GitManager()
            if git_manager.auto_commit_conversion(output_files, document.path):
                console.print("Files committed to git", style="green")
            else:
                console.print("Git commit failed", style="red")
        
    except KeyboardInterrupt:
        console.print("\nConversion cancelled by user", style="yellow")
    except Exception as e:
        console.print(f"\n[bold red]Conversion failed:[/bold red] {e}", style="red")
        raise click.ClickException(str(e))


@cli.command()
@click.option('--output-dir', '-o', type=click.Path(path_type=Path), default=Path('output'),
              help='Directory to watch for files')
def status(output_dir: Path):
    """Show comprehensive status of FS documents and conversion progress.
    
    Displays:
    • Available FS documents in source directory with versions and file sizes
    • Converted documents with version counts and latest versions
    • Git repository status with file counts and recent changes
    
    This command helps you track what documents are available for conversion
    and what has already been converted, along with version control status.
    """
    console.print(f"[bold]Status Report[/bold]", style="blue")
    
    # FS Source directory status
    parser = FSParser()
    documents = parser.find_all_fs_documents()
    
    console.print(f"\n[bold]FS Source Directory[/bold]")
    if documents:
        console.print(f"   Found {len(documents)} FS document(s)")
        
        table = Table(title="Available FS Documents")
        table.add_column("Document", style="cyan")
        table.add_column("Version", style="green")
        table.add_column("Size", style="yellow")
        
        for doc in documents[:5]:  # Show first 5
            size = f"{doc.path.stat().st_size / (1024*1024):.1f} MB"
            table.add_row(doc.display_name, doc.version_display, size)
        
        if len(documents) > 5:
            table.add_row("...", f"({len(documents) - 5} more)", "")
        
        console.print(table)
    else:
        console.print("   No FS documents found")
    
    # Output directory status
    console.print(f"\n[bold]Converted Documents[/bold]")
    if output_dir.exists():
        doc_groups = parser.group_by_base_name()
        converted_docs = []
        
        for base_name in doc_groups:
            doc_dir_name = base_name.replace('_', ' ').title().replace(' ', '_')
            doc_dir = output_dir / doc_dir_name
            if doc_dir.exists():
                versions = [d.name for d in doc_dir.iterdir() if d.is_dir() and d.name.startswith('v')]
                converted_docs.append((doc_dir_name, len(versions)))
        
        if converted_docs:
            table = Table(title="Converted Documents")
            table.add_column("Document", style="cyan")
            table.add_column("Versions", style="green")
            table.add_column("Latest", style="yellow")
            
            for doc_name, version_count in converted_docs:
                doc_dir = output_dir / doc_name
                versions = sorted([d.name for d in doc_dir.iterdir() if d.is_dir() and d.name.startswith('v')], key=version_sort_key, reverse=True)
                latest = versions[0] if versions else "None"
                table.add_row(doc_name.replace('_', ' '), str(version_count), latest)
            
            console.print(table)
        else:
            console.print("   No converted documents found")
    else:
        console.print(f"   Output directory [bold]{output_dir}[/bold] does not exist")
    
    # Git status
    console.print(f"\n[bold]Git Repository Status[/bold]")
    git_manager = GitManager()
    
    if (Path.cwd() / '.git').exists():
        status_info = git_manager.get_status()
        
        if "error" in status_info:
            console.print(f"Git error: {status_info['error'][0]}", style="red")
        else:
            console.print(f"   Untracked files: {len(status_info['untracked'])}")
            console.print(f"   Modified files: {len(status_info['modified'])}")
            console.print(f"   Staged files: {len(status_info['staged'])}")
            
            if status_info['untracked'] or status_info['modified'] or status_info['staged']:
                table = Table(title="Git Status")
                table.add_column("File", style="cyan")
                table.add_column("Status", style="yellow")
                
                for file in status_info['untracked'][:5]:
                    table.add_row(file, "Untracked")
                for file in status_info['modified'][:5]:
                    table.add_row(file, "Modified")
                for file in status_info['staged'][:5]:
                    table.add_row(file, "Staged")
                
                console.print(table)
            else:
                console.print("Working directory clean", style="green")
    else:
        console.print("No git repository found", style="red")
        console.print("   Run 'word2wiki init-git' to initialize a repository")


@cli.command()
@click.option('--output-dir', '-o', type=click.Path(path_type=Path), default=Path('output'),
              help='Output directory to browse')
def browse(output_dir: Path):
    """Browse converted document versions and open them in your web browser.
    
    Features:
    • Interactive selection from available converted documents
    • Shows version count for each document  
    • Opens the document's version index in your default browser
    • Version index provides navigation to all sections and versions
    • Includes diff comparison tools between versions
    
    This is the main way to view and navigate your converted HTML documents.
    """
    console.print("[bold]Browse Converted Documents[/bold]", style="blue")
    
    if not output_dir.exists():
        console.print(f"Output directory [bold]{output_dir}[/bold] does not exist", style="red")
        return
    
    # Find all document directories
    doc_dirs = [d for d in output_dir.iterdir() if d.is_dir()]
    if not doc_dirs:
        console.print("No converted documents found", style="red")
        return
    
    # Create choices for document selection
    choices = []
    for doc_dir in doc_dirs:
        version_index = doc_dir / "version_index.html"
        if version_index.exists():
            doc_name = doc_dir.name.replace('_', ' ')
            versions = [d.name for d in doc_dir.iterdir() if d.is_dir() and d.name.startswith('v')]
            choices.append((f"{doc_name} ({len(versions)} versions)", doc_dir))
    
    if not choices:
        console.print("No valid document indexes found", style="red")
        return
    
    # Interactive selection
    console.print("\nAvailable documents:")
    for i, (doc_name, doc_dir) in enumerate(choices, 1):
        console.print(f"   {i}. {doc_name}")
    
    console.print("   0. Cancel")
    
    try:
        choice = IntPrompt.ask(
            "Select document to browse (enter number)",
            default=0,
            show_default=True
        )
        
        if choice == 0 or choice > len(choices):
            return
            
        selected_dir = choices[choice - 1][1]
    except (KeyboardInterrupt, EOFError):
        return
    version_index = selected_dir / "version_index.html"
    
    if version_index.exists():
        # Start HTTP server for proper diff functionality
        import subprocess
        import threading
        import time
        import webbrowser
        import socket
        
        def find_free_port():
            """Find a free port starting from 8000"""
            for port in range(8000, 8100):
                try:
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                        s.bind(('localhost', port))
                        return port
                except OSError:
                    continue
            return 8000  # fallback
        
        port = find_free_port()
        
        console.print(f"\n[bold blue]Starting HTTP server...[/bold blue]")
        console.print(f"   Port: {port}")
        console.print(f"   Directory: {output_dir.absolute()}")
        
        # Start server in background
        try:
            server_process = subprocess.Popen(
                ["python", "-m", "http.server", str(port)],
                cwd=output_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            
            # Wait a moment for server to start
            time.sleep(2)
            
            # Check if server started successfully
            if server_process.poll() is None:
                relative_path = selected_dir.name + "/version_index.html"
                http_url = f"http://localhost:{port}/{relative_path}"
                
                console.print(f"[bold blue]Opening in browser:[/bold blue]")
                console.print(f"   {http_url}")
                
                webbrowser.open(http_url)
                console.print("Opened in default browser", style="green")
                
                console.print(f"\n[yellow]Server is running...[/yellow]")
                console.print(f"Press [bold]Ctrl+C[/bold] to stop the server")
                
                try:
                    # Keep server running until user stops it
                    server_process.wait()
                except KeyboardInterrupt:
                    console.print(f"\n[yellow]Stopping server...[/yellow]")
                    server_process.terminate()
                    try:
                        server_process.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        server_process.kill()
                    console.print("Server stopped", style="green")
            else:
                console.print("Failed to start HTTP server", style="red")
                
        except Exception as e:
            console.print(f"Error starting server: {e}", style="red")
    else:
        console.print("Version index not found", style="red")


@cli.command()
def init_git():
    """Initialize a git repository for version control of converted documents.
    
    Sets up:
    • New git repository in current directory (if not already present)
    • Appropriate .gitignore for the project
    • Initial configuration for document versioning
    
    This enables automatic version control integration when using --git-commit
    with the convert command, and allows manual commits with the commit command.
    """
    console.print("Initializing git repository...", style="blue")
    
    git_manager = GitManager()
    if git_manager.init_repository():
        console.print("Git repository ready", style="green")
    else:
        console.print("Failed to initialize git repository", style="red")


@cli.command()
@click.argument('files', nargs=-1, type=click.Path(exists=True, path_type=Path))
@click.option('--message', '-m', type=str, required=True,
              help='Commit message')
@click.option('--author-name', type=str, default=None,
              help='Author name for commit')
@click.option('--author-email', type=str, default=None,
              help='Author email for commit')
def commit(files, message: str, author_name: Optional[str], author_email: Optional[str]):
    """Commit specified files to git with a custom commit message.
    
    Usage:
    • Specify one or more files or directories to commit
    • Provide a descriptive commit message with -m
    • Optionally set custom author name and email
    • Files are automatically staged before committing
    
    Examples:
        python main.py commit output/ -m "Added new document conversion"
        python main.py commit file1.html file2.html -m "Updated documentation"
        python main.py commit . -m "Complete project update" --author-name "John Doe"
    """
    if not files:
        console.print("No files specified", style="red")
        return
    
    console.print(f"Committing {len(files)} file(s)...", style="blue")
    
    git_manager = GitManager()
    file_paths = [Path(f) for f in files]
    
    if git_manager.add_files(file_paths):
        if git_manager.commit_changes(message, author_name, author_email):
            console.print("Files committed successfully", style="green")
        else:
            console.print("Commit failed", style="red")
    else:
        console.print("Failed to add files", style="red")


@cli.command()
@click.option('--output-dir', '-o', type=click.Path(path_type=Path), default=Path('output'),
              help='Output directory to clear')
@click.option('--force', '-f', is_flag=True, default=False,
              help='Force deletion without confirmation prompt')
def clear(output_dir: Path, force: bool):
    """Clear the output directory by removing all converted files.
    
    WARNING: This permanently deletes all converted HTML files, indexes, and media!
    
    Features:
    • Removes entire output directory and all contents
    • Interactive confirmation prompt (unless --force is used)
    • Preserves source documents (only removes converted output)
    • Useful for clean rebuilds or testing
    
    Examples:
        python main.py clear                    # Interactive confirmation
        python main.py clear --force           # Skip confirmation
        python main.py clear -o custom_output  # Clear specific directory
    """
    if not output_dir.exists():
        console.print(f"Output directory [bold]{output_dir}[/bold] does not exist", style="yellow")
        return
    
    # Count items to be deleted
    total_items = sum(1 for _ in output_dir.rglob('*'))
    
    console.print(f"\n[bold red]WARNING:[/bold red] This will permanently delete:")
    console.print(f"   Directory: [bold]{output_dir.absolute()}[/bold]")
    console.print(f"   Total items: [bold]{total_items}[/bold] files and folders")
    
    if not force:
        if not Confirm.ask("\n[bold yellow]Are you sure you want to proceed?[/bold yellow]", default=False):
            console.print("Clear operation cancelled", style="yellow")
            return
    
    try:
        console.print(f"\nRemoving [bold]{output_dir}[/bold]...", style="blue")
        shutil.rmtree(output_dir)
        console.print("Output directory cleared successfully", style="green")
        
    except Exception as e:
        console.print(f"Failed to clear output directory: {e}", style="red")


@cli.command()
@click.option('--output-dir', '-o', type=click.Path(path_type=Path), default=Path('output'),
              help='Base output directory for converted files')
@click.option('--no-split', is_flag=True, default=False,
              help='Do not split by headers, create single files')
@click.option('--header-level', '-h', type=int, default=1,
              help='Header level to split on (1-6)')
@click.option('--git-commit', is_flag=True, default=False,
              help='Automatically commit converted files to git')
@click.option('--skip-existing', is_flag=True, default=False,
              help='Skip documents that already have converted versions')
def convert_all(
    output_dir: Path,
    no_split: bool,
    header_level: int,
    git_commit: bool,
    skip_existing: bool
):
    """Convert all FS documents found in the source directory.
    
    Features:
    • Automatically finds and converts all .docx files in FS_source/
    • Batch processing with progress tracking
    • Same conversion options as single convert command
    • Optional skip of already converted documents
    • Summary report of successful and failed conversions
    
    This is ideal for:
    • Initial bulk conversion of document repositories
    • Regular batch updates of multiple documents
    • Automated conversion workflows
    
    Examples:
        python main.py convert-all                    # Convert all documents
        python main.py convert-all --no-split        # Single file outputs
        python main.py convert-all --skip-existing   # Only new documents
        python main.py convert-all --git-commit      # Auto-commit all
    """
    console.print("[bold]Converting All FS Documents[/bold]", style="blue")
    
    # Find all documents
    parser = FSParser()
    documents = parser.find_all_fs_documents()
    
    if not documents:
        console.print("No FS documents found in source directory", style="yellow")
        return
    
    console.print(f"Found [bold]{len(documents)}[/bold] FS document(s)")
    
    # Filter out existing if requested
    if skip_existing:
        docs_to_convert = []
        for doc in documents:
            existing_versions = parser.find_existing_versions(doc.base_name)
            if not existing_versions or f"v{doc.full_version}" not in existing_versions:
                docs_to_convert.append(doc)
            else:
                console.print(f"   Skipping [dim]{doc.display_name}[/dim] (already converted)", style="yellow")
        documents = docs_to_convert
    
    if not documents:
        console.print("No documents to convert (all already exist)", style="yellow")
        return
    
    console.print(f"Converting [bold]{len(documents)}[/bold] document(s)...\n")
    
    # Initialize converter
    converter = VersionAwareConverter(
        base_output_dir=output_dir,
        split_by_headers=not no_split,
        header_level=header_level
    )
    
    # Track results
    successful = []
    failed = []
    all_output_files = []
    
    # Convert each document
    for i, document in enumerate(documents, 1):
        try:
            console.print(f"\n[{i}/{len(documents)}] Converting [bold]{document.display_name}[/bold] {document.version_display}", style="blue")
            
            output_files = converter.convert_document(document)
            successful.append(document)
            all_output_files.extend(output_files)
            
        except Exception as e:
            console.print(f"   [bold red]Failed:[/bold red] {e}", style="red")
            failed.append((document, str(e)))
    
    # Show summary
    console.print(f"\n[bold]Conversion Summary[/bold]", style="blue")
    console.print(f"   Successful: [bold green]{len(successful)}[/bold green]")
    console.print(f"   Failed: [bold red]{len(failed)}[/bold red]")
    console.print(f"   Total files created: [bold]{len(all_output_files)}[/bold]")
    
    if failed:
        console.print(f"\n[bold red]Failed Conversions:[/bold red]")
        for doc, error in failed:
            console.print(f"   • {doc.display_name}: {error}")
    
    # Git integration
    if git_commit and successful:
        console.print(f"\nCommitting {len(all_output_files)} files to git...", style="blue")
        git_manager = GitManager()
        if git_manager.auto_commit_conversion(all_output_files, Path("batch_conversion")):
            console.print("All files committed to git", style="green")
        else:
            console.print("Git commit failed", style="red")


@cli.command()
@click.option('--output-dir', '-o', type=click.Path(path_type=Path), default=Path('output'),
              help='Base output directory for converted files')
@click.option('--no-split', is_flag=True, default=False,
              help='Do not split by headers, create single files')
@click.option('--header-level', '-h', type=int, default=1,
              help='Header level to split on (1-6)')
@click.option('--git-commit', is_flag=True, default=False,
              help='Automatically commit converted files to git')
@click.option('--force', '-f', is_flag=True, default=False,
              help='Force clear without confirmation prompt')
def reset(
    output_dir: Path,
    no_split: bool,
    header_level: int,
    git_commit: bool,
    force: bool
):
    """Reset by clearing output directory and converting all documents fresh.
    
    This is a convenience command that combines:
    1. clear --force (removes all existing converted files)
    2. convert-all (converts all source documents)
    
    Features:
    • Complete clean slate - removes all previous conversions
    • Batch converts all documents with fresh versions
    • Same conversion options as convert-all
    • Optional confirmation prompt (unless --force)
    • Ideal for complete rebuilds
    
    Use cases:
    • Testing conversion changes across all documents
    • Clean rebuild after configuration changes
    • Resolving conversion conflicts or corrupted output
    
    Examples:
        python main.py reset                     # Interactive confirmation + convert all
        python main.py reset --force           # Skip confirmation
        python main.py reset --no-split       # Clean rebuild with single files
    """
    console.print("[bold]Reset: Clear and Convert All[/bold]", style="blue")
    
    # Step 1: Clear existing output
    if output_dir.exists():
        total_items = sum(1 for _ in output_dir.rglob('*'))
        
        console.print(f"\n[bold]Step 1: Clear Output Directory[/bold]")
        console.print(f"   Directory: [bold]{output_dir.absolute()}[/bold]")
        console.print(f"   Total items: [bold]{total_items}[/bold] files and folders")
        
        if not force:
            if not Confirm.ask("\n[bold yellow]Clear existing output and rebuild everything?[/bold yellow]", default=False):
                console.print("Reset operation cancelled", style="yellow")
                return
        
        try:
            console.print(f"Removing [bold]{output_dir}[/bold]...", style="blue")
            shutil.rmtree(output_dir)
            console.print("Output directory cleared", style="green")
        except Exception as e:
            console.print(f"Failed to clear output directory: {e}", style="red")
            return
    else:
        console.print(f"\n[bold]Step 1: Clear Output Directory[/bold]")
        console.print("   Output directory does not exist - skipping clear")
    
    # Step 2: Convert all documents
    console.print(f"\n[bold]Step 2: Convert All Documents[/bold]")
    
    # Find all documents
    parser = FSParser()
    documents = parser.find_all_fs_documents()
    
    if not documents:
        console.print("No FS documents found in source directory", style="yellow")
        return
    
    console.print(f"Found [bold]{len(documents)}[/bold] FS document(s) to convert")
    
    # Initialize converter
    converter = VersionAwareConverter(
        base_output_dir=output_dir,
        split_by_headers=not no_split,
        header_level=header_level
    )
    
    # Track results
    successful = []
    failed = []
    all_output_files = []
    
    # Convert each document
    for i, document in enumerate(documents, 1):
        try:
            console.print(f"\n[{i}/{len(documents)}] Converting [bold]{document.display_name}[/bold] {document.version_display}", style="blue")
            
            output_files = converter.convert_document(document)
            successful.append(document)
            all_output_files.extend(output_files)
            
        except Exception as e:
            console.print(f"   [bold red]Failed:[/bold red] {e}", style="red")
            failed.append((document, str(e)))
    
    # Show final summary
    console.print(f"\n[bold]Reset Complete - Final Summary[/bold]", style="blue")
    console.print(f"   Documents converted: [bold green]{len(successful)}[/bold green]")
    console.print(f"   Conversion failures: [bold red]{len(failed)}[/bold red]")
    console.print(f"   Total files created: [bold]{len(all_output_files)}[/bold]")
    
    if failed:
        console.print(f"\n[bold red]Failed Conversions:[/bold red]")
        for doc, error in failed:
            console.print(f"   • {doc.display_name}: {error}")
    
    # Git integration
    if git_commit and successful:
        console.print(f"\nCommitting {len(all_output_files)} files to git...", style="blue")
        git_manager = GitManager()
        if git_manager.auto_commit_conversion(all_output_files, Path("reset_conversion")):
            console.print("All files committed to git", style="green")
        else:
            console.print("Git commit failed", style="red")


if __name__ == '__main__':
    cli()