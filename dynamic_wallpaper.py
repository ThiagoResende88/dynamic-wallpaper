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

def set_wallpaper(image_path):
    """Sets the wallpaper using gsettings or feh."""
    if not os.path.exists(image_path):
        print(f"Error: Image not found at {image_path}")
        return

    try:
        # First, try gsettings (for Gnome, Cinnamon, etc.)
        
        # Set picture-uri for light mode
        subprocess.run(['gsettings', 'set', 'org.gnome.desktop.background', 'picture-uri', f'file://{image_path}'], check=True, capture_output=True, text=True)

        # Set picture-uri-dark for dark mode
        subprocess.run(['gsettings', 'set', 'org.gnome.desktop.background', 'picture-uri-dark', f'file://{image_path}'], check=True, capture_output=True, text=True)

        print(f"Wallpaper set to {image_path}")
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        # If gsettings fails, try feh (for i3, bspwm, etc.)
        print("gsettings failed, trying feh...")
        try:
            subprocess.run(['feh', '--bg-fill', image_path], check=True, capture_output=True, text=True)
            print(f"Wallpaper set to {image_path}")
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            print("Error: Could not set wallpaper. Please make sure 'gsettings' or 'feh' is installed.")

def set_theme(theme_name):
    """Saves the selected theme to the config file."""
    theme_path = os.path.join(WALLPAPER_BASE_DIR, theme_name)
    if not os.path.isdir(theme_path):
        print(f"Error: Theme '{theme_name}' not found at {theme_path}")
        return

    with open(THEME_CONFIG_FILE, 'w') as f:
        f.write(theme_name)
    print(f"Theme set to '{theme_name}'")

def get_current_theme():
    """Reads the current theme from the config file."""
    if not os.path.exists(THEME_CONFIG_FILE):
        return None
    with open(THEME_CONFIG_FILE, 'r') as f:
        return f.read().strip()

def main():
    parser = argparse.ArgumentParser(description='Dynamic wallpaper script.')
    parser.add_argument('--theme', type=str, help='Set the wallpaper theme.')
    args = parser.parse_args()

    if args.theme:
        set_theme(args.theme)
        # After setting the theme, also set the wallpaper for the current hour

    current_theme = get_current_theme()
    if not current_theme:
        print("No theme set. Please set a theme with --theme <theme_name>")
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
        print(f"No wallpaper found for hour {hour} in theme '{current_theme}'")

if __name__ == "__main__":
    main()