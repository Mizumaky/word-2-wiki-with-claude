#!/usr/bin/env python3
"""Interactive launcher for Word2Wiki converter with arrow key navigation"""

import os
import sys
import subprocess
import webbrowser
import time
from pathlib import Path

try:
    import questionary
    from questionary import Style
except ImportError:
    print("Installing required dependencies...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "questionary"])
    import questionary
    from questionary import Style

# Custom style for the menu
custom_style = Style([
    ('question', 'bold'),
    ('answer', 'fg:#44aa44 bold'),
    ('pointer', 'fg:#44aa44 bold'),
    ('highlighted', 'fg:#44aa44 bold'),
    ('selected', 'fg:#cc5454'),
    ('separator', 'fg:#666666'),
    ('instruction', 'fg:#999999'),
    ('text', ''),
    ('disabled', 'fg:#858585 italic')
])

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_status():
    """Get current project status"""
    output_dir = Path("output")
    if not output_dir.exists():
        return "No output directory found", 0
    
    file_count = len(list(output_dir.rglob("*.html")))
    if file_count == 0:
        return "No files converted yet", 0
    else:
        return f"{file_count} HTML files ready", file_count

def show_banner():
    """Display project banner"""
    print("\n" + "="*60)
    print("                    Word2Wiki Converter")
    print("         Convert Word documents to HTML wiki format")
    print("="*60)
    
    status_text, file_count = get_status()
    print(f"Status: {status_text}")
    print()

def browse_documents():
    """Start server and open browser"""
    status_text, file_count = get_status()
    
    if file_count == 0:
        questionary.print("No files to browse!")
        questionary.print("   Convert documents first using 'Convert all documents'")
        questionary.press_any_key_to_continue().ask()
        return
    
    questionary.print("Starting server on http://localhost:8000...")
    questionary.print("   Opening browser...")
    
    server_process = None
    try:
        # Start server in background
        os.chdir("output") 
        server_process = subprocess.Popen(
            [sys.executable, "-m", "http.server", "8000"],
            stdout=subprocess.DEVNULL, 
            stderr=subprocess.DEVNULL
        )
        os.chdir("..")
        time.sleep(2)
        
        # Open browser
        webbrowser.open("http://localhost:8000")
        
        questionary.print("Server started successfully!")
        questionary.print("\nNavigation tips:")
        questionary.print("   • Go to: Hr_Fs_Billing_Accounts_Receivables_Cz/")
        questionary.print("   • Choose version: v00_02 or v00_03_2025_08_21/") 
        questionary.print("   • Open any HTML file to view")
        questionary.print("   • Use 'Show changes' to compare versions")
        
        questionary.press_any_key_to_continue(message="Press any key when done browsing (will stop server)...").ask()
        
    except Exception as e:
        questionary.print(f"Error starting server: {e}")
        questionary.press_any_key_to_continue().ask()
    finally:
        if server_process:
            server_process.terminate()
            questionary.print("Server stopped")
            time.sleep(1)

def convert_all():
    """Convert all documents"""
    questionary.print("Converting all documents...")
    questionary.print("   This may take a few minutes")
    
    try:
        result = subprocess.run([sys.executable, "main.py", "convert-all"], 
                              capture_output=False, text=True, check=False)
        
        if result.returncode == 0:
            questionary.print("Conversion completed successfully!", style="fg:#44aa44 bold")
        else:
            questionary.print(f"Conversion failed (exit code: {result.returncode})", style="fg:#cc5454 bold")
            
    except Exception as e:
        questionary.print(f"Error during conversion: {e}", style="fg:#cc5454 bold")
    
    questionary.press_any_key_to_continue().ask()

def show_status():
    """Show detailed status"""
    questionary.print("Project Status")
    
    try:
        result = subprocess.run([sys.executable, "main.py", "status"], 
                              capture_output=True, text=True, check=False)
        
        if result.returncode == 0:
            print(result.stdout)
        else:
            questionary.print("Failed to get status", style="fg:#cc5454 bold")
            print(result.stderr)
            
    except Exception as e:
        questionary.print(f"Error getting status: {e}", style="fg:#cc5454 bold")
    
    questionary.press_any_key_to_continue().ask()

def clear_files():
    """Clear all converted files"""
    if not questionary.confirm("Are you sure you want to clear all converted files?").ask():
        return
        
    questionary.print("Clearing all files...")
    
    try:
        result = subprocess.run([sys.executable, "main.py", "clear", "--force"],
                              capture_output=False, text=True, check=False)
        
        if result.returncode == 0:
            questionary.print("Files cleared successfully!", style="fg:#44aa44 bold")
        else:
            questionary.print(f"Clear failed (exit code: {result.returncode})", style="fg:#cc5454 bold")
            
    except Exception as e:
        questionary.print(f"Error clearing files: {e}", style="fg:#cc5454 bold")
    
    questionary.press_any_key_to_continue().ask()

def reset_project():
    """Reset project (clear + convert all)"""
    if not questionary.confirm("Reset will clear all files and convert everything. Continue?").ask():
        return
    
    questionary.print("WARNING: If you have the server running, stop it first!")
    questionary.print("   The reset may fail if files are locked by the server.")
    if not questionary.confirm("Continue with reset?").ask():
        return
        
    questionary.print("Resetting project (clear + convert all)...")
    questionary.print("   This may take several minutes")
    
    try:
        # Use echo to auto-confirm the reset
        result = subprocess.run('echo y | python main.py reset', 
                              shell=True, capture_output=True, text=True, check=False)
        
        # Check the actual output for success/failure indicators
        output = result.stdout + result.stderr
        
        if result.returncode == 0 and "Failed to clear" not in output:
            questionary.print("Reset completed successfully!", style="fg:#44aa44 bold")
        elif "Failed to clear" in output:
            questionary.print("Reset failed - files are locked (server running?)", style="fg:#cc5454 bold")
            questionary.print("   Stop the server first, then try reset again")
        else:
            questionary.print(f"Reset failed (exit code: {result.returncode})", style="fg:#cc5454 bold")
            if output.strip():
                questionary.print("Output:")
                print(output[:500])  # Show first 500 chars of output
            
    except Exception as e:
        questionary.print(f"Error during reset: {e}", style="fg:#cc5454 bold")
    
    questionary.press_any_key_to_continue().ask()

def advanced_options():
    """Show advanced options menu"""
    while True:
        clear_screen()
        show_banner()
        
        action = questionary.select(
            "Advanced Options:",
            choices=[
                "Convert specific file",
                "Initialize git repository", 
                "Git commit files",
                "Open command prompt/terminal",
                "Back to main menu"
            ],
            style=custom_style
        ).ask()
        
        if action == "Back to main menu":
            break
        elif action == "Convert specific file":
            convert_specific_file()
        elif action == "Initialize git repository":
            init_git()
        elif action == "Git commit files":
            git_commit()
        elif action == "Open command prompt/terminal":
            open_terminal()

def convert_specific_file():
    """Convert a specific file"""
    source_dir = Path("FS_source")
    if not source_dir.exists():
        questionary.print("❌ No FS_source directory found", style="fg:#cc5454 bold")
        questionary.press_any_key_to_continue().ask()
        return
    
    files = list(source_dir.glob("*.docx"))
    if not files:
        questionary.print("❌ No .docx files found in FS_source/", style="fg:#cc5454 bold")
        questionary.press_any_key_to_continue().ask()
        return
    
    file_choices = [f.name for f in files]
    file_choices.append("Cancel")
    
    selected_file = questionary.select(
        "Select file to convert:",
        choices=file_choices,
        style=custom_style
    ).ask()
    
    if selected_file == "Cancel":
        return
    
    questionary.print(f"🔄 Converting {selected_file}...", style="fg:#44aa44 bold")
    
    try:
        result = subprocess.run([sys.executable, "main.py", "convert", "-f", f"FS_source/{selected_file}"],
                              capture_output=False, text=True, check=False)
        
        if result.returncode == 0:
            questionary.print("✅ Conversion completed!", style="fg:#44aa44 bold")
        else:
            questionary.print(f"❌ Conversion failed (exit code: {result.returncode})", style="fg:#cc5454 bold")
            
    except Exception as e:
        questionary.print(f"❌ Error during conversion: {e}", style="fg:#cc5454 bold")
    
    questionary.press_any_key_to_continue().ask()

def init_git():
    """Initialize git repository"""
    questionary.print("🗂️ Initializing git repository...", style="fg:#44aa44 bold")
    
    try:
        result = subprocess.run([sys.executable, "main.py", "init-git"],
                              capture_output=False, text=True, check=False)
        
        if result.returncode == 0:
            questionary.print("✅ Git repository initialized!", style="fg:#44aa44 bold")
        else:
            questionary.print(f"❌ Git init failed (exit code: {result.returncode})", style="fg:#cc5454 bold")
            
    except Exception as e:
        questionary.print(f"❌ Error initializing git: {e}", style="fg:#cc5454 bold")
    
    questionary.press_any_key_to_continue().ask()

def git_commit():
    """Git commit files"""
    files = questionary.text("Enter files to commit (or 'all' for all files):").ask()
    if not files:
        return
        
    message = questionary.text("Enter commit message:").ask()
    if not message:
        return
    
    questionary.print("💾 Committing to git...", style="fg:#44aa44 bold")
    
    try:
        if files.lower() == "all":
            result = subprocess.run([sys.executable, "main.py", "commit", ".", "-m", message],
                                  capture_output=False, text=True, check=False)
        else:
            result = subprocess.run([sys.executable, "main.py", "commit", files, "-m", message],
                                  capture_output=False, text=True, check=False)
        
        if result.returncode == 0:
            questionary.print("✅ Files committed successfully!", style="fg:#44aa44 bold")
        else:
            questionary.print(f"❌ Commit failed (exit code: {result.returncode})", style="fg:#cc5454 bold")
            
    except Exception as e:
        questionary.print(f"❌ Error committing: {e}", style="fg:#cc5454 bold")
    
    questionary.press_any_key_to_continue().ask()

def open_terminal():
    """Open command prompt/terminal"""
    questionary.print("🧰 Opening terminal...", style="fg:#44aa44 bold")
    
    try:
        if os.name == 'nt':
            os.system("start cmd")
        else:
            os.system("gnome-terminal &")  # Linux
    except Exception as e:
        questionary.print(f"❌ Error opening terminal: {e}", style="fg:#cc5454 bold")
        questionary.press_any_key_to_continue().ask()

def main():
    """Main application loop"""
    # Change to script directory
    os.chdir(Path(__file__).parent)
    
    # Check dependencies
    try:
        import click, pypandoc, rich, bs4
    except ImportError as e:
        questionary.print(f"Missing required dependency: {e}")
        questionary.print("Installing dependencies...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
            questionary.print("Dependencies installed!")
        except Exception as install_error:
            questionary.print(f"Failed to install dependencies: {install_error}")
            questionary.press_any_key_to_continue().ask()
            return
    
    while True:
        clear_screen()
        show_banner()
        
        action = questionary.select(
            "What would you like to do?",
            choices=[
                "Browse documents (start server)",
                "Convert all documents",
                "Show status",
                "Clear all files", 
                "Reset (clear + convert all)",
                "Advanced options",
                "Exit"
            ],
            style=custom_style
        ).ask()
        
        if action == "Exit":
            questionary.print("Goodbye!")
            break
        elif action == "Browse documents (start server)":
            browse_documents()
        elif action == "Convert all documents":
            convert_all()
        elif action == "Show status":
            show_status()
        elif action == "Clear all files":
            clear_files()
        elif action == "Reset (clear + convert all)":
            reset_project()
        elif action == "Advanced options":
            advanced_options()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        questionary.print("\nGoodbye!")
    except Exception as e:
        questionary.print(f"\nUnexpected error: {e}")
        questionary.press_any_key_to_continue().ask()