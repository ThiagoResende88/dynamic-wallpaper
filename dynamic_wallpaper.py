import os
import argparse
import subprocess
import datetime

# --- Configuration ---
# The base directory where your theme folders are located.
# This is now relative to the script's location.
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
WALLPAPER_BASE_DIR = os.path.join(SCRIPT_DIR, 'images')

# The location of the configuration file to store the current theme.
THEME_CONFIG_FILE = os.path.expanduser('~/.dwall_theme')
# -------------------

# Log file for debugging
LOG_FILE = os.path.expanduser('~/.wallpaper_debug.log')

def log_message(message):
    """Appends a timestamped message to the debug log file."""
    with open(LOG_FILE, 'a') as f:
        f.write(f"{datetime.datetime.now()}: {message}\n")

def set_wallpaper(image_path):
    """Sets the wallpaper using gsettings or feh."""
    if not os.path.exists(image_path):
        log_message(f"Error: Image not found at {image_path}")
        return

    try:
        # First, try gsettings (for Gnome, Cinnamon, etc.)
        log_message(f"Attempting to set wallpaper with gsettings: {image_path}")
        
        # Set picture-uri for light mode
        result_light = subprocess.run(['gsettings', 'set', 'org.gnome.desktop.background', 'picture-uri', f'file://{image_path}'], check=True, capture_output=True, text=True)
        log_message(f"gsettings (light mode) stdout: {result_light.stdout.strip()}")
        log_message(f"gsettings (light mode) stderr: {result_light.stderr.strip()}")

        # Set picture-uri-dark for dark mode
        result_dark = subprocess.run(['gsettings', 'set', 'org.gnome.desktop.background', 'picture-uri-dark', f'file://{image_path}'], check=True, capture_output=True, text=True)
        log_message(f"gsettings (dark mode) stdout: {result_dark.stdout.strip()}")
        log_message(f"gsettings (dark mode) stderr: {result_dark.stderr.strip()}")

        log_message(f"Wallpaper set to {image_path} using gsettings.")
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        log_message(f"gsettings failed: {e}")
        log_message("gsettings failed, trying feh...")
        try:
            result_feh = subprocess.run(['feh', '--bg-fill', image_path], check=True, capture_output=True, text=True)
            log_message(f"feh stdout: {result_feh.stdout.strip()}")
            log_message(f"feh stderr: {result_feh.stderr.strip()}")
            log_message(f"Wallpaper set to {image_path} using feh.")
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            log_message(f"feh failed: {e}")
            log_message("Error: Could not set wallpaper. Please make sure 'gsettings' or 'feh' is installed.")

def set_theme(theme_name):
    """Saves the selected theme to the config file."""
    theme_path = os.path.join(WALLPAPER_BASE_DIR, theme_name)
    if not os.path.isdir(theme_path):
        log_message(f"Error: Theme '{theme_name}' not found at {theme_path}")
        return

    with open(THEME_CONFIG_FILE, 'w') as f:
        f.write(theme_name)
    log_message(f"Theme set to '{theme_name}'")

def get_current_theme():
    """Reads the current theme from the config file."""
    if not os.path.exists(THEME_CONFIG_FILE):
        return None
    with open(THEME_CONFIG_FILE, 'r') as f:
        return f.read().strip()

def main():

    # Configurar environment variables para funcionar no cron
    os.environ['DISPLAY'] = ':0'
    os.environ['DBUS_SESSION_BUS_ADDRESS'] = f"unix:path=/run/user/{os.getuid()}/bus"
    os.environ['XAUTHORITY'] = os.path.expanduser('~/.Xauthority')
    
    # Log para debug
    log_message("Script executado")
        
    parser = argparse.ArgumentParser(description='Dynamic wallpaper script.')
    parser.add_argument('--theme', type=str, help='Set the wallpaper theme.')
    args = parser.parse_args()

    if args.theme:
        set_theme(args.theme)
        # After setting the theme, also set the wallpaper for the current hour

    current_theme = get_current_theme()
    if not current_theme:
        log_message("No theme set. Please set a theme with --theme <theme_name>")
        return

    now = datetime.datetime.now()
    hour = now.hour

    # Assumes images are named 0.jpg, 1.png, etc.
    # It will try to find both .jpg and .png extensions.
    image_name_jpg = f"{hour}.jpg"
    image_name_png = f"{hour}.png"
    
    image_path_jpg = os.path.join(WALLPAPER_BASE_DIR, current_theme, image_name_jpg)
    image_path_png = os.path.join(WALLPAPER_BASE_DIR, current_theme, image_name_png)

    if os.path.exists(image_path_jpg):
        set_wallpaper(image_path_jpg)
    elif os.path.exists(image_path_png):
        set_wallpaper(image_path_png)
    else:
        log_message(f"No wallpaper found for hour {hour} in theme '{current_theme}'")

if __name__ == "__main__":
    main()
