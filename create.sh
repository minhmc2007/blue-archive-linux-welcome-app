#!/bin/bash
#
# This script configures the Blue Archive Welcome App to autostart
# in both the live environment and for the first login on an installed system.
#
# !! IMPORTANT !!
# This script should be run from the root of your forked project directory
# during your ISO build process. The `BUILD_ROOT` variable should point
# to the temporary filesystem of your ISO (for Arch, this is usually 'airootfs').
#

set -e # Exit immediately if a command fails

# --- Configuration ---
# Your app's name, used for filenames and paths
APP_NAME="blue-archive-linux-welcome-app"

# The path to your ISO's temporary root filesystem
# You might need to change this depending on your build tools (e.g., archiso)
BUILD_ROOT="/Blue-Archive-Linux/blue_archive_linux/airootfs"

# --- Source Files (from your project) ---
SOURCE_DESKTOP_FILE="usr/share/applications/${APP_NAME}.desktop"

# --- Destination Paths (inside the ISO) ---
# For the Live Boot (system-wide autostart)
DEST_LIVE_AUTODIR="${BUILD_ROOT}/etc/xdg/autostart"

# For the Post-Install (skeleton for new users)
DEST_SKEL_AUTODIR="${BUILD_ROOT}/etc/skel/.config/autostart"


# --- Main Logic ---

echo "--- Setting up autostart for Blue Archive Welcome App ---"

# 1. Verify the source file exists
if [ ! -f "$SOURCE_DESKTOP_FILE" ]; then
    echo "ERROR: Source file not found: $SOURCE_DESKTOP_FILE"
    echo "Please run this script from the root of your project directory."
    exit 1
fi

# 2. Set up autostart for the LIVE environment
echo "[1/2] Configuring for Live Boot..."
# Create the destination directory if it doesn't exist
mkdir -p "$DEST_LIVE_AUTODIR"
# Copy the .desktop file
cp -v "$SOURCE_DESKTOP_FILE" "${DEST_LIVE_AUTODIR}/${APP_NAME}.desktop"
echo "Live Boot autostart setup complete."
echo

# 3. Set up autostart for the INSTALLED system
echo "[2/2] Configuring for Post-Installation..."
# Create the destination directory if it doesn't exist
mkdir -p "$DEST_SKEL_AUTODIR"
# Copy the .desktop file
cp -v "$SOURCE_DESKTOP_FILE" "${DEST_SKEL_AUTODIR}/${APP_NAME}.desktop"
echo "Post-install autostart setup complete."
echo

echo "--- Autostart configuration finished successfully! ---"
