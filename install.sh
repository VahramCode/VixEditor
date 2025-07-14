#!/bin/bash

# مسیرهایی که فایل‌ها باید نصب بشن
INSTALL_DIR="/opt/vix"
BIN_DIR="/usr/local/bin"

echo "Starting Vix Editor installation..."

# 1. Create the installation directory
echo "Creating installation directory: $INSTALL_DIR..."
sudo mkdir -p "$INSTALL_DIR" || { echo "Error: Could not create $INSTALL_DIR. Do you have sudo privileges?"; exit 1; }

# 2. Copy core files (vix.py and other resources)
echo "Copying core files to $INSTALL_DIR..."
# Make sure these paths correctly point to files within your 'src' folder in the GitHub repo
sudo cp "./src/vix.py" "$INSTALL_DIR/" || { echo "Error copying vix.py."; exit 1; }
# If you have other files like images, uncomment and add them here:
# sudo cp "./src/your_image.png" "$INSTALL_DIR/"

# 3. Create the executable 'vix' script in a public PATH
echo "Creating 'vix' executable script in $BIN_DIR..."
# This is the content of your original 'vix' bash script
echo '#!/bin/bash' | sudo tee "$BIN_DIR/vix" > /dev/null
echo "python3 $INSTALL_DIR/vix.py \"\$@\"" | sudo tee -a "$BIN_DIR/vix" > /dev/null

# 4. Make the 'vix' script executable
echo "Making 'vix' script executable..."
sudo chmod +x "$BIN_DIR/vix" || { echo "Error setting executable permissions."; exit 1; }

echo "Vix Editor installed successfully!"
echo "You can now run 'vix <filename>' from your terminal."

